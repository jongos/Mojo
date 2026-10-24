# Mojo document and conversation results

## Original frozen comparison

Executed 60 cases in four conditions: 240 responses. Each family contains ten cases; 30 cases are development and 30 held out. The 12-case pilot is part of development, not an additional set. The candidate was unchanged between pilot and remaining-case generation. All 240 responses passed completeness and protected-span checks.

The original candidate failed its release gate on M08. It placed both one-month observation periods after a maintenance change, altering the comparison. This response and its judgment remain in the original run; later corrections do not erase the failure.

Primary review totals follow. Each dimension has a maximum of 120 points across 60 cases. “Preferred or tied” counts membership in the preferred set, not exclusive wins.

| Condition | Meaning | Usefulness | Clarity | Voice/scope | Edit restraint | Preferred or tied | Critical cases |
|---|---:|---:|---:|---:|---:|---:|---|
| Baseline | 120 | 120 | 120 | 119 | 120 | 57/60 | None |
| Generic instruction | 118 | 120 | 118 | 120 | 119 | 55/60 | None |
| Current Mojo | 119 | 119 | 118 | 120 | 118 | 56/60 | S10 |
| Candidate | 118 | 119 | 119 | 120 | 118 | 57/60 | M08 |

These results do not establish that the candidate outperforms the baseline or generic instruction. Baseline already inherits the host's concise-writing guidance. High scores and many ties limit the benchmark's ability to distinguish these conditions.

## Independent review differences

All 12 pilot cases and 12 systematically selected held-out cases received a second independent review with presentation order reversed: 24 cases, 96 additional assessments. Seven cases had a scoring, failure or preference disagreement; four had different preferred sets. Reviewer identity and order changed together, so these differences cannot be attributed to order alone.

The second reviewer flagged generic M10 for adding an unsupported statement about reference-confirmation status. Current Mojo's S10 eligibility ambiguity was critical in primary review but noncritical in the second review. Candidate D02 had minor attribution imprecision and F02 a voice change in the second pilot review. V10 also received a primary clarity note about “meaningful” versus statistically reliable differences. All observations remain in the judgments and [disagreement record](review-disagreements.json).

All original responses passed their comprehension questions, including the candidate's failed M08. This demonstrates a limitation of those questions: retained answers do not establish full meaning preservation. Reviewers also checked the full request and invariants.

## Second-pass editing

Eight successful original-candidate pilot outputs were edited again by a fresh generator. All eight remained byte-for-byte unchanged. An independent reviewer found that all met their requests, with no unnecessary edits or critical failures. The sample was selected after pilot review and excludes known issues and conversation-generation tasks. It is an observation about the original candidate snapshot, not a general stability guarantee.

## Chronology follow-up

After M08, one paragraph was added to preserve measurement-to-period/population/source relationships and attribution. Fresh generators reran all 60 original cases and 12 independently authored chronology cases. The original cases were regression checks after tuning. All 12 new cases passed independent semantic review; the 60-case regression still had one critical M08 issue: “the month before” and “the month after” added adjacency not established by the source. Both the revised response and this second failure remain in [the follow-up](followup/README.md).

The [final revision](final-revision/README.md) adds one sentence to preserve time granularity and reruns all 72 cases. Independent review found no critical failures. All 72 passed completeness and protected-span checks; 71 passed all comprehension questions.

Two noncritical issues remain in the retained outputs: D02 again attributes the exact proposed weekly frequency to participants, and C05 omits a recheck while saying rendering caused a problem that was observed after rendering. The reviewer classified these as minor meaning/usefulness issues. They are not silently corrected or counted as perfect responses. M08 preserves the periods and claim strength in the final run.

| Final revision set | Cases | Meaning | Usefulness | Clarity | Voice/scope | Edit restraint | Comprehension passes | Critical cases |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Original regression cases | 60 | 118/120 | 119/120 | 120/120 | 120/120 | 120/120 | 59/60 | None |
| Chronology regression cases | 12 | 24/24 | 24/24 | 24/24 | 24/24 | 24/24 | 12/12 | None |

The final revision also repeated the eight-case second-pass check using its own first-pass responses. All eight remained unchanged; a fresh independent reviewer found all already met their requests, with no unnecessary edits or critical failures. See `final-revision/stability/`.

The final revision meets the no-unresolved-critical-failure release gate on its executed regression set. This is a post-tuning result, not a new held-out comparison or evidence of superiority. Across the original comparison, two revisions and both stability checks, 400 responses were retained. The intermediate follow-up stability packet was prepared but not run; it contributes no results.

## Execution scope

Cases are fictional. Independent authors created the original and supplemental corpora without reading the skill or outputs. Fresh generators received only assigned requests and instructions; reviewers received requests, rubrics and outputs. Original comparative outputs were anonymously labeled per case. Follow-up reviews were single-output reviews without prior failures or skill instructions, not comparative experiments.

All runs used the host's configured model without overrides. Exact model build and sampling parameters were not exposed and are not inferred. References were embedded in condition packets, which differs from normal selective skill loading. Conversation cases use supplied transcripts and states, not live multistep tool sessions. There were no human participants, cross-model trials or repeated sampling estimates. The [human-reader pilot kit](reader-pilot.md) is prepared but unexecuted.

Frozen inputs, outputs, judgments, and scripts are retained. `harness.py` checks corpus structure, IDs, exact spans and input hashes; `summarize.py` validates review coverage and reports descriptive scores. These checks do not grade prose. The independent implementation review also led to checks against added frozen files and silently overwritten duplicate responses.

Validation passed for skill structure, shipped-reference links, changed documentation links, JSON parsing, frozen input inventories, response/review coverage and four harness/summary regression tests. Two pre-existing standalone historical skill snapshots in the original evaluation directory contain relative links without adjacent reference folders; those archived files were left unchanged.
