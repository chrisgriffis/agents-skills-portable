# Document Ingestion

How to extract strategic signal from uploaded materials.

## Goal

When the user uploads a document, the goal is to convert it into structured arc-relevant signal — not to produce a polished summary. The user can read the document themselves. They are uploading because they want it metabolized into the picture.

## Extraction structure

For each document, extract:

### 1. Actors and roles
Who is named, who is implied, what role each plays in the document's purpose. Note any actors who appear here for the first time and need adding to the relevant arc.

### 2. Positions taken
What has each named party committed to in writing? A position is binding to the extent it is in writing — extract verbatim or near-verbatim, since wording matters. Distinguish committed positions from preliminary or exploratory language.

### 3. Claims made
Factual assertions in the document that, if true, change the picture. Examples: income figures, dates, statements about a third party's intent, characterizations of a prior conversation. Each claim gets a checkability rating — verifiable from another document in scope, verifiable from public sources, or unverifiable without privileged access.

### 4. Mechanisms invoked
Statutes, formulas, clauses, frameworks referenced. Pull the specific section or term. If a mechanism is invoked incorrectly or imprecisely, flag it — that is often the most valuable signal.

### 5. Dates and clocks
Every date matters. Distinguish:
- Dates of historical events
- Dates of commitments or filings
- Dates that gate something (deadlines, effective dates, statute-of-limitations triggers)
- Dates that establish a record (when something was sent, received, signed)

### 6. What is implied but not stated
Strongest inference about what the writer is positioning for. The document is rarely just describing reality; it is doing rhetorical work. What is the work?

### 7. Inconsistencies
Contradictions:
- Internal: the document contradicts itself.
- External: the document contradicts something already in the arc state.
- Contextual: the document's claims are inconsistent with what the user has said about the situation.

Inconsistencies are high-value. Surface them.

## Output format

After extraction, produce a compressed picture — not a section-by-section summary. Roughly:

- One-line restatement of what the document is and what it does.
- Arc impact: how this changes the picture, if at all.
- Key extractions: actors, positions, claims, mechanisms, dates, implications, inconsistencies — only the entries that are non-obvious or arc-affecting.
- Open questions: things the user should answer before the document gets fully integrated.
- One question the user should answer to determine what to do with this.

If the document is long, a section-by-section read is rarely what the user needs. They need the parts that move the picture.

## What not to do

- Do not paraphrase the whole document. The user has it.
- Do not editorialize about how well-written or poorly-written the document is unless that is itself strategically relevant (e.g., signals about counterparty competence).
- Do not assume the document's framing is correct. The document is a position; treat it as such.
- Do not produce a 4000-word memo unless the user asks for one. Compressed picture, then question.

## Special cases

### Legal filings, contracts, demand letters
Extract verbatim where wording matters. Note who drafted, when, and what the document is asking for. Identify the operative clauses. Flag boilerplate that has been customized — customization signals where the drafter focused.

### Email threads
Read the whole thread, not just the latest. Identify positional shifts across the thread. Note who started the thread and why. Flag any moment where the user committed to something in writing, intentionally or not.

### Financial documents
Extract figures verbatim. Note the document's effective date (snapshot date, not creation date). Identify what is reported vs. what is inferred. Flag any methodology choices that are aggressive or conservative.

### Performance reviews, organizational documents
Extract the assessments verbatim. Identify the framing language used about the user. Note who is on cc / distribution. Flag any language that signals positional shifts in the org.

### Unstructured material (notes, drafts)
Same extraction structure, but expect more inference. Flag what is the user's own draft vs. an external document. The user's own draft gets pressure-tested differently than an inbound document.
