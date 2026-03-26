## SLOT 1: Constrained linear regression formulation of the weight calibration error minimization problem

The weight calibration problem for epistemic ground-motion logic trees is formalized as a constrained linear regression problem in which the decision variables $w_k$ represent the branch weights assigned to each of the $N$ candidate ground-motion prediction equations (GMPEs). The objective is to determine non-negative weights that minimize the prediction error between the weighted combination of candidate GMPE predictions and a calibration target, extending classical ordinary least-squares regression by introducing inequality constraints that enforce the physical requirement of non-negative weights [@KBSpec].

The design matrix $\mathbf{A} \in \mathbb{R}^{n \times N}$ is constructed such that entry $A_{ik}$ denotes the prediction from GMPE $k$ at evaluation point $i$. Each column of $\mathbf{A}$ contains the predictions from a single candidate GMPE across all $n$ evaluation points, and each row contains the predictions of all $N$ candidate GMPEs at a single evaluation point. The calibration target vector $\mathbf{y} \in \mathbb{R}^n$ contains the reference values against which the weighted combination $\hat{\mathbf{y}} = \mathbf{A}\mathbf{w}$ is matched, where $\mathbf{w} = (w_1, w_2, \ldots, w_N)^\top$ is the weight vector to be determined [@KBSpec].

The prediction error is measured as the squared Euclidean distance between the weighted prediction and the calibration target. The objective function minimizes the residual sum of squares:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2$$

This objective is a strictly convex quadratic function of $\mathbf{w}$ with Hessian $2\mathbf{A}^\top\mathbf{A}$, which is positive semidefinite and becomes positive definite when $\mathbf{A}$ has full column rank [@KBSpec].

Physical plausibility requires that all weights satisfy $w_k \geq 0$ for $k = 1, \ldots, N$. A negative weight $w_k < 0$ would imply subtracting a weighted contribution from candidate GMPE $k$ in the combined prediction, which would require the existence of an anti-GMPE with negated predictions -- a construct with no physical foundation in seismic hazard assessment. No such anti-GMPE exists in any defensible collection of ground-motion models. Enforcing $w_k \geq 0$ ensures that the calibrated weights represent physically meaningful, non-negative contributions from each branch GMPE to the ensemble prediction. A practical consequence of the non-negativity constraint is that the optimal solution is frequently sparse: many weights attain exactly zero at the optimum, automatically performing simultaneous model selection and weight assignment [@KBSpec].

The complete constrained formulation is the non-negative least-squares (NNLS) problem:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N$$

The feasible set is the non-negative orthant, a closed convex cone in $\mathbb{R}^N$. The combination of a strictly convex objective and a convex feasible set guarantees a unique global minimizer when $\text{rank}(\mathbf{A}) = N$, a condition requiring $n \geq N$ and linear independence of the candidate GMPE prediction vectors; this minimizer is computable via active-set algorithms in polynomial time [@KBSpec]. This formulation establishes the mathematical foundation for constrained weight calibration and provides the optimization structure upon which the normalization equality constraint is imposed in the extension that follows.
