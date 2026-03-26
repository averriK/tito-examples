# Weight Calibration via Constrained Linear Regression for Epistemic GMPE Logic Trees

## SLOT 1: Constrained linear regression formulation of the weight calibration error minimization problem

The calibration of branch weights for an epistemic ground-motion logic tree is formulated as a constrained linear regression problem in which the decision variables $w_k$ represent the probability assigned to each of the $N$ candidate ground-motion prediction equations (GMPEs). The objective is to determine non-negative weights that minimize the prediction error between the weighted linear combination of branch GMPE predictions and a calibration target, such as an observed or reference hazard curve. This formulation extends classical ordinary least-squares regression by introducing explicit inequality constraints that enforce the physical requirement that all weights be non-negative. [@SpecCompileResearch]

**Design matrix and target vector.** Assemble the hazard rate predictions of the $N$ candidate GMPEs into a design matrix $\mathbf{\Lambda} \in \mathbb{R}^{m \times N}$, where each row corresponds to a distinct intensity level and each column corresponds to a candidate GMPE. Define the entries as:

$$\Lambda_{jk} = \lambda_I^{(k)}(i_j^*),$$

where $\lambda_I^{(k)}(i_j^*)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE evaluated at intensity level $i_j^*$, for $j = 1, \ldots, m$ and $k = 1, \ldots, N$. Each column $\mathbf{\Lambda}_{\cdot k}$ contains the hazard curve of the $k$-th candidate GMPE across all $m$ intensity levels, and each row $\mathbf{\Lambda}_{j \cdot}$ contains the exceedance rates of all $N$ GMPEs at a single intensity level $i_j^*$. The target vector $\bar{\boldsymbol{\lambda}} \in \mathbb{R}^m$ contains the observed or reference mean hazard exceedance rates, with components $\bar{\lambda}_j = \bar{\lambda}_I(i_j^*)$. The weight vector $\mathbf{w} = (w_1, \ldots, w_N)^\top$ represents the unknown branch weights, and the weighted linear combination of branch hazard curves is $\hat{\bar{\boldsymbol{\lambda}}} = \mathbf{\Lambda}\mathbf{w}$. [@SpecCompileResearch]

**Objective function.** The objective of weight calibration is to find the weight vector $\mathbf{w}$ that minimizes the global root-mean-square error (RMSE) between the weighted linear combination of candidate hazard curves and the target hazard curve across all $m$ intensity levels:

$$\mathrm{RMSE}(\mathbf{w}) = \sqrt{\frac{1}{m} \sum_{j=1}^{m} \left( \sum_{k=1}^{N} w_k \lambda_I^{(k)}(i_j^*) - \bar{\lambda}_j \right)^2} = \frac{1}{\sqrt{m}} \left\|\mathbf{\Lambda} \mathbf{w} - \bar{\boldsymbol{\lambda}}\right\|_2.$$

Since $m$ is a fixed positive constant, minimizing RMSE is mathematically equivalent to minimizing the residual sum of squares:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{\Lambda} \mathbf{w} - \bar{\boldsymbol{\lambda}}\right\|_2^2.$$

The objective is a strictly convex quadratic in $\mathbf{w}$ with Hessian $2\mathbf{\Lambda}^\top\mathbf{\Lambda}$, which is positive semidefinite (and positive definite when $\mathbf{\Lambda}$ has full column rank). The gradient is $2\mathbf{\Lambda}^\top(\mathbf{\Lambda}\mathbf{w} - \bar{\boldsymbol{\lambda}})$, and unconstrained minimization yields the normal equations: [@SpecCompileResearch]

$$\mathbf{\Lambda}^\top \mathbf{\Lambda}\, \hat{\mathbf{w}} = \mathbf{\Lambda}^\top \bar{\boldsymbol{\lambda}}.$$

When $\mathbf{\Lambda}$ has full column rank (assured when $m \geq N$ and the candidate GMPE hazard curves are linearly independent across the intensity levels), the Gram matrix $\mathbf{\Lambda}^\top\mathbf{\Lambda} \in \mathbb{R}^{N \times N}$ is invertible and the unique ordinary least-squares solution is:

$$\hat{\mathbf{w}} = \left(\mathbf{\Lambda}^\top \mathbf{\Lambda}\right)^{-1} \mathbf{\Lambda}^\top \bar{\boldsymbol{\lambda}}.$$

**Non-negativity constraints and physical motivation.** The unconstrained OLS solution may admit negative components when two or more candidate GMPEs produce highly correlated hazard predictions. A negative weight $w_k < 0$ would imply subtracting the contribution of branch $k$ from the weighted combination---a construct with no physical meaning in logic trees, where weights represent non-negative probabilities or relative model plausibilities. No anti-GMPE with negated predictions exists in any defensible collection of ground-motion models. Enforcing $w_k \geq 0$ for all $k$ ensures that the calibrated weights represent physically meaningful contributions from each branch GMPE to the ensemble prediction. Additionally, the non-negativity constraint often produces sparse solutions in which many weights are exactly zero, automatically performing simultaneous model selection and weight assignment. [@SpecCompileResearch]

**Complete constrained formulation.** The weight calibration problem is formulated as the non-negative least-squares (NNLS) problem:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{\Lambda} \mathbf{w} - \bar{\boldsymbol{\lambda}}\right\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N.$$

The feasible region is the non-negative orthant of $\mathbb{R}^N$, a closed convex cone. The strictly convex quadratic objective over this convex feasible set guarantees a unique global minimizer, provided $\mathbf{\Lambda}$ has full column rank. This formulation defines the weight vector $\mathbf{w}$ as the solution to a bounded linear regression problem, with non-negativity inequality constraints replacing the unconstrained domain $\mathbb{R}^N$. [@SpecCompileResearch]

The constrained minimization may be solved via the active-set method of Lawson and Hanson, which partitions the index set $\{1, \ldots, N\}$ into an active set (indices where $w_k = 0$) and a passive set (indices where the weight is strictly positive), iteratively solving unconstrained OLS sub-problems on the passive set and updating the partition until the Karush-Kuhn-Tucker (KKT) optimality conditions are satisfied. This formulation establishes the mathematical foundation---objective function, decision variables, and inequality constraints---upon which the weight normalization extension of SLOT 2 is constructed. [@SpecCompileResearch]

---

## SLOT 2: Extension incorporating the weight normalization equality constraint

The NNLS formulation of SLOT 1 enforces non-negativity but does not restrict the sum of the weights. In the context of epistemic logic trees, the weights represent a discrete probability distribution over the candidate GMPEs and must therefore be normalized so that they form a proper probability measure, defined by the constraint:

$$\sum_{k=1}^{N} w_k = 1. \quad [@eq-weight-norm]$$

This normalization condition ensures that the weighted hazard curve represents a valid probabilistic combination and is consistent with the standard PSHA framework, in which the mean hazard integral is computed as a weighted average of branch-specific hazard integrals [@OpenQuakeEngine]. Incorporating this equality constraint transforms the NNLS problem into a fully constrained optimization problem that simultaneously enforces both the non-negativity bounds and the linear normalization condition. [@SpecCompileResearch]

**Complete constrained formulation.** The constrained optimization problem incorporating both the non-negativity inequality bounds and the weight normalization equality constraint is:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{\Lambda} \mathbf{w} - \bar{\boldsymbol{\lambda}}\right\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{N} w_k = 1, \quad w_k \geq 0, \quad k = 1, \ldots, N.$$

This is a convex quadratic program with $N$ linear inequality constraints and one linear equality constraint. The feasible region is the standard $(N-1)$-dimensional simplex:

$$\Delta_{N-1} = \left\{\mathbf{w} \in \mathbb{R}^N : \sum_{k=1}^{N} w_k = 1,\; w_k \geq 0 \right\},$$

a closed, compact, convex polytope defined by the intersection of the hyperplane $\sum_{k=1}^N w_k = 1$ and the non-negative orthant. The simplex is more restrictive than the non-negative orthant of SLOT 1, reducing the problem by one degree of freedom. The strictly convex quadratic objective over this compact convex feasible set guarantees a unique global minimizer $\mathbf{w}^*$. [@SpecCompileResearch]

**KKT optimality conditions.** The Karush-Kuhn-Tucker (KKT) conditions characterize the unique minimizer $\mathbf{w}^*$ of the fully constrained problem. There exist a Lagrange multiplier $\mu \in \mathbb{R}$ associated with the equality constraint and multipliers $\nu_k \geq 0$ associated with the non-negativity constraints such that the gradient of the Lagrangian vanishes at the optimum:

$$\nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w}^*, \mu, \boldsymbol{\nu}) = 2\mathbf{\Lambda}^\top(\mathbf{\Lambda}\mathbf{w}^* - \bar{\boldsymbol{\lambda}}) - \mu \mathbf{1} + \boldsymbol{\nu} = \mathbf{0},$$

where $\mathbf{1} \in \mathbb{R}^N$ is the vector of ones and $\boldsymbol{\nu} = (\nu_1, \ldots, \nu_N)^\top$, with complementary slackness holding: $\nu_k w_k^* = 0$ for all $k = 1, \ldots, N$. [@SpecCompileResearch]

**Solution properties.** The solution $\mathbf{w}^* = (w_1^*, \ldots, w_N^*)^\top$ simultaneously satisfies non-negativity ($w_k^* \geq 0$), normalization ($\sum_{k=1}^N w_k^* = 1$), and prediction-error minimality over the simplex. The addition of the normalization constraint may modify the sparsity pattern relative to the NNLS solution of SLOT 1: the redistribution requirement may activate additional GMPEs, but sparse solutions with some $w_k^* = 0$ remain possible, enabling simultaneous calibration and implicit model selection. When one or more candidate GMPEs are eliminated ($w_k^* = 0$), the effective logic tree reduces to the subset of GMPEs with strictly positive weights. [@SpecCompileResearch][@eq-weight-norm]

**Connection to PSHA.** The calibrated weight vector $\mathbf{w}^*$ defines a proper discrete probability distribution over the $N$ candidate GMPE branches. The resulting mean hazard curve is computed as the weighted linear combination:

$$\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k^* \lambda_I^{(k)}(i^*),$$

consistent with the standard PSHA framework [@OpenQuakeEngine] and the logic-tree normalization condition [@eq-weight-norm]. The fully constrained formulation ensures that the calibrated weights are statistically optimal (minimizing prediction error over the evaluation points) and probabilistically valid (non-negative and summing to unity), fulfilling the dual requirements for defensible probability assignment in epistemic logic trees.
