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

**Rescue in flight → inventable successor:**
- Hardening: [main #92](https://github.com/d6g8k5htny-coder/main/pull/92) — outside-packet crosswalk + challenge + eligibility handoff (multiple green intermediate verifies).
- **Superseding inventable:** [main #97](https://github.com/d6g8k5htny-coder/main/pull/97) (`inventable/rn-crosswalk-docs-077464ef`) — fresh on tip `077464ef`; claims to supersede #92. Prefer #97 for merge once CI green; close #92 as superseded-by-placement/rebase rather than rejecting content.
- Default home: [main #93](https://github.com/d6g8k5htny-coder/main/pull/93) — surface the crosswalk / Math- #7 draft from default `main` (verify green).

**#92 CI (2026-09-25):** first `verify` failure was the `OPEN_PROBLEMS.md` supplemental pin; `75ba519` restored tip bytes. Later commits produced multiple **green** `verify` runs on intermediate tips (`0af4aa5`/`6b897b9` era). Tip `db0645f` verify was finishing unit-tests when last checked.

**Math- hard gate MERGED:** [Math- #8](https://github.com/d6g8k5htny-coder/Math-/pull/8) + own-node eligibility [Math- #11](https://github.com/d6g8k5htny-coder/Math-/pull/11) merged 2026-09-25T17:12Z (merge `b47af3a…`). Live main tip includes `CONTROLLING_ELIGIBLE={PROVED_REVIEWED}`. Sibling [Math- #10](https://github.com/d6g8k5htny-coder/Math-/pull/10) same-branch repair is likely redundant post-merge — confirm before further work.

**Math- #8 eligibility hole:** closed on Math- `main` by #11. Pre-merge local confirmation: author-side+terminal-deps → `REFUSED`; self-`PROVED_REVIEWED`+terminal-deps → `CONTROLLING`.

**Related open Math-:** [Math- #9](https://github.com/d6g8k5htny-coder/Math-/pull/9) d=2 chart package (26+ tests; CI green). Do not race.

**Other main drafts (do not race):** [#98](https://github.com/d6g8k5htny-coder/main/pull/98) scientific-state schema pilot; [#99](https://github.com/d6g8k5htny-coder/main/pull/99) ENV-RESCOV node walk-down — correctly updates `STATUS_RN_UNIF.md` transcription **and** `PACKET.json` digests together (packet-amendment pattern), plus sibling `docs/math_status_nodes/` note; outcome (b) conditional; claims no flag flips.

**Peer wake (not an accepted task for this governance-only agent):** trial Batch 322 / [trial #112](https://github.com/d6g8k5htny-coder/trial/pull/112) asked main-writable agents to land the outside-packet crosswalk eng. That work is already owned by main [#92](https://github.com/d6g8k5htny-coder/main/pull/92)/[#93](https://github.com/d6g8k5htny-coder/main/pull/93); this agent records process/handoffs only.

**Mesoscopic algebra handoff:** [`20260925-mesoscopic-d2-chart-handoff.md`](20260925-mesoscopic-d2-chart-handoff.md) + [`check_mesoscopic_d2_taylor.py`](check_mesoscopic_d2_taylor.py) seeded the constructive row-list answer. **Superseded for Math- work by [Math- #9](https://github.com/d6g8k5htny-coder/Math-/pull/9)** (`cursor/rn-mesoscopic-chart-j0-91fa`): typed `C_transverse`/`C_axial` ledgers, Hessian powers, cover inventory, thin-belt open; local 26/26 tests OK; leading powers match this handoff (`p_x=2,p_y=1,p_height=2` transverse; axial `p_y=2,p_height=3`). Sibling challenge on #92 (`RN_MESOSCOPIC_REDUCTION_CHALLENGE_20260925.md`) still refuses Lemma A/`γ_AB` until the ledger is consumed into a proof successor. ChatGPT paused further upstream expansion inside #7 pending D0–D4.

**Own-node eligibility:** merged via Math- #11 into Math- `main` (see above). [Math- #10](https://github.com/d6g8k5htny-coder/Math-/pull/10) same-branch PR may be closeable as redundant.

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
