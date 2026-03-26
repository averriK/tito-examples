## SLOT 1: Extension of the error-minimization formulation to the unit-sum constraint

The weight-calibration problem formulated in the knowledge base casts the determination of GMPE branch weights as a constrained linear regression in log-spectral space [@SpecCompile2026]. The baseline non-negative least-squares (NNLS) formulation minimizes the squared residual between the weighted log-spectral combination and a target vector, subject only to component-wise non-negativity. Denoting by $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times N}$ the log-domain design matrix whose $(i,k)$-th entry is $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$, by $\mathbf{y} \in \mathbb{R}^n$ the log-domain target vector with $y_i = \ln S_a^{\mathrm{obj}}(T_i)$, and by $\mathbf{w} = (w_1, \dots, w_N)^\top$ the weight vector, the NNLS problem takes the form [@SpecCompile2026]:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \dots, N.$$

Incorporating the normalization condition $\sum_{k=1}^{N} w_k = 1$ changes the feasible set from the non-negative orthant $\mathbb{R}_{\geq 0}^N$ to the standard $(N-1)$-dimensional probability simplex [@CornellQP2023]:

$$\Delta^{N-1} = \left\{ \mathbf{w} \in \mathbb{R}^N : \mathbf{1}^\top \mathbf{w} = 1,\; w_k \geq 0 \; \text{for all} \; k \right\}.$$

The simplex $\Delta^{N-1}$ is a closed, bounded, convex polytope of affine dimension $N-1$; its vertices are the standard basis vectors $\mathbf{e}_k$, each corresponding to a degenerate solution that assigns all weight to a single candidate GMPE. The resulting fully constrained least-squares problem is a quadratic program (QP) with one linear equality constraint, $N$ linear inequality constraints, and a strictly convex quadratic objective [@LawsonHanson1995][@HeinzChang2001]:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \mathbf{1}^\top \mathbf{w} = 1, \quad w_k \geq 0, \quad k = 1, \dots, N.$$

In the classification of Lawson and Hanson (1995, Chapter 23), this is an LSEI (least-squares with equality and inequality constraints) problem with the identifications $\mathbf{E}_1 = \tilde{\mathbf{A}}$, $\mathbf{f}_1 = \mathbf{y}$, $\mathbf{E}_2 = \mathbf{1}^\top$, $\mathbf{f}_2 = 1$, $\mathbf{G} = \mathbf{I}_N$, and $\mathbf{h} = \mathbf{0}$ [@LawsonHanson1995]. The identical formulation arises in the remote-sensing literature under the designation *fully constrained least squares* (FCLS), where the simplex-constrained weights represent fractional material abundances [@HeinzChang2001].

The objective $f(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ has Hessian $\mathbf{H} = 2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$, which is positive definite when $\tilde{\mathbf{A}}$ has full column rank, a condition satisfied when the $N$ log-spectral vectors are linearly independent over the period mesh [@SpecCompile2026]. Because the objective is strictly convex and $\Delta^{N-1}$ is non-empty, compact, and convex, the extended problem admits a unique global minimizer $\mathbf{w}^* \in \Delta^{N-1}$ by the Weierstrass extreme-value theorem combined with strict convexity [@BoydEE364a2023].

### First-order optimality conditions

The Lagrangian associates an unrestricted scalar multiplier $\mu \in \mathbb{R}$ with the equality constraint and a non-negative multiplier vector $\boldsymbol{\lambda} \in \mathbb{R}^N_+$ with the component-wise non-negativity constraints [@NocedalWright2006]:

$$\mathcal{L}(\mathbf{w}, \mu, \boldsymbol{\lambda}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \mu\!\left(\mathbf{1}^\top \mathbf{w} - 1\right) - \boldsymbol{\lambda}^\top \mathbf{w}.$$

Because $\Delta^{N-1}$ satisfies Slater's constraint qualification (any interior point such as $\mathbf{w} = \mathbf{1}/N$ is strictly feasible for $N \geq 2$), the Karush-Kuhn-Tucker (KKT) conditions are both necessary and sufficient for global optimality [@TibshiraniKKT2016][@BoydEE364a2023]. Setting $\nabla_{\mathbf{w}} \mathcal{L} = \mathbf{0}$ at the optimal triple $(\mathbf{w}^*, \mu^*, \boldsymbol{\lambda}^*)$ yields the stationarity condition [@NocedalWright2006]:

$$2\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}\right) + \mu^*\mathbf{1} - \boldsymbol{\lambda}^* = \mathbf{0}.$$

The complete KKT system further requires primal feasibility ($\mathbf{1}^\top \mathbf{w}^* = 1$, $\mathbf{w}^* \geq \mathbf{0}$), dual feasibility ($\boldsymbol{\lambda}^* \geq \mathbf{0}$), and complementary slackness ($\lambda_k^* w_k^* = 0$ for all $k$) [@NocedalWright2006].

Defining the passive set $\mathcal{P}^* = \{k : w_k^* > 0\}$ and the zero set $\mathcal{Z}^* = \{k : w_k^* = 0\}$, complementary slackness forces $\lambda_k^* = 0$ for every $k \in \mathcal{P}^*$, reducing the stationarity condition to two sub-conditions [@LawsonHanson1995][@NocedalWright2006]:

$$2\left[\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}\right)\right]_k = -\mu^* \quad \forall\, k \in \mathcal{P}^*, \qquad 2\left[\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}\right)\right]_k \geq -\mu^* \quad \forall\, k \in \mathcal{Z}^*.$$

The scalar $\mu^*$ acts as a uniform shift applied to every component of the gradient residual vector and represents the marginal cost of enforcing unit-sum normalization. Its value is determined jointly by the equality constraint and the partition of $\{1, \dots, N\}$ into positive-weight and zero-weight branches; $\mu^*$ equals zero if and only if the unconstrained NNLS solution $\hat{\mathbf{w}}$ already satisfies $\mathbf{1}^\top\hat{\mathbf{w}} = 1$ [@LawsonHanson1995][@NocedalWright2006].

### Contrast with pure NNLS optimality conditions

The optimality structure of the simplex-constrained QP differs fundamentally from that of the pure NNLS problem. The NNLS KKT conditions require each passive-set gradient component $[\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\hat{\mathbf{w}} - \mathbf{y})]_k$ to vanish identically and each zero-set component to be non-negative [@SpecCompile2026]. In the simplex-constrained QP, passive-set gradient components are not required to vanish; instead they must equal the common, generally non-zero constant $-\mu^*$. The presence of the equality constraint removes one degree of freedom, confining the feasible set to the affine subspace $\mathbf{1}^\top \mathbf{w} = 1$; no further descent is possible along the simplex tangent space at $\mathbf{w}^*$, a condition strictly weaker than the absolute vanishing of each gradient component demanded by NNLS [@SpecCompile2026][@NocedalWright2006].

At the algorithmic level, the equality constraint transforms the sub-problem solved on $\mathcal{P}^*$ during each active-set iteration from a plain unconstrained least-squares problem into an equality-constrained one. Specifically, when $|\mathcal{P}^*| = p$, the sub-problem on $\mathcal{P}^*$ minimizes $\|\tilde{\mathbf{A}}_{\mathcal{P}^*}\mathbf{w}_{\mathcal{P}^*} - \mathbf{y}\|_2^2$ subject to $\mathbf{1}_p^\top \mathbf{w}_{\mathcal{P}^*} = 1$, treated by variable elimination (setting $w_{k^*} = 1 - \sum_{k \in \mathcal{P}^* \setminus \{k^*\}} w_k$) or by an equality-constrained QR factorization [@HaskellHanson1981].

### Algorithmic treatments

Three algorithmic approaches are available for computing $\mathbf{w}^*$.

The LSEI algorithm of Lawson and Hanson (1995, Chapter 23) eliminates the equality constraint by dimensional reduction: substituting $w_N = 1 - \sum_{k=1}^{N-1} w_k$ into the objective converts the unit-sum equality into the bound $\sum_{k=1}^{N-1} w_k \leq 1$ and produces an $(N-1)$-variable NNLS sub-problem solvable by the standard Lawson-Hanson active-set method [@LawsonHanson1995]. In R, the function `pnnls` in the `lsei` package implements a generalization of this approach via Householder orthogonalization, accepting both non-negativity constraints and a unit-sum equality constraint while returning exact zero values for eliminated branches and avoiding numerical precision artifacts associated with general-purpose QP solvers [@LseiPackage2023].

The second approach augments the QP formulation of the knowledge base by appending the equality $\mathbf{1}^\top \mathbf{w} = 1$ to the $N$ non-negativity constraints. In R, `quadprog::solve.QP` accommodates the equality by placing it as the first row of the constraint matrix with `meq = 1`; a small positive-definite ridge perturbation to $\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ is recommended when candidate GMPE log-spectra are nearly collinear [@SpecCompile2026]. The CVXR disciplined convex programming framework accepts the simplex constraint via separate `sum(w) == 1` and `w >= 0` constraint objects, with DCP composition rules verifying convexity automatically and dispatching to solvers such as CLARABEL or OSQP; in the listing below, `K` denotes the number of candidate GMPEs [@SpecCompile2026][@BoydEE364a2023]:

```r
library(CVXR)

K       <- ncol(A_tilde)
w       <- Variable(K)
obj     <- Minimize(sum_squares(A_tilde %*% w - y))
cons    <- list(w >= 0, sum(w) == 1)
prob    <- Problem(obj, cons)
res     <- solve(prob)
w_star  <- as.vector(res$getValue(w))
```

The third approach employs iterative gradient projection onto $\Delta^{N-1}$: at each step the gradient update is projected back onto the simplex using the $O(N \log N)$ sorting-based simplex projection algorithm [@Wang2013], which is efficient for large $N$ and standard in the simplex-constrained least-squares literature.

## SLOT 2: Validity of post-hoc normalization versus direct constrained optimization

The NNLS formulation produces a non-negative weight vector $\hat{\mathbf{w}} \in \mathbb{R}^N_+$
whose component sum $s = \mathbf{1}^\top\hat{\mathbf{w}}$ is determined by the problem data and
the non-negativity constraint alone, with no guarantee that $s = 1$ [@SpecCompile2026]. The
post-hoc normalization strategy forms the rescaled vector $\mathbf{w}^{\mathrm{norm}} =
\hat{\mathbf{w}}/s$, which is feasible for the simplex-constrained problem by construction
($\mathbf{1}^\top\mathbf{w}^{\mathrm{norm}} = 1$, $\mathbf{w}^{\mathrm{norm}} \geq \mathbf{0}$).
The central question is whether $\mathbf{w}^{\mathrm{norm}}$ coincides with the constrained
minimizer $\mathbf{w}^* = \arg\min_{\mathbf{w} \in \Delta^{N-1}} \|\tilde{\mathbf{A}}\mathbf{w} -
\mathbf{y}\|_2^2$ analyzed in SLOT 1.

A rigorous analysis of the optimality conditions of both problems establishes that this equivalence
does not hold in general.

### Non-homogeneity of the objective function

The fundamental obstruction to equivalence is that the squared residual objective
$f(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$ is not positively
homogeneous. Direct algebraic expansion gives:

$$f(\alpha\mathbf{w}) = \alpha^2\|\tilde{\mathbf{A}}\mathbf{w}\|_2^2 -
2\alpha\langle\tilde{\mathbf{A}}\mathbf{w},\, \mathbf{y}\rangle + \|\mathbf{y}\|_2^2.$$

This expression is not proportional to $f(\mathbf{w})$ for any fixed exponent $p$ unless
$\mathbf{y} = \mathbf{0}$: the cross-term $-2\alpha\langle\tilde{\mathbf{A}}\mathbf{w},
\mathbf{y}\rangle$ is linear in $\alpha$, the leading term grows as $\alpha^2$, and the constant
$\|\mathbf{y}\|_2^2$ is scale-independent [@Anonymous2025]. Because $f$ is not homogeneous of
degree zero in $\mathbf{w}$, the NNLS minimizer $\hat{\mathbf{w}}$ over $\mathbb{R}^N_+$ and the
simplex minimizer $\mathbf{w}^*$ over $\Delta^{N-1}$ are governed by qualitatively different
optimization trade-offs: the NNLS problem imposes no constraint on total weight magnitude and
allows the optimizer to freely exploit any scale that reduces prediction error, whereas the simplex
QP fixes the scale and optimizes only the directional allocation of weights.

### Formal proof via KKT conditions

A direct proof of non-equivalence proceeds through the optimality conditions of both problems.
For any index $k$ in the NNLS passive set $\mathcal{P}$ (where $\hat{w}_k > 0$), the NNLS KKT
stationarity condition requires [@SpecCompile2026]:

$$\left[\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\hat{\mathbf{w}} -
\mathbf{y}\right)\right]_k = 0
\quad \Leftrightarrow \quad
\left[\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\hat{\mathbf{w}}\right]_k =
\left[\tilde{\mathbf{A}}^\top\mathbf{y}\right]_k
\quad \forall\, k \in \mathcal{P}.$$

Evaluating the gradient of $f$ at $\mathbf{w}^{\mathrm{norm}} = \hat{\mathbf{w}}/s$ and
substituting the NNLS passive-set condition yields, for all $k \in \mathcal{P}$:

$$\left[\tilde{\mathbf{A}}^\top\!\left(\tilde{\mathbf{A}}\mathbf{w}^{\mathrm{norm}} -
\mathbf{y}\right)\right]_k
= \left(\frac{1}{s} - 1\right)\left[\tilde{\mathbf{A}}^\top\mathbf{y}\right]_k.$$

For $\mathbf{w}^{\mathrm{norm}}$ to satisfy the simplex KKT stationarity condition from SLOT 1,
the quantity $2[\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^{\mathrm{norm}} -
\mathbf{y})]_k$ must equal a single constant $-\mu^{\dagger}$ for all $k \in \mathcal{P}$. When
$s \neq 1$, this requires $[\tilde{\mathbf{A}}^\top\mathbf{y}]_k$ to be identical for every
$k \in \mathcal{P}$ [@NocedalWright2006][@HaskellHanson1981]. The quantity
$[\tilde{\mathbf{A}}^\top\mathbf{y}]_k = \sum_{i=1}^n \tilde{A}_{ik}\, y_i$ measures the inner
product of the $k$-th GMPE log-spectral vector with the log-target; requiring these inner products
to be identical across all positive-weight branches is a non-generic algebraic condition that has
no structural basis in the construction of the design matrix or the seismic hazard target, and
fails for any collection of candidate GMPEs with genuinely distinct log-spectral shapes
[@Anonymous2025][@SpecCompile2026].

A complementary global argument follows from strict convexity. Because $f$ has a unique minimizer
$\mathbf{w}^*$ on $\Delta^{N-1}$, strict convexity implies $f(\mathbf{v}) > f(\mathbf{w}^*)$
for every feasible $\mathbf{v} \neq \mathbf{w}^*$ [@BoydVandenberghe2004]. Since
$\mathbf{w}^{\mathrm{norm}}$ is feasible but generically distinct from $\mathbf{w}^*$, it follows
that $f(\mathbf{w}^{\mathrm{norm}}) > f(\mathbf{w}^*)$: the post-hoc-normalized solution is
strictly sub-optimal relative to the directly constrained solution. No upper bound on this
sub-optimality gap can be established without additional problem-specific information; in principle
the gap can be arbitrarily large.

### Geometric interpretation

The NNLS solution $\hat{\mathbf{w}}$ identifies the closest point in the convex cone
$\mathcal{C} = \{\tilde{\mathbf{A}}\mathbf{v} : \mathbf{v} \geq \mathbf{0}\}$ to the target
$\mathbf{y}$ under the Euclidean metric of $\mathbb{R}^n$. The simplex QP solution $\mathbf{w}^*$
identifies the closest point in the convex hull
$\mathrm{conv}\{\tilde{\mathbf{A}}_{\cdot 1}, \dots, \tilde{\mathbf{A}}_{\cdot N}\}$ to
$\mathbf{y}$, where $\tilde{\mathbf{A}}_{\cdot k}$ is the $k$-th column of $\tilde{\mathbf{A}}$
[@HeinzChang2001]. Post-hoc normalization maps $\hat{\mathbf{w}}$ to $\mathbf{w}^{\mathrm{norm}}$
by radial projection from the origin in weight space toward the hyperplane
$\mathbf{1}^\top\mathbf{w} = 1$. The level sets of $f$ are axis-aligned ellipsoids determined by
the eigenstructure of $\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ and are not spheres centered at
the origin [@SpecCompile2026]; radial projection does not preserve proximity to the least-squares
pre-image of $\mathbf{y}$ in the $f$-metric and does not in general deliver the point on the
simplex that minimizes $f$ [@BoydVandenberghe2004]. The two operations -- radial projection of
$\hat{\mathbf{w}}$ onto $\Delta^{N-1}$ and orthogonal projection of the image
$\tilde{\mathbf{A}}\hat{\mathbf{w}}$ onto the convex hull of GMPE columns -- coincide only when
$\hat{\mathbf{w}}$ already lies in $\Delta^{N-1}$, i.e., when $s = 1$.

### Exact conditions for equivalence

Post-hoc normalization yields $\mathbf{w}^{\mathrm{norm}} = \mathbf{w}^*$ if and only if one of
two conditions holds:

1. $s = \mathbf{1}^\top\hat{\mathbf{w}} = 1$: the NNLS solution already satisfies the unit-sum
   constraint, making normalization an identity operation.
2. $\tilde{\mathbf{A}}^\top\mathbf{y} \propto \mathbf{1}$: all candidate GMPEs have equal inner
   product with the log-target vector, a structural coincidence of zero measure in the space of
   generic problem instances [@HaskellHanson1981].

Neither condition is guaranteed by the problem formulation: the sum $s$ depends on
$(\tilde{\mathbf{A}}, \mathbf{y})$ in a non-trivial way, and the isotropy condition on
$\tilde{\mathbf{A}}^\top\mathbf{y}$ is not enforced by any physical or modelling constraint on
the candidate GMPE set [@Anonymous2025][@SpecCompile2026]. The empirical literature confirms the
practical significance of this non-equivalence: Heinz and Chang (2001) demonstrated that FCLS
consistently achieves lower residuals than NNLS followed by normalization for realistic
hyperspectral design matrices with log-spectral structure analogous to the present application,
confirming that the sub-optimality gap is non-trivial in practice [@HeinzChang2001].

### Conclusion

Post-hoc normalization of NNLS weights does not constitute a mathematically valid substitute for
direct constrained optimization under the unit-sum requirement. The unit-sum equality constraint
introduces the Lagrange multiplier $\mu^*$, which applies a uniform shift to the gradient
optimality conditions across all passive-set components -- an effect that simple rescaling of the
NNLS solution cannot replicate. The minimum log-spectral matching error subject to both
non-negativity and unit-sum is achieved only by solving the simplex-constrained problem directly:
through the modified Lawson-Hanson active-set algorithm (as implemented in `pnnls`), the
equality-constrained QP interface (`quadprog` with `meq = 1` or CVXR with `sum(w) == 1`), or the
gradient projection method described in SLOT 1 [@LseiPackage2023][@SpecCompile2026][@HaskellHanson1981].
Post-hoc normalization may serve as an approximation only when $s$ is sufficiently close to unity,
a condition that is data-dependent and cannot be guaranteed in advance.
