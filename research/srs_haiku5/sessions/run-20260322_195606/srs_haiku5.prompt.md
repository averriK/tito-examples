# Structured Prompt: Epistemic Logic-Tree Weight Calibration via Constrained Error Minimization

## CONTEXT

The overarching goal of this investigation is the formulation of a robust calibration framework for the weights of an epistemic logic tree that combines different ground-motion prediction equations (GMPEs) through a weighted sum whose weights must equal unity.
^[Confidence: HIGH, Rationale: Direct paraphrase of the TASK_FILE purpose statement (line 3). The original is in Spanish; the English rendering preserves the stated objective without additions.]

GMMs constitute one of the principal contributors to epistemic uncertainty in PSHA, alongside source model components such as fault geometry, seismicity rates, and magnitude-frequency distributions. Epistemic uncertainty, as distinct from aleatory variability, represents incomplete scientific knowledge of the true ground-motion process; it is in principle reducible with additional data and is represented in PSHA by a discrete set of alternative models. Different GMPEs are constructed from distinct datasets, adopt distinct functional forms, and encode distinct assumptions about source scaling, geometric spreading, anelastic attenuation, and site amplification. In regions where observational strong-motion data are sparse, the median predictions of plausible candidate GMPEs can diverge substantially across engineering-relevant spectral periods and magnitude-distance ranges, producing a wide spread of hazard curves. The spread among GMM predictions at low annual exceedance rates is frequently the dominant contributor to the epistemic uncertainty band on the hazard curve. Because this uncertainty cannot be reduced without additional observational constraints, it must be explicitly represented in the hazard model through a logic tree that samples the space of defensible model alternatives.
^[Confidence: HIGH, Rationale: Reproduced from TASK_FILE (lines 5-6). Restates domain background on GMMs and epistemic uncertainty in PSHA without additions or omissions.]

In the ground-motion logic trees used in this assessment, each tree is defined for a specific tectonic region type (TRT) and comprises a single branching level with one branch set. Each branch specifies an alternative GMPE and is assigned a non-negative weight $w_k$ such that the normalization condition holds [@eq-weight-norm]:
^[Confidence: HIGH, Rationale: Reproduced from TASK_FILE (lines 7-10). Introduces the weight normalization framework as given in the original.]

$$
\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0
$${#eq-weight-norm}

where $N$ is the number of branches in the set. The weights define a discrete probability distribution over the space of candidate GMPEs. When all $N$ models are assigned equal weight, $w_k = 1/N$ for all $k$, the logic tree represents a state of maximum model uncertainty, assigning no prior preference to any individual GMPE relative to the others.
^[Confidence: HIGH, Rationale: Reproduced from TASK_FILE (line 13). Defines the equal-weight baseline case as stated in the original.]

The logic tree is propagated through the PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing a weighted combination of the resulting hazard curves. The mean hazard curve is the weighted average [@eq-mean-hazard]:
^[Confidence: HIGH, Rationale: Reproduced from TASK_FILE (lines 15-16). Introduces the mean hazard computation framework.]

$$
\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k\, \lambda_I^{(k)}(i^*)
$${#eq-mean-hazard}

where $\lambda_I^{(k)}(i^*)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE [@OpenQuakeEngine]. The full distribution over branches also permits the computation of fractile hazard curves at prescribed probability levels, which characterize the spread of hazard estimates arising from GMM epistemic uncertainty. This framework is the standard mechanism within the OpenQuake Engine for capturing model-to-model variability in ground-motion prediction.
^[Confidence: HIGH, Rationale: Reproduced from TASK_FILE (lines 18-21). Describes the mean hazard computation and the OpenQuake framework reference as given in the original.]

## SLOTS

### SLOT 1: Constrained linear regression formulation of the weight calibration error minimization problem

The existing error minimization formulation in the knowledge base (kb/) defines an objective function that minimizes prediction error with decision variables $w_k$ representing branch weights. This slot requires formalizing that problem as a generalization of a constrained linear regression problem, retaining the same hypotheses as the kb/ formulation. The optimization must include non-negativity bound constraints $w_k \geq 0$ for all $k = 1, \ldots, N$, casting the weight vector as the regression coefficient vector subject to inequality bounds. This formulation establishes the mathematical foundation - objective function, decision variables, and inequality constraints - upon which the normalization extension in SLOT 2 is built.
^[Confidence: HIGH, Rationale: Directly justified by TASK_FILE (lines 24-25): "Extiende la formulacion del problema de minimizar el error presente en kb/... Asume las mismas hipotesis: la formulacion como generalizacion de un problema de regresion lineal condicionado, con pesos acotados mayores que cero." This slot covers the base formulation requirements without introducing objectives beyond those stated in the task.]

### SLOT 2: Extension incorporating the weight normalization equality constraint

The constrained optimization formulation from SLOT 1 is to be extended by incorporating the equality constraint $\sum_{k=1}^{N} w_k = 1$ as the final derivation step. The complete formulation must simultaneously enforce non-negativity bounds ($w_k \geq 0$) and weight normalization ($\sum w_k = 1$), yielding a fully constrained optimization problem. This extension relative to the existing kb/ formulation ensures that the calibrated weights define a proper discrete probability distribution over the candidate GMPEs, consistent with the logic-tree normalization condition [@eq-weight-norm].
^[Confidence: HIGH, Rationale: Directly justified by TASK_FILE (lines 24-25): "Extiende la formulacion... para el caso en que la suma de los pesos debe ser igual a 1... con el paso final en donde los pesos deben sumar 1." This slot addresses the explicit extension request without fabricating additional requirements. The link to the normalization condition is supported by TASK_FILE (lines 7-13).]

## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology, with impersonal academic voice.
- Mathematical notation must remain consistent with the symbols defined in the context ($w_k$, $N$, $\lambda_I^{(k)}(i^*)$, $\bar{\lambda}_I(i^*)$); inline math uses $...$ and display math uses $$...$$ in LaTeX format.
- All existing citation tokens (e.g., [@OpenQuakeEngine]) and cross-reference labels (e.g., [@eq-weight-norm], {#eq-weight-norm}) are to be preserved in downstream outputs.
^[Confidence: HIGH, Rationale: The language and style constraints derive from TASK_FILE line 1: "DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)." Mathematical notation and citation preservation constraints follow from the notation used throughout TASK_FILE and FORMAT_RULES requirements. No invented constraints appear.]
