# Source map: monitor-and-regulate-thinking

Every hard instruction in this package maps to a record below. A record either grounds the instruction in a Cognition Today source location or declares it a compiler-added design inference with no source authority.

Load this file only when provenance, adaptation, or source-intent preservation is needed. It is not required to execute the skill.

## Contents

1. [Schema](#schema)
2. [Records](#records)
3. [Coverage note](#coverage-note)

## Schema

```yaml
- operation_id: stable-operation-name
  layer: source-grounded | design-inference
  source_id: article-url#heading-or-element   # or "none" for design inferences
  source_claim: what-the-source-asserts        # or "none"
  design_inference: why-it-is-being-applied-to-an-agent
  agent_rule: executable-runtime-instruction
  validation_status: untested-or-tested-result
```

`layer: source-grounded` means the mechanism comes from the article and the agent-side application is the inference. `layer: design-inference` means no part of the rule is claimed by the source; it is an engineering decision that must not be described as psychology.

## Records

```yaml
- operation_id: separate-object-and-meta-levels
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#cognition-vs-metacognition
  source_claim: Object-level cognition and meta-level cognition exchange information through monitoring and control.
  design_inference: Separating task state from a monitoring model may improve agent strategy selection.
  agent_rule: Identify the object task and meta objective before regulating the process.
  validation_status: untested

- operation_id: classify-knowledge-state
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#metamemory
  source_claim: Metamemory supports judgments about whether and how something is known without complete retrieval.
  design_inference: Explicit knowledge-state labels can reduce conflation of familiarity, inference, and verified knowledge.
  agent_rule: Classify only the task-relevant knowledge states before choosing a control operation.
  validation_status: untested

- operation_id: diagnose-retrieval-condition
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#theories-of-metamemory
  source_claim: Cue familiarity, accessibility, competition, and their interaction offer different accounts of memory judgments.
  design_inference: These distinctions can route an agent toward detail retrieval, partial-evidence testing, or candidate discrimination.
  agent_rule: Select a retrieval control based on the observed condition without presenting it as a diagnosis.
  validation_status: untested

- operation_id: regulate-thinking
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#what-is-metacognition
  source_claim: Metacognition includes monitoring and modifying cognition.
  design_inference: Monitoring is useful only when it changes task execution or calibration.
  agent_rule: Select one primary control operation, apply it to the object task, and evaluate the effect.
  validation_status: untested

- operation_id: test-target-detail-before-accepting-knowledge
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#theories-of-metamemory
  source_claim: A judgment can be produced from cue familiarity before any target content is retrieved.
  design_inference: Requiring one specific, checkable detail is a cheap discriminator between a familiar label and retrieved knowledge, and it applies to the agent's own output as well as the user's report.
  agent_rule: When a topic is recognized but no specific detail has been produced, label the state familiar-cue and retrieve or request a target detail before relying on the claim.
  validation_status: untested

- operation_id: monitor-metamemory-dimensions
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#metamemory
  source_claim: The source describes eight categories of knowledge about memory, including strategy, task, capacity, change, anxiety, activities, achievement motivation, and locus.
  design_inference: Each dimension can be reframed as a bounded question about the current task; capacity in particular must be reframed as a question about available context rather than about a person.
  agent_rule: Ask only the metamemory dimensions that change the next action, and never convert capacity or anxiety into a claim about the user.
  validation_status: untested

- operation_id: preserve-task-bounded-learning
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#metamemory
  source_claim: Metacognition includes a knowledge component about how one's own thinking and memory operate.
  design_inference: Retaining what worked in this task is useful; generalizing a transient difficulty into a stable trait is both unsupported and hard for a user to falsify in conversation.
  agent_rule: Record learning as task-bounded statements about assumptions, sources, and strategies. Never state or imply a global trait about the user or the agent.
  validation_status: untested

- operation_id: prefer-control-over-rationalization
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#how-metacognition-metamemory-and-meta-skills-affect-us
  source_claim: Metacognitive activity can serve an evaluative or rationalizing function as well as a controlling function, and a post-hoc account can be persuasive without being accurate.
  design_inference: Fluent explanation is an agent's default output mode, so an unguarded metacognitive skill degrades into confident storytelling about reasoning that did not occur.
  agent_rule: Produce a changed next action before producing an account of the previous one, and mark post-hoc explanations as interpretations.
  validation_status: untested

- operation_id: prohibit-literal-epistemic-feeling-claims
  layer: source-grounded
  source_id: https://cognitiontoday.com/metacognition-metamemory-meta-skills/#what-is-metacognition
  source_claim: Human metacognitive judgments are accompanied by epistemic feelings, which are informative but fallible.
  design_inference: An agent has no epistemic feelings; borrowing the vocabulary would misrepresent the system and disguise an absence of evidence as an intuition.
  agent_rule: Report the evidence condition instead of a sensation. Never write that something feels certain, uncertain, or familiar to the agent. Treat a user's reported epistemic feeling as evidence about the user, not about the world.
  validation_status: untested

- operation_id: select-monitoring-intensity
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: A single monitoring depth either overloads light personal questions or underserves multi-thread planning work. Three intensity levels bound the overhead of the skill.
  agent_rule: Choose Light, Standard, or Persistent intensity before running the loop, and do not expose the full schema at Light intensity.
  validation_status: untested

- operation_id: limit-to-one-primary-control-operation
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Applying several interventions simultaneously makes the evaluation step uninterpretable and tends to produce a bulleted list of concerns instead of a changed answer.
  agent_rule: Select exactly one primary control operation per loop.
  validation_status: untested

- operation_id: bound-recursion
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Reflection on reflection has no natural stopping condition, and an agent will continue as long as it is rewarded for appearing thorough.
  agent_rule: If the first control operation produces no change, try exactly one alternate operation, then return to the object task or state what information is required.
  validation_status: untested

- operation_id: refuse-diagnosis
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: The source article discusses mental health, but converting a cognitive-monitoring procedure into clinical inference would be both unsupported and harmful. The boundary is an engineering and safety decision, not a source claim.
  agent_rule: Do not diagnose mental-health, neurological, personality, or memory conditions. Do not assert unconscious motives. Offer alternative models and controllable options, and recommend professional help where stakes warrant it.
  validation_status: untested

- operation_id: withhold-hidden-reasoning
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Externalized assumptions, evidence, and decision bases give the user everything an audit needs; requests for private reasoning traces invite fabrication of a trace that did not exist.
  agent_rule: Provide assumptions, evidence status, and the basis for the decision. Do not expose or invent private chain-of-thought, and do not demand it from another agent.
  validation_status: untested

- operation_id: coordinate-with-working-context-runtime
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Long agent tasks lose source intent across compaction. A separate runtime can preserve it, but activating it on short tasks adds cost without benefit and lets state management crowd out domain reasoning.
  agent_rule: Activate manage-working-context only when it is discoverable and at least one runtime trigger holds. Pass a source-intent capsule that keeps source claims separate from design inferences. Complete the task normally when the runtime is absent.
  validation_status: untested
```

## Coverage note

Records with `layer: design-inference` carry no source authority. When adapting this skill, they may be changed freely on engineering grounds. Records with `layer: source-grounded` must retain their attribution and source URL.

Every `validation_status` is `untested`. No forward evaluation has been run against this build.
