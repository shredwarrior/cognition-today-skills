# Benchmarks

**Status: no benchmark has been run. This directory contains a template and empty result directories.**

Any performance claim about these skills that is not backed by a filled `run-manifest.json` and raw results in this directory is unsupported. That includes claims made in the root README, in a launch article, or anywhere else.

## Contents

| Path | Purpose |
| --- | --- |
| `run-manifest.json` | Template recording the exact artifact, models, arms, judging setup, costs, and gate outcomes for one run |
| `raw-results/` | Machine-readable prompts, outputs, judgments, and scores. Empty |
| `reports/` | Human-readable analysis per run. Empty |

## What a report must contain

Every benchmark report published from this directory includes all of the following. A report missing any of them is not publishable.

1. Repository commit and skill versions.
2. Model, provider, harness, and relevant configuration for every arm.
3. Prompt-set version and any exclusions, with reasons.
4. Number of trials, ties, failures, and missing runs.
5. Aggregate and per-model results.
6. Positive, negative, boundary, and long-context breakdowns.
7. Confidence intervals or another appropriate uncertainty estimate.
8. Token and latency costs per arm.
9. Judge agreement and a position-bias check.
10. Human-review sampling method and coverage.
11. Raw machine-readable prompts, outputs, judgments, and scores.
12. Known limitations and representative losing examples.

## Language rules for reporting

Write what was measured:

- "Preferred in 64 percent of decisive blinded comparisons on this prompt set."
- "Improved median rubric score for positive-trigger planning prompts on two of three model families."

Do not write:

- "Makes any model creative."
- "Scientifically proves metacognition improves AI."
- "Model-agnostic performance gains."

Model-agnostic means the capability is expressed in an open, model-neutral skill format and has been tested across multiple model families. It does not mean behaviour is identical across them.

## Reporting discipline

**Do not average away a serious regression.** Severe failures — diagnosis of a person, fabricated reasoning traces, invented facts, destruction of user-approved content, safety or compliance violations, claims that the agent possesses human cognition — are reported separately and individually, even when the aggregate passes every gate.

**Report losses.** Include representative cases where the baseline arm beat the skill arm. A benchmark with no losing examples has either not been run honestly or has not been run on hard enough prompts.

**Never edit the artifact mid-run.** If a defect appears during a benchmark, cut a new skill version and rerun the affected arms.

## Attribution

Part of Simulated Cognitive Skills for LLM Creativity and Metacognition, by Aditya Shukla, [Cognition Today](https://cognitiontoday.com). Licensed CC BY-NC-SA 4.0.
