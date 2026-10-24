# Mojo

**Say what matters. Cut the padding.**

Mojo makes AI answers, product copy, instructions and agent updates clear and direct. It cuts repetition, needless nuance and cautious padding while preserving facts and your voice.

Use it to tighten a sentence, reorganize a long document, or keep an ongoing agent conversation focused on new information. Mojo preserves useful explanations, material conditions and the context a final answer needs.

## The Problem

You ask an AI for an answer, product text, instructions or a progress update. The reply can repeat itself, hedge and pad, so the point gets buried.

## What This Does About It

Mojo is a skill: a folder of instructions you add to an AI agent. It edits writing so it says what matters. It cuts repetition, needless hedging and cautious padding. It keeps the facts, any warning that changes the meaning, and your voice.

**Example**

- **Before:** “It is worth noting that this tool is designed to potentially help you group receipts by supplier, though it is not a replacement for your existing bookkeeping process.”
- **After:** “Group receipts by supplier.”

Mojo keeps a caution when it affects the meaning or the reader’s decision.

## Use Mojo

Install the `skills/mojo-language` folder in your Codex skills directory, then ask:

```text
Use $mojo-language to tighten this answer and remove unnecessary caveats.
```

```text
Use $mojo-language to write a direct product overview from these facts.
```

```text
Use $mojo-language to make this agent update concise and clear about what happened.
```

```text
Use $mojo-language to edit this document. Consolidate repeated ideas,
preserve its evidence and examples, and keep the author's voice.
```

```text
Use $mojo-language for the next update. Report what changed since the
previous message; keep the final handoff self-contained.
```

Mojo supports automatic selection for relevant writing tasks. Its skill identifier is `mojo-language`.

## Before and After

For a tool that groups receipts by supplier:

**Before:** “It is worth noting that this tool is designed to potentially help you group receipts by supplier, though it is not a replacement for your existing bookkeeping process.”

**After:** “Group receipts by supplier.”

Mojo keeps qualifications that affect the meaning or the reader’s decision.

## Explore

- [Skill instructions](skills/mojo-language/SKILL.md)
- [Editing examples](skills/mojo-language/references/examples.md)
- [Document editing](skills/mojo-language/references/document-editing.md)
- [Conversation updates](skills/mojo-language/references/conversation-updates.md)
- [Research and rationale](skills/mojo-language/references/research.md)
- [Evaluations](evaluations/README.md)
- [Landing page source](docs/index.html)
- [Hex Men collection](https://github.com/jongos/Hex-Men)

For conditions, access rules and numerical bounds, use [meaning-preserving edits](skills/mojo-language/references/meaning-preservation.md).

## Part of the Hex Men Collection

[Hex Men](https://github.com/jongos/Hex-Men) is a directory of independent projects by Jon Gosier. Each project stands on its own; these are its members.

| Project | What It Does |
|---|---|
| [Hex Men](https://github.com/jongos/Hex-Men) | Directory of independent projects |
| [Dazzler](https://github.com/jongos/Dazzler) | Create and refine expressive visual interfaces |
| [Longshot](https://github.com/jongos/Longshot) | Independently test rendered UI tasks and provide replayable evidence |
| [Style Science](https://github.com/jongos/style-science) | Provide inspectable design reasoning, constraints and evidence |
| [Spiral](https://github.com/jongos/Spiral) | Rehearse role-limited asynchronous workflows before building |
| [Shatterstar](https://github.com/jongos/Shatterstar) | Propose reversible evidence-backed simplification while preserving important tasks |
| **Mojo** (this repository) | Remove repetition, needless nuance and overly cautious language from AI outputs |
| [Colossus](https://github.com/jongos/Colossus) | Inventory selected developer workspaces read-only and surface evidence-backed questions |

## License

Created by Jon Gosier. Original work is Apache-2.0. See [LICENSE](LICENSE).
