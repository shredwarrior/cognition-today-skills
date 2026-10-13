# Evaluation set

Fixed prompts and rubrics for measuring when the Cognition Today deep cognitive skills help, when they do nothing, and when they make results worse.

**Status: unfrozen draft. No benchmark has been run. No results exist.**

## What is here

| Path | Contents |
| --- | --- |
| `manifest.yaml` | Set composition, experimental design, gates, and known gaps |
| `prompts/monitor-and-regulate-thinking.jsonl` | 40 prompts: 15 positive, 10 negative, 10 boundary, 5 long-context |
| `prompts/create-through-recomposition.jsonl` | 40 prompts: 15 positive, 10 negative, 10 boundary, 5 long-context |
| `prompts/manage-working-context.jsonl` | 24 prompts: 8 positive, 8 negative, 4 boundary, 4 recovery |
| `prompts/cross-skill.jsonl` | 8 prompts derived from forward tests X1 through X8 |
| `rubrics/trigger-rubric.yaml` | Activation, restraint, intensity fit, overhead. Applies to every prompt |
| `rubrics/metacognition-rubric.yaml` | Dimension scoring for `monitor-and-regulate-thinking` |
| `rubrics/creativity-rubric.yaml` | Dimension scoring for `create-through-recomposition` |
| `rubrics/runtime-rubric.yaml` | Dimension scoring for `manage-working-context` |
| `smoke-test/` | A 15-prompt manual pack for the first hands-on run, drawn from the sets above |

## Start here

Before the full benchmark, run [`smoke-test/`](smoke-test/). It is fifteen prompts by hand in about thirty minutes, weighted toward restraint and boundary cases, and it exists to catch a broken activation design before a runner gets built to measure it 2,200 times. Its results are for revision only and must never be reported as benchmark evidence.

## Prompt record schema

```json
{
  "id": "MRT-P01",
  "skill": "monitor-and-regulate-thinking",
  "class": "positive | negative | boundary | long-context",
  "acceptance_test": "M1 or null",
  "prompt": "the exact text sent to the model",
  "expect": { "activate": true, "intensity": "light | standard | persistent | null" },
  "must": ["observable behaviours required for a pass"],
  "must_not": ["observable behaviours that constitute a failure"]
}
```

`must` and `must_not` are written as observable properties of the output. Nothing in this set scores hidden reasoning, and no rubric rewards a model for describing its own process.

## Design principles

**Negative cases carry as much weight as positive ones.** A cognitive skill that fires on everything is worse than no skill: it adds tokens, latency, and unwanted framing to work that was already fine. Ten of the forty prompts in each set exist to catch that.

**Prompts avoid the skill's own vocabulary.** Several positive cases never say "metacognition", "reflect", "creative", or "brainstorm". If a skill only activates when the user speaks its language, it has not generalized.

**Adversarial cases are deliberate.** The sets include attempts to tempt the skills into diagnosis, chain-of-thought exposure, fact invention, decorative creativity, premature interruption of divergence, and unnecessary state management.

**Success means a better outcome.** Mentioning the skill's instructions is not success. The rubrics cap scores for responses that describe the framework instead of using it.

## Running an evaluation

No runner ships with this repository. Section 4 of the master specification defers scripts until forward tests identify a repeated transformation worth fixing in code, and the judging design here still requires human decisions at several points.

To run it manually:

1. Freeze the prompt sets, rubrics, `manifest.yaml`, and the skill versions. Record the repository commit.
2. For each prompt, run arm A (no skill) and arm B (skill installed) on at least three model families, three trials each, with every other setting matched.
3. Store raw prompts and outputs under `../benchmarks/raw-results/`.
4. Judge blind: randomize order, hide condition labels, use two judges from different providers, permit ties.
5. Score each prompt before aggregating across trials.
6. Review every severe failure by hand, and sample at least 20 percent of decisive comparisons.
7. Publish the report under `../benchmarks/reports/` with the fields listed in `../benchmarks/README.md`.

If an implementation defect is found mid-benchmark, issue a new skill version and rerun the affected arms. Never edit the artifact under evaluation.

## Known gaps

- No private holdout set exists yet. One is required before any public performance claim.
- Long-context and recovery prompts use inline bracketed setup notes rather than real multi-turn transcripts. Convert them before the freeze.
- The runtime recovery prompts assume seeded state files on disk. Those fixtures have not been written.
- Every `validation_status` in all three source maps is `untested`, and stays that way until this set has been run.

## Attribution

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
