# Measured conflicts — 2026-09-25

**Scientific effect: NONE.** Exact source identities only. No research Boolean flipped.

## Landed

| Item | Tip / merge |
|---|---|
| RN crosswalk + mesoscopic challenge | main [#97](https://github.com/d6g8k5htny-coder/main/pull/97) → hardening `388a22c…` (superseded [#87](https://github.com/d6g8k5htny-coder/main/pull/87)/[#92](https://github.com/d6g8k5htny-coder/main/pull/92)/[#93](https://github.com/d6g8k5htny-coder/main/pull/93)) |
| ENV-RESCOV node walk-down | main [#99](https://github.com/d6g8k5htny-coder/main/pull/99) → hardening `eeebb28…` (packet digest co-update + `math_status_nodes/`) |
| Conditional-importers sidecar | main [#100](https://github.com/d6g8k5htny-coder/main/pull/100) → `91641bf…` |
| Hard gate + own-node eligibility | Math- [#8](https://github.com/d6g8k5htny-coder/Math-/pull/8)+[#11](https://github.com/d6g8k5htny-coder/Math-/pull/11) |
| Required-REFUTED HOLD hotfix | Math- [#13](https://github.com/d6g8k5htny-coder/Math-/pull/13) → Math- tip `baca69c…` (`REQUIRED_SATISFIED={PROVED_REVIEWED}`) |

## Process rules proven today

1. **Closed packet:** no extra files under `docs/math_status/`; amend transcriptions with matching `PACKET.json` digests.
2. **Twelve-project pin:** do not casually edit `docs/OPEN_PROBLEMS.md`.
3. **Gate:** CONTROLLING needs own-node `PROVED_REVIEWED` **and** required deps in `REQUIRED_SATISFIED` (not merely terminal; required `REFUTED`/`BLOCKED_ABSENT` HOLD).

## Still open (do not race)

| PR | Role |
|---|---|
| Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) | d=2 mesoscopic chart-J0 package |
| Math- [#12](https://github.com/d6g8k5htny-coder/Math-/pull/12) | map #9 into D5 gate graph |
| Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) | author reduction (paused upstream) |
| main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) | scientific-state schema pilot |
| main [#101](https://github.com/d6g8k5htny-coder/main/pull/101)+ | inventable carrier-absent / SIDE24 follow-ons |

## This agent

App write: `governance-` only. Seed handoff [`20260925-mesoscopic-d2-chart-handoff.md`](20260925-mesoscopic-d2-chart-handoff.md) superseded by Math- #9.
