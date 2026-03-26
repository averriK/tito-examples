# Constrained Weight Calibration for Epistemic Logic Trees in PSHA

## CONTEXT

The overarching research objective is the formulation of a robust framework for calibrating the branch weights of an epistemic logic tree that combines multiple ground-motion prediction models through a weighted sum whose weights satisfy the normalization condition $\sum w_k = 1$.

Ground-motion models (GMMs) constitute a principal source of epistemic uncertainty in probabilistic seismic hazard assessment (PSHA), alongside source model components such as fault geometry, seismicity rates, and magnitude-frequency distributions. Epistemic uncertainty, as distinct from aleatory variability, represents incomplete scientific knowledge of the true ground-motion process; it is in principle reducible with additional data and is represented in PSHA by a discrete set of alternative models. Different GMPEs are constructed from distinct datasets, adopt distinct functional forms, and encode distinct assumptions about source scaling, geometric spreading, anelastic attenuation, and site amplification. In regions where observational strong-motion data are sparse, the median predictions of plausible candidate GMPEs can diverge substantially across engineering-relevant spectral periods and magnitude-distance ranges, producing a wide spread of hazard curves. The spread among GMM predictions at low annual exceedance rates is frequently the dominant contributor to the epistemic uncertainty band on the hazard curve. Because this uncertainty cannot be reduced without additional observational constraints, it must be explicitly represented in the hazard model through a logic tree that samples the space of defensible model alternatives.

In the ground-motion logic trees used in this assessment, each tree is defined for a specific tectonic region type (TRT) and comprises a single branching level with one branch set. Each branch specifies an alternative GMPE and is assigned a non-negative weight $w_k$ such that the normalization condition holds:

$$
\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0
$$

where $N$ is the number of branches in the set. The weights define a discrete probability distribution over the space of candidate GMPEs. When all $N$ models are assigned equal weight, $w_k = 1/N$ for all $k$, the logic tree represents a state of maximum model uncertainty, assigning no prior preference to any individual GMPE relative to the others.

The logic tree is propagated through the PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing a weighted combination of the resulting hazard curves. The mean hazard curve is the weighted average:

$$
\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k\, \lambda_I^{(k)}(i^*)
$$

where $\lambda_I^{(k)}(i^*)$ denotes the mean annual exceedance rate computed with the $k$-th branch GMPE. The full distribution over branches also permits the computation of fractile hazard curves at prescribed probability levels, which characterize the spread of hazard estimates arising from GMM epistemic uncertainty. This framework is the standard mechanism within the OpenQuake Engine for capturing model-to-model variability in ground-motion prediction.

## SLOTS

### SLOT 1: Extension of the error minimization formulation with unit-sum weight constraint

The error minimization problem formulated in the knowledge base (kb/) is to be extended to the case where the logic-tree branch weights satisfy the normalization condition $\sum_{k=1}^{N} w_k = 1$. The extended formulation adopts the following hypotheses, carried over from the KB formulation:

- The problem is cast as a generalization of a constrained linear regression problem.
- All weights are bounded below by zero: $w_k \geq 0$ for all $k = 1, \ldots, N$.
- The final derivation step incorporates the unit-sum constraint $\sum_{k=1}^{N} w_k = 1$ as an additional equality condition on the optimization.



The formulation builds upon the existing KB error minimization framework and extends it to the fully constrained optimization problem enforcing both non-negativity and normalization simultaneously.

**Coverage**: This slot addresses the sole explicit question in TASK_FILE (lines 24-25), which requests extending the KB error minimization formulation to the unit-sum case under the three stated hypotheses. No sub-requirements from the question are omitted, and no additional objectives are introduced.

## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology.

**Coverage**: Both constraints derive from the directive on line 1 of TASK_FILE. No additional global constraints are present in the task.

## COVERAGE SUMMARY

All explicit requirements in TASK_FILE are accounted for in this structured prompt:

- The purpose statement (line 3) and technical context (lines 5-21) are reflected in the CONTEXT section, providing the domain background that downstream workflows require.
- The sole explicit question (lines 24-25) is captured in SLOT 1 with all three stated hypotheses preserved.
- The global language and style directives (line 1) are captured in the CONSTRAINTS section.
- No requirements from TASK_FILE remain uncovered, and no slots or constraints have been introduced without explicit justification from TASK_FILE.
