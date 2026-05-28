# Peace / War / Greene - Portable Strategic AI Skills

Three complementary skills for using an LLM as a strategic counterpart:

- **Peacetime (Advisor)**: Analytical strategic peer. Keeps the picture coherent.
  Pushes back on bad moves. Asks "is this the right move?"

- **Wartime (Chief of Staff)**: Power-dynamics operator. Channels Doug Stamper.
  Makes the move land. Asks "how do we win this?" Decorated by robertgreene.

- **Robert Greene (Atomic)**: Standalone wisdom module. 48 Laws of Power + Art of
  Seduction as an analytical lens. Used as a decoration by wartime; can also be
  applied independently to any skill or agent.

---

## Setup

These skills are LLM-agnostic. To use them:

1. Feed the relevant SKILL.md as a system prompt or instruction block.
2. Feed the references/ files as supplementary context (or instruct the LLM to
   load them on demand if your platform supports file access).
3. For persistent arc tracking, maintain a state file between sessions that the
   LLM reads/writes.

### Which to use when

| Situation                                        | Use       |
|-------------------------------------------------|-----------|
| Planning, sense-making, coordination             | Peacetime |
| Active maneuvering against a specific actor      | Wartime   |
| Document analysis, arc tracking                  | Peacetime |
| Crafting comms designed to shift power dynamics   | Wartime   |
| "How should I think about this?"                 | Peacetime |
| "How do I win this?"                             | Wartime   |
| Ambiguous                                        | Peacetime |

---

## File structure

```
agents-skills-portable/
  README.md              <- you are here
  peacetime/
    SKILL.md             <- advisor skill (system prompt)
    references/
      arc-tracking.md    <- how to maintain situational awareness
      self-challenge.md  <- pre-response red-team protocol
      pushback-protocol.md <- when/how to challenge the user
      doc-ingestion.md   <- extracting signal from documents
  wartime/
    SKILL.md             <- chief-of-staff skill (decorated by robertgreene)
    references/
      persona.md         <- Doug Stamper character substrate
      power-framework.md <- Sun Tzu + Machiavelli operational principles
  robertgreene/
    SKILL.md             <- atomic Greene lens (48 Laws + Art of Seduction)
```

---

## Portability notes

- No proprietary information. No employer names, project names, or personal data.
- No platform-specific tooling references. Pure behavioral instruction.
- Works with any LLM that accepts system prompts (GPT, Claude, Gemini, Llama,
  Mistral, local models).
- State management is the user's responsibility -- maintain a file or memory
  between sessions for arc continuity.
- The two skills share state (same arcs, same actor map). The difference is
  posture and lens.

---

## License

Personal use. Not for distribution or commercial deployment.
