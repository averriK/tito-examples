## SLOT 3: Epistemic Uncertainty and Ground-Motion Logic Trees

Epistemic uncertainty in PSHA refers to uncertainty arising from incomplete knowledge that is, in principle, reducible with additional data or modelling effort. In ground-motion modelling, this manifests as the inability to identify a single GMM as definitively correct for a given tectonic setting when the observational record is limited. A ground-motion logic tree provides a structured probabilistic representation of this uncertainty by enumerating a discrete set of mutually exclusive and collectively exhaustive model alternatives, each assigned a weight that reflects the analyst's degree of belief in that model given the available evidence [@PAG2022a][@PAG2022b].

In the ground-motion logic trees used in this assessment, each tree is defined for a specific tectonic region type (TRT) and comprises a single branching level with one branch set. Each branch specifies an alternative GMPE and is assigned a non-negative weight $w_k$ such that the normalization condition holds [@GmmLTASC][@GmmLTSCC][@GmmLTSIF][@GmmLTSIS]:

$$\sum_{k=1}^{N} w_k = 1, \qquad w_k \geq 0$$

where $N$ is the number of branches in the set. The weights define a discrete probability distribution over the space of candidate GMPEs. When all $N$ models are assigned equal weight, $w_k = 1/N$ for all $k$, the logic tree represents a state of maximum model uncertainty, assigning no prior preference to any individual GMPE relative to the others.

The logic tree is propagated through the PSHA computation by evaluating the hazard integral separately for each branch GMPE and computing a weighted combination of the resulting hazard curves. The mean hazard curve is the weighted average:

$$\bar{\lambda}(Y > y) = \sum_{k=1}^{N} w_k\, \lambda_k(Y > y)$$

where $\lambda_k(Y > y)$ is the mean annual exceedance rate computed with the $k$-th branch GMPE [@OpenQuakeEngine]. The full distribution over branches also permits the computation of fractile hazard curves at prescribed probability levels, which characterize the spread of hazard estimates arising from GMM epistemic uncertainty. This framework is the standard mechanism within the OpenQuake Engine for capturing model-to-model variability in ground-motion prediction.

The four tectonic region types covered in this assessment are Active Shallow Crust (ASC), Stable Continental Crust (SCC), Subduction Interface (SIF), and Subduction Intraslab (SIS). Each TRT is assigned its own independent logic tree, reflecting the physical differences in source mechanism, wave propagation path, and site response among crustal, stable continental, and subduction tectonic environments. Each logic tree is identified by a unique logic tree ID and a branch set ID as specified in the OpenQuake NRML input files. The per-TRT logic tree contents, GMPE identifiers, weights, and hazard library parameter requirements are detailed in the sections that follow [@GmmLTASC][@GmmLTSCC][@GmmLTSIF][@GmmLTSIS].
