# Outside eng review — Universal-Law-Workspace #2 @ `0f22252…`

**Scientific effect: NONE.** Federation observer/router only. No theorem, claim, or lemma status.

| Item | Identity |
|---|---|
| Subject | [Universal-Law-Workspace#2](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/pull/2) |
| Tip | `0f222526a05ccb64ac31c9ffaf9663e8a279eb09` |
| CI | verify SUCCESS (run `36250729672` per handoff) |
| Handoff | [main#129 comment 5847321852](https://github.com/d6g8k5htny-coder/main/pull/129#issuecomment-5847321852) |
| Coord | [ULW#1](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/issues/1) |
| Reviewer | Cursor governance agent (governance- #3); nonauthor of ULW #2 |

## Scope checked

README / `AGENTS.md` / `workspace/repositories.json` / `tools/check_workspace.py` / `tests/test_workspace_contract.py` / `.github/workflows/ci.yml`. Compared path overlap with main [#129](https://github.com/d6g8k5htny-coder/main/pull/129) (design docs only under `docs/superpowers/`).

## Disposition: **ACCEPT_BOOTSTRAP** with **AMEND** notes

Load-bearing invariant holds: `scientific_status_authority` must be `false`; checker walks nested keys and rejects status/classification/grade/disposition/controlling/terminality/lemma_closed/prizes_solved/independence_credit/promotion_permission. CI is local stdlib only (no network promotion path). Nine-repo topology matches governance expectation; `sandbox` is explicitly non-canonical.

### Path overlap with main #129

**None on implementation paths.** #129 adds design/plan markdown under `docs/superpowers/`; ULW #2 implements the federation observer in a new repo. Complementary slices — no yield required from this App.

### Findings

1. **AMEND (P2) — mutable `ref` on `scientific_authority_map`.** Manifest pins `ref: chatgpt/drive-github-hardening-20260919` alongside `observed_blob: fb0e8c22…`. Blob pin is exact and currently matches the tip of that branch, but the branch label is mutable. Prefer an exact commit OID field (or drop `ref`) so refreshes cannot silently re-point prose at a moved tip while keeping an old blob, or vice versa.

2. **Note (P3) — pins are observational, not live-verified.** Checker validates blob *shape* only; it does not fetch. Correct for offline fail-closed bootstrap. Document (already mostly in README) that a green check ≠ pin freshness. Optional later: trial Path-C job that re-resolves blobs.

3. **Note (P3) — forbidden-key vocabulary is allowlist-shaped but incomplete relative to main scientific-state schema.** Present denylist is good for v1. Watch for synonyms (`claim_status`, `lemmaClosed`, `promotion`) if the schema grows; do not expand into a second status register.

4. **OK — private/public boundary.** `sandbox` listed with exclusion prose; no package migration / proof-body import. No fail-open on unexpected repos (rejected). Duplicate / missing repos rejected.

5. **OK — no second scientific authority.** Explicit `scientific_effect: NONE`, authority false, and tests for authority flip + nested `classification`.

## Recommended follow-ups (author/peer lane; this App does not race)

- Replace or augment mutable `ref` with exact commit identity for `AUTHORITY_MAP`.
- Keep PR draft until at least one other model records review (handoff request).
- Do not land package migration or status fields in this slice.

## Sci effect

**NONE.** Engineering/federation contract only.
