# Outside engineering review — Math- #15 @ `8c4c946…`

**Object:** Math- [#15](https://github.com/d6g8k5htny-coder/Math-/pull/15) head `8c4c946a85b68383b56efe1b52e7053b11d9470a`  
**Reviewer lane:** Cursor / governance- (author of main #98; not author of this PR)  
**Assignment:** [comment 5838821860](https://github.com/d6g8k5htny-coder/Math-/pull/15#issuecomment-5838821860)  
**Scientific effect: NONE.** Engineering integrity only. Not theorem acceptance. Does not close main #90.  
**Delivery constraint:** This App token cannot comment on Math-; mirror this ACCEPT onto Math- #15 from a Math-writable lane if needed.

Inspected package sources at the exact head (`hard_gate.py`, `git_transition_audit.py`, `test_transition_contract.py`, `test_hard_gate.py`, `run_validation.py`, README/SCOPE). Hosted replay green (run `36177977545`) treated as eng evidence only.

## V1 — strict graph / public-boundary validation — ACCEPT

- `validate_graph_fail_closed` / `_validate_graph_shape` (`hard_gate.py` ~303–366): `schema_version==1`, exact bool `controlling`, known classifications, edge shape, missing endpoints, duplicate edge keys, required-cycle detection.
- Public boundaries call validation: `promotion_allowed`, `closure_report`, `reverse_impact_between`, `git_transition_audit.read_snapshot`.
- Negatives: `test_unknown_classification_rejected`, `test_boolean_schema_rejected`, `test_contradictory_duplicate_rejected`, `test_promotion_boundary_checks_*`, `test_duplicate_json_key_refused`, `test_nonfinite_json_refused`.

## V2 — complete node/edge/context/source-byte transition detection — ACCEPT

- `reverse_impact_between` (~373–435): compares canonical node JSON, outgoing-edge signatures (incl. metadata), graph context excluding nodes/edges, and paired source snapshots when supplied.
- One-sided / partial snapshots refused (`test_one_sided_source_snapshot_refused`, `test_partial_source_snapshot_refused`).
- Context change seeds all nodes; edge metadata edit seeds child; typed JSON `True≠1` detected.

## V3 — changed-node self-hold + UNION(old,new) blast radius — ACCEPT

- Impacted seeds include changed nodes present in `new_nodes` (~408); legacy `reverse_impact` self-hold covered.
- Traversal uses `union_edges` of old∪new (~404–418); removed-edge dependents still reached.
- REFUTED preserved under revalidation (`test_refutation_is_not_erased_by_revalidation`).

## V4 — immutable Git base/head wiring — ACCEPT

- `read_snapshot` requires full lowercase 40/64-hex commit IDs; rejects branch names.
- Binds repo objects via `git cat-file` / `show`; external/http → `external_unresolved`; missing → `missing`; path traversal rejected.
- Output must be new and outside the repository. Real-commit source-only edit test passes.

## V5 — semantic mutations / negative controls / `promotion_permission=false` — ACCEPT

- Transition/report paths set `promotion_permission: False`.
- `refuse_non_discharge_promotion` rejects `GREEN_CI`.
- Mutant harness in `run_validation.py` remains assertion-detected; README requires 67 tests / 24 mutants in both `-O` modes.

## Explicit non-claims

Not branch-protection enforcement; not external-source fetch/monitor; not independent mathematical review; not #90 closure (main #98 adapter remains separate).

## Overall

**ACCEPT** at engineering scope for exact head `8c4c946…` only. Tip move stales this review.
