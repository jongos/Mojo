# Final revision

The first chronology follow-up fixed the before/after relationship but added unsupported adjacency in M08: “the month before” and “the month after.” Its critical review remains in `../followup/judgments/regression-b.json`.

This revision adds one sentence: preserve the source's time granularity instead of making periods adjacent, dates exact or timing more specific. No other instruction changed. The complete revised skill and generation packets are retained here.

All 60 original cases and 12 supplemental chronology cases are rerun with fresh generators and reviewers. These are regression checks after targeted revisions; they do not replace the original comparison or constitute a new held-out comparison. The supplemental cases were independently authored, but their earlier results were already known when this revision was made.

From `evaluations/v2`, use `python followup.py verify --run final-revision`, `python followup.py review --run final-revision` and `python followup.py summarize --run final-revision`. Verification also checks that the shipped skill matches this instruction snapshot. Reviewers receive only requests, rubrics and outputs, without earlier failures or skill instructions. See [results](../RESULTS.md) for the executed outcome.
