# Build report

Generated from *Cognition Today Deep Cognitive Skills: Master Implementation Specification*, version 1.1-draft, dated 2026-08-03.

Section 10.2 step 13 requires that every design deviation be recorded and approved before publication. This is that record. Section 10.1 instructs the builder to report deviations rather than silently repair the specification, so nothing below was resolved unilaterally.

## Contents

1. [What was built](#what-was-built)
2. [Deviations from the specification](#deviations-from-the-specification)
3. [Things the specification expected that are absent](#things-the-specification-expected-that-are-absent)
4. [Global acceptance gate status](#global-acceptance-gate-status)
5. [Publication blockers](#publication-blockers)
6. [Decisions needed from Aditya Shukla](#decisions-needed-from-aditya-shukla)

## What was built

| Area | Files | State |
| --- | --- | --- |
| `monitor-and-regulate-thinking` | `SKILL.md`, `LICENSE.txt`, `agents/openai.yaml`, 6 references | Complete |
| `create-through-recomposition` | `SKILL.md`, `LICENSE.txt`, `agents/openai.yaml`, 7 references | Complete |
| `manage-working-context` | `SKILL.md`, `LICENSE.txt`, `agents/openai.yaml`, 7 references | Complete |
| Evaluation set | Manifest, 112 prompts across 4 files, 4 rubrics | Complete, unfrozen |
| Benchmarks | README, run-manifest template, empty result directories | Template only |
| Repository files | README, LICENSE, CITATION.cff, CONTRIBUTING, this report | Complete |
| Automation | `tools/validate_skills.py`, `.github/workflows/validate-skills.yml` | Passing |

`SKILL.md` line counts: metacognition 223, creativity 251, runtime 200. All are well under the 500-line ceiling, leaving room for the operational detail that forward testing will add.

Structural validation currently reports `PASS`, 8797 checks, 0 warnings.

The runtime was added in a second build pass, after the first two packages were reviewed. Deviations D9 through D12 and open question Q5 belong to that pass.

## Deviations from the specification

### D1 — The donation URL was resolved from `links.txt`

**Specification.** Section 9.1 marks `<DONATION_URL>` a publication blocker and forbids fabricating one.

**Built.** Both packages use `https://buymeacoffee.com/adityashukla`, taken from `links.txt` in the build directory.

**Why.** The URL was supplied alongside the specification rather than invented. It was not fabricated, but the specification did not itself designate it canonical.

**Needs approval.** Confirm this is the canonical donation URL. If it is not, this is still a publication blocker.

### D2 — The general control-selection table stayed in `SKILL.md`

**Specification.** Section 6.12 lists "the epistemic-state taxonomy and control-selection table" as required content of `references/metamemory-model.md`. Section 10.3 forbids duplicating explanatory material between a `SKILL.md` and a reference.

**Built.** The blockage-keyed condition-to-operation table from Section 6.5 is in `SKILL.md` Step 5. `metamemory-model.md` holds the epistemic-state taxonomy and a separate state-keyed control mapping.

**Why.** The two requirements conflict. The blockage-keyed table is runtime-critical and belongs where the procedure is; duplicating it into the reference would violate the no-duplication rule. The two tables are keyed on different things, so both exist without repeating each other. Each file points at the other.

### D3 — A `layer` field was added to the source-map schema

**Specification.** Section 3 defines a six-field minimum schema and calls it a minimum.

**Built.** Every record carries `layer: source-grounded` or `layer: design-inference`.

**Why.** Acceptance gate 5 requires that every hard instruction either has a source-map record or is labeled a design inference. Without an explicit field, that distinction lives only in prose and cannot be checked mechanically. The validator now enforces it: `source-grounded` records must carry a `cognitiontoday.com` URL, and `design-inference` records must set `source_id` and `source_claim` to `none`.

### D4 — An epistemic legend notation was introduced in the references

**Specification.** Section 3 requires the four layers stay distinct but prescribes no notation for prose files.

**Built.** Reference files use `[S]` source claim, `[D]` design inference, `[A]` agent rule, `[V]` validation result, and `[?]` for a topic the specification named without transcribing.

**Why.** Sentence-by-sentence layer separation is unreadable in prose without a marker. `[?]` was added because several required reference topics are named in the specification but not supplied.

### D5 — A repository-level validation script was written

**Specification.** Section 4 says not to create scripts for these first versions. Section 16.2 requires automated structural validation in CI.

**Built.** `tools/validate_skills.py` at the repository root. No scripts exist inside either skill package.

**Why.** The Section 4 prohibition concerns skill procedures that require contextual judgment. Structural validation is deterministic file checking and is explicitly required by the launch package. The runtime packages remain script-free.

### D6 — `references/examples.md` was written for both skills

**Specification.** Section 4's tree omits `examples.md` from the metacognition package, but Section 10.4 requires both `SKILL.md` files to route to `references/examples.md`.

**Built.** Both packages have one. The routing instruction would otherwise point at a missing file.

### D7 — The cross-skill prompt set has 8 prompts, not 40

**Specification.** Section 16.5 requires 40 to 60 prompts per domain skill. It sets no size for a cross-skill set.

**Built.** 40 prompts for each domain skill. 8 cross-skill prompts, one per forward test X1 through X8.

### D8 — Behavioural acceptance tests were encoded rather than executed

**Specification.** Section 10.2 step 12 instructs the builder to run the acceptance tests in Sections 6.13, 7.15, 11, and 12.

**Built.** Every acceptance test M1-M12, C1-C14, and X1-X8 is encoded as an evaluation prompt with observable `must` and `must_not` criteria and an `acceptance_test` field linking it back.

**Why.** These tests require running the skills against live models across multiple families and judging blind. That is a benchmark run, not a build step. Encoding them makes them executable; nothing has executed them.

### D9 — A third provenance layer, `author-specified`, was introduced

**Specification.** Section 3 separates source claim, design inference, agent rule, and validation result. The source map originally allowed two layers: `source-grounded` and `design-inference`.

**Built.** A third value, `author-specified`, citing `master-specification#<section>`.

**Why.** The runtime's state contract comes from Section 5 of the specification. No article claims it, so it is not `source-grounded`. It is also not the compiler's invention, so labeling it `design-inference` would both understate its authority and misattribute its authorship. The distinction has a practical consequence: `design-inference` rules may be changed on engineering grounds, `author-specified` rules are under change control.

**Consequence.** Some records in the first two packages are currently mislabeled. See Q5.

### D10 — The runtime's reference structure was chosen by the compiler

**Specification.** Section 4's tree does not include `manage-working-context`, and no section specifies its reference files.

**Built.** Seven references mirroring the domain packages: `state-model.md`, `capsule-contract.md`, `compaction-and-recovery.md`, plus the four standard provenance and example files.

**Why.** The split follows progressive disclosure. `capsule-contract.md` is loaded only when integrating a skill; `compaction-and-recovery.md` only when resuming or failing. Merging them would force both into context on every activation.

### D11 — The capsule contract was versioned and made skill-agnostic

**Specification.** Section 5 lists nine capsule fields. It does not version them or describe how a new skill becomes compatible.

**Built.** `capsule_version: 1`, a required-versus-optional split, a `retrieval_status` return field, a compatibility checklist, and a versioning policy.

**Why.** Stated build requirement: this runtime is the substrate for future Cognition Today skills. An unversioned interface breaks every existing caller the first time a field is renamed. The required-field split and `retrieval_status` are compiler additions and are labeled as design inferences.

**Needs approval.** The capsule contract is now a public interface. Changes to it require approval under the change-control rule, because every future skill will depend on it.

### D12 — A fourth rubric and a 24-prompt runtime set

**Specification.** Section 4's tree lists three rubrics. Section 16.5 sizes prompt sets at 40 to 60 per domain skill.

**Built.** `runtime-rubric.yaml` and 24 runtime prompts: 8 positive, 8 negative, 4 boundary, 4 recovery.

**Why.** The runtime is not a domain skill and is scored against the four dependency states in Section 11 and the eight areas in Section 16.10, which 24 prompts cover. Negative cases are weighted unusually heavily because an always-on state manager is this skill's worst failure mode and it is discoverable on every turn.

### D13 — Repository and skill titles rebranded on author instruction

**Specification.** Section 16.1 fixes the launch positioning as "Cognition Today Cognitive Skills — evaluated cognitive control layers for model-agnostic agents." Sections 6.3 and 7.3 fix `display_name` as "Monitor and Regulate Thinking" and "Create Through Recomposition."

**Built.** The repository is titled **Simulated Cognitive Skills for LLM Creativity and Metacognition**. Display titles are Simulated Metacognition, Simulated Creative Cognition, and Simulated Working Memory, with the operational verb phrases moved into `short_description` and retained in each `SKILL.md` H1.

**Why.** Directed by Aditya Shukla after the build, superseding the earlier positioning. The change is an improvement on the honesty discipline rather than a cost to it: "simulated" states the analogy in the title instead of deferring it to a guardrail, and each `SKILL.md` now opens with a note that the word is literal.

**Unchanged.** The frontmatter `name` field of each skill, which must equal its folder name under Gate 1 and is the invocation identifier. Renaming those would break installation paths, eval prompt references, the run manifest, and the source maps. Titles and identifiers are now deliberately different things, and the README says so.

**Resolved alongside Q4.** The GitHub repository is `shredwarrior/cognition-today-skills`. The local directory name is unchanged.

## Things the specification expected that are absent

### A1 — No `assets/` directory in the creativity package

Section 4 anticipates `assets/decompose-recompose-source-visual.*`. No image was supplied. Section 10.2 step 10 permits source visuals only when legally owned, relevant, and verified, and Section 6.3 forbids pointing metadata at nonexistent files. An empty directory or a placeholder image would violate both.

`source-graph.yaml` records `source_visual_verified: false` and describes what to do when a diagram is supplied.

### A2 — Source notes are second-hand

Sections 6.12 and 7.14 require attributed source notes under named article headings. The specification names the headings and restates the claims the agent rules depend on, but does not reproduce the article text, and the articles were not fetched during this build.

Both `source-notes.md` files are organized under the required headings and mark every claim `spec-attributed` or `pending`, with a verification ledger at the end. Nothing is presented as a quotation. Roughly a third of the entries are `pending`.

**This is the largest open item in the build.** Reading the four articles and resolving the ledgers would materially improve both packages.

### A3 — Source URL anchors are constructed, not verified

Source-map records and reference files cite anchors such as `#theories-of-metamemory` and `#randomness-induced-creativity`. Four came from the specification directly. The rest were derived by slugifying the heading names the specification lists.

Constructed anchors may not match the live pages. The article URLs are correct; the fragments need checking. The CI link check validates base URLs only, since a fragment cannot be verified by HTTP status.

### A4 — The runtime exists but has never run

Built in the second pass, outside the original scope of Section 0, which treated `manage-working-context` as a dependency contract only. Arm C of the benchmark design is now unblocked.

Two things follow. First, the runtime's article grounding is the weakest in the repository: Section 2 names three supporting sources but supplies no headings, no claims, and no anchors for any of them, and none was read during this build. Almost everything in the package is `author-specified` or `design-inference`, and `source-notes.md` says so at the top.

Second, no state file has ever been written by this skill. The formats, consolidation boundaries, degraded mode, and recovery behaviour are specified and internally consistent, and entirely unexercised.

### A4b — No seeded state fixtures for recovery testing

The four runtime recovery prompts assume state files already on disk in specific conditions: complete, partial, absent, and containing a broken pointer. Those fixtures have not been written, so the recovery prompts cannot be run as-is.

### A5 — No holdout evaluation set

Section 16.5 requires a private holdout alongside the public set. Only the public set exists. Required before any public performance claim.

### A6 — Long-context prompts are not real transcripts

The five long-context prompts in each set use bracketed setup notes such as `[Long session, manage-working-context NOT installed]`. Real multi-turn transcripts are needed before the benchmark freeze.

### A7 — `CITATION.cff` `date-released` is still null

`repository-code` is now `https://github.com/shredwarrior/cognition-today-skills`. `date-released` stays null until a public version is cut. See Q4.

## Global acceptance gate status

Against Section 13.

| # | Gate | Status |
| ---: | --- | --- |
| 1 | Folder names match frontmatter names | Pass, CI-enforced |
| 2 | Frontmatter contains only `name` and `description` | Pass, CI-enforced |
| 3 | Trigger descriptions contain positive and negative boundaries | Pass, CI-enforced |
| 4 | Each `SKILL.md` under 500 lines | Pass, 223, 251, and 200 |
| 5 | Every hard instruction has a source-map record or a design-inference label | Pass, CI-enforced via `layer` |
| 6 | Source claims never presented as proof of agent architecture | Pass, CI checks the obvious phrasings; reviewed by hand |
| 7 | Tables and flowcharts have machine-readable equivalents | Pass for equivalence; **unverified against source visuals**, since none exist |
| 8 | Metacognition changes the object-level task | **Untested.** Encoded in the rubric as a double-weighted dimension |
| 9 | Creativity produces structural variation | **Untested.** Encoded as a double-weighted dimension |
| 10 | Creativity does not hijack first-pass debugging | **Untested.** Prompts CTR-N02, CTR-B05, CTR-B06 |
| 11 | Metacognition does not interrupt divergence | **Untested.** Prompts MRT-P05, X1, X2 |
| 12 | Both skills complete without the runtime | **Untested.** Prompts MRT-L01, CTR-L01 |
| 13 | Runtime preserves state without taking over | **Untested.** Ownership boundary is a binary rubric dimension. Prompts MWC-P07, MWC-R01, X5 |
| 14 | Personal guidance does not become diagnosis | **Untested.** Prompts MRT-P02, MRT-B05, X3. Binary rubric dimension |
| 15 | Neither skill requests or exposes hidden chain-of-thought | **Untested.** Prompt MRT-B07 |
| 16 | Attribution, source links, license, disclaimer, donation present | Pass, CI-enforced |
| 17 | A fresh agent can use each package without this conversation | Pass by construction; **unverified** |
| 18 | Positive, negative, boundary, persistent-failure, long-context, and conflicting-instruction tests pass | **Untested.** All classes are written |
| 19 | Untested compiler-added rules remain marked `untested` | Pass, CI-enforced |
| 20 | Not publicly released while a blocker remains | Pass. Marked `v0.1.0-unpublished` |

Nine of twenty gates pass mechanically. Eleven are behavioural and require a benchmark run. None is now blocked on a missing component.

## Publication blockers

Against Section 14.

| Blocker | State |
| --- | --- |
| Replace `<DONATION_URL>` | Resolved from `links.txt`, pending confirmation. See D1 |
| Complete CC BY-NC-SA 4.0 text in each `LICENSE.txt` | Resolved. Full legal code, 21 KB, at the root and in all three packages |
| Confirm noncommercial, not merely resale prohibition, is intended | **Open.** See Q1 |
| Verify ownership and redistribution rights for bundled visuals | Not applicable. No visuals bundled |
| Forward-test both skills and update `validation_status` records | **Open.** No test has been run |
| Approve every design inference that became a hard or default rule | **Open.** See Q2 |

## Decisions needed from Aditya Shukla

**Q1 — Is the licensing restriction noncommercial use, or resale only?**

Section 9.2 flags that CC BY-NC-SA 4.0 prohibits all commercial use, which is broader than a resale prohibition. Under the current license a consultancy could not use these skills on client work internally. If that is not the intent, the license must be replaced with a reviewed custom source-available license rather than patched with a note.

**Q2 — Approve or revise the compiler-added rules that became defaults.**

Each is labeled `layer: design-inference` and none has source authority:

| Rule | Where | Risk if wrong |
| --- | --- | --- |
| Two materially similar failures before creativity may enter debugging | Creativity trigger | Too high, and genuinely stuck sessions grind; too low, and ideation replaces reading the error |
| Three intensity levels for metacognition | Metacognition | Wrong granularity produces either overhead on light questions or thin handling of complex ones |
| Exactly one primary control operation per loop | Metacognition Step 5 | May be too strict when two interventions genuinely compose |
| Three variants by default | Creativity Step 7 | Cheap to change, low risk |
| One alternate control attempt, then stop | Metacognition Step 7 | Bounds recursion; may terminate a productive second pass |
| Ten-label epistemic-state enum | Metacognition | Too many labels invites database-style output; too few loses the familiarity distinction |
| `.cognition-today/` as the default state path | Runtime | See Q6 |
| Consolidation boundaries and the six triggers for them | Runtime | Too eager grows the ledger on every turn; too lazy loses decisions to compaction |
| Size targets of 100 and 400 lines | Runtime | Arbitrary until measured against real sessions |
| `capsule_version: 1` and the required-field split | Runtime | Becomes expensive to change once other skills depend on it. See D11 |
| Degraded-mode behaviour when no filesystem exists | Runtime | Untested in any client |

**Q3 — Should the articles be read and the source notes rebuilt before anything else?**

This is the recommended next step. It converts roughly a third of the reference content from `pending` to attributed, verifies the constructed URL anchors, and is a prerequisite for any honest public claim about source authority. It matters most for the runtime, where all three articles are unread and nothing is currently derived from them.

**Q4 — Confirm the repository name and GitHub location.**

Resolved in this pass as `shredwarrior/cognition-today-skills`, matching the git user.name already on this machine. README, `CITATION.cff`, `INSTALL.md`, and `.cursor-plugin/plugin.json` use that URL. Revisit only if the public name should differ.

**Q5 — Approve retrofitting the `author-specified` layer to the first two packages.**

The runtime introduced a third provenance layer (D9). Applying it revealed that several records in the domain packages are mislabeled: rules taken verbatim from your specification — the three-level intensity ladder, the ten-label epistemic-state enum, the fifteen-operator selection discipline, the state schemas — are currently marked `design-inference`, which credits them to the compiler rather than to you and puts them outside change control.

This is a mechanical relabel of roughly six to eight records across two files, with no change to any rule text. It was not done unilaterally because `CONTRIBUTING.md` places source interpretations under change control, and both packages had already been reviewed.

Recommended: approve. Leaving it understates your authorship and lets rules you specified be revised as though they were engineering guesses.

**Q6 — Confirm the state-file location and whether it should be version-controlled.**

The runtime defaults to `.cognition-today/` at the workspace root, holding `working-context.md` and `memory-base.md`. Two open points: whether that path is right, and whether the repository should recommend committing these files, ignoring them, or leaving the choice to the user. Committing makes decisions reviewable in pull requests; ignoring keeps working notes out of history. The skill currently takes no position.
