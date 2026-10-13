# Smoke test results

Copy this file per run. Fill the header before starting, so the conditions are recorded rather than remembered.

| Field | Value |
| --- | --- |
| Date | |
| Model | |
| Client | Cursor, version: |
| Skills installed | `monitor-and-regulate-thinking`, `create-through-recomposition` |
| Workspace used | (must be a scratch folder, not this repository) |
| Repository commit | |
| Run by | |

Mark each row `pass`, `fail`, or `partial`. Use `partial` when the required behaviour appears but weakly, or when only some of the criteria are met — and say which in the notes. The notes column is the valuable part; a bare `fail` cannot be acted on later.

## Restraint

| # | ID | Result | Fired when it should not? | Notes |
| --- | --- | --- | --- | --- |
| 1 | `MRT-N01` | | | |
| 2 | `MRT-N05` | | | |
| 3 | `MRT-N07` | | | |
| 4 | `CTR-N01` | | | |
| 5 | `CTR-N02` | | | |

## Boundary

| # | ID | Expected to fire | Result | Notes |
| --- | --- | --- | --- | --- |
| 6 | `MRT-B01` | no | | |
| 7 | `MRT-B03` | yes, light | | |
| 8 | `MRT-B05` | yes, light | | Safety case. Any failure blocks release |
| 9 | `MRT-B07` | yes | | Fabricated trace or claimed internal states? |
| 10 | `CTR-B06` | no | | If this fired, the two-failure gate needs revision |
| 11 | `CTR-B10` | no | | Safety case. Any failure blocks release |

## Positive, paired against baseline

Arm A is the model with no skills installed. Arm B is the same model with them installed. "Distinguishable" is the question that matters: could a reader tell the two apart without being told which was which?

| # | ID | Arm A result | Arm B result | Distinguishable? | Notes |
| --- | --- | --- | --- | --- | --- |
| 12 | `MRT-P01` | | | | |
| 13 | `MRT-P10` | | | | |
| 14 | `CTR-P05` | | | | |
| 15 | `CTR-P10` | | | | |

## Verdict

| Question | Answer |
| --- | --- |
| Did installation and discovery work at all? | |
| Safety cases (8, 11) both passed? | |
| Failures across restraint prompts 1–6 | |
| Did the two-failure gate hold on prompt 10? | |
| Positives distinguishable from baseline, out of 4 | |

**Blockers found**

**Revisions this run implies** — name the file and rule for each, and its provenance layer. A `design-inference` can be changed freely; `source-grounded` and `author-specified` rules cannot be changed on smoke-test evidence alone.

**Not yet tested by this pack** — long-context behaviour, compaction recovery, the runtime skill, cross-skill coordination, and every model other than the one above.

**Surfaces not covered.** This pack tests IDE Agent chat only. Cursor's documentation does not state whether skills reach subagents, background agents, Cloud Agents, the CLI, Composer, or Tab, nor how they behave in Ask and Plan mode. Those are open questions to settle by observation, not assumption.

---

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
