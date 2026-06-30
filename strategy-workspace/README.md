# Strategy Workspace Framework

A reusable architecture for maintaining organizational strategy as a living
document system, paired with AI agent infrastructure for persistent situational
awareness across sessions.

This is the methodology, not the content. Adapt the structure to any
multi-actor situation where you need to track positions, maneuvers, and
evolving reads over months or years.

---

## Core Concept

A strategy workspace is not a single document. It is a **layered system** where
different time horizons, update frequencies, and audiences get different
containers -- connected by cross-references and a merge-direction discipline.

The layers solve a fundamental problem: no single document can simultaneously
serve as "what is my 3-5 year strategic position" AND "what did Actor X say on
Tuesday and what do I owe them by Thursday." Different questions demand different
containers.

---

## The Three-Layer Architecture

```
CAREER ARC INTEGRATOR (Layer 1)
    Structured sections. Kind/unkind reads. Evolution tracking.
    Time horizon: 3-5 years. Update: after strategic shifts.
        |
        |--- integrates from --->  LIFETIME DOSSIER (Layer 2)
        |                              Running actor register. Current reads.
        |                              Relationship dynamics, operating patterns.
        |                              Updated every working session.
        |                              Time horizon: role tenure.
        |
        |--- integrates from --->  PUSH-SPECIFIC DOSSIER (Layer 3)
                                       Tactical: deliverable states, logistics.
                                       References Layer 2 entries by person-ID.
                                       Active for campaign duration. Frozen after.
                                       Postmortem folds into Layer 1.
```

### Layer 1: Career Arc Integrator

The strategic backbone. Structured sections that answer "what is my position,
who are the actors, what's the terrain, where am I going." Updated infrequently
but with full editorial weight. Contains:

- Objective (sanitized + real versions)
- Self-assessment (leverage, constraints, perception map)
- Cast (structured per-actor entries with named fields)
- Terrain (org chart vs. real power graph, fault lines, oxygen-consuming crises)
- Prior Art (precedents, scar tissue, radioactive phrases)
- Technical Substance (what's actually being built, where critics have points)
- Current State (in motion, signals being interpreted)
- Active Arcs (case studies of live strategic situations)

The **unkind read** principle: write the unflattering version. Charitable framing
in writing is how the dossier stops predicting things. If you can't write the
unkind read of yourself and your actors, the document is decorative.

### Layer 2: Lifetime Dossier (Agent State)

The running operational memory. Updated every working session by the AI agent.
Contains current reads on people, relationship dynamics, recent signals, and
operating patterns. This is where freshness lives -- it's the working surface
the agent reads/writes on every interaction.

Persists across all campaigns/pushes. Accumulates over role tenure.

### Layer 3: Push-Specific Working Dossier

Tactical state for a time-bounded campaign. What you owe, to whom, by when.
References Layer 2 entries rather than duplicating them. Created fresh for each
push/campaign. Frozen after the event. Postmortem distills upward into Layer 1.

### Merge Direction: Always Upward

Push detail summarizes into lifetime. Lifetime distills into career arc. Never
duplicate downward. Lower layers reference upper layers; they don't copy content
from them.

### Evolution Tracking

Layer 1 preserves dated reads so strategy can be informed by trajectory, not
just current state. Example: "Actor X went from 'allied via Y, needs
independent development' (Apr) to 'tired ally with high standards, personally
existential stakes' (May)." The evolution IS the insight.

---

## Companion Documents

### Rolling Context (Paste-In)

A compressed ASCII-only shorthand mirror of Layer 1. Used as paste-in context
for fresh AI sessions. Top-level keys followed by terse bullets. Exists because
not every AI session can read the full dossier -- the rolling context bootstraps
enough picture to be useful in a cold start.

Rules:
- ASCII only (no em-dashes, curly quotes, unicode). Gets copy-pasted into tools
  that mangle extended characters.
- ~1/3 the length of the full dossier
- Must stay in sync at the strategic-claim level

### Safety Net / Emergency Cards

Human-readable continuity cards for operating without AI. The "if access dies"
scenario. Contains:
- Immediate action items (what's on the clock right now)
- Boundary rules (what never goes into non-secure tools)
- Key people cards (one-line operational summaries)
- Active arcs compressed
- What you already shipped (don't re-do list)
- What NOT to do

---

## The Visual Layer

Each document gets a "visual HTML" companion -- a rendered, styled version
designed for a different cognitive mode than reading raw markdown. The visual
is not a dashboard; it's an editorial presentation that makes the strategic
picture legible at a glance while preserving the weight and gravity of the
content.

Design principles for strategy visuals:
- **Prestige register.** This is a coffee-table book, not a Jira board. Serif
  typography, generous whitespace, considered layout. The binding should crackle.
- **Appropriate gravitas.** Gold accents, chapter-style sections, pull quotes
  for key insights. The content deserves a presentation that signals "this
  matters."
- **Dramatis personae.** Cast entries styled as character cards with colored
  edge-coding (ally/adversary/asset/unknown). Named fields visible at a glance.
- **Terrain as geography.** Power graphs rendered as spatial diagrams, not
  tables. Fault lines with severity markers.
- **Timeline as chronicle.** Events on a vertical timeline with the current
  moment marked. Creates narrative momentum.
- **Self-contained.** Single HTML file, inline styles only, no external
  dependencies. Opens in any browser on any machine.

See `templates/visual-dossier.html` for a starter template.

See `templates/weapon-rack.md` for the verbal combat preparation template (multi-shelf
ammunition structure with kill phrases, designed for principals deploying arguments
orally in meetings rather than in writing).

---

## Operational Conventions

### Two Registers (Do Not Cross)

| | Full prose docs | Paste-in / copy-paste contexts |
|---|---|---|
| Format | Markdown, full editorial | Plain text, key: + bullets |
| Punctuation | Whatever it needs | ASCII only |
| Length | Whatever it needs | ~1/3 natural length |
| Voice | Considered, written | Telegraphic, scannable |

### The Cast Entry Schema

Each actor in the dossier gets structured fields. This is not optional -- the
structure forces rigorous thinking and makes updates surgical.

```
### [Name] ([Role])

- Role / actual power:
- How they got here / what they're protecting:
- Failure mode(s):
- Current relationship to you:
- What they want that you could plausibly give them:
- What they fear your initiative might trigger:
- Who they actually listen to:
- Last meaningful interaction / signal:
- Notes:
```

The field "What they fear your initiative might trigger" is the most important.
It forces you to model the world from their position, not yours.

### Fold-In Workflow

When new material arrives:
1. Read the material
2. Classify: Layer 2 update (person/relationship) vs. Layer 3 (tactical state)
   vs. Layer 1 (strategic shift)
3. Update the appropriate layer(s). They must stay consistent.
4. Add dated changelog entry to Layer 1
5. Commit on feature branch, merge to main

### Hard Rules (Adapt to Your Context)

- Write the unkind read. Always.
- Capture priors BEFORE new data arrives (lets you see what changed vs.
  confirmed)
- Radioactive language stays in the dossier. Never leaks into org-facing comms.
- The dossier predicts; it does not prescribe. When it stops predicting
  correctly, update the model, don't force reality to conform.
- Evolution tracking: don't overwrite old reads. Date them and add new ones
  alongside. The trajectory is data.

---

## Agent Integration

The strategy workspace is designed to be maintained by an AI agent across
sessions. The agent:

1. Reads state on session start (Layer 2 + handoff notes)
2. Updates Layer 2 based on new information surfaced during the session
3. Produces a handoff artifact at session end (what happened, what changed,
   what's next)
4. Periodically runs consistency checks across all layers

The agent's persistent state includes:
- Lifetime dossier (Layer 2)
- Trajectory tracking (master arc + sub-tracks + watch items)
- Operating notes (craft-level learnings about advising this user)
- Latest handoff (rolling bootstrap for new sessions)
- PERT chart (day-by-day execution plan for current push)

### The Allup Protocol

Periodic integrity verification. Non-optional. The protocol exists because
corner-cutting CREATES MORE WORK in subsequent sessions. Prevents drift,
hallucination, and cascading stale-reference failures.

Seven steps (expanded from original five to close gaming loopholes):

0. Ground rules preamble (read before proceeding -- psychologically primes the
   executor not to cut corners by foreshadowing that step 5 will catch skipped work)
1. Full self-consistency pass (read all state files, reconcile contradictions)
2. File reference cross-check (confirm all pointers are valid)
3. Cascade check and FIX (not just detect -- remediate, then cascade the fix to
   all downstream representations: readme -> visual -> handoff -> resume template)
4. Self-flag debrief (what was caught, what was missed, what was changed)
5. Hallucination challenge (did I actually do the work or am I reporting
   assumed state? If skipped, rating capped at 3/5)
6. Context decay rating (1-5, capped at 3 if any files unverified)

The cascade requirement (step 3) is the critical addition. Previous versions
detected inconsistencies but left them for "later." This compounds into
multi-session debt spirals. The protocol now requires: find it, fix it, cascade
it, all in one pass.

### The Harden/Hardenout Protocol

Terminal actions of a working session. Each is defined by reference to avoid
duplication drift:

- **Thread-transfer block:** a paste-ready message for bootstrapping the next
  session. Contains: agent activation line, temporal anchor, state file pointers
  with read-order, exhibits location, cloud doc links, and a "context from killed
  session" section for anything not yet persisted.
- **Harden:** allup (by reference) + sync operational state to archival + write
  handoff + commit + produce thread-transfer block. Every session close gets one.
- **Hardenout:** harden (by reference) + export to portable repo (sync meta,
  templates, agent/skill defs with structural relationships intact, push to
  remote). That's it -- one additional step on top of harden.

---

## Directory Structure (Template)

```
strategy/
  README.md                    <- distributable overview (no names)
  readme-visual.html           <- pretty HTML of public readme
  .gitattributes               <- LF normalization
  private/                     <- radioactive content
    org-strategy-dossier.md    <- Layer 1 (career arc)
    org-strategy-visual.html   <- prestige HTML of Layer 1 (full)
    org-strategy-visual-sanitized.html  <- sanitized tier (shareable)
    org-strategy-visual-redacted.html   <- deep-redacted (showpiece)
    org-strategy-visual.pdf    <- print companion (generated, not maintained)
    rolling-context.txt        <- compressed paste-in
    README-private.md          <- full strategic detail
    agent-states/stamper/             <- Layer 2 archival copy (synced on harden)
      dossier.md               <- lifetime actor register
      trajectory.md            <- arc tracking
      dossier-visual.html      <- actor visualization
    safety-net/                <- emergency continuity cards
    archive/           <- recovered session history
    exhibits/                  <- source material + active pushes
      [push-name]/
        backlog.md             <- master work tracking
        prep/                  <- active working docs
          working-dossier.md   <- Layer 3 (push-specific)
        prep/sent/             <- shipped artifacts
        prep/data/             <- reference material
        prep/data/verbatim/    <- immutable source (never edit)
        inbound/               <- received docs (read-only)

[agent-state]/                 <- separate from strategy repo (operational/hot)
  dossier.md                   <- Layer 2 (lifetime) -- SOURCE OF TRUTH
  trajectory.md                <- arc tracking
  operating-notes.md           <- craft learnings
  latest-handoff.md            <- session bootstrap
  pert-chart.md                <- execution plan
```

---

## Public/Private Split Rationale

The workspace separates into screen-shareable (architecture, methodology,
conventions) and radioactive (names, political reads, unkind assessments).
Motivation: "someone glances at my screen" or "I want to show someone how this
system works" without exposing the content that would end relationships.

The public layer explains the WHAT and HOW.
The private layer contains the WHO and WHY.

---

## Three-Tier Redaction Model

A single visual artifact can exist at three information densities for different
audiences:

1. **Full** -- everything visible. Internal use only. The actual weapon.
2. **Sanitized** -- framework sophistication visible, behavioral reads stripped.
   Names replaced with role labels (e.g. "The Director" instead of an actual
   name). Structural analysis, fault lines, terrain maps preserved. Shows the
   quality of thinking without revealing what you know about specific people.
   Suitable for: trusted peers who'd benefit from the framework, peer review
   of analytical rigor.
3. **Deep-redacted** -- structure-only skeleton. All content replaced with
   opaque blocks (Unicode U+2588 full blocks, NOT CSS tricks that can be
   defeated by select-all or style inspection). Zero information recoverable.
   Suitable for: showing someone "I have this" without showing them what "this"
   contains. Amusement value. Flexing the architecture itself.

The sanitization principle: keep structural/analytical value, strip behavioral
reads, motive attributions, unkind assessments, and your own positioning/plays.
The viewer should think "this person thinks rigorously about org dynamics" not
"this person is tracking my weaknesses."

---

## Print-Ready Visual Pattern

Each HTML visual embeds its own @media print CSS block. The PDF is a GENERATED
ARTIFACT from the HTML, not a separate maintained document. Regenerate anytime
with a headless browser:

```
edge --headless --print-to-pdf="output.pdf" --no-pdf-header-footer "file:///path/to/visual.html"
```

Print CSS design principles:
- Extra left gutter margin for physical binding (1.25in left vs 0.75in right)
- page-break-before: always on chapter-level sections
- break-inside: avoid on atomic elements (cards, timeline entries, blockquotes)
- page-break-after: avoid on headings (keeps them with their content)
- Strip decorative binding frame (box-shadow, border-image) for print
- Force background colors to print (print-color-adjust: exact on cards/terrain)
- Frontispiece becomes a full title page (padding: 3in top)

The maintained artifact is the HTML. The PDF is disposable and regenerable.

---

## Operational / Archival State Split

Agent state exists in two copies:

- **Operational** (hot copy): read/written by the agent during sessions. Lives
  wherever the AI tooling expects it. May be dirty, may have uncommitted edits,
  may be ahead of the archival copy. This is always current truth.
- **Archival** (cold copy): committed to the durable strategy repo. Synced from
  operational during harden operations. Insurance against tool access loss,
  session corruption, or needing to reconstruct from zero.

They are EXPLICITLY allowed to drift. The operational copy wins on conflicts.
The archival copy is a checkpoint, not a constraint. This matters because the
agent writes state mid-session before commits; forcing commit-on-every-write
would create noise in git history.

---

## When to Use This

This framework is appropriate when:
- Multiple actors with non-aligned interests
- Stakes are career-level or higher
- Time horizon is months to years
- You need persistent situational awareness across many conversations
- The strategic picture is too complex for a single document
- You operate through an AI counterpart that needs to maintain state

It is overkill for:
- Simple project management
- Technical work with no political dimension
- Short-term tactical problems
- Situations with fewer than 3 relevant actors

---

## License

Personal use. Adapt freely for your own strategic work.
