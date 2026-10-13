# Source map: create-through-recomposition

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

## Records

```yaml
- operation_id: decompose-creative-object
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#the-decompose-recompose-model-of-ideation
  source_claim: Creative ideation can involve decomposing available knowledge into relevant units before recombination.
  design_inference: Explicit decomposition can make an agent's recombination space inspectable and controllable.
  agent_rule: Decompose the current artifact or problem into task-relevant units, relations, assumptions, and constraints.
  validation_status: untested

- operation_id: vary-construal-level
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/#creative-cognition-the-construal-level-theory
  source_claim: Concrete and abstract construals expose different properties and conceptual associations.
  design_inference: Moving between abstraction levels may help an agent escape an exhausted local neighbor set.
  agent_rule: Raise or lower construal when the current representation yields only obvious candidates, then return to executable detail.
  validation_status: untested

- operation_id: select-creative-operator
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-thinking/#what-is-creativity-really
  source_claim: Transformation, combination, perspective shifts, constraints, cross-domain borrowing, functional-unfixedness, lateral thinking, divergence, diffused attention, and improvisation can facilitate different forms of creativity.
  design_inference: Routing an observed blockage to a small operator set is more reliable than applying a generic "be creative" prompt.
  agent_rule: Select one primary and at most two secondary operators based on the blockage.
  validation_status: untested

- operation_id: recompose-variants
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#what-can-we-make-of-these-processes
  source_claim: Modified decomposed units can be recomposed into a new entity that can itself be decomposed and iterated.
  design_inference: Structural variants and delta tracking can preserve purposeful iteration.
  agent_rule: Recompose coherent variants, compare them after divergence, and iterate only on the selected entity.
  validation_status: untested

- operation_id: escape-persistent-fixedness
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-thinking/#overcome-functional-fixedness
  source_claim: Fixed assumptions about an object's or concept's function can block alternative solutions.
  design_inference: Repeated technical failures may justify changing the problem representation instead of repeating local patches. The two-failure activation threshold is compiler-added and is not a source claim.
  agent_rule: After two materially similar failed approaches, separate invariants from assumptions and generate a falsifiable alternate representation.
  validation_status: untested

- operation_id: apply-psychological-distance
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/#psychological-distance-and-creativity
  source_claim: Psychological distance is linked to construal level and varies along informational, personal, temporal, and spatial dimensions.
  design_inference: Varying distance along the dimension on which the current representation is most rigidly fixed is cheaper than varying all four.
  agent_rule: Select one distance dimension based on where the representation is fixed. Do not force all four into every task, and do not assert what a real group feels when adopting a personal-distance viewpoint.
  validation_status: untested

- operation_id: preserve-construal-benefit-caveat
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/#psychological-distance-and-creativity
  source_claim: The relationship between construal level, psychological distance, and creative benefit is not uniform; analytical and holistic processing styles interact with it.
  design_inference: Dropping this caveat would convert a qualified source into a general claim that abstraction improves creativity.
  agent_rule: Never tell a user that thinking more abstractly will make them more creative. Treat construal shifting as a diagnosed tool.
  validation_status: untested

- operation_id: test-chance-configurations
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#randomness-induced-creativity
  source_claim: Chance or unexpected juxtaposition of units can produce configurations that directed search would not reach.
  design_inference: A language model produces surprising juxtapositions cheaply, so the discriminating work is the relevance test rather than the generation.
  agent_rule: After pairing distant units, state the relation the pairing creates and test whether it serves the objective. Never present an untested random pairing as a result.
  validation_status: untested

- operation_id: choose-decomposition-depth
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#depth-of-decomposition
  source_claim: Decomposition can be carried out at different depths, and depth changes which relations become available for recombination.
  design_inference: Beyond a certain depth the organizing structure disappears and recombination yields variety without coherence, leaving convergence nothing to select on.
  agent_rule: Do not atomize past the level at which the artifact's organizing principle is still visible.
  validation_status: untested

- operation_id: separate-divergence-from-convergence
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#diffused-thinking
  source_claim: Creative work draws on both focused attention and a looser diffused mode with wider association.
  design_inference: Evaluating each candidate as it is generated collapses divergence into a slow form of convergence and suppresses structurally distant options.
  agent_rule: Postpone comparative judgment until the candidate set exists, then converge against the criteria fixed before generation.
  validation_status: untested

- operation_id: prohibit-literal-neural-claims
  layer: source-grounded
  source_id: https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/#default-mode-and-central-executive-influences
  source_claim: The source attributes creative output to interaction between default-mode and central-executive networks in the human brain.
  design_inference: Only the two-phase alternation between loose generation and directed control transfers to an agent; the neural account does not.
  agent_rule: Never state that the agent activates a default-mode network, engages an executive network, has working memory, incubates, or experiences insight. Name the phase instead.
  validation_status: untested

- operation_id: require-novelty-plus-usefulness
  layer: source-grounded
  source_id: https://cognitiontoday.com/creative-thinking/#what-is-creativity-really
  source_claim: Creativity involves output that is novel and also useful or appropriate to its context, not novelty alone.
  design_inference: Scoring novelty alone rewards outputs that destroy coherence, factuality, or the user's approved direction.
  agent_rule: Define evaluation criteria before generating, and score candidates on usefulness and coherence alongside originality.
  validation_status: untested

- operation_id: gate-creativity-behind-persistent-failure
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Without a gate, a creativity skill hijacks first-pass debugging and substitutes ideation for reading the error. Two materially similar failed approaches with collected evidence is the chosen threshold and is untested.
  agent_rule: Enter technical problem solving only when two materially similar approaches have failed, evidence has been collected, and a representational change is more promising than another local patch. Then exit creative mode and resume deterministic testing.
  validation_status: untested

- operation_id: lock-invariants-across-iterations
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Repeated revision regresses without an explicit invariant set; elements a user approved in an early round silently disappear later, and the project cycles instead of converging.
  agent_rule: Record user-approved elements, factual requirements, functional constraints, and contracts before generating. Preserve them through every iteration unless the user explicitly unlocks them.
  validation_status: untested

- operation_id: default-to-three-structural-variants
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: A conservative mutation, a structural alternative, and a high-distance alternative span the useful range at low cost. Larger sets add tokens faster than they add distinct structure.
  agent_rule: When the user has not specified a count, produce three candidates spanning conservative, structural, and high-distance.
  validation_status: untested

- operation_id: maintain-delta-ledger
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Iterative creative work needs an explicit record of what changed, what stayed fixed, and what was rejected, or the same rejected direction reappears two rounds later.
  agent_rule: During repeated revision, maintain and report a delta summary, and treat user feedback as preference evidence outranking generic convention.
  validation_status: untested

- operation_id: coordinate-with-working-context-runtime
  layer: design-inference
  source_id: none
  source_claim: none
  design_inference: Long creative projects lose invariants and rejected directions across compaction. A separate runtime can preserve them, but must not acquire authority over the creative rules.
  agent_rule: Activate manage-working-context only when it is discoverable and at least one runtime trigger holds. Pass invariants, operators, variants, rejections, preferences, and the next action. Complete the task normally when the runtime is absent.
  validation_status: untested
```

## Coverage note

Records with `layer: design-inference` carry no source authority and may be changed on engineering grounds when adapting the skill. Records with `layer: source-grounded` must retain their attribution and source URL.

Every `validation_status` is `untested`. No forward evaluation has been run against this build.
