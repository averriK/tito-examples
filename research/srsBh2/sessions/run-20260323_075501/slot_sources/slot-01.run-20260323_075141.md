## SLOT 1: Extend weight formulation with sum-to-1 constraint

### Problem Statement and Constraint Integration

The spectral-matching weight-calibration problem, as formulated in the KB literature, minimizes the residual sum of squares between the weighted linear combination of candidate ground-motion spectra and a PSHA-derived target spectrum. [KB:spec.compile.research.md] The unconstrained ordinary least-squares objective is given by $\min_{\mathbf{w}} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2$, where $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ is the design matrix of log-spectral ordinates and $\mathbf{y} \in \mathbb{R}^n$ is the target log-spectrum. [KB:spec.compile.research.md] To incorporate epistemic logic tree conventions and ensure physical interpretability, the weight vector must satisfy two constraints: positivity ($w_k > 0$ for all $k$) and sum-to-unity ($\sum_{k=1}^K w_k = 1$). [KB:spec.compile.research.md] The sum-to-one constraint is essential in probability and decision-theoretic frameworks because it ensures that weights represent a normalized probability distribution or relative contribution measure, preventing the algorithm from assigning arbitrarily large or disproportionately skewed weights to individual records. ^[Confidence: HIGH, Rationale: The sum-to-one constraint is a standard requirement in epistemic logic trees for PSHA (as confirmed in the KB constraint statement) and is mathematically justified as a normalization that converts weights to interpretable relative contributions.]

### Constrained Optimization Formulation

The extended weight-calibration problem with sum-to-one constraint is formulated as a constrained least-squares problem: ^[Confidence: HIGH, Rationale: The problem formulation directly extends the unconstrained OLS framework (KB: SLOT 3) with the addition of explicitly stated sum-to-one and positivity constraints from the task requirements.]

$$\mathbf{w}^* = \underset{\mathbf{w} \in \mathbb{R}^K}{\arg\min} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^K w_k = 1 \quad \text{and} \quad w_k > 0, \; k = 1, \dots, K.$$

This is a constrained quadratic program combining an equality constraint (sum-to-one) and inequality constraints (positivity). [KB:spec.compile.research.md] The problem is a direct generalization of the bounded-weight least-squares formulation described in the KB, with the addition of an equality constraint replacing or supplementing the box constraints. The feasible region is now a $K$-dimensional simplex $\Delta^K = \{\mathbf{w} : w_k \geq 0, \sum_{k=1}^K w_k = 1\}$, which is a compact and convex polytope. ^[Confidence: HIGH, Rationale: The problem structure and constraints are directly derived from the unconstrained formulation (KB: SLOT 3) and bounded formulation (KB: SLOT 6), with the mathematical addition of an equality constraint well-established in constrained optimization theory.]

### Lagrangian Formulation and KKT Conditions

The constrained problem is solved via the method of Lagrange multipliers. Define the Lagrangian: ^[Confidence: HIGH, Rationale: The Lagrangian method is the standard mathematical approach for constrained optimization problems and is applied correctly here to the simplex-constrained least-squares problem.]

$$\mathcal{L}(\mathbf{w}, \lambda, \boldsymbol{\mu}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \left(1 - \sum_{k=1}^K w_k\right) + \sum_{k=1}^K \mu_k (0 - w_k),$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier for the equality constraint and $\boldsymbol{\mu} = (\mu_1, \dots, \mu_K)^\top$ with $\mu_k \geq 0$ are the multipliers for the non-negativity constraints $w_k \geq 0$. ^[Confidence: HIGH, Rationale: The definitions of Lagrange multipliers and their roles in enforcing equality and inequality constraints are standard in convex optimization theory.] The Karush-Kuhn-Tucker (KKT) conditions at optimality require: ^[Confidence: HIGH, Rationale: The KKT conditions are the necessary and sufficient conditions for optimality in convex constrained optimization, correctly applied to this problem with both equality and inequality constraints.]

$$\frac{\partial \mathcal{L}}{\partial w_k} = 2(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}))_k - \lambda - \mu_k = 0,$$

$$\mu_k w_k^* = 0 \quad \text{(complementary slackness)},$$

$$\sum_{k=1}^K w_k^* = 1, \quad w_k^* \geq 0.$$

Rearranging the first condition: ^[Confidence: HIGH, Rationale: Algebraic manipulation of the KKT gradient condition is straightforward and correctly performed.]

$$2(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}))_k = \lambda + \mu_k.$$

For indices $k$ where $w_k^* > 0$ (active set), the complementary slackness condition forces $\mu_k = 0$, yielding: ^[Confidence: HIGH, Rationale: Complementary slackness is a fundamental property of KKT conditions: if a constraint is inactive (weight is positive), its multiplier must be zero.]

$$2(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}))_k = \lambda.$$

For indices where $w_k^* = 0$ (inactive set), we must have: ^[Confidence: HIGH, Rationale: For inactive constraints (weights equal to zero), the dual variable must be non-negative to ensure the KKT conditions are satisfied.]

$$2(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}))_k \leq \lambda,$$

to ensure $\mu_k \geq 0$. ^[Confidence: HIGH, Rationale: The KKT conditions are the standard first-order optimality conditions for constrained convex quadratic programs, derived directly from Lagrangian formulation and applied to the equality and inequality constraints as specified in the problem.]

### Closed-Form Solution for the Equality-Constrained Problem

When the positivity constraint is temporarily relaxed (assuming all weights remain strictly positive at the optimum), the problem reduces to: ^[Confidence: HIGH, Rationale: Relaxing the non-negativity constraint to analyze the equality-constrained case is a standard approach in optimization; this case provides the basis for the subsequent active-set algorithm.]

$$\min_{\mathbf{w}} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \mathbf{1}^\top \mathbf{w} = 1,$$

where $\mathbf{1} = (1, 1, \dots, 1)^\top \in \mathbb{R}^K$ is the all-ones vector. The Lagrangian is: ^[Confidence: HIGH, Rationale: The Lagrangian formulation for the equality-constrained case is the direct application of the method of Lagrange multipliers to a simpler version of the problem.]

$$\mathcal{L}(\mathbf{w}, \lambda) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda(1 - \mathbf{1}^\top \mathbf{w}).$$

Setting the gradient with respect to $\mathbf{w}$ to zero: ^[Confidence: HIGH, Rationale: Taking the gradient and setting it to zero yields the first-order optimality condition for the equality-constrained problem.]

$$2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}) - \lambda \mathbf{1} = \mathbf{0}.$$

Rearranging: ^[Confidence: HIGH, Rationale: Algebraic rearrangement of the first-order condition to isolate the Gram matrix product.]

$$2\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}} \mathbf{w} = 2\tilde{\mathbf{A}}^\top \mathbf{y} + \lambda \mathbf{1}.$$

Multiplying both sides by $\mathbf{1}^\top$ and using $\mathbf{1}^\top \mathbf{w} = 1$: ^[Confidence: HIGH, Rationale: This algebraic manipulation uses the constraint $\mathbf{1}^\top \mathbf{w} = 1$ to solve for the Lagrange multiplier $\lambda$.]

$$2 \mathbf{1}^\top \tilde{\mathbf{A}}^\top \tilde{\mathbf{A}} \mathbf{w} = 2 \mathbf{1}^\top \tilde{\mathbf{A}}^\top \mathbf{y} + \lambda \mathbf{1}^\top \mathbf{1}.$$

Since $\mathbf{1}^\top \mathbf{1} = K$: ^[Confidence: HIGH, Rationale: The sum of $K$ ones is $K$ by definition.]

$$\lambda = \frac{2(\mathbf{1}^\top \tilde{\mathbf{A}}^\top \tilde{\mathbf{A}} \mathbf{w} - \mathbf{1}^\top \tilde{\mathbf{A}}^\top \mathbf{y})}{K}.$$

The closed-form solution is obtained by solving the linear system: ^[Confidence: HIGH, Rationale: The augmented saddle-point system is the standard formulation for solving equality-constrained least-squares problems; it combines the first-order condition and the constraint into a single linear system.]

$$\begin{pmatrix} 2\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}} & -\mathbf{1} \\ -\mathbf{1}^\top & 0 \end{pmatrix} \begin{pmatrix} \mathbf{w} \\ \lambda/2 \end{pmatrix} = \begin{pmatrix} 2\tilde{\mathbf{A}}^\top \mathbf{y} \\ -1 \end{pmatrix}.$$

This is a saddle-point system that can be solved using standard linear-algebra methods (LU decomposition, QR factorization, or iterative solvers). ^[Confidence: HIGH, Rationale: Saddle-point systems are well-studied in numerical linear algebra, and standard direct and iterative solvers are widely available and numerically stable for moderate problem sizes.] Define the augmented matrix system as: ^[Confidence: HIGH, Rationale: The matrix notation consolidates the system components (Gram matrix, constraint vector, and augmented right-hand side) in standard form for computational implementation.]

$$\begin{pmatrix} \tilde{\mathbf{G}} & -\mathbf{1} \\ -\mathbf{1}^\top & 0 \end{pmatrix}^{-1} \begin{pmatrix} \tilde{\mathbf{A}}^\top \mathbf{y} \\ -1/2 \end{pmatrix},$$

where $\tilde{\mathbf{G}} = \tilde{\mathbf{A}}^\top \tilde{\mathbf{A}}$ is the Gram matrix. ^[Confidence: HIGH, Rationale: The Gram matrix notation and its relationship to the spectral correlations are consistent with KB: SLOT 3, which introduces the same matrix in the unconstrained context.] Provided the augmented matrix is non-singular (which holds generically when $n > K$ and $\tilde{\mathbf{A}}$ has full column rank), the unique solution $(\mathbf{w}^*, \lambda^*)$ is obtained from this system. ^[Confidence: HIGH, Rationale: The derivation follows standard Lagrangian methods for constrained optimization and is mathematically sound; the augmented saddle-point system is a well-known technique in numerical linear algebra for solving equality-constrained least-squares problems.]

### Handling Non-Negativity: Simplex-Constrained Optimization

When non-negativity is enforced (i.e., $w_k \geq 0$), the solution lies on the simplex $\Delta^K$. If the unconstrained equality-constrained solution $\mathbf{w}^{\text{eq}}$ obtained from the saddle-point system has all positive components, then $\mathbf{w}^* = \mathbf{w}^{\text{eq}}$. If any component is negative, an active-set method must partition the indices into those with $w_k = 0$ and those with $w_k > 0$, solving the reduced equality-constrained problem iteratively. [KB:spec.compile.research.md] The active-set algorithm for simplex-constrained least-squares proceeds as follows: (1) Solve the equality-constrained problem over all $K$ variables; (2) if any $w_k < 0$, remove the most negative index from the active set and fix it to zero; (3) re-solve the equality-constrained problem over the remaining free variables; (4) repeat until all weights are non-negative. This approach is equivalent to solving a sequence of reduced equality-constrained problems on lower-dimensional subspaces, each of which can be addressed using the saddle-point formulation above. ^[Confidence: HIGH, Rationale: The active-set method for simplex-constrained optimization is a standard algorithmic approach (mentioned in KB: SLOT 5 for NNLS) and is applicable here as a generalization to the simplex-constrained case.]

### Implementation Considerations

The simplex-constrained least-squares problem can be implemented using several approaches. For moderate problem sizes, the augmented Lagrangian system can be solved directly using dense linear algebra (e.g., the `solve` function in R combined with a block-matrix inversion). Alternatively, the problem can be reformulated as a constrained quadratic program and solved using convex optimization libraries such as `quadprog` (which supports both equality and inequality constraints) or `CVXR` (for more complex penalty combinations). [KB:spec.compile.research.md] In R, a direct implementation using `quadprog` specifies equality constraints via the `meq` argument:

```r
library(quadprog)

K     <- ncol(A_tilde)
Dmat  <- 2 * crossprod(A_tilde) + diag(K) * 1e-8
dvec  <- 2 * as.vector(crossprod(A_tilde, y))
Amat  <- rbind(rep(1, K), diag(K), -diag(K))
bvec  <- c(1, rep(0, K), rep(-Inf, K))

fit_simplex <- solve.QP(Dmat = Dmat, dvec = dvec, Amat = Amat, bvec = bvec, meq = 1)
w_simplex   <- fit_simplex$solution
```

The argument `meq = 1` indicates that the first constraint is an equality constraint (the sum-to-one condition), while the remaining constraints are inequalities (non-negativity and absence of upper bounds). ^[Confidence: MEDIUM, Rationale: The implementation guidance combines established quadratic programming techniques (from KB: SLOT 6) with the simplex constraint; R syntax is provided as a practical tool but would benefit from validation on actual data to confirm numerical stability.]

---

