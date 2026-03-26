# Structured Prompt: Constrained Weight Calibration for Epistemic Logic Trees

## CONTEXT

The overarching research objective is to formulate a robust framework for calibrating the weights of an epistemic logic tree that combines different seismic ground-motion prediction models through a weighted sum whose weights satisfy normalization.


Ground-motion models (GMMs) constitute a principal source of epistemic uncertainty in probabilistic seismic hazard analysis (PSHA), alongside source model components such as fault geometry, seismicity rates, and magnitude-frequency distributions. Epistemic uncertainty represents incomplete scientific knowledge of the true ground-motion process and is represented in PSHA by a discrete set of alternative models within a logic tree. Different ground-motion prediction equations (GMPEs) are constructed from distinct datasets, adopt distinct functional forms, and encode distinct assumptions about source scaling, geometric spreading, anelastic attenuation, and site amplification. The spread among GMM predictions at low annual exceedance rates frequently constitutes the dominant contributor to the epistemic uncertainty band on the hazard curve.


In the ground-motion logic trees used in this assessment, each tree is defined for a specific tectonic region type (TRT) and comprises a single branching level with one branch set. Each branch specifies an alternative GMPE and is assigned a non-negative weight $w_k$ satisfying the normalization condition [@eq-weight-norm]:


$$
\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0
$${#eq-weight-norm}

where $N$ is the number of branches in the set. Equal weights $w_k = 1/N$ represent a state of maximum model uncertainty, assigning no prior preference to any individual GMPE relative to the others.


The logic tree is propagated through the PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing a weighted combination. The mean hazard curve is the weighted average [@eq-mean-hazard]:


$$
\bar{\lambda}_I(i^*) = \sum_{k=1}^{N} w_k\, \lambda_I^{(k)}(i^*)
$${#eq-mean-hazard}

where $\lambda_I^{(k)}(i^*)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE [@OpenQuakeEngine]. The full distribution over branches also permits the computation of fractile hazard curves at prescribed probability levels, characterizing the spread of hazard estimates arising from GMM epistemic uncertainty.


## SLOTS

### SLOT 1: Extension of the error minimization formulation with sum-to-one weight constraint

Extend the error minimization problem formulation present in the knowledge base (`kb/`) to the case in which the logic tree weights must satisfy the normalization constraint $\sum_{k=1}^{N} w_k = 1$. The derivation assumes the following hypotheses:


- The formulation constitutes a generalization of a constrained linear regression problem.
- All weights are bounded to be strictly greater than zero: $w_k > 0$ for all $k$.
- The final derivation step imposes the unity sum constraint $\sum_{k=1}^{N} w_k = 1$ on the weight vector.


The extension builds upon the existing error minimization formulation in `kb/` and maintains consistency with the epistemic logic tree framework for PSHA ground-motion models described in the context section, including the weight normalization condition [@eq-weight-norm] and the mean hazard curve formulation [@eq-mean-hazard].


*Coverage: This slot corresponds to the single explicit question in TASK_FILE (line 24). All sub-conditions specified in the question - constrained regression generalization, strict positivity bounds, and unity sum constraint as the final step - are addressed. No requirements from TASK_FILE remain unaccounted for.*

## CONSTRAINTS

- Output language: English.
- Document style: professional engineering methodology, with an impersonal academic voice suitable for a technical audience in seismic hazard analysis.
- Mathematical notation: LaTeX format using `$...$` for inline expressions and `$$...$$` for display equations, consistent with the notation established in the context ($w_k$, $N$, $\lambda_I^{(k)}$, $\bar{\lambda}_I$).

