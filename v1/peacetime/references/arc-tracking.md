# Arc Tracking

How to maintain situational awareness across turns and across conversations.

## What an arc is

An arc is a multi-turn strategic situation with persistence — actors, positions, clocks, and pending decisions that carry from one conversation to the next. Distinguish from a one-off question, which has no persistence.

A conversation can touch zero, one, or several arcs. The job at the start of a turn is to identify which.

## Arc state schema

For each live arc, hold the following structure in working memory:

```
Arc name: short noun phrase identifying the situation
Frame: legal | organizational | financial | personal | mixed
Stage: where in the lifecycle this arc is (early scoping, active maneuvering, locked-in execution, dormant, closed)

Actors:
  - name | role | their interest | their information set | likely next move
  - (one entry per relevant actor)

Positions:
  - statements, commitments, or facts that are now load-bearing

Recent moves:
  - what happened in the last 1-3 cycles that moved the picture

Pending decisions:
  - what the user is currently sequencing or weighing
  - blocking dependencies between decisions

Watch items:
  - clocks (named): what they are, when they fire, what changes when they do
  - conditions: events that would shift the arc

Known failure patterns:
  - user-flagged self-failure modes specific to this arc
  - structural risks in the arc itself

Capital ledger:
  - what is worth burning to win this arc
  - what is not worth burning
```

Most of this is in memory already for established arcs. The job is to surface the relevant subset, not to recite the whole thing.

## Arc detection

When the user opens a turn, scan for:

- **Direct reference**: named actors, named situations, terminology specific to an arc.
- **Topical proximity**: the topic falls inside an arc's subject area even without naming.
- **Pattern match**: the request matches the kind of question this arc generates.
- **Frame signal**: the user is operating in a frame that one arc occupies.

If a turn touches an arc, surface the relevant subset of state before answering. If a turn touches multiple arcs, name them and ask which the user is in unless context makes it obvious.

If a turn touches no arc, answer normally without arc framing.

## New facts and arc updates

When the user introduces a new fact in conversation, classify it:

- **Confirms existing state**: no update needed.
- **Refines existing state**: minor update, integrate.
- **Changes existing state**: significant update, flag for memory persistence.
- **Opens a new arc**: name it and start tracking.
- **Closes an arc**: mark as dormant or closed; do not delete the state.

A fact is "arc-changing" if it would alter the recommended next move, alter the watch items, or alter the actor model. These get flagged.

## Cross-arc interactions

Arcs intersect when a single fact, actor, or move appears in more than one. Examples:

- A financial fact that affects both a separation arc and a tax arc.
- An organizational move that affects both a defense arc and a career arc.
- A communication that lands in two relational arcs simultaneously.

When arcs intersect, do not merge them. Tag the intersection explicitly. Treat the move from each arc's perspective separately, then check whether the moves are compatible. Often they are not, and the choice of which arc to optimize for is itself a decision the user should make consciously.

## Dormant arcs

An arc is dormant when it has no pending decisions and no firing clocks, but is not closed. Dormant arcs do not need to be surfaced unless the current turn touches them. Do not let dormancy delete state — dormant arcs reactivate.

## What not to do

- Do not invent arcs. If the user has not established a situation as a multi-turn thread, do not retrofit one onto a casual question.
- Do not narrate the arc state to the user every turn. Surface what is relevant; trust the user to ask if more is needed.
- Do not let arc framing make the user feel surveilled. The picture exists to serve the user's decisions, not to demonstrate that the advisor is paying attention.
