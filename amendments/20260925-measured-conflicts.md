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
| CONTRIBUTION_PLAN stale next-items retired (LPW REFUTED via lpw README) | Hard gate + own-node + REFUTED HOLD | Math- [#8](https://github.com/d6g8k5htny-coder/Math-/pull/8)+[#11](https://github.com/d6g8k5htny-coder/Math-/pull/11)+[#13](https://github.com/d6g8k5htny-coder/Math-/pull/13) @ `baca69c…` |

## Process rules proven

1. Closed `math_status` packet; transcription edits co-update `PACKET.json` digests.
2. Do not casually edit twelve-project-pinned `OPEN_PROBLEMS.md` (#107 used archive-pinned errata instead).
3. Gate: own-node `PROVED_REVIEWED` + required deps in `REQUIRED_SATISFIED`; required `REFUTED`/`BLOCKED_ABSENT` HOLD.
4. New hardening `verify` commands need `closure_pipeline` allowlisting (#98 hit this).
5. Math- exact-replay pins (`SOURCE_FILES` / workflow hashes): editing `hard_gate.py` / `test_hard_gate.py` without regenerating identities fails with `ValueError: source identity mismatches: hard_gate.py,test_hard_gate.py` (Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) @ `7eb4afe…`, run `36171889414`).
6. Citing a register tab from new prose requires updating `registers/CONSUMERS.json` in the **same** change: `consumers_check` compares recorded vs scanned prose consumers (main [#105](https://github.com/d6g8k5htny-coder/main/pull/105) @ `36fe375…` body claimed the map update; tip file list is only `docs/CONTRIBUTION_PLAN.md` → `NEW lpw_fold_dispositions: prose consumers differ`).

## Still open (do not race)

| PR | Tip / note |
|---|---|
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | `6742548…`; **CONFLICTING**; **AMEND REQUIRED** vs [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) six-pin witness; tip still algebraic-factor skeleton (not finite-r repair) |
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | `6f72f8a…`; **BLOCKED** pending #9/#17 pin repair; fingerprint align to thin-belt-factor tip |
| Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) | `8c4c946…`; **replay green** (67-test/24-mutant package); DRAFT awaiting distinct-lane review — do not concurrent-edit; supplies snapshot CLI contract for main #98 AMEND |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | author reduction paused |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | `0449280…`; verify green; OpenAI **AMEND_REQUIRED** — wire real base→head CI (reuse Math- #15 snapshot CLI contract); tip self-audit ≠ change propagation; Cursor owns repair |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | #110 tip `e8f585d…` after #105; CI re-queued; #106 fail `pinned_sources_check` |
| Math- [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) | `e707da6…`; OpenAI D5 pin-compatibility review (six-pin Fraction witness + 16 tests); REVIEW.md sha256 `105831c6…` |
| Math- [#16](https://github.com/d6g8k5htny-coder/Math-/pull/16) | `32b80ee…`; OpenAI review package: finite-r pin counterexample + real before/after adapter probes (evidence for #9/#98 findings); not a status flip |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `da195ed…`; `REVIEW_TOPOLOGY.md` only — no path overlap with this PR |

## This agent

App write: `governance-` only. Do not race #4's `REVIEW_TOPOLOGY.md` or peer ACTIVE leases in [`work_leases/CURRENT.json`](../work_leases/CURRENT.json).
