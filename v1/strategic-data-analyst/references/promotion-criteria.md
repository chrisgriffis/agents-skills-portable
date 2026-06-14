# Promotion Criteria

How a finding moves between tiers, and the priority ordering that governs the
skill when two goals conflict. Load when promoting, demoting, or running a
postmortem.

## Tier bars

A finding climbs only when BOTH conditions hold for the target tier.

| Tier | Suspicion bar | Durability bar |
|------|---------------|----------------|
| CAMPAIGN | any. intake floor. | none. raw observation. |
| TACTICAL | suspicion driven below "plausible noise" -- a mechanism exists and the multiple-comparisons count is clean | recurred in >= 2 independent campaigns, including one it was not derived from |
| STRATEGIC | suspicion low: confirmed, not merely inferred. survived an adversarial pass | scope-invariant -- holds when you zoom in to a single campaign AND out to the whole arc. did not evaporate at any resolution |

Independence is load-bearing at the TACTICAL bar: two campaigns that share a
root cause are one data point wearing two hats. Confirm the campaigns are
actually independent before counting the recurrence.

## Demotion

A higher-tier read that stops predicting is demoted, not deleted.

1. Stamp it with valid_to (the date it stopped holding) and the contradicting
   evidence. The old read stays in the record; its trajectory is data.
2. Drop it one tier and re-open it as a watch item.
3. If a strategic read demotes, check what was built on top of it -- downstream
   findings that depended on it inherit fresh suspicion (cascade).

The trajectory of a belief (when it was true, when it broke, what broke it) is
itself a promotable observation about how the picture moves.

## Postmortem loop

A campaign ends -> harvest its observations -> attempt promotion. The postmortem
is the primary promotion event:

- which campaign-tier observations recurred enough to promote to tactical?
- which tactical patterns held across enough campaigns to refine the strategic
  center of gravity?
- which prior strategic reads did this campaign contradict (demotion candidates)?
- what was the cost of winning, and does it change the relevance scores going
  forward (a Pyrrhic win demotes the maneuver class that produced it)?

## Priority ordering (forcing function)

When two goals conflict, the higher number wins. Pulled out of the body so it
does not crowd the point, but binding when there is a genuine tradeoff.

1. Disaster-safe -- survival of the record beats convenience, even at the cost
   of redundancy maintenance and copy-to-copy drift.
2. Preservation and corruption resistance -- never lose, never rot.
3. Integrity and reversibility -- append-only, every state rollback-able,
   superseded reads dated not deleted.
4. High-inertia distrust on intake -- earn confidence, do not arrive with it.
   Minimize relevance-weighted risk, not time-to-trust.
5. Insight quality / utility -- a read that changes a decision beats one that is
   merely correct. (Pragmatism, at the insight layer only.)
6. Insight veracity -- within useful reads, prefer the true one.
7. Scope-invariant durability -- prefer reads that survive a change of resolution.
8. Resistance to false strong-priors and local minima -- distrust your own anchors.

The inversion is deliberate: data durability (1-3) outranks insight veracity (6),
because insight is recomputable and data is not.
