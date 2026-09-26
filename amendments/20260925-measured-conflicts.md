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
| REVIEW_TOPOLOGY v1.1 (policy; sci effect NONE) | governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) @ `6da327b…` merged |
| Finite-r Hermite repair (deterministic C6; sci effect NONE) | Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) @ `e93eade…` merged |
| Thin-tube / FIXED_ANNULUS candidate (sci effect NONE; R6 citation note stands) | Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) @ `2804dc1…` merged |
| All-height annulus bridge candidate (sci effect NONE; R6 citation note stands) | Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) @ `dedc69e…` merged |
| Inner axial density candidate package (sci effect NONE; not theorem) | Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) @ `b420099…` merged |
| Transition-integrity eng package (sci effect NONE; not theorem acceptance) | Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `8c4c946…` merged |
| Scientific-state schema pilot / claims→gate adapter (eng only; sci effect NONE) | main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) @ `b59359e…` → merge `ebedb78…` |

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
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | **CLOSED UNMERGED** SUPERSEDED BLOCKED INPUT (5841262266); falsified six-pin leading rows; do not consume |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | `36fb7eb…` **CLOSED** SUPERSEDED/BLOCKED INPUT (stale #9 fingerprint map post-#19) |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | **SUPERSEDED/NONBLOCKING** at fixed-annulus+height-window (5840305109); PR22 route reviewed; not global D5 |
| Math- [#18](https://github.com/d6g8k5htny-coder/Math-/pull/18) | SMT MATCH done; D6 analytic **AMEND F10** on governance-; peer redirected to D6 (not SMT redo) |
| main [#90](https://github.com/d6g8k5htny-coder/main/issues/90) | Still **OPEN** — eng-gate close pending after #98 merge receipt `ebedb78…` |
| main [#112](https://github.com/d6g8k5htny-coder/main/pull/112) | Section3 **C1–C5 ACCEPT** + Section4 **R1–R5 ACCEPT** + Section5 **N1–N6 ACCEPT**; Sections6+ outside |
| main [#118](https://github.com/d6g8k5htny-coder/main/pull/118) | `435d8c8…` byte-exact Q0_LEDGER mirror; **CI green** (5 checks); keep DRAFT; serialize with #98 Q0 packaging |
| Math- [#49](https://github.com/d6g8k5htny-coder/Math-/pull/49) | `596e809…` collision/simplex integrate; **CI green**; observe; merge ≠ theorem |
| main [#120](https://github.com/d6g8k5htny-coder/main/pull/120) | `7ed8d1e…` SIDE24 source-custody; **verify FAIL** `36205808386` (certificates 11≠10); author-lane; no re-ratification |
| Math- [#46](https://github.com/d6g8k5htny-coder/Math-/pull/46) | `79a791a…` lemma/theorem reading maps; **observe**; ready-for-review |
| main [#121](https://github.com/d6g8k5htny-coder/main/pull/121) | `2624262…` Q0-C103 pair-Palm; **CI green**; observe; eng≠theorem |
| main [#122](https://github.com/d6g8k5htny-coder/main/pull/122) | `d49be07…` SARD-G repair; **CI green**; observe; eng≠theorem |
| main [#111](https://github.com/d6g8k5htny-coder/main/pull/111) | `7b874c0…`; RN-UNIF walk-down over-claim scope fixes; **verify green**; eng≠discharge; flags unchanged |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | #110 tip `e8f585d…` **verify green** (5 checks); inventable pin only; #106 fail `pinned_sources_check` |
| Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) | `dedc69e…` **MERGED**; Cursor R6 AMEND stands (AAL 7.1); merge ≠ theorem accept |
| Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) | `2804dc1…` **MERGED**; Cursor R6 AMEND stands (citation); merge ≠ theorem accept |
| Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) | `b420099…` **MERGED**; Cursor (2)–(8) ACCEPT on governance-; inner axial only; merge ≠ RN closure |
| Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) | `e93eade…` **MERGED**; Cursor R1–R6 ACCEPT on governance-; merge ≠ theorem acceptance; sci effect NONE |
| Math- [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) | **CLOSED** CONSUMED REVIEW EVIDENCE — six-pin witness (5841313010) |
| Math- [#16](https://github.com/d6g8k5htny-coder/Math-/pull/16) | **CLOSED** SUPERSEDED/CONSUMED EVIDENCE (5841312565) |
| Outside reviews (#15/#16/#18/#19/#21/#22) | #15 eng ACCEPT; #16 R1–R5 ACCEPT; #18 MATCH×7; #19 R1–R6 ACCEPT; #21 (2)–(8) ACCEPT; #22 R1–R8+S ACCEPT — all on governance-; #98 AMEND_REQUIRED on main author lane |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `6da327b…` **MERGED**; P1–P5 ACCEPT |

### Closed without merge (2026-09-25)

| PR | Note |
|---|---|
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | SUPERSEDED/BLOCKED INPUT — mapped known-bad #9 fingerprints; successor only after six-pin repair |
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | CLOSED UNMERGED SUPERSEDED BLOCKED INPUT — falsified leading pins; jets≠repair (5841262266) |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | SUPERSEDED/BLOCKED INPUT — closed unmerged after #19/#21 land; history preserved |
| Math- [#37](https://github.com/d6g8k5htny-coder/Math-/pull/37) | Section9 Borel repair MERGED @ `694b7ff…`; xAI C1–C6 ACCEPT (scoped) |
| Math- [#47](https://github.com/d6g8k5htny-coder/Math-/pull/47) | CLOSED UNMERGED duplicate of #37 |
| Math- [#38](https://github.com/d6g8k5htny-coder/Math-/pull/38) | BLOCKED_INPUT closed — fingerprint sync of unrepaired #9 (5840255614) |

## This agent

App write: `governance-` only. Do not race #4's `REVIEW_TOPOLOGY.md` or peer ACTIVE leases in [`work_leases/CURRENT.json`](../work_leases/CURRENT.json).
| Math- [#52](https://github.com/d6g8k5htny-coder/Math-/pull/52)/[#53](https://github.com/d6g8k5htny-coder/Math-/pull/53) | D2 cumulative confirm / pin-neighborhood recon; **observe** |
| Math- [#54](https://github.com/d6g8k5htny-coder/Math-/pull/54) | `6e4085a…` proof-index amend delivered (TRANSVERSE blob MATCH); **Landing FAIL**; peer ACTIVE |
