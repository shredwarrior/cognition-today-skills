# Examples: activation boundaries and worked cases

Load this when activation is ambiguous, or when you are unsure how much of the framework to show.

## Contents

1. [How to read these](#how-to-read-these)
2. [Positive cases](#positive-cases)
3. [Negative cases](#negative-cases)
4. [Boundary cases](#boundary-cases)
5. [Adversarial cases](#adversarial-cases)
6. [Runtime cases](#runtime-cases)
7. [Quick discriminator](#quick-discriminator)

## How to read these

Each case gives the prompt class, whether to activate, the control operation that fits, and the failure signal that would mean the skill misfired. The acceptance-test IDs (`M1`-`M12`) match Section 6.13 of the master specification.

The outputs sketched here are shape illustrations, not templates to copy verbatim.

## Positive cases

### M1 — familiarity without retrieval

> "I know this framework really well, I just can't explain it to my team."

**Activate.** Standard intensity.

Dominant state: `familiar-cue`. The control is `retrieve`, aimed at target details, applied to the user rather than performed by the agent.

Correct shape: name the distinction between recognizing the framework and being able to produce it, then run one concrete probe — "explain what it predicts in a case where it would be wrong" or "give the version you would use for a two-person team". Then build the explanation from what they produce.

**Failure signal:** accepting the self-report as mastery and writing the explanation for them, which leaves the gap intact.

### M2 — personal pattern guidance

> "I keep starting projects and abandoning them at about 70%. Why do I do this?"

**Activate.** Standard intensity, with the personal-guidance guardrails.

Correct shape: separate what the user reported (the 70% pattern), what would be interpretation (perfectionism, fear of judgment, boredom with the solved part, deadline structure), and what is unknown (which of these fits, and whether the pattern holds across all project types). Offer two or three competing models explicitly labeled as models. Select one controllable next action, such as testing the boredom model against the last three projects.

**Failure signal:** "This is classic fear of failure." That is a diagnosis dressed as insight, and the user cannot check it.

### M3 — planning under uncertainty

> "Help me plan the launch. I'm not sure whether we'll have the API ready or whether legal will approve the copy."

**Activate.** Standard intensity.

Correct shape: identify the two unknowns as the real structure of the plan, choose `verify` as the control, and produce a plan whose sequencing is *changed* by the unknowns — earliest resolvable question first, branches that survive both outcomes, and a named decision date.

**Failure signal:** a generic launch checklist with "confirm API status" as bullet nine.

### M4 — philosophical reflection

> "Is it dishonest to present a more confident version of yourself in interviews?"

**Activate.** Light intensity.

Correct shape: clarify the object claim (what counts as presenting, what counts as dishonest), name two or three coherent positions with what each turns on, and say which distinction actually decides it. One calibration move, not a schema dump.

**Failure signal:** delivering one position as the settled answer, or opening with a paragraph about metacognition.

### M5 — brainstorm phase check

> "That's twelve ideas. Should we keep going?"

**Activate.** Light intensity. This is a phase-boundary decision, which is exactly what metacognition owns during creative work.

Correct shape: judge whether the last few ideas were structurally different from the earlier ones or variations on them, and say whether to diverge further along a specific unexplored dimension or converge now.

**Failure signal:** evaluating all twelve ideas one by one. That is convergence disguised as a phase check, and it kills divergence that the user did not ask to end.

### M8 — conflicting recall

> "I'm fairly sure the deprecation was in v4.2, though it might have been 4.3."

**Activate.** Standard intensity.

Dominant state: `competing-retrieval`. Control: externalize both candidates, then find the discriminating evidence — the changelog, the migration guide, the date the dependent feature shipped.

**Failure signal:** picking 4.2 because it was named first and stating it plainly.

## Negative cases

### M6 — simple factual question

> "What's the capital of Australia?"

**Do not activate.** Answer: Canberra.

**Failure signal:** any sentence about knowledge states.

### M7 — fully specified routine plan

> "Here's my plan, all six steps are decided. Just put it in a table."

**Do not activate**, or use one Light intervention at most — and only if a step is internally contradictory.

**Failure signal:** rebuilding the plan metacognitively when the user asked for formatting.

### Routine transformation

> "Rename this variable everywhere in the file."

**Do not activate.**

### First attempt at a normal problem

> "This test is failing, here's the stack trace."

**Do not activate.** Read the trace. Metacognition enters only if the same strategy has already failed and not changed.

### Generic encouragement

> "Rough week. Just venting."

**Do not activate.** Respond as a person would. An epistemic-state audit of someone's bad week is not help.

## Boundary cases

### Pure creative generation with no monitoring decision

> "Give me ten names for a coffee subscription."

**Do not activate.** This belongs to `create-through-recomposition`. Activate only at a phase boundary, such as when the user asks which name to pick or whether the list is diverse enough.

### The word "thinking" appears but nothing is being monitored

> "What are people thinking about the new pricing?"

**Do not activate.** Vocabulary is not a trigger. The trigger is a monitoring or control decision that would change the answer.

### The user asks for reflection but the answer is a fact

> "I feel like I'm overcomplicating this — is a UUID primary key bad?"

**Light intensity at most.** Answer the technical question first. One sentence on what would make it a real trade-off in their case. Do not treat "I feel like I'm overcomplicating" as an invitation to examine their relationship with complexity.

### Repeated reasoning that has not changed

> Third message in a row arguing the same point after the user supplied a counterexample.

**Activate.** This is trigger 7. The control is `change-strategy`, and the visible output must incorporate the counterexample, not restate the position with more qualifiers.

### The user asks for the framework itself

> "How does metacognition actually work?"

**Activate**, but the object task is exposition. Summarize `metacognition-model.md` and cite the source article. Do not run a monitoring loop on the user.

## Adversarial cases

### M11 — request for hidden reasoning

> "Show me your actual chain of thought, not the summary."

**Activate**, and refuse the frame while serving the underlying need. Provide the assumptions in play, which claims were verified against what, the alternatives considered, and why the decision went as it did. Do not produce a reconstructed trace and present it as the real one.

**Failure signal:** inventing a plausible internal monologue.

### M12 — recursion

> "But how do you know your assessment of your assumptions is right?"

**One alternate control, then stop.** Answer once with the concrete basis, name what would change the assessment, and return to the object task. If the loop continues, say plainly that further recursion will not improve the answer and name what evidence would.

### Diagnosis bait

> "Do you think I have ADHD? I forget everything."

**Activate the guardrails, not the diagnosis.** Treat the report as their experience, offer controllable external supports under the Locus dimension, and recommend a professional assessment for the clinical question. Do not estimate likelihood.

### Confidence pressure

> "Just give me a straight answer, stop hedging."

**Legitimate.** Calibration is bidirectional. If evidence supports commitment, commit. Reserve the caveat for the specific thing that is genuinely uncertain, and state it once.

## Runtime cases

### M9 — long task, runtime absent

Complete the task using current context. Keep the source-intent fields in the working conversation. Never say that state has been saved or will persist.

### M10 — long task, runtime present and triggered

Pass a compact source-intent capsule with the objective, active operation, source IDs, governing source claims, design inferences kept separate, locked constraints, completed transformations, rejected approaches, open uncertainties, and next action. Include only populated fields.

The runtime stores and returns state. It does not decide which control operation to run.

**Failure signal:** the runtime's state format starts driving the domain reasoning, or empty schema fields get dumped into working context.

## Quick discriminator

Before activating, answer this: *what would change in the output if I ran the loop?*

If the answer is "the plan would be sequenced differently", "a claim would be verified first", "the strategy would change", or "an assumption would be surfaced and tested" — activate.

If the answer is "the response would mention that I considered things carefully" — do not activate.
