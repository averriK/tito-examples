# Structured Prompt: Epistemic Logic Tree Weight Calibration

## CONTEXT

A research investigation addresses the calibration of weights in an epistemic logic tree combining multiple seismic ground-motion prediction models through a weighted sum. Ground Motion Models (GMMs) represent a principal source of epistemic uncertainty in Probabilistic Seismic Hazard Analysis (PSHA). The logic tree framework assigns non-negative weights $w_k$ to alternative candidate GMPEs, with normalization $\sum_{k=1}^{N} w_k = 1$. Different candidate GMPEs diverge substantially in their median predictions across engineering-relevant spectral periods, producing uncertainty bands on computed hazard curves. This uncertainty must be explicitly represented through a logic tree that samples the space of defensible model alternatives.

The weights define a discrete probability distribution over candidate GMPEs. When all $N$ models are assigned equal weight, the logic tree represents maximum model uncertainty. The logic tree is propagated through PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing weighted combinations of hazard curves. The mean hazard curve is the weighted average:

$$\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k \, \lambda_I^{(k)}(i^*)$$

where $\lambda_I^{(k)}(i^*)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE.

---

## SLOTS

### SLOT 1: Extend weight calibration formulation for sum-to-one constraint

Extend the formulation of the weight calibration problem to minimize prediction error under the constraint that the sum of weights must equal 1. Assume the same underlying hypotheses as existing formulations in kb/:

- Formulation as a generalization of a constrained linear regression problem
- Weights bounded and strictly greater than zero
- Final constraint that weights must sum to 1

Provide the complete mathematical formulation, including the optimization objective, all constraints, and discussion of how this differs from unconstrained or partially constrained weight optimization schemes.

**Coverage note**: Derived from line 24 of TASK_FILE. Requirement asks for extension of an existing formulation (referenced as "kb/") to incorporate the sum-to-one normalization constraint.

### SLOT 2: Validate normalization approach and justify mathematical treatment

Determine whether it is mathematically valid to take an existing positive-weight formulation from kb/*.md and simply normalize the resulting weights so that their sum equals 1, or whether this approach requires different mathematical treatment. Provide complete justification for the answer, including:

- Whether post-hoc normalization preserves the properties of the original optimization solution
- Whether this approach is equivalent to solving a constrained optimization problem directly
- Any mathematical conditions or assumptions under which normalization is or is not valid

**Coverage note**: Derived from line 27 of TASK_FILE. Requirement asks for validation of a specific normalization procedure and mathematical justification for the conclusions.

---

## CONSTRAINTS

- **Language**: All output must be in English with professional engineering and scientific methodology style.

---

## COVERAGE AND HALLUCINATION CHECK

- **SLOT 1 justification**: TASK_FILE line 24 explicitly requests extension of weight formulation with the hypotheses listed; this slot directly addresses that requirement without inversion or reordering.
- **SLOT 2 justification**: TASK_FILE line 27 explicitly asks whether normalization is valid and demands justification; this slot captures that question without invention.
- **Constraint justification**: TASK_FILE line 1 mandates English language and professional engineering methodology style.
- **No omissions**: All explicit work items in TASK_FILE are captured.
- **No duplicates**: SLOT 1 and SLOT 2 address distinct mathematical questions and are not rephrasings of each other.
