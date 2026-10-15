"""JSON input-boundary regressions; coordination only, scientific effect NONE.

Run: python -B -S [-O] -m unittest discover -s work_leases \
     -p 'test_check_work_leases_input_types.py' -v
Only disposable ledgers are used. No real lease, repository or schedule is changed.
"""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from work_leases import check_work_leases as checker

NOW_TEXT = "2026-10-15T12:00:00Z"
NOW = checker.parse_ts(NOW_TEXT)
SCRIPT = Path(checker.__file__).resolve()
NON_STRINGS = (None, False, True, 0, 1, 1.5, [], ["x"], {})
NON_OBJECTS = (False, True, 0, 1, 1.5, "", "x", [], ["x"])


def lease(work_id="a", **changes):
    value = {
        "work_id": work_id,
        "state": "ACTIVE",
        "scientific_authority": False,
        "write_scope": [f"docs/{work_id}.md"],
        "evidence": ["https://example.invalid/evidence"],
        "heartbeat_at": "2026-10-15T11:00:00Z",
        "expires_at": "2026-10-15T13:00:00Z",
        "source": {"pr_state": "open"},
    }
    value.update(changes)
    return value


def ledger(*leases):
    return {"scientific_authority": False, "leases": list(leases)}


class InputTypes(unittest.TestCase):
    def run_cli(self, doc=None, *, self_test=False):
        # Outer -O/-OO is explicitly propagated; inherited Python settings cannot
        # silently turn the normal child into an optimized or different import run.
        flags = ["-B", "-S"] + ["-O"] * sys.flags.optimize
        env = {key: val for key, val in os.environ.items()
               if key not in {"PYTHONHOME", "PYTHONPATH", "PYTHONOPTIMIZE",
                              "PYTHONSTARTUP", "PYTHONINSPECT"}}
        with tempfile.TemporaryDirectory(prefix="lease-input-types-") as directory:
            path = Path(directory) / "ledger.json"
            raw = json.dumps(doc, ensure_ascii=True).encode("utf-8")
            path.write_bytes(raw)
            args = (["--self-test"] if self_test else
                    ["--ledger", str(path), "--now", NOW_TEXT])
            result = subprocess.run(
                [sys.executable, *flags, str(SCRIPT), *args],
                cwd=directory, env=env, capture_output=True, text=True,
                timeout=10, check=False,
            )
            self.assertEqual(path.read_bytes(), raw, "CLI changed the input ledger")
            return result

    def assert_refused(self, doc, diagnostic):
        # Separate subtests exercise both entry points even when the old API crashes.
        with self.subTest(entry="API"):
            before = copy.deepcopy(doc)
            try:
                problems = checker.check_ledger(doc, now=NOW)
            except (AttributeError, TypeError) as exc:
                self.fail(f"unhandled JSON input type: {type(exc).__name__}: {exc}")
            self.assertTrue(any(diagnostic in item for item in problems), problems)
            self.assertEqual(doc, before, "API changed the input ledger")
        with self.subTest(entry="CLI"):
            result = self.run_cli(doc)
            self.assertEqual(result.returncode, 1, result)
            self.assertEqual(result.stdout, "", result)
            self.assertTrue(result.stderr.startswith("work_leases: FAIL\n"), result.stderr)
            self.assertIn(diagnostic, result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_non_object_roots_are_reported(self):
        for value in (None, *NON_OBJECTS):
            with self.subTest(value=value):
                self.assert_refused(value, "ledger must be an object")

    def test_non_string_states_use_existing_invalid_state_diagnostic(self):
        for value in (*NON_STRINGS, "", "UNKNOWN"):
            with self.subTest(value=value):
                self.assert_refused(ledger(lease(state=value)), "a: invalid state")

    def test_active_timestamps_require_strings(self):
        for field in ("heartbeat_at", "expires_at"):
            for value in (*NON_STRINGS, "", "not-a-date"):
                with self.subTest(field=field, value=value):
                    self.assert_refused(ledger(lease(**{field: value})), "a: bad timestamps")

    def test_active_source_requires_object_or_null(self):
        for value in NON_OBJECTS:
            with self.subTest(value=value):
                self.assert_refused(ledger(lease(source=value)), "a: source must be an object")

    def test_active_pr_state_requires_string_or_null(self):
        for value in NON_STRINGS[1:]:
            with self.subTest(value=value):
                self.assert_refused(ledger(lease(source={"pr_state": value})),
                                    "a: source.pr_state must be a string")

    def test_malformed_rows_do_not_hide_later_diagnostics_or_overlap(self):
        doc = ledger(
            lease("state", state=[]),
            lease("time", heartbeat_at=None),
            lease("source", source=["x"]),
            lease("closed", source={"pr_state": "closed"}),
            lease("left", write_scope=["shared/"]),
            lease("right", write_scope=["shared/file.md"],
                  expires_at="2026-10-15T11:30:00Z"),
        )
        for diagnostic in ("state: invalid state", "time: bad timestamps",
                           "source: source must be an object", "closed: ACTIVE lease has pr_state='closed'",
                           "right: ACTIVE lease expired", "left vs right"):
            with self.subTest(diagnostic=diagnostic):
                self.assert_refused(doc, diagnostic)

    def test_valid_states_and_optional_source_preserved(self):
        for state in ("OFFERED", "ACTIVE", "BLOCKED", "RELEASED", "SUPERSEDED"):
            for source in (None, {}, {"pr_state": None}, {"pr_state": "open"}):
                with self.subTest(state=state, source=source):
                    row = lease(state=state, source=source)
                    if state != "ACTIVE":
                        # Existing non-ACTIVE semantics do not inspect timing/evidence.
                        row.update(evidence=[], heartbeat_at=None, expires_at=None)
                    doc = ledger(row)
                    before = copy.deepcopy(doc)
                    self.assertEqual(checker.check_ledger(doc, now=NOW), [])
                    self.assertEqual(doc, before)
                    result = self.run_cli(doc)
                    self.assertEqual(result.returncode, 0, result)
                    self.assertEqual(result.stderr, "", result)
                    self.assertEqual(
                        result.stdout,
                        f"work_leases: OK leases=1 ACTIVE={int(state == 'ACTIVE')} "
                        f"OFFERED={int(state == 'OFFERED')} scientific_authority=false\n",
                    )
        row = lease()
        del row["source"]
        self.assertEqual(checker.check_ledger(ledger(row), now=NOW), [])
        self.assertEqual(checker.check_ledger(ledger(), now=NOW), [])
        # Existing naive/offset timestamp conversion stays intact.
        self.assertEqual(checker.parse_ts("2026-10-15T12:00:00"), NOW)
        self.assertEqual(checker.parse_ts("2026-10-15T07:00:00-05:00"), NOW)

    def test_existing_refusals_and_delegation_preserved(self):
        cases = (
            (ledger(lease(evidence=[])), "ACTIVE requires nonempty evidence"),
            (ledger(lease(scientific_authority=True)), "scientific_authority must be false"),
            (ledger(lease(write_scope="docs/")), "write_scope must be a list"),
            (ledger(lease(), lease()), "duplicate work_id"),
            (ledger(lease(source={"pr_state": "merged"})), "pr_state='merged'"),
            (ledger(lease(heartbeat_at="2026-10-15T13:00:00Z")), "heartbeat_at must be before"),
            (ledger(None), "lease entry must be an object"),
            (ledger({}), "lease missing work_id"),
            ({"scientific_authority": False, "leases": {}}, "leases must be a list"),
        )
        for doc, diagnostic in cases:
            with self.subTest(diagnostic=diagnostic):
                self.assert_refused(doc, diagnostic)
        first = lease("a", write_scope=["docs/"])
        second = lease("b", write_scope=["docs/x.md"])
        self.assert_refused(ledger(first, second), "ACTIVE write_scope overlap")
        for donor, recipient in ((first, second), (second, first)):
            with self.subTest(delegator=donor["work_id"]):
                doc = ledger({**donor, "delegates_to": recipient["work_id"]}, recipient)
                self.assertEqual(checker.check_ledger(doc, now=NOW), [])
                self.assertEqual(self.run_cli(doc).returncode, 0)

    def test_programmer_type_errors_are_not_swallowed(self):
        error = TypeError("deliberate internal fault")
        with mock.patch.object(checker, "parse_ts", side_effect=error):
            with self.assertRaises(TypeError) as caught:
                checker.check_ledger(ledger(lease()), now=NOW)
            self.assertIs(caught.exception, error)
        error = AttributeError("deliberate internal fault")
        with mock.patch.object(checker, "check_lease", side_effect=error):
            with self.assertRaises(AttributeError) as caught:
                checker.check_ledger(ledger(lease()), now=NOW)
            self.assertIs(caught.exception, error)

    def test_existing_self_test_preserved(self):
        result = self.run_cli(self_test=True)
        self.assertEqual(result.returncode, 0, result)
        self.assertEqual(result.stdout, "work_leases self-test: OK\n")
        self.assertEqual(result.stderr, "", result)


if __name__ == "__main__":
    unittest.main()
