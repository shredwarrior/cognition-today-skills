# Source notes: creative cognition

Attributed notes for the three canonical sources of this skill, organized under the sources' own section headings.

## Sources

- **A** — Aditya Shukla, [Creative Cognition: The Construal Level Theory & Psychological Distance](https://cognitiontoday.com/creative-cognition-construal-level-theory-psychological-distance/), Cognition Today.
- **B** — Aditya Shukla, [15 Ways to Trigger the Brain's Creative Thinking Mode](https://cognitiontoday.com/creative-thinking/), Cognition Today.
- **C** — Aditya Shukla, [HOW Ideas come alive: Decompose & Recompose](https://cognitiontoday.com/how-ideas-come-alive-decompose-recompose/), Cognition Today.

## Contents

1. [Status of this file](#status-of-this-file)
2. [Creative Cognition and the Construal Level Theory (A)](#creative-cognition-and-the-construal-level-theory-a)
3. [Examples of construal levels (A)](#examples-of-construal-levels-a)
4. [Psychological distance and creativity (A)](#psychological-distance-and-creativity-a)
5. [What is creativity? (B)](#what-is-creativity-b)
6. [The fifteen creative-thinking approaches (B)](#the-fifteen-creative-thinking-approaches-b)
7. [The Decompose-Recompose model of ideation (C)](#the-decompose-recompose-model-of-ideation-c)
8. [Randomness-induced creativity (C)](#randomness-induced-creativity-c)
9. [Depth of decomposition (C)](#depth-of-decomposition-c)
10. [Diffused thinking (C)](#diffused-thinking-c)
11. [Default-mode and central-executive influences (C)](#default-mode-and-central-executive-influences-c)
12. [What can we make of these processes? (C)](#what-can-we-make-of-these-processes-c)
13. [Verification ledger](#verification-ledger)

## Status of this file

This build was compiled from the master implementation specification, which names the source headings and states the claims the agent rules depend on, but does not reproduce the article text. Each section records the **relied-upon claim**, what **depends on it**, and a **verification** status of `spec-attributed` or `pending`.

Nothing below is a quotation. Before public release, read all three articles and replace `pending` entries with attributed notes and, where useful, short quotations within fair-use limits.

## Creative Cognition and the Construal Level Theory (A)

**Relied-upon claim.** The same object can be represented at different levels of construal, and concrete versus abstract construals expose different properties and conceptual associations.

**Depends on it.** `vary-construal-level`; the three-level table and the traversal rule in `construal-distance-model.md`.

**Verification.** `spec-attributed`. Anchored at `#creative-cognition-the-construal-level-theory`.

**Caveat preserved.** Higher construal is not presented by the source as uniformly better. The skill is forbidden from treating abstraction as a general performance enhancer.

## Examples of construal levels (A)

**Relied-upon claim.** Construal levels can be illustrated by describing a single object at low, intermediate, and high levels of abstraction.

**Depends on it.** The worked bicycle example and the worked traversals in `construal-distance-model.md`.

**Verification.** `pending`. The specification requires that construal distinctions be illustrated but does not supply the source's own examples. All examples in this package are compiler-written and must not be attributed to the article.

## Psychological distance and creativity (A)

**Relied-upon claims.**

1. Psychological distance and construal level are linked; greater distance is associated with more abstract construal.
2. Distance varies along informational, personal, temporal, and spatial dimensions.
3. The relationship between construal, distance, and creative benefit is not uniform; analytical and holistic processing styles interact with it.

**Depends on it.** The four-dimension distance table and the analytical/holistic caveat in `construal-distance-model.md`.

**Verification.** `spec-attributed` for claims 1-3, since the specification requires the four distance types and explicitly requires that the analytical/holistic caveat be preserved. `pending` for the underlying empirical evidence, which this package makes no claims about.

## What is creativity? (B)

**Relied-upon claim.** Creativity involves producing something that is both novel and useful or appropriate to its context, rather than novelty alone.

**Depends on it.** `select-creative-operator`; the Step 1 requirement to define evaluation criteria before generating; the prohibition on scoring novelty alone.

**Verification.** `spec-attributed`. Anchored at `#what-is-creativity-really`. The specification's own evaluation guidance repeatedly pairs novelty with usefulness and coherence.

## The fifteen creative-thinking approaches (B)

**Relied-upon claim.** The article presents fifteen approaches that facilitate creative thinking, including default-mode activation, chance configurations, limiting resources, transformation, combination, perspective change, changing processing level, flexible attention, retrieving more material, cross-domain borrowing, overcoming functional fixedness, lateral thinking, assuming multiple solutions, diffused thinking, and improvisation.

**Depends on it.** The entire operator matrix in `creative-operator-matrix.md`; `escape-persistent-fixedness`, anchored at `#overcome-functional-fixedness`.

**Verification.** `spec-attributed` for the fifteen operator names and for the functional-fixedness mechanism. `pending` for the source's own description of each approach; the agent-side translation, preferred condition, and guardrail columns are compiler-written design inferences.

**Caveat preserved.** The source presents these as available approaches, not as an ordered procedure. Applying all fifteen would misrepresent the source as well as produce bad output.

## The Decompose-Recompose model of ideation (C)

**Relied-upon claim.** Creative ideation can involve decomposing available knowledge into relevant units, modifying them, and recombining them into a new entity.

**Depends on it.** `decompose-creative-object`; the loop in `decompose-recompose-model.md`; Steps 4 and 8 of the procedure in `SKILL.md`.

**Verification.** `spec-attributed`. Anchored at `#the-decompose-recompose-model-of-ideation`.

## Randomness-induced creativity (C)

**Relied-upon claim.** Chance or unexpected juxtaposition of units can produce configurations that deliberate, directed search would not reach.

**Depends on it.** Operator 2 in `creative-operator-matrix.md`; the chance-configuration section of `decompose-recompose-model.md`.

**Verification.** `spec-attributed`. The requirement that randomness be followed by relevance testing is a compiler-added guardrail, not a source claim.

## Depth of decomposition (C)

**Relied-upon claim.** Decomposition can be carried out at different depths, and the depth changes which relations become available for recombination.

**Depends on it.** The depth table and the anti-atomization rule in `decompose-recompose-model.md`; Step 5 of the procedure.

**Verification.** `spec-attributed` for the existence and relevance of depth. `pending` for the source's own account of how to choose depth; the shallow/medium/deep table is compiler-written.

## Diffused thinking (C)

**Relied-upon claim.** Creative work draws on both focused attention and a looser, diffused mode in which associations range more widely.

**Depends on it.** Operators 8 and 14 in `creative-operator-matrix.md`; the focused/diffused table in `decompose-recompose-model.md`; the divergence phase in `SKILL.md`.

**Verification.** `spec-attributed`.

## Default-mode and central-executive influences (C)

**Relied-upon claim.** The source attributes contributions to both the default-mode network, associated with spontaneous self-generated thought, and the central executive network, associated with directed control, with creative output emerging from their interaction.

**Depends on it.** Operator 1 in `creative-operator-matrix.md`; the divergence/convergence phase separation.

**Verification.** `spec-attributed` for the attribution of both networks. `pending` for the source's detailed neuroscience.

**Caveat preserved and hardened.** This is a claim about human neural systems. The package prohibits any statement that the agent activates, engages, or possesses these networks. Only the two-phase alternation transfers.

## What can we make of these processes? (C)

**Relied-upon claim.** A recomposed entity can itself be decomposed, which makes ideation iterative rather than a single event.

**Depends on it.** `recompose-variants`; the iteration rule and delta ledger in `decompose-recompose-model.md`; Step 11 of the procedure.

**Verification.** `spec-attributed`. Anchored at `#what-can-we-make-of-these-processes`.

## Verification ledger

| Section | Source | Status | Blocking public claims? |
| --- | --- | --- | --- |
| Creative Cognition and the Construal Level Theory | A | `spec-attributed` | No |
| Examples of construal levels | A | `pending` | Yes, if any example is attributed to the article |
| Psychological distance and creativity | A | `spec-attributed` | No |
| What is creativity? | B | `spec-attributed` | No |
| The fifteen creative-thinking approaches | B | Partial | Yes, for per-operator descriptions |
| The Decompose-Recompose model of ideation | C | `spec-attributed` | No |
| Randomness-induced creativity | C | `spec-attributed` | No |
| Depth of decomposition | C | Partial | Yes, for the depth-selection guidance |
| Diffused thinking | C | `spec-attributed` | No |
| Default-mode and central-executive influences | C | Partial | Yes, for any neuroscience claim |
| What can we make of these processes? | C | `spec-attributed` | No |

Resolve every `pending` and `Partial` row against the articles before the first public release.
