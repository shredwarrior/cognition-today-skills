# State model

The two-file model, its mutation policy, and the exact file formats. Load this before creating, reading, or rewriting any state file.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [Sources](#sources)
3. [Why two files](#why-two-files)
4. [The mutation invariant](#the-mutation-invariant)
5. [The transformation layer](#the-transformation-layer)
6. [Where the files live](#where-the-files-live)
7. [Format: working-context.md](#format-working-contextmd)
8. [Format: memory-base.md](#format-memory-basemd)
9. [What belongs in which file](#what-belongs-in-which-file)
10. [Consolidation boundaries](#consolidation-boundaries)
11. [Size discipline](#size-discipline)
12. [Ownership boundary](#ownership-boundary)

## Epistemic legend

| Label | Meaning |
| --- | --- |
| `[S]` | Source claim from a cited Cognition Today article |
| `[M]` | Specified directly by Aditya Shukla in the master implementation specification. No article claims it; it is not the compiler's invention either |
| `[D]` | Design inference. Compiler-added engineering decision with no authority |
| `[A]` | Agent rule. The executable instruction |
| `[V]` | Validation result. `untested` until a recorded evaluation exists |
| `[?]` | Named in the specification but not transcribed from the source. Verify before public claims |

This package carries more `[M]` than either domain skill, because the master specification defined its state contract directly rather than deriving it from an article.

## Sources

- Aditya Shukla, [Memory Models in Psychology](https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/), Cognition Today.
- Aditya Shukla, [A Thrifty Brain gave us Multi-tasking Abilities](https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/), Cognition Today.
- Aditya Shukla, [Metacognition & Metamemory Explained](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

`[?]` None of the three articles was read during this build. See `source-notes.md` for the verification ledger.

## Why two files

`[S]` Memory models in psychology distinguish a limited-capacity active store, where material is currently being manipulated, from a durable store, where stable material is retained. Movement between them is not automatic.

`[D]` The transferable structure is the separation, not the neuroscience. An agent session has an equivalent problem: a small, fast-changing representation of what is being worked on right now, and a slower, larger record of what has been settled. Collapsing them produces one of two failures — either the durable record churns on every step and stops being trustworthy, or the active representation grows until it costs as much as the history it was supposed to replace.

`[A]` Never describe the agent as having short-term or long-term memory, encoding, consolidating in the biological sense, or a memory store. Describe the files: a working representation and a durable ledger.

| File | Function `[M]` | Mutation policy `[M]` |
| --- | --- | --- |
| `working-context.md` | Short, mutable representation of the current objective, active operation, constraints, decisions, uncertainty, pointers, and next action | The only file rewritten during ordinary work |
| `memory-base.md` | Durable ledger of stable definitions, evidence, approved decisions, failed approaches, provenance, and resumable thread capsules | Updated only at an explicit consolidation boundary |

## The mutation invariant

`[M]` Do not update both files in the same ordinary work step. At consolidation, freeze the current working state into the durable ledger, and derive the next working state as a separate operation.

`[A]` Consolidation is therefore always two sequential operations, never one:

1. **Freeze.** Write the settled material from `working-context.md` into `memory-base.md`. Do not touch `working-context.md` in this step.
2. **Derive.** As a separate operation, rewrite `working-context.md` for the next phase, carrying forward only what remains active.

`[D]` The reason for the ordering is auditability. If both files change at once, a reader cannot tell whether the ledger recorded what the working context actually held, or whether both were rewritten to agree with each other after the fact. Sequencing the writes makes the freeze inspectable.

`[A]` If a step tempts you to update both, it is a consolidation and must be split. If it cannot be split, it is not a consolidation and `memory-base.md` stays closed.

## The transformation layer

`[D]` The two-file model says where state lives but not how bulk material enters it. Without a defined entry path the common failure is a dump pasted straight into the working context, which grows it past the point of usefulness in one step, or a prose summary of the dump, which reads well and silently merges the epistemic layers.

`[A]` Bulk material never enters either file in the form it arrived in. It passes through a transformation, and the transformation is a consolidation like any other.

`[A]` Choose the structuring form from the material, not from preference:

| Form | The material has | Produces |
| --- | --- | --- |
| Schema | Recurring typed fields across entries | Fields named once, entries beneath them |
| Table | Items comparable along shared dimensions | One row per item; columns only for dimensions that differ |
| Restructure | Argument or narrative with no repeating unit | Nested claims with their support, ordered by dependency |

`[A]` One form per dump. Material that fits none of the three is usually two dumps and is split before transforming.

`[D]` The forms are ordered by how much they constrain later compression. A schema and a table survive being shortened because their structure is separate from their content; prose does not, which is why restructure is the last resort rather than the default.

`[A]` What the transformation drops: restatement, hedging, transitions, formatting, and the reasoning walk. What it must keep: every claim, constraint, decision, rejection, and number, each carrying the pointer it came from.

`[A]` When the layer of an item is genuinely unclear, keep the item and mark it unresolved. Never assign it to `governing_source_claims` or `design_inferences` to make the structure look complete. An unresolved label is recoverable; a wrong one is not.

`[A]` The flow, in order, and never collapsed into one step:

1. **Transform.** Structure the dump. Nothing is written yet.
2. **Freeze.** Write the structure into `memory-base.md` as a permanent update — `Evidence` for findings, `Stable definitions` for settled terms, `Provenance` for source mapping.
3. **Derive.** Separately, write into `working-context.md` only the slice the active operation needs, plus a pointer to the frozen structure.

`[A]` Discard the raw material after the freeze. Retain the pointer to its origin, not its text.

`[A]` The check that the layer did its job: the derived slice is materially smaller than the frozen structure. If they are the same size, the material was moved rather than transformed.

`[D]` This is the only path by which a domain skill's bulk output reaches durable state. Domain skills still do not write the files — they hand over the dump and the runtime performs all three steps.

## Where the files live

`[D]` The location is a compiler decision. The specification defines the two files but not their path.

Default:

```text
<project-root>/.cognition-today/
├── working-context.md
└── memory-base.md
```

`[A]` Resolution order:

1. A location the user names in this session.
2. A location documented in the project, for example in `AGENTS.md` or a project README.
3. The default above, at the root of the current workspace.

`[A]` State is project-scoped, not global. Do not write to the user's home directory. Do not create state directories in unrelated projects.

`[A]` On first creation, tell the user the path and that these are plain files they can read, edit, commit, or delete. State the agent writes about a user's work should never be invisible to them.

`[A]` Never overwrite an existing state file on initialization. If one exists, read it first.

## Format: working-context.md

`[D]` The structure is a compiler decision; the field list is `[M]`. Keep it in this order so a reader can scan it.

```markdown
# Working context

- updated: 2026-08-03T19:40:00Z
- active_skill: create-through-recomposition
- active_operation: recompose-variants
- capsule_version: 1

## Objective

One or two sentences. What finishing looks like.

## Locked constraints

- Constraints and user-approved elements that survive every iteration.

## Governing source claims

- Claims from cited sources currently governing the active operation, with source IDs.

## Design inferences

- Agent-side operationalizations in play, labeled as inferences. Never merged with the list above.

## Completed transformations

- What has already been done and does not need redoing.

## Rejected approaches

- What was tried or considered and set aside, each with the reason.

## Open uncertainties

- What is unresolved, and what would resolve it.

## Pointers

- Where the material lives: file paths, URLs, message references. Pointers, not copies.

## Next action

One sentence. The single thing to do next.
```

`[A]` Omit any section that is empty. An empty heading is noise that costs tokens on every read.

## Format: memory-base.md

```markdown
# Memory base

- updated: 2026-08-03T19:40:00Z
- consolidations: 4

## Stable definitions

Terms, entities, and conventions fixed for this project.

## Evidence

Findings with their source and how they were established.

## Approved decisions

- 2026-08-03 — Decision, who approved it, and what it constrains.

## Failed approaches

- Approach, what happened, and what the failure ruled out.

## Provenance

Source IDs in use, and which source claims versus design inferences govern them.

## Thread capsules

### thread: api-deprecation-schedule

- status: paused
- frozen_at: 2026-08-03T19:40:00Z
- objective: ...
- locked_constraints: ...
- completed: ...
- rejected: ...
- open_uncertainties: ...
- next_action: ...
```

`[A]` Thread capsules are sections inside `memory-base.md`, not separate files. The model is two files. Do not add a third.

`[A]` `memory-base.md` is append-oriented. Correct an entry when it is wrong; do not silently delete history that a later decision depends on.

## What belongs in which file

| Item | File | Why |
| --- | --- | --- |
| Current objective | Working context | Changes as work proceeds |
| Next action | Working context | Changes every step |
| Open uncertainties | Working context | Resolves and moves |
| Active operation and skill | Working context | Changes on handoff |
| A decision the user approved | Memory base | Must survive every later rewrite |
| An approach that failed and why | Memory base | Prevents rediscovering it in round nine |
| A definition the project settled on | Memory base | Stable |
| Evidence and how it was established | Memory base | Stable |
| A paused thread | Memory base | Resumable later |
| The structure derived from a dump | Memory base | Permanent once frozen; the transform is not repeated |
| A large source corpus or a raw dump | Neither, in raw form. Transform it, freeze the structure, keep a pointer in the working context | Copying it in defeats the purpose |

`[A]` When unsure, put it in the working context. Promotion at the next consolidation is cheap; demoting something wrongly frozen into the ledger is not.

## Consolidation boundaries

`[A]` Consolidate at an explicit boundary, not on a timer. The boundaries:

- The user approves an element, a decision, or a direction.
- A workstream completes.
- A thread is being paused to switch to another.
- A context compaction is expected or has been announced.
- A round of iteration closes and its deltas are settled.
- A dump has been transformed and its structure has settled.
- A hand-off has been signalled, or context has reached 98%.
- The session is ending.

`[A]` Do not consolidate mid-operation. A half-finished transformation frozen into the ledger reads later as a settled decision.

`[D]` Consolidating too often is the more likely error. Each consolidation costs two writes and adds to a file that is read on every resume. If nothing has settled, nothing needs freezing.

## Size discipline

`[D]` A state system that grows without bound recreates the problem it was built to solve.

`[A]` Targets, not hard limits:

| File | Target | On exceeding |
| --- | --- | --- |
| `working-context.md` | Under 100 lines | Move settled material to the ledger at the next boundary, or replace inline content with a pointer |
| `memory-base.md` | Under 400 lines | Compress older thread capsules to objective, outcome, and next action; keep decisions and failures in full |

`[A]` Never compress a locked constraint, an approved decision, or a failed approach out of existence. Those are the entries the whole system exists to preserve.

## Ownership boundary

`[M]` The domain skill does not directly mutate these files unless the runtime delegates a documented operation. The runtime remains the state owner.

`[M]` The runtime owns attention, continuity, retrieval pointers, and compaction-safe state. It must not reinterpret or broaden a domain skill.

`[A]` Concretely, this runtime never decides which control operation a metacognitive skill should select, never decides which creative operator to apply, never judges whether a candidate is good, and never edits a domain artifact. It records, preserves, and returns. If a domain skill hands it a bad capsule, it stores the bad capsule and may say so; it does not fix it.

`[V]` untested.
