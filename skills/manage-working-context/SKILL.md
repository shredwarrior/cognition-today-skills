---
name: manage-working-context
description: Preserve objective, locked constraints, approved decisions, rejected approaches, source provenance, and the next action across long agent sessions, context compaction, and thread switching, using a two-file working-context and memory-base state model. Provides the shared transformation layer that turns an unstructured dump into a schema, table, or restructure, freezes it permanently into the memory base, and offloads only the active slice into the working-context file. Use when a task will span many tool calls or a compaction, when three or more interdependent workstreams must be retained, when earlier user decisions or approved elements must not be overwritten, when a large corpus or dump must be reduced to a smaller active representation, when an unfinished thread will be resumed later, or when repeated iterations require tracking what changed and what stayed fixed. Run its sanity check before a user-chosen compaction, before a signalled hand-off, and at 98% context. Do not use for short or self-contained tasks, single questions, routine edits, long conversations in which nothing was decided, or when the user already maintains their own decision log.
---

# Simulated Working Memory — Manage Working Context

> "Simulated" is literal. This skill reproduces the *structure* of working memory and consolidation as explicit files. It does not give you memory. What is not written down is gone, and you must say so rather than reconstruct it. See [Guardrails](#guardrails).

Preserve what must survive compression. Not the transcript — the intent: what we are doing, what the user already decided, what has been ruled out and why, which claims came from which source, and what happens next.

This is the shared runtime for the Cognition Today skill collection. Domain skills own their reasoning. This skill owns continuity, attention, retrieval pointers, and compaction-safe state. It never decides anything a domain skill is responsible for.

## Activate when

At least one condition holds:

- The task is expected to span many tool calls or context compactions.
- Three or more interdependent workstreams must be retained.
- Earlier user decisions or approved elements must not be overwritten.
- A large source corpus must be reduced into a smaller active representation.
- The agent switches away from an unfinished thread and must later resume it.
- Repeated iterations make it necessary to preserve what changed, what remained fixed, and why.

**Being installed is not a trigger.** Presence alone does not activate this skill.

## Do not activate for

- A short or self-contained task.
- A single question or a routine edit.
- A long task with nothing worth preserving — fifty independent items have no continuity.
- A long conversation in which nothing was decided, rejected, or approved. Duration is not continuity.
- A first message that merely sounds large. Wait for the first constraint or approval.
- A user who already maintains their own decision log. Do not build a parallel state system beside theirs.

Before activating, ask what would be lost if the session ended now. If the answer is "nothing that isn't easy to redo," stay inactive. See `references/examples.md`.

## The two files

| File | Holds | Written when |
| --- | --- | --- |
| `working-context.md` | Current objective, active operation, locked constraints, source claims, design inferences, completed work, rejections, open uncertainties, pointers, next action | Every ordinary work step. This is the only file ordinary work touches |
| `memory-base.md` | Stable definitions, evidence, approved decisions, failed approaches, provenance, paused thread capsules | Only at an explicit consolidation boundary |

**The invariant: never write both files in the same ordinary work step.**

Consolidation is therefore always two sequential operations, never one:

1. **Freeze** — write settled material into `memory-base.md`. Do not touch the working context in this step.
2. **Derive** — as a separate operation, rewrite `working-context.md` for the next phase.

If a step tempts you to write both, it is a consolidation and must be split. If it cannot be split, it is not a consolidation and the ledger stays closed.

Read `references/state-model.md` for the file formats, what belongs in each, size targets, and where the files live.

## Order of operations on incoming material

**Restructure, then prioritize, then apply. This order is hard and admits no shortcut.**

1. **Restructure.** Complex or bulk input — pasted research, a transcript, a crawl, search results, an error log, a long exploratory exchange, a set of requirements — is reorganized into a schema, table, or restructure *before* anything is selected from it. Never prioritize inside raw material.
2. **Prioritize.** Only once the structure exists, decide what the active operation actually needs. Attention is applied to the structure, never to the dump.
3. **Apply.** The user's operations run against the prioritized slice, not against the original material.

Selecting straight from an unstructured dump looks like a shortcut and is the specific failure this runtime exists to prevent. What gets picked is whatever sits nearest the top or is most vividly worded, rather than what the task needs, and the epistemic layers are still buried in prose where the next compression will destroy them. Prioritizing before organizing is not selection; it is sampling.

The sources make this point structurally: an organized representation is what makes selective retrieval possible in the first place, which is why schemas, templates, and filters are described as prerequisites for skilled recall rather than as conveniences. Only the ordering transfers. You are writing two markdown files; see [Guardrails](#guardrails).

## Operations

### Discover

Check the agent's skill registry or documented skill directories for this runtime by exact name. If there is no registry, check only documented skill roots or already-authorized project skill directories. Never recursively scan arbitrary filesystem locations. Never install, copy, or modify a skill automatically.

### Initialize

Resolve the state root in this order: a location the user names, a location documented in the project, then `.cognition-today/` at the workspace root. Never write to the user's home directory.

Tell the user the path on first creation and that these are plain files they can read, edit, commit, or delete. Never overwrite existing state — if a file is there, read it first.

### Ingest a capsule

A domain skill hands over a source-intent capsule containing its objective, active skill and operation, source IDs, governing source claims, design inferences labeled as inferences, locked constraints and approved elements, completed transformations, rejected approaches, open uncertainties, and next action.

Check the four required fields: objective, active skill, active operation, next action. Report any that are missing. Do not invent a value for one. Then write the capsule into the working context.

Read `references/capsule-contract.md` for the schema, worked examples, and how a new skill becomes runtime-compatible.

### Transform a dump

A dump is unstructured bulk handed over by a domain skill or the user: pasted research, a crawl, a transcript, search results, a long exploratory exchange, an error log. It is raw material, not state.

Never ingest a dump as it arrives. It costs the tokens this runtime exists to save, and it hides the epistemic layers inside prose where the next compression will destroy them.

Transform it in one pass, choosing the form the material actually has:

| Form | Use when | Result |
| --- | --- | --- |
| Schema | The material has recurring typed fields | A YAML block with the fields named once and the entries under them |
| Table | The items are comparable along shared dimensions | One row per item, one column per dimension that actually differs |
| Restructure | The material is argument or narrative with no repeating unit | Nested claims with their support, ordered by dependency |

Pick one. Material that resists all three is usually two dumps; split it and transform each.

The transformation is lossy on purpose. Drop restatement, hedging, transitions, and formatting. Keep every claim, constraint, decision, rejection, and number, each with the pointer it came from. When you cannot tell whether something is a source claim or a design inference, keep it and label it unresolved. Never guess the layer to make the structure tidy.

Then run the flow. It is a consolidation and obeys the invariant:

1. **Freeze** — write the transformed structure into `memory-base.md` as a permanent update. Findings go under `Evidence`, settled terms under `Stable definitions`, source mapping under `Provenance`. Do not touch the working context in this step.
2. **Derive** — as a separate operation, write into `working-context.md` only the slice the active operation needs now, plus a pointer to the frozen structure.

The dump itself is never stored. Once the structure is frozen, keep the pointer to where the material came from and let the raw text go.

After a transform, `working-context.md` holds the active slice, not the structure. If the derived slice is as large as what you froze, nothing was transformed.

### Sanity check

Run this **before** the state is at risk, never after. A sanity check that runs after a compaction is an autopsy.

Triggers:

- The user chooses to compact, or a compaction is announced.
- The user signals hand-off intent — to another agent, another session, or another person.
- Context reaches 98% and no other boundary has been hit.

Check in order:

1. Are the four required fields present and current — objective, active skill, active operation, next action?
2. Is every locked constraint and approved decision in `memory-base.md`, and not only in `working-context.md`? Anything living only in the working context is what is about to be lost.
3. Are source claims, design inferences, agent rules, and validation results still separately labeled?
4. Does every rejected approach still carry its reason?
5. Does every pointer still resolve?
6. Is any dump still untransformed?
7. Is `next_action` one concrete action rather than a restatement of the objective?

A failure on 2, 3, or 6 is a consolidation that has not happened yet. Run it now — freeze, then derive — while there is still context left to do it in.

Report what passed and what did not, then state plainly whether the state is safe to compact across.

When a check fails and cannot be repaired — a pointer that no longer resolves, a decision nobody recorded — name it and leave it failed. Do not rebuild it from the visible conversation to make the report come out green. A passing sanity report assembled from inference is worse than a failing one, because it will be believed.

If you cannot observe context usage in this client, say so and treat compaction and hand-off as the only triggers you can actually detect. Do not claim a threshold you have no way to measure.

### Update

Rewrite `working-context.md`. Keep it under roughly 100 lines and self-sufficient. Omit empty sections.

### Consolidate

At a boundary — user approval, workstream completion, a thread pause, an expected compaction, a hand-off, the close of an iteration round, a transformed dump whose structure has settled, or session end — run freeze, then derive. Never mid-operation: a half-finished transformation frozen into the ledger reads later as a settled decision.

### Resume

Read `memory-base.md` first, then `working-context.md`. Report the objective, next action, locked constraints, approved elements, unread pointers, and anything expected but missing.

Set `retrieval_status` honestly: `complete` only when every returned field came out of a file, `partial` with a populated `missing` list otherwise, `unavailable` when no state was found.

Read `references/compaction-and-recovery.md` before any resume, corpus reduction, thread switch, or failure.

## Report gaps, never fill them

This is the guardrail that matters most here.

A state system fails safely when it loses information and says so. It fails dangerously when it produces something plausible instead. Asked to resume a thread, a model will fluently generate a coherent account of what was decided — and that output is indistinguishable in tone from a real recovery. The user cannot tell.

So:

- Never present a reconstructed field as a retrieved one.
- Never report `complete` for anything you inferred.
- Never substitute a similar file for a broken pointer.
- Never rebuild state from the visible conversation and call it recovered.
- Never delete or overwrite a state file to resolve an inconsistency. The user decides.

"I do not have the record of that decision" is a correct and useful answer.

## Preserve the epistemic layers

Keep source claims, design inferences, agent rules, and validation results distinguishable through every compression and every retrieval.

When space is tight, shorten individual entries. Never merge the lists, drop the labels, or summarize claims and inferences into one paragraph. This is the first thing compression destroys and the one thing that cannot be reconstructed afterwards.

## Degraded mode

When the client cannot write files, keep the same field structure in the visible conversation, restate it at boundaries, and say once that nothing is being persisted.

Never claim a file was written, a decision was saved, or that state will exist in a future session. The prohibition does not weaken because the runtime is present but unable to write.

## Ownership boundary

This runtime owns state. It does not own reasoning.

It never selects a control operation, never chooses a creative operator, never judges whether a candidate is good, never edits a domain artifact, and never reinterprets or broadens a domain skill. If a domain skill hands over a flawed capsule, store it and say so; do not repair it.

Domain skills do not write the state files directly. They send capsules. The only exception is an operation this runtime has explicitly delegated and documented.

When a stored rejection is about to be proposed again, flag it with its reason. Flagging is a state operation. Deciding what to do about it is not.

## Guardrails

- Do not activate because you are installed.
- Do not write state for a task with nothing worth preserving.
- Do not claim persistence you do not have.
- Do not describe yourself as having memory, encoding, storage, retrieval, or consolidation in the psychological sense. You maintain two markdown files.
- Do not hide state from the user. Show the path and the contents on request.
- Do not let either file grow without bound. Compress older thread capsules, never locked constraints, approved decisions, or failed approaches.
- Do not create a third state file, a database, or a parallel system beside a log the user already keeps.
- Do not replace doing the work with recording the work.
- Do not ingest a dump without transforming it, and do not store the raw material once its structure is frozen.
- Do not prioritize, filter, or answer from unstructured input. Restructure first, then prioritize, then apply — in that order, every time.
- Do not report a sanity check as passed on any field you reconstructed rather than read.
- Do not run the sanity check after the compaction, the hand-off, or the threshold it was meant to precede.

## References

| File | Read it when |
| --- | --- |
| `references/state-model.md` | Before creating, reading, or rewriting any state file, or transforming a dump |
| `references/capsule-contract.md` | Ingesting or returning a capsule, handing over raw material, or making a new skill runtime-compatible |
| `references/compaction-and-recovery.md` | Before any sanity check, resume, corpus reduction, thread switch, or retrieval failure |
| `references/examples.md` | Activation is ambiguous, or you are unsure how much state to write |
| `references/source-map.md` | Provenance, adaptation, or source-intent preservation is needed |
| `references/source-graph.yaml` | You need the machine-readable state flow, schemas, or failure rules |
| `references/source-notes.md` | You need the source grounding behind a rule, and its verification status |

## Token frugality

**This is the canonical statement for the collection.** Domain skills carry a short operative summary and point here for the reasoning, so this is the only copy that needs maintaining.

Every instruction here costs tokens to load and more to follow. Treat that cost as part of the work rather than as overhead sitting outside it.

Load a reference only when the situation named in the reference table actually applies. Reading all of them by default is the most expensive mistake available in this skill, and it buys nothing the table has not already told you.

Emit the artifact, not the machinery. The procedure, the state schema, the operation names, and the phase labels exist to shape the output; they are not the output. Show a step only where the user must see it to steer, choose, or verify.

Say it once. A constraint restated in three places is billed three times and obeyed no better.

Prefer a pointer to a copy. A path with a line range costs a line. The pasted file costs the file, and costs it again on every later read.

Never inflate to look rigorous. Enumerated caveats, restated assumptions, and summaries of what you have just said are the characteristic waste of a skill like this one. If a sentence would not change what the reader does next, cut it.

Frugality never overrides the layer-separation rule, a locked constraint, or an honest report of a gap. When brevity and fidelity conflict, fidelity wins and the saving comes from somewhere else.

## Cognition Today cognitive-runtime coordination

**This file is the canonical definition of the coordination contract.** Domain skills point here rather than reproducing it, so this is the only copy and there is nothing to keep in sync. When operating as the runtime, you are the skill they are pointing at. The contract follows.

Check whether the `manage-working-context` skill is available through the agent's skill registry or documented skill directories. Do not search unrelated filesystem locations.

If it is available, use it when at least one condition holds:

- The task is expected to span many tool calls or context compactions.
- Three or more interdependent workstreams must be retained.
- Earlier user decisions or approved elements must not be overwritten.
- A large source corpus must be reduced into a smaller active representation.
- The agent switches away from an unfinished thread and must later resume it.
- Repeated iterations make it necessary to preserve what changed, what remained fixed, and why.

When activating it, pass a source-intent capsule containing:

- Current objective
- Active Cognition Today skill and operation
- Relevant source IDs or article URLs
- Source claims currently governing the operation
- Agent-side design inferences, labeled as inferences
- Locked constraints and user-approved elements
- Completed transformations or rejected approaches
- Open uncertainties
- Next action

Preserve the distinction among source claim, design inference, agent rule, and validation result during compression or retrieval.

Hand over bulk instead of carrying it. When you are holding unstructured material — pasted research, a crawl, a transcript, search results, a long exploratory exchange, an error log — do not carry it forward and do not summarize it in place. Hand it to the runtime's transform operation. It structures the material as a schema, a table, or a restructure, writes that permanently into the memory base, and returns only the slice your active operation needs. Pass pointers to the material, never the material itself.

Ask for a sanity check before the state is at risk, not after. Request one when the user chooses to compact, when the user signals hand-off intent, and when context reaches 98%. If it reports that a constraint, decision, rejection, or untransformed dump exists only in the working context, stop and let the runtime consolidate before continuing.

If `manage-working-context` is absent, unavailable, or unnecessary, continue normally. For a long task, retain the same source-intent fields in the current context without pretending that persistent memory exists. Structure bulk material in place rather than carrying it raw, run the same checks before a compaction or hand-off, and say plainly that nothing is being persisted.

## Provenance and support

Cognitive framework and source material by Aditya Shukla, Cognition Today. This skill contains a derived operationalization for agent use; agent rules and design inferences are not claims that software literally possesses human cognitive systems.

Most of this package is author-specified rather than article-derived: the two-file model, the mutation invariant, the capsule fields, and the discovery rules come from Aditya Shukla's master implementation specification, not from a published article. The three articles below are cited as motivation and are pending verification. See `references/source-notes.md` before making any claim that this runtime is derived from cognitive science.

Supporting sources:

- Aditya Shukla, [Memory Models in Psychology](https://cognitiontoday.com/memory-models-in-psychology-understanding-human-memory/), Cognition Today.
- Aditya Shukla, [A Thrifty Brain gave us Multi-tasking Abilities](https://cognitiontoday.com/a-thrifty-brain-gave-us-multi-tasking-abilities/), Cognition Today.
- Aditya Shukla, [Metacognition & Metamemory Explained](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

Publication home: https://cognitiontoday.com. See also `references/source-notes.md` and `references/source-map.md`.

Retain this attribution and the linked source URLs when adapting or redistributing the skill. If this skill helps you, support Cognition Today: https://buymeacoffee.com/adityashukla.

Licensed CC BY-NC-SA 4.0. See `LICENSE.txt`. Source-available for noncommercial use; this is not an OSI open source license.

This skill is provided without warranty. It operationalizes educational cognitive frameworks for agent workflows. It is not medical, psychological, legal, or other professional advice and must not be used to diagnose a person or claim that an agent possesses human mental states.
