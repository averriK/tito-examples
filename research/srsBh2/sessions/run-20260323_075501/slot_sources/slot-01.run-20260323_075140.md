## SLOT 1: Extend weight formulation with sum-to-1 constraint

The spectral-matching problem for ground-motion record selection can be formulated as a constrained linear regression in which weights assigned to candidate records must satisfy both positivity and normalization requirements. [KB:spec.compile.research.md] The classical unconstrained ordinary least-squares (OLS) solution permits negative weights and places no constraint on their magnitude, necessitating extensions that impose physical plausibility. [KB:spec.compile.research.md] Incorporating the requirement that weights sum to unity formalizes the epistemic logic tree framework in which each weight represents the fractional contribution—or equivalently, the prior probability—assigned to a ground-motion prediction equation or record within the suite.
^[Confidence: HIGH, Rationale: The foundational setup is directly supported by the KB document (SLOT 3 and motivation sections), which establishes the unconstrained OLS problem and the need for constraints. The framing in terms of epistemic logic trees is consistent with the task context.]

The extended problem formulation combines the log-domain regression objective from the KB with three inequality and equality constraints. [KB:spec.compile.research.md] Let $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ denote the transformed design matrix with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$ (the natural logarithm of spectral acceleration of record $k$ at period $T_i$), let $\mathbf{y} \in \mathbb{R}^n$ denote the log-domain target spectral vector with components $y_i = \ln S_a^{\mathrm{obj}}(T_i)$, and let $\mathbf{w} = (w_1, \dots, w_K)^\top$ denote the weight vector. [KB:spec.compile.research.md] The constrained optimization problem is formulated as:

$$\mathbf{w}^* = \underset{\mathbf{w} \in \mathbb{R}^K}{\arg\min} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad w_k > 0 \text{ for } k = 1, \dots, K, \quad \sum_{k=1}^{K} w_k = 1.$$

This formulation generalizes the non-negative least-squares (NNLS) and bounded-variable least-squares (BVLS) formulations described in the knowledge base [KB:spec.compile.research.md] by replacing the lower bound of zero with an open lower bound $w_k > 0$ (strictly positive) and adding a linear equality constraint that the weights must sum to exactly one.
^[Confidence: HIGH, Rationale: The problem statement directly extends the NNLS and BVLS formulations from the KB (SLOT 5 and SLOT 6). The mathematical notation is consistent with the KB's presentation, and the constraint structure is a natural combination of known constraints.]

The constrained quadratic programming problem with positivity and equality constraints is solved using the method of Lagrange multipliers. Define the Lagrangian:

$$\mathcal{L}(\mathbf{w}, \boldsymbol{\lambda}, \mu) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \sum_{k=1}^{K} \lambda_k (-w_k) + \mu \left(\sum_{k=1}^{K} w_k - 1\right),$$

where $\boldsymbol{\lambda} = (\lambda_1, \dots, \lambda_K)^\top$ are the Lagrange multipliers for the inequality constraints $-w_k \leq 0$ (equivalently, $w_k \geq 0$), and $\mu$ is the Lagrange multiplier for the equality constraint $\sum_{k=1}^{K} w_k = 1$. The complementary slackness conditions require that $\lambda_k w_k = 0$ for each $k$: if $w_k > 0$ then $\lambda_k = 0$; if $w_k = 0$ then $\lambda_k \geq 0$.
^[Confidence: HIGH, Rationale: The Lagrangian formulation is the standard approach for constrained optimization with inequality and equality constraints. The setup is consistent with standard convex optimization theory and is applicable to the constraint structure specified in the task.]

The first-order optimality conditions (Karush-Kuhn-Tucker, or KKT, conditions) require:

$$\frac{\partial \mathcal{L}}{\partial w_k} = 2 \tilde{\mathbf{A}}_{\cdot k}^\top (\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) - \lambda_k + \mu = 0 \quad \text{for } k = 1, \dots, K,$$

where $\tilde{\mathbf{A}}_{\cdot k}$ denotes the $k$-th column of $\tilde{\mathbf{A}}$. Rearranging:

$$2 \tilde{\mathbf{A}}_{\cdot k}^\top (\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) = \lambda_k - \mu.$$

At the optimum, if $w_k^* > 0$, then $\lambda_k = 0$ by complementary slackness, and the first-order condition becomes:

$$2 \tilde{\mathbf{A}}_{\cdot k}^\top (\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) = -\mu.$$

This equation states that the reduced gradient (the cross-correlation between the $k$-th candidate spectrum and the residual, scaled by 2) must equal the negative of the Lagrange multiplier $\mu$ for every record with $w_k^* > 0$. The multiplier $\mu$ thus plays the role of a common Lagrange price: it is the value of relaxing the sum-to-one constraint by an infinitesimal amount, and all active (positive-weight) records share this price at optimality.
^[Confidence: HIGH, Rationale: The KKT conditions are the standard optimality characterization for constrained quadratic programming. The interpretation of $\mu$ as the Lagrange price is standard in constrained optimization theory. The first-order conditions are correctly derived from the Lagrangian.]

An alternative formulation removes the lower-bound inequality constraints and reformulates the problem directly as a constrained least-squares minimization with only the equality constraint:

$$\mathbf{w}^* = \underset{\mathbf{w} \in \mathbb{R}^K}{\arg\min} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1.$$

This relaxation permits $w_k$ to be negative or zero. The Lagrangian becomes:

$$\mathcal{L}(\mathbf{w}, \mu) = \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 + \mu \left(\sum_{k=1}^{K} w_k - 1\right).$$

Setting the gradient with respect to $\mathbf{w}$ to zero:

$$2\tilde{\mathbf{A}}^\top (\tilde{\mathbf{A}}\mathbf{w}^* - \mathbf{y}) + \mu \mathbf{1} = \mathbf{0},$$

where $\mathbf{1} \in \mathbb{R}^K$ is the all-ones vector. Rearranging:

$$\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}} \mathbf{w}^* = \tilde{\mathbf{A}}^\top \mathbf{y} - \frac{\mu}{2} \mathbf{1}.$$

Premultiplying both sides by $\mathbf{1}^\top (\tilde{\mathbf{A}}^\top \tilde{\mathbf{A}})^{-1}$ and enforcing the constraint $\mathbf{1}^\top \mathbf{w}^* = 1$, one can solve for $\mu$ and then recover $\mathbf{w}^*$ in closed form. [KB:spec.compile.research.md]
^[Confidence: HIGH, Rationale: This is the standard equality-constrained least-squares approach, which admits a closed-form solution via Lagrange multipliers. The algebraic derivation is correct and represents a well-known technique in linear algebra and optimization.]

To enforce strict positivity ($w_k > 0$ for all $k$), the constrained problem must include the inequality constraints in the Lagrangian and either use active-set methods or add a small barrier term. An interior-point method parameterized by a barrier parameter $\epsilon > 0$ would replace the constraints with a penalty:

$$\mathbf{w}^* = \underset{\mathbf{w} \in \mathbb{R}^K}{\arg\min} \; \|\tilde{\mathbf{A}}\mathbf{w} - \mathbf{y}\|_2^2 - \epsilon \sum_{k=1}^{K} \ln w_k \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1,$$

where the logarithmic barrier $-\epsilon \sum_{k=1}^{K} \ln w_k$ diverges to $+\infty$ as any $w_k \to 0^+$, enforcing the positivity constraint at the limit as $\epsilon \to 0^+$. This formulation is strictly convex, and solvers such as interior-point methods or trust-region algorithms converge rapidly to a unique global optimum.
^[Confidence: HIGH, Rationale: The interior-point/barrier method is a standard technique in constrained optimization for enforcing inequality constraints. The logarithmic barrier function is the canonical approach and is well-documented in the optimization literature. The claim about strict convexity and convergence is standard.]

In practice, if the unconstrained equality-constrained solution (without positivity bounds) yields all positive weights, that solution is the global minimum of the strictly-positivity-constrained problem. Verification can be performed by checking that all computed $w_k^* > 0$ and that the KKT conditions are satisfied with $\lambda_k = 0$ for all $k$. If any unconstrained solution has $w_k^* \leq 0$, an active-set method or interior-point solver is required to find the correct constrained minimum.
^[Confidence: HIGH, Rationale: This is a practical observation consistent with the theory: if the unconstrained solution is already feasible (all positive weights), it is automatically optimal for the constrained problem. The verification via KKT conditions is the standard optimality test.]

