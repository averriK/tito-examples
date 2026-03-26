# Weight Calibration and Sum-to-One Normalization in Epistemic Logic Trees

## SLOT 1: Extend weight calibration formulation for sum-to-one constraint

The weight calibration problem for epistemic logic trees in probabilistic seismic hazard analysis requires that weights form a discrete probability distribution over candidate Ground Motion Prediction Equations (GMPEs). This requirement mandates that the weights sum to unity, formalizing the principle that logic tree branches collectively represent certainty in model selection. [@SpecResearch]

### Foundational Problem Formulation

The weight calibration problem is formulated as a constrained least-squares regression in log-spectral space. The design matrix $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ contains the logarithmic spectral accelerations of $K$ candidate records at $n$ period points, with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$. The target vector $\tilde{\mathbf{y}} \in \mathbb{R}^n$ contains the log-domain target spectral ordinates $\tilde{y}_i = \ln S_a^{\mathrm{obj}}(T_i)$. The weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ must satisfy all specified constraints. The log-log formulation provides improved homoscedasticity and alignment with PSHA conventions, where $\ln S_a(T)$ is modeled as normally distributed. [@SpecResearch]

### Complete Mathematical Formulation with Sum-to-One Constraint

The extended formulation incorporates the sum-to-one normalization constraint alongside non-negativity and, optionally, upper-bound constraints on individual weights:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2$$

subject to the constraints:

$$\sum_{k=1}^{K} w_k = 1,$$

$$w_k \geq 0 \quad \text{for all} \quad k = 1, \dots, K,$$

$$w_k \leq w_{\max} \quad \text{for all} \quad k = 1, \dots, K \quad \text{(optional)}.$$

The objective function measures prediction error as the squared $\ell_2$ norm of residuals in log-spectral units. The equality constraint $\sum_{k=1}^{K} w_k = 1$ enforces that the weights form a convex combination, essential for representing a discrete probability distribution over candidate GMPEs. [@SpecResearch]

### Constraint Set Structure and Convexity

The feasible region defined by these constraints is a polytope: the intersection of one equality constraint (sum-to-one), $K$ non-negativity constraints, and $K$ optional upper-bound constraints. When only non-negativity and sum-to-one constraints are present, the feasible region is a standard probability simplex $\Delta_K = \{\mathbf{w} \in \mathbb{R}^K : \sum w_k = 1, w_k \geq 0\}$. When upper bounds are imposed, the feasible region becomes a subset of the simplex.

The objective function is a strictly convex quadratic function in $\mathbf{w}$ with Hessian matrix $\mathbf{H} = 2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$. The Hessian is positive semidefinite and positive definite when $\tilde{\mathbf{A}}$ has full column rank (equivalently, when the candidate spectral shapes are linearly independent over the period mesh). The convexity of the objective function combined with the convexity of the feasible set (a compact polytope) guarantees the existence and uniqueness of a global minimizer. [@SpecResearch]

### Lagrangian Formulation and KKT Conditions

The problem can be reformulated as a standard quadratic program (QP) by introducing the Lagrangian. Define the equality constraint matrix $\mathbf{C}_{\text{eq}} = \mathbf{1}^\top \in \mathbb{R}^{1 \times K}$ (a row vector of ones) and the equality constraint right-hand side $\mathbf{d}_{\text{eq}} = 1$. The non-negativity constraints are encoded as $-\mathbf{w} \leq \mathbf{0}$, and optional upper-bound constraints as $\mathbf{w} \leq w_{\max} \mathbf{1}$.

The standard QP form is:

$$\mathbf{w}^* = \arg\min_{\mathbf{w}} \frac{1}{2} \mathbf{w}^\top \mathbf{H} \mathbf{w} + \mathbf{c}^\top \mathbf{w},$$

where $\mathbf{H} = 2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ is the Hessian and $\mathbf{c} = -2\tilde{\mathbf{A}}^\top\tilde{\mathbf{y}}$ is the linear coefficient vector. The constraints are:

$$\mathbf{C}_{\text{eq}} \mathbf{w} = \mathbf{d}_{\text{eq}}, \quad \mathbf{G}_{\text{ineq}} \mathbf{w} \leq \mathbf{h}_{\text{ineq}},$$

where $\mathbf{G}_{\text{ineq}}$ encodes the non-negativity and optional upper-bound constraints. [@SpecResearch]

The Lagrangian is:

$$\mathcal{L}(\mathbf{w}, \lambda, \boldsymbol{\mu}) = \frac{1}{2} \mathbf{w}^\top \mathbf{H} \mathbf{w} + \mathbf{c}^\top \mathbf{w} - \lambda (\mathbf{C}_{\text{eq}} \mathbf{w} - \mathbf{d}_{\text{eq}}) - \boldsymbol{\mu}^\top (\mathbf{G}_{\text{ineq}} \mathbf{w} - \mathbf{h}_{\text{ineq}}),$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier for the equality constraint and $\boldsymbol{\mu}$ is the vector of multipliers for the inequality constraints. The Karush-Kuhn-Tucker (KKT) conditions for optimality require:

$$\nabla_{\mathbf{w}} \mathcal{L} = \mathbf{H} \mathbf{w}^* + \mathbf{c} - \lambda^* \mathbf{C}_{\text{eq}}^\top - \mathbf{G}_{\text{ineq}}^\top \boldsymbol{\mu}^* = \mathbf{0},$$

$$\mathbf{C}_{\text{eq}} \mathbf{w}^* = \mathbf{d}_{\text{eq}},$$

$$\mathbf{G}_{\text{ineq}} \mathbf{w}^* \leq \mathbf{h}_{\text{ineq}},$$

$$\boldsymbol{\mu}^* \geq \mathbf{0}, \quad \boldsymbol{\mu}^* \odot (\mathbf{G}_{\text{ineq}} \mathbf{w}^* - \mathbf{h}_{\text{ineq}}) = \mathbf{0}.$$

The complementarity condition (the final line) states that at optimality, each inequality constraint is either active (with a positive multiplier, binding at the solution) or inactive (with a zero multiplier). [@SpecResearch]

### Solution Methods

Standard convex optimization algorithms can solve this problem effectively: active-set methods (which maintain and update sets of active inequality constraints), interior-point methods (which traverse the interior of the feasible region), or second-order cone programming (SOCP) solvers. For moderate problem sizes typical in GMPE logic tree applications ($K$ often between 3 and 20 and $n$ between 50 and 100 ordinates), active-set algorithms such as those in specialized QP solvers provide reliable and numerically stable solutions with fast convergence. [@SpecResearch]

In R, the quadprog package provides the `solve.QP` function, which solves problems of the form:

$$\min \frac{1}{2} \mathbf{w}^\top \mathbf{D} \mathbf{w} - \mathbf{d}^\top \mathbf{w}$$

subject to $\mathbf{A} \mathbf{w} \geq \mathbf{b}$. To enforce the sum-to-one constraint using `quadprog`, the equality $\sum w_k = 1$ can be replaced by two inequality constraints: $\sum w_k \geq 1$ and $-\sum w_k \geq -1$, or equality constraint handling can be integrated through matrix augmentation. Alternatively, the general convex-optimization frameworks (such as CVXR in R or CVXPy in Python) permit direct specification of equality constraints in disciplined convex programming (DCP) syntax. [@SpecResearch]

### Differentiation from Prior Formulations

This sum-to-one constrained formulation represents a material departure from the unconstrained OLS and NNLS formulations in the knowledge base. The unconstrained OLS solution admits negative weights and is unbounded above, unsuitable for probability distributions. The non-negative least-squares (NNLS) formulation enforces non-negativity but does not constrain the sum of weights, permitting weights to grow without upper limit. The bounded-variable least-squares (BVLS) formulation introduces two-sided bounds on individual weights but does not enforce the sum-to-one requirement. The extended formulation presented here combines non-negativity (or non-negativity with upper bounds) with the fundamental probabilistic requirement that weights form a normalized distribution. [@SpecResearch]

### Interpretation and Practical Significance

The sum-to-one constraint ensures that the fitted weights can be directly interpreted as branch probabilities in epistemic logic trees. This is not merely a normalization artifact but a fundamental requirement for consistent PSHA computation. The weighted average hazard curve is constructed as $\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k \lambda_I^{(k)}(i^*)$, where the weighting scheme must represent a valid discrete probability distribution. The constraint transforms the unconstrained formulation from $K$ degrees of freedom to $N-1$ effective degrees of freedom, since once $N-1$ weights are specified, the final weight is determined by the constraint.

---

## SLOT 2: Validate normalization approach and justify mathematical treatment

A critical practical question arises when implementing weight calibration: is it mathematically valid to compute weights from an unconstrained or partially constrained optimization problem and then post-hoc normalize them by dividing by their sum, or must the sum-to-one constraint be enforced directly during optimization?

### Post-Hoc Normalization Does Not Preserve Optimality

The fundamental issue is that post-hoc normalization does not satisfy the optimality conditions of the constrained problem. Consider the unconstrained OLS solution $\hat{\mathbf{w}}_0$, obtained by minimizing $f(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2$ over all $\mathbf{w} \in \mathbb{R}^K$. Post-hoc normalization divides each component by the sum to produce $\hat{\mathbf{w}}_{\mathrm{norm}} = \hat{\mathbf{w}}_0 / \sum_{k=1}^{K} \hat{w}_{0,k}$. This normalized vector satisfies $\sum_{k=1}^{K} \hat{w}_{\mathrm{norm},k} = 1$ by construction. However, in general, $\hat{\mathbf{w}}_{\mathrm{norm}}$ does not minimize the original objective subject to the sum-to-one constraint. [@SpecResearch]

To establish this rigorously, consider the Lagrangian of the sum-to-one constrained problem:

$$\mathcal{L}(\mathbf{w}, \lambda) = \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2 + \lambda \left(\sum_{k=1}^{K} w_k - 1\right),$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier for the equality constraint. The Karush-Kuhn-Tucker (KKT) first-order necessary conditions for optimality require:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \tilde{\mathbf{y}}) + \lambda^* \mathbf{1} = \mathbf{0}, \quad \sum_{k=1}^{K} w_k^* = 1,$$

where $\mathbf{1} = (1, 1, \dots, 1)^\top$. These conditions imply that the gradient of the Lagrangian with respect to $\mathbf{w}$ is proportional to $\mathbf{1}$: all components of the gradient are equal at optimality. [@SpecResearch]

In contrast, the unconstrained OLS solution $\hat{\mathbf{w}}_0$ satisfies:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\hat{\mathbf{w}}_0 - \tilde{\mathbf{y}}) = \mathbf{0},$$

so the gradient is zero at every component. When $\hat{\mathbf{w}}_0$ is normalized to $\hat{\mathbf{w}}_{\mathrm{norm}}$, the gradient vector becomes:

$$\nabla_{\mathbf{w}} \left\|\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\mathrm{norm}} - \tilde{\mathbf{y}}\right\|_2^2 = 2\tilde{\mathbf{A}}^\top\left(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\mathrm{norm}} - \tilde{\mathbf{y}}\right).$$

This gradient is generally not proportional to $\mathbf{1}$, and the normalized weights do not satisfy the KKT conditions for the constrained problem. Therefore, in general, post-hoc normalization of an unconstrained solution does not yield the constrained optimum. [@SpecResearch]

### Objective Function Homogeneity and Scale Invariance

The fundamental reason for this inequivalence lies in the homogeneity properties of the objective function. The objective function $f(\mathbf{w}) = \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2$ is not homogeneous of any degree because of the constant term $-\tilde{\mathbf{y}}$, which does not scale with the weights. A homogeneous function of degree $d$ must satisfy $f(c \mathbf{w}) = c^d f(\mathbf{w})$ for all $c > 0$. Since the target vector $\tilde{\mathbf{y}}$ is fixed and independent of the weight scaling, this property fails. [@SpecResearch]

Consider a scaled weight vector $\mathbf{w}' = c \hat{\mathbf{w}}_{\mathrm{NNLS}}$ for some positive scalar $c$. The objective function value becomes:

$$f(\mathbf{w}') = \|c(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\mathrm{NNLS}}) - \tilde{\mathbf{y}}\|_2^2 = \|c(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\mathrm{NNLS}}) - \tilde{\mathbf{y}}\|_2^2.$$

The scaled prediction $c(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\mathrm{NNLS}})$ moves farther from the target $\tilde{\mathbf{y}}$ unless $c = 1$. The function $f$ is not scale-invariant: scaling all weights changes the predicted spectral values, and the residual vector is not invariant to this scaling unless the design matrix has special structure (which is not assumed in general). [@SpecResearch]

### Empirical Consequence: Suboptimality of Normalized Solutions

In practical computation, normalizing an unconstrained solution yields a worse (larger) objective value than solving the constrained problem directly. Denote the unconstrained optimum as $\hat{\mathbf{w}}_{\mathrm{unc}} = \arg\min_{\mathbf{w}} f(\mathbf{w})$, and let $\hat{\mathbf{w}}_{\mathrm{norm}} = \hat{\mathbf{w}}_{\mathrm{unc}} / \|\hat{\mathbf{w}}_{\mathrm{unc}}\|_1$ be its normalization to the simplex. The constrained optimum is $\hat{\mathbf{w}}_{\mathrm{const}} = \arg\min_{\mathbf{w} \in \Delta_K} f(\mathbf{w})$.

In general, $f(\hat{\mathbf{w}}_{\mathrm{norm}}) > f(\hat{\mathbf{w}}_{\mathrm{const}})$ because the unconstrained minimum lies outside the simplex (in the unconstrained space $\mathbb{R}^K$), and normalizing it projects the unconstrained solution onto the feasible set in a way that increases the objective value. This is a foundational principle of constrained optimization: the constrained minimum must have a smaller or equal objective value than any feasible point. Since the unconstrained optimum is outside the feasible region, any projection of it onto the feasible region yields a point with worse objective value than the constrained optimum. [@SpecResearch]

To illustrate with a concrete example, consider $K = 2$ records and $n = 1$ period point. The design matrix is $\tilde{\mathbf{A}} = [a_1, a_2]$ (a row vector), and the target is $\tilde{y}$. The unconstrained OLS solution minimizes $f(w_1, w_2) = (a_1 w_1 + a_2 w_2 - \tilde{y})^2$, yielding the condition $a_1 w_1 + a_2 w_2 = \tilde{y}$ (a line in $(w_1, w_2)$-space). If both coefficients are nonzero, the unconstrained problem has infinitely many solutions. Any point on this line can be normalized to lie on the sum-to-one simplex $w_1 + w_2 = 1$. The constrained problem selects a unique point on the simplex that also satisfies the error minimization criterion. Post-hoc normalization of an arbitrary unconstrained solution will not yield the constrained optimum unless special alignment conditions hold. [@SpecResearch]

### Analysis of NNLS Post-Hoc Normalization

A similar argument applies to non-negative least-squares (NNLS) post-hoc normalization. The NNLS solution $\hat{\mathbf{w}}_{\geq 0}$ minimizes $\|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2$ subject to $w_k \geq 0$. If this solution is normalized to produce $\tilde{\mathbf{w}} = \hat{\mathbf{w}}_{\geq 0} / \sum_k \hat{w}_k^{\geq 0}$, the normalized weights satisfy $\sum_k \tilde{w}_k = 1$ and $\tilde{w}_k \geq 0$, but they do not minimize the objective among all weights satisfying both constraints. [@SpecResearch]

The KKT stationarity condition for the NNLS-plus-normalization problem is:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \tilde{\mathbf{y}}) + \nu \mathbf{1} + \boldsymbol{\mu} = \mathbf{0},$$

where $\nu$ is the multiplier for the equality constraint and $\boldsymbol{\mu}$ is the vector of multipliers for $w_k \geq 0$. Normalizing the NNLS solution does not satisfy this condition in general, so the normalized weights are suboptimal. [@SpecResearch]

### Conditions for Approximate Validity

Post-hoc normalization can be approximately valid under specific restrictive conditions. If the unconstrained optimum $\hat{\mathbf{w}}_0$ happens to satisfy $\sum_{k=1}^{K} \hat{w}_{0,k} = 1$ already, then normalization is a null operation and the solution is trivially optimal. This occurs when the data matrix and target have special symmetries or when the problem is formulated in specific coordinates.

More generally, if the unconstrained solution lies within a small neighborhood of the simplex (with $|\sum_k \hat{w}_k - 1| \ll 1$), then the scaling by $1/s$ is a small perturbation and post-hoc normalization approximates the constrained solution. This scenario arises when the design matrix is well-conditioned and the target is achievable or near-achievable by a linear combination of spectral ordinates. However, this approximate validity requires careful verification in each application and does not eliminate the optimality gap. When unconstrained weights deviate significantly from unit sum (for example, when the candidate spectrum set spans a large range of scales or when the target spectrum is far from the convex hull of candidate spectra), the approximation breaks down and direct constrained optimization is essential. [@SpecResearch]

### Correct Approach: Direct Constrained Optimization

To obtain weights that sum to one while minimizing prediction error, the constrained problem must be solved directly using methods suited to simplex constraints. Algorithm options include:

1. **Active-set methods adapted for simplex constraints**, in which the algorithm iteratively identifies which weights are zero and which are positive, then solves an unconstrained OLS sub-problem on the positive-weight subset while enforcing the sum-to-one constraint on those components only.

2. **Interior-point methods** (barrier or primal-dual), which treat the simplex as a smooth manifold and follow a central path to the optimum, respecting the constraint throughout.

3. **Quadratic programming solvers** for the case without regularization penalties (e.g., using CVXR with CLARABEL or SCS, or dedicated QP solvers like `quadprog` in R).

4. **Projected gradient or Frank-Wolfe methods**, which iteratively move within the simplex by projecting gradient steps onto the feasible region.

These algorithms guarantee that the resulting weights $\hat{\mathbf{w}}_{\mathrm{const}}$ satisfy the sum-to-one constraint exactly and minimize the objective over all feasible points. [@SpecResearch]

### Summary and Recommendation

Post-hoc normalization of an unconstrained or partially constrained solution is not mathematically equivalent to solving the constrained problem directly. The squared-error objective is scale-dependent, the constrained and post-hoc approaches satisfy fundamentally different optimality conditions (different KKT conditions), and the normalized solution is generally suboptimal in terms of the original objective function. The validity of post-hoc normalization hinges on a key mathematical distinction: normalization does not preserve optimality of the original unconstrained or partially constrained solution when viewed as a solution to the fully constrained problem. Normalization does preserve the property that resulting weights form a convex combination and are non-negative. If the goal is merely to ensure weights are convex-combined non-negative values that approximate a target without requiring optimality with respect to the weighted-error objective, normalization is valid. But if the goal is to obtain the solution that minimizes prediction error subject to all constraints simultaneously, one must solve the constrained problem directly.

For weight calibration in epistemic logic trees representing seismic hazard, direct constrained optimization is the mathematically rigorous approach. The computational overhead of adding the sum-to-one constraint is negligible; modern QP solvers integrate the constraint handling seamlessly into the optimization procedure. Post-hoc normalization may be used as a computational shortcut only if the deviation in objective value is acceptable for the intended application, and this deviation must be quantified and reported.

---

## References

