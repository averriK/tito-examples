# Constrained Weight Calibration for Epistemic Logic Trees: Unit-Sum Normalization in Least-Squares Formulation

## SLOT 1: Extension of the Error Minimization Formulation with Unit-Sum Weight Constraint

The error minimization problem established in the knowledge base addresses the selection and weighting of candidate ground-motion prediction models through least-squares regression. The foundational formulation minimizes the residual sum of squares (RSS) over unconstrained weights, admitting negative values that lack physical meaning. This extension incorporates both non-negativity and unit-sum normalization as equality and inequality constraints, yielding a constrained quadratic programming problem consistent with the probabilistic treatment of epistemic uncertainty in logic-tree representations. [KB:spec.compile.research.md]

### Problem Statement and Constraint Structure

The constrained optimization problem is formulated as follows. Let $\tilde{\mathbf{A}} \in \mathbb{R}^{n \times K}$ denote the design matrix with entries $\tilde{A}_{ik} = \ln S_{a,k}(T_i)$, where $S_{a,k}(T_i)$ is the pseudo-spectral acceleration of the $k$-th candidate model at period $T_i$. The target vector $\tilde{\mathbf{y}} \in \mathbb{R}^n$ contains the log-spectral ordinates $\tilde{y}_i = \ln S_a^{\mathrm{obj}}(T_i)$ of the PSHA-derived target spectrum. The weight vector $\mathbf{w} = (w_1, \ldots, w_K)^\top$ is subject to three constraints that extend the KB framework: [KB:spec.compile.research.md]

$$\min_{\mathbf{w} \in \mathbb{R}^K} \; \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} w_k = 1, \quad w_k \geq 0 \; \text{for all} \; k = 1, \ldots, K.$$

^[Confidence: HIGH, Rationale: The problem statement extends the unconstrained least-squares formulation from KB SLOT 3 by adding the normalization constraint as an explicit equality condition. The non-negativity constraint carries forward from KB SLOT 5. This formulation is a standard form for constrained convex quadratic programming with the log-spectral design matrix and target vector as described in the KB.]

The constraint set defines the unit simplex $\Delta^K = \{\mathbf{w} \in \mathbb{R}^K : \sum_k w_k = 1, \, w_k \geq 0\}$, a compact convex polytope. The objective function is a strictly convex quadratic with positive-semidefinite Hessian $2\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}}$ (assuming $\tilde{\mathbf{A}}$ has full column rank). The problem thus admits a unique global minimizer. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The geometric characterization of the simplex and the convexity of the objective are standard results in convex analysis. The convexity properties ensure existence and uniqueness of the global minimum, which is consistent with the convex optimization framework presented in KB SLOT 7.]

### Lagrangian Formulation and First-Order Conditions

The constraint is incorporated via the Lagrangian:

$$\mathcal{L}(\mathbf{w}, \lambda, \boldsymbol{\mu}) = \|\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}}\|_2^2 - \lambda \left(\sum_{k=1}^{K} w_k - 1\right) - \sum_{k=1}^{K} \mu_k w_k,$$

where $\lambda \in \mathbb{R}$ is the Lagrange multiplier associated with the equality constraint and $\boldsymbol{\mu} = (\mu_1, \ldots, \mu_K)^\top$ with $\mu_k \geq 0$ are the multipliers for the non-negativity inequalities. The Karush-Kuhn-Tucker (KKT) conditions require:

$$\frac{\partial \mathcal{L}}{\partial w_k} = 2\left(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}})\right)_k - \lambda - \mu_k = 0,$$

with complementary slackness $\mu_k w_k = 0$ and $\mu_k \geq 0$ for all $k$.

^[Confidence: HIGH, Rationale: The Lagrangian formulation and KKT conditions are the standard framework for constrained optimization with inequality and equality constraints. The derivation follows directly from first-order optimality conditions for the simplex-constrained quadratic program.]

Rearranging the first-order condition:

$$2\left(\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}})\right)_k = \lambda + \mu_k.$$

Let $\mathbf{g} = 2\tilde{\mathbf{A}}^\top(\tilde{\mathbf{A}}\mathbf{w} - \tilde{\mathbf{y}})$ denote the gradient of the objective at $\mathbf{w}$. Then $g_k = \lambda + \mu_k$. Since $\mu_k \geq 0$ and $\mu_k w_k = 0$:
- If $w_k > 0$, then $\mu_k = 0$ and $g_k = \lambda$.
- If $w_k = 0$, then $g_k = \lambda + \mu_k \geq \lambda$, with $\mu_k = g_k - \lambda \geq 0$.

At the optimum, all positive-weight indices share a common gradient value $\lambda$, while zero-weight indices have gradient at least $\lambda$.

^[Confidence: HIGH, Rationale: The interpretation of the KKT conditions for the simplex-constrained problem is the standard characterization of the solution structure. The property that all active (positive-weight) components have equal gradient at optimality is a fundamental feature of least-squares problems over the simplex.]

### Reduced Formulation and Active Set

Let $\mathcal{A} = \{k : w_k > 0\}$ denote the active set of indices with positive weight. The solution can be characterized through the reduced problem:

$$\min_{\mathbf{w}_{\mathcal{A}} \in \mathbb{R}^{|\mathcal{A}|}} \; \|\tilde{\mathbf{A}}_{\mathcal{A}}\mathbf{w}_{\mathcal{A}} - \tilde{\mathbf{y}}\|_2^2 \quad \text{subject to} \quad \sum_{k \in \mathcal{A}} w_k = 1, \quad w_k \geq 0,$$

where $\tilde{\mathbf{A}}_{\mathcal{A}} \in \mathbb{R}^{n \times |\mathcal{A}|}$ is the design matrix restricted to the active columns. If $|\mathcal{A}| \leq n$, this sub-problem admits a unique solution when the active columns are linearly independent. The gradient condition $g_k = \lambda$ for $k \in \mathcal{A}$ and $g_k \geq \lambda$ for $k \notin \mathcal{A}$ ensures that no index can profitably enter the active set, confirming optimality.

^[Confidence: HIGH, Rationale: The reduction to the active set problem and the optimality characterization are the standard active-set method approach for linearly constrained quadratic programs. This is well-established in convex optimization theory.]

### Unconstrained Auxiliary Problem

An equivalent formulation uses an unconstrained auxiliary problem with a slack variable. Eliminate the normalization constraint through $\mathbf{w} = \tilde{\mathbf{w}}/\sum_j \tilde{w}_j$, where $\tilde{\mathbf{w}} \in \mathbb{R}^K_{\geq 0}$ is the unnormalized weight vector. The objective becomes:

$$\min_{\tilde{\mathbf{w}} \in \mathbb{R}^K_{\geq 0}} \; \left\|\tilde{\mathbf{A}} \frac{\tilde{\mathbf{w}}}{\sum_j \tilde{w}_j} - \tilde{\mathbf{y}}\right\|_2^2.$$

Let $s = \sum_j \tilde{w}_j$. Then:

$$\min_{\tilde{\mathbf{w}}, s} \; \left\|\tilde{\mathbf{A}} \frac{\tilde{\mathbf{w}}}{s} - \tilde{\mathbf{y}}\right\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{K} \tilde{w}_k = s, \quad \tilde{w}_k \geq 0, \quad s > 0.$$

This reformulation highlights that the constrained problem is equivalent to a non-negative least-squares problem followed by normalization; the optimal value of $s$ emerges from the KKT conditions of the full simplex-constrained program.

^[Confidence: HIGH, Rationale: The reformulation via the slack variable $s$ is a standard technique in convex optimization for converting simplex-constrained problems into non-negative least-squares form. The equivalence is well-founded.]

### Comparison with KB Benchmarks

The KB framework establishes three reference problems: the unconstrained OLS solution (KB SLOT 3), the non-negative least-squares (NNLS) solution (KB SLOT 5), and the bounded-weight solution (KB SLOT 6). The unit-sum constrained problem sits between NNLS and bounded-weight constraints in terms of restrictiveness. [KB:spec.compile.research.md]

The unconstrained OLS solution $\hat{\mathbf{w}}_{\mathrm{OLS}} = (\tilde{\mathbf{A}}^\top\tilde{\mathbf{A}})^{-1}\tilde{\mathbf{A}}^\top\tilde{\mathbf{y}}$ does not satisfy the unit-sum condition in general; it is obtained by solving an unrestricted problem over all of $\mathbb{R}^K$. The NNLS solution $\hat{\mathbf{w}}_{\mathrm{NNLS}}$ minimizes the same objective over the non-negative orthant $\mathbb{R}^K_{\geq 0}$, a much larger feasible region than the unit simplex. The proposed unit-sum constrained solution $\hat{\mathbf{w}}_*$ minimizes over the intersection of the non-negative orthant and the hyperplane $\sum w_k = 1$, a tighter constraint. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The comparison of constraint sets and solution regions is based directly on the mathematical definitions given in the KB. The ordering of feasibility regions (simplex is contained in non-negative orthant is contained in $\mathbb{R}^K$) is a basic fact of convex geometry.]

The residual sum of squares satisfies:

$$\mathrm{RSS}(\hat{\mathbf{w}}_{\mathrm{OLS}}) \leq \mathrm{RSS}(\hat{\mathbf{w}}_{\mathrm{NNLS}}) \leq \mathrm{RSS}(\hat{\mathbf{w}}_*),$$

because the feasible region shrinks as constraints tighten, monotonically increasing the optimal objective value. The residual $\mathrm{RSS}(\hat{\mathbf{w}}_*)$ is the smallest-RSS solution achievable under both non-negativity and unit-sum normalization simultaneously.

^[Confidence: HIGH, Rationale: The monotonic increase in the objective value as the feasible region shrinks is a basic consequence of constrained optimization: a tighter feasible set excludes the previous optimum, forcing a sub-optimal point. This is elementary convex optimization.]

### Role in Epistemic Logic Trees

In the context of epistemic logic trees for PSHA, the unit-sum constraint $\sum_{k=1}^{K} w_k = 1$ enforces the normalization condition required for the weights to form a valid probability distribution over the discrete set of candidate models. [KB:spec.compile.research.md] The non-negativity constraint $w_k \geq 0$ ensures physical plausibility by precluding anti-models. Together, they ensure that the calibrated weights $\hat{\mathbf{w}}_*$ define a discrete probability measure over the branch set.

The optimization-based calibration approach performs simultaneous model selection and weight assignment: indices with $\hat{w}_k = 0$ are effectively de-selected, while indices with $\hat{w}_k > 0$ receive positive probability. This is advantageous in regions where observational data density is variable, allowing data-driven suppression of poorly-supported models while assigning proportionate weight to those consistent with available information.

^[Confidence: HIGH, Rationale: The connection to logic-tree normalization is drawn from the task context and is consistent with the probabilistic treatment of epistemic uncertainty outlined in the PSHA framework. The role of weights as a probability distribution is standard in risk analysis.]

### Computational Approaches

The simplex-constrained quadratic program is solvable by several methods. An active-set algorithm partitions the variables into the active set (positive weights) and inactive set (zero weights), iteratively refining the partition until KKT conditions are satisfied. For small to moderate problem sizes ($K \lesssim 100$), a direct approach using interior-point methods or Sequential Least Squares Programming (SLSQP) is efficient. For larger $K$ or when coupled with additional penalty terms (Lasso or Ridge regularization, extending the convex framework from KB SLOT 7), convex optimization libraries such as CVXR or dedicated solvers (OSQP, CLARABEL) handle the problem robustly. [KB:spec.compile.research.md]

The specialization of the general convex formulation from KB SLOT 7 to the unit-sum case sets $\lambda_1 = \lambda_2 = 0$ (no penalty terms), applies the simplex constraint in place of the box constraints $[w_{\min}, w_{\max}]$, and solves the resulting problem. The same disciplined convex programming methodology applies, with convexity verification automatic through the DCP composition rules in libraries such as CVXR.

^[Confidence: MEDIUM, Rationale: The computational methods referenced (active-set, interior-point, SLSQP) are standard techniques for quadratic programming, though specific implementation details depend on the chosen solver library. The reduction from the general KB formulation to the simplex-constrained case is straightforward and well-founded, but no computational benchmarks or implementation results are provided in the KB or from external sources in this analysis.]

### Summary

The extension of the error minimization formulation with unit-sum weight normalization maintains the three stated hypotheses: (1) the problem is a generalization of constrained linear regression, (2) non-negativity is enforced for all weights, and (3) the unit-sum constraint is incorporated as an equality condition in the optimization. The resulting constrained quadratic program admits a unique solution over the unit simplex, ensuring that the calibrated weights form a valid discrete probability distribution over candidate models. This formulation bridges the unconstrained and NNLS approaches documented in the KB, enabling calibration that respects both physical plausibility and the normalization requirement of logic-tree representations. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The summary accurately reflects the constrained optimization framework developed in the preceding sections and maintains consistency with the three hypotheses stated in the task. All claims are supported by the problem formulation and the KB material on convex optimization and least-squares methods.]
