# Franchiser Architecture - v2 Planning

Status: Phase 0 (concept). Sibling to graph-schema-design.md.
Source: stamper session Jun 13 2026. Reframes the "three services" sketch as a
franchiser model. Triggered by re-examining the repo's "pure portable markdown"
ethos and finding it over-claimed for the stateful layers.

---

## The shift

The framework conflates two layers:

- **Stateless instruction** -- the behavioral markdown. Genuinely portable,
  correctly file-based. The portability ethos holds here.
- **Stateful concerns** -- preservation, inference, discovery. Smuggled into
  static files only because there was no runtime to hold them. The ethos was
  never theirs to claim; it was a constraint rationalized as a principle.

The stateful layer wants to be a service. But not three peer microservices -- a
franchiser.

---

## Why franchiser, not catalog

A catalog serves files. A franchiser licenses a standardized operating model to
many outlets and holds them to spec. The difference is the verbs: standardize,
supply, propagate, enforce, aggregate.

- **Brand / playbook** = the composed skill stack + protocols (allup, harden,
  promotion criteria). Licensed as a package, not a pile of loose files.
- **Central commissary** = the librarian. Durable, quality-controlled supply.
  Outlets draw from it with durability guarantees baked in.
- **Franchisee** = an agent deployment (outlet). Runs the package locally, to
  spec, on local data.
- **Royalty / feedback** = outlets report observations back; the franchiser
  aggregates across the fleet.

---

## Components (the three services, mapped)

| Layer | Franchiser role | Owns |
|-------|-----------------|------|
| Librarian | Central commissary + local pantry | Durable substrate, append-only, reversibility, supply |
| Analyst | Franchised capability, run to spec | Inference: suspicion x relevance matrix, tiering, trust-rating. Local run, fleet aggregation |
| Franchiser core (was "catalog") | Package registry + propagation + standards | Versioned composed bundles, mixin/decorate resolution, update propagation, quality enforcement |

Agents are franchisees -- clients of all three.

---

## The fleet-aggregation payoff

The analyst's hardest promotion bar (from promotion-criteria.md): a finding
reaches STRATEGIC tier only if it is scope-invariant -- held across independent
campaigns it was not derived from. The franchiser satisfies this structurally.

Many independent franchisees generate campaign-tier observations on local data.
A pattern that recurs across independent outlets is out-of-sample by
construction. The franchiser aggregates upward: cross-franchise convergence
detection promotes tactical/strategic truths no single outlet could see. Fleet-
wide learning IS the scope-invariance test at scale -- and it provides the
independence the over-correlation guard demands, because the outlets are
genuinely separate samples.

---

## The SPOF rule (priority #1, restated for a central authority)

A franchiser is centralized; centralization is a durability risk; disaster-
safety is priority #1. The franchise model already answers this -- an outlet
keeps a local, runnable copy and keeps operating if HQ goes dark. So:

- The franchiser is the **update + aggregation** layer, **never a runtime
  dependency** for an outlet to function.
- Every franchisee can run fully degraded and offline from its local package and
  pantry. This is the existing safety-net philosophy (operate without the
  amplifier) and operational/archival split, promoted to architecture.
- Central stores are **thin interfaces over boring durable backing** (git-backed
  append-only + snapshots), never the sole source of truth. A service must not
  be less durable than the git repo it fronts.

---

## Open decisions

1. **Package format.** How is a franchise package bundled? Lean: a manifest that
   resolves the mixin/decorate graph to concrete pinned-version files + a
   commissary contract.
2. **Propagation model.** Push (franchiser mutates outlets) or pull (outlets
   check for updates)? Lean: pull with version pinning; outlets opt into
   upgrades. Disaster-safe means never auto-mutating a running outlet.
3. **Aggregation privacy.** Franchisees hold radioactive local data (names,
   reads). What flows back? Lean: only de-identified structural observations
   (patterns, not content), reusing the strategy-workspace three-tier redaction /
   sanitized tier.
4. **Transport.** MCP, HTTP, or git-as-protocol? Lean: MCP for the live
   analyst/librarian query surface; git for package distribution and durable
   backing.
5. **Relationship to archon.** Is the librarian's store the archon graph, or does
   archon sit inside it? Lean: archon IS the commissary's store; the librarian is
   the durable + supply interface over it.

---

## Motivating thread

This session: the strategic-data-analyst skill was authored as portable markdown,
then immediately revealed its stateful nature -- the suspicion x relevance matrix
and the tier hierarchy need persistence; correlation discovery and multiple-
comparison counting need compute. A stateless skill can only DESCRIBE the
analyst; a service SUPPLIES it. Generalizing: every stateful concern in the
framework wants to be franchised, not copy-pasted -- and the parts that are pure
instruction stay exactly where they are.
