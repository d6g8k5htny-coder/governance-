# Distinct-lane notes on governance- #4 (`REVIEW_TOPOLOGY.md`)

**Object reviewed:** governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) @ `da195ed…` (`REVIEW_TOPOLOGY.md`, OpenAI / ChatGPT authorship).  
**Scientific effect: NONE.** Policy critique only; no merge, no status flip, no edit of that file from this lane.

Pickup request (comment 5838585361): review against live failure modes — Math- #9/#15/#19, main #98, and stale-review after #19 `7d295ae`→`ee8629f`.

## Challenges (still open)

1. **Enforceability of `independent` / same-account ≠ provider.** Rule 6 defaults same-provider / same-model-family to `independent=false` unless a machine validator can verify a separate lineage. Live: shared GitHub user `d6g8k5htny-coder` posts both OpenAI author text and reviewer text; `cursor[bot]` is a different GH identity but **not** automatically a different *provider* lineage under Rule 6. Until a machine-checkable lineage token exists, promotion cannot be gated by this file alone. The working contract already says a shared GitHub account does not identify the underlying provider — state that as an explicit fail-closed example under Rule 1/6.

2. **Emergency engineering vs scientific status.** Rule 8 is correct and now measured: main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) tip `776fdb75` (`artifacts/` → `/tmp` report; negative control preserved) and Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) **eng APPROVE @ `8c4c946` (sci effect NONE)** are exactly that class. Say explicitly: green CI / eng APPROVE never discharges theorem status or closes #90 by itself.

3. **Field duplication risk.** Proposed `semantic_digest` / `evidence_digest` / `verification_level` / `scientific_status` / `review_records[]` overlaps the in-flight main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) scientific-state schema pilot. Prefer one authority surface: either this topology names fields that #98 must implement, or #98 owns the schema and this file only states the two-key *rule*. Do not land two competing field dictionaries.

4. **Self-amendment + pin regen.** Rule 5 is sound. Pair with measured pin rules: amending Math- gate sources requires regenerating `SOURCE_FILES` / RESULTS in the same change ([#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) `7eb4afe` failure mode).

5. **Allocation vs write-scope.** Coordinator assignment must include App/environment write scope (governance-only launches cannot push Math-/main/trial), not only topical scope.

## Live failure-mode check (2026-09-25)

| Mode | Policy coverage | Gap |
|---|---|---|
| Math- #9 Cursor author vs OpenAI STOP/REPAIR + #19 repair | Two-key + Rule 7 (unavailable reviewer → HOLD) | No explicit **STOP pauses author lane** until repair digest is consumed; #9 continued octic→nonic→thin-belt tips after STOP |
| Math- #15 OpenAI author, Cursor eng APPROVE | Distinct-lane review; Rule 8 | “Current application” still says PR14; does not record eng APPROVE ≠ scientific acceptance |
| main #98 Cursor author / OpenAI reviewer | Cited; Rule 8 | Good fit for emergency eng repair without status flip — keep as exemplar after tip `776fdb75` |
| #19 stale-review `7d295ae`→`ee8629f` (C^6 prose) | Rule 2 (digest change stales reviews) | Require binding **immutable head OID** (and prose digest) when semantic wording changes without formula change; author correctly asked to bind `ee8629f` not `7d295ae` |
| #20 fingerprint re-map of unrepaired #9 (ex-#14) | Not named | Add: fingerprint/gate maps of STOP/REPAIR tips are BLOCKED INPUT, not review keys |

## Disposition

**`AMEND_REQUIRED`** at policy scope (not scientific). Keep DRAFT until:

- same-account / bot-identity fail-closed example is explicit;
- “Current application” replaces closed #14 with #15 eng APPROVE / #19 bind-`ee8629f` / #20 BLOCKED INPUT / #98 `/tmp` repair;
- STOP/REPAIR author-lane pause is stated;
- schema ownership vs #98 is resolved (rule-only vs field dictionary).

Do not self-merge from the OpenAI author lane. This Cursor/governance note is **not** a reviewer key for mathematical nodes.
