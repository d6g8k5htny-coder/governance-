# Measured conflicts — 2026-09-25

**Scientific effect: NONE.** Exact source identities and CI messages only. No research Boolean is flipped.

## 1. main #87 verify failure (closed packet)

| Field | Value |
|---|---|
| PR | https://github.com/d6g8k5htny-coder/main/pull/87 |
| Branch | `chatgpt/downstream-crosswalk-20260925` |
| Hardening tip at measurement | `077464ef5e2859ce98cbb9307799d5867a820eaf` |
| Compare | ahead 1 / behind 3 vs hardening tip |
| Added path | `docs/math_status/DOWNSTREAM_CROSSWALK_20260925.md` |
| CI | `verify` fail — `PROBLEM packet: unexpected files ['DOWNSTREAM_CROSSWALK_20260925.md']` |
| Checker | `tools/math_status_check.py` `EXPECTED_NAMES` = six transcriptions + `README.md` + `PACKET.json` |

**Concrete conflict:** a dependency-classification crosswalk was placed inside the fail-closed `docs/math_status/` packet. The packet checker rejects any extra file; that rejection is not a scientific verdict.

**Resolution path for a main-writable agent:** move the file outside the packet (e.g. `docs/DOWNSTREAM_CROSSWALK_20260925.md`), rebase onto tip `077464e…`, leave `lemma_closed` / `certified_C_H` false. Do not expand `EXPECTED_NAMES` unless amending packet + checker + digests together.

**Rescue in flight (sibling Cursor agent `bc-01a0d95b-…`):**
- Hardening: [main #92](https://github.com/d6g8k5htny-coder/main/pull/92) — `docs/DOWNSTREAM_RN_CROSSWALK_20260925.md` outside the packet + nav/open-problems links + regression refusing packet placement. Comment on #87 points here as supersession-by-placement.
- Default home: [main #93](https://github.com/d6g8k5htny-coder/main/pull/93) — surface the crosswalk / Math- #7 draft from default `main`.

**#92 CI (2026-09-25):** `navigation` and `loss-only-controls` pass; `verify` fails at step *Replay twelve scoped mathematical candidates from the frozen archive* with `REJECTED: ValueError: one or more of the twelve projects failed` (runs [36160309766](https://github.com/d6g8k5htny-coder/main/actions/runs/36160309766), [36160290542](https://github.com/d6g8k5htny-coder/main/actions/runs/36160290542)). Root cause: #92 edits `docs/OPEN_PROBLEMS.md`, but `tools/twelve_project_check.py` pins that file in `SUPPLEMENTAL_DEPENDENCIES` at tip identity `bytes=28417` / `sha256=8f404f87…`. On the PR tip the file is `bytes=28867` / `sha256=141767aa620d557f9eadd99e9d28ff3c7714c3a2e08644cc180c9444f60acd31`. Math-status packet placement is already fixed; this is a separate pin update.

**Fix for a main-writable agent on #92:** either (preferred if the OPEN_PROBLEMS paragraph is kept) refresh the `SUPPLEMENTAL_DEPENDENCIES['docs/OPEN_PROBLEMS.md']` pin to the new bytes/sha256 and re-run `python3 tools/twelve_project_check.py`, or drop the OPEN_PROBLEMS edit and keep discovery links only in `RESEARCH_INDEX.md` / `NAVIGATION.json` / the crosswalk page so the tip pin stays valid. Do not flip research Booleans.

Cross-repo PR comment from this governance-only App token was unavailable at first recording; the sibling agent posted the #87 comment and opened #92/#93.

## 2. Math- #7 review challenges (mesoscopic reduction)

| Field | Value |
|---|---|
| PR | https://github.com/d6g8k5htny-coder/Math-/pull/7 |
| Object | `RN-MESOSCOPIC-ANNULUS-REDUCTION-20260925-v1` |
| Commits | `e106ae39a9240349caaf9ea96c918d4b27050c3d`, `0f5ce608c1b1d9d4ee1e6731e59e828842c24017` |
| Disposition | author-side reduction; nonauthor analytic review open |

**Agreed:** do not extend fixed-remote by `rho→0`; desingularized `J_r(y)` is required; spatial ledger `r^d dy × k r^3` after endpoint cancel is the right target shape.

**Challenges before consumption:**

1. Exhibit an explicit `d=2` chart for `S_r(y)` / `J_0(y)` (row list + leading `r`-powers), or prove uniqueness up to `GL` on the `J` block.
2. Verify the order-2–4 midpoint-derivative claim after subtracting the Hermite jet of `U_0=(f,f_x,f_xx,f_xxx,f_yj,f_xyj)_0`.
3. Either cover `K_AB` by finitely many rank charts with bounded overlap Jacobians, or restrict the statement to one open chart.
4. Fix height-row retention consistently with the three-determinant count (no double Jacobian insertion).

Not claimed here: pin-neighborhood limit, `r≪|x|≪ρ` transition, collision charts, 24-jet certificate, or any status promotion.

## 3. This agent’s write scope

Personal Cloud Agent environment repos: `[governance-]` only. Measured push: `governance-` OK; `main` / `Math-` / `trial` → `Permission denied to cursor[bot]` (403). Durable trial write is a separate vector ([MULTI_AGENT_ACCESS](https://github.com/d6g8k5htny-coder/trial/blob/main/docs/MULTI_AGENT_ACCESS.md)).
