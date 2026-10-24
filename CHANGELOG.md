# Changelog

## 2026-10-24 - Document Editing and Conversation Repetition Control

- **Changed:** Added document-level editing, scope-sensitive revision, conversation repetition control and a stopping rule for effective text. Strengthened preservation of chronology, time granularity and attribution.
- **Added:** A 60-case, four-condition benchmark; anonymous primary and reversed-order reviews; two retained follow-up runs with 12 additional chronology cases; and second-pass editing checks.
- **Why:** Reduce repeated ideas across sections and updates without losing meaning, useful context or the author's voice.
- **Validation:** Retained 400 generated responses, including failures and revisions. Final 72-case review found no critical failures and two noncritical issues; 71/72 comprehension checks passed. All eight final second-pass edits remained unchanged and passed independent review. Four harness tests, frozen-input checks, skill structure and changed-document links passed. The original comparison does not establish superiority; see [the full results](evaluations/v2/RESULTS.md).

## 2026-10-24 - Meaning-Preserving Conditions and Bounds

- **Changed:** Added guidance for necessary versus sufficient conditions, logical operators, bounds, conflicting sources and multilingual editing.
- **Added:** Twelve retained edge-case responses and reviews.
- **Why:** Concise edits can change eligibility or claim strength through a single connective.
- **Validation:** Twelve responses reviewed; one initial response failed the necessary/sufficient distinction and one needed a clearer OR. Both revised outputs passed informed review; no independent efficacy claim.


## 2026-10-24 — Mojo Marketing Copy Review

**Changed:** Tightened product introductions and removed repeated qualifications and explanations. Preserved setup requirements, commands, material claims and each project’s voice.

**Added:** None.

**Why:** Help readers understand the product and choose their next action with less reading.

**Validation:** Local links and command preservation checked. Mojo has no standalone landing page; its README and Hex Men listing were reviewed. Canonical skill instructions and runtime behavior are unchanged.
