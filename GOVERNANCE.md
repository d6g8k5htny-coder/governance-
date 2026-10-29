# CBZ-0 governance and tool registry

Effective 2026-10-29 under the owner's Crystalline Baseline Protocol.
The current owner directive supersedes conflicting legacy approvals, freezes,
review-family requirements and routing ceremony. Decisions are autonomous
for CBZ-0; actual platform enforcement remains in effect.

## Layer A

No logical placeholders or stubbed closure; no unverified axiom injection;
no floating-point bound certification; no weakened bounds; no removed or
disabled failing tests without a precise quarantine; no hidden vacuity;
truthful status surfaces; self-verified auditing tools.

Layer B operational changes are recorded in DECISIONS.md. A coordination
record or green operational check supplies no mathematical evidence.

## Tool registry: work-leases

- Path: work_leases/check_work_leases.py.
- Purpose: validate ledger schema, record shape, evidence-list shape,
  expiry and normalized lexical write-scope collisions.
- Why: unsupported schema, malformed evidence, aliased overlapping paths
  and duplicate JSON authority members could previously pass.
- Run: python -B -S work_leases/check_work_leases.py --ledger FILE.json
- Self-test: python -B -S work_leases/check_work_leases.py --self-test
- Regression commands: STATUS.md, How to verify.
- Verification: 35 methods in normal, -O and -OO modes, no failures,
  errors or skips; four old-accept/new-refuse counterexamples and six
  killed source mutants. Original 22 methods and CURRENT.json unchanged.
- Limits: references are not authenticated; paths are normalized lexically,
  not resolved through filesystem aliases. Missing schema retains the tested
  v1 compatibility behavior; an explicit unsupported schema fails.
- Authority: operational validation only. No mathematical statement, kernel
  run, source custody, present ownership or Layer A compliance is certified.
  Historical CURRENT.json is not a current CBZ ownership map.
- Maintenance: self-contained Python standard-library tool.
