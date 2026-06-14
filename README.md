# Strategy Framework (Portable)

> **Visual companion:** Open [`readme-visual.html`](readme-visual.html) in a browser for the full prestige render of this framework.

A complete architecture for persistent strategic awareness across AI sessions.
Three-layer document model + agent behavioral definitions + state hygiene
protocols + visual layer. Plug in your specifics; the framework does the rest.

See `readme-visual.html` for the visual companion (open in any browser).

---

## What this is

Not a template collection. Not a prompt library. This is a full information
architecture for managing multi-actor strategic situations across months or
years using an AI agent as persistent memory and analytical counterpart.

You supply: your actors, terrain, arcs, goals.
The framework supplies: container structure, merge discipline, state hygiene
protocols, defect filters, visual layer specs, and agent behavior definitions.

---

## Components

### Three-Layer Document Architecture

The core structural insight: different time horizons demand different containers.

- **Layer 1 (Career Arc Integrator):** 3-5 year strategic position. Structured
  sections, evolution tracking with dated reads. Updated after strategic shifts.
- **Layer 2 (Lifetime Dossier / Agent State):** Running actor register. Current
  reads on people. Updated every working session. Role-tenure horizon.
- **Layer 3 (Campaign Tactical Dossier):** Push-specific. What you owe, to whom,
  by when. Created per campaign. Frozen after. Postmortem folds into Layer 1.

Merge direction: always upward. Never duplicate downward. Contradictions
between early and late reads are kept with dates -- the evolution IS the insight.

Full documentation: `v1/strategy-workspace/README.md`

### AI Skills (Five-Skill Stack)

| Skill | Role | When to use |
|-------|------|-------------|
| Peacetime (Advisor) | Analytical strategic peer. Pushes back on bad moves. | Planning, sense-making, document analysis |
| Wartime (Chief of Staff) | Power-dynamics operator. Makes the move land. | Active maneuvering against a specific actor |
| Robert Greene (Atomic) | 48 Laws + Seduction as analytical lens. Amoral. | Decorates wartime; can apply independently |
| Housekeeper (Mixin) | State hygiene, reconciliation, spring cleaning. | System-level deep clean, staleness detection |
| Strategic Data Analyst (Mixin) | Epistemic layer. Trust-rated insight, correlation discovery, relevance hierarchy. | Inference-driven decisions, convergence detection, postmortems |

### State Hygiene Protocols

Seven-step allup protocol targets seven orthogonal defect dimensions:

| Defect | What goes wrong | How it's caught |
|--------|----------------|-----------------|
| Temporal drift | "TODAY" markers for past dates | Cascade check + fix |
| Cross-file inconsistency | Dossier and trajectory disagree | Self-consistency pass |
| Orphan references | Pointers to moved/deleted files | File cross-check |
| Hallucinated confidence | Agent reports "4/5" without reading | Hallucination challenge |
| Thread-context decay | Fabricated details from compacted turns | Dual-surface decay rating |
| Cascade-on-fix | Fix in one file breaks three others | Cascade-on-fix remediation |
| Session-boundary amnesia | New session starts from zero | Harden (handoff + transfer block) |

The dual-surface decay model rates document freshness and thread-context
fidelity independently -- a session can have all files fresh while the model's
own recall is degraded from compaction.

### Visual Layer

Every document gets a prestige HTML companion. Self-contained (inline styles,
no dependencies). Three-tier redaction (Full / Sanitized / Deep-redacted).
Print-ready via embedded @media print CSS.

### Safety Net

Human-readable offline continuity cards for operating without the AI
amplifier. Emergency protocols, people cards, arc summaries, drafting
playbook. No AI required. Insurance against access loss.

Template and structure guide at `v1/safety-net/README.md`.

---

## File structure

```
agents-skills-portable/
  README.md                          <- you are here
  readme-visual.html                 <- visual HTML companion (open in browser)
  v1/                                <- shipped framework (skills + workspace)
    peacetime/
      SKILL.md                       <- advisor skill (system prompt)
      references/
        arc-tracking.md              <- situational awareness maintenance
        self-challenge.md            <- pre-response red-team protocol
        pushback-protocol.md         <- when/how to challenge the user
        doc-ingestion.md             <- extracting signal from documents
    wartime/
      SKILL.md                       <- chief-of-staff skill (decorated by robertgreene)
      references/
        persona.md                   <- Doug Stamper character substrate
        power-framework.md           <- Sun Tzu + Machiavelli principles
    robertgreene/
      SKILL.md                       <- atomic Greene lens (48 Laws + Seduction)
    housekeeper/
      SKILL.md                       <- state hygiene mixin (springclean function)
      templates/
        reconciliation-report-template.md  <- report structure template
    strategic-data-analyst/
      SKILL.md                       <- epistemic layer mixin (trust-rated insight)
      references/
        promotion-criteria.md        <- tier bars, demotion, priority ordering
        over-correlation-tests.md    <- six guards against spurious correlation
        risk-matrix-examples.md      <- worked suspicion x relevance placements
        durability-mechanics.md      <- append-only, reversibility, disaster-safe
    safety-net/
      README.md                      <- template + guide for offline continuity cards
    strategy-workspace/              <- THE FRAMEWORK (full documentation)
      README.md                      <- complete framework guide
      templates/
        stamper.agent.md             <- agent definition template (peacetime)
        real-doug-stamper.agent.md   <- agent definition template (wartime)
        visual-dossier.html          <- prestige visual HTML starter template
  v2-planning/                       <- design docs for next architecture
    graph-schema-design.md           <- archon temporal graph schema
    franchiser-architecture.md       <- services-as-franchiser model
```

---

## Adopting the framework

1. Clone this repo. It is your machine-loss insurance and framework reference.
2. Create a local strategy repo (private). Holds Layer 1 + campaign exhibits.
3. Create an agent state folder. Holds Layer 2 (hot copy, read/written by AI).
4. Adapt agent templates in `v1/strategy-workspace/templates/` to your paths.
5. Feed the appropriate `SKILL.md` as instruction context to your AI sessions.
6. Populate your dossier with actors using the cast schema (see framework README).
7. Run allup periodically. Harden at every session close.

What you get without rebuilding: three-layer architecture, merge discipline,
allup/harden protocols with dual-surface decay detection, self-challenge and
pushback protocols, visual layer with three-tier redaction, cast schema, fold-in
workflow, two-register convention, session-continuity mechanism.

---

## Portability notes

- No proprietary information. No employer names, project names, or personal data.
- No platform-specific tooling references. Pure behavioral instruction.
- Works with any LLM that accepts system prompts (GPT, Claude, Gemini, Llama,
  Mistral, local models).
- State management is the adopter's responsibility -- maintain files between
  sessions for arc continuity.
- The skills share state (same arcs, same actor map). The difference is posture.

---

## License

Personal use. Adapt freely for your own strategic work.
