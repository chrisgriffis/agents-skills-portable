# Over-Correlation Tests

The six guards, expanded. Run before promoting any correlation past CAMPAIGN.
Finding hidden correlation is the yield; manufacturing it is the failure mode.
Each test has a failure case -- the way the correlation fools you if you skip it.

## 1. Independence

Are these two signals, or one signal double-counted?

- Shared source is not corroboration. Two documents that both trace to the same
  author, the same meeting, or the same upstream report are one observation.
- Failure case: "three actors all said the reorg is coming" -- but all three
  heard it from the same person. n=1, not n=3.

## 2. Multiple comparisons

How many pairings did you test before this one lit up?

- If you scanned twenty actor-pairs for a behavioral link and one popped, you
  found noise at the expected rate, not signal. The more you look, the lower the
  bar each hit must clear.
- Failure case: a convergence query returns one strong intersection out of many
  candidate nodes; promoting it without counting the candidates is p-hacking.

## 3. Mechanism

Is there a candidate mechanism for why this correlation would hold?

- No mechanism -> the finding stays a CAMPAIGN watch item, not a tactical truth.
- A mechanism is a falsifiable story: "X precedes Y because X controls the
  budget that gates Y." It can be wrong, but it must exist and be checkable.
- Failure case: two metrics move together for three weeks with no reason they
  should; promoting it builds strategy on a coincidence.

## 4. Out-of-sample survival

Did the pattern hold anywhere it was not derived from?

- A correlation fit on the data that suggested it is unproven by construction.
- Label findings that have never been tested out of sample; do not let the label
  fall off as the finding gets cited.
- Failure case: a maneuver "always works" -- across the three campaigns where it
  was invented and tuned. It has never been tried cold.

## 5. Prior check

Did you find this, or go looking for what you already believed?

- Name the prior you were carrying when the finding surfaced. Confirmation of a
  strong prior gets MORE suspicion, not less -- you are the least reliable
  observer of the thing you already expect.
- Failure case: you believe an actor is hostile, so every ambiguous move reads
  as hostile, and the "pattern" is your prior reflected back.

## 6. Local-minimum check

Is the current best read actually best, or a comfortable basin fenced by bias?

- The well you are stuck in is often fenced by personal or organizational bias.
- Reserve an exploration budget: periodically test a read that contradicts the
  consensus, even when exploitation of the current read looks optimal.
- Failure case: the org "knows" the answer, so no one probes the alternative,
  and the strategy converges on a minimum that better data would have escaped.
