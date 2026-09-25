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
| SIDE24_CELL square importers | main [#102](https://github.com/d6g8k5htny-coder/main/pull/102) @ hardening tip `848aea2…` |
| Hard gate + own-node + REFUTED HOLD | Math- [#8](https://github.com/d6g8k5htny-coder/Math-/pull/8)+[#11](https://github.com/d6g8k5htny-coder/Math-/pull/11)+[#13](https://github.com/d6g8k5htny-coder/Math-/pull/13) @ `baca69c…` |

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
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | `8b615b1…`; replay green; **CONFLICTING** vs Math- `main` after #13; OpenAI review: label axial net r² diagnostic until compensation density bounded |
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | `1fd5ead…`; successor to closed [#12](https://github.com/d6g8k5htny-coder/Math-/pull/12); **replay green** (×2) |
| Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) | `7eb4afe…`; edge/complete-record transitions; **replay FAIL** until SOURCE_FILES regenerated (PR body already says keep draft until then) |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | author reduction paused |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | `0449280…`; schema pilot; allowlist fixed (`d765efa`); verify still pending/queued |
| main [#108](https://github.com/d6g8k5htny-coder/main/pull/108) | `92b10b0…`; tip-observe; one verify pass (`36171701033`), one still pending |
| main [#109](https://github.com/d6g8k5htny-coder/main/pull/109) | `86feed0…`; errata pointer; **verify green** (×2) |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | cellcount pins; #106 fail `pinned_sources_check` on `research/cover/ledger.py` digest drift; #110 verify still pending |
| main [#105](https://github.com/d6g8k5htny-coder/main/pull/105) | `36fe375…`; consumers map missing (see rule 6) |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `da195ed…`; `REVIEW_TOPOLOGY.md` only — no path overlap with this PR; OpenAI-authored, asks distinct-lane review |

## This agent

App write: `governance-` only. d=2 handoff superseded by Math- #9 / remapped by #14. Do not race #4's `REVIEW_TOPOLOGY.md`.

Machine coordination: [`work_leases/CURRENT.json`](../work_leases/CURRENT.json) (checker: `python3 work_leases/check_work_leases.py`).
