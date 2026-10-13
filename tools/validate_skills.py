"""Structural validation for the Cognition Today deep cognitive skills.

Checks the mechanically verifiable subset of the global acceptance gates in
Section 13 of the master implementation specification. Behavioural gates -- does
the metacognition skill actually change the object-level task, does the
creativity skill produce structural variation -- cannot be checked here. They
belong to the evaluation set under evals/.

Run from anywhere:

    python tools/validate_skills.py

Exits 0 when every check passes, 1 when any check fails. Warnings do not fail
the run. PyYAML is used when available and skipped with a warning when not.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
EVALS_ROOT = REPO_ROOT / "evals"

MAX_SKILL_LINES = 500
TOC_REQUIRED_ABOVE_LINES = 100

ALLOWED_FRONTMATTER_KEYS = {"name", "description"}

REQUIRED_SKILL_FILES = ["SKILL.md", "LICENSE.txt", "agents/openai.yaml"]

REQUIRED_REFERENCES = {
    "monitor-and-regulate-thinking": [
        "metacognition-model.md",
        "metamemory-model.md",
        "source-notes.md",
        "source-map.md",
        "source-graph.yaml",
        "examples.md",
    ],
    "create-through-recomposition": [
        "decompose-recompose-model.md",
        "creative-operator-matrix.md",
        "construal-distance-model.md",
        "source-notes.md",
        "source-map.md",
        "source-graph.yaml",
        "examples.md",
    ],
    "manage-working-context": [
        "state-model.md",
        "capsule-contract.md",
        "compaction-and-recovery.md",
        "source-notes.md",
        "source-map.md",
        "source-graph.yaml",
        "examples.md",
    ],
}

# Three provenance layers, because three different parties authored the rules.
# source-grounded  : the mechanism comes from a cited Cognition Today article.
# author-specified : Aditya Shukla specified it directly in the master
#                    implementation specification. No article claims it, but it
#                    is not the compiler's invention either, and change control
#                    applies.
# design-inference : the compiler's engineering decision. No authority. Freely
#                    revisable on engineering grounds.
VALID_LAYERS = {"source-grounded", "author-specified", "design-inference"}
UNSOURCED_LAYERS = {"author-specified", "design-inference"}

# Section 4: keep the runtime packages clean. Launch and public-relations files
# belong at the repository root, not inside an installable skill.
FORBIDDEN_SKILL_FILENAMES = {
    "README.md",
    "CHANGELOG.md",
    "INSTALL.md",
    "QUICKSTART.md",
    "QUICK-REFERENCE.md",
    "CONTRIBUTING.md",
}

# Section 14: nothing ships publicly while one of these is still in a
# publishable artifact. Governance documents are exempt because they have to be
# able to name the tokens in order to define the rule.
PUBLICATION_BLOCKERS = ["<DONATION_URL>", "TODO", "TBD", "FIXME", "XXX", "PLACEHOLDER"]

BLOCKER_SCAN_ROOTS = ["skills", "evals", "benchmarks", "README.md", "CITATION.cff"]

REQUIRED_ATTRIBUTION = [
    "Cognition Today",
    "Aditya Shukla",
    "https://cognitiontoday.com",
    "https://buymeacoffee.com/adityashukla",
]

WARRANTY_SENTINEL = "This skill is provided without warranty."

# Shared by every package. Domain skills point at the runtime for the full
# contract instead of restating the capsule schema, so those phrases live only
# in manage-working-context.
RUNTIME_CONTRACT_SENTINELS = [
    "## Cognition Today cognitive-runtime coordination",
    "Do not search unrelated filesystem locations.",
]
RUNTIME_CANONICAL_SENTINELS = [
    "pass a source-intent capsule containing",
    "without pretending that persistent memory exists",
]
DOMAIN_RUNTIME_POINTER_SENTINELS = [
    "source-intent capsule",
    "nothing is being persisted",
]

SOURCE_MAP_REQUIRED_FIELDS = [
    "operation_id",
    "layer",
    "source_id",
    "source_claim",
    "design_inference",
    "agent_rule",
    "validation_status",
]

# Section 3: human constructs may not be asserted of the software itself.
# Matches only first-person or agent-subject assertions, so that describing human
# cognition does not trip the check. Lines that state the prohibition rather than
# commit it are filtered out by NEGATION_MARKERS below.
LITERAL_COGNITION_PATTERNS = [
    r"\b(?:I|the agent|this skill)\s+(?:have|has|feel|feels|experience|experiences)\s+"
    r"(?:human\s+)?(?:metacognition|metamemory|working memory|epistemic feelings|consciousness)\b",
    r"\b(?:I|the agent)\s+(?:activate|activates|engage|engages)\s+(?:my|its|the)\s+"
    r"(?:default[- ]mode|central[- ]executive)\b",
]

NEGATION_MARKERS = [
    "do not",
    "don't",
    "never",
    "must not",
    "cannot",
    "prohibit",
    "forbidden",
    "avoid",
    "not a claim",
    "does not",
]


@dataclass
class Report:
    """Collects failures and warnings across every check."""

    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks_run: int = 0

    def check(self, condition: bool, message: str) -> bool:
        self.checks_run += 1
        if not condition:
            self.failures.append(message)
        return condition

    def warn(self, condition: bool, message: str) -> None:
        if not condition:
            self.warnings.append(message)

    @property
    def passed(self) -> bool:
        return not self.failures


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Split a SKILL.md into its YAML frontmatter mapping and its body.

    Parsed by hand so the validator has no hard dependency on PyYAML. The
    specification allows only two scalar keys, so a full parser is unnecessary.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    block, body = text[4:end], text[end + 5 :]

    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            current_key = match.group(1)
            fields[current_key] = match.group(2).strip()
        elif current_key and line.startswith((" ", "\t")):
            fields[current_key] += " " + line.strip()
    return fields, body


def validate_frontmatter(skill_dir: Path, fields: dict[str, str], report: Report) -> None:
    name = skill_dir.name

    report.check(bool(fields), f"{name}: SKILL.md has no YAML frontmatter")
    report.check(
        set(fields) <= ALLOWED_FRONTMATTER_KEYS,
        f"{name}: frontmatter may contain only name and description, found {sorted(fields)}",
    )
    report.check(
        "name" in fields and "description" in fields,
        f"{name}: frontmatter must contain both name and description",
    )
    report.check(
        fields.get("name") == name,
        f"{name}: frontmatter name '{fields.get('name')}' does not match the folder name",
    )

    description = fields.get("description", "")
    report.check(
        "Use for" in description or "Use when" in description,
        f"{name}: description states no positive activation boundary",
    )
    report.check(
        "Do not use" in description,
        f"{name}: description states no negative activation boundary",
    )
    report.warn(
        len(description) <= 1024,
        f"{name}: description is {len(description)} characters; some clients truncate long descriptions",
    )


def validate_skill_body(skill_dir: Path, text: str, body: str, report: Report) -> None:
    name = skill_dir.name
    line_count = len(text.splitlines())

    report.check(
        line_count < MAX_SKILL_LINES,
        f"{name}: SKILL.md is {line_count} lines, limit is {MAX_SKILL_LINES}",
    )

    for sentinel in RUNTIME_CONTRACT_SENTINELS:
        report.check(
            sentinel in body,
            f"{name}: runtime coordination block is missing or altered, expected to contain '{sentinel}'",
        )
    extra = (
        RUNTIME_CANONICAL_SENTINELS
        if name == "manage-working-context"
        else DOMAIN_RUNTIME_POINTER_SENTINELS
    )
    for sentinel in extra:
        report.check(
            sentinel in body,
            f"{name}: runtime coordination block is missing or altered, expected to contain '{sentinel}'",
        )

    for item in REQUIRED_ATTRIBUTION:
        report.check(item in body, f"{name}: attribution block is missing '{item}'")

    report.check(
        WARRANTY_SENTINEL in body,
        f"{name}: warranty and safety disclaimer is missing",
    )
    report.check(
        "CC BY-NC-SA 4.0" in body,
        f"{name}: license label is missing from SKILL.md",
    )
    report.check(
        "Retain this attribution" in body,
        f"{name}: redistribution instruction is missing from the attribution block",
    )


def validate_reference_links(skill_dir: Path, body: str, report: Report) -> None:
    """Every `references/...` path named in SKILL.md must exist on disk."""
    name = skill_dir.name
    for target in sorted(set(re.findall(r"`(references/[A-Za-z0-9._/-]+)`", body))):
        report.check(
            (skill_dir / target).exists(),
            f"{name}: SKILL.md points at '{target}', which does not exist",
        )


def validate_required_files(skill_dir: Path, report: Report) -> None:
    name = skill_dir.name

    for relative in REQUIRED_SKILL_FILES:
        report.check((skill_dir / relative).exists(), f"{name}: missing required file {relative}")

    for reference in REQUIRED_REFERENCES.get(name, []):
        report.check(
            (skill_dir / "references" / reference).exists(),
            f"{name}: missing required reference references/{reference}",
        )

    for path in skill_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.name in FORBIDDEN_SKILL_FILENAMES:
            report.failures.append(
                f"{name}: {path.relative_to(skill_dir)} does not belong inside a skill package"
            )
        depth = len(path.relative_to(skill_dir).parts)
        report.check(
            depth <= 2,
            f"{name}: {path.relative_to(skill_dir)} is nested more than one level below SKILL.md",
        )


def validate_reference_tocs(skill_dir: Path, report: Report) -> None:
    """Section 10.3: a reference longer than 100 lines needs a table of contents."""
    name = skill_dir.name
    references = skill_dir / "references"
    if not references.exists():
        return
    for path in sorted(references.glob("*.md")):
        line_count = len(read(path).splitlines())
        if line_count > TOC_REQUIRED_ABOVE_LINES:
            report.check(
                "## Contents" in read(path),
                f"{name}: references/{path.name} is {line_count} lines and needs a table of contents",
            )


def validate_source_map(skill_dir: Path, report: Report) -> None:
    """Every record must carry the full provenance schema and a known layer."""
    name = skill_dir.name
    path = skill_dir / "references" / "source-map.md"
    if not path.exists():
        return

    text = read(path)
    # Only the blocks under "## Records" are real records. The block above it
    # documents the schema and uses placeholder values on purpose.
    _, _, records_section = text.partition("\n## Records\n")
    report.check(bool(records_section), f"{name}: source-map.md has no '## Records' section")

    blocks = re.findall(r"```yaml\n(.*?)```", records_section, re.DOTALL)
    record_blocks = [block for block in blocks if block.lstrip().startswith("- operation_id:")]
    report.check(bool(record_blocks), f"{name}: source-map.md contains no operation records")

    if yaml is None:
        report.warnings.append(f"{name}: PyYAML not installed, source-map records parsed by pattern only")

    for block in record_blocks:
        records = None
        if yaml is not None:
            try:
                records = yaml.safe_load(block)
            except yaml.YAMLError as error:
                report.failures.append(f"{name}: source-map.md YAML does not parse: {error}")
                continue

        if records is None:
            operation_ids = re.findall(r"- operation_id:\s*(\S+)", block)
            report.check(bool(operation_ids), f"{name}: source-map.md block has no operation_id")
            continue

        for record in records:
            operation_id = record.get("operation_id", "<unnamed>")
            for required in SOURCE_MAP_REQUIRED_FIELDS:
                report.check(
                    required in record,
                    f"{name}: source-map record '{operation_id}' is missing field '{required}'",
                )
            layer = record.get("layer")
            report.check(
                layer in VALID_LAYERS,
                f"{name}: source-map record '{operation_id}' has unknown layer '{layer}'",
            )
            if layer == "source-grounded":
                report.check(
                    str(record.get("source_id", "")).startswith("https://cognitiontoday.com/"),
                    f"{name}: source-grounded record '{operation_id}' lacks a Cognition Today source URL",
                )
            if layer in UNSOURCED_LAYERS:
                report.check(
                    record.get("source_claim") == "none",
                    f"{name}: {layer} record '{operation_id}' must set source_claim to none",
                )
            if layer == "author-specified":
                report.check(
                    str(record.get("source_id", "")).startswith("master-specification#"),
                    f"{name}: author-specified record '{operation_id}' must cite the "
                    f"specification section as master-specification#<section>",
                )
            if layer == "design-inference":
                report.check(
                    record.get("source_id") == "none",
                    f"{name}: design-inference record '{operation_id}' must set source_id to none",
                )
            report.check(
                bool(record.get("validation_status")),
                f"{name}: source-map record '{operation_id}' has no validation_status",
            )


def validate_yaml_files(root: Path, report: Report) -> None:
    if yaml is None:
        report.warnings.append("PyYAML not installed, YAML syntax checks skipped")
        return
    for path in sorted(root.rglob("*.yaml")):
        try:
            yaml.safe_load(read(path))
        except yaml.YAMLError as error:
            report.failures.append(f"{path.relative_to(REPO_ROOT)}: YAML does not parse: {error}")
        else:
            report.checks_run += 1


def validate_no_blockers(root: Path, report: Report) -> None:
    """Unresolved placeholders in a publishable artifact block publication."""
    candidates: list[Path] = []
    for entry in BLOCKER_SCAN_ROOTS:
        target = root / entry
        if target.is_dir():
            candidates.extend(target.rglob("*"))
        elif target.is_file():
            candidates.append(target)

    for path in sorted(candidates):
        # LICENSE.txt is verbatim third-party legal text and is never edited here.
        if not path.is_file() or path.suffix.lower() == ".txt":
            continue
        text = read(path)
        for blocker in PUBLICATION_BLOCKERS:
            report.check(
                blocker not in text,
                f"{path.relative_to(REPO_ROOT)}: unresolved publication blocker '{blocker}'",
            )


def validate_no_literal_cognition_claims(root: Path, report: Report) -> None:
    """Flag agent-subject cognition claims, but not lines that prohibit them."""
    for path in sorted(root.rglob("*.md")):
        for number, line in enumerate(read(path).splitlines(), start=1):
            lowered = line.lower()
            if any(marker in lowered for marker in NEGATION_MARKERS):
                continue
            for pattern in LITERAL_COGNITION_PATTERNS:
                match = re.search(pattern, line, re.IGNORECASE)
                report.check(
                    match is None,
                    f"{path.relative_to(REPO_ROOT)} line {number}: "
                    f"asserts human cognition of the agent: '{match.group(0) if match else ''}'",
                )


def validate_evals(report: Report) -> None:
    """Prompt files must be valid JSONL, and their counts must match the manifest."""
    if not EVALS_ROOT.exists():
        report.warnings.append("evals/ not present, evaluation checks skipped")
        return

    counts: dict[str, int] = {}
    seen_ids: set[str] = set()

    for path in sorted((EVALS_ROOT / "prompts").glob("*.jsonl")):
        records = []
        for number, line in enumerate(read(path).splitlines(), start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                report.failures.append(f"{path.name} line {number}: invalid JSON: {error}")
        counts[path.stem] = len(records)

        for record in records:
            for required in ("id", "skill", "class", "prompt", "expect"):
                report.check(
                    required in record,
                    f"{path.name}: record {record.get('id', '<unnamed>')} is missing '{required}'",
                )
            identifier = record.get("id")
            report.check(identifier not in seen_ids, f"{path.name}: duplicate prompt id '{identifier}'")
            seen_ids.add(identifier)

    manifest_path = EVALS_ROOT / "manifest.yaml"
    if yaml is not None and manifest_path.exists():
        manifest = yaml.safe_load(read(manifest_path))
        for entry in manifest.get("prompt_sets", []):
            declared, actual = entry.get("total"), counts.get(entry.get("id"))
            report.check(
                declared == actual,
                f"evals/manifest.yaml: set '{entry.get('id')}' declares {declared} prompts, file has {actual}",
            )

    run_manifest = REPO_ROOT / "benchmarks" / "run-manifest.json"
    if run_manifest.exists():
        try:
            json.loads(read(run_manifest))
            report.checks_run += 1
        except json.JSONDecodeError as error:
            report.failures.append(f"benchmarks/run-manifest.json: invalid JSON: {error}")


def validate_skill(skill_dir: Path, report: Report) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        report.failures.append(f"{skill_dir.name}: SKILL.md is missing")
        return

    text = read(skill_file)
    fields, body = parse_frontmatter(text)

    validate_frontmatter(skill_dir, fields, report)
    validate_skill_body(skill_dir, text, body, report)
    validate_reference_links(skill_dir, body, report)
    validate_required_files(skill_dir, report)
    validate_reference_tocs(skill_dir, report)
    validate_source_map(skill_dir, report)


def main() -> int:
    report = Report()

    if not SKILLS_ROOT.exists():
        print(f"FAIL  no skills directory at {SKILLS_ROOT}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    report.check(bool(skill_dirs), "skills/ contains no skill packages")

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, report)

    validate_yaml_files(REPO_ROOT, report)
    validate_no_blockers(REPO_ROOT, report)
    validate_no_literal_cognition_claims(REPO_ROOT, report)
    validate_evals(report)

    print(f"Validated {len(skill_dirs)} skill package(s) across {report.checks_run} checks.\n")

    for warning in report.warnings:
        print(f"WARN  {warning}")
    for failure in report.failures:
        print(f"FAIL  {failure}")

    if report.passed:
        print(f"\nPASS  {report.checks_run} checks, {len(report.warnings)} warning(s).")
        return 0

    print(f"\nFAIL  {len(report.failures)} failure(s), {len(report.warnings)} warning(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
