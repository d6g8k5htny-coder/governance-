# Review topology v1 — two-key mathematical promotion

**Object:** REVIEW-TOPOLOGY-20260925-v1  
**Author lane:** OpenAI / ChatGPT  
**Scientific effect:** NONE. This is a working governance contract, not theorem acceptance.

## Purpose

Prevent a model from authoring a mathematical object, reviewing its own amended object, and then converting same-lineage agreement into scientific acceptance. The research architecture already separates source identity, verification evidence and scientific status. This policy adds a fourth boundary: **authorship and qualifying review are separate keys**.

## Two-key rule

A mathematical node that requires independent review may enter a positive reviewed/controlling state only when both keys exist for the exact same semantic object:

1. **Author key** — immutable source identity / semantic digest for the statement, scope, domain and dependency set.
2. **Reviewer key** — at least one qualifying independent review whose reviewed semantic digest equals the current author key and whose review scope covers the promoted scope.

CI, hashes, mutation tests, CAS/SMT/proof-assistant checks, same-lineage critique and repeated execution are evidence but are not the reviewer key by themselves.

## Review record

A qualifying review record carries:

- `review_id`
- `claim_id`
- exact `semantic_digest`
- `author_lineage`
- `reviewer_lineage`
- `review_scope`
- `disposition`: `ACCEPTED | AMEND_REQUIRED | BLOCKED | REFUTED`
- `independent` (validator-derived where possible)
- exact review evidence identities
- timestamp
- optional `supersedes_review_id`

Lineage should identify provider/model/agent/session or another stable token sufficient to detect self-review and known shared lineage.

## Fail-closed rules

1. `author_lineage == reviewer_lineage` cannot satisfy independent review.
2. A semantic-digest change stales all reviews of the previous digest.
3. `AMEND_REQUIRED`, `BLOCKED` and `REFUTED` never count as acceptance.
4. Partial review cannot promote a broader statement/domain/scope.
5. If a reviewer edits the mathematical source it is reviewing, that review becomes amendment evidence; the amended digest requires a fresh qualifying review by a distinct lineage.
6. Same-provider or same-model-family reviews default to `independent=false` unless an explicit project policy establishes a genuinely separate lineage and the machine validator can verify it.
7. An unavailable independent reviewer leaves the node author-side/HOLD; it does not justify self-acceptance.
8. Engineering emergency repairs may be merged to preserve integrity, but cannot change scientific status until separately reviewed.

## Author/reviewer handoff

- Author posts exact source identity, declared scope, imported dependencies, known limitations and requested review interfaces.
- Reviewer works from that immutable identity and returns interface-level findings.
- `AMEND_REQUIRED` returns to the author lane. The author fixes it and emits a new digest.
- A distinct reviewer then reviews the new digest.
- The status/promotion engine consumes only qualifying review records; it never infers acceptance from conversation prose.

## Parallel-agent allocation

To maximize throughput without sacrificing independence:

- one lane authors/repairs;
- one distinct lane reviews/falsifies;
- numerical/formal lanes independently reproduce narrow calculations;
- integration agents maintain graphs, CI and provenance but do not award mathematical acceptance;
- a coordinator assigns collision-free scopes and closes stale surfaces.

If only one agent is available, it may author and adversarially self-audit, but the result remains author-side until another qualifying reviewer appears.

## Architecture integration

The scientific-state schema should keep these orthogonal:

- `semantic_digest` — identity of scientific content;
- `evidence_digest` — identity of evidence carriers;
- `verification_level` — L0–L5 mechanical evidence;
- `scientific_status` — authoritative disposition;
- `review_records[]` — lineage/scope-specific review evidence.

No one field is a proxy for another.

## Current application

- Cursor-authored PR98 and PR9/PR14: OpenAI is reviewer; Cursor repairs review findings.
- OpenAI-authored gate hotfixes: Cursor or another distinct lane should review before any scientific status use.
- D1/D2/D3/D4/D6 require independent review; OpenAI same-lineage inspection may find blockers but cannot self-award `PROVED_REVIEWED`.
- Formal-verification work under main #95 requires a separate review of the exact certified statement before it can contribute a reviewer key.

This policy does not alter any current theorem status.
