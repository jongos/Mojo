# Document and conversation benchmark

Start with [the protocol](protocol.md), [corpus design](design.md) and the executed results in `RESULTS.md`. This directory keeps a new 60-case benchmark separate from the earlier evaluation. The current condition includes the previously added meaning-preservation guidance; it is not the initial published skill.

The original candidate failed a chronology case. Its [first follow-up](followup/README.md) and [final revision](final-revision/README.md) preserve the subsequent instruction changes and regression results separately. The final revision matches the shipped skill; the original condition snapshots intentionally remain unchanged.

## Reproduce

1. Use Python 3.10 or later. `python harness.py verify` checks corpus structure and frozen input hashes. Text hashes normalize line endings to LF so Windows and Git checkouts agree. A changed file set is rejected, including newly added instruction references.
2. Give a fresh generator only its assigned `packets/CONDITION-PHASE.json`. Conditions are baseline, generic, current and candidate; phases are pilot (12) and remaining (48). Preserve each response as `{id, output}` in `outputs/CONDITION-PHASE.json`. Never expose `rubric.json`, `build_corpus.py`, condition maps, competing responses or earlier judgments to generators.
3. Run `python harness.py check --outputs outputs/CONDITION-PHASE.json --phase PHASE`. Missing protected spans are review flags, not an automatic semantic grade. Run the remaining cases only after the pilot decision is recorded.
4. Run `python review_packets.py PHASE` to generate anonymous review packets. Give the normal and reversed packets to separate reviewers without condition maps or prior judgments. Review against the protocol and retain both judgments. Do not describe model judgments as human-reader results.
5. Keep requests, outputs, judgments, disagreements and corrections together. Record actual scope and unresolved failures in the results; a clean JSON file does not establish writing quality.

`prepare` creates condition packets from the snapshots and freezes inputs. It refuses a changed frozen file set or content. An intentional instruction revision needs a new preserved snapshot/run rather than overwriting this run's history. `build_corpus.py` reproduces the original fixed corpus; do not use it to rewrite a completed evaluation.

Run `python summarize.py` to validate judgment coverage and produce descriptive condition totals in `summary.json`. It preserves ties and reports whether all primary and sampled reversed reviews are present. See [the sampling record](review-sampling.md) for the two primary review partitions and selected follow-up cases.

Run `python -m unittest discover -p 'test_*.py' -v` for harness and summary regressions. The harness makes no model calls and has no third-party Python dependencies. [The reader-pilot kit](reader-pilot.md) is prepared separately; it is not evidence that reader sessions occurred.
