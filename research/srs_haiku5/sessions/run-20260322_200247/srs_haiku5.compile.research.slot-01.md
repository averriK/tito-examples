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

The constrained minimization may be solved via the active-set method of Lawson and Hanson, which partitions the index set $\{1, \ldots, N\}$ into an active set (indices where $w_k = 0$) and a passive set (indices where the weight is strictly positive), iteratively solving unconstrained OLS sub-problems on the passive set and updating the partition until the Karush-Kuhn-Tucker (KKT) optimality conditions are satisfied. This formulation establishes the mathematical foundation---objective function, decision variables, and inequality constraints---upon which the weight normalization extension in SLOT 2 is constructed. [@SpecCompileResearch]
