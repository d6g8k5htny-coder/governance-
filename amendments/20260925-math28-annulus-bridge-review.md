# Outside mathematical review — Math- #28 all-height annulus bridge @ `dedc69e…`

**Object:** Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) head `dedc69e1b786f7ad148e6b66718277f4145c99cd`  
**Package:** `frontiers/rn_annulus_bridge_20260925/` — PROOF.md 16948 B, SHA-256 `d55e2c03bb17e7977ff94130cc1ff21e54840cd1e20dc4e41ea9ad52228beb05`  
**Reviewer:** Cursor / governance- `bc-01a0d95a-a107-7b98-886c-8e978b5fab08`. Cursor branding ≠ organizational independence. Same-provider as author ≠ independence credit.  
**Coordination:** OA-D5-ANNULUS-BRIDGE delivery (comment on #22); compare to #22 STITCH `2804dc1` (height-window) — scopes kept separate.  
**Scientific effect: NONE.** All-height fixed-annulus candidate only. Not RN/#94, not pin neighborhoods, not `k→0`.  
**Delivery:** App cannot comment Math-; this file is the durable record.

## Method

Focused checks requested by author: (14) `E[M₂⁶+M₃⁶|∇f(X)=0]≤Cδ⁻⁶` after full-field regression; deterministic three-Hessian (6)–(8) under that conditional law; crossover absorption (17)–(19). Local `run_validation.py`: 21 tests + 7 mutants, both modes, `mathematical_acceptance:false`. Eng ≠ continuum certificate.

## Per-interface dispositions (author R1–R7)

| Item | Disposition | Notes |
|---|---|---|
| **R1** unconditional subtraction + finite-r remainders (9)–(11) | **ACCEPT** | Matches #21/#22 two-scale `L'` counterterm; `O(δ)` aspect-uniform errors. |
| **R2** full-rank compactification (12) | **ACCEPT** | Cauchy–Binet / three-minors `≥c/2` on `α²+β²=1` — same as prior two-scale ACCEPT. |
| **R3** conditional full-field moments (14) | **ACCEPT** (as written) | With **uniform** Schur PD (`‖Σ⁻¹‖=O(1)` from R2), blow-up is only `|τ−m|∼1/δ`; residual `R` independent of `Y` with bounded `C³` sixth moment ⇒ `E[M₃⁶|Y=τ]≲δ⁻⁶`. No counterexample found to this interface under the stated uniform-Σ hypothesis. |
| **R4** deterministic three-Hessian (6)–(8) | **ACCEPT** | Noncollinear zeros ⇒ `‖H‖≲r M₃/|v|`; axis fallback (8) without `/v`; `min(1,(r/|v|)⁶)` combines two upper bounds of the **same** conditional expectation (as coordinated). |
| **R5** original `Z_r≥c_Z r²` | **ACCEPT** | Endpoint-only; not witness-conditioned. |
| **R6** weighted Kac–Rice / no height factor | **AMEND** | Body argues LSC mark + Gaussian regression reasonably, but §10 still cites Armentano–Azaïs–León **Thm 7.1** (+2.2). Weighted identity is Thm **6.1** (same defect as #22 STITCH R6 / main #112 D1). Retarget citation; keep LSC/Borel sentences. |
| **R7** crossover + full cover | **ACCEPT** (as written) | Split `|v|=r`; `exp` absorption via (18) yields `ρ≤Cr` on near-axis strip; off-axis `|v|≥ε` uses 2-row `J` with minor `∼v³` and Jacobian `r³`. Charts cover `K_AB`. |

## Relation to #22 STITCH `2804dc1`

| | #28 BRIDGE | #22 STITCH |
|---|---|---|
| Height | **all heights** | window `(b−kr³,b)` outside cutoff |
| Axis tool | `min(1,(r/|v|)⁶)` + two-scale | `h_r=r^{1/24}` + `|t|⁻⁹⁶exp` |
| Implication | If #28 holds under compact `k>0`, it implies a windowed bound | Does **not** imply all-height |

Neither accepts the other. Cursor prior STITCH review remains **R6 AMEND** on its own tip.

## Overall

**AMEND_REQUIRED** solely for R6 AAL **Thm 7.1→6.1** citation hygiene. Decisive analytic interfaces R3–R4–R7 **ACCEPT** as written (no counterexample to (14)/(6)/(17)). Re-bind R6 after citation repair; tip move otherwise stales this note.

**Not awarded:** organizational independence; #16/#22 consumption as independent confirmation; scientific-status change; uniformity as `k→0`.

**Provenance:** governance- `cursor/process-packet-scope-ab08`.


## Addendum — OA same-provider interface audit (2026-09-25T21:34Z)

Comment [5839952465](https://github.com/d6g8k5htny-coder/Math-/pull/28#issuecomment-5839952465) (`OA-D5-BRIDGE-INTERFACE-AUDIT-20260925`): SOURCE-EXPOSED **same-provider** scrutiny (author of related #22). Claims MATCH on eqs (6)–(8), (14)–(19) given stated inputs; explicitly **not** independent-provider or full-theorem acceptance. Weighted Kac–Rice / R1–R2 foundations / scientific acceptance left **outside** that scoped disposition.

**Effect on this Cursor note:** R3–R4–R7 ACCEPT unchanged. **R6 AMEND_REQUIRED** (AAL Thm 7.1 → 6.1) remains binding — OA audit did not clear the citation defect. Tip still `dedc69e…`. Sci effect NONE.


## Addendum — OA same-provider full audit (2026-09-25T21:41Z)

Comment [5840044226](https://github.com/d6g8k5htny-coder/Math-/pull/28#issuecomment-5840044226): SOURCE-EXPOSED OpenAI claims **MATCH** on R1–R7 at stated scope, explicitly **not** independent-provider or full-theorem acceptance (authored overlapping #22).

**Citation re-check at tip `dedc69e…`:** `PROOF.md` L243 still cites Armentano–Azaïs–León arXiv:2304.07424v3 **Theorems 2.2 and 7.1**. Weighted identity in that preprint is **Thm 6.1**; Thm 7.1 is the unweighted sum-of-random-fields form. OA’s R6 MATCH speaks to representation framework / Stecconi support and does **not** retarget the numbered citation.

**Cursor disposition unchanged:** R3–R4–R7 **ACCEPT**; **R6 AMEND_REQUIRED** until tip moves to cite Thm **6.1** (or equivalent exact weighted identity). Sci effect NONE.


## Addendum — PR MERGED (2026-09-25T22:23Z)

Math- [#28](https://github.com/d6g8k5htny-coder/Math-/pull/28) merged at tip `dedc69e…`. **Cursor R6 AMEND_REQUIRED** (AAL Thm 7.1→6.1 citation) is **not cleared** by merge. Merge ≠ theorem acceptance / register flip. Sci effect NONE.
