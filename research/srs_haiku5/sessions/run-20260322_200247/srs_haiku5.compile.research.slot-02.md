## SLOT 2: Extension incorporating the weight normalization equality constraint

The NNLS formulation of SLOT 1 enforces non-negativity but does not restrict the sum of the weights. In the context of epistemic logic trees, the weights represent a discrete probability distribution over the candidate GMPEs and must therefore be normalized so that they form a proper probability measure, defined by the constraint:

$$\sum_{k=1}^{N} w_k = 1. \quad [@eq-weight-norm]$$

This normalization condition ensures that the weighted hazard curve represents a valid probabilistic combination and is consistent with the standard PSHA framework, in which the mean hazard integral is computed as a weighted average of branch-specific hazard integrals [@OpenQuakeEngine]. Incorporating this equality constraint transforms the NNLS problem into a fully constrained optimization problem that simultaneously enforces both the non-negativity bounds and the linear normalization condition. [@SpecCompileResearch]

**Complete constrained formulation.** The constrained optimization problem incorporating both the non-negativity inequality bounds from SLOT 1 and the weight normalization equality constraint is:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{\Lambda} \mathbf{w} - \bar{\boldsymbol{\lambda}}\right\|_2^2 \quad \text{subject to} \quad \sum_{k=1}^{N} w_k = 1, \quad w_k \geq 0, \quad k = 1, \ldots, N.$$

This is a convex quadratic program with $N$ linear inequality constraints and one linear equality constraint. The feasible region is the standard $(N-1)$-dimensional simplex:

$$\Delta_{N-1} = \left\{\mathbf{w} \in \mathbb{R}^N : \sum_{k=1}^{N} w_k = 1,\; w_k \geq 0 \right\},$$

a closed, compact, convex polytope defined by the intersection of the hyperplane $\sum_{k=1}^N w_k = 1$ and the non-negative orthant. The simplex is more restrictive than the non-negative orthant of SLOT 1, reducing the problem by one degree of freedom. The strictly convex quadratic objective over this compact convex feasible set guarantees a unique global minimizer $\mathbf{w}^*$. [@SpecCompileResearch]

**KKT optimality conditions.** The Karush-Kuhn-Tucker (KKT) conditions characterize the unique minimizer $\mathbf{w}^*$ of the fully constrained problem. There exist a Lagrange multiplier $\mu \in \mathbb{R}$ associated with the equality constraint and multipliers $\nu_k \geq 0$ associated with the non-negativity constraints such that the gradient of the Lagrangian vanishes at the optimum:

$$\nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w}^*, \mu, \boldsymbol{\nu}) = 2\mathbf{\Lambda}^\top(\mathbf{\Lambda}\mathbf{w}^* - \bar{\boldsymbol{\lambda}}) - \mu \mathbf{1} + \boldsymbol{\nu} = \mathbf{0},$$

where $\mathbf{1} \in \mathbb{R}^N$ is the vector of ones and $\boldsymbol{\nu} = (\nu_1, \ldots, \nu_N)^\top$, with complementary slackness holding: $\nu_k w_k^* = 0$ for all $k = 1, \ldots, N$. [@SpecCompileResearch]

**Solution properties.** The incorporation of the normalization constraint transforms the NNLS problem into a constrained quadratic program on the simplex, restricting the feasible region from the entire non-negative orthant to the compact simplex. The solution $\mathbf{w}^* = (w_1^*, \ldots, w_N^*)^\top$ simultaneously satisfies non-negativity ($w_k^* \geq 0$), normalization ($\sum_{k=1}^N w_k^* = 1$), and prediction-error minimality over the simplex. The addition of the normalization constraint may modify the sparsity pattern relative to the unconstrained NNLS solution: the redistribution requirement may activate additional GMPEs, but sparse solutions with some $w_k^* = 0$ remain possible, enabling simultaneous calibration and implicit model selection. When one or more candidate GMPEs are eliminated ($w_k^* = 0$), the effective logic tree reduces to the subset of GMPEs with strictly positive weights. [@SpecCompileResearch][@eq-weight-norm]

**Connection to PSHA.** The calibrated weight vector $\mathbf{w}^*$ defines a proper discrete probability distribution over the $N$ candidate GMPE branches. The resulting mean hazard curve is computed as the weighted linear combination:

$$\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k^* \lambda_I^{(k)}(i^*),$$

consistent with the standard PSHA framework [@OpenQuakeEngine] and the logic-tree normalization condition [@eq-weight-norm]. The fully constrained formulation ensures that the calibrated weights are statistically optimal (minimizing prediction error over the evaluation points) and probabilistically valid (non-negative and summing to unity), fulfilling the dual requirements for defensible probability assignment in epistemic logic trees.
