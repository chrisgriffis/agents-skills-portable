# v2 Planning

Design area for the next architecture. Phase 0 (concept). Nothing here is
implemented; `v1/` remains the shipped framework. This README is the origin
story and the honest state of the idea -- including where the idea fights itself.

---

## Origin: the analyst as catalyst

v2 did not start as an architecture. It started as one more skill.

The `strategic-data-analyst` was written as a portable `SKILL.md`, same as the
other five -- behavioral markdown, fed as context, no runtime. It did not fit the
mold. The skill's two load-bearing mechanisms strained the format immediately:

- The **suspicion x relevance matrix** and the **campaign/tactical/strategic
  hierarchy** are *state*. They have to persist and accrue across sessions to
  mean anything. A prompt cannot hold them; it can only re-describe them cold
  each time.
- **Correlation discovery, multiple-comparison counting, out-of-sample tests**
  are *compute*. They are operations run over a body of data, not instructions
  recited to a model.

A stateless skill can DESCRIBE the analyst. It cannot BE it. That mismatch was
the catalyst: the analyst is the first thing in this repo whose value is not
instruction but a running process with memory.

---

## The epiphany: instruction is not state

The analyst's strain exposed a conflation baked into v1. Two different things
were living in the same `SKILL.md` files:

- **Stateless instruction** -- how to think, what posture to take, what to check.
  Genuinely portable. Correctly a file.
- **Stateful concerns** -- preservation, inference, discovery. Smuggled into
  static files only because there was no runtime to hold them.

The "pure portable markdown" ethos in the root README was load-bearing for the
first and over-claimed for the second. It was, in part, a limitation rationalized
as a principle. The stateful concerns do not want to be files. They want to be
services.

---

## The decomposition: three services

Pulling the stateful concerns out gives three layers, cut by what each owns:

| Service | Owns | v1 ancestor |
|---------|------|-------------|
| **Librarian** | Durable substrate: append-only record, reversibility, corruption resistance, supply | the archon graph + harden/archival split |
| **Analyst** | Inference: the matrix, tiering, trust-rating, correlation discovery | `strategic-data-analyst` skill |
| **Catalog** | Composition + distribution: serves skills/agents, resolves the mixin/decorate graph | the `SKILL.md` collection itself |

Agents are clients of all three.

---

## The reframe: franchiser, not catalog

The third service is more than a file-server. A catalog *serves*; a franchiser
*licenses a standardized operating model to many outlets and keeps them to spec*
-- standardize, supply, propagate, aggregate. Agents become franchisees: each
runs the package locally, on local data, to spec, and reports observations back.

The payoff: the analyst's hardest promotion bar (a finding reaches STRATEGIC tier
only if it held across independent campaigns it was not derived from) is
satisfied structurally. Many independent franchisees are independent samples by
construction. Fleet-wide aggregation IS the out-of-sample test at scale.

Detail in `franchiser-architecture.md`.

---

## Tensions (the part the origin story wants to skip)

The franchiser frame fights itself, and the decomposition has holes. Recorded
here so the idea carries its own counter-argument instead of being sold.

**Standardization vs. bespoke value.** A franchise's whole value is uniformity --
every outlet identical. The analyst's whole value is the *local, bespoke read*.
The frame imports homogenization into the one place that should stay
heterogeneous.

**The franchiser is a bias amplifier.** It propagates the central model to every
outlet, which makes it the most efficient possible mechanism for pushing HQ's
priors fleet-wide. That contradicts the analyst's own priority #8: resistance to
local minima fenced by *organizational* bias. And it undercuts the aggregation
payoff -- independent samples stop being independent the moment the franchiser
succeeds at standardizing how they think. Salvage requires an explicit heresy
mechanism: outlets rewarded for contradicting the center. Not yet designed.

**Missing layers the three services do not cover:**

- **Actuation.** The stack has no hands. Librarian stores, analyst rates, catalog
  distributes -- nothing touches the world. All sensor, no actuator. Whether the
  human stays the sole trigger ("the principal decides") is a deliberate fork or
  a blind spot, and it has not been decided.
- **Calibration.** The analyst rates everyone's trust; nothing rates the
  analyst's. No layer checks, in hindsight, whether promoted "truths" actually
  predicted, or walks back the priors when they did not. It can be confidently
  miscalibrated forever -- the exact failure it claims to resist, with no
  instrument pointed at itself. Allup measures session integrity, not hit-rate.
- **Identity / boundary.** A multi-tenant franchiser with no security model. The
  v1 radioactive-content / redaction-tier / boundary-rules concern is authz, and
  it is homeless in this decomposition.
- **Control plane.** Everything is reactive (the user says "allup"). Fleet scale
  needs triggers and cadence -- the thing that wakes the analyst on schedule or
  event.

Of these, **actuation** and **calibration** are conceptual gaps; the other two
are infrastructure.

---

## Documents

- `graph-schema-design.md` -- archon temporal graph schema. The librarian's store.
- `franchiser-architecture.md` -- the services-as-franchiser decomposition.

---

## Status

Phase 0, concept only. The honest next step is not more architecture -- it is
resolving the two conceptual gaps (does the stack act, and who grades the
analyst) and the franchiser's internal contradiction, before any of it is built.
