# Measured board-pointer matrix — 2026-10-26

**Scientific effect: NONE.** Navigation / onboarding pointers only. No research
Boolean, lease, claim, or workflow contract is changed by this note.

**Current board (live):** [main#619](https://github.com/d6g8k5htny-coder/main/issues/619) **OPEN**
(successor to [#539](https://github.com/d6g8k5htny-coder/main/issues/539) **OPEN**;
[#475](https://github.com/d6g8k5htny-coder/main/issues/475) **CLOSED**;
[#419](https://github.com/d6g8k5htny-coder/main/issues/419) closed/full).

Measured by Cursor cloud run `bc-01a175d4-6ed4-7bbb-9a17-c0a42467eed8` after
sibling surveys ([Survey main open PRs](https://cursor.com/agents/bc-179e41e6-6e3f-579d-944f-47690587bba2),
[Survey Math and meta PRs](https://cursor.com/agents/bc-1652b9e3-d5ad-58a7-b1c9-0848d3c76b76)).
Tip SHAs below are `main` default-branch HEADs as of the measurement window
(~2026-10-26T01:35Z).

[Mandate](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OWNER_MANDATE_20261015.md)
· [Delegation](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OP-AUTONOMY-20260923-v2.1.md)

## Default-branch `AGENTS.md` (or equivalent) vs current board

| Repository | Tip (`main`) | Active-board pointer on tip | Gap | Open route PR (if any) |
|---|---|---|---|---|
| `governance-` | `25b10da3b6cb26423fd46aaee8427b87e3db6b21` | **#475** (closed) in `AGENTS.md` / `README.md`; also `REVIEW_TOPOLOGY.md` / `work_leases/README.md` | Missing #619 | [#27](https://github.com/d6g8k5htny-coder/governance-/pull/27) draft `9f2bda23299a` (AGENTS+README); [#28](https://github.com/d6g8k5htny-coder/governance-/pull/28) Ready `b70db9d8d957` (REVIEW_TOPOLOGY + work_leases README) |
| `meta-framework` | `fa610d66058ecf435393f87c827cc8d5e06bba54` | **#475** | Missing #619 | [#38](https://github.com/d6g8k5htny-coder/meta-framework/pull/38) draft `aa41439a6817` (AGENTS+README; wording matches gov #27 chain) |
| `main` | `1354bc8d62ba0418af2725c1350a19e3723704e5` | **#539** | Missing #619 | none observed in this sweep |
| `Math-` | `8b5451059903997a1956c3a9c52f02cf09928bef` | **#539** | Missing #619 | none observed |
| `query-` | `c4ece326e187ea6950e9dbbdf922f888759fb8c4` | **#539** | Missing #619 | none observed (0 open PRs) |
| `google-drive` | `ad08584b3ea9d533af10113e85169f471fa8ec93` | **#86** (closed downstream queue) | No #539/#619 | none observed (0 open PRs; archive onboarding) |

`AGENTS.md` blob SHAs at measurement (path identity only):

| Repo | `AGENTS.md` blob |
|---|---|
| Math- | `b9d03715a19f9ff0c5672349e4f99f30ab773b41` |
| meta-framework | `b8e84161a4d37b5e6f4af4369cbf3b37406147fb` |
| query- | `7686130c9d6bbb97a667a8c7639d65cafce87e42` |
| google-drive | `840a5833750ee6aa37a7706fce49003052614adc` |
| main | `ae458e9f99948c4f69e62e10280d27ccc71efe70` |

## Suggested copy pattern (docs-only; not applied here)

When a sibling opens a route PR, prefer the same history chain already used on
governance-#27 / meta-framework#38:

> active board [#619](https://github.com/d6g8k5htny-coder/main/issues/619)
> (continued from [#539](https://github.com/d6g8k5htny-coder/main/issues/539),
> [#475](https://github.com/d6g8k5htny-coder/main/issues/475) and the full
> [#419](https://github.com/d6g8k5htny-coder/main/issues/419))

Keep [#307](https://github.com/d6g8k5htny-coder/main/issues/307) /
[#229](https://github.com/d6g8k5htny-coder/main/issues/229) as readable history.
Do not transfer, renew, or release any claim by the pointer edit.

## Related open work (not owned by this note)

- governance-#27 nonauthor eng PASS_SCOPED_WITH_FINDINGS already posted; needs separate integrator.
- governance-#28 CI green; awaiting separate nonauthor eng review (author ≠ reviewer).
- meta-framework#38 still draft; empty check rollup expected for docs-only paths; needs eng review + integrator.
- Math-#512 Ready @ `f0cba7dcaec2…` (gates green, no reviews) is a separate scientific/eng lane — not a board-pointer task.

credit 0 · sci NONE · eng ≠ discharge · no flags · OBL OPEN
