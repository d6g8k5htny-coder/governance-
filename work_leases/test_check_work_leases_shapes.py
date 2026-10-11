"""Negative controls for check_work_leases.py (scientific effect NONE).

Run: python3 -B -S -m unittest work_leases.test_check_work_leases_shapes -v
Each test fails against the pre-repair checker (string write_scope evaded the overlap check;
LICENSE-style scopes were misclassified; `or True` made the Taylor regression vacuous).
"""
import unittest
from datetime import datetime, timedelta, timezone

from work_leases import check_work_leases as c

NOW = datetime(2026, 10, 12, tzinfo=timezone.utc)


def lease(wid, scope, **extra):
    base = {"work_id": wid, "state": "ACTIVE", "scientific_authority": False, "evidence": ["x"],
            "expires_at": (NOW + timedelta(hours=1)).isoformat(), "heartbeat_at": NOW.isoformat(),
            "write_scope": scope}
    base.update(extra)
    return base


class WriteScopeShape(unittest.TestCase):
    def test_string_write_scope_is_refused_not_iterated(self):
        problems = c.check_ledger({"leases": [lease("a", "docs/"), lease("b", ["docs/x.md"])]}, now=NOW)
        self.assertTrue(any("write_scope must be a list" in p for p in problems), problems)

    def test_list_of_non_strings_is_refused(self):
        problems = c.check_ledger({"leases": [lease("a", ["docs/", 3])]}, now=NOW)
        self.assertTrue(any("write_scope must be a list" in p for p in problems), problems)

    def test_two_active_overlapping_lists_still_collide(self):
        problems = c.check_ledger({"leases": [lease("a", ["docs/"]), lease("b", ["docs/x.md"])]}, now=NOW)
        self.assertTrue(any("ACTIVE write_scope overlap" in p for p in problems), problems)

    def test_malformed_scope_excluded_from_pairwise_not_crashed(self):
        # Two-row regression: [3] vs ['docs/x.md']. The malformed row is
        # reported and excluded from pairwise comparison; it must not reach
        # path_overlap's string methods (AttributeError pre-fix).
        problems = c.check_ledger({"leases": [lease("a", [3]), lease("b", ["docs/x.md"])]}, now=NOW)
        self.assertTrue(any("write_scope must be a list" in p for p in problems), problems)
        self.assertFalse(any("ACTIVE write_scope overlap" in p for p in problems), problems)

    def test_noniterable_scope_excluded_from_pairwise(self):
        # Non-list scope (int 3) against another ACTIVE row: reported and
        # excluded; scopes_overlap must never iterate a non-list.
        problems = c.check_ledger({"leases": [lease("a", 3), lease("b", ["docs/x.md"])]}, now=NOW)
        self.assertTrue(any("write_scope must be a list" in p for p in problems), problems)
        self.assertFalse(any("ACTIVE write_scope overlap" in p for p in problems), problems)

    def test_dotted_directory_prefix_collides_with_child(self):
        # G16-R1 regression: ".github" is a directory claim (leading dot is not
        # an extension), so it collides with ".github/workflows/check.yml".
        # Both orders; ledger-level scientific_authority=False per the fixture.
        doc = lambda a, b: {"scientific_authority": False,
                            "leases": [lease("a", [a]), lease("b", [b])]}
        for a, b in [(".github", ".github/workflows/check.yml"),
                     (".github/workflows/check.yml", ".github")]:
            with self.subTest(a=a, b=b):
                problems = c.check_ledger(doc(a, b), now=NOW)
                self.assertTrue(any("ACTIVE write_scope overlap" in p for p in problems), problems)


class PathOverlapClassification(unittest.TestCase):
    def test_marked_directory_collides_with_child(self):
        self.assertTrue(c.path_overlap("docs/", "docs/x.md"))

    def test_sibling_files_do_not_collide(self):
        self.assertFalse(c.path_overlap("docs/a.md", "docs/b.md"))

    def test_extensionless_name_is_a_directory_claim(self):
        self.assertTrue(c.path_overlap("LICENSE", "LICENSE/anything"))
        self.assertTrue(c.path_overlap("LICENSE", "LICENSE"))

    def test_dotted_file_is_not_a_prefix(self):
        self.assertFalse(c.path_overlap("docs/a.md", "docs/a.md.bak"))


if __name__ == "__main__":
    unittest.main()
