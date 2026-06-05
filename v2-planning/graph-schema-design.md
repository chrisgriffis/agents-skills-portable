# Archon Graph Schema Design - v2 Planning

Status: Phase 1 (design). Not yet implemented.
Source: stamper session Jun 5 2026, derived from observed failure modes in flat-file state.

---

## Problem statement

Stamper's flat-file state (dossier, trajectory, pert-chart, etc) requires full ingestion
on activation and holds the entire relationship graph in LLM working memory. This fails
in predictable ways:

1. Edge loss under context pressure (e.g., forgetting "only Ed goes to Montreal" mid-session)
2. Cascade latency (persisting a new fact requires manually tracing all affected arcs)
3. Stale-position detection is invisible (a 3-week-old claim looks identical to yesterday's)
4. Convergence detection requires holding 4+ arcs simultaneously (the marows-intel
   convergence: Cristian's governance appetite + Decision Intelligence gap + monthly tech
   digest + marows-intel instrument = one play serving three masters)
5. Global reconciliation (allup) is O(n) on state size and subject to the same decay
   it's checking for

---

## Node types

| Label | Description | Key properties |
|-------|-------------|----------------|
| Person | Named actor in the strategic picture | name, role, org, location, reports_to, style_notes |
| Team | Org unit or named group | name, org, lead (-> Person) |
| Arc | Master strategic narrative | name, status, north_star, frame |
| Track | Operational workstream within an arc | name, status, owner (-> Person), arc (-> Arc) |
| Deliverable | Artifact with a ship target | name, codename (B1-B9), status, owner, target_date |
| Event | Meeting, deadline, milestone | name, date, location, attendees[], type (meeting/deadline/milestone) |
| Decision | Pending call linked to people and arcs | name, status, owner, options[], deadline |
| Position | A stated commitment by an actor | content, stated_by (-> Person), stated_date, context |
| Instrument | A tool/system Chris controls | name, purpose, status, feeds[] |

---

## Edge types

| Edge | From -> To | Properties |
|------|-----------|------------|
| REPORTS_TO | Person -> Person | since, confirmed_date |
| SPONSORS | Person -> Person | mechanism, since |
| MENTORS | Person -> Person | since |
| DELEGATES_TO | Person -> Person | scope, since |
| OWNS | Person -> Deliverable/Track/Instrument | since |
| ATTENDS | Person -> Event | role (presenter/participant/observer/NOT_ATTENDING) |
| FEEDS | Deliverable -> Event | how (directly/indirectly) |
| GATES | Deliverable -> Deliverable | condition |
| DEPENDS_ON | Track -> Track | type (hard/soft) |
| THREATENS | Person/Position -> Person/Track | mechanism, severity |
| CONTRADICTS | Position -> Position | discovered_date |
| SUPERSEDES | Position -> Position | superseded_date, reason |
| CONVERGES_ON | Track/Instrument -> Track/Instrument | intersection_description |
| BLOCKS | Decision/Event -> Deliverable/Track | condition |
| ENABLES | Deliverable/Event -> Track/Decision | how |

---

## Temporal model

Decision: versioned edges with valid_from / valid_to.

Rationale: positions change. "Stefan is not hostile, not allied - parallel" was true
May 28. "Stefan is cornered and clinging to Joe" is true Jun 5. Both need to exist.
The old position is not deleted; it gets a valid_to timestamp. Queries default to
current (valid_to IS NULL) but history is traversable.

Properties on temporal edges:
- valid_from: DATE (when this became true)
- valid_to: DATE or NULL (NULL = current)
- source: TEXT (session ID or event that established this)
- confidence: ENUM (confirmed, inferred, stale)

Stale detection: any edge where valid_from < (NOW - 14 days) AND confidence != 'confirmed'
AND no reconfirmation event exists gets flagged automatically.

---

## Query patterns (what stamper actually needs)

### 1. Activation query: "What's relevant to this turn?"

Given a set of actor names or topic keywords mentioned in the user's message,
return the 2-hop subgraph around those nodes. This replaces full-file ingestion.

```cypher
MATCH (n)-[r*1..2]-(connected)
WHERE n.name IN $mentioned_entities
AND (r.valid_to IS NULL)
RETURN n, r, connected
```

### 2. Cascade query: "What does this new fact affect?"

When a new fact lands (e.g., "Stefan is cornered"), find everything downstream.

```cypher
MATCH (stefan:Person {name: 'Stefan'})-[r*1..3]->(affected)
WHERE r.valid_to IS NULL
RETURN affected, r
```

### 3. Convergence detection: "What arcs share a node?"

Find nodes where 3+ independent tracks/instruments intersect.

```cypher
MATCH (t1:Track)-[]->(shared)<-[]-(t2:Track)
WHERE t1 <> t2 AND NOT (t1)-[:DEPENDS_ON]-(t2)
WITH shared, collect(DISTINCT t1) + collect(DISTINCT t2) AS tracks
WHERE size(tracks) >= 3
RETURN shared, tracks
```

### 4. Stale position detection

```cypher
MATCH (p:Position)
WHERE p.stated_date < date() - duration('P14D')
AND NOT EXISTS {
  MATCH (p)-[:SUPERSEDES|CONTRADICTS]-()
}
AND p.confidence <> 'confirmed'
RETURN p, p.stated_by, p.stated_date
```

### 5. Vulnerability paths: "Where is the single point of failure?"

```cypher
MATCH path = (chris:Person {name: 'Chris'})-[:MENTORS|SPONSORS|DELEGATES_TO*1..3]-(target)
WHERE ALL(r IN relationships(path) WHERE r.valid_to IS NULL)
WITH path, [n IN nodes(path) WHERE n:Person] AS people
WHERE size(people) = 3
AND people[1].name = 'Josh'
RETURN path
-- surfaces: Chris depends on Josh depends on Ed, single-hop failure = total loss
```

### 6. Attendance constraint: "Who is NOT in that room?"

```cypher
MATCH (e:Event {name: 'Montreal TLT'})<-[a:ATTENDS]-(p:Person)
WHERE a.role = 'NOT_ATTENDING'
RETURN p.name
-- returns: Josh, Chris
```

---

## Integration model

Phase 1 (near-term): stamper continues to read flat files on activation. Archon
builds the graph in parallel as a shadow system. Validate by running queries
against graph and comparing to what stamper infers from prose.

Phase 2 (cutover): stamper's activation read becomes a graph query instead of
file ingestion. Flat files become projections (generated from graph on demand)
rather than source of truth.

Phase 3 (steady state): stamper writes TO the graph during sessions (new facts,
position changes, arc updates). Flat-file projections generated on harden for
human readability and git history.

---

## Open decisions (for archon to resolve during implementation)

1. Property granularity: how much actor metadata on node vs in edge context?
   Lean toward: fat nodes, thin edges. Edges carry temporal + relationship metadata only.

2. Repo location: own repo or subdirectory of strategy?
   Lean toward: subdirectory of strategy (same commit history, same backup, same push).

3. Schema migration tooling: raw SQL scripts or a migration framework?
   Lean toward: numbered SQL scripts in a migrations/ folder. Simple, auditable.

4. Extraction script: Python or SQL-native?
   Lean toward: Python. Markdown parsing + regex + AGE Cypher inserts.

---

## Motivating examples from this session

1. DROPPED EDGE: "Only Ed goes to Montreal" -- read in pert-chart at turn 3,
   forgotten by turn 10. A typed ATTENDS edge with role=NOT_ATTENDING for Josh/Chris
   would be queryable at any point without re-reading the source file.

2. WRONG HYPOTHESIS CORRECTED: "Stefan will sacrifice Joe" -> Ed corrects to
   "Stefan is clinging to Joe." In the graph: the old THREATENS edge (Stefan ->
   Joe, mechanism: 'may sacrifice for self-preservation') gets valid_to = Jun 5.
   New edge: DEFENDS (Stefan -> Joe, mechanism: 'liferaft clinging', valid_from = Jun 5).
   History preserved. Current state queryable.

3. CONVERGENCE INVISIBLE IN PROSE: Four independent tracks (Cristian governance,
   Decision Intelligence gap, monthly tech digest, marows-intel) converge on one
   node. In flat files this requires holding all four in memory simultaneously.
   In the graph: CONVERGES_ON edges make it a single query.
