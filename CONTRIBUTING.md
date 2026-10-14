# Contributing

This repository converts cognitive-psychology frameworks published on [Cognition Today](https://cognitiontoday.com) into executable agent skills that simulate the structure of human cognitive functions. Those articles are the ground truth; the conversion discipline is the product. A contribution that improves output quality while breaking the provenance chain will be declined.

Two constraints follow from the branding and are not negotiable. The skills simulate structure, so no contribution may assert that the agent possesses metacognition, memory, or creativity in the human sense. And the source articles are the authority, so no contribution may substitute an external citation for one of them in a `source-grounded` record.

Read this before opening a pull request.

## The four layers

Every operational rule in this repository belongs to exactly one of four layers, and the layers must never be merged.

| Layer | What it is | Where it lives |
| --- | --- | --- |
| Source claim | What a Cognition Today article asserts about human cognition or behaviour | `references/source-notes.md`, `source_claim` in the source map |
| Design inference | Why that structure might be useful in an agent workflow | `design_inference` in the source map, `[D]` in references |
| Agent rule | The executable instruction the skill imposes | `SKILL.md`, `agent_rule` in the source map |
| Validation result | What forward tests actually showed | `validation_status` |

If you cannot say which layer your change belongs to, the change is not ready.

## Evidence requirements

**Adding or changing a hard agent rule** requires a `source-map.md` record declaring one of three layers. A rule with no record will fail CI.

| `layer` | `source_id` | Means | Revisable on engineering grounds? |
| --- | --- | --- | --- |
| `source-grounded` | A `cognitiontoday.com` article URL with heading anchor | A published article supplies the mechanism | No. Attribution must be retained |
| `author-specified` | `master-specification#<section>` | Aditya Shukla specified it directly. No article claims it, but it is not yours either | No. Under change control |
| `design-inference` | `none` | Your engineering decision. No authority | Yes |

Pick the layer honestly. Labeling your own choice `author-specified` borrows authority you do not have; labeling a specified rule `design-inference` lets someone later revise a decision that was not theirs to revise.

**Do not import external frameworks.** Capability logic must be grounded in the named Cognition Today articles. If a rule from another literature would genuinely improve the skill, open an issue proposing it rather than adding it. It may belong in a future skill built from a different source.

**Do not upgrade a design inference into a finding.** Compiler-added thresholds — the two-failure gate, the three-variant default, the intensity ladder — stay labeled as design inferences and stay `untested` until an evaluation says otherwise.

**Do not claim the agent has human cognition.** No metacognition, metamemory, working memory, default-mode network, central executive, epistemic feelings, incubation, insight, or consciousness. These are source structures; their agent-side implementation is an explicit operational analogy. CI checks for the obvious phrasings; the reviewer checks for the rest.

## Structural requirements

- Frontmatter contains exactly `name` and `description`. Nothing else.
- The folder name matches the frontmatter `name`.
- Each `SKILL.md` stays under 500 lines.
- Reference files sit exactly one level below `SKILL.md`.
- A reference longer than 100 lines carries a `## Contents` table.
- Nothing is duplicated between a `SKILL.md` and a reference. If a table belongs in both places, pick one and route to it.
- No `README.md`, `CHANGELOG.md`, install guide, or quick-reference file inside a skill folder. Repository-level files handle installation, evaluation, citation, and public communication.
- No unresolved placeholders. `TODO`, `TBD`, `FIXME`, and `<DONATION_URL>` all fail CI.

Run `python tools/validate_skills.py` before pushing. It checks all of the above.

## Testing requirements

Structural validation is necessary and not sufficient. It cannot tell whether the metacognition skill actually changed the object-level task or whether the creativity skill produced structural rather than lexical variation.

**Behaviour changes need evaluation evidence.** If your change affects triggers, procedures, or output contracts, run the relevant prompts from `evals/prompts/` on both arms and include the outputs in the pull request. Include the negative and boundary cases, not only the positive ones. A change that improves positive-case behaviour while increasing false activation is a regression.

**New rules need new test cases.** Add prompts to the relevant set, including at least one negative or boundary case that the new rule could plausibly break.

## Attribution requirements

Every package keeps: `Cognition Today`, `Aditya Shukla`, `https://cognitiontoday.com`, every exact source-article URL that package uses, the statement separating source claims from agent operationalization, the redistribution instruction, the warranty disclaimer, and the donation link.

Removing or weakening any of these will be declined. This is the condition on which the underlying work is shared.

## Licensing

Content is licensed CC BY-NC-SA 4.0: source-available for noncommercial use, not OSI open source. Contributions are accepted under the same terms. If executable scripts are added later, they will be licensed separately under PolyForm Noncommercial 1.0.0 unless Aditya Shukla approves another software license.

## Change control

These require explicit approval from Aditya Shukla before merge:

- Triggers and activation boundaries
- Capability scope
- Source interpretations
- Default operations
- Runtime activation conditions
- Licensing
- Attribution

Formatting fixes, typo corrections, and test-result updates do not require approval, provided they do not alter meaning.

## Reporting a behaviour problem

Useful reports name the model and version, the client, the skill version or commit, the exact prompt, what happened, what you expected, and whether it reproduces. Distinguish installation failures from skill-behaviour failures; they get triaged differently.

Reports that a skill activated when it should not have are as valuable as reports that it failed to activate.

## Adding a new skill to the collection

New Cognition Today skills coordinate with `manage-working-context` through a versioned source-intent capsule. The contract and a compatibility checklist are in [`skills/manage-working-context/references/capsule-contract.md`](skills/manage-working-context/references/capsule-contract.md).

In short: embed the coordination block verbatim, declare it in `SKILL.md` and not in `agents/openai.yaml`, emit the four required capsule fields with source claims and design inferences as separate lists, and stay fully functional when the runtime is absent.

You should not need to modify the runtime to add a skill. If you do, that is a capsule-contract version change and needs approval.

