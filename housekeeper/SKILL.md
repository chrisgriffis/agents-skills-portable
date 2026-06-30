---
name: housekeeper
description: "State hygiene, global reconciliation, and spring cleaning. Mixin to advisor. Redeployable housekeeping functions for multi-file strategic state systems."
---

# Housekeeper

Mixin skill for the advisor. Provides redeployable housekeeping functions that
maintain the integrity of a multi-file strategic state system across sessions,
compaction events, and human error.

The advisor's allup protocol catches session-level drift. The housekeeper
catches system-level rot: stale documents nobody remembered to update, naming
inconsistencies that accumulated over weeks, arcs that exist in one layer but
never propagated, and structural debt that only surfaces when you read
everything in one pass.

---

## Activation

Invoke when the user says "springclean", "housekeep", or "spring cleaning."
Also invoke proactively when:
- A harden reveals more than 3 cascade fixes needed
- A new session bootstrap from rolling context produces confusion
- The user returns from a multi-day gap (3+ days since last session)
- Explicit structural cleanup is requested

The housekeeper does not override advisor procedures. It adds a function
library. When active, the advisor gains access to the springclean function
and its sub-operations.

---

## Functions

### springclean

Full-system reconciliation. Non-negotiable steps, in order:

**Phase 1: Enumerate**

Discover every non-.git file across all state surfaces:
- Agent state folder (stamper.state/ or equivalent)
- Strategy repo (all of private/, exhibits/, archive/, safety-net/)
- Any referenced external locations

No shortcuts. No sampling. Every file gets registered.

**Phase 2: Ingest**

Read every file completely. As you read, build intermediate working state:
- Actor registry (name, aliases, role, org position, disposition)
- Name index (every human name encountered, source file, line)
- Arc registry (arc name, status, which layers contain it)
- File registry (path, size, staleness estimate, last-referenced-by)
- Consistency ledger (contradictions found, severity)

Use SQL tables, markdown scratch, or whatever substrate fits context. The
point is dense saturation -- you cannot reconcile what you have not loaded.

**Phase 3: Entity Audit (Name Hygiene)**

Cross-reference every name against the canonical actor registry:
- Flag typos (character-distance matching: "jsoh" -> "Josh")
- Flag ghost names (appear once, never defined)
- Flag alias collisions (same person, different names across files)
- Flag stale attributions (role/action assigned to wrong person)

Severity: CRITICAL if a name error could cause a wrong move. HIGH if it
pollutes a document that gets pasted to stakeholders. MEDIUM if internal
only. LOW if cosmetic.

**Phase 4: Cross-File Consistency**

For each file, check:
- Do path references point to files that actually exist?
- Do line-number references match current content?
- Do temporal markers ([TODAY], [CURRENT], dates) reflect reality?
- Do claims in one file contradict claims in another?
- Are file-size/line-count claims in README/index files accurate?

Flag and severity-rank every inconsistency found.

**Phase 5: Arc Coherence**

For each known arc (from trajectory, dossier, campaign files):
- Which layers contain it? (L1 career, L2 operational, L3 tactical)
- Is it current in all layers where it should be?
- Has it been folded up when complete?
- Are there arcs that exist only in one layer (orphaned)?

The merge direction is ALWAYS upward. If L2 has an arc that L1 does not,
that is a fold-up debt, not an error. But it must be flagged.

**Phase 6: Severity Catalog**

Produce a ranked list of all issues found:
- CRITICAL: would cause a wrong move or dangerous bootstrap
- HIGH: would mislead a stakeholder-facing artifact
- MEDIUM: internal inconsistency, no immediate harm
- LOW: cosmetic, informational

**Phase 7: Greene Read (Optional)**

If requested or if the system has not had a power-dynamics assessment in
14+ days, produce a Robert Greene analytical pass across the full state.
Uses the robertgreene skill's framework. Covers:
- Current board position (who holds what)
- Information asymmetries (who knows what others do not)
- Active law violations or masterclasses
- Risk surface (where power could shift against the principal)
- Timing assessment (what clocks are running, whose benefit)

**Phase 8: Produce Report**

Output the Global Reconciliation Report using the template at:
`templates/reconciliation-report-template.md`

The report is the deliverable. It contains findings, not fixes. Fixes are
a separate decision the user makes after reviewing findings.

**Phase 9: Remediate (User-Gated)**

After the user reviews the report and approves, apply fixes:
- Update temporal markers
- Fix path references
- Correct name errors
- Update line counts / file sizes in indexes
- Flag items that require human judgment (do not auto-fix)

---

### quicksweep

Lighter version. Runs Phases 1, 3, 4, and 6 only. Skips full ingestion,
arc coherence, and Greene read. Use for routine maintenance between full
springcleans. Takes ~5 minutes instead of ~30.

---

### staleness-check

Single-file or single-folder check. Answers: "is this document current?"
Reads the file, cross-references claims against known state, reports
staleness estimate with specific stale claims identified. Use before
pasting any document to a stakeholder or using it as a bootstrap.

---

## Report Archival

Every springclean produces a report. Reports are archived as:
- Pretty HTML in `stamper.state/snapshots/` (dated, self-contained)
- Optionally committed to strategy repo `private/housekeeping/`

Reports are reference artifacts. They do not replace live state files.
They document the system's health at a point in time.

---

## Relationship to Allup

Allup is a session-level integrity check. Springclean is a system-level
deep clean. They are complementary:

| Dimension | Allup | Springclean |
|-----------|-------|-------------|
| Scope | State files only | All files, all surfaces |
| Frequency | Every session close | Every 1-2 weeks or on demand |
| Depth | Verify current state | Full historical reconciliation |
| Output | Decay rating | Structured report |
| Fixes | Immediate (cascade) | User-gated after review |
| Greene read | No | Optional |
| Duration | 5-10 min | 20-40 min |

---

## Portability

This skill is domain-agnostic. Any multi-file state system benefits from
periodic springcleaning. The specific file paths, actor registries, and
arc definitions are supplied by the adopting agent/skill -- the housekeeper
provides the PROCESS, not the CONTENT.

Adapt by:
1. Defining your state surfaces (where files live)
2. Defining your actor registry schema
3. Defining your arc/track structure
4. Running springclean

The templates work with any naming convention. The severity framework is
universal.
