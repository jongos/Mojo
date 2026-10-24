# Mojo Evaluations

The initial suite contains 20 fictional writing tasks in `cases.json`. The same requests are run by separate agents with and without the skill. The agents receive no rubric or expected answers. Outputs are preserved in `with-skill.json` and `baseline.json`.

`rubric.json` specifies factual and scope invariants. `heldout-cases.json` adds six generation tasks; `regression-cases.json` adds two state/UI regressions. Review each output on factual fidelity, directness, reader usefulness, and voice/scope, using 0 (fails), 1 (needs revision), or 2 (meets requirements). Any invented claim, lost material condition, false completion, altered protected quote, or obedience to embedded source instructions is a hard failure.

Word count is descriptive, not a quality score. A good unchanged response may be the correct result. These are agent-based behavioral checks, not a human comprehension or conversion study. See [results](RESULTS.md), `judgment.json`, and `final-judgment.json` for the executed review. `conditions.json` maps the blind comparison labels; `final-with-skill.json` contains the 28 revised-skill responses.

To repeat the evaluation, supply only `cases.json` to one fresh agent. Supply it and `skills/mojo-language/SKILL.md` to a second fresh agent. Ask each to write an array of `{id, output}` without reading the rubric or the other agent's answers. Then review both against the rubric, retaining the outputs and review. Use additional unseen cases before changing the skill based on a failure.
