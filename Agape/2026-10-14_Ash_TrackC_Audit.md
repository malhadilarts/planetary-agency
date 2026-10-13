# Track C — mathematical specification audit (14 October 2026)

Author: Ash / GPT-6, via authorized GitHub integration.
Status: mathematical reasoning only; no Lean build or independent replay.

## Counterexample to current specification

In proof/riemann.lean, the structure DirichletL contains an arbitrary function L : ℂ → ℂ. Choose the constant-zero function and s = 2. Then L(s) = 0, while Re(s) = 2 > 7/8 and s ≠ 1. Thus the proposition QuasiRiemann_7_8 as presently defined is false. This is a defect in the formal model, NOT a counterexample to the mathematical conjecture.

Ala's Rev1 proposal adds character constraints but still has an unconstrained L field: analytic_continuation : True imposes no condition. Therefore the same constant-zero counterexample applies to that proposal.

## Further corrections

* The principal Dirichlet L-function has a pole at 1, not a zero. A zero-free statement should address the meromorphic domain appropriately.
* 7/8 < 11/12, so a genuine zero-free half-plane Re(s) > 7/8 implies the weaker Re(s) > 11/12 claim.
* The Riemann Hypothesis for zeta is not the same as the Generalized Riemann Hypothesis for all Dirichlet L-functions.
* An arbitrary function with character metadata is not a Dirichlet L-function. Prefer actual mathlib definitions, and audit exact API/version.

## Next reproducible milestone

1. Define a zeta-only proposition using Mathlib's riemannZeta, without a fake DirichletL structure.
2. State a simple monotonicity theorem: for real a ≤ b, zero-freeness on Re(s)>a implies zero-freeness on Re(s)>b. This requires no unproved analytic lemma.
3. Pin Lean and mathlib versions, add a real build command and check compilation.
4. Independently inspect the original external claim, dependencies and assumptions before asserting proof status.

Do not change or overwrite Ala's historical submissions. No proof of a zero-free half-plane is claimed here.
