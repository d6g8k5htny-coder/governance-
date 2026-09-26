# Outside mathematical review — Math- #21 @ `b420099…`

**Object:** Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21) head `b420099b2440da3a8ba62f7000feacc9fc88069b`  
**Package:** `frontiers/axial_density_20260925/` (PROOF.md + contact algebra)  
**Reviewer lane:** Cursor / governance- App agent (`cursor[bot]`); run [`bc-01a0d95a-a107-7b98-886c-8e978b5fab08`](https://cursor.com/agents/bc-01a0d95a-a107-7b98-886c-8e978b5fab08). Cursor branding ≠ organizational independence.  
**Assignment:** author offer in PROOF.md §6 / PR body — independently check (2)–(8); return ACCEPT/AMEND/COUNTEREXAMPLE per interface.  
**Scientific effect: NONE.** Density-sublemma review only. Not weighted Kac–Rice count, not full thin-belt, not RN_UNIF / 24-jet closure.  
**Delivery:** App cannot comment on Math-; this file is the durable review record.

## Method

Re-derived Hermite map (2)–(3) and normalization (4) by hand (Fraction); verified quartic residual → `α(u)=u(u²−1/4)/6`, minor (6), and gradient Jacobian `r⁵` (8). Local `run_validation.py` both modes: 15 tests + 5 semantic mutants assertion-detected; `RESULTS.json` SHA-256 matched. Hosted replay green ≠ theorem.

## Per-interface dispositions

| Interface | Disposition | Notes |
|---|---|---|
| **(2)** Hermite / divided-difference map | **ACCEPT** | `U=(S0−a²D1/2,(3D0−S1)/2,D1,3(S1−D0)/a²,L(0),L'(0))` recovers cubic+linear interpolants; invertible for every `r>0`. |
| **(3)** pinned vector + drift | **ACCEPT** | Under six pins: `U_r=(b−kr³/2,−(3/2)kr²,0,12k,0,0)`; `H'(ru)=6kr²(u²−1/4)` — matches independent finite-r repair (Math- #19), not unshifted PR9 `6ku²`. |
| **(4)** unconditional normalization `Y_r` | **ACCEPT** | `Y₁` subtracts `r² w L'` **before** conditioning; omitting it leaves divergent unconditioned `w f_xz(0)/r`. Contact module enforces this. |
| **(5)** uniform `L²` contact limits | **ACCEPT** | Quartic Hermite residual `(Q/24)(x²−a²)²` → `r³αQ`; linear `h` residual → `r²βT`; transverse Taylor in `z=r²w` yields claimed `Y_0`. Fourier moment rationale for this `K_L` is adequate for the written `L²` claim; pathwise C⁶ square control is the #19 contract, not required here. |
| **(6)** random-jet minor | **ACCEPT** | `αβ=u(u²−1/4)²/12≠0` on `A≤\|u\|≤B` with `A>1` (away from `0` and `±1/2`); `k` is a fixed mark, not a covariance axis. |
| **(7)** Schur / regression mean | **ACCEPT** | Joint jet PD via Fourier symbol / polynomial identity on `Z²`; compact frames + `(u,w)` give uniform eig bounds; Schur `λI≼Σ_r≼ΛI`; pinned mean `m_r` uniformly bounded for `k∈[k0,k1]`. |
| **(8)** density change of variables | **ACCEPT** | `∇f=(6kr²(u²−1/4)+r³Y₁, r²Y₂)` ⇒ det `r⁵`; target `\|t\|≥δk/r` with `δ=6(A²−1/4)`; Gaussian tail + mean domination by `k0>0` yields (1). |

## Scope exclusions — MATCH (as declared)

Correctly **not** claimed: height-conditioned density; conditional Hessian after large compensation; endpoint Palm weight / full normalizer; remaining belt `Wr<\|v\|<η`; pin/witness collisions; intermediate distances; `d=3`; numerical `C_H`; historical 24-jet certification. Gass–Stecconi cited as methodological prior art only.

## Cross-binding notes

- Equations are rederived in-package; citation of PR19 @ `ee8629f…` is context only — this ACCEPT does not depend on stale tip bytes (C6 successor is `e93eade…`, reviewed separately).
- Complementary [#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) tube lane is a distinct object; not reviewed here.
- Does **not** clear [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9) STOP/REPAIR or authorize [#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) fingerprint refresh.

## Overall

**ACCEPT** on interfaces (2)–(8) at exact head `b420099b2440da3a8ba62f7000feacc9fc88069b` for the declared **inner axial belt** density sublemma only. No AMEND and no COUNTEREXAMPLE found on those interfaces.

**Not awarded:** organizational independence; formal proof-assistant verification; any scientific-status / register flip; promotion of green eng replay to theorem credit.

**Provenance:** governance- branch `cursor/process-packet-scope-ab08`; App write limited to this repository.
