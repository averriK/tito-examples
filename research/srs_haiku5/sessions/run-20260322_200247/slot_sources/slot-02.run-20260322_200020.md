## SLOT 2: Extension incorporating the weight normalization equality constraint

The constrained optimization formulation developed in SLOT 1 enforces non-negativity but does not constrain the magnitude of the weight vector. The definition of a logic tree presented in the context [@eq-weight-norm] requires that the branch weights form a discrete probability distribution, satisfying the normalization condition $\sum_{k=1}^N w_k = 1$. This equality constraint ensures that the weighted combination of branch predictions appropriately represents the epistemic uncertainty by assigning a prior probability mass to each branch, with the sum of all probabilities equal to unity. [@OpenQuakeEngine]

^[Confidence: HIGH, Rationale: The motivation for the normalization constraint is directly stated in the task context, which defines the logic-tree normalization condition equation {#eq-weight-norm}. The connection to epistemic uncertainty and discrete probability distributions over GMPEs is consistent with the PSHA framework presented in the context.]

The complete constrained optimization problem for GMPE logic tree weight calibration combines both the non-negativity inequality constraints from SLOT 1 and the normalization equality constraint:

$$\min_{\mathbf{w} \in \mathbb{R}^N} \|\mathbf{A}\mathbf{w} - \mathbf{b}\|_2^2 \quad \text{subject to} \quad w_k \geq 0, \quad k = 1, \ldots, N, \quad \text{and} \quad \sum_{k=1}^N w_k = 1.$$

The feasible set is the $(N-1)$-simplex, a compact convex polytope defined as the intersection of the non-negative orthant with the affine hyperplane where weights sum to unity. The strictly convex quadratic objective combined with this convex feasible set guarantees a unique global minimiser $\mathbf{w}^*$. This formulation ensures that the calibrated weights define a proper discrete probability distribution over the space of candidate GMPEs, consistent with the logic-tree normalization requirement [@eq-weight-norm] and the epistemic uncertainty quantification framework in probabilistic seismic hazard assessment. [@OpenQuakeEngine]

^[Confidence: HIGH, Rationale: The extension from SLOT 1 by adding the equality constraint is mathematically sound and directly supports the logic-tree framework defined in the context. The feasible set (simplex) and its geometric properties are standard results in convex geometry. The connection to epistemic uncertainty quantification is consistent with the PSHA context provided in the task context.]

The constrained minimization problem on the simplex is a convex optimization problem admitting efficient solution through interior-point methods, active-set algorithms, or coordinate-descent schemes adapted for simplex constraints. The optimised weight vector $\mathbf{w}^*$ simultaneously minimises the prediction error across all evaluation scenarios while enforcing both the physical non-negativity requirement and the probabilistic normalization requirement mandated by the logic-tree structure. This fully constrained formulation completes the weight calibration framework, enabling the systematic determination of branch weights that balance fidelity to observed or target hazard predictions against the constraints imposed by the discrete probability distribution over candidate GMPEs.

^[Confidence: MEDIUM, Rationale: The mathematical formulation of the constrained problem on the simplex is correct and well-supported. The statement about solution algorithms is standard in convex optimization but not explicitly detailed in the available KB. The claim about 'observed or target hazard predictions' reflects the general framework but the specific nature of the target is not fully specified in the task context, warranting MEDIUM confidence rather than HIGH.]

---
