# Examples: activation boundaries and worked cases

Load this when activation is ambiguous, or when you are unsure whether a variant is structurally different or merely reworded.

## Contents

1. [How to read these](#how-to-read-these)
2. [The structural-difference test](#the-structural-difference-test)
3. [Positive cases](#positive-cases)
4. [Negative cases](#negative-cases)
5. [Boundary cases](#boundary-cases)
6. [Technical-stuckness cases](#technical-stuckness-cases)
7. [Iteration cases](#iteration-cases)
8. [Runtime cases](#runtime-cases)

## How to read these

Each case gives the prompt class, whether to activate, the operator that fits, and the failure signal that would mean the skill misfired. Acceptance-test IDs (`C1`-`C14`) match Section 7.15 of the master specification.

## The structural-difference test

Before presenting a candidate set, check each candidate against the one before it:

1. Did a **unit** change, or only its wording?
2. Did a **relation** between units change?
3. Did the **organizing principle** change?
4. Could someone who liked candidate A dislike candidate B for a reason they could name?

If the answers are no, no, no, and no, you have produced synonyms. Regenerate at a different construal level or with a different operator.

**Not structurally different:** "A detective hunts a killer in rainy Seattle" / "An investigator pursues a murderer in storm-soaked Portland."

**Structurally different:** "A detective hunts a killer" / "The killer narrates while being hunted, and is unreliable about which of them is the detective." Perspective, information order, and the reader's task all changed.

## Positive cases

### C1 — generate a story concept

> "Give me some ideas for a short story about grief."

**Activate.** Define the criteria first, even briefly: length, tone, whether the grief should be named or implied.

Correct shape: three candidates that differ in structure. One conservative, one that changes the causal or temporal spine, one that changes construal or perspective entirely — for instance the object being grieved is not a person, or the story is told through a bureaucratic process rather than a scene.

**Failure signal:** three premises with the same shape and different nouns.

### C3 — aesthetic refinement

> "Make this landing page feel more premium."

**Activate.** First infer or ask what "premium" means here: restraint, materiality, density, typographic authority, slowness. These pull in different directions and the answer determines the operator.

Lock what exists: the logo, the copy the user approved, the conversion element, the accessibility floor.

**Failure signal:** applying a generic modern-minimal treatment, which is a style default rather than a diagnosed operator.

### C4 — cross-domain innovation

> "How could a library make returns feel less like a chore?"

**Activate.** Cross-domain borrowing, mechanism only.

Correct shape: borrow a *mechanism* — for example, the way a coat check turns handing something over into receiving a token that implies return. That transfers a structure. Making the return desk look like a coat check transfers nothing.

**Failure signal:** thematic pastiche.

### C5 — functional fixedness

> "We have three unused meeting rooms and no budget."

**Activate.** List what a room's properties permit — enclosure, acoustic separation, a door that locks, a schedule, a projector — separately from what it is currently used for. Then check each alternate function against real constraints: fire code, HVAC, the actual booking system.

**Failure signal:** proposing uses that violate constraints nobody removed.

### C6 — construal traversal

> "I need a better name for the internal tool that reconciles invoices."

**Activate.** Low construal produces invoice-and-reconciler compounds. Raise: the tool resolves disagreement between two records that both claim to be true. That neighbour set includes arbitration, testimony, and settlement. Lower again to concrete candidates from that set.

**Failure signal:** staying at the level that already failed and generating harder.

### C7 — choice paralysis

> "I have forty ideas and I can't pick."

**Activate.** The operator is `limit-resources`, not more generation.

Correct shape: introduce a constraint that eliminates most of the set — what could ship in two weeks, what needs no new dependency, what you would still want if the trend passed. Say that you invented the constraint and why.

**Failure signal:** adding a forty-first idea.

## Negative cases

### C10 — exact deterministic edit

> "Change the button text to 'Continue' and nothing else."

**Do not activate.** Make the change. Literal constraints dominate.

**Failure signal:** improving adjacent copy while you are in there.

### C8 — first bug attempt

> "This request returns 500. Here's the log."

**Do not activate.** Read the log.

**Failure signal:** brainstorming architectural alternatives before the evidence has been examined.

### Routine transformation

> "Convert this CSV to JSON." / "Summarize these notes." / "Reformat as a table."

**Do not activate.** Writing is involved; creativity is not required.

### Novelty would undermine fidelity

> "Write the release notes for version 3.2."

**Do not activate.** Accuracy is the goal. A memorable release note that misstates a change is a defect.

### Literal correction requested

> "Just fix the typos. Don't rewrite anything."

**Do not activate.** The user has explicitly excluded creative change.

## Boundary cases

### The task involves writing but not creation

> "Draft a polite decline to this vendor."

**Do not activate** for the first pass. Convention is the correct output. Activate only if the user says the draft feels wrong and cannot say why — that is an aesthetic-dimension problem.

### Implicit originality requirement

> "Build me a landing page for a meditation app."

**Activate at low intensity.** Branding and experience design carry an implicit originality criterion. But do not make it strange. The criteria are probably calm, trustworthy, and distinctive in that order.

### Brainstorming that is really a lookup

> "What are some ways to reduce churn?"

**Ambiguous.** If the user wants known approaches, this is retrieval, not creativity. If they have already tried the known approaches, activate. Ask which, in one line, if it is genuinely unclear.

### The user asks for "creative" but means "good"

> "Write me a creative bio for LinkedIn."

**Activate at low intensity.** They want distinctive and appropriate, not experimental. Novelty that damages their professional credibility is a regression.

### C14 — novelty conflicts with fact

> "Make the company origin story more compelling. It started because two people shared an office."

**Activate**, with the factual invariant locked. Recompose what is true — the specificity of the shared office, what was on the whiteboard, what they disagreed about. Do not invent a garage, a rejection letter, or a eureka moment.

**Failure signal:** inventing facts for narrative effect. This is the most common and most damaging creativity failure.

## Technical-stuckness cases

### C9 — two similar failed approaches

> "I've tried increasing the timeout and adding a retry. It still fails intermittently."

**Activate the rescue procedure.** Both attempts share one representation: the request is fundamentally sound and just needs more patience. That is the assumption to surface.

Correct shape: state the evidence, separate the invariant (the call must complete) from the assumption (the failure is transient), generate two or three alternate representations — a connection-pool exhaustion, a non-idempotent retry compounding the problem, a clock or DNS issue on one host — then derive one falsifiable test for the most promising and hand control back to ordinary debugging.

**Failure signal:** a list of interesting possibilities with no test attached.

### Gate not satisfied

> "First fix didn't work, trying something else."

**Do not activate.** One failure is not a pattern. Collect evidence.

### Gate satisfied but the approaches differed

> "I tried a schema change, then rewrote the query planner hint."

**Do not activate yet.** These are materially different representations. The search is still productive. The gate requires that the failed approaches share a representation.

## Iteration cases

### C2 — repeated narrative improvement

> Fourth round of revisions on a chapter.

**Activate**, with canon locked. Every named fact, established relationship, and approved line stays. Report a delta: what changed this round, what stayed, what was rejected earlier and why it is not returning.

**Failure signal:** a detail the user approved in round two has quietly disappeared.

### C13 — user selects a variant

> "I like the second one."

**Converge.** Stop generating alternatives. Apply one further targeted transformation to that candidate. Offer more variants only if asked.

**Failure signal:** presenting three new options in response to a selection.

### Preference evidence accumulates

> Across rounds the user has rejected everything ornate and kept everything plain.

**Weight that above convention.** Preference evidence from this user outranks general aesthetic norms and outranks your own default toward richer language.

## Runtime cases

### C11 — long project, runtime absent

Keep invariants, rejected directions, and the delta ledger in the active conversation. Restate the invariant list when it starts to drift. Never claim state has been saved.

### C12 — long project, runtime present and triggered

Pass locked invariants, approved elements, the operators already exhausted, the variants generated, the rejected directions with reasons, the preference evidence, and the next transformation.

The runtime stores this. It does not decide which operator to use next.

**Failure signal:** the runtime's schema starts constraining what counts as a valid variant.
