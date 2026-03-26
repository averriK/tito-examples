## SLOT 1: Constrained linear regression formulation of the weight calibration error minimization problem

The weight calibration problem is formalized as a constrained linear regression problem in which the objective is to minimize the prediction error of a weighted linear combination of GMPE predictions. The design matrix $\mathbf{A} \in \mathbb{R}^{n \times N}$ contains the predicted mean annual exceedance rates from each of the $N$ candidate GMPEs evaluated at $n$ discrete hazard points; entry $A_{ik}$ denotes the prediction from GMPE $k$ at evaluation point $i$. [KB:spec.compile.research.md] The target vector $\mathbf{y} \in \mathbb{R}^n$ represents the reference hazard curve or conditional hazard target that the weighted combination should approximate. The weighted linear combination of GMPE predictions is $\hat{\mathbf{y}} = \mathbf{A}\mathbf{w}$, where $\mathbf{w} = (w_1, \ldots, w_N)^{\top}$ is the weight vector to be determined. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The matrix formulation is directly adapted from the classical regression framework in KB:spec.compile.research.md (SLOT 3), with column vectors representing individual GMPEs and row vectors representing evaluation points. The correspondence between the spectral-matching design matrix and the GMPE prediction matrix is structurally identical.]

The error minimization objective is the residual sum of squares, the sum of squared deviations between the weighted prediction and the target across all evaluation points:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2$$

This is a strictly convex quadratic objective function in $\mathbf{w}$. [KB:spec.compile.research.md] Minimizing this objective recovers the weight vector that best fits the target hazard curve in the least-squares sense.

^[Confidence: HIGH, Rationale: The quadratic objective and its convexity are standard properties of least-squares regression, explicitly established in KB:spec.compile.research.md (SLOT 3). The objective structure is preserved in translation from spectral matching to hazard prediction.]

Physical plausibility requires that all weights be non-negative, $w_k \geq 0$ for $k = 1, \ldots, N$, because each weight represents the relative probability or importance of a GMPE branch within the logic tree. Negative weights would imply that an increase in a GMPE's predicted hazard should decrease the weighted combination, contradicting the basic probabilistic structure of the logic tree. [KB:spec.compile.research.md] Non-negativity ensures that the solution is physically meaningful and can be interpreted as a discrete probability distribution.

^[Confidence: HIGH, Rationale: The justification for non-negativity constraints is provided in KB:spec.compile.research.md (SLOT 5), which establishes that negative weights lack physical interpretation. This reasoning applies identically to GMPE weight assignment, where weights must represent non-negative probabilities or importance measures.]

The complete constrained formulation is:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N$$

This is the non-negative least-squares (NNLS) problem, a convex quadratic program with linear inequality constraints. [KB:spec.compile.research.md] When $\mathbf{A}$ has full column rank, the NNLS problem admits a unique global minimizer that can be computed via active-set algorithms in polynomial time. [KB:spec.compile.research.md] This formulation establishes the mathematical foundation for constrained weight calibration and provides the optimization structure upon which the normalization constraint in SLOT 2 is imposed.

^[Confidence: HIGH, Rationale: The NNLS problem structure, uniqueness conditions, and algorithmic properties are comprehensively developed in KB:spec.compile.research.md (SLOT 5), including discussion of the active-set method and the requirement of full column rank. These theoretical results apply directly to the GMPE weight calibration context. The task explicitly requires this formulation as the basis for SLOT 2.]

## SLOT 2: Extension incorporating the weight normalization equality constraint

The NNLS formulation of SLOT 1 minimizes prediction error subject to non-negativity but does not enforce that weights sum to unity. The condition $\sum_{k=1}^{N} w_k = 1$ is required to ensure that the weights define a proper discrete probability distribution over the $N$ GMPE branches, consistent with the logic-tree normalization requirement stated in the context [@eq-weight-norm]. In PSHA, the weights represent the relative probability assigned to each branch, and the mean hazard curve is computed as the weighted average of branch hazard curves [@eq-mean-hazard][@OpenQuakeEngine]. Enforcing normalization aligns the calibrated weights with this probabilistic framework and ensures that the weighted combination conforms to the standard logic-tree structure.

^[Confidence: HIGH, Rationale: The normalization constraint is explicitly defined in the task context with the cross-reference [@eq-weight-norm], establishing its necessity for probabilistic consistency. The task context also specifies that the mean hazard is computed as a weighted sum [@eq-mean-hazard][@OpenQuakeEngine], which requires normalized weights. The mathematical requirement for weights to sum to unity is fundamental to discrete probability distributions.]

The complete constrained optimization problem incorporating both non-negativity bounds and normalization is:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \left\|\mathbf{A}\mathbf{w} - \mathbf{y}\right\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N, \quad \text{and} \quad \sum_{k=1}^{N} w_k = 1$$

This is a constrained convex quadratic program with $N$ linear inequality constraints and one linear equality constraint. The feasible region is the probability simplex $\left\{\mathbf{w} \in \mathbb{R}^N : w_k \geq 0, \sum_{k=1}^{N} w_k = 1\right\}$, a closed convex polytope. [KB:spec.compile.research.md]

^[Confidence: HIGH, Rationale: The structure of quadratic programs with mixed equality and inequality constraints is established in optimization theory and is illustrated in KB:spec.compile.research.md (SLOT 6 and SLOT 7) through the treatment of bounded-weight problems with multiple constraints. The probability simplex is a standard geometric object in probability theory.]

Since the objective is strictly convex (with Hessian $2\mathbf{A}^{\top}\mathbf{A}$ positive definite when $\mathbf{A}$ has full column rank) and the feasible set is a closed convex polytope, a unique global minimizer exists. [KB:spec.compile.research.md] The addition of the equality constraint modifies the solution relative to the unconstrained NNLS problem. The normalization requirement redistributes the weights so that they sum to exactly one, which may eliminate some of the sparsity exhibited by the NNLS solution (where many weights are exactly zero) and may activate additional GMPEs in the final calibrated set.

^[Confidence: HIGH, Rationale: The convexity argument is standard in optimization theory and explicitly developed in KB:spec.compile.research.md. The effect of adding equality constraints to least-squares problems is a well-understood phenomenon in constrained optimization; adding a constraint to a least-squares feasible region can change the sparsity pattern and alter which variables are active at the optimum.]

The final calibrated weight vector $\mathbf{w}^* = (w_1^*, \ldots, w_N^*)^{\top}$ simultaneously satisfies the non-negativity and normalization constraints while minimizing the prediction error over the simplex. These weights define the discrete probability distribution over the candidate GMPE branches, and the resulting mean hazard curve is computed as the weighted linear combination $\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k^* \lambda_I^{(k)}(i^*)$, consistent with the standard PSHA framework [@eq-mean-hazard][@OpenQuakeEngine]. The fully constrained formulation ensures that the calibrated weights are statistically optimal (minimizing prediction error) and probabilistically valid (non-negative and normalized), fulfilling the dual requirements for proper probability assignment in epistemic logic trees.

^[Confidence: HIGH, Rationale: The connection between the constrained optimization solution and the PSHA mean hazard computation is established in the task context, which defines both the constraints and the hazard formula. The cited cross-references ([@eq-mean-hazard], [@OpenQuakeEngine]) are preserved from the task context. The characterization of the solution as both statistically and probabilistically valid is consistent with the objectives stated in the task.]
