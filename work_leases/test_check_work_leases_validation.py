"""Lease-input refusal and preservation controls; scientific effect NONE.

The old checker accepts the four regression classes. Tests use real API/CLI
entry points and disposable ledgers, with child optimization mode propagated.
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

from work_leases import check_work_leases as checker

NOW_TEXT = "2026-10-29T16:00:00Z"
NOW = checker.parse_ts(NOW_TEXT)
SCRIPT = Path(checker.__file__).resolve()


def lease(work_id="a", **changes):
    row = {
        "work_id": work_id,
        "state": "ACTIVE",
        "scientific_authority": False,
        "write_scope": [f"docs/{work_id}.md"],
        "evidence": ["https://example.invalid/evidence"],
        "heartbeat_at": "2026-10-29T15:00:00Z",
        "expires_at": "2026-10-29T17:00:00Z",
        "source": {"pr_state": "open"},
    }
    row.update(changes)
    return row


def ledger(*rows, **changes):
    doc = {
        "schema": "governance.work-leases/v1",
        "scientific_authority": False,
        "leases": list(rows),
    }
    doc.update(changes)
    return doc


class LeaseValidation(unittest.TestCase):
    def run_cli(self, raw, *, ascii_output=False):
        flags = ["-B", "-S"] + ["-O"] * sys.flags.optimize
        env = {key: value for key, value in os.environ.items()
               if key not in {"PYTHONHOME", "PYTHONPATH", "PYTHONOPTIMIZE",
                              "PYTHONSTARTUP", "PYTHONINSPECT"}}
        if ascii_output:
            env["PYTHONIOENCODING"] = "ascii"
        with tempfile.TemporaryDirectory(prefix="lease-validation-") as tmp:
            path = Path(tmp) / "ledger.json"
            data = raw.encode("utf-8")
            path.write_bytes(data)
            result = subprocess.run(
                [sys.executable, *flags, str(SCRIPT),
                 "--ledger", str(path), "--now", NOW_TEXT],
                cwd=tmp, env=env, capture_output=True, timeout=10,
                check=False,
            )
            self.assertEqual(path.read_bytes(), data, "CLI changed input bytes")
            return result

    def assert_cli_refused(self, raw, diagnostic, **options):
        result = self.run_cli(raw, **options)
        self.assertEqual(result.returncode, 1, result)
        self.assertEqual(result.stdout, b"", result)
        self.assertTrue(result.stderr.startswith(b"work_leases: FAIL\n"), result)
        self.assertIn(diagnostic.encode("ascii"), result.stderr)
        self.assertNotIn(b"Traceback", result.stderr)

    def assert_refused(self, doc, diagnostic):
        with self.subTest(entry="API"):
            before = copy.deepcopy(doc)
            problems = checker.check_ledger(doc, now=NOW)
            self.assertTrue(any(diagnostic in problem for problem in problems), problems)
            self.assertEqual(doc, before, "API changed input")
        with self.subTest(entry="CLI"):
            self.assert_cli_refused(json.dumps(doc), diagnostic)

    def test_unsupported_declared_schema_is_refused(self):
        for value in ("other", "governance.work-leases/v2", None, True, 1, [], {}):
            with self.subTest(schema=value):
                self.assert_refused(ledger(schema=value), "unsupported ledger schema")

    def test_supported_and_omitted_schema_preserve_legacy_inputs(self):
        for declared in (True, False):
            doc = ledger(lease())
            if not declared:
                del doc["schema"]
            before = copy.deepcopy(doc)
            self.assertEqual(checker.check_ledger(doc, now=NOW), [])
            result = self.run_cli(json.dumps(doc))
            self.assertEqual(result.returncode, 0, result)
            self.assertEqual(result.stderr, b"", result)
            self.assertEqual(
                result.stdout,
                b"work_leases: OK leases=1 ACTIVE=1 OFFERED=0 scientific_authority=false\n",
            )
            self.assertEqual(doc, before)

    def test_active_evidence_requires_nonempty_string_list(self):
        values = (None, "", "evidence", False, True, 0, 1, {}, [],
                  [""], ["  "], [None], [False], [1], [{}], [["x"]])
        for value in values:
            with self.subTest(evidence=value):
                self.assert_refused(
                    ledger(lease(evidence=value)), "ACTIVE requires nonempty evidence",
                )
        row = lease()
        del row["evidence"]
        self.assert_refused(ledger(row), "ACTIVE requires nonempty evidence")

    def test_nonactive_evidence_preserves_historical_semantics(self):
        for state in ("OFFERED", "BLOCKED", "RELEASED", "SUPERSEDED"):
            doc = ledger(lease(state=state, evidence=None,
                               heartbeat_at=None, expires_at=None))
            self.assertEqual(checker.check_ledger(doc, now=NOW), [])
            self.assertEqual(self.run_cli(json.dumps(doc)).returncode, 0)

    def test_normalized_scope_aliases_cannot_hide_active_overlap(self):
        pairs = (
            ("./tools/x.py", "tools/x.py"),
            ("tools//x.py", "tools/x.py"),
            ("unused/../tools/x.py", "tools/x.py"),
            ("tools/./", "tools/x.py"),
            (".", "tools/x.py"),
            ("tools/..", "docs/x.md"),
            ("./docs.v1/", "docs.v1/x.md"),
        )
        for left, right in pairs:
            for a, b in ((left, right), (right, left)):
                with self.subTest(left=a, right=b):
                    self.assert_refused(
                        ledger(lease("a", write_scope=[a]), lease("b", write_scope=[b])),
                        "ACTIVE write_scope overlap",
                    )

    def test_path_overlap_api_uses_the_same_lexical_identity(self):
        for left, right in (("./tools/x.py", "tools/x.py"),
                            ("tools/../docs", "docs/x.md"),
                            (".", "LICENSE")):
            with self.subTest(left=left, right=right):
                self.assertTrue(checker.path_overlap(left, right))
                self.assertTrue(checker.path_overlap(right, left))

    def test_normalized_siblings_and_delegation_remain_valid(self):
        for left, right in (("./docs/a.md", "docs/b.md"),
                            ("docs/../tools/a", "tools/ab"),
                            ("./docs/a.md", "docs/a.md.bak")):
            with self.subTest(left=left, right=right):
                self.assertFalse(checker.path_overlap(left, right))
                doc = ledger(lease("a", write_scope=[left]), lease("b", write_scope=[right]))
                self.assertEqual(checker.check_ledger(doc, now=NOW), [])
        doc = ledger(lease("a", write_scope=["./tools/"], delegates_to="b"),
                     lease("b", write_scope=["tools/x.py"]))
        self.assertEqual(checker.check_ledger(doc, now=NOW), [])
        self.assertEqual(self.run_cli(json.dumps(doc)).returncode, 0)

    def test_unsafe_scope_paths_are_refused(self):
        for path in ("/tools/x.py", "//server/x.py", "../tools/x.py",
                     "tools/../../x.py", "C:/tools/x.py", "tools\\x.py", "tools/\0x.py"):
            with self.subTest(path=path):
                self.assert_refused(
                    ledger(lease(write_scope=[path])),
                    "write_scope path must be repository-relative",
                )

    def test_invalid_paths_do_not_hide_later_lease_checks(self):
        doc = ledger(
            lease("unsafe", write_scope=["../outside"]),
            lease("closed", source={"pr_state": "closed"}),
            lease("a", write_scope=["./shared"]),
            lease("b", write_scope=["shared/x.md"]),
        )
        for diagnostic in ("unsafe: write_scope path", "closed: ACTIVE lease",
                           "ACTIVE write_scope overlap: a vs b"):
            with self.subTest(diagnostic=diagnostic):
                self.assert_refused(doc, diagnostic)

    def test_duplicate_root_authority_json_is_refused_in_both_orders(self):
        for members in (
            '"scientific_authority":true,"scientific_authority":false',
            '"scientific_authority":false,"scientific_authority":true',
            '"scientific_authority":false,"scientific_authority":false',
            '"scientific_authority":true,"scientific_\\u0061uthority":false',
        ):
            with self.subTest(members=members):
                raw = '{"schema":"governance.work-leases/v1","leases":[],' + members + '}'
                self.assert_cli_refused(raw, "duplicate JSON member 'scientific_authority'")

    def test_nested_duplicate_members_are_refused(self):
        doc = ledger(lease(source={"pr_state": "open"}))
        raw = json.dumps(doc).replace(
            '"pr_state": "open"', '"pr_state": "closed", "pr_state": "open"',
        )
        self.assert_cli_refused(raw, "duplicate JSON member 'pr_state'")

    def test_duplicate_key_diagnostic_is_ascii_safe(self):
        raw = '{"scientific_authority":false,"leases":[],"雪":1,"\\u96ea":2}'
        self.assert_cli_refused(
            raw, "duplicate JSON member '\\u96ea'", ascii_output=True,
        )

    def test_malformed_json_uses_failure_diagnostic_without_traceback(self):
        self.assert_cli_refused('{"leases":', "Expecting value")


if __name__ == "__main__":
    unittest.main()
