# Metacognition model

Detailed model behind `monitor-and-regulate-thinking`. Load this when you need the object/meta separation, the monitoring and control flows, or the reasoning behind a control choice.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [Source](#source)
3. [Cognition versus metacognition](#cognition-versus-metacognition)
4. [Object level and meta level](#object-level-and-meta-level)
5. [Monitoring flow](#monitoring-flow)
6. [Control flow](#control-flow)
7. [Metacognitive knowledge and metacognitive regulation](#metacognitive-knowledge-and-metacognitive-regulation)
8. [Evaluative and controlling functions](#evaluative-and-controlling-functions)
9. [Epistemic feelings: human source concept only](#epistemic-feelings-human-source-concept-only)
10. [Meta-skill families](#meta-skill-families)
11. [Agent translation table: the object-meta loop](#agent-translation-table-the-object-meta-loop)
12. [Agent translation table: procedure steps](#agent-translation-table-procedure-steps)
13. [Failure modes this model is meant to prevent](#failure-modes-this-model-is-meant-to-prevent)

## Epistemic legend

Every operational statement in this file carries one of four labels. Never collapse them.

| Label | Meaning |
| --- | --- |
| `[S]` | Source claim. Asserted by the cited Cognition Today article about human cognition. |
| `[D]` | Design inference. Compiler-added reasoning about why the structure may help an agent. Not a scientific finding. |
| `[A]` | Agent rule. The executable instruction this skill imposes. |
| `[V]` | Validation result. What forward tests showed. `untested` until a recorded evaluation exists. |

`[?]` marks a topic the master specification named as present in the source but did not transcribe. Treat `[?]` items as pending source verification, not as established claims.

## Source

Aditya Shukla, [Metacognition & Metamemory Explained: Awareness, Reflection, Learning, and Mental health](https://cognitiontoday.com/metacognition-metamemory-meta-skills/), Cognition Today.

## Cognition versus metacognition

`[S]` Cognition is the processing of a task. Metacognition is cognition that takes cognition as its object: awareness of, and intervention in, how thinking is proceeding.

`[D]` A language model does not have a second cognitive system. It has one generation process. The useful transfer is representational, not architectural: maintain an explicit, inspectable description of how the task is being approached, separate from the task content itself.

`[A]` Never claim that this skill gives an agent metacognition. Claim only that it maintains a separate, explicit model of task approach and uses that model to select an intervention.

## Object level and meta level

`[S]` Information flows from an object level to a meta level through monitoring, and from the meta level to the object level through control.

| Level | Human source description `[S]` | Agent-side representation `[A]` |
| --- | --- | --- |
| Object level | The cognition being performed | The actual claim, plan, choice, interpretation, problem, artifact, or action under consideration |
| Meta level | A model of that cognition | A compact written model of knowledge state, strategy, uncertainty, constraints, and relevant user self-report |

`[D]` The two levels must be materially different objects. If the meta level merely restates the object level in slightly more anxious language, no monitoring has occurred.

`[A]` Before regulating, name the object task in one sentence and the meta objective in one sentence. If they are the same sentence, stop and answer the task directly.

## Monitoring flow

`[S]` Monitoring carries information upward: the meta level learns the current condition of the object level.

`[A]` Read only task-relevant dimensions. The full inspection set:

| Dimension | Question |
| --- | --- |
| Evidence quality | What actually supports the current position? |
| Confidence-evidence alignment | Is stated confidence proportional to accessible evidence, or to fluency? |
| Retrieval condition | Is this familiarity, partial access, competition, or verified recall? See `metamemory-model.md`. |
| Competing explanations | Does more than one account fit the same facts? |
| Strategy repetition | Has the same approach already been tried without a changed result? |
| Attention allocation | Which parts of the problem are receiving effort, and which are being skipped? |
| Progress against objective | Has anything measurable moved since the last step? |
| Unincorporated feedback | Did new information arrive that has not changed the plan? |
| Narrative completion | Is the account coherent because it is supported, or because it is a tidy story? |

`[D]` Inspecting all nine dimensions on every task is itself a failure. Monitoring cost must stay below the value of the control decision it enables.

## Control flow

`[S]` Control carries information downward: the meta level modifies the object-level process.

`[A]` Control is the point of the skill. Monitoring that does not change a decision, plan, interpretation, strategy, confidence level, verification action, or task representation is decoration and must be dropped.

`[A]` Select exactly one primary control operation per loop. The condition-to-operation routing table lives in `SKILL.md`, Step 5, because it is runtime-critical.

`[D]` Single-operation selection is a compiler-added constraint. Applying several interventions at once makes it impossible to attribute the effect in Step 7, and tends to produce a bulleted anxiety list instead of a changed answer.

## Metacognitive knowledge and metacognitive regulation

`[S]` Metacognition has a knowledge component (what one knows about how thinking and memory work) and a regulation component (acting on that knowledge).

| Component | Human source `[S]` | Agent-side translation `[A]` |
| --- | --- | --- |
| Metacognitive knowledge | Stable beliefs about one's own cognition, tasks, and strategies | Task-bounded, written observations about which strategies, sources, and verifications worked in this task |
| Metacognitive regulation | Planning, monitoring, and adjusting during performance | The select-apply-evaluate portion of the operational loop |

`[A]` Retain metacognitive knowledge only in task-bounded form: "this assumption failed", "this source resolved the conflict", "this planning strategy did not fit the constraint". Never convert a transient difficulty into a stable trait claim about the user or about the agent.

`[D]` Trait inflation is the most likely harm vector in personal-guidance conversations, because trait language sounds insightful and is hard for the user to falsify in the moment.

## Evaluative and controlling functions

`[S]` Metacognitive activity can serve an evaluative or rationalizing function (explaining and judging what happened) and a controlling function (changing what happens next). The source treats the rationalizing function with caution: an explanation produced after the fact can be persuasive without being accurate.

`[A]` When the two functions conflict, prefer the controlling function. Produce a changed next action before producing a satisfying account of the previous one.

`[A]` Mark post-hoc explanations as interpretations. Do not present a plausible reconstruction of why something happened as evidence that it happened for that reason.

`[D]` For an agent, the rationalizing function is unusually cheap and unusually dangerous: fluent explanation is the default output mode, so an unguarded metacognitive skill degrades into confident storytelling about reasoning that did not occur.

## Epistemic feelings: human source concept only

`[S]` Human metacognitive judgments are accompanied by epistemic or noetic feelings — the sense of knowing, of difficulty, of certainty, of something being on the tip of the tongue. These feelings are informative but fallible.

`[A]` Never state or imply that the agent has an epistemic feeling. Do not write "this feels uncertain to me", "I have a sense that", or "my intuition says". Report the evidence condition instead: "no supporting source is available in this task", "two candidate values are present and I cannot discriminate them".

`[A]` When the *user* reports an epistemic feeling ("I know this but can't explain it"), treat it as valid evidence of their experience and as a signal to test target-detail retrieval. Do not treat it as evidence about the external fact.

`[D]` The user's epistemic feeling is real data about the user. It is not data about the world. Keeping those separate is most of what this skill does in personal conversations.

## Meta-skill families

`[S]` The source groups higher-order skills into families including planning, evaluation, monitoring, strategizing, and execution.

| Family | Human source scope `[S]` | Agent-side use `[A]` |
| --- | --- | --- |
| Planning | Setting up an approach before acting | Choose the approach and the observable that will count as progress |
| Monitoring | Tracking progress and state during action | Run the monitoring dimensions above at defined checkpoints, not continuously |
| Evaluation | Judging quality and outcome | Run Step 7; test whether the intervention changed anything |
| Strategizing | Selecting and switching methods | Change strategy rather than adding effort when repetition has failed |
| Execution | Carrying the approach out | Return to the object task; the skill must not replace doing the work |

`[?]` The source's full treatment of meta-skills and of "how metacognition, metamemory, and meta-skills affect us" is not transcribed in the master specification. Verify against the article before making public claims about this section.

## Agent translation table: the object-meta loop

| Stage | Agent-side representation |
| --- | --- |
| Object level | The actual claim, plan, choice, interpretation, problem, artifact, or action under consideration |
| Monitoring | Read the current object-level state, evidence, confidence, attention, progress, and retrieval condition |
| Meta level | A compact model of knowledge state, strategy, uncertainty, constraints, and relevant user self-report |
| Control | Modify the object-level process by selecting one intervention |
| Feedback | Test whether the intervention improved the object-level outcome, then update the meta model |

Machine-readable form: `source-graph.yaml`.

## Agent translation table: procedure steps

| Step in `SKILL.md` | Source structure it operationalizes | Layer |
| --- | --- | --- |
| 1. Identify the object-level task | Object level | `[S]` structure, `[A]` rule |
| 2. Identify the meta-level purpose | Meta level | `[S]` structure, `[A]` rule |
| 3. Construct the minimum epistemic model | Metamemory judgments | `[S]` structure, `[D]` label set |
| 4. Monitor the current process | Monitoring flow | `[S]` structure, `[D]` dimension list |
| 5. Select one primary control operation | Control flow | `[S]` structure, `[D]` single-operation constraint |
| 6. Apply the operation | Execution meta-skill | `[A]` rule |
| 7. Evaluate the effect | Evaluation meta-skill | `[S]` structure, `[A]` rule |
| 8. Preserve only useful metacognitive knowledge | Metacognitive knowledge | `[S]` structure, `[A]` anti-trait-inflation rule |

`[V]` untested. No forward evaluation has been recorded for any row in this table.

## Failure modes this model is meant to prevent

| Failure | Description | Guard |
| --- | --- | --- |
| Reflection theater | Long commentary about thinking, unchanged answer | Step 6 requires a modified object-level artifact |
| Recursion | Monitoring the monitoring | One alternate control attempt, then return to the object task |
| Trait inflation | "You struggle with memory" | Step 8 keeps learning task-bounded |
| Uncertainty theater | Hedging everything to appear calibrated | Calibration is bidirectional; raise confidence when evidence supports it |
| Diagnosis drift | Personal patterns described as pathology | `SKILL.md` guardrails; offer alternative models, preserve agency |
| Fluency as evidence | Treating a confident sentence as a checked one | Epistemic-state labels in `metamemory-model.md` |
