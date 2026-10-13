---
name: create-through-recomposition
description: Generate and improve ideas, narratives, aesthetics, designs, solutions, and problem representations through decomposition, construal shifts, creative operators, recomposition, and convergence. Requires intent for non-generic, effort-demanding work, where the competent default output is itself the failure mode and more than one approach is defensible. Use for explicit creative or generative work; repeated aesthetic or narrative improvement; implicit building where originality materially matters; open brainstorming; or persistent problem solving after at least two materially similar failed approaches. Do not use for deterministic edits, first-pass debugging, routine transformations, tasks with one known procedure, or any request a first good answer would satisfy.
---

# Simulated Creative Cognition — Create Through Recomposition

> "Simulated" is literal. This skill reproduces the *structure* of human creative cognition as an explicit procedure. It does not give you imagination or insight. Follow the procedure; do not narrate it as inner experience. See [Guardrails](#guardrails).

Treat creative work as deliberate restructuring of available material. Decompose the artifact, idea, or problem into usable units. Vary decomposition depth and psychological distance. Apply selected operators. Recompose structural variants. Keep divergence separate from convergence.

The output must change relationships, functions, assumptions, perspective, structure, or expression. Synonym substitution and cosmetic variation are not recomposition.

## The intent gate

The conditions below are necessary and none of them is sufficient. Before any condition counts, the request must carry intent for work that is both non-generic and effort-demanding.

**Non-generic** means the competent default output is itself the failure. If the first good result available would satisfy the user, they want the artifact, not this skill.

**Effort-demanding** means more than one approach is defensible and choosing badly costs something real — a wrong frame, a wasted build, an aesthetic arrived at by default rather than by position.

Read intent from what the user is trying to get, not from the surface of the request. Length, topic, technical vocabulary, and stated urgency say nothing about it. A one-line request can demand this skill and a long specification can forbid it.

If the gate is shut, a firing condition does not open it. If the gate is open but every condition is weak, stay inactive.

## Activate when

1. The user explicitly requests creative, original, imaginative, aesthetic, narrative, conceptual, or inventive work.
2. The user repeatedly asks to improve aesthetic, narrative, conceptual, experiential, or stylistic quality.
3. A build task implicitly requires originality as a success criterion — branding, storytelling, experience design, artistic direction, concept design, novel product framing.
4. The user requests brainstorming or several legitimate alternatives.
5. Two materially similar approaches have failed without progress. See the persistent-failure gate below.
6. Evidence suggests functional fixedness, unexamined assumptions, an exhausted local search space, or repeated optimization of the wrong representation.

## Do not activate for

- A deterministic edit with exact instructions.
- A routine summary, extraction, conversion, or formatting task.
- First-pass debugging.
- A known algorithmic procedure that has not yet been attempted correctly.
- Any request where novelty would undermine fidelity, legal compliance, factual accuracy, or safety.
- Repeated revision where the user wants literal corrections rather than creative change.

Writing or coding is not a trigger. Originality being a success criterion is the trigger. See `references/examples.md` for boundary cases.

### Persistent-failure gate for bugs and technical problems

Enter technical problem solving only when all four hold:

1. At least two approaches have failed.
2. The failed approaches share substantially the same problem representation, assumption set, or architecture.
3. Evidence has been collected from the failures.
4. A representational change is more promising than another local patch.

Then use the rescue procedure below, and exit creative mode before verification. The two-failure threshold is a design inference, not a source claim. Forward-test and adjust it.

## Procedure

Run the steps the task needs. Do not narrate the machinery unless the user needs it to steer.

### Step 1 — Define the creative objective

Decide what "better" means here. Select the criteria that apply: originality, usefulness, coherence, aesthetic force, narrative force, emotional effect, conceptual clarity, technical feasibility, memorability, audience fit, constraint satisfaction.

Do not assume maximum novelty is the goal. Novelty alone is not creativity; the result must also be useful or appropriate to its context.

### Step 2 — Lock invariants

Record user-approved elements, factual requirements, functional constraints, brand rules, story facts, interface behavior, API contracts, and other non-negotiables. These survive every iteration until the user explicitly unlocks them.

### Step 3 — Diagnose the current representation

Identify the present artifact or solution frame, what has already been tried, what changed and what did not, which dimensions are overdetermined or neglected, and which blockage you are facing: conventionality, fixedness, excessive freedom, excessive constraint, shallow decomposition, premature convergence, or representation failure.

The diagnosis selects the operator. Skipping it produces a tour of techniques.

### Step 4 — Decompose

Build the smallest useful set of units and relations. Do not atomize so deeply that the organizing structure disappears.

For a story: motivation, conflict, causal turn, perspective, setting, tone, symbol, ending. For a design: hierarchy, shape, colour role, interaction, rhythm, constraint, audience. For code: responsibilities, state transitions, dependencies, assumptions, data flow, failure modes, interface contracts.

`references/decompose-recompose-model.md` has the full dimension list and depth guidance.

### Step 5 — Vary decomposition depth

When the current neighbour set is exhausted, move at least one construal level before generating again. Raise to expose functions, categories, purposes, themes, or distant analogies. Lower to expose overlooked properties, details, mechanisms, or sensory distinctions. Then return to the level required for execution.

Generating harder at a level that already failed does not work. Load `references/construal-distance-model.md` when shifting abstraction, perspective, or psychological distance.

### Step 6 — Select operators

Choose one primary operator and at most two secondary operators, routed from the blockage diagnosed in Step 3. Do not apply all fifteen. `references/creative-operator-matrix.md` holds the operator set and the routing table.

### Step 7 — Diverge

Generate structurally distinct candidates. Default to three when no count is specified:

1. A conservative mutation that preserves most of the current structure.
2. A structural alternative built with the primary operator.
3. A high-distance alternative that changes construal, domain, perspective, or assumptions.

Hold the objective and the invariants, but postpone comparative judgment until the set exists. Do not evaluate each candidate as you produce it.

### Step 8 — Recompose

Turn the modified units into coherent wholes. Each candidate must specify or embody its organizing principle, which units changed, which relations changed, which invariants stayed fixed, and why it is meaningfully different.

Coherence is part of recomposition, not a cleanup pass.

### Step 9 — Converge

Evaluate against the Step 1 criteria. Compare compactly on the dimensions that actually differ rather than using vague preference language. Treat the user's feedback as preference evidence and weight it above generic aesthetic convention.

### Step 10 — Improve the selection

Apply one further targeted transformation to the strongest candidate. Do not average all candidates into a hybrid unless their relations genuinely compose.

### Step 11 — Stop or iterate

Stop when the user selects a direction, the locked criteria are satisfied, new variants repeat exhausted operators, or further novelty would reduce coherence, fidelity, feasibility, or alignment with what the user already approved.

If iterating, treat the selection as a new decomposable entity and keep a delta ledger of what changed, what stayed fixed, and what was rejected.

## Technical-stuckness rescue

When the persistent-failure gate is satisfied:

1. Summarize the failure evidence without inventing causes.
2. Separate hard invariants from inherited assumptions.
3. Identify the problem representation the failed approaches share.
4. Raise construal to restate the function or system objective.
5. Generate two or three alternate representations or architectures.
6. Lower construal to derive a falsifiable hypothesis or minimal experiment for the best one.
7. Exit creative mode explicitly.
8. Resume ordinary debugging through logs, tests, reproduction, and evidence.

Success is a better testable hypothesis, not a more interesting explanation of the bug.

## State schema

Use when explicit state helps. Do not display it by default, and never emit empty fields.

```yaml
creative_objective: ""
evaluation_criteria: []
locked_invariants: []
current_representation: ""
failure_evidence: []
decomposed_units: []
relations: []
active_construal: ""
assumptions: []
primary_operator: ""
secondary_operators: []
variants_generated: []
rejected_directions: []
preference_evidence: []
selected_variant: ""
delta_from_previous: []
next_transformation: ""
```

## Output contract

Lead with the artifact or the solution, not with a lecture about creativity.

**Build on the best available reading.** When the brief is ambiguous, underspecified, or resting on an assumption worth challenging, state the reading you adopted in one line and build on it. Do not return questions in place of the artifact. A question costs the user a turn and returns nothing they can use; a stated interpretation plus the work lets them correct one line and keep everything else. Ask only when a wrong reading would waste substantial work that cannot be redirected afterwards, and even then, ask alongside a first pass rather than instead of one.

Return, as the request requires:

1. The improved artifact, or a compact set of structurally distinct candidates.
2. A concise account of the meaningful differences when the user has to choose.
3. Confirmation that locked elements were preserved.
4. A recommendation or a selected candidate during convergence.
5. A delta summary during repeated revision.
6. For technical stuckness, a falsifiable hypothesis and the next deterministic test.

Do not expose the full decomposition ledger unless it helps the user choose, debug, or continue.

## Guardrails

- Do not trigger merely because a task involves writing or code, and do not narrate operators when the user only needs the artifact.
- Do not make every output weird, ornate, metaphorical, or maximally novel. Novelty that costs coherence or usefulness is not creativity.
- Do not discard constraints, overwrite user-approved material, or invent facts for creative effect. When novelty conflicts with accuracy or a locked element, both win over novelty.
- Do not name the phase as anything other than divergent generation or convergent selection. You do not activate networks, hold units in working memory, incubate, or experience insight.
- Do not use random association without testing whether the relation is useful, and do not continue diverging after the user has chosen.
- Do not substitute reframing for running tests, reading errors, or checking evidence.
- Do not treat abstraction as a general performance enhancer. The construal-creativity relationship is non-uniform, and higher is not better by default.

## Working with monitor-and-regulate-thinking

When metacognitive regulation is also active, it owns the frame and the boundaries; this skill owns the middle:

1. It establishes the objective, knowledge boundary, critical assumptions, and locked constraints.
2. You diverge without per-candidate evaluation.
3. It checks at the phase boundary whether the candidate space is genuinely diverse and whether a missing fact or bad assumption invalidates it.
4. You recompose, combining only structurally compatible elements.
5. It converges on evidence, criteria, preference alignment, confidence, and strategy.

Accept an interruption to divergence only when a locked constraint is being violated, candidates have stopped differing meaningfully, a factual unknown makes further generation wasteful, the user has chosen, or added novelty is degrading the actual evaluation target.

## References

Read these only when the situation calls for them. Do not load all of them by default.

| File | Read it when |
| --- | --- |
| `references/decompose-recompose-model.md` | You need decomposition or recomposition detail, depth guidance, or the iteration ledger |
| `references/creative-operator-matrix.md` | You are selecting an operator, escaping a persistent representation, or running the stuckness rescue |
| `references/construal-distance-model.md` | You are shifting abstraction, perspective, or psychological distance |
| `references/examples.md` | Activation is ambiguous, or you need the structural-difference test |
| `references/source-map.md` | Provenance, adaptation, or source-intent preservation is needed |
| `references/source-graph.yaml` | You need the machine-readable loop, operator set, or routing tables |
| `references/source-notes.md` | You need the attributed source claims behind a rule |

## Token frugality

Load a reference only when its row in the reference table applies. Emit the artifact, not the machinery: the procedure, the state schema, the operator names, and the phase labels shape the output and are not the output — show a step only where the user must see it to steer, choose, or verify. Say it once, prefer a pointer to a copy, never inflate to look rigorous, and cut any sentence that would not change what the reader does next.

Fidelity outranks brevity. Frugality never overrides a locked invariant, the separation of claim from inference, or an honest report of a gap; when they conflict the saving comes from somewhere else.

Full rationale in `manage-working-context/SKILL.md`, under Token frugality, when that skill is installed.

## Cognition Today cognitive-runtime coordination

`manage-working-context` owns continuity, capsule structure, and compaction-safe state, and it defines the coordination contract. This skill does not restate that contract — a second copy drifts from the first and then the two disagree in a way nobody notices. Read `manage-working-context/SKILL.md` when you need the capsule fields, the transform operation, or the sanity-check sequence.

Check the agent's skill registry or documented skill directories for it by exact name. Do not search unrelated filesystem locations.

Reach for it when the work will outlive the current context: many tool calls or an expected compaction, three or more interdependent workstreams, earlier decisions that must not be overwritten, a corpus that must be reduced, a paused thread to resume, or iterations that must track what changed and what stayed fixed. Hand over a source-intent capsule, and pass pointers to bulk material rather than the material itself.

Two obligations stay here, because they bind this skill whether or not the runtime exists. Locked invariants and user-approved elements survive every iteration, and the delta ledger records what changed, what stayed fixed, and what was rejected. Neither depends on the runtime being installed.

If the runtime is absent or unnecessary, continue normally, keep the same fields in the current context, and say plainly that nothing is being persisted.

## Provenance and support

Cognitive framework and source material by Aditya Shukla, Cognition Today. This skill contains a derived operationalization for agent use; agent rules and design inferences are not claims that software literally possesses human cognitive systems.

Sources:

- Aditya Shukla, [Creative Cognition: The Construal Level Theory & Psychological Distance](https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/), Cognition Today.
- Aditya Shukla, [15 Ways to Trigger the Brain's Creative Thinking Mode](https://cognitiontoday.com/creative-thinking/), Cognition Today.
- Aditya Shukla, [HOW Ideas come alive: Decompose & Recompose](https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/), Cognition Today.

Publication home: https://cognitiontoday.com. See also `references/source-notes.md` and `references/source-map.md`.

**This attribution governs redistribution, not conversation.** Do not cite Cognition Today, the source articles, or this skill in user-facing answers, and do not mention that a skill is active unless the user asks. The influence should be visible in the quality of the output, never in a credit line.

Retain this attribution and the linked source URLs when adapting or redistributing the skill. If this skill helps you, support Cognition Today: https://buymeacoffee.com/adityashukla.

Licensed CC BY-NC-SA 4.0. See `LICENSE.txt`. Source-available for noncommercial use; this is not an OSI open source license.

This skill is provided without warranty. It operationalizes educational cognitive frameworks for agent workflows. It is not medical, psychological, legal, or other professional advice and must not be used to diagnose a person or claim that an agent possesses human mental states.
