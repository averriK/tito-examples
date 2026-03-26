## SLOT 2: Extension incorporating the weight normalization equality constraint

The NNLS formulation minimizes prediction error subject to non-negativity but does not enforce that the calibrated weights define a proper discrete probability distribution over the $N$ GMPE branches. The logic-tree normalization condition [@eq-weight-norm] requires that branch weights sum to unity:

$$\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0, \quad k = 1, \ldots, N$$

In probabilistic seismic hazard analysis (PSHA), branch weights represent the relative probability assigned to each GMPE branch, and the mean hazard curve is computed as the weighted average of branch hazard curves [@eq-mean-hazard][@OpenQuakeEngine]. Enforcing normalization aligns the calibrated weights with this probabilistic framework and ensures that the weighted combination conforms to the standard logic-tree structure.

The complete weight calibration formulation incorporating both non-negativity bounds and the normalization equality constraint is:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N, \quad \text{and} \quad \sum_{k=1}^{N} w_k = 1$$

The feasible set is the intersection of the non-negative orthant with the hyperplane $\sum_{k=1}^{N} w_k = 1$, forming the $(N-1)$-dimensional probability simplex:

$$\Delta^{N-1} = \left\{\mathbf{w} \in \mathbb{R}^N : w_k \geq 0, \quad \sum_{k=1}^{N} w_k = 1\right\}$$

This simplex is a closed, convex, compact polytope representing all possible discrete probability distributions over the $N$ candidate GMPEs [@KBSpec]. Since the objective function is strictly convex (with Hessian $2\mathbf{A}^\top\mathbf{A}$ positive definite when $\mathbf{A}$ has full column rank) and the feasible set is a closed convex polytope, a unique global minimizer exists within the simplex [@KBSpec]. The addition of the normalization equality constraint modifies the solution relative to the inequality-only NNLS case: restricting the feasible region from the entire non-negative orthant to the simplex redistributes the weights so that they sum to exactly one, which may reduce the sparsity exhibited by the NNLS solution and may activate additional GMPEs in the final calibrated set [@KBSpec].

The optimal weight vector $\mathbf{w}^* = (w_1^*, \ldots, w_N^*)^\top$ simultaneously satisfies the non-negativity and normalization conditions while minimizing the prediction error over the simplex. The resulting mean hazard curve is computed as the weighted linear combination [@eq-mean-hazard][@OpenQuakeEngine]:

$$\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k^* \lambda_I^{(k)}(i^*)$$

consistent with the standard PSHA framework. The fully constrained formulation ensures that the calibrated weights are both statistically optimal -- minimizing the prediction error with respect to the calibration target -- and probabilistically valid, satisfying the non-negativity bounds and normalization condition that define a proper discrete probability distribution over the epistemic logic tree [@KBSpec].
