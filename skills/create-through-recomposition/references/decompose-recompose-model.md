# Decompose-recompose model

The core ideation loop behind `create-through-recomposition`. Load this when you need decomposition or recomposition detail beyond the procedure in `SKILL.md`.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [Source](#source)
3. [The loop](#the-loop)
4. [Memory systems as human source concepts](#memory-systems-as-human-source-concepts)
5. [Decomposition dimensions](#decomposition-dimensions)
6. [Depth of decomposition](#depth-of-decomposition)
7. [Domain-specific decomposition sets](#domain-specific-decomposition-sets)
8. [Chance configurations](#chance-configurations)
9. [Focused and diffused attention](#focused-and-diffused-attention)
10. [Default-mode and central-executive contributions](#default-mode-and-central-executive-contributions)
11. [Recomposition requirements](#recomposition-requirements)
12. [Iteration and the delta ledger](#iteration-and-the-delta-ledger)
13. [Prohibited claims](#prohibited-claims)

## Epistemic legend

`[S]` source claim, `[D]` design inference, `[A]` agent rule, `[V]` validation result, `[?]` named in the specification but not transcribed from the source; verify before public claims.

## Source

Aditya Shukla, [HOW Ideas come alive: Decompose & Recompose](https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/), Cognition Today.

Supporting: Aditya Shukla, [15 Ways to Trigger the Brain's Creative Thinking Mode](https://cognitiontoday.com/creative-thinking/), Cognition Today.

## The loop

`[S]` Creative ideation can be described as decomposing available knowledge into relevant units, modifying those units under some influence, and recomposing them into a new entity. The recomposed entity can itself be decomposed, which makes ideation iterative rather than a single flash.

| Stage | Agent-side operation `[A]` |
| --- | --- |
| Decompose | Isolate the relevant components, properties, functions, relationships, assumptions, constraints, examples, techniques, and experiences |
| Influence / modify | Apply goals, perspective changes, construal shifts, constraints, analogies, chance combinations, or another selected operator |
| Recompose | Combine the modified units into a new coherent form |
| Iterate | Treat the recomposed form as a new decomposable entity, and repeat only while improvement remains available |

`[D]` The value of making this explicit for an agent is inspectability. A model asked to "be creative" produces output whose novelty cannot be attributed or steered. A model that names its units, states which one it changed, and states which relation it rewired produces variation that a user can direct.

`[A]` If you cannot say which unit changed and which relation changed, you have not recomposed. You have paraphrased.

## Memory systems as human source concepts

`[S]` The source describes ideation as drawing on long-term memory for material and working memory for the active manipulation of that material. Capacity limits on the active workspace shape how much can be combined at once.

`[D]` The agent-side analogue is the context window and the actively referenced subset of it. This is a functional resemblance, not the same mechanism.

`[A]` Never write that the agent is holding units in working memory, retrieving from long-term memory, or consolidating. Write that material is present in context, retrievable through a tool, or absent.

`[A]` Respect the capacity insight operationally: a decomposition of forty units is not more creative than one of seven. It is less usable and it makes relation-level manipulation impossible.

## Decomposition dimensions

`[A]` Select only the dimensions relevant to the domain. Selecting all of them is a symptom of not having understood the artifact.

- Components or modules
- Functions and intended effects
- Relationships and dependencies
- Sequence or narrative causality
- Constraints and invariants
- Assumptions and implied rules
- Sensory properties
- Emotional tone
- Aesthetic grammar
- Audience or stakeholder perspective
- Domain conventions
- Available resources and by-products
- Existing examples and analogues
- Failure evidence

`[D]` Assumptions and implied rules are the highest-yield dimension for stuck problems, and the one most often skipped, because assumptions are invisible from inside the representation that contains them.

## Depth of decomposition

`[S]` Decomposition can be shallow or deep, and the depth changes what becomes available for recombination. Breaking an idea into its parts exposes relations that the whole concealed.

`[A]` Choose depth deliberately:

| Depth | What it exposes | Risk |
| --- | --- | --- |
| Shallow | Obvious swappable parts | Variants stay conventional |
| Medium | Functions, roles, and relations between parts | Usually the productive level |
| Deep | Primitive properties and atomic attributes | The organizing structure disappears and recomposition produces noise |

`[A]` Do not atomize past the level at which the artifact's organizing principle is still visible. If the parts can no longer be told apart by function, you have gone too deep.

`[D]` The failure at deep decomposition is specific: recombining primitives generates enormous variety with almost no coherence, and the convergence step then has nothing to select on.

## Domain-specific decomposition sets

`[A]` Starting sets. Adapt rather than apply mechanically.

| Domain | Units |
| --- | --- |
| Story | Motivation, conflict, causal turn, perspective, setting, tone, symbol, ending |
| Design | Hierarchy, shape, colour role, interaction, rhythm, constraint, audience |
| Code | Responsibilities, state transitions, dependencies, assumptions, data flow, failure modes, interface contracts |
| Product or concept | Job to be done, user, mechanism, differentiator, cost structure, distribution, constraint |
| Argument | Claim, warrant, evidence, scope condition, countercase, consequence |

## Chance configurations

`[S]` Randomly or unexpectedly juxtaposing units can produce configurations that deliberate search would not reach. Novel combinations arise partly from encountering pairings that were not being looked for.

`[A]` Pair distant or unlikely units on purpose, then immediately test whether the relation between them does any work. A random pairing that survives a relevance test is an idea. One that does not is noise.

`[A]` Never present an untested random pairing as a result. The test is the operator, not the randomness.

`[D]` This is the operator most often faked. Producing a surprising juxtaposition is easy for a language model; producing one whose relation holds under examination is the actual task.

## Focused and diffused attention

`[S]` Creative work draws on both narrowly focused attention and a looser, more diffused mode in which associations range more widely. Neither mode alone accounts for ideation.

| Mode | Source function `[S]` | Agent-side operation `[A]` |
| --- | --- | --- |
| Focused | Directed search, evaluation, refinement | Optimize within the current representation; converge; execute |
| Diffused | Loose association, distant material, unexpected relations | Sample material outside the current neighbour set; suspend fit-checking temporarily |

`[A]` Diffusion is a bounded phase, not a licence. Enter it deliberately, generate, then reintroduce the objective during convergence. Do not deliver diffused-phase material as a finished answer.

## Default-mode and central-executive contributions

`[S]` The source attributes contributions to both the default-mode network, associated with spontaneous and self-generated thought, and the central executive network, associated with directed control, with creative output arising from their interaction.

`[D]` This is a claim about human neural systems. The transferable structure is only the two-phase alternation between loose generation and directed control, which the agent implements as divergence and convergence phases.

`[A]` Never write that the agent activates a default-mode network, engages an executive network, or has neural modes. Describe the phase: divergent generation or convergent selection.

`[?]` The source's detailed treatment of these networks is not transcribed in the master specification. Verify before making any public claim about the neuroscience.

## Recomposition requirements

`[A]` Each recomposed candidate must specify or embody all five:

1. The organizing principle that holds it together.
2. Which units changed.
3. Which relations changed.
4. Which invariants stayed fixed.
5. Why the result is meaningfully different, in terms of structure rather than wording.

`[A]` Coherence is part of recomposition, not a later cleanup step. A combination that has not re-established internal consistency is an unfinished candidate.

## Iteration and the delta ledger

`[S]` A recomposed entity is itself decomposable, which is what makes ideation iterative.

`[A]` When iterating, keep a delta ledger: what changed this round, what stayed fixed, what was rejected, and why. Preference evidence from the user belongs in this ledger and outranks generic aesthetic convention.

`[A]` Stop iterating when the user selects a direction, the locked criteria are met, new variants repeat exhausted operators, or further novelty would cost coherence, fidelity, feasibility, or alignment with what the user has already approved.

`[D]` Without a delta ledger, repeated revision regresses: an element the user approved in round two quietly disappears in round five, and the project cycles instead of converging.

## Prohibited claims

- Do not say the agent has working memory, long-term memory, a default-mode network, a central executive, incubation, or insight.
- Do not present the human neural account as a description of how the model produced the output.
- Do not treat surprise as evidence of quality.
- Do not describe synonym substitution, reordering, or tonal adjustment as recomposition.

`[V]` untested. No forward evaluation has been recorded for this model.
