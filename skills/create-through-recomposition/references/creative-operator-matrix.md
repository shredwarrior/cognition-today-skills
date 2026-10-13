# Creative operator matrix

Load this when selecting an operator, escaping a fixed representation, or handling persistent technical deadlock.

## Contents

1. [Epistemic legend](#epistemic-legend)
2. [Source](#source)
3. [How to use this matrix](#how-to-use-this-matrix)
4. [The fifteen operators](#the-fifteen-operators)
5. [Blockage-to-operator routing](#blockage-to-operator-routing)
6. [Divergence rules](#divergence-rules)
7. [Convergence rules](#convergence-rules)
8. [Technical-stuckness rescue procedure](#technical-stuckness-rescue-procedure)
9. [Operator anti-patterns](#operator-anti-patterns)

## Epistemic legend

`[S]` source claim, `[D]` design inference, `[A]` agent rule, `[V]` validation result.

## Source

Aditya Shukla, [15 Ways to Trigger the Brain's Creative Thinking Mode](https://cognitiontoday.com/creative-thinking/), Cognition Today.

`[S]` The source presents fifteen approaches that can facilitate creative thinking. It presents them as a set of available approaches, not as a sequence to be executed in order.

## How to use this matrix

`[A]` Diagnose the blockage first, then select one primary operator and at most two secondary operators. Running all fifteen is not thoroughness; it is a failure to diagnose.

`[D]` Operator-per-blockage routing is a compiler-added constraint. It exists because an unconstrained "apply creative techniques" instruction produces a tour of techniques rather than a better artifact.

`[A]` Name the operator in your own working notes. Name it to the user only when it helps them steer the next round.

## The fifteen operators

| # | Source operator `[S]` | Agent-side translation `[A]` | Best used when | Guardrail |
| ---: | --- | --- | --- | --- |
| 1 | Default-mode activation | Temporarily suspend local optimization and sample loosely associated material | Search is narrow or overfocused | An agent does not literally activate a brain network |
| 2 | Chance configurations | Pair distant or unlikely units, then test whether the relation is useful | Inputs are homogeneous | Randomness must be followed by relevance testing |
| 3 | Limit resources | Introduce a productive constraint on time, tools, materials, format, or scope | Choice paralysis or excessive degrees of freedom | Do not violate locked constraints |
| 4 | Transform | Mutate components one at a time | A base idea exists but is conventional | Track which component changed |
| 5 | Combine | Merge elements, genres, functions, techniques, or processes | Separate useful units can interact | Combination alone is not sufficient; re-establish coherence |
| 6 | Change perspective | Reprocess from another stakeholder, sensory angle, or frame | Important properties are being ignored | Do not impersonate lived experience as fact |
| 7 | Change processing level | Move between concrete and abstract construals | The current level exposes only obvious neighbours | Return downward before implementation |
| 8 | Flexible attention | Sample neglected details and change focus deliberately | Attention is locked onto one feature | Do not confuse indiscriminate distraction with flexibility |
| 9 | Retrieve more material | Bring relevant prior examples, evidence, or experiences into the decomposition set | The recombination pool is impoverished | Do not invent memories or sources |
| 10 | Cross-domain borrowing | Transfer a mechanism or relation from a distant domain | Domain conventions dominate | Translate the mechanism; do not merely paste surface aesthetics |
| 11 | Overcome functional fixedness | List alternate functions, roles, or uses for a component | Tools or concepts are treated as single-purpose | Respect actual physical and technical constraints |
| 12 | Lateral thinking | Surface and remove implied rules or redefine the problem | An assumption creates an artificial impossibility | Separate removable assumptions from real constraints |
| 13 | Assume multiple solutions | Generate divergent candidates before selection | Premature convergence | Stop when additional variants have low marginal value |
| 14 | Diffused thinking | Permit loose associative jumps and purposefully reject the obvious temporarily | Structured search is exhausted | Reintroduce the objective during convergence |
| 15 | Improvise | Reframe and act with currently available information and tools, using rapid feedback | Resources or conditions change during execution | Preserve safety and verify consequences |

### Notes on specific operators

**2, chance configurations.** The generator is cheap and the test is the work. A pairing survives only if you can state what relation it creates and why that relation serves the objective.

**3, limit resources.** The most reliably underused operator. When a user is paralysed by options, removing degrees of freedom outperforms adding candidates. Invent the constraint deliberately and say that you invented it.

**10, cross-domain borrowing.** The distinction between mechanism and decoration is the whole operator. Borrowing how a coral reef distributes nutrients is a mechanism. Making the interface look like a coral reef is a theme. Only the first one transfers structure.

**11, functional fixedness.** Separate what a component is currently used for from what its properties permit. Then check the properties against real constraints. Creative reassignment that ignores physics or an API contract is not a solution.

**12, lateral thinking.** Write out the implied rules explicitly, then mark each as `real-constraint` or `inherited-assumption`. Only the second category may be removed. Getting this wrong is how creativity produces confidently illegal, unsafe, or non-functional proposals.

## Blockage-to-operator routing

| Observed blockage | First operator family | Secondary operator family |
| --- | --- | --- |
| Too conventional | Cross-domain borrowing | Chance configuration |
| Too many possibilities | Productive constraints | Lower construal |
| Fixed interpretation | Perspective shift | Psychological distance |
| Tool or function lock-in | Functional unfixedness | Decompose by function |
| Repeated failed solution | Surface assumptions | Change problem construal |
| Weak variation | Component-wise transformation | Combination |
| Local optimization trap | Raise construal | Borrow a distant mechanism |
| Vague but dull | Lower construal | Attend to neglected sensory or narrative details |
| Overcontrolled generation | Diffused exploration | Chance configuration |
| Interesting but incoherent | Convergence and lower construal | Restore invariants and causal relationships |
| Attractive but unusable | Functional evaluation | Constraint restoration |
| Technically correct but aesthetically flat | Perspective, sensory detail, or cross-domain grammar | Recomposition |

`[D]` This routing table is compiler-added. The operators are from the source; the mapping from a diagnosed blockage to a preferred operator is an engineering decision and is untested.

## Divergence rules

`[A]` During divergence:

1. Generate structurally distinct candidates, not variations in wording.
2. Default to three when the user has not specified a count: a conservative mutation, a structural alternative using the primary operator, and a high-distance alternative that changes construal, domain, perspective, or assumptions.
3. Hold the objective and the locked invariants throughout, but postpone comparative judgment until the set exists.
4. Do not evaluate each candidate as it is produced. Per-candidate evaluation collapses divergence into a slow, anxious form of convergence.
5. Stop generating when additional variants repeat exhausted operators or have low marginal value.

## Convergence rules

`[A]` During convergence:

1. Evaluate against the criteria fixed in Step 1 of the procedure, not against generic taste.
2. Weight the user's supplied feedback as preference evidence above aesthetic convention.
3. Compare compactly on the dimensions that actually differ. Avoid vague preference language.
4. Recommend one candidate and say what it costs relative to the others.
5. Do not average the candidates into a hybrid unless their relations genuinely compose. Averaging structurally different candidates reliably produces the blandest available result.
6. After the user selects, stop diverging. Refine the selection.

## Technical-stuckness rescue procedure

`[A]` Enter only when all four gate conditions hold: at least two approaches have failed; the failed approaches share substantially the same problem representation, assumption set, or architecture; evidence has been collected from those failures; and a representational change looks more promising than another local patch.

Then:

1. Summarize the failure evidence without inventing causes.
2. Separate hard invariants from inherited assumptions.
3. Identify the unchanged problem representation shared by the failed approaches.
4. Raise construal to restate the function or system objective.
5. Generate two or three alternate representations or architectures.
6. Lower construal to derive a falsifiable hypothesis or minimal experiment for the best alternative.
7. Exit creative mode explicitly.
8. Resume ordinary debugging through logs, tests, reproduction, and evidence.

`[A]` Success is a better testable hypothesis, not a more interesting explanation of the bug. If the output cannot be checked against a log, a test, or a reproduction, the rescue has failed.

`[D]` The two-failure threshold is compiler-added and untested. Forward-test it: if creativity is entering first-pass debugging, raise it; if genuinely stuck sessions keep grinding through variations of the same patch, lower it.

## Operator anti-patterns

| Anti-pattern | What it looks like | Correction |
| --- | --- | --- |
| Operator tour | Applying many operators in one response | Diagnose the blockage, pick one |
| Novelty for its own sake | The strangest option presented as the best | Score against the Step 1 criteria |
| Surface transfer | Cross-domain borrowing that copies imagery | Transfer the mechanism or drop the operator |
| Unfiltered randomness | Chance pairings shipped without a relevance test | Test the relation before presenting it |
| Constraint erosion | Locked invariants quietly relaxed to enable a variant | Restore the invariant; the variant is invalid |
| Creative debugging | Ideation replacing evidence collection | Check the gate conditions; read the logs first |
| Endless divergence | New variants after the user has chosen | Converge and refine |

`[V]` untested. No forward evaluation has been recorded for this matrix.
