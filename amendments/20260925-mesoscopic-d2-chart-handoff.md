# Handoff sketch — explicit d=2 contact chart for Math- PR7

**Not a Math- publication.** Written from governance- because this App token cannot push `Math-`. Intended for authors of [Math- #7](https://github.com/d6g8k5htny-coder/Math-/pull/7) / a successor PR to verify, correct, and relocate under `frontiers/rn_mesoscopic_20260925/`. Scientific effect: NONE. No Boolean flipped.

**Companion challenge (main):** [RN_MESOSCOPIC_REDUCTION_CHALLENGE_20260925.md](https://github.com/d6g8k5htny-coder/main/blob/cursor/downstream-crosswalk-outside-packet-31c5/docs/RN_MESOSCOPIC_REDUCTION_CHALLENGE_20260925.md) on [main #92](https://github.com/d6g8k5htny-coder/main/pull/92) refuses Lemma A / `γ_AB` until the `J_0`/`det S_r` ledger exists (independence credit 0). This handoff is the constructive next sketch for that challenge’s item 1 (enumerate rows), not a rebuttal.

**Sources used:** fixed-remote `U_0`/`v_0` conventions at `191ea7d…` / Math- tip remote-window proof; mesoscopic reduction `e106ae39…`.

## Contact pins (d=2)

Parent/fixed-remote contact observations at the midpoint 0:

```text
U_0 = (f, f_x, f_xx, f_xxx, f_y, f_xy)_0
v_0 = (b, 0, 0, 12k, 0, 0)
```

Free at contact (independent symmetric jet entries not fixed by `U_0`): notably `f_yy`, `f_xxy`, `f_xyy`, `f_yyy`, and order-4+ terms.

## Taylor residuals at x = r y

Write y=(y1,y2). Under exact `U_0=v_0`, the leading raw residuals are:

```text
∂1 f(ry) = 6k r² y1² + r² (y1 y2 f_xxy + (1/2) y2² f_xyy) + O(r³)
∂2 f(ry) = r y2 f_yy + (r²/2)(y1² f_xxy + 2 y1 y2 f_xyy + y2² f_yyy) + O(r³)
f(ry)-b  = (r²/2) y2² f_yy + 2k r³ y1³ + O(r³·(jet≥3 transverse) + r⁴)
```

(Axial third-derivative Hermite identity used as `f_xxx(0)=12k`; signs follow the remote-window height gap convention.)

## Candidate divided-difference block J_0(y)

On the open set where the scaled pins ±e1/2 are excluded and the chart below is full rank, take

```text
J_0¹(y) := lim r→0  ∂1 f(ry) / r²     = 6k y1² + y1 y2 f_xxy + (1/2) y2² f_xyy
J_0²(y) := lim r→0  ∂2 f(ry) / r      = y2 f_yy
J_0ʰ(y) := lim r→0  (f(ry)-b) / r²    = (1/2) y2² f_yy
```

**Rank observation:** `J_0²` and `J_0ʰ` are linearly dependent through `f_yy` when only these leading terms are kept (`J_0ʰ = (y2/2) J_0²` on `{y2≠0}`). So a height-retained chart must either drop one of `{J_0²,J_0ʰ}` or bring in a higher-order independent height residual (the `2k y1³` term after subtracting `(r²/2) y2² f_yy`, which is O(r) after `/r²` — wait: `(f-b - (r²/2)y2² f_yy)/r³ → 2k y1³ + …`). Correct independent height row after removing the transverse-Hessian piece is order `r³`:

```text
J_0ʰ⊥(y) := lim r→0  ( f(ry)-b - (r/2) y2 · ∂2 f(ry) ) / r³
         = lim r→0  ( f(ry)-b - (r²/2) y2 · (∂2 f(ry)/r) ) / r³
```

which cancels the leading `(r²/2) y2² f_yy` piece. With free jets set to zero the contact limit is `2k y1³`. With free jets retained, order-3 mixed terms appear; **the exact list must be matched to the finite-r transform `S_r`, not only this contact Taylor.**

## What this sketch does and does not settle

Settles enough to answer PR7 challenge (1) partially for d=2: leading powers are `(r², r, r²)` for `(∂1, ∂2, f-b)` before independence cleanup, and height independence likely needs an `r³` row once the `f_yy` piece is removed.

Does **not** settle: exact `det S_r` exponent; Schur complement after conditioning on `U_r`; overlap Jacobians near chart walls; Fourier-covariance positivity of the chosen rows; any Kac–Rice bound.

## Suggested Math- next commit

1. Formalize `S_r(y)` with these leading scalings for one open chart `{|y|∈[A,B], y2≥δ>0, dist(y,±e1/2)≥δ}`.
2. Mutation-test the algebraic expansion (symbolic Taylor vs finite-difference on a jet polynomial).
3. Keep disposition author-side; do not touch `lemma_closed`.
