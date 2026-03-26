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

