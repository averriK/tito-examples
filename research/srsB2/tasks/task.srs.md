DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)

El propósito de esta investigación es formular un marco robusto de calibración de pesos de un árbol lógico epistémico que combina diferentes modelos de predicción del movimiento sísmico mediante una suma ponderada cuyos pesos deben dar 1

GMMs constitute one of the principal contributors to epistemic uncertainty in PSHA, alongside source model components such as fault geometry, seismicity rates, and magnitude-frequency distributions. Epistemic uncertainty, as distinct from aleatory variability, represents incomplete scientific knowledge of the true ground-motion process; it is in principle reducible with additional data and is represented in PSHA by a discrete set of alternative models. Different GMPEs are constructed from distinct datasets, adopt distinct functional forms, and encode distinct assumptions about source scaling, geometric spreading, anelastic attenuation, and site amplification. In regions where observational strong-motion data are sparse, the median predictions of plausible candidate GMPEs can diverge substantially across engineering-relevant spectral periods and magnitude-distance ranges, producing a wide spread of hazard curves. The spread among GMM predictions at low annual exceedance rates is frequently the dominant contributor to the epistemic uncertainty band on the hazard curve . Because this uncertainty cannot be reduced without additional observational constraints, it must be explicitly represented in the hazard model through a logic tree that samples the space of defensible model alternatives.

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


Pregunta: Extiende la formulación del problema de minimizar el error presente en kb/ para el caso en que la suma de los pesos debe ser igual a 1. Asume las mismas hipótesis: la formulación como generalización de un problema de regresión lineal condicionado, con pesos acotados mayores que cero, con el paso final en donde los pesos deben sumar 1. 


PREGUNTA: ¿es valido tomar la formulacion de kb/*.md de pesos positivos y simplemente normalizar la suma de pesos a uno? o este set de pesos requiere un tratamiento matematico diferente? justifica  