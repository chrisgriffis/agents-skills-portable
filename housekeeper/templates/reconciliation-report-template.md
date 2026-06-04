# Global Reconciliation Report Template

> Replace bracketed content with actuals. Delete this instruction block.

---

# GLOBAL RECONCILIATION REPORT - [Day] [Date] [Year]

System: [system name / agent identity]
Surfaces scanned: [count] files across [count] locations
Duration: [time]
Decay rating at start: [N]/5

---

## 1. ENTITY AUDIT (Name Hygiene)

### Canonical Actor Count: [N]

### Issues Found: [N]

| Severity | Name Found | File | Line | Should Be | Status |
|----------|-----------|------|------|-----------|--------|
| CRITICAL | [typo] | [file] | [N] | [correct] | OPEN |
| HIGH | [typo] | [file] | [N] | [correct] | OPEN |
| MEDIUM | [typo] | [file] | [N] | [correct] | OPEN |
| LOW | [typo] | [file] | [N] | [correct] | OPEN |

### Ghost Names (appear once, never defined):
- [name] in [file]:[line] -- likely meant [X] or needs registration

### Alias Collisions:
- [Person] appears as: [alias1], [alias2] -- canonical is [X]

---

## 2. CROSS-FILE CONSISTENCY

### Path References: [N] checked, [N] broken

| File | Line | Points To | Status | Fix |
|------|------|-----------|--------|-----|
| [file] | [N] | [path] | BROKEN | [what to do] |

### Temporal Markers: [N] checked, [N] stale

| File | Marker | Claims | Reality | Fix |
|------|--------|--------|---------|-----|
| [file] | [TODAY] | [date] | [actual] | Update to [X] |

### Cross-File Contradictions:

| Claim | File A says | File B says | Resolution |
|-------|------------|------------|------------|
| [topic] | [X] | [Y] | [which is correct] |

### Stale Documents (>7 days without update, actively referenced):

| File | Last meaningful update | Staleness | Risk |
|------|----------------------|-----------|------|
| [file] | [date] | [N] days | [what breaks] |

---

## 3. ARC COHERENCE

### Active Arcs: [N]

| Arc | L1 (Career) | L2 (Operational) | L3 (Tactical) | Status | Fold-up Debt |
|-----|:-----------:|:----------------:|:--------------:|--------|:------------:|
| [arc] | Y/N | Y/N | Y/N | [status] | [yes/no] |

### Orphaned Arcs (exist in one layer only):
- [arc] -- exists only in [layer]. Needs: [propagation/archival/deletion]

### Completed but Unfrozen:
- [arc] -- completed [date], still live in [layer]. Needs postmortem fold.

---

## 4. SEVERITY CATALOG

### Summary: [N] CRITICAL, [N] HIGH, [N] MEDIUM, [N] LOW

### CRITICAL (would cause wrong move or dangerous bootstrap):
1. [description] -- [file]:[line] -- Fix: [action]

### HIGH (would mislead stakeholder-facing artifact):
1. [description] -- [file]:[line] -- Fix: [action]

### MEDIUM (internal inconsistency, no immediate harm):
1. [description] -- [file]:[line] -- Fix: [action]

### LOW (cosmetic, informational):
1. [description] -- [file]:[line] -- Fix: [action]

---

## 5. GREENE READ (if performed)

### Board Position
[Current power map. Who holds what. Where the principal sits.]

### Information Asymmetries
[Who knows what others do not. Where this creates advantage or risk.]

### Active Laws
| Law | Application | Assessment |
|-----|------------|------------|
| [N]: [name] | [how it applies] | Masterclass / Violation / Neutral |

### Risk Surface
[Where power could shift against the principal. What would trigger it.]

### Timing Assessment
[What clocks are running. Whose benefit. What expires.]

### Synthesis
[One-paragraph overall read. Position strength. Primary vulnerability.
Recommended posture.]

---

## 6. RECONCILIATION ACTIONS (User-Gated)

### Approved for immediate fix (no judgment required):
- [ ] [action] in [file]
- [ ] [action] in [file]

### Requires human judgment:
- [ ] [decision needed] -- options: [A] or [B]
- [ ] [decision needed] -- options: [A] or [B]

### Deferred to next session:
- [ ] [what] -- reason: [why defer]

---

## 7. POST-RECONCILIATION STATE

Decay rating after fixes: [N]/5
Files modified: [count]
Next recommended springclean: [date or trigger condition]
