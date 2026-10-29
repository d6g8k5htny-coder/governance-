# Work-lease / collision ledger

**Scientific effect: NONE.** Coordination only. Not a claim database, not scientific status, not review acceptance.

Machine-readable leases so agents can see who owns which write scopes without treating prose claims or idle Cloud Agents as activity evidence.

## Record fields

| Field | Meaning |
|---|---|
| `work_id` | Stable lease id |
| `scope` | Exact human-readable scope claim |
| `owner` | `{provider, model, agent}` when known |
| `source` | `{repo, branch, pr, issue}` identities |
| `claimed_at` / `heartbeat_at` / `expires_at` | ISO-8601 UTC |
| `state` | `OFFERED` \| `ACTIVE` \| `BLOCKED` \| `RELEASED` \| `SUPERSEDED` |
| `write_scope` | Path prefixes this lease may edit |
| `dependency_lane` | `D0`…`D7` (or `GOV`) |
| `scientific_authority` | Always `false` for this ledger |
| `evidence` | Fresh commit / comment / artifact URLs that justify ACTIVE |
| `delegates_to` | Optional `work_id` that may share overlapping write scope |

## Rules (enforced by `check_work_leases.py`)

1. `OFFERED` is never treated as `ACTIVE`.
2. `ACTIVE` requires `evidence` to be a nonempty list of nonblank strings, and `heartbeat_at` before `expires_at`. The checker validates the evidence shape; it does not fetch or authenticate the references.
3. Stale heartbeat (`heartbeat_at` ≥ `expires_at` or clock past `expires_at`) must not remain `ACTIVE` — use `BLOCKED` or `RELEASED`.
4. Two `ACTIVE` leases with overlapping `write_scope` paths fail unless one lists the other in `delegates_to`. Comparison normalizes POSIX `.`, `..` and repeated separators; `.` covers the repository. Absolute paths, parent escapes, backslashes, colons and NULs are refused. This is lexical path comparison; it does not resolve filesystem links.
5. An `ACTIVE` lease whose `source.pr_state` is `closed` or `merged` fails (lease must be `RELEASED` / `SUPERSEDED`).
6. Reviewer independence lineage is **not** recorded here; see `REVIEW_TOPOLOGY.md` / governance- [#4](https://github.com/d6g8k5htny-coder/governance-/pull/4). Writer ownership ≠ reviewer key.
7. A declared `schema` must be `governance.work-leases/v1`. Omitted schemas retain legacy API and CLI compatibility.
8. JSON duplicate members are refused at every nesting level, including keys spelled with escapes. Malformed JSON fails with a diagnostic and a nonzero exit status.

Run the input and collision controls in both modes:

```bash
python -B -S -m unittest discover -s work_leases -p 'test_*.py' -v
python -B -O -S -m unittest discover -s work_leases -p 'test_*.py' -v
python -B -S work_leases/check_work_leases.py --self-test
```

## Files

- `CURRENT.json` — retained historical lease snapshot (dated 2026-09-28), **not** a live ledger. Its counts are historical, not a current ownership census; see the [root README](../README.md) for the current characterization. For live coordination state, consult the actual task/scheduling instructions and the [current coordination board #619](https://github.com/d6g8k5htny-coder/main/issues/619) (continued from [#539](https://github.com/d6g8k5htny-coder/main/issues/539), [#475](https://github.com/d6g8k5htny-coder/main/issues/475) and the full [#419](https://github.com/d6g8k5htny-coder/main/issues/419)); the earlier [#307](https://github.com/d6g8k5htny-coder/main/issues/307) and [#229](https://github.com/d6g8k5htny-coder/main/issues/229) remain readable history.
- `check_work_leases.py` — fail-closed checker (stdlib only)
