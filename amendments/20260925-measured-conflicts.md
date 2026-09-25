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
| Finite-r Hermite repair (deterministic C6; sci effect NONE) | Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) @ `e93eade…` merged |
| Thin-tube / FIXED_ANNULUS candidate (sci effect NONE; R6 citation note stands) | Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) @ `2804dc1…` merged |
| All-height annulus bridge candidate (sci effect NONE; R6 citation note stands) | Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) @ `dedc69e…` merged |
| Inner axial density candidate package (sci effect NONE; not theorem) | Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) @ `b420099…` merged |
| Transition-integrity eng package (sci effect NONE; not theorem acceptance) | Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `8c4c946…` merged |

## Process rules proven

1. Closed `math_status` packet; transcription edits co-update `PACKET.json` digests.
2. Do not casually edit twelve-project-pinned `OPEN_PROBLEMS.md` (#107 used archive-pinned errata instead).
3. Gate: own-node `PROVED_REVIEWED` + required deps in `REQUIRED_SATISFIED`; required `REFUTED`/`BLOCKED_ABSENT` HOLD.
4. New hardening `verify` commands need `closure_pipeline` allowlisting (#98 hit this).
5. Math- exact-replay pins (`SOURCE_FILES` / workflow hashes): editing `hard_gate.py` / `test_hard_gate.py` without regenerating identities fails with `ValueError: source identity mismatches: hard_gate.py,test_hard_gate.py` (Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `7eb4afe…`, run `36171889414`).
6. Citing a register tab from new prose requires updating `registers/CONSUMERS.json` in the **same** change: `consumers_check` compares recorded vs scanned prose consumers (main [#105](https://github.com/d6g8k5htny-coder/main/pull/105) @ `36fe375…` body claimed the map update; tip file list is only `docs/CONTRIBUTION_PLAN.md` → `NEW lpw_fold_dispositions: prose consumers differ`).
7. Do not refresh D5 hard-gate fingerprints from a STOP/REPAIR chart tip (Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) and [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) closed SUPERSEDED/BLOCKED INPUT; [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) leading pins remain unshifted — jets≠repair even after [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) merge).
8. CI that writes a new top-level directory (e.g. `artifacts/` via `--write-report`) must keep `REPOSITORY_TOP_LEVEL` / ignore lists in sync, or verify fails even when the feature under test is green (main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) run `36179103673`).

## Still open (do not race)

| PR | Tip / note |
|---|---|
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | `1e745d2…`; **STOP/REPAIR**; octacosic jets; jets≠repair |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | `36fb7eb…` **CLOSED** SUPERSEDED/BLOCKED INPUT (stale #9 fingerprint map post-#19) |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | **SUPERSEDED/NONBLOCKING** at fixed-annulus+height-window (5840305109); PR22 route reviewed; not global D5 |
| Math- [#18](https://github.com/d6g8k5htny-coder/Math-/pull/18) | SMT MATCH×7; D6 analytic **AMEND** F10 p=1 wording / slices 1,3–6 ACCEPT (`amendments/20260925-math18-d6-analytic-review.md`); keep DRAFT |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | `22d9976…` E complete; verify **SPLIT** (pass `36195412945` / fail `36195408373` Q0 revalidation refuse); **OA E re-review OFFERED**; #90 OPEN |
| main [#112](https://github.com/d6g8k5htny-coder/main/pull/112) | `d5b75f9…`; tip-observe `e3cd7d4…` after #105; **verify green**; serialize `PACKET.json` with #111 |
| main [#111](https://github.com/d6g8k5htny-coder/main/pull/111) | `7b874c0…`; RN-UNIF walk-down over-claim scope fixes; **verify green**; eng≠discharge; flags unchanged |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | #110 tip `e8f585d…` **verify green** (5 checks); inventable pin only; #106 fail `pinned_sources_check` |
| Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) | `dedc69e…` **MERGED**; Cursor R6 AMEND stands (AAL 7.1); merge ≠ theorem accept |
| Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) | `2804dc1…` **MERGED**; Cursor R6 AMEND stands (citation); merge ≠ theorem accept |
| Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) | `b420099…` **MERGED**; Cursor (2)–(8) ACCEPT on governance-; inner axial only; merge ≠ RN closure |
| Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) | `e93eade…` **MERGED**; Cursor R1–R6 ACCEPT on governance-; merge ≠ theorem acceptance; sci effect NONE |
| Math- [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) | `e707da6…`; **replay green**; **undrafted** — hosted witness verified; ready for distinct-lane check; no self-approval |
| Math- [#16](https://github.com/d6g8k5htny-coder/Math-/pull/16) | `32b80ee…`; **Cursor R1–R5 ACCEPT** (`amendments/20260925-math16-transverse-review.md`); fixed-η transverse count only — **not** PR9 acceptance; do not race |
| Outside reviews (#15/#16/#18/#19/#21/#22) | #15 eng ACCEPT; #16 R1–R5 ACCEPT; #18 MATCH×7; #19 R1–R6 ACCEPT; #21 (2)–(8) ACCEPT; #22 R1–R8+S ACCEPT — all on governance-; #98 AMEND_REQUIRED on main author lane |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `6da327b…` REVIEW_TOPOLOGY v1.1; **Cursor policy ACCEPT** of five findings (`amendments/20260925-review-topology-rereview.md`); keep DRAFT; sci effect NONE |

### Closed without merge (2026-09-25)

| PR | Note |
|---|---|
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | SUPERSEDED/BLOCKED INPUT — mapped known-bad #9 fingerprints; successor only after six-pin repair |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | SUPERSEDED/BLOCKED INPUT — closed unmerged after #19/#21 land; history preserved |
| Math- [#38](https://github.com/d6g8k5htny-coder/Math-/pull/38) | BLOCKED_INPUT closed — fingerprint sync of unrepaired #9 (5840255614) |

## This agent

App write: `governance-` only. Do not race #4's `REVIEW_TOPOLOGY.md` or peer ACTIVE leases in [`work_leases/CURRENT.json`](../work_leases/CURRENT.json).
