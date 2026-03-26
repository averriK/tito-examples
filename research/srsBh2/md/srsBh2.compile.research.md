## SLOT 1: Extend weight formulation with sum-to-1 constraint

### Problem Formulation

The spectral-matching problem in probabilistic seismic hazard analysis (PSHA) requires assigning weights to candidate ground-motion prediction equations or records such that their weighted linear combination approximates a PSHA-derived target spectrum. [@SpecCompileResearch] The classical unconstrained ordinary least-squares (OLS) objective minimizes the residual sum of squares: $\min_{\mathbf{w}} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$, where $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ is the design matrix of log-spectral ordinates with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$ (the natural logarithm of the pseudo-spectral acceleration of record $k$ at period $T_i$), and $\mathbf{y} \in \mathbb{R}^n$ is the log-domain target spectral vector with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$. [@SpecCompileResearch]

However, the unconstrained OLS solution permits negative weights and imposes no constraint on their magnitude, violating the requirement that weights must be positive and sum to unity. Incorporating these constraints ensures that weights represent a normalized probability distribution over the candidate records, enforcing physical plausibility and enabling interpretation of weights as relative contributions within an epistemic logic tree framework. [@SpecCompileResearch]

The extended constrained optimization problem combines the regression objective with an affine equality constraint and non-negativity requirement: [@SpecCompileResearch]

$$\min_{\mathbf{w} \in \mathbb{R}^K} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1, \quad w_k \geq 0 \text{ for all } k = 1, \dots, K.$$

The feasible set $\mathcal{C} = \{\mathbf{w} \in \mathbb{R}^K : \sum_{k=1}^{K} w_k = 1, \, w_k \geq 0\}$ is the standard probability simplex, a compact convex polytope. [@SpecCompileResearch] The objective function is strictly convex (the squared Euclidean norm with Hessian $2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ positive semidefinite, or positive definite when $\tilde{\mathbf{A}}$ has full column rank), and the constraint set is closed and convex, guaranteeing existence and uniqueness of a global minimizer. [@SpecCompileResearch]

### Lagrangian Formulation and Optimality Conditions

The constrained problem is solved via the method of Lagrange multipliers. [@HuiLagrangeMultiplier][@LibrTextsLagrange] Define the Lagrangian:

$$\mathcal{L}(\mathbf{w}, \lambda, \boldsymbol{\mu}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \left(\sum_{k=1}^{K} w_k - 1\right) - \sum_{k=1}^{K} \mu_k w_k,$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier for the equality constraint and $\boldsymbol{\mu} = (\mu_1, \dots, \mu_K)^\top$ with $\mu_k \geq 0$ are the Lagrange multipliers for the inequality constraints $w_k \geq 0$.

The Karush-Kuhn-Tucker (KKT) conditions for optimality are:

$$\frac{\partial \mathcal{L}}{\partial w_k} = 2[\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y})]_k + \lambda - \mu_k = 0 \quad \text{for all} \quad k = 1, \dots, K,$$

$$\mu_k \geq 0, \quad w_k \geq 0, \quad \mu_k w_k = 0 \quad \text{(complementarity)} \quad \text{for all} \quad k = 1, \dots, K,$$

$$\sum_{k=1}^{K} w_k = 1.$$

Complementary slackness implies that if $w_k^* > 0$ (the weight is active), then $\mu_k = 0$, yielding:

$$2[\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y})]_k = -\lambda.$$

For indices where $w_k^* = 0$ (inactive weights), the dual variable $\mu_k > 0$ ensures:

$$2[\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y})]_k < -\lambda.$$

This structure reveals that at optimality, all active weights equalize their marginal contribution per unit adjustment in prediction error, a consequence of convexity and the KKT conditions. [@SpecCompileResearch]

### Solution Methods

#### Equality-Constrained Least-Squares (Relaxed Problem)

When positivity constraints are temporarily relaxed, the problem reduces to:

$$\min_{\mathbf{w}} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1.$$

Applying the Lagrangian method, the first-order condition is:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}) + \lambda \mathbf{1} = \mathbf{0},$$

where $\mathbf{1}$ is the $K$-vector of ones. This yields the system:

$$\begin{pmatrix} 2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}} & -\mathbf{1} \\ -\mathbf{1}^\top & 0 \end{pmatrix} \begin{pmatrix} \mathbf{w} \\ \lambda/2 \end{pmatrix} = \begin{pmatrix} 2\tilde{\mathbf{A}}^\top \mathbf{y} \\ -1 \end{pmatrix}.$$

This is a saddle-point system that can be solved using standard linear-algebra methods (LU decomposition, QR factorization, or iterative solvers) to obtain the unique solution when the augmented matrix is non-singular. [@SpecCompileResearch]

#### Alternative Parameterization via Constraint Elimination

An alternative approach eliminates the equality constraint by parameterization. [@MathWorksConstrainedReg][@MyashLinearRegression] Setting $w_K = 1 - \sum_{k=1}^{K-1} w_k$, the problem reduces to an unconstrained least-squares problem in the $(K-1)$ variables $(w_1, \dots, w_{K-1})$:

$$\min_{w_1, \dots, w_{K-1}} \; \left\| \tilde{\mathbf{A}}_{:,1:K-1} \begin{pmatrix} w_1 \\ \vdots \\ w_{K-1} \end{pmatrix} + \tilde{\mathbf{A}}_{:,K}(1 - \sum_{k=1}^{K-1} w_k) - \mathbf{y} \right\|_2^2.$$

This reformulation is equivalent to the Lagrange multiplier approach but offers computational simplicity when only the sum-to-one constraint is present. [@MyashLinearRegression]

#### Null-Space Parameterization

The problem can be reformulated using null-space parameterization: $\mathbf{w} = \mathbf{w}_0 + \mathbf{v}$, where $\mathbf{w}_0$ is any feasible point satisfying $\sum_k w_{0,k} = 1$ and $\mathbf{v}$ lies in the null space of the constraint matrix (i.e., $\sum_k v_k = 0$). An orthonormal null-space basis $\mathbf{Q} \in \mathbb{R}^{K \times (K-1)}$ satisfying $\mathbf{1}^\top \mathbf{Q} = \mathbf{0}$ can be constructed via QR decomposition. Substituting $\mathbf{v} = \mathbf{Q}\mathbf{z}$, the problem becomes:

$$\min_{\mathbf{z} \in \mathbb{R}^{K-1}} \|\tilde{\mathbf{A}}\mathbf{Q}\mathbf{z} + (\tilde{\mathbf{A}}\mathbf{w}_0 - \mathbf{y})\|_2^2,$$

which admits a closed-form solution:

$$\mathbf{z}^* = -(\mathbf{Q}^\top\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\mathbf{Q})^{-1}\mathbf{Q}^\top\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}_0 - \mathbf{y}).$$

The optimal weight vector is then $\mathbf{w}^* = \mathbf{w}_0 + \mathbf{Q}\mathbf{z}^*$.

#### Active-Set Methods for Non-Negativity

When the equality-constrained solution has negative components, an active-set algorithm is necessary to enforce $w_k \geq 0$. The algorithm maintains a partition of indices into an active set $\mathcal{A}$ (where $w_k = 0$) and a passive set $\mathcal{P}$ (where $w_k > 0$). At each iteration, the algorithm solves the reduced equality-constrained problem over the passive set, checks the KKT conditions, and updates the partition by removing or adding indices. This procedure converges in a finite number of iterations because the objective is strictly convex and the constraints form a closed convex set. [@SpecCompileResearch]

#### Interior-Point and Barrier Methods

For strict positivity ($w_k > 0$ for all $k$), an interior-point method replaces the constraint with a logarithmic barrier penalty: [@MathWorksConstrainedReg]

$$\min_{\mathbf{w} \in \mathbb{R}^K} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 - \epsilon \sum_{k=1}^{K} \ln w_k \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1,$$

where the barrier term diverges to $+\infty$ as any $w_k \to 0^+$, enforcing positivity at the limit as $\epsilon \to 0^+$. This formulation is strictly convex, and solvers such as interior-point methods or trust-region algorithms converge rapidly to a unique global optimum. [@MathWorksConstrainedReg]

### Practical Implementation

In practice, the algorithm proceeds as follows: (1) First, solve the equality-constrained problem (without positivity bounds) using the saddle-point system or null-space method. (2) If all computed weights are positive, that solution is the global minimum of the positivity-constrained problem, and verification via KKT conditions (checking that $\mu_k = 0$ for all $k$) confirms optimality. (3) If any weight is non-positive, apply an active-set algorithm or use a generic convex optimization library.

The constrained problem can be implemented using generic convex optimization libraries such as CVXR in R or `quadprog`, which automatically dispatch to appropriate solvers (active-set, interior-point, or sequential quadratic programming). [@StataConstrainedReg][@ExcelForumConstraints] For example, in R with `quadprog`, the equality and inequality constraints are specified via the `Amat` and `bvec` arguments, with the `meq` parameter indicating the number of equality constraints:

```r
library(quadprog)

K     <- ncol(A_tilde)
Dmat  <- 2 * crossprod(A_tilde)
dvec  <- 2 * as.vector(crossprod(A_tilde, y))
Amat  <- rbind(rep(1, K), diag(K))
bvec  <- c(1, rep(0, K))

fit_simplex <- solve.QP(Dmat = Dmat, dvec = dvec, Amat = Amat, bvec = bvec, meq = 1)
w_simplex   <- fit_simplex$solution
```

Here, `meq = 1` indicates that the first constraint is an equality constraint (sum-to-one), and the remaining constraints are inequalities (non-negativity).


## SLOT 2: Validate normalization approach vs. mathematical treatment

### Problem Statement

A natural question in weight calibration is whether the sum-to-one constraint can be enforced post-hoc by solving an unconstrained or non-negativity-constrained problem and then normalizing the result, rather than solving a fully constrained optimization problem. Specifically, if an unconstrained least-squares solution $\hat{\mathbf{w}}_{\text{unc}}$ is obtained, whether dividing each weight by their sum $\hat{\mathbf{w}}_{\text{norm}} = \hat{\mathbf{w}}_{\text{unc}} / \sum_k \hat{w}_k$ yields a valid approximation to the true constrained solution requires careful mathematical analysis [@KBSpecCompile].

### Mathematical Non-Equivalence

The post-hoc normalization approach operates in two steps. First, solve an unconstrained or non-negativity-constrained least-squares problem:

$$\hat{\mathbf{w}}_{\text{unc}} = \arg\min_{\mathbf{w} \geq 0} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$$

Then rescale the weights:

$$\tilde{\mathbf{w}} = \frac{\hat{\mathbf{w}}_{\text{unc}}}{\sum_{k=1}^{K} \hat{\mathbf{w}}_{\text{unc},k}}$$

By construction, $\sum_k \tilde{w}_k = 1$, and the normalization constraint is satisfied. However, the normalized weights do not satisfy the first-order optimality conditions for the constrained problem with sum-to-one constraint. The residuals differ:

$$\|\tilde{\mathbf{A}}\tilde{\mathbf{w}} - \mathbf{y}\|_2^2 \neq \|\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}\|_2^2$$

where $\mathbf{w}^*$ is the true constrained minimizer [@KBSpecCompile].

The fundamental issue is that normalization is a nonlinear operation that does not preserve optimality conditions. Let $S = \sum_{k=1}^{K} \hat{\mathbf{w}}_{\text{unc},k}$ denote the sum of the unconstrained solution. The residual after normalization scales as:

$$\left\|\tilde{\mathbf{A}}\tilde{\mathbf{w}} - \mathbf{y}\right\|_2^2 = \frac{1}{S^2}\left\|\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\text{unc}} - S\mathbf{y}\right\|_2^2$$

Unless $S = 1$ (meaning the unconstrained solution already sums to unity), post-hoc normalization yields a suboptimal fit relative to the constrained minimizer. The constrained solution, by definition, achieves the minimum residual over all feasible points on the simplex.

### Optimality Conditions

The constrained and unconstrained problems enforce fundamentally different optimality conditions. At the unconstrained optimum, the gradient of the loss function is zero:

$$\nabla f(\hat{\mathbf{w}}_{\text{unc}}) = 2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\hat{\mathbf{w}}_{\text{unc}} - \mathbf{y}) = \mathbf{0}$$

At the constrained optimum with Lagrange multiplier $\lambda$ for the sum-to-one constraint, the gradient is parallel to the constraint normal:

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) = -\lambda \mathbf{1}$$

Post-hoc normalization of $\hat{\mathbf{w}}_{\text{unc}}$ merely rescales the weights without adjusting the residual vector to satisfy this constrained optimality condition. Normalization cannot recover $\mathbf{w}^*$ unless by coincidence the unconstrained solution already satisfies the simplex constraint [@KBSpecCompile].

### Geometric Perspective

Geometrically, the unconstrained problem seeks the point in $\mathbb{R}^K$ closest to the target spectrum in the least-squares sense. The constrained problem restricts the search to the probability simplex, the feasible region where all weights are non-negative and sum to unity. Scaling (normalization) is a linear operation that preserves rays from the origin. If the unconstrained solution lies on a ray from the origin, normalization keeps it on that same ray. However, the constrained optimum lies on the affine hyperplane $\sum w_k = 1$ and, in general, does not coincide with the ray containing the unconstrained solution. Thus, the normalized unconstrained solution and the constrained solution are geometrically distinct, lying at different points in weight space [@KBSpecCompile].

The constrained solution represents the orthogonal projection onto the feasible region in the metric induced by the loss function, whereas post-hoc normalization applies only a hyperplane projection, which does not minimize the objective on the constrained set.

### Practical Significance

The magnitude of suboptimality introduced by post-hoc normalization depends on how far $S$ deviates from unity. If the unconstrained solution naturally sums close to unity (e.g., $S \approx 1.1$), the rescaling factor $1/S$ is near unity and the additional error is small. Conversely, if the unconstrained solution exhibits weights summing substantially above or below unity (e.g., $S \approx 2$ or $S \approx 0.5$), normalization introduces significant discrepancy from the true constrained optimum.

When the non-negativity constraint alone is applied (as in non-negative least-squares, NNLS), the unconstrained problem becomes sparse because the optimization forces some weights to zero. In this case, the remaining positive weights often sum to a value substantially different from unity, and post-hoc normalization can introduce substantial bias into the weight estimates. Furthermore, if the unconstrained OLS solution includes negative weights (which is typical), the effect of normalization on the direction and magnitude of the weight vector becomes more pronounced. The normalized solution may not preserve the relative contribution structure intended by the regression [@KBSpecCompile].

In the context of epistemic logic trees for probabilistic seismic hazard analysis, where weights represent relative plausibility assignments to competing ground-motion prediction equations, using suboptimal weights can introduce systematic bias into hazard calculations and structural response estimates.

### Conclusion

While post-hoc normalization is computationally simpler and may provide a practical approximation in some applications where the unconstrained sum is already close to unity, it does not solve the constrained optimization problem and introduces potentially significant suboptimality. The constrained solution, obtained by enforcing both the non-negativity and sum-to-one constraints simultaneously during optimization, minimizes the objective residual on the feasible region. For epistemic logic tree construction in probabilistic seismic hazard analysis, where the sum-to-one constraint is a fundamental requirement reflecting the probabilistic interpretation of weights, constrained optimization via Lagrange multipliers or equivalent quadratic programming formulations is the theoretically sound and practically preferable approach [@KBSpecCompile]. Practitioners should employ dedicated constrained optimization solvers (such as active-set methods, interior-point methods, or convex quadratic programming packages) rather than normalizing the output of unconstrained or non-negativity-constrained solvers.
