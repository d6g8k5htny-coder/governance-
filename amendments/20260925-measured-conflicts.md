# Measured conflicts — 2026-09-25

**Scientific effect: NONE.** Exact source identities and CI messages only. No research Boolean is flipped.

## 1. Downstream RN crosswalk land (closed)

| Field | Value |
|---|---|
| Wrong placement | main [#87](https://github.com/d6g8k5htny-coder/main/pull/87) put crosswalk inside closed `docs/math_status/` → `packet: unexpected files` (CLOSED) |
| Rescue | main [#92](https://github.com/d6g8k5htny-coder/main/pull/92) outside-packet path + challenge note (CLOSED superseded) |
| Default-home pointer | main [#93](https://github.com/d6g8k5htny-coder/main/pull/93) (CLOSED) |
| **Landed** | inventable [#97](https://github.com/d6g8k5htny-coder/main/pull/97) **MERGED** → hardening tip `388a22c…` (`docs/DOWNSTREAM_RN_CROSSWALK_20260925.md`, mesoscopic challenge, Math- #8 eligibility handoff docs) |

Pin lesson: do not edit byte-pinned `docs/OPEN_PROBLEMS.md` for discovery links; use unpinned pages or refresh `SUPPLEMENTAL_DEPENDENCIES` in the same change.

## 2. Math- hard gate

| Item | Status |
|---|---|
| Gate + own-node eligibility | Math- [#8](https://github.com/d6g8k5htny-coder/Math-/pull/8)+[#11](https://github.com/d6g8k5htny-coder/Math-/pull/11) **MERGED**; `CONTROLLING_ELIGIBLE={PROVED_REVIEWED}` on Math- `main` (28 tests OK locally) |
| Remaining hole | Required `REFUTED` still counts as terminal on tip; a self-`PROVED_REVIEWED` node with required REFUTED dep can become CONTROLLING (measured on Math- main). Fix: Math- [#13](https://github.com/d6g8k5htny-coder/Math-/pull/13) (draft hotfix: only PROVED_REVIEWED/SUPERSEDED_NONBLOCKING satisfy required edges) |
| D5 chart graph | Math- [#12](https://github.com/d6g8k5htny-coder/Math-/pull/12) maps [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) chart-J0 into the gate graph |
| Redundant | Math- [#10](https://github.com/d6g8k5htny-coder/Math-/pull/10) same-branch eligibility PR likely closeable |

## 3. Mesoscopic algebra

| Item | Status |
|---|---|
| Author reduction | Math- [#7](https://github.com/d6g8k5htny-coder/Math-/pull/7) draft; author paused upstream expansion pending D0–D4 |
| Challenge | Landed via #97 on hardening (`RN_MESOSCOPIC_REDUCTION_CHALLENGE_20260925.md`); independence credit 0 |
| Chart package | Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) typed `C_transverse`/`C_axial` + Hessian/thin-belt; 26+ tests |
| Governance seed | [`20260925-mesoscopic-d2-chart-handoff.md`](20260925-mesoscopic-d2-chart-handoff.md) superseded by #9 (powers matched) |

## 4. Other open drafts (do not race)

- main [#99](https://github.com/d6g8k5htny-coder/main/pull/99) ENV-RESCOV node walk-down — correct packet transcription+digest co-update + `math_status_nodes/`
- main [#98](https://github.com/d6g8k5htny-coder/main/pull/98) scientific-state schema pilot
- main [#100](https://github.com/d6g8k5htny-coder/main/pull/100)–[#104](https://github.com/d6g8k5htny-coder/main/pull/104) inventable/audit follow-ons

## 5. This agent’s write scope

Personal Cloud Agent environment repos: `[governance-]` only. Measured push: `governance-` OK; `main` / `Math-` / `trial` → `Permission denied to cursor[bot]` (403). Durable trial write is a separate vector ([MULTI_AGENT_ACCESS](https://github.com/d6g8k5htny-coder/trial/blob/main/docs/MULTI_AGENT_ACCESS.md)).
