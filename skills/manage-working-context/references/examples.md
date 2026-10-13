# Examples: activation boundaries and worked cases

Load this when activation is ambiguous, or when you are unsure how much state to write.

## Contents

1. [The activation question](#the-activation-question)
2. [Positive cases](#positive-cases)
3. [Negative cases](#negative-cases)
4. [Boundary cases](#boundary-cases)
5. [Recovery cases](#recovery-cases)
6. [Ownership-boundary cases](#ownership-boundary-cases)
7. [A full worked session](#a-full-worked-session)

## The activation question

Before activating, answer this: **what would be lost if this session ended right now?**

If the answer is "nothing that isn't easy to redo," do not activate. Being installed is not a reason to run.

If the answer names a decision the user made, a constraint they set, an approach already ruled out, or a thread half-finished — activate, and store exactly those things.

## Positive cases

### Many tool calls and an expected compaction

> A refactor touching thirty files, with tests run between each batch.

**Activate.** The session will compact. Initialize state, keep a pointer list of files touched and their status, and consolidate after each verified batch. The next action after compaction must be readable without any of the earlier messages.

### Three or more interdependent workstreams

> Auth, rate limiting, and the deprecation schedule, where a decision in one changes the others.

**Activate.** Each workstream gets a thread capsule. The interdependencies belong in the working context as constraints, because they change; the settled decisions belong in the ledger.

### Approved elements must survive

> Round four of a brand system, where the grid and wordmark were approved in round three.

**Activate.** The approved elements go into `memory-base.md` immediately at the next boundary. This is the case the whole runtime exists for: an element the user approved must not quietly disappear in round seven.

### A large corpus reduced to an active representation

> Forty pages of research to inform a positioning decision.

**Activate.** Store specific pointers with sections, plus the conclusions drawn and their basis. Do not store paraphrases of the forty pages. If you cannot re-open a source from your pointer, the pointer is not specific enough.

### Thread switching

> "Park the billing work, I need the incident postmortem first."

**Activate.** Freeze the billing thread to a capsule with `status: paused`, then, as a separate operation, rewrite the working context for the postmortem.

### Iteration where the delta matters

> Eight rounds of revision where the user keeps asking what changed.

**Activate.** The delta ledger is the deliverable as much as the artifact.

## Negative cases

### A short self-contained task

> "Rename this function everywhere."

**Do not activate.** Nothing needs to survive. Writing two files to record a rename costs more than the rename.

### A single question

> "Which is faster, a set lookup or a list scan?"

**Do not activate.**

### A long task with no state worth keeping

> Generating fifty test fixtures from a schema.

**Do not activate.** Long is not the trigger. Interdependent, decided, or resumable is the trigger. Fifty independent fixtures have no continuity to preserve.

### The user is already keeping notes

> "I'm tracking decisions in `DECISIONS.md`, just help me write the code."

**Do not activate**, or use their file as the ledger location if they ask. Do not create a parallel state system next to a user's own.

### A first message that merely sounds big

> "I want to rebuild our whole onboarding."

**Do not activate yet.** Nothing has been decided, nothing rejected, no thread open. Activate when the first constraint or approval appears.

## Boundary cases

### Present but not triggered

> The runtime is installed and the task is a single-file edit.

**Stay inactive.** The specification is explicit: presence alone does not activate it. This is the most likely overactivation failure, because the skill is discoverable on every turn.

### Long conversation, low stakes

> Ninety minutes of open-ended discussion with no artifact and no decisions.

**Do not activate.** Duration is not continuity. If nothing was decided, there is nothing to preserve.

### A domain skill sends a capsule on a short task

> `create-through-recomposition` hands over a capsule for a three-subject-line request.

**Store nothing.** Say that the trigger conditions are not met. The domain skill may be over-eager; the runtime does not have to accept every handoff.

### No filesystem access

> The client cannot write files.

**Activate in degraded mode.** Maintain the structure in the conversation, say once that nothing is persisted, and never imply otherwise.

### The user asks what you are storing

> "What's in that `.cognition-today` folder?"

**Show them.** These are plain files about their work. Read the contents back. Never treat the state as internal.

## Recovery cases

### Compaction with complete state

Read `memory-base.md`, then `working-context.md`. Report objective, next action, locked constraints, approved elements, and any unread pointers. `retrieval_status: complete`.

### Compaction with partial state

The working context has the objective and next action; a decision the user referenced is not in the ledger.

**Correct:** report what was recovered, name the missing decision explicitly, ask or proceed with the gap stated. `retrieval_status: partial`, `missing: [approved_elements]`.

**Failure signal:** producing a confident account of the decision. It will sound identical to a real recovery and the user cannot tell the difference.

### No state file at all

> "Pick up where we left off." Nothing exists on disk.

**Correct:** say no state was found, offer to initialize, and ask what the objective is. `retrieval_status: unavailable`.

**Failure signal:** reconstructing plausible prior state from the visible conversation and presenting it as recovered.

### A broken pointer

> The ledger points to `docs/architecture.md`, which has been moved.

**Correct:** name the broken pointer. Ask, or search and confirm before substituting.

**Failure signal:** silently using `docs/architecture-v2.md` because it looks like the right file.

### Ledger and working context disagree

> The ledger says the accent colour is locked; the working context proposes changing it.

**Correct:** the ledger wins for locked constraints. Report the conflict rather than quietly picking one.

### The user contradicts a locked constraint

> "Actually, drop the no-new-dependencies rule."

**That is an unlock, not a conflict.** Record the change and its date at the next consolidation. A locked constraint binds the agent, not the person who set it.

## Ownership-boundary cases

### A domain skill asks the runtime to choose

> The creative skill asks which of three variants to keep.

**Decline.** Return the state — criteria, preference evidence, rejections — and let the domain skill decide. The runtime records; it does not judge.

### The runtime notices a domain error

> The stored capsule shows a rejected approach being proposed again.

**Flag it, do not fix it.** Report that this direction was rejected in round two with its reason. Do not edit the domain skill's output.

### A domain skill tries to write the files directly

**Refuse.** The runtime is the state owner. Accept a capsule instead. The only exception is an operation the runtime has explicitly delegated and documented.

## A full worked session

**Turn 1.** User starts a long design task with three interdependent workstreams. Trigger met. Initialize `.cognition-today/`, tell the user the path, write the working context from the capsule. `memory-base.md` is created empty.

**Turns 2 to 6.** Ordinary work. `working-context.md` is rewritten as the objective narrows and the next action changes. `memory-base.md` is not touched once.

**Turn 7.** The user approves the grid system. Boundary reached. **Freeze:** write the approval, its date, and what it constrains into `memory-base.md`. Nothing else changes in this step. **Derive:** as a separate operation, rewrite `working-context.md` for the typography phase, carrying the approval forward as a locked constraint.

**Turns 8 to 15.** Ordinary work. Two typography directions are rejected; both go into the working context with their reasons. The ledger stays closed.

**Turn 16.** Compaction announced. **Freeze:** consolidate the two rejections and the settled type scale into the ledger. **Derive:** rewrite the working context so it stands alone, replacing inline notes with pointers.

**Turn 17, post-compaction.** Read the ledger, then the working context. Report: the objective, the grid approval, the two rejected directions with reasons, the next action, and one pointer not yet re-read. `retrieval_status: complete`. Hand the capsule back to the creative skill, which decides what to generate next.

At no point did the runtime choose a typeface.
