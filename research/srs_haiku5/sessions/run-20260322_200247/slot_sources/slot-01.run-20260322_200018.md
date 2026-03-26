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

