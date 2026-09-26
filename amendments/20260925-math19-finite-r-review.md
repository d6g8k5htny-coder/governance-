# Outside mathematical review — Math- #19 @ `e93eade…`

**Object:** Math- [#19](https://github.com/d6g8k5htny-coder/Math-/pull/19) head `e93eade078cac2e8b14aa39d402a3043b7cdb1c7`  
**Package:** `reviews/d5_finite_r_hermite_repair_20260925/` (REPAIR.md + C6_REMAINDERS.md + oracle)  
**Reviewer lane:** Cursor / governance- App agent (`cursor[bot]`); run [`bc-01a0d95a-a107-7b98-886c-8e978b5fab08`](https://cursor.com/agents/bc-01a0d95a-a107-7b98-886c-8e978b5fab08). Cursor branding ≠ organizational independence.  
**Assignment:** [comment 5838822251](https://github.com/d6g8k5htny-coder/Math-/pull/19#issuecomment-5838822251) (originally bound `ee8629f…`); rebound to successor C6 tip `e93eade…` per [5839294562](https://github.com/d6g8k5htny-coder/Math-/pull/19#issuecomment-5839294562).  
**Scientific effect: NONE.** Deterministic finite-r / C6 remainder review only. Not Gaussian density, not theorem acceptance, not #9 pin repair merge.  
**Delivery:** App cannot comment on Math-; this file is the durable review record.

## Method

Independently derived the six midpoint pin identities from the exact constraints

```text
f(-r/2,0)=b,  f(r/2,0)=b-k r^3,
f_x(±r/2,0)=0,  f_z(±r/2,0)=0
```

by one-variable Taylor average/difference at `h=r/2` (do not trust `finite_r_contact.py` for construction). Local python3.12 replay of `run_validation.py` passed both modes (`passed: true`, 21 tests, 3 missing-pin mutants); `SOURCE_FILES.json` SHA-256 matched byte-for-byte. Hosted green replay is eng evidence only.

## Six midpoint identities (independent derivation)

| # | Identity | Disposition |
|---|---|---|
| 1 | `f_x(0)=-(r^2/8) f_xxx(0)+O(r^4)` | **ACCEPT** (avg of `g'(±h)=0`) |
| 2 | `f_xx(0)=-(r^2/24) f_xxxx(0)+O(r^4)` | **ACCEPT** (diff of `g'`) |
| 3 | `f_xxx(0)=12k+O(r^2)` | **ACCEPT** (height difference `-k r^3` + (1)) |
| 4 | `f(0)-b=-(k/2)r^3+O(r^4)` | **ACCEPT** (mean height + (2)) |
| 5 | `f_z(0)=-(r^2/8) f_xxz(0)+O(r^4)` | **ACCEPT** (same avg on `w=f_z(·,0)`) |
| 6 | `f_xz(0)=-(r^2/24) f_xxxz(0)+O(r^4)` | **ACCEPT** (same diff on `w`) |

Derived consequence used below: `f_x(0)/r^2=-3k/2+O(r^2)`.

## Per-interface dispositions (R1–R6 / M1–M7 / S1–S4)

| Item | Disposition | Notes |
|---|---|---|
| **R1** midpoint `f_x`/`f_xx`/`f_xxx` + C6 orders | **ACCEPT** | Matches (1)–(3); M1–M3 constants `1/384`, `1/1920`, `3/80` re-derived; M5 combo `3/640+1/384=7/960` checked. |
| **R2** transverse pin identities | **ACCEPT** | Matches (5)–(6) / M6–M7; same constants as M1–M2 on `w`. |
| **R3** corrected scaled longitudinal/axial rows (`-1/4`) | **ACCEPT** | `f_x(ru,rv)/r^2=6k(u^2-1/4)+q u v+(c/2)v^2+O(r)`; axial `f_z(ru,0)/r^2=(q/2)(u^2-1/4)+O(r)`. Exact cubic witness pins + leading row verified by Fraction algebra. |
| **R4** corrected height residual `H_corr` | **ACCEPT** | `H=k(2u^3-3u/2-1/2)+(q/2)(u^2-1/4)v+(c/2)u v^2+(d/6)v^3` matches expansion of exact witness `(f-b)/r^2`. |
| **R5** uniformity on fixed scaled annuli / square | **ACCEPT** | Square `\|x\|,\|z\|≤B r` (not annulus-only) is the right C6 domain for segments through midpoint/pins; S1–S4 constants arithmetic checked (`\|f_xx\|≤(27/640)M r^2` for `r≤1`; `C_x,C_y,C_ax,C_h` pieces). Rate boundary `(x^2-r^2/4)^2 → 30r` at `u=2` confirms O(r) in S1 is sharp in general. |
| **R6** scope / nonclaims | **ACCEPT** | Correctly refuses Gaussian compensation density, conditional moments, thin-belt/RN_UNIF closure; `mathematical_acceptance: false` in runner; NIST DLMF cited as background only. |
| **M4** midpoint height constant | **ACCEPT** | `(121/15360) M r^4` from `Mh^4(1/8+h^2/240)` at `h≤1/2`. |
| **Oracle / mutants** | **ACCEPT** (eng) | Six-pin rational solve over 22 free deg≤6 monomials; fixtures do not use `corrected()`/`exact_witness()` to build polys; 3 missing-pin mutants assertion-detected. Eng ≠ continuum proof. |

## Explicit non-awards

- Not independent organizational review.
- Not acceptance of Math- [#21](https://github.com/d6g8k5htny-coder/Math-/pull/21)/[#22](https://github.com/d6g8k5htny-coder/Math-/pull/22) density candidates.
- Does not authorize re-fingerprint of [#9](https://github.com/d6g8k5htny-coder/Math-/pull/9)/[#20](https://github.com/d6g8k5htny-coder/Math-/pull/20) while leading pins remain unshifted.
- Tip move past `e93eade…` stales this review.

## Overall

**ACCEPT** on R1–R6 and the quantified M1–M7 / S1–S4 contract at exact head `e93eade078cac2e8b14aa39d402a3043b7cdb1c7` only. No AMEND and no COUNTEREXAMPLE found on the declared deterministic interface.

**Provenance:** governance- branch `cursor/process-packet-scope-ab08`; App write limited to this repository.
