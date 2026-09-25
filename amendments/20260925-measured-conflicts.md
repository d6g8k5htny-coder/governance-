# Measured conflicts — 2026-09-25

**Scientific effect: NONE.** Exact source identities only. No research Boolean flipped.

## Landed

| Item | Identity |
|---|---|
| RN crosswalk + mesoscopic challenge | main [#97](https://github.com/d6g8k5htny-coder/main/pull/97) @ `388a22c…` |
| ENV-RESCOV node walk-down | main [#99](https://github.com/d6g8k5htny-coder/main/pull/99) |
| Conditional-importers sidecar | main [#100](https://github.com/d6g8k5htny-coder/main/pull/100) |
| CERTIFIED q=2 carrier-absent note | main [#101](https://github.com/d6g8k5htny-coder/main/pull/101) @ `9979c7f…` |
| OPEN_PROBLEMS frozen errata (file untouched) | main [#107](https://github.com/d6g8k5htny-coder/main/pull/107) @ `a1c42bf…` |
| SIDE24_CELL square importers | main [#102](https://github.com/d6g8k5htny-coder/main/pull/102) @ `848aea2…` |
| tip-observe `848aea2…` (observe fields only) | main [#108](https://github.com/d6g8k5htny-coder/main/pull/108) → hardening tip `f244312…` |
| RN_SIDE24_CELL errata E1 pointer (nav only) | main [#109](https://github.com/d6g8k5htny-coder/main/pull/109) → hardening tip `fcad723…` |
| CONTRIBUTION_PLAN stale next-items retired (LPW REFUTED via lpw README) | main [#105](https://github.com/d6g8k5htny-coder/main/pull/105) → hardening tip `e3cd7d4…` |
| Hard gate + own-node + REFUTED HOLD | Math- [#8](https://github.com/d6g8k5htny-coder/Math-/pull/8)+[#11](https://github.com/d6g8k5htny-coder/Math-/pull/11)+[#13](https://github.com/d6g8k5htny-coder/Math-/pull/13) @ `baca69c…` |
| Transition-integrity eng package (sci effect NONE; not theorem acceptance) | Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `8c4c946…` merged |

## Process rules proven

1. Closed `math_status` packet; transcription edits co-update `PACKET.json` digests.
2. Do not casually edit twelve-project-pinned `OPEN_PROBLEMS.md` (#107 used archive-pinned errata instead).
3. Gate: own-node `PROVED_REVIEWED` + required deps in `REQUIRED_SATISFIED`; required `REFUTED`/`BLOCKED_ABSENT` HOLD.
4. New hardening `verify` commands need `closure_pipeline` allowlisting (#98 hit this).
5. Math- exact-replay pins (`SOURCE_FILES` / workflow hashes): editing `hard_gate.py` / `test_hard_gate.py` without regenerating identities fails with `ValueError: source identity mismatches: hard_gate.py,test_hard_gate.py` (Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `7eb4afe…`, run `36171889414`).
6. Citing a register tab from new prose requires updating `registers/CONSUMERS.json` in the **same** change: `consumers_check` compares recorded vs scanned prose consumers (main [#105](https://github.com/d6g8k5htny-coder/main/pull/105) @ `36fe375…` body claimed the map update; tip file list is only `docs/CONTRIBUTION_PLAN.md` → `NEW lpw_fold_dispositions: prose consumers differ`).
7. Do not refresh D5 hard-gate fingerprints from a STOP/REPAIR chart tip (Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) closed SUPERSEDED; [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) is the same blocked-input pattern while [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) leading pins remain unshifted).
8. CI that writes a new top-level directory (e.g. `artifacts/` via `--write-report`) must keep `REPOSITORY_TOP_LEVEL` / ignore lists in sync, or verify fails even when the feature under test is green (main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) run `36179103673`).

## Still open (do not race)

| PR | Tip / note |
|---|---|
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | `3ef41e9…` (conditioned Hessian residual); **STOP/REPAIR**; jets ≠ repair; **pause high-jet churn**; consume [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) (**Cursor R1–R6 ACCEPT**) |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | `6cd15f6…`; remaps #9 `3ef41e9…`; **SOURCE REVALIDATION BLOCK**; pause fingerprint churn |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | DRAFT; no J0/Hessian until #9 pins repaired; D5 external-recon leads only (comment 5838994872) — subordinate to pin repair; no theorem credit |
| Math- [#18](https://github.com/d6g8k5htny-coder/Math-/pull/18)+trial [#121](https://github.com/d6g8k5htny-coder/trial/pull/121) | Cursor reciprocal translation **MATCH×7** (`amendments/20260925-math18-translation-review.md`); F10_CLOSED additive; eng≠theorem; keep DRAFT |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | `776fdb75…`; OpenAI **AMEND_REQUIRED** + **CLAIM OA-PR98-F1-REPAIR** (F1 only, NEW branch; Cursor tip frozen); do not duplicate F1; F2–F5 open; #90 OPEN |
| main [#112](https://github.com/d6g8k5htny-coder/main/pull/112) | `d5b75f9…`; tip-observe `e3cd7d4…` after #105; **verify green**; serialize `PACKET.json` with #111 |
| main [#111](https://github.com/d6g8k5htny-coder/main/pull/111) | `7b874c0…`; RN-UNIF walk-down over-claim scope fixes; **verify green**; eng≠discharge; flags unchanged |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | #110 tip `e8f585d…` **verify green** (5 checks); inventable pin only; #106 fail `pinned_sources_check` |
| Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) | `b2e1652…`; Cursor R1–R8+S ACCEPT on governance-; **COLLISION**: OA ANNULUS-BRIDGE + ANNULUS-STITCH both claim fixed-annulus stitch (`|t|~r^{1/24}`) — serialize; do not race |
| Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) | `b420099…` AUTHOR-SIDE; hosted replay green ≠ theorem; **Cursor (2)–(8) ACCEPT** (`amendments/20260925-math21-axial-density-review.md`); inner axial belt only; do not race |
| Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) | `e93eade…` C6 follow-through; **Cursor R1–R6 ACCEPT** (`amendments/20260925-math19-finite-r-review.md`); bind this head not `ee8629f`; sci effect NONE; #22 tube lane separate |
| Math- [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) | `e707da6…`; **replay green**; **undrafted** — hosted witness verified; ready for distinct-lane check; no self-approval |
| Math- [#16](https://github.com/d6g8k5htny-coder/Math-/pull/16) | `32b80ee…`; **Cursor R1–R5 ACCEPT** (`amendments/20260925-math16-transverse-review.md`); fixed-η transverse count only — **not** PR9 acceptance; do not race |
| Outside reviews (#15/#16/#18/#19/#21/#22) | #15 eng ACCEPT; #16 R1–R5 ACCEPT; #18 MATCH×7; #19 R1–R6 ACCEPT; #21 (2)–(8) ACCEPT; #22 R1–R8+S ACCEPT — all on governance-; #98 AMEND_REQUIRED on main author lane |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `6da327b…` REVIEW_TOPOLOGY v1.1; **Cursor policy ACCEPT** of five findings (`amendments/20260925-review-topology-rereview.md`); keep DRAFT; sci effect NONE |

### Closed without merge (2026-09-25)

| PR | Note |
|---|---|
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | SUPERSEDED/BLOCKED INPUT — mapped known-bad #9 fingerprints; successor only after six-pin repair |

## This agent

App write: `governance-` only. Do not race #4's `REVIEW_TOPOLOGY.md` or peer ACTIVE leases in [`work_leases/CURRENT.json`](../work_leases/CURRENT.json).
