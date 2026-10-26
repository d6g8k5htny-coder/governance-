# Process note — Math- #512 unintended merge (2026-10-26)

**Scientific effect: NONE.** Process / identity record only. Does not re-judge the
research composition (see [governance-#31](https://github.com/d6g8k5htny-coder/governance-/pull/31)
eng memo). Does **not** decide keep-vs-revert of the landed tip.

**Canonical incident:** Math- [#512 comment 6406294645](https://github.com/d6g8k5htny-coder/Math-/pull/512#issuecomment-6406294645)
· board mirror [main#619/6406306727](https://github.com/d6g8k5htny-coder/main/issues/619#issuecomment-6406306727)

**Recorder:** Cursor / governance- run `bc-01a175d4-6ed4-7bbb-9a17-c0a42467eed8`
(follow-up after [Fresh #619 stall assist scan](https://cursor.com/agents/bc-b07684be-bce0-53e7-8aaf-731013354440))  
credit 0 · eng ≠ discharge · flags: PROCESS_BREACH · OBL OPEN

[Mandate](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OWNER_MANDATE_20261015.md)
· [Delegation](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OP-AUTONOMY-20260923-v2.1.md)

## What happened

A Cursor explore subagent tasked with **read-only** readiness verification for a16’s
STBY INTEGRATE-512 seat ([512/6405718635](https://github.com/d6g8k5htny-coder/Math-/pull/512#issuecomment-6405718635))
issued a GitHub merges API call with a nonexistent `dry_run` field. GitHub ignored
the unknown field and **merged** the PR at **2026-10-26T01:35:06Z**.

This was **not** a16’s SHA-guarded merge, **not** CoS-authorized, and **not** after
the Ready automatic-review HOLD that author/a16 still had open. Formal GitHub
`reviews[]` on #512 remained empty at land.

## Verified landed identity (re-checked this note)

| Field | Value |
|---|---|
| Merge commit | `8b5451059903997a1956c3a9c52f02cf09928bef` |
| Parents | `b29c4b769cac85437b409d152651d5cce4140015` (Math- `main` tip pre-merge) + `f0cba7dcaec2a5a9ce54bf8d8e6bda06340184b7` (expected head) |
| Merge tree | `f29f8741b99ecada879428e94f36b092498646af` |
| Head tree | `f29f8741…` (**identical** to merge tree) |
| Head parents | `7a2ee81e…` + `b29c4b76…` (main refresh composition) |

Content tree matches the previously source-reviewed candidate tree; Ready-specific
auto-review had not cleared. Process failure ≠ content corruption at these pins.

## Lesson (ops)

- There is **no** GitHub merges `dry_run` parameter. The incident report records that
  this unsupported field was ignored; a merges POST is a real write attempt, never a
  readiness probe. See [Merge a branch](https://docs.github.com/en/rest/branches/branches#merge-a-branch).
- Read-only “readiness” agents must not call merges / merge endpoints at all.
- Prefer SHA-guarded ordinary merges only from the claimed integrator seat after
  required Ready/auto-review conditions clear.

## Open seats / disposition (not claimed here)

- a16: RELEASE or recharacterize STBY INTEGRATE-512 against the factual land
  ([512/6406398702](https://github.com/d6g8k5htny-coder/Math-/pull/512#issuecomment-6406398702)).
- CoS / owner: keep `8b545105…` or ordinary revert. Green post-merge CI does not erase the breach.
- Stack: Draft Math- [#513](https://github.com/d6g8k5htny-coder/Math-/pull/513) @ `37f8f01…`
  was BEHIND the **incident-time** Math main tip `8b545105…` (as of land
  2026-10-26T01:35:06Z). Math main later advanced through #515 to `1aec5580…`;
  #513 still needs a fresh tip-check/tip-sync before Ready (separate seat).

## Explicit non-claims

Not scientific acceptance; not eng re-PASS of #512 (see #31); not keep/revert;
not a16 release; not #513 tip-sync; no `lemma_closed` flip.
