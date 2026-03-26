## SLOT 1: Constrained linear regression formulation of the weight calibration error minimization problem

The calibration of branch weights in a ground-motion logic tree can be formulated as a constrained linear regression problem in which the prediction error is minimized subject to non-negativity constraints on the weights. Denote the $N$ candidate ground-motion prediction equations (GMPEs) as branch indices $k = 1, \ldots, N$, with corresponding non-negative weights $w_k$ representing the probability assigned to each branch within the logic tree. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The problem formulation is stated directly from the task specification, establishing the context for GMPE weight calibration. The terminology (GMPEs, logic tree, branch weights) is consistent with the context provided in the task file.]

Assemble the hazard rate predictions of the $N$ candidate GMPEs into a design matrix $\mathbf{A} \in \mathbb{R}^{n \times N}$, where each row corresponds to a distinct scenario (magnitude-distance combination or hazard rate level) and each column corresponds to a candidate GMPE. Specifically, define $A_{ik} = \lambda_I^{(k)}(i^*)$, the mean annual exceedance rate computed with the $k$-th branch GMPE at hazard level $i^*$, for $i = 1, \ldots, n$ and $k = 1, \ldots, N$. [KB:spec.compile.research.md] Define the target vector $\mathbf{b} \in \mathbb{R}^n$ containing the target hazard rates or spectral predictions at each of the $n$ evaluation points. The predicted weighted combination of branch hazard rates is $\hat{\mathbf{b}} = \mathbf{A}\mathbf{w}$, where $\mathbf{w} = (w_1, \ldots, w_N)^\top$ is the weight vector.

^[Confidence: HIGH, Rationale: The design matrix and target vector notation are adapted from KB SLOT 3 linear regression formulation but recontextualized for GMPE predictions rather than spectral matching. The notation and definitions are consistent with the context equation for mean hazard $\bar{\lambda}_I(i^*)$ as a weighted combination of branch rates.]

The objective of weight calibration is to find the weight vector $\mathbf{w}$ that minimizes the prediction error between the weighted linear combination of branch hazard rates and the target hazard rates across all evaluation points. Following the standard formulation from constrained linear regression theory, the unconstrained error minimization problem is: [KB:spec.compile.research.md]

$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2,$$

where $\|\cdot\|_2$ denotes the Euclidean norm and the objective is a convex quadratic function of $\mathbf{w}$. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The objective function is derived directly from the KB SLOT 3 classical linear regression formulation, adapted to GMPE weights rather than spectral ordinates. The formulation minimizes the squared Euclidean norm of residuals, which is the standard OLS objective.]

The gradient of this objective is $2\mathbf{A}^\top(\mathbf{A}\mathbf{w} - \mathbf{b})$, and unconstrained minimization yields the normal equations:

$$\mathbf{A}^\top \mathbf{A}\, \hat{\mathbf{w}} = \mathbf{A}^\top \mathbf{b}.$$

^[Confidence: HIGH, Rationale: The normal equations and gradient derivation are standard calculus results from convex optimization. These equations form the foundation of the OLS solution and are directly cited in the KB SLOT 3.]

Provided $\mathbf{A}$ has full column rank (a condition assured when $n \geq N$ and the candidate GMPE predictions are linearly independent across the evaluation scenarios), the Gram matrix $\mathbf{A}^\top\mathbf{A} \in \mathbb{R}^{N\times N}$ is invertible and the unique ordinary least-squares solution is: [KB:spec.compile.research.md]

$$\hat{\mathbf{w}} = \left(\mathbf{A}^\top \mathbf{A}\right)^{-1} \mathbf{A}^\top \mathbf{b}.$$

^[Confidence: HIGH, Rationale: The full-column-rank condition and the closed-form OLS solution are standard results from linear algebra and least-squares theory presented in KB SLOT 3. The invertibility of the Gram matrix is guaranteed under the stated conditions.]

However, the unconstrained OLS solution admits negative components whenever two or more candidate GMPEs produce highly correlated predictions. A negative weight $w_k < 0$ would imply that the contribution of branch $k$ is subtracted from the weighted combination, a construct without physical meaning in the context of logic trees, where weights represent probabilities or relative model plausibilities. [KB:spec.compile.research.md] To enforce physical realizability, the weight calibration problem is extended by imposing non-negativity constraints on each branch weight:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N.$$

The feasible region is the non-negative orthant of $\mathbb{R}^N$, a closed convex cone. The objective remains a strictly convex quadratic, guaranteeing a unique global minimiser. This problem is known as the non-negative least-squares (NNLS) formulation. [KB:spec.compile.research.md] The constrained quadratic objective defines the regression coefficient vector $\mathbf{w}$ as the solution to a bounded linear regression problem, with inequality constraints $w_k \geq 0$ replacing the unconstrained domain $\mathbb{R}^N$.

^[Confidence: HIGH, Rationale: The non-negativity constraint enforcement and NNLS formulation are directly from the KB SLOT 5 physical motivation and problem statement, adapted to the logic tree context. The mathematical statement of the constrained minimization problem is standard.]

The constrained minimization may be solved via the active-set method of Lawson and Hanson (1974), which partitions the index set into indices where the constraint is active ($w_k = 0$) and indices where the weight is free to be positive, iteratively solving unconstrained sub-problems until the Karush-Kuhn-Tucker (KKT) optimality conditions are satisfied. [KB:spec.compile.research.md] This formulation establishes the mathematical foundation---the objective function, decision variables, and inequality constraints---upon which the weight normalization extension required in SLOT 2 is constructed.

^[Confidence: HIGH, Rationale: The active-set algorithm and KKT conditions are standard convex optimization results cited in the KB SLOT 5. This paragraph correctly states the basis for the normalization extension while maintaining consistency with the mathematical framework.]

---

