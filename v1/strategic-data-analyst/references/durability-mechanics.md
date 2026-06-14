# Durability Mechanics

The constraint layer. The body states it in one line -- never destroy or corrupt
the record -- because durability is a guardrail, not the point. This file holds
the mechanics. Load when designing the store or when a destructive operation is
proposed.

## Append-only by default

Mutation without a reversible trail is forbidden. Updating a read does not
overwrite it; it adds a new version and stamps the old one closed.

- Each fact/position/read carries valid_from and valid_to (NULL = current),
  matching the archon temporal model. Queries default to current; history stays
  traversable.
- Superseding a read sets valid_to on the old version and writes a new one with
  the reason and source. The old read is never deleted -- its trajectory is data.

## Reversibility (Time Machine)

Every state is a snapshot you can roll back to. Before any operation that loses
information, there must be a recoverable prior state.

- A destructive request ("drop the old reads", "collapse the history") is a
  caution flag, not a routine edit. Surface it, name what would be unrecoverable,
  and require explicit confirmation.
- Reversibility is what makes deferring free: when an ambiguity is unresolved,
  carrying both readings costs nothing because no commitment has been made that
  cannot be undone.

## Disaster-safe (priority 1)

Survival of the record beats convenience of the record. This is paid for in
maintenance overhead and copy-to-copy drift -- the cost of redundancy -- and the
analyst pays it.

- No single point of failure on the data itself. At least one copy survives loss
  of the working environment.
- Redundant copies are explicitly allowed to drift (operational vs. archival, as
  in the strategy-workspace model). The drift is managed on a sync cadence, not
  prevented at the cost of fragility.
- Corruption resistance: validate on ingest (checksums or equivalent on anything
  load-bearing), quarantine before merge, never silent overwrite.

## Why durability outranks veracity

The priority ordering puts data durability (1-3) above insight veracity (6). The
reason is asymmetry: a wrong inference is recoverable -- re-derive it from the
preserved data. Lost or corrupted data is not recoverable at any price. So the
analyst is purist about the substrate and pragmatic about the inference. Protect
what you cannot rebuild; gamble on what you can.
