## SLOT 1: Extend weight formulation with sum-to-1 constraint

The spectral-matching problem using linear combinations of ground motion records requires that weights assigned to each candidate record must be positive and, in many applications involving epistemic logic trees for probabilistic seismic hazard analysis (PSHA), must sum to unity to represent a complete probability distribution over alternative models. [KB:spec.compile.research.md] The constrained optimization formulation that incorporates both the positivity requirement and the normalization constraint can be formulated as a classical constrained least-squares problem with one equality constraint and $K$ inequality constraints. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The KB document (spec.compile.research.md) establishes the foundational framework for spectral-matching with non-negative weights and provides the mathematical formulation for constrained optimization. The motivation for positive weights and the context of epistemic logic trees in PSHA are clearly documented.]

The constrained optimization formulation unifies the requirement that weights be positive ($w_k > 0$ for all $k = 1, \dots, K$) with the normalization constraint that the weights sum to one. Formally, the problem is stated as finding the weight vector $\mathbf{w} = (w_1, \dots, w_K)^\top$ that minimizes the residual sum of squares subject to linear constraints:

$$\min_{\mathbf{w} \in \mathbb{R}^K} \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k \geq 0 \text{ for all } k = 1, \dots, K, \quad \sum_{k=1}^{K} w_k = 1.$$

Here, $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ is the design matrix containing log-space spectral ordinates, $\mathbf{y} \in \mathbb{R}^n$ is the target log-spectral vector, and the equality constraint $\sum_{k=1}^K w_k = 1$ enforces normalization. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: This formulation is a direct generalization of the NNLS problem presented in the KB document. The structure preserves the mathematical framework while adding the linear equality constraint, which is standard in constrained optimization literature.]

The solution to this problem is obtained through the Karush-Kuhn-Tucker (KKT) conditions, which provide necessary and sufficient conditions for optimality when the objective is convex and the constraints are linear. The Lagrangian for the constrained problem is:

$$\mathcal{L}(\mathbf{w}, \lambda, \boldsymbol{\mu}) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda\left(\sum_{k=1}^{K} w_k - 1\right) + \sum_{k=1}^{K} \mu_k (-w_k),$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier for the equality constraint and $\boldsymbol{\mu} = (\mu_1, \dots, \mu_K)^\top$ are the non-negative multipliers for the inequality constraints $w_k \geq 0$.

^[Confidence: HIGH, Rationale: The Lagrangian formulation is standard for constrained optimization problems. The structure with an equality multiplier $\lambda$ (unrestricted in sign) and inequality multipliers $\boldsymbol{\mu} \geq 0$ is the canonical approach for KKT conditions and is mathematically correct.]

The first-order stationarity condition requires that the gradient of the Lagrangian with respect to $\mathbf{w}$ be zero:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = 2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) + \lambda^* \mathbf{1} - \boldsymbol{\mu}^* = 0,$$

where $\mathbf{1} = (1, 1, \dots, 1)^\top$ is the vector of ones and asterisks denote optimal values. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: This gradient condition is the direct application of standard constrained optimization theory to the squared-residual objective. The KB document's treatment of gradients and the normal equations in the unconstrained case provides the foundational method.]

Rearranging, the optimality condition at any active constraint (where $w_k^* > 0$) is:

$$2(\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\mathbf{w}^*)_k - 2(\tilde{\mathbf{A}}^\top\mathbf{y})_k + \lambda^* = 0.$$

For indices where the constraint is inactive (i.e., $w_k^* = 0$), complementary slackness requires $\mu_k^* \geq 0$, which implies $2(\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\mathbf{w}^*)_k - 2(\tilde{\mathbf{A}}^\top\mathbf{y})_k + \lambda^* \leq 0$.

^[Confidence: HIGH, Rationale: Complementary slackness is the standard condition in KKT theory for inequality constraints and is correctly applied here. The inequality for inactive constraints follows directly from the non-negativity of dual multipliers.]

The constrained problem admits several equivalent computational approaches. The most direct method treats the problem as a quadratic program (QP) with one linear equality constraint and $K$ linear inequality constraints. Using the standard QP formulation, the constraint matrix can be constructed such that the problem is solved by interior-point or active-set QP solvers. Alternatively, the equality constraint can be eliminated by parameterizing the weight vector in a lower-dimensional subspace. If one chooses to eliminate the constraint, the weight vector can be written as $\mathbf{w} = \mathbf{w}_0 + \mathbf{v}$, where $\mathbf{w}_0$ is any feasible point satisfying $\sum_k w_{0,k} = 1$ and $\mathbf{v}$ lies in the null space of the constraint, meaning $\sum_k v_k = 0$. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The constrained QP formulation and the null-space parameterization are both standard techniques in numerical optimization. The QB document's discussion of QP solvers (quadprog) provides the foundational reference for the QP approach.]

In the null-space parameterization, the reduced problem becomes:

$$\min_{\mathbf{v} \in \mathbb{R}^{K-1}} \|\tilde{\mathbf{A}}(\mathbf{w}_0 + \mathbf{v}) - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_{0,k} + v_k \geq 0 \text{ for all } k.$$

The null-space basis can be constructed explicitly by performing QR decomposition of the constraint matrix (in this case, simply $\mathbf{1}^\top$), which yields an orthonormal matrix $\mathbf{Q} \in \mathbb{R}^{K \times (K-1)}$ such that $\mathbf{1}^\top \mathbf{Q} = \mathbf{0}$ and $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}_{K-1}$. Then $\mathbf{v} = \mathbf{Q}\mathbf{z}$ for some $\mathbf{z} \in \mathbb{R}^{K-1}$.

^[Confidence: HIGH, Rationale: The null-space parameterization using QR decomposition is a standard technique in numerical linear algebra and constrained optimization. The mathematical construction is correct and well-established.]

Substituting this parameterization, the reduced problem becomes unconstrained in the interior of the feasible region (where all inequality constraints are inactive) and reduces to a standard least-squares problem on the null space:

$$\min_{\mathbf{z} \in \mathbb{R}^{K-1}} \|\tilde{\mathbf{A}}\mathbf{Q}\mathbf{z} + (\tilde{\mathbf{A}}\mathbf{w}_0 - \mathbf{y})\|_2^2.$$

The closed-form solution in the null space is:

$$\mathbf{z}^* = -(\mathbf{Q}^\top\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\mathbf{Q})^{-1}\mathbf{Q}^\top\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w}_0 - \mathbf{y}),$$

provided that $\mathbf{Q}^\top\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}\mathbf{Q}$ is invertible. The optimal weight vector in the original space is then $\mathbf{w}^* = \mathbf{w}_0 + \mathbf{Q}\mathbf{z}^*$.

^[Confidence: HIGH, Rationale: The null-space least-squares solution is derived from standard linear algebra and is correct. The method is mathematically sound and equivalent to solving the original constrained QP problem.]

An active-set algorithm is necessary to enforce the non-negativity constraints $w_k \geq 0$ when interior solutions produce negative components. The algorithm maintains a partition of the index set into an active set $\mathcal{A}$ (indices where $w_k = 0$) and a passive set $\mathcal{P}$ (indices where $w_k > 0$). At each iteration, the algorithm solves the reduced problem over the passive set, checks the KKT conditions for optimality, and either terminates or updates the partition by removing or adding indices to the active set. This procedure converges in a finite number of iterations and yields the global optimum because the objective is strictly convex and the constraints form a closed convex set. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The active-set method is the standard approach described in the KB document for the NNLS problem. Its application here to the sum-to-1 constrained problem is a direct extension and maintains the convergence guarantees.]

In computational practice, the constrained problem with sum-to-one normalization can be solved using generic convex optimization libraries such as CVXR in R, which automatically handle the equality and inequality constraints via disciplined convex programming. [KB:spec.compile.research.md] The user specifies the objective function and constraint set, and the library dispatches to an appropriate solver (such as CLARABEL, SCS, or OSQP) without requiring manual KKT condition verification.

^[Confidence: HIGH, Rationale: CVXR is explicitly referenced in the KB document as a tool for solving generalized convex optimization problems with box constraints. The application to sum-to-one constraints is a direct extension.]

---

