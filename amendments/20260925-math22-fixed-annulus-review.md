# Outside mathematical review — Math- #22 fixed-annulus stitch @ `2804dc1…`

**Object:** Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) tip `2804dc1db27ef3b1fdef6bb350b486162692cc4a`  
**New package:** `FIXED_ANNULUS_CANDIDATE.md` (17646 B; SHA-256 `1fd9fe7141e464fd1c09ebf0318d8a701729c9c61ea24f73f7e20a9cf10c552b`) + `annulus.py` / `test_annulus.py` / `ANNULUS_RECON.md`  
**Prior ACCEPT still binds:** core five files + `TWO_SCALE_*` remain **byte-identical** to `b2e1652…` (R1–R8 + S ACCEPT in `amendments/20260925-math22-thin-tube-review.md`).  
**Reviewer:** Cursor / governance- `bc-01a0d95a-a107-7b98-886c-8e978b5fab08`. Cursor branding ≠ organizational independence. Same-provider as author ≠ independence credit.  
**Scientific effect: NONE.** Height-windowed fixed-annulus stitch candidate only. Not all-height full annulus, not RN/#94.  
**Delivery:** App cannot comment Math-; this file is the durable record.

## Method

Verified contact minor `t^6/24` on columns `(S,C,D)`, Cauchy–Binet lower bound `det(MMᵀ)≥t^{12}/576`, cutoff margin `12q=½` for `q=1/24`, and r-power ledger (−6+6+3−2 → +1 physical intensity). Local `test_annulus` 12/12 PASS. Eng ≠ analytic certificate.

## Per-interface dispositions (author R1–R8)

| Item | Disposition | Notes |
|---|---|---|
| **R1** six-pin regression + original `Z_r≥c_Z r²` | **ACCEPT** | Matches #19/#21/#22 Hermite target `(b−kr³/2,−(3/2)kr²,0,12k,0,0)`; endpoint-only floor as before. |
| **R2** `J_r` expansion (A10) + O(r) Cov perturbation | **ACCEPT** | Height residual cancels quadratic/`C` as in #16; `‖Cov(J_r)−MGMᵀ‖≤Cr` absolute (not relative to vanishing floor). |
| **R3** eigenfloor + cutoff | **ACCEPT** | `λ_min(MGMᵀ)≳\|t\|¹²` via `(t⁶/24)²`; `h_r=r^{1/24}` ⇒ `r/\|t\|¹²≤√r→0` — cutoff chosen **after** explicit floor (not η(r) into unspecified PR16 constants). |
| **R4** joint density + retained exp | **ACCEPT** (as written) | Uses `zᵀΣ⁻¹z≥z₁²/Σ₁₁` to keep `exp(−c/t²)` in the **joint** 3D density; Jacobian `r⁻⁶`. |
| **R5** three-gradient Hessians + conditional `C³` | **ACCEPT** (as written) | `‖H‖≲r\|t\|⁻¹ M₃`; crude `E[M₃⁶|…]≲\|t\|⁻⁷²` from `‖Σ⁻¹‖≲\|t\|⁻¹²`; product `≲r⁶\|t\|⁻⁷⁸`. Deliberately non-sharp. |
| **R6** weighted / height-disintegrated Kac–Rice | **AMEND** | Cites Armentano–Azaïs–León arXiv:2304.07424v3 **Theorem 7.1** (+2.2). Same citation defect flagged on main #112 D1 §9 review: Thm 7.1 is not the weighted identity (weighted form is Thm **6.1**; unweighted Gaussian zeros Thm **2.2**). Retarget citation / write the LSC→Borel hypotheses explicitly. Algebraic intensity ledger does not cure the import label. |
| **R7** inner-strip + region union | **ACCEPT** (as written) | Reuses two-scale (A25) on `|t|<h_r`; `δ²≤2r^{1/12}` ⇒ `ρ≤C r` via exponential domination; height window only helps. Boundary null sets OK. |
| **R8** scope | **ACCEPT** | Explicitly **not** all-height full annulus; height window essential outside `h_r`; excludes pins, `B₀→∞`, intermediate distances, collisions, `d≥3`, `k_→0`, 24-jet. |

## Overall

**AMEND_REQUIRED** (R6 citation / weighted-import hygiene only). Algebraic stitch ledger R1–R5 and R7–R8 **ACCEPT** as author-side candidate mathematics pending the Kac–Rice citation repair.

After R6 amend lands on a new immutable tip, re-bind and re-check R6 only (other interfaces stay ACCEPT unless tip bytes change).

**Not awarded:** organizational independence; all-height `O(r³)` over the fixed annulus; consumption of #16/#22 as independent confirmation; scientific-status change.

**Provenance:** governance- `cursor/process-packet-scope-ab08`.


## Addendum — consolidation (2026-09-25T21:34Z)

Author comment [5839954609](https://github.com/d6g8k5htny-coder/Math-/pull/22#issuecomment-5839954609): keep #22 unchanged as windowed fallback; prioritize full nonauthor of #28 remaining foundations/weighted KR; no third proof; neither candidate silently superseded. Cursor **R6 AMEND** on this tip (`2804dc1…`) still stands. Sci effect NONE.
