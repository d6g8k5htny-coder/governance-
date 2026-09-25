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

**#92 CI (2026-09-25):** first `verify` failure was the `OPEN_PROBLEMS.md` supplemental pin (`28417`/`8f404f87…` → edited `28867`/`141767aa…`; runs [36160309766](https://github.com/d6g8k5htny-coder/main/actions/runs/36160309766), [36160290542](https://github.com/d6g8k5htny-coder/main/actions/runs/36160290542)). Sibling follow-up `75ba519` restored tip `OPEN_PROBLEMS.md` and kept crosswalk pointers on unpinned pages; `verify` re-queued. Packet placement remains correct (`docs/DOWNSTREAM_RN_CROSSWALK_20260925.md`).

**Related Math- work (do not race):** [Math- #8](https://github.com/d6g8k5htny-coder/Math-/pull/8) (`cursor/downstream-hard-gate-91fa`) adds an executable fail-closed D0–D7 promotion gate complementary to the human crosswalk; scientific effect claimed NONE; maps PR7 as open/paused. Local replay here: 24/24 `test_hard_gate` OK; `hard_gate.py` reports `lemma_closed=false`, `illegal_promotion_refused=true`.

**Math- #8 review note:** GRAPH edges `math.rn-mesoscopic-reduction → hist.CH-LIFT` and `→ hist.Piece-2-annulus` are present with `required: false` (related-region pointers, not CONTROLLING blockers). Required dep for mesoscopic is `math.rn-fixed-remote-window` only. That matches the crosswalk’s “live gap / not historical carrier” split; no change requested unless a later edit flips those edges to `required: true` without an importing proof step.

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
