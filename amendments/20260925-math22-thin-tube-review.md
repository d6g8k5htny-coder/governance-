# Outside mathematical review — Math- #22 @ `b2e1652…`

**Object:** Math- [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) tip `b2e1652f1374c3b45759324a1ad1fd4177458500`  
**Core package (byte-identical to `35eddbb…`):** `PROOF.md`, `thin_tube.py`, `test_thin_tube.py`, `README.md`, `RECON.md`  
**Extension:** `TWO_SCALE_ADDENDUM.md` + `two_scale.py` / tests (new at tip)  
**Reviewer lane:** Cursor / governance- App agent (`cursor[bot]`); run [`bc-01a0d95a-a107-7b98-886c-8e978b5fab08`](https://cursor.com/agents/bc-01a0d95a-a107-7b98-886c-8e978b5fab08). Cursor branding ≠ organizational independence. Same-provider as author ≠ independence credit.  
**Assignment:** author offer R1–R8 on PROOF.md; addendum offers S6–S21 separately.  
**Scientific effect: NONE.** Author-side density/count candidates only. Not RN/annulus closure, not register flip.  
**Delivery:** App cannot comment on Math-; this file is the durable review record.

## Method

Independently checked T3/T4 pin target, contact coefficients `a(u)=u(u²−1/4)/6`, `b(u)=(u²−1/4)/2`, minor `ab=u(u²−1/4)²/12`, tube area `4K(B−A)r³`, and power ledger `r⁻²·r³·r⁻⁵·r⁻⁶=r⁻¹⁰`. Local unittest: 15 thin-tube + 13 two-scale methods PASS in normal and `-O` modes. Git blob SHAs of the five core files match `35eddbb…` exactly at tip.

## R1–R8 (original fixed-K thin tube)

| Item | Disposition | Notes |
|---|---|---|
| **R1** six-pin transform + target | **ACCEPT** | Invertible `U_r` (T3); pinned `v_r=(b−kr³/2,−kr²,0,12k,0,0)` (T4). Consistent with #21 Hermite coords via shear of det 1 (documented in addendum §2); neither invalidates the other. |
| **R2** uniform `L^p` Taylor + centered contact rows | **ACCEPT** | Homogeneous residual (T7)–(T10): `g_xxx=O(r²)⇒g_x=O(r⁴)`; scales `(r³,r²)` retain first random row. Fourier/`L^p` rationale matches #21. |
| **R3** periodic covariance rank + compactness | **ACCEPT** | Positive Fourier weights + polynomial-on-`Z²` argument; compact `O(2)` for uniform eig floors (T11)–(T12). Euclidean `diag(24,2,2)` correctly labeled sanity-only. |
| **R4** joint Gaussian large-deviation target | **ACCEPT** | Deterministic drift `\|μ_r\|≥c₀/r` from `6k(u²−1/4)/r` (T13); density (T14) with full 2×2 Schur — not a scalar-density inference. |
| **R5** extra-conditioning Hessian cost | **ACCEPT** | Stacked 9-vector; conditional mean `O(r⁻¹)`; crude `E[W F_j\|∇f=0]≤C r⁻⁶` (T15)–(T16) admissible vs exponential. |
| **R6** original full-normalizer floor | **ACCEPT** | Endpoint-only `Z_r≥c_Z r²` via `A_r=f_zz` event of uniform positive probability (T17)–(T18); no remote H3 numerical floor imported. |
| **R7** marked Kac–Rice + physical tube | **ACCEPT** (as written) | Stecconi arXiv:2103.10853v1 Thm 29 / §8.4 cited for weighted formula (T19); nondegeneracy away from pins argued for this `K_L`. Application scope is the declared local hypotheses — not a reprint of Stecconi's theorem. |
| **R8** excluded regimes | **ACCEPT** | Explicitly refuses full annulus, pin neighborhoods, `r≪\|x\|≪ρ`, collisions, `d≥3`, `k_-→0`, diverging `K(r)`. |

**Overall (R1–R8):** **ACCEPT** for the declared shrinking-width tube sublemma at the byte-identical core (`35eddbb…` / tip core files). No COUNTEREXAMPLE. Eng tests ≠ analytic certificate.

## Two-scale addendum (S-interfaces) — tip `b2e1652…`

| Block | Disposition | Notes |
|---|---|---|
| **S6–S9** pins / subtraction / Jacobian | **ACCEPT** | Hermite/affine `U_r`; essential `r t L'` counterterm; `diag(r²δ, rδ)` ⇒ `r³ δ²`. |
| **S10–S12** aspect-uniform remainders | **ACCEPT** | Errors `O(δ)` with no hidden `1/α`/`1/β`; limit matrix `M(u,α,β)`. |
| **S13–S15** all-minors rank | **ACCEPT** | Cauchy–Binet `det(MMᵀ)≥m₀/2` on `α²+β²=1` restores rank at both aspect ends. Exact minors checked by two-scale tests. |
| **S16–S19** rare cost / normalizer / Kac–Rice | **ACCEPT** (as written) | Same structure as R5–R7 with `δ`-powers; `Z_r≥c_Z r²` reused. |
| **S20–S21** width corollaries | **ACCEPT** (quantifiers) | Power-width `ε=K r^γ` and log-width `D_N/√log(1/r)` as stated; correctly **not** a fixed-ε annulus closure (still retains `r⁻³` in crude (S5)). |
| **Explicit complement** | **MATCH** | Intermediate fixed scaled width remains open; same-provider #21/#22 disclosed. |

**Overall (two-scale):** **ACCEPT** on the declared near-axis crossover / shrinking-width corollaries only. Does **not** close fixed-ε scaled annulus.

## Explicit non-awards

- Not organizational or cross-provider independence.
- Not acceptance of Math- [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) chart program or fingerprint refresh for [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20).
- Not weighted global RN count / 24-jet / elder-selection theorems.
- Tip move past `b2e1652…` stales this review.

**Provenance:** governance- `cursor/process-packet-scope-ab08`; App write limited to this repository (cannot push `main`/`Math-`/`trial`).
