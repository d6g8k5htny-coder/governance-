# D6 analytic review — frozen parent `PROOF.md` (Math- #18 assignment)

**Assignment:** [Math- #18 comment 5840296378](https://github.com/d6g8k5htny-coder/Math-/pull/18#issuecomment-5840296378)  
**Object:** `frontiers/full_price_20260924/PROOF.md` blob `582180e41dca0ad815ad0f18574df42040912149`  
**SHA256 (measured):** `87521901ca8e5405b4d1e47f1deb1cd0326affbd6f5967b53c4178590da993f9` (11352 B) — MATCH  
**PR18 tip (pilot packaging only):** `0ae7e8fdf5d359f80cf6a3dcd614120f7aa9a19c` — not edited  

**Reviewer provenance:** Cursor / governance- App agent (`cursor[bot]`); run [`bc-01a0d95a-a107-7b98-886c-8e978b5fab08`](https://cursor.com/agents/bc-01a0d95a-a107-7b98-886c-8e978b5fab08). Cursor branding ≠ organizational independence. Same GitHub App identity as other Cursor lanes ≠ provider independence credit.  

**Scientific effect: NONE.** Scoped analytic disposition only. Not P15 theorem acceptance. Not unrestricted prize / register flip. Prior SMT MATCH×7 treated only as checked algebraic substeps. App cannot comment on Math-; this file is the durable record.

---

## Slice dispositions

| # | Slice | Verdict | Notes |
|---|---|---|---|
| 1 | Coordinatewise hazard + separate-concavity / chord; p=0,1 | **ACCEPT** | (F4)–(F8): one-coordinate mixture `A0+B0 e^{-t_i}` under decreasingness; `∂²F≤0` is separate concavity only; chord + iteration → (F6); `t_i=φ(p_i)` with `p'_i≤p_i` including `p_i=1` (`φ(1)=1`); zero-prob product factor handled without division. No joint-concavity claim. |
| 2 | Capacity/clutter local-good; binomial ratio; worst case n=3,a=1 | **AMEND** | (F9)–(F11) chain for `1/2<p<1` and application at interior `p_⋆=1-e^{-1}` is sound: adjoining two trials gives `(1-p)²P(S=a+1)-p²P(S=a)=p(1-2p)P(S=a)<0` when `P(S=a)>0`. **Defect:** (F10) writes `p>1/2` and strict `<0` without excluding `p=1`. At `p=1`, `S=2a+1` a.s. so `P(S=a)=0` and the difference is `0`, not strictly negative. Scope-correct to `1/2<p<1` (or note endpoint degeneracy). `p_⋆` application and `H_(n,a)≥H_(3,1)=h_⋆>1` for the realized class remain intact after that wording fix. |
| 3 | Global hazard: local→global; independence; product → `-log μ_p(D)` | **ACCEPT** | (F13): disjoint blocks ⇒ independent local good-events; global good ⇒ all locals good ⇒ `μ(D)≤∏μ(D_i)` ⇒ sum of local hazards ≤ global hazard. Independence is used for the product of local measures, not for “crossing failures.” Zero local/global good-prob capped by price-one. Sum of (F12) + palette coverage ⇒ (F2). |
| 4 | Coverage: full-block generators; `K≥K_H(d)`; realized family | **ACCEPT** | Explicitly binds original realized covers (SHA `c0dbb821…`) and `K_H(d)` palette — not arbitrary downsets. Full-block `{X_i}` cover of `O_K(D)` is cited as already proved in the realized-cover source; this parent supplies the price/hazard budget, not a new setwise cover proof. Scope sentence (“not unrestricted downset/prize”) is correct. |
| 5 | Sharpness at capacity-one / demand-two; alternative covers | **ACCEPT** | Single block `a=1,d=2,n=3`, `K=2`, no macro edges: unique nonempty obstruction is the full triple; at `p_i=p_⋆`, `c_i=1` every generator costs 1 while hazard `=h_⋆`, so any smaller factor than `ρ_⋆=1/h_⋆` breaks (F2). Applies to alternative generator covers, not only the chosen full-block cover. |
| 6 | Demand-one boundary / counterexample; exact theorem scope | **ACCEPT** | `d=1`, `n=a+1`, `K=1`: at `p_⋆,c=1` cover cost ≥1 but hazard `<1` via `μ=1-p_⋆^{a+1}>e^{-1}`. Correctly states this falsifies a *uniform same-palette transformed-price guarantee admitting all d=1 examples*, without claiming necessity of `d≥2` for every multi-block mixed-demand instance. Preserves P15-B local-budget distinction. |

---

## F10 / p=1 precision (explicit)

- **Application point:** `p_⋆=1-e^{-1}∈(1/2,1)` is interior — the odd-majority comparison used for `H_(3,1)` is valid there.
- **Parent wording defect:** §3 (F10) asserts strict negativity for all `p>1/2`, which includes `p=1` where both binomial masses at level `a` vanish and the signed difference is zero. **AMEND** the hypothesis to `1/2 < p < 1` (matching the additive SMT endpoint clarification already MATCH’d as non-verbatim).
- No counterexample to Theorem F’s stated `d_i≥2` realized-class claim was found from this endpoint issue alone.

---

## Overall scoped theorem disposition

**AMEND_REQUIRED** solely for (F10) endpoint wording (`p>1/2` strict `<0` → `1/2<p<1`). Slices 1,3–6 **ACCEPT** at the exact realized-family / `K≥K_H(d)` / transformed-price scope of Theorem F.

This is **not** ACCEPT of an unrestricted prize theorem, not Gaussian/RN closure, and not a status flip. SMT MATCH×7 does not discharge these analytic/combinatorial interfaces beyond the algebraic identities they encode.

**Re-bind** after a tip/parent wording repair (or an explicit parent erratum sentence). Sci effect NONE.
