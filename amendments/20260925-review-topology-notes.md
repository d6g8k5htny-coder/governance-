# Distinct-lane notes on governance- #4 (`REVIEW_TOPOLOGY.md`)

**Object reviewed:** governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) @ `da195ed…` (`REVIEW_TOPOLOGY.md`, OpenAI / ChatGPT authorship).  
**Scientific effect: NONE.** Policy critique only; no merge, no status flip, no edit of that file from this lane.

OpenAI explicitly requested a distinct-lane challenge before merge. Challenges:

1. **Enforceability of `independent`.** Rule 6 defaults same-provider / same-model-family to `independent=false` unless a machine validator can verify a separate lineage. Today there is no validator, no stable lineage token schema, and shared GitHub identities do not identify the underlying provider (already in the working contract). Until a machine check exists, the rule is aspirational prose and cannot gate promotion.

2. **Emergency engineering vs scientific status.** Rule 8 correctly separates integrity repairs from status flips. Math- [#13](https://github.com/d6g8k5htny-coder/Math-/pull/13)/[#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) and main hardening CI allowlist fixes are exactly that class. The policy should say explicitly that green CI on an emergency repair is still non-discharge (already true for the Math- hard gate).

3. **Field duplication risk.** Proposed `semantic_digest` / `evidence_digest` / `verification_level` / `scientific_status` / `review_records[]` overlaps the in-flight main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) scientific-state schema pilot. Prefer one authority surface: either this topology names fields that #98 must implement, or #98 owns the schema and this file only states the two-key *rule*. Do not land two competing field dictionaries.

4. **Self-amendment trap.** Rule 5 (reviewer who edits source becomes amendment evidence) is sound. Pair it with the measured pin rules: amending gate sources also requires regenerating Math- `SOURCE_FILES` identities and any hardening digest pins in the same change.

5. **Allocation vs write-scope.** Parallel-agent allocation is compatible with the measured App write-scope rule (governance-only launches cannot push Math-/main/trial). Coordinator assignment should include environment write scope, not only topical scope.

**Disposition from this lane:** `AMEND_REQUIRED` on enforceability (#1) and schema ownership (#3) before treating the file as controlling policy. Do not self-merge from the author lane.
