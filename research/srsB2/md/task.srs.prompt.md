# Structured Prompt: Epistemic Logic-Tree Weight Calibration Under Unit-Sum Constraint

## CONTEXT

The research objective is to formulate a robust calibration framework for the weights of an epistemic logic tree that combines different seismic ground-motion prediction models through a weighted sum subject to a unit-sum normalization constraint.

GMMs constitute one of the principal contributors to epistemic uncertainty in PSHA, alongside source model components such as fault geometry, seismicity rates, and magnitude-frequency distributions. Epistemic uncertainty, as distinct from aleatory variability, represents incomplete scientific knowledge of the true ground-motion process; it is in principle reducible with additional data and is represented in PSHA by a discrete set of alternative models. Different GMPEs are constructed from distinct datasets, adopt distinct functional forms, and encode distinct assumptions about source scaling, geometric spreading, anelastic attenuation, and site amplification. In regions where observational strong-motion data are sparse, the median predictions of plausible candidate GMPEs can diverge substantially across engineering-relevant spectral periods and magnitude-distance ranges, producing a wide spread of hazard curves. The spread among GMM predictions at low annual exceedance rates is frequently the dominant contributor to the epistemic uncertainty band on the hazard curve. Because this uncertainty cannot be reduced without additional observational constraints, it must be explicitly represented in the hazard model through a logic tree that samples the space of defensible model alternatives.

In the ground-motion logic trees used in this assessment, each tree is defined for a specific tectonic region type (TRT) and comprises a single branching level with one branch set. Each branch specifies an alternative GMPE and is assigned a non-negative weight $w_k$ such that the normalization condition holds [@eq-weight-norm]:

$$
\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0
$${#eq-weight-norm}

where $N$ is the number of branches in the set. The weights define a discrete probability distribution over the space of candidate GMPEs. When all $N$ models are assigned equal weight, $w_k = 1/N$ for all $k$, the logic tree represents a state of maximum model uncertainty, assigning no prior preference to any individual GMPE relative to the others.

The logic tree is propagated through the PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing a weighted combination of the resulting hazard curves. The mean hazard curve is the weighted average [@eq-mean-hazard]:

$$
\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k\, \lambda_I^{(k)}(i^*)
$${#eq-mean-hazard}

where $\lambda_I^{(k)}(i^*)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE [@OpenQuakeEngine]. The full distribution over branches also permits the computation of fractile hazard curves at prescribed probability levels, which characterize the spread of hazard estimates arising from GMM epistemic uncertainty. This framework is the standard mechanism within the OpenQuake Engine for capturing model-to-model variability in ground-motion prediction.

## SLOTS

### SLOT 1: Extension of the error-minimization formulation to the unit-sum constraint

The weight-calibration error-minimization problem formulated in the knowledge base (kb/) addresses the case of non-negative weight bounds only. This slot covers the extension of that formulation to incorporate the additional equality constraint that the weights must sum to one ($\sum_{k=1}^{N} w_k = 1$). The same working hypotheses apply: the problem is cast as a generalization of a constrained linear regression problem, the weights are bounded to be non-negative ($w_k \geq 0$), and the unit-sum normalization is imposed as the final constraining step.

### SLOT 2: Validity of post-hoc normalization versus direct constrained optimization

The knowledge base (kb/) formulation yields a set of non-negative weights without enforcing that they sum to one. This slot covers a rigorous assessment of whether it is mathematically valid to obtain those weights and then normalize them post-hoc - dividing each by $\sum_k w_k$ - to satisfy the unit-sum condition, or whether the normalization constraint changes the structure of the optimization problem in a way that demands a fundamentally different mathematical treatment. A formal justification is required.

## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology, impersonal academic voice.
