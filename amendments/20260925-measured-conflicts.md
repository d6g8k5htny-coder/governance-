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
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | `9896386…` (Inventory algebraic-factor × height-r combined skeletons); **CONFLICTING**; **STOP/REPAIR** + revalidation — unshifted `6k y1^2` still present; jets ≠ repair; consume [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) @ `ee8629f…` after distinct-lane check |
| Math- [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) | `6a41ea9…`; remaps #9 `9896386…`; **SOURCE REVALIDATION BLOCK** — falsified pins; PR17/PR19 apply; jets ≠ repair; overlaps [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | DRAFT; no J0/Hessian until #9 pins repaired; D5 external-recon leads only (comment 5838994872) — subordinate to pin repair; no theorem credit |
| Math- [#18](https://github.com/d6g8k5htny-coder/Math-/pull/18) | `0ae7e8f…`; P15 SMT pilot green; translation audit + H5/H6 probe in trial [#121](https://github.com/d6g8k5htny-coder/trial/pull/121) @ `391f6a8…` (main issue [#113](https://github.com/d6g8k5htny-coder/main/issues/113)); same-provider ≠ acceptance; owner: **optional diagnostic only** (no platform); **CI green** @ `391f6a8…`; keep DRAFT |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | `776fdb75…`; `/tmp` report fix; **ALL CI green**; keep DRAFT pending OpenAI event-report readback; #90 OPEN; eng≠discharge |
| main [#112](https://github.com/d6g8k5htny-coder/main/pull/112) | `d5b75f9…`; tip-observe `e3cd7d4…` after #105; **verify green**; serialize `PACKET.json` with #111 |
| main [#111](https://github.com/d6g8k5htny-coder/main/pull/111) | `7b874c0…`; RN-UNIF walk-down over-claim scope fixes; **verify green**; eng≠discharge; flags unchanged |
| main [#110](https://github.com/d6g8k5htny-coder/main/pull/110)/[#106](https://github.com/d6g8k5htny-coder/main/pull/106) | #110 tip `e8f585d…` **verify green** (5 checks); inventable pin only; #106 fail `pinned_sources_check` |
| Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) | `b420099…` AUTHOR-SIDE; hosted replay+Drive landing green (36185607110) — **≠ density theorem**; distinct review of PROOF.md (2)-(8) open; do not race |
| Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) | `ee8629f…`; author follow-through on C6 domain + constraint-solved tests (5839177785) — author-side ≠ outside acceptance; tip move stales review bind; distinct-lane review still required |
| Math- [#17](https://github.com/d6g8k5htny-coder/Math-/pull/17) | `e707da6…`; **replay green**; **undrafted** — hosted witness verified; ready for distinct-lane check; no self-approval |
| Math- [#16](https://github.com/d6g8k5htny-coder/Math-/pull/16) | `32b80ee…`; **REVIEW PICKUP** for `TRANSVERSE_BOUND_CANDIDATE.md` (R1–R5); assign distinct reviewer after #9 finite-pin repair — leave AUTHOR_SIDE if none |
| Outside reviews (#15/#16/#18/#19) | Assignments posted 5838821860/2651/2251/3056 — #15 eng ACCEPT on governance-; #16/#18/#19 still OFFERED |
| governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4) | `da195ed…`; distinct-lane **AMEND_REQUIRED** (same-account≠provider; stale Current application; STOP pause; schema vs #98) — see `amendments/20260925-review-topology-notes.md` |

### Closed without merge (2026-09-25)

| PR | Note |
|---|---|
| Math- [#14](https://github.com/d6g8k5htny-coder/Math-/pull/14) | SUPERSEDED/BLOCKED INPUT — mapped known-bad #9 fingerprints; successor only after six-pin repair |

## This agent

App write: `governance-` only. Do not race #4's `REVIEW_TOPOLOGY.md` or peer ACTIVE leases in [`work_leases/CURRENT.json`](../work_leases/CURRENT.json).
