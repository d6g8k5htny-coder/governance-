#!/usr/bin/env python3
"""Fail-closed checker for governance work-lease / collision ledger.

Scientific effect: NONE. Coordination coverage only — not claim status,
not review acceptance, not theorem discharge.

Catches:
- ACTIVE lease with empty evidence
- ACTIVE lease past expires_at (stale heartbeat)
- two ACTIVE leases with overlapping write_scope (unless delegates_to)
- ACTIVE lease whose source.pr_state is closed/merged
- scientific_authority not false
- duplicate work_id
- invalid state token
"""

from __future__ import annotations

import argparse
import json
import posixpath
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALLOWED_STATES = frozenset({"OFFERED", "ACTIVE", "BLOCKED", "RELEASED", "SUPERSEDED"})
CLOSED_PR_STATES = frozenset({"closed", "merged"})
SCHEMA = "governance.work-leases/v1"
ROOT = Path(__file__).resolve().parent
DEFAULT_LEDGER = ROOT / "CURRENT.json"


def parse_ts(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def normalized_scope_path(path: str) -> str:
    """Normalize a lexical POSIX scope without resolving filesystem links."""
    normalized = posixpath.normpath(path)
    if (path.startswith("/") or "\\" in path or ":" in path or "\0" in path
            or normalized == ".." or normalized.startswith("../")):
        raise ValueError("write_scope path must be repository-relative: " + ascii(path))
    return normalized


def path_overlap(a: str, b: str) -> bool:
    """True when two write_scope entries collide (exact or prefix)."""
    if not a or not b:
        return False
    a = normalized_scope_path(a)
    b = normalized_scope_path(b)
    if a == b or a == "." or b == ".":
        return True
    # Component-prefix rule: a scope collides with anything beneath it at a path-component
    # boundary. This is the conservative reading of the write_scope contract ("path prefixes
    # this lease may edit") and needs no file-vs-directory guessing from the name: ".github"
    # and "docs.v1" collide with their children, "docs/" still collides, while "docs/a.md"
    # does not collide with the sibling "docs/a.md.bak". Name-based classification (dot in
    # basename, suffix heuristics) was tried and misclassified dotted directory prefixes, so
    # it is intentionally not used here. The former fallback `"/" not in a + "/"` was dead
    # code (always false) and is gone.
    return b.startswith(a + "/") or a.startswith(b + "/")


def scopes_overlap(left: list[str], right: list[str]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for a in left:
        for b in right:
            if path_overlap(a, b):
                hits.append((a, b))
    return hits


def delegation_allows(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return a.get("delegates_to") == b.get("work_id") or b.get("delegates_to") == a.get("work_id")


def check_lease(lease: dict[str, Any], now: datetime, problems: list[str]) -> None:
    wid = lease.get("work_id", "<missing>")
    state = lease.get("state")
    if not isinstance(state, str) or state not in ALLOWED_STATES:
        problems.append(f"{wid}: invalid state {state!r}")
        return
    if lease.get("scientific_authority") is not False:
        problems.append(f"{wid}: scientific_authority must be false")
    scope = lease.get("write_scope")
    if scope is not None and not (isinstance(scope, list) and all(isinstance(p, str) and p for p in scope)):
        # A string here would be iterated character by character by scopes_overlap and evade the
        # ACTIVE overlap check; refuse the shape instead of guessing what was meant.
        problems.append(f"{wid}: write_scope must be a list of nonempty strings, got {type(scope).__name__}")
    elif scope is not None:
        for path in scope:
            try:
                normalized_scope_path(path)
            except ValueError as exc:
                problems.append(f"{wid}: {exc}")
    if state != "ACTIVE":
        return
    evidence = lease.get("evidence")
    if (not isinstance(evidence, list) or not evidence
            or not all(isinstance(item, str) and item.strip() for item in evidence)):
        problems.append(f"{wid}: ACTIVE requires nonempty evidence list of nonempty strings")
    try:
        expires = parse_ts(lease["expires_at"])
        heartbeat = parse_ts(lease["heartbeat_at"])
    except (KeyError, ValueError) as exc:
        problems.append(f"{wid}: bad timestamps ({exc})")
        return
    if heartbeat >= expires:
        problems.append(f"{wid}: heartbeat_at must be before expires_at")
    if now >= expires:
        problems.append(f"{wid}: ACTIVE lease expired at {lease['expires_at']} (stale; move to BLOCKED/RELEASED)")
    source = lease.get("source")
    if source is None:
        source = {}
    elif not isinstance(source, dict):
        problems.append(f"{wid}: source must be an object or null")
        return
    pr_state = source.get("pr_state")
    if pr_state is not None and not isinstance(pr_state, str):
        problems.append(f"{wid}: source.pr_state must be a string or null")
        return
    if pr_state in CLOSED_PR_STATES:
        problems.append(
            f"{wid}: ACTIVE lease has pr_state={pr_state!r}; release/supersede when PR closes"
        )


def _write_scope_shape_ok(lease: dict[str, Any]) -> bool:
    """True when write_scope is absent or a list of safe nonempty strings.

    Malformed scopes are already reported by check_lease; they must be
    excluded here, because the pairwise scopes_overlap comparison below
    calls path_overlap's string methods and crashes on non-string entries.
    """
    scope = lease.get("write_scope")
    if scope is None:
        return True
    if not (isinstance(scope, list) and all(isinstance(p, str) and p for p in scope)):
        return False
    try:
        for path in scope:
            normalized_scope_path(path)
    except ValueError:
        return False
    return True


def check_ledger(doc: dict[str, Any], now: datetime | None = None) -> list[str]:
    if not isinstance(doc, dict):
        return ["ledger must be an object"]
    now = now or datetime.now(timezone.utc)
    problems: list[str] = []
    schema = doc.get("schema", SCHEMA)
    if not isinstance(schema, str) or schema != SCHEMA:
        problems.append(f"unsupported ledger schema {ascii(schema)}; expected {SCHEMA!r}")
    if doc.get("scientific_authority") is not False:
        problems.append("ledger scientific_authority must be false")
    leases = doc.get("leases")
    if not isinstance(leases, list):
        return problems + ["leases must be a list"]
    seen: dict[str, dict[str, Any]] = {}
    for lease in leases:
        if not isinstance(lease, dict):
            problems.append("lease entry must be an object")
            continue
        wid = lease.get("work_id")
        if not isinstance(wid, str) or not wid:
            problems.append("lease missing work_id")
            continue
        if wid in seen:
            problems.append(f"duplicate work_id {wid}")
        seen[wid] = lease
        check_lease(lease, now, problems)

    active = [L for L in seen.values() if L.get("state") == "ACTIVE" and _write_scope_shape_ok(L)]
    for i, a in enumerate(active):
        for b in active[i + 1 :]:
            hits = scopes_overlap(a.get("write_scope") or [], b.get("write_scope") or [])
            if hits and not delegation_allows(a, b):
                sample = ", ".join(f"{x}~{y}" for x, y in hits[:3])
                problems.append(
                    f"ACTIVE write_scope overlap: {a['work_id']} vs {b['work_id']} ({sample})"
                )
    return problems


def self_test() -> None:
    """Synthetic fixtures proving the two required catches."""
    now = parse_ts("2026-09-25T18:30:00Z")
    base = {
        "schema": "governance.work-leases/v1",
        "scientific_authority": False,
        "leases": [],
    }

    overlap_doc = {
        **base,
        "leases": [
            {
                "work_id": "a",
                "state": "ACTIVE",
                "scientific_authority": False,
                "write_scope": ["tools/foo.py"],
                "evidence": ["https://example.test/a"],
                "claimed_at": "2026-09-25T18:00:00Z",
                "heartbeat_at": "2026-09-25T18:10:00Z",
                "expires_at": "2026-09-26T00:00:00Z",
                "source": {"pr_state": "open"},
                "delegates_to": None,
            },
            {
                "work_id": "b",
                "state": "ACTIVE",
                "scientific_authority": False,
                "write_scope": ["tools/"],
                "evidence": ["https://example.test/b"],
                "claimed_at": "2026-09-25T18:00:00Z",
                "heartbeat_at": "2026-09-25T18:10:00Z",
                "expires_at": "2026-09-26T00:00:00Z",
                "source": {"pr_state": "open"},
                "delegates_to": None,
            },
        ],
    }
    overlap_problems = check_ledger(overlap_doc, now=now)
    if not any("write_scope overlap" in p for p in overlap_problems):
        raise AssertionError(f"expected overlap catch, got {overlap_problems}")

    closed_doc = {
        **base,
        "leases": [
            {
                "work_id": "c",
                "state": "ACTIVE",
                "scientific_authority": False,
                "write_scope": ["docs/x.md"],
                "evidence": ["https://example.test/c"],
                "claimed_at": "2026-09-25T18:00:00Z",
                "heartbeat_at": "2026-09-25T18:10:00Z",
                "expires_at": "2026-09-26T00:00:00Z",
                "source": {"pr": 1, "pr_state": "closed"},
                "delegates_to": None,
            }
        ],
    }
    closed_problems = check_ledger(closed_doc, now=now)
    if not any("pr_state='closed'" in p or 'pr_state="closed"' in p or "pr_state='closed'" in p for p in closed_problems):
        if not any("pr_state=" in p and "closed" in p for p in closed_problems):
            raise AssertionError(f"expected closed-PR catch, got {closed_problems}")

    offered_doc = {
        **base,
        "leases": [
            {
                "work_id": "d",
                "state": "OFFERED",
                "scientific_authority": False,
                "write_scope": ["anywhere/"],
                "evidence": [],
                "claimed_at": "2026-09-25T18:00:00Z",
                "heartbeat_at": "2026-09-25T18:00:00Z",
                "expires_at": "2026-09-26T00:00:00Z",
                "source": {"pr_state": None},
                "delegates_to": None,
            }
        ],
    }
    if check_ledger(offered_doc, now=now):
        raise AssertionError("OFFERED lease must not be treated as ACTIVE failure")


def unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Refuse duplicate members, including escaped spellings and nested keys."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON member " + ascii(key))
        result[key] = value
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--now",
        default=None,
        help="ISO-8601 UTC override for expiry checks (tests/replay)",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        self_test()
        print("work_leases self-test: OK")
        return 0

    try:
        doc = json.loads(args.ledger.read_text(encoding="utf-8"), object_pairs_hook=unique_json_object)
    except ValueError as exc:
        print("work_leases: FAIL", file=sys.stderr)
        print(f"  - {exc}", file=sys.stderr)
        return 1
    now = parse_ts(args.now) if args.now else datetime.now(timezone.utc)
    problems = check_ledger(doc, now=now)
    if problems:
        print("work_leases: FAIL", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    n = len(doc.get("leases") or [])
    active = sum(1 for L in doc.get("leases") or [] if L.get("state") == "ACTIVE")
    offered = sum(1 for L in doc.get("leases") or [] if L.get("state") == "OFFERED")
    print(
        f"work_leases: OK leases={n} ACTIVE={active} OFFERED={offered} "
        f"scientific_authority=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
