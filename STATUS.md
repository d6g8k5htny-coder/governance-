# Governance repository state

This repository contains historical federation governance records and a
standard-library validator for coordination ledger inputs. It grants no
mathematical truth or kernel-verification status.

## Baseline state

CBZ-0 is NOT ESTABLISHED. Federation discovery and closure are in progress.
This repair closes four operational validation defects; it is not a final
G0-G11 federation verification pass.

## Verified scope

The validator refuses unsupported schema declarations, malformed ACTIVE
evidence, normalized overlapping scopes and duplicate JSON members.
All 35 fixture methods passed in normal, -O and -OO modes without skips;
the previous 22 methods and historical CURRENT.json bytes are unchanged.
Six adversarial source mutations were detected. Hosted execution is separate
evidence, not inferred from these local tests.

No mathematical obligation is declared CLOSED and no mathematical quarantine
is introduced by this repair. The historical ledger has no ACTIVE rows and
does not establish present CBZ ownership.

## How to verify

From the repository root with Python 3.11 or newer:

    python -B -S -m unittest discover -s work_leases -p 'test_check_work_leases*.py' -v
    python -B -O -S -m unittest discover -s work_leases -p 'test_check_work_leases*.py' -v
    python -B -OO -S -m unittest discover -s work_leases -p 'test_check_work_leases*.py' -v
    python -B -S work_leases/check_work_leases.py --self-test
    python -B -S work_leases/check_work_leases.py

The final command validates an unchanged historical snapshot, not live custody.
The existing hosted work-leases workflow runs matching fixtures in Python3.11
in normal and optimized modes. This repository has no Lean/kernel gate.

## Governance and decisions

[GOVERNANCE.md](GOVERNANCE.md) holds the rule/tool registry.
[DECISIONS.md](DECISIONS.md) is append-only.

Layer A: no placeholders, new unverified axioms, float bound certification,
weaker bounds/tests, hidden vacuity, false status or unsound auditor claims.
Never treat this operational validator as a Layer A or mathematical certifier.
