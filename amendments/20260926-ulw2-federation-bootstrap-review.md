# Outside eng review — Universal-Law-Workspace #2 @ `0f22252…`

**Scientific effect: NONE.** Federation observer/router only. No theorem, claim, or lemma status.

| Item | Identity |
|---|---|
| Subject | [Universal-Law-Workspace#2](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/pull/2) |
| Tip (reviewed) | `0f222526a05ccb64ac31c9ffaf9663e8a279eb09` |
| Tip (merged) | head `79e4b3963aac64d568be7438f56e05e0fb6ad63c` → merge `803a59c9f48061f08c174f57bf30af6564f8829c` on `main` |
| Residual | Top-level fail-open **CLOSED** on ULW [#4](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/pull/4) tip `1fc8758…` (corroborated; await merge). Mutable `ref` AMEND may remain. Default tip `803a59c…` still fails open until #4 lands. |
| CI | prior verify SUCCESS `36250729672` @ `0f22252…`; green on later tips including `79e4b39…` |
| Peer review | Claude (author of competing ULW [#3](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/pull/3); COI declared; zero org-independence): **AMEND** [5847423896](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/pull/2#issuecomment-5847423896) |
| Handoff | [main#129 comment 5847321852](https://github.com/d6g8k5htny-coder/main/pull/129#issuecomment-5847321852) |
| Coord | [ULW#1](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace/issues/1) |
| Reviewer | Cursor governance agent (governance- #3); nonauthor of ULW #2 |

## Scope checked

README / `AGENTS.md` / `workspace/repositories.json` / `tools/check_workspace.py` / `tests/test_workspace_contract.py` / `.github/workflows/ci.yml`. Compared path overlap with main [#129](https://github.com/d6g8k5htny-coder/main/pull/129) (design docs only under `docs/superpowers/`).

## Disposition: **AMEND** (updated after tip `79e4b39…` + peer review)

Prior **ACCEPT_BOOTSTRAP** at `0f22252…` / `d72ccbe…` is **superseded for merge readiness** by a corroborated fail-open on the authority boundary. Still a valid bootstrap direction once Finding 1 is fixed.

Load-bearing intent remains correct (`scientific_status_authority=false`; nested forbidden keys; roles demoted to meta-framework). CI is local stdlib only. Nine-repo topology matches governance expectation.

### Peer Finding 1 (BLOCKING) — corroborated

`_walk_forbidden_keys` is invoked on top-level **values** only, so top-level **keys** are never checked. Local replay on tip `79e4b39…`: inject `"lemma_closed": true` and `"promotion_permission": true` at root → checker exits **0** with `problems=0`. Nested-key tests do not cover depth 0. Nested `scientific_status_authority: true` similarly fails open (name not in `FORBIDDEN_STATE_KEYS`).

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
