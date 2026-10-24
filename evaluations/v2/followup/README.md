# Chronology follow-up

This is a separate revision after the original candidate's M08 failure. Read [the decision](decision.md) before interpreting these results. The original comparison remains frozen in the parent directory.

`skill/` preserves the revised instructions. `instruction-hashes.json` was written before reading the 12 independently authored supplemental cases. `input-hashes.json` freezes the cases, rubrics and generation packets. Hashes normalize text line endings; inventory readers accept Windows and POSIX path separators.

From the parent `v2` directory:

1. Run `python followup.py verify` to check this historical revision's frozen inputs. The later `--run final-revision` verifies the final revision against the shipped skill as well.
2. Give fresh generators only the three files in `packets/`: 12 pilot regression requests, 48 remaining regression requests and 12 new supplemental requests. Retain their responses in `outputs/` with matching filenames. The original 60 cases are regression coverage, not new held-out evidence.
3. Run `python followup.py review` to validate outputs and prepare reviewer packets. Give the two 30-case regression packets and the 12-case supplemental packet to separate fresh reviewers. They receive requests, rubrics and responses, without skill instructions, prior results or revision details.
4. Preserve judgments in `judgments/`, then run `python followup.py summarize`. Report critical failures separately from comprehension-question success and style scores.

The generators and reviewers make no external calls on behalf of fictional users. The Python tools prepare and validate artifacts; they do not invoke a model or grade prose. See [the consolidated results](../RESULTS.md) for the executed outcome and scope.
