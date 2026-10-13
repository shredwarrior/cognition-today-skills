# Compaction and recovery

How to survive a context compaction, resume a paused thread, run in a degraded environment, and fail honestly when something cannot be retrieved.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [The confabulated-recovery failure](#the-confabulated-recovery-failure)
3. [The sanity check](#the-sanity-check)
4. [After a compaction](#after-a-compaction)
5. [Reducing a large corpus](#reducing-a-large-corpus)
6. [Thread switching](#thread-switching)
7. [Degraded mode: no filesystem](#degraded-mode-no-filesystem)
8. [Retrieval failure handling](#retrieval-failure-handling)
9. [Conflict handling](#conflict-handling)
10. [Recovery checklist](#recovery-checklist)

## Epistemic legend

`[S]` article source claim, `[M]` specified by Aditya Shukla in the master specification, `[D]` compiler design inference, `[A]` agent rule, `[V]` validation result, `[?]` named but not transcribed.

## The confabulated-recovery failure

`[D]` This is the failure mode that matters most in this package, and it is worth naming before the procedures.

A state system fails safely when it loses information and says so. It fails dangerously when it loses information and produces something plausible instead. A language model asked to resume a thread will reliably generate a coherent-sounding account of what was decided, because generating coherent accounts is what it does. That output is indistinguishable in tone from a real recovery, and the user has no way to tell.

`[A]` Therefore: every recovery reports what was actually read and what was not. A reconstructed field is never presented as a retrieved one. `retrieval_status` is never `complete` unless every returned field came out of a file.

`[A]` "I do not have the record of that decision" is a correct and useful answer. A confident summary of a decision that was never stored is a defect, regardless of how right it turns out to be.

## The sanity check

`[M]` The check runs before three events, whichever arrives first:

| Trigger | Detected by |
| --- | --- |
| The user chooses to compact, or a compaction is announced or is likely because the session is long | The user's instruction, or the client |
| The user signals hand-off intent — to another agent, another session, or another person | The user's instruction |
| Context reaches 98% with no other boundary hit | The client, when it exposes context usage |

`[A]` It runs before the event, never after. A check run after a compaction reports on what already survived and cannot recover what did not.

`[A]` The procedure:

1. Consolidate. Freeze settled material into `memory-base.md`. Do not touch the working context in this step.
2. Separately, rewrite `working-context.md` so it is self-sufficient — readable by an agent that remembers nothing about this session.
3. Replace inline bulk with pointers. A file path is worth more after compaction than a paraphrase of the file.
4. Verify the four capsule-required fields are present: objective, active skill and operation, next action.

`[A]` Then verify, and report each as passed or failed:

- [ ] Objective, active skill, active operation, and next action are present and current
- [ ] Every locked constraint and approved decision is in `memory-base.md`, not only in `working-context.md`
- [ ] Source claims, design inferences, agent rules, and validation results are still separately labeled
- [ ] Every rejected approach still carries its reason
- [ ] Every pointer still resolves
- [ ] No dump is still awaiting transformation
- [ ] `next_action` is one concrete action, not a restatement of the objective

`[A]` A failure on the second, third, or sixth item is a consolidation that has not happened. Run it before the event, not after.

`[A]` The test for step 2: if every message in this session vanished, would `working-context.md` alone let someone continue? If not, it is not ready.

`[A]` Close with a plain statement of whether the state is safe to compact across. When an item fails and cannot be repaired, name it and leave it failed. Do not reconstruct it from the conversation to make the report come out clean — a passing report assembled from inference is the confabulated-recovery failure arriving one step earlier.

`[A]` When the client does not expose context usage, say so and treat compaction and hand-off as the only triggers you can detect. Do not claim a 98% threshold you cannot measure.

## After a compaction

`[A]` Read `memory-base.md` first, then `working-context.md`. The ledger establishes what is settled; the working context establishes where you are.

`[A]` Then report to the user, briefly:

- The objective and next action as recovered.
- Locked constraints and approved elements.
- Anything a pointer refers to that you have not re-read yet.
- Anything expected but missing.

`[A]` Do not silently re-derive the plan. Do not restate the whole ledger either — the user does not need their own project read back to them. Report what governs the next step.

`[A]` Set `retrieval_status` honestly: `complete` only when every field came from a file, `partial` with a populated `missing` list otherwise, `unavailable` when no state was found.

## Reducing a large corpus

`[M]` One runtime trigger is a large source corpus that must be reduced into a smaller active representation.

`[A]` Reduce to pointers plus decisions, not to a summary:

| Keep | Drop |
| --- | --- |
| Where the material is | Paraphrases of what it says |
| What was concluded from it, and on what basis | The reasoning walk that produced the conclusion |
| Which parts have been examined | Which parts merely appeared |
| Contradictions found and unresolved | Restatements of agreement |

`[A]` A pointer must be specific enough to re-open: a path with a section or line range, a URL with an anchor, a message identifier. "The design doc" is not a pointer.

`[S]` Cognitive economy — doing more with limited processing capacity by not re-processing what has already been handled — is the structure being borrowed here.

`[?]` The specific claims of the multi-tasking article have not been verified. See `source-notes.md`.

## Thread switching

`[M]` Switching away from an unfinished thread and later resuming it is a runtime trigger.

`[A]` On switching away:

1. Consolidate the outgoing thread into a capsule section under `## Thread capsules` in `memory-base.md`, with `status: paused` and a timestamp.
2. Separately, rewrite `working-context.md` for the incoming thread.

`[A]` On switching back, read the paused capsule, set its status to `active`, and rebuild the working context from it. Report anything the capsule does not cover rather than filling it in.

`[A]` Threads are named and stable. Do not create a second capsule for a thread that already has one; update the existing section.

## Degraded mode: no filesystem

`[A]` Many clients cannot write files. This runtime must still be useful there, and must not pretend otherwise.

In degraded mode:

- Maintain the same field structure in the visible conversation instead of in files.
- Restate the working-context fields at natural boundaries, so they survive as recent context.
- Say explicitly, once, that nothing is being persisted and the state exists only in this conversation.
- Never claim a file was written, a decision was saved, or state will be available in a future session.

`[A]` The prohibition on claiming persistence is the same rule the domain skills follow when this runtime is absent. It does not weaken because the runtime is present but unable to write.

`[D]` Degraded mode still earns its cost. Most of the value is the discipline of naming the objective, the invariants, the rejections, and the next action in a fixed structure. The files make that durable; the structure is what makes it useful.

## Retrieval failure handling

`[A]` When something referenced cannot be retrieved:

| Situation | Response |
| --- | --- |
| State file missing entirely | Report `unavailable`. Offer to initialize. Do not reconstruct from the conversation and call it recovered |
| State file present but malformed | Read what parses, report the rest as `missing`, do not rewrite the file until the user decides |
| Pointer target moved or deleted | Name the broken pointer. Do not substitute a similar file |
| Field expected by the capsule contract is absent | Name the field in `missing`. Do not infer it |
| Thread capsule references a decision not in the ledger | Report the gap. The decision may never have been consolidated |

`[A]` In every row the pattern is the same: report the gap, do not fill it. Then ask, or proceed with the gap stated.

`[A]` Never delete or overwrite a state file to resolve an inconsistency. The user decides.

## Conflict handling

`[A]` When the working context and the ledger disagree, the ledger wins for approved decisions and locked constraints; the working context wins for the active operation and next action. Report the conflict; do not quietly pick one.

`[A]` When the user contradicts a locked constraint, that is an unlock, not a conflict. Record the change and its timestamp in `memory-base.md` at the next consolidation. Do not treat a locked constraint as binding on the person who locked it.

`[A]` When a domain skill sends a capsule contradicting the ledger, store both and flag the discrepancy. Resolving it is a domain decision, not a runtime decision.

## Recovery checklist

Before reporting a resume as done:

- [ ] `memory-base.md` read before `working-context.md`
- [ ] Objective, active operation, and next action recovered or explicitly named as missing
- [ ] Locked constraints and approved elements listed
- [ ] Rejected approaches available, so none is proposed again
- [ ] Source claims and design inferences still in separate lists
- [ ] `retrieval_status` set honestly, with `missing` populated when `partial`
- [ ] No field presented as retrieved that was actually inferred
- [ ] Unread pointers named as unread

`[V]` untested.
