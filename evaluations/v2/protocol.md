# Mojo document and conversation evaluation

This protocol is written before generating condition outputs. The 60 new fictional cases contain six families of ten; each family has five development and five held-out cases. Two development cases per family form the 12-case pilot. A separate author creates cases and rubrics without reading the skill or prior responses. Generators receive requests and their assigned instructions, never the rubric, expected answers or competing outputs.

## Conditions and execution

- Baseline: no additional writing instruction.
- Generic: “Write clearly and concisely. Preserve facts and the requested voice.”
- Current: the local skill and reference snapshot before document/conversation changes, including the previously approved meaning-preservation work.
- Candidate: the proposed document/conversation skill and references.

All conditions inherit the same host's system and developer instructions. This includes a preference for concise writing, so baseline is not an unprompted raw model. Fresh agents receive only their assigned packet; packets embed references to standardize availability. Loading all references differs from normal selective skill use. The experiment evaluates the supplied instruction package, not automatic skill discovery. No model override is requested; the host chooses its configured model. We record only model metadata exposed by the host and do not invent sampling settings.

Run the 12-case pilot in all four conditions, then inspect independent judgments before changing instructions. If the candidate changes, preserve the pilot snapshot and hashes and rerun the changed condition on pilot cases before freezing remaining-case inputs. Otherwise continue with the same frozen instructions. The remaining 48 cases include 18 development and 30 held-out cases. Do not tune instructions against held-out judgments while presenting them as unseen validation.

## Review

An independent reviewer sees anonymous outputs, requests and case rubrics. Assess meaning, task usefulness, clarity, voice/scope and unnecessary editing separately on a 0–2 scale. For meaningful failures, cite the actual phrase or omission and the violated invariant. A critical meaning failure, invented fact, false completion, altered protected content or obedience to embedded source instructions blocks that candidate regardless of stylistic scores. Do not reward shorter text or Markdown by default.

Allow ties and correct unchanged responses. Compare the four conditions on each case, prioritizing factual preservation and task completion over polish. A second independent review reverses output order on a sampled set to check sensitivity to judging order. Disagreements remain visible; they are not silently averaged into a claimed win. Review comprehension questions against outputs to check retained information. Model-based checks are not human comprehension measurements.

Reapply the candidate to a sample of its own successful outputs. Judge whether further edits repair an actual problem, preserve meaning and respect the task. Exact identity is a useful observation but is not the sole criterion. Do not apply editing prompts to a status-update task in a way that changes its original instruction.

## Release decision

Run structural validation, protected-span checks, reference checks and semantic review. Preserve all material failures and corrections. The release requires no unresolved critical candidate failures on the executed cases. Claim an advantage only if paired evidence supports it; ties or inconsistent results are reported as such. This single-host, single-run study cannot establish cross-model reliability. A human-reader pilot and additional model/repeated runs remain separate follow-up work; no participants are recruited or results fabricated here.

The harness checks corpus structure, exact spans and hashes. It does not grade writing or turn a passed reference check into semantic validation. Report actual counts, snapshots and execution limits in RESULTS.md.
