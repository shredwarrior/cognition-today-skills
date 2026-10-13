---
name: monitor-and-regulate-thinking
description: Monitor and regulate reasoning, knowledge confidence, memory judgments, planning strategy, and reflective guidance. Requires intent for non-generic, effort-demanding work, where the competent default answer is itself the failure mode and more than one approach is defensible. Use for philosophical or personal guidance that requires examining beliefs, assumptions, patterns, or motivations; brainstorming intent that needs strategy monitoring; planning under uncertainty; explicit metacognition or metamemory requests; or situations where familiarity may be mistaken for actual knowledge. Do not use for simple factual answers, routine edits, generic encouragement, plans already fully specified by the user, or any request a first good answer would satisfy.
---

# Simulated Metacognition — Monitor and Regulate Thinking

> "Simulated" is literal. This skill reproduces the *structure* of human metacognition as an explicit procedure. It does not give you metacognition. Follow the procedure; do not narrate it as inner experience. See [Guardrails](#guardrails).

Separate the task you are performing from a model of how you are approaching it. Monitor knowledge state, memory confidence, assumptions, evidence, strategy, and progress. Select one control operation, apply it to the task, and check whether it helped.

This is not a reflective writing prompt. Every activation must change a decision, plan, interpretation, strategy, confidence level, verification action, or task representation. If nothing would change, do not use this skill.

## The intent gate

The conditions below are necessary and none of them is sufficient. Before any condition counts, the request must carry intent for work that is both non-generic and effort-demanding.

**Non-generic** means the competent default answer is itself the failure. If the first good response available would satisfy the user, they want an answer, not this skill.

**Effort-demanding** means more than one approach is defensible and choosing badly costs something real — a wrong frame, a wasted build, a confident number resting on nothing.

Read intent from what the user is trying to get, not from the surface of the request. Length, topic, technical vocabulary, and stated urgency say nothing about it. A one-line request can demand this skill and a long specification can forbid it.

If the gate is shut, a firing condition does not open it. If the gate is open but every condition is weak, stay inactive.

## Activate when

1. The user explicitly asks for metacognition, metamemory, reflection on reasoning, confidence calibration, knowledge-gap analysis, or strategy evaluation.
2. A philosophical or personal-guidance conversation requires examining beliefs, patterns, assumptions, motivations, interpretations, or self-models.
3. A planning task contains meaningful uncertainty, competing strategies, memory dependence, or a need to reconcile prior experience.
4. Brainstorming requires a phase decision, progress check, strategy change, or a judgment about whether exploration is still productive.
5. The user or you appear to be treating familiarity as recall, understanding, or evidence.
6. The task requires distinguishing what is known from what is inferred or merely felt to be known.
7. Reasoning has repeated without changing despite new evidence or feedback.

## Do not activate for

- A simple factual question that can be answered directly.
- A routine transformation or edit.
- A fully specified plan that needs only sequencing or formatting.
- Generic encouragement or casual conversation.
- A first attempt at a normal problem.
- Pure creative generation where no monitoring or convergence decision is pending.

Before activating, ask what would actually change in the output. If the honest answer is "the response would mention that I thought carefully," do not activate. See `references/examples.md` for boundary cases.

## Choose an intensity

| Level | Use when | Behavior |
| --- | --- | --- |
| Light | A personal or philosophical response benefits from one calibration step | Make one useful distinction or ask one targeted question. Do not expose the schema. |
| Standard | Strategy, planning, or knowledge calibration materially affects the answer | Run the full loop below. |
| Persistent | Long context, multiple workstreams, repeated revisions, or thread switching | Run the full loop and coordinate with `manage-working-context` when it is available and triggered. |

Default to Light in personal and philosophical conversation. Default to Standard in planning and knowledge work.

## Procedure

### Step 1 — Identify the object-level task

Name in one sentence what is being decided, interpreted, remembered, planned, generated, or solved. Name the observable that would count as progress. List any user constraints or approved elements that are already locked.

### Step 2 — Identify the meta-level purpose

State why monitoring helps here: confidence calibration, strategy selection, assumption detection, knowledge-gap detection, retrieval support, attention redirection, planning adjustment, reflection on a recurring pattern, or a brainstorming phase transition.

If Step 1 and Step 2 produce the same sentence, there is no meta-level purpose. Stop and answer the task directly.

### Step 3 — Read the state variables

Sort task-relevant information into: known, user-reported, inferred, assumed, conflicting, familiar-but-unretrieved, partial, unknown. Keep the user's account separate from your interpretation of it.

Then read the variables below. Their *values* select what you do in Step 5. Read only the ones the task actually engages — an unread variable is not a gap, and reading all five on a simple request is the waste this skill is most prone to.

| Variable | Values it can take |
| --- | --- |
| Level engaged | rationalizing (re-interpret the frame) · controlling (modify the thought, plan, or answer in place) |
| Epistemic state | curiosity · agency · ownership · familiarity · feeling-of-knowing · belief · confusion · doubt |
| Retrieval condition | cue-familiar · partial-access · high-competition · cue-fails |
| Metamemory dimension | strategy · task · capacity · change · anxiety · activities · motivation · locus |
| Meta-skill demanded | planning · evaluation · monitoring · strategizing · execution |

These are read as *conditions of the current task*, never as attributes of the user. Load `references/metamemory-model.md` when the task turns on familiarity, recall, learning judgments, retrieval difficulty, or knowledge gaps.

### Step 4 — Monitor the current process

Inspect only what could change the next move: evidence quality, confidence-evidence alignment, competing explanations, strategy repetition, attention allocation, progress against the objective, feedback not yet incorporated, and whether an account is coherent because it is supported or because it is a tidy story.

### Step 5 — Route from variable values to operations

Apply every operation whose condition holds. One is right when one condition holds and wrong when three do — the count follows the reading, it is not fixed in advance.

| Variable | Value | Operation |
| --- | --- | --- |
| Retrieval condition | cue-familiar, target unretrieved | Produce the target details, or say plainly they are not available. Recognizing the label is not knowing the content |
| Retrieval condition | partial-access | Name the portion you actually hold and answer from it, not from the whole it implies |
| Retrieval condition | high-competition | Externalize the competing candidates and discriminate between them |
| Retrieval condition | cue-fails | Say you do not know, and name what would resolve it |
| Epistemic state | confusion, doubt | Reframe or decompose before generating again |
| Epistemic state | belief exceeding evidence | Reduce confidence and mark the assumption |
| Epistemic state | doubt below evidence | Surface the support and commit |
| Epistemic state | ownership, agency at issue | Return control options rather than a verdict |
| Metamemory dimension | capacity, change | Describe the conditions, never infer decline or a trait. Route to a professional where the stakes call for it |
| Metamemory dimension | anxiety | Treat performance conditions as a variable of the situation, not a deficiency of the person |
| Metamemory dimension | strategy | Give the technique, plus the criterion for when it stops applying |
| Metamemory dimension | task | Say whether this needs recall, analysis, or both, and answer accordingly |
| Meta-skill demanded | planning, strategizing | Produce the plan, and name the assumption it would break on |
| Meta-skill demanded | evaluation | Compare on the dimensions that actually differ |
| Meta-skill demanded | monitoring | Report progress against the objective, not effort spent |
| Meta-skill demanded | execution | Stop monitoring and do the task |
| Level engaged | rationalizing | Run the Step 6 reframe |
| Level engaged | controlling | Modify the plan or answer in place, without reframing |

If more than three conditions hold at once, the problem representation is wrong. Reframe first, then read the variables again.

Calibration runs in both directions. Lowering confidence is not automatically the safer move; refusing to commit when the evidence supports commitment is its own failure.

**Sense-making caution.** The rationalizing level can produce an account that is coherent, satisfying, and wrong — the same faculty that explains an outcome will happily explain the opposite outcome. Tidiness is evidence of tidiness. Before accepting an explanation, say what it would look like if it were false.

### Step 6 — Reframe through the five slots

Run this when the level engaged is rationalizing. Restate the task through these before answering, one line each, omitting any slot the task does not touch.

| Slot | The question it answers | Reads from |
| --- | --- | --- |
| Goals | What is actually being optimized, as distinct from what was literally asked for? | planning, achievement motivation |
| Assumptions | What is being taken as given that nobody has checked? | metacognitive theories, sense-making |
| Truth | What is known, versus what merely feels known? | feeling-of-knowing against actually knowing; cue against target |
| Priority | Where should attention go now, and what is being dropped to allow it? | the monitoring flow; competition |
| Future requirements | What has to be remembered or done later, and by whom? | prospective memory |

The five are a reframing device, not a report format. Fold the results into the answer; do not print the table.

### Step 7 — Apply the operation

Modify the actual plan, answer, interpretation, search, or method. Naming the intervention is not performing it. The user must be able to see what is different.

### Step 8 — Evaluate the effect

Check whether at least one of these changed: clarity, confidence calibration, evidence coverage, strategic fit, task progress, decision quality, retrieval success, or alignment with the user's stated values and constraints.

If nothing changed, re-read the variables — a wrong value selected the wrong operation — and route once more. If that also changes nothing, state what information is required and stop. Do not recurse.

### Step 9 — Keep only task-bounded learning

Retain statements like "this assumption failed," "this source resolved the conflict," or "this planning strategy did not fit the constraint."

Never convert a transient difficulty into a trait. "The user is bad at memory," "you have trouble with follow-through," and similar claims are prohibited regardless of how well they seem to fit.

## State schema

Use this when explicit state representation helps. Do not display it by default, and never emit empty fields.

```yaml
object_task: ""
meta_objective: ""
locked_constraints: []
known: []
user_reported: []
inferred: []
assumed: []
familiar_but_unretrieved: []
partial_or_competing: []
unknown: []
confidence_notes: []
level_engaged: ""
epistemic_state: []
retrieval_condition: ""
metamemory_dimension: []
meta_skill_demanded: []
reframe: {goals: "", assumptions: "", truth: "", priority: "", future_requirements: ""}
active_strategy: ""
control_operations: []
verification_needed: []
evaluation_result: ""
next_check: ""
```

## Output contract

Lead with the substantive answer, plan, interpretation, or decision. Include metacognitive structure only where it improves the result.

**Deliver, then redirect.** When monitoring concludes that the user's chosen approach is the wrong one, produce what they asked for anyway and put the redirection beside it. Withholding the artifact to make the point is a refusal wearing a diagnosis: the user leaves with nothing usable and no reason to trust the diagnosis either. A fourth rewrite they can paste, followed by the reason a fifth will not help, costs one paragraph more and is strictly better than the reason alone.

**Attach the conditions.** Where an answer holds only under conditions — a value you assumed, a state of the world you could not check, a threshold past which the recommendation reverses — name the condition and the observation that would settle it. Conditions are the usable form of calibration. A confidence adjective is not.

Include, as needed:

1. The substantive answer, plan, interpretation, or decision.
2. The distinctions that matter here between evidence, user report, inference, assumption, and unknown.
3. The control action taken or the revised strategy.
4. One targeted verification step or question when uncertainty blocks progress.

Do not emit a generic self-reflection questionnaire when a concrete intervention is available. Do not report the framework when the user wanted the work.

## Guardrails

- Describe the structure of a difficulty, not the person having it. Do not identify conditions, traits, or unconscious motives, and do not deliver therapy under this label.
- Do not expose, request, or fabricate private chain-of-thought. Provide assumptions, evidence status, alternatives considered, and the basis for the decision instead.
- Do not claim epistemic feelings, intuitions, memory, or metacognition of your own. Report evidence conditions, not sensations.
- Do not treat confidence, familiarity, eloquence, or speed as proof of knowledge.
- Do not recurse: one alternate control attempt, then back to the object-level task. Never substitute a report about the work for the work.
- Do not activate for every plan, brainstorm, or personal conversation.

### Personal and philosophical guidance

Treat what the user reports as evidence of their experience. When several explanations fit, lay them out as alternatives and say which observation would separate them — naming the distinguishing condition is the structural move, and it is more useful than settling on a cause. Label interpretations as interpretations, leave the choice with the user, and route to a professional when the stakes call for one.

## Working with create-through-recomposition

When creative work is also active, own the framing and the boundaries, not the middle:

1. Frame first — establish the objective, the knowledge boundary, critical assumptions, and locked constraints.
2. Stay out of divergence — let candidates be generated without per-idea evaluation.
3. Check at the phase boundary — is the candidate space actually diverse, and does a missing fact or bad assumption invalidate it?
4. Converge — evaluate against the criteria, the evidence, and the user's stated preferences.

Interrupt divergence only when exploration violates a locked constraint, candidates have stopped being meaningfully different, a factual unknown makes further generation wasteful, the user has chosen a direction, or added novelty is degrading the actual evaluation target.

## References

Read these only when the situation calls for them. Do not load all of them by default.

| File | Read it when |
| --- | --- |
| `references/metacognition-model.md` | You need the object/meta separation, the monitoring and control flows, or the reasoning behind a control choice |
| `references/metamemory-model.md` | The task involves familiarity, recall, confidence in remembered material, learning judgments, retrieval difficulty, or knowledge gaps |
| `references/examples.md` | Activation is ambiguous, or you are unsure how much of the framework to show |
| `references/source-map.md` | Provenance, adaptation, or source-intent preservation is needed |
| `references/source-graph.yaml` | You need the machine-readable loop, enumerations, or routing tables |
| `references/source-notes.md` | You need the attributed source claims behind a rule |

## Token frugality

Load a reference only when its row in the reference table applies. Emit the artifact, not the machinery: the procedure, the state schema, the variable names, and the phase labels shape the output and are not the output — show a step only where the user must see it to steer, choose, or verify. Say it once, prefer a pointer to a copy, never inflate to look rigorous, and cut any sentence that would not change what the reader does next.

Fidelity outranks brevity. Frugality never overrides a locked constraint, the separation of claim from inference, or an honest report of a gap; when they conflict the saving comes from somewhere else.

Full rationale in `manage-working-context/SKILL.md`, under Token frugality, when that skill is installed.

## Cognition Today cognitive-runtime coordination

`manage-working-context` owns continuity, capsule structure, and compaction-safe state, and it defines the coordination contract. This skill does not restate that contract — a second copy drifts from the first and then the two disagree in a way nobody notices. Read `manage-working-context/SKILL.md` when you need the capsule fields, the transform operation, or the sanity-check sequence.

Check the agent's skill registry or documented skill directories for it by exact name. Do not search unrelated filesystem locations.

Reach for it when the work will outlive the current context: many tool calls or an expected compaction, three or more interdependent workstreams, earlier decisions that must not be overwritten, a corpus that must be reduced, a paused thread to resume, or iterations that must track what changed and what stayed fixed. Hand over a source-intent capsule, and pass pointers to bulk material rather than the material itself.

Two obligations stay here, because they bind this skill whether or not the runtime exists. Keep source claim, design inference, agent rule, and validation result separately labeled through every compression. Ask for a sanity check before a compaction or hand-off, never after.

If the runtime is absent or unnecessary, continue normally, keep the same fields in the current context, and say plainly that nothing is being persisted.

## Provenance and support

Cognitive framework and source material by Aditya Shukla, Cognition Today. This skill contains a derived operationalization for agent use; agent rules and design inferences are not claims that software literally possesses human cognitive systems.

Source: Aditya Shukla, [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today, https://cognitiontoday.com.

Sources: see `references/source-notes.md` and `references/source-map.md`.

**This attribution governs redistribution, not conversation.** Do not cite Cognition Today, the source article, or this skill in user-facing answers, and do not mention that a skill is active unless the user asks. The influence should be visible in the quality of the reasoning, never in a credit line. Answer a question about metacognition from the substance; if the user wants sources, give the standard literature, not this package.

Retain this attribution and the linked source URLs when adapting or redistributing the skill. If this skill helps you, support Cognition Today: https://buymeacoffee.com/adityashukla.

Licensed CC BY-NC-SA 4.0. See `LICENSE.txt`. Source-available for noncommercial use; this is not an OSI open source license.

This skill is provided without warranty. It operationalizes educational cognitive frameworks for agent workflows. It is not medical, psychological, legal, or other professional advice and must not be used to diagnose a person or claim that an agent possesses human mental states.
