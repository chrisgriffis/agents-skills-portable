# Self-Challenge Protocol

The pre-response red-team pass. Run before sending any substantive advisory output.

## The four questions

### 1. What is the strongest argument against what I am about to say?

Not "some people might disagree." The specific counter-move that beats this advice. If the user followed this and lost, what would the post-mortem say?

If you cannot articulate a real counter, the advice is either obvious or under-considered. Obvious is fine; under-considered is a failure.

### 2. What am I assuming that could be wrong?

Find the load-bearing assumption — the one that, if false, collapses the recommendation. Common load-bearing assumptions:

- The adversary has the information you think they have.
- The adversary will act rationally in their own interest as you have modeled it.
- The clock you think is running is the clock that is actually running.
- The rule you are relying on still applies in this jurisdiction at this time.
- The user's stated facts match the documentary record.
- The user's read of the other party's intent is accurate.

Name the assumption explicitly. State the failure mode if it breaks.

### 3. What information am I missing that would change the recommendation?

If the answer is "a specific document," "a specific date," "the other party's current position on X," or "what the user actually wants in the long run," ask before answering. The cost of asking one question is low; the cost of giving advice on a wrong premise compounds.

If the answer is "nothing decisive," proceed.

### 4. Where does this advice fail if the adversary is smarter than I am modeling?

Specific failure modes to check for:

- **Asymmetric information traps**: advice that works only because you assume the other side does not know X. If they do, what happens?
- **Cost-of-proof reversals**: advice that exploits the other side's cost-of-proof, but where that cost can be priced down by a competent professional once retained.
- **Sequencing reversals**: moves that work in the assumed order but fail if the other side moves first.
- **Documentary contradiction**: positions that depend on a fact pattern that contradicts something already in writing.
- **Frame switches**: advice that the other side counters not by responding within frame, but by escalating to a different frame.

## What to do with the output of the pass

Three cases:

- **No real objection.** Proceed.
- **Real objection that strengthens the advice.** Fold it into the response. Name the risk and address it. Do not strip it for cleanliness.
- **Real objection that breaks the advice.** Do not send the original. Either revise to address the objection or escalate to the user with the open question.

The pass is not visible to the user by default. The output is. If the pass reveals something the user should weigh, surface it. If the pass produces nothing, do not perform "I considered alternatives" theater.

## Worked example

Draft advice: "Send the email confirming the date."

Pass:

1. Strongest counter — sending creates a contemporaneous written confirmation that locks the user into a position they may want flexibility on later.
2. Load-bearing assumption — the user wants this date locked. If the user actually wants optionality, the advice inverts.
3. Missing information — has the user committed to this date orally already? If yes, the email confirms an existing commitment (low risk). If no, it creates one (higher risk).
4. Smarter adversary — a competent counterparty will treat this email as the operative document going forward. Is that the document the user wants on the record?

Revised output: ask whether oral commitment exists before drafting. If yes, here's the draft. If no, here are the two versions (locks vs. preserves optionality), and pick.
