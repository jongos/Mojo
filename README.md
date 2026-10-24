# Mojo

**Say what matters. Cut the padding.**

Mojo removes repetition, needless nuance, and overly cautious language from AI outputs. Use it to make answers, product copy, instructions, and agent updates clear and direct.

It cuts the disclaimers that say nothing, the distinctions that change nothing, and the extra paragraphs that repeat the point. Useful facts, meaningful uncertainty, and your voice stay intact.

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

Mojo supports automatic selection for relevant writing tasks. Its skill identifier is `mojo-language`.

## Before and After

**Before:** “It is worth noting that this tool is designed to potentially help you group receipts by supplier, though it is not a replacement for your existing bookkeeping process.”

**After:** “Group receipts by supplier.”

This example assumes supplier grouping is a confirmed feature. Mojo makes supported claims direct and keeps conditions that affect use.

## Explore

- [Skill instructions](skills/mojo-language/SKILL.md)
- [Editing examples](skills/mojo-language/references/examples.md)
- [Research and rationale](skills/mojo-language/references/research.md)
- [Evaluations](evaluations/README.md)
- [Hex Men collection](https://github.com/jongos/Hex-Men)
