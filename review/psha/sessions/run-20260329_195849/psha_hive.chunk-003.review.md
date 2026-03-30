---
reference-location: section
link-citations: true                   # make in-text cites clickable
---


Probabilistic seismic hazard analysis (PSHA) aggregates the contributions of all plausible earthquake scenarios, obscuring the specific combinations of magnitude ($M$), source-to-site distance ($R$), and ground-motion residual ($\varepsilon$) that control site hazard. **Hazard disaggregation** quantifies the relative contribution of each scenario class—binned by magnitude $m_k$, distance $r_j$, and residual $\varepsilon_\ell$—to the annual frequency of exceedance at a specified ground-motion threshold $i^*$ [@Bazzurro1999].
^[Confidence: HIGH, Rationale: The description of PSHA disaggregation as a method for quantifying the contributions of scenarios binned by magnitude, distance, and epsilon to the hazard at a specified ground-motion threshold is an accurate characterisation of the methodology introduced by Bazzurro and Cornell (1999), confirmed by the published paper in the Bulletin of the Seismological Society of America [WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard]. The notation ($M$, $R$, $\varepsilon$) and the concept of binning by these three parameters are standard in the disaggregation literature.]

Disaggregation is performed at a target hazard level, defined by an annual exceedance probability or return period. This produces conditional probability distributions over scenario bins and identifies controlling scenario parameters responsible for site hazard [@Kramer1997]. The ground-motion exceedance probability and total annual exceedance rate are defined in the hazard analysis (see [@eq-hazard-integral], [@eq-epsilon-star]). The joint exceedance rate for scenario $(m_k, r_j, \varepsilon_\ell)$ from source $s$ is given in [@eq-disagg-rate], where $\phi$ is the standard normal probability density function and $\mathbf 1_{{\cdot}}$ is the indicator function. Integration over $\varepsilon$ yields the two-dimensional ($M$–$R$) formulation. Partitioning parameter space into magnitude bins $m_k$, distance bins $r_j$, and residual bins $\varepsilon_\ell$, the contribution from bin $(k,j,\ell)$ is in [@eq-disagg-bin].
^[Confidence: HIGH, Rationale: The Kramer (1997) reference is a standard graduate-level geotechnical earthquake engineering textbook that includes disaggregation methodology; the citation is appropriate for the concept of conditional probability distributions and controlling scenario parameters. The description of disaggregation as producing conditional distributions over scenario bins at a target hazard level is consistent with Bazzurro and Cornell (1999) [WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard] and standard PSHA practice [WEB:https://opensha.org/resources/PSHA_Primer_v2_0.pdf]. The reference to a separate equation [@eq-epsilon-star] for the epsilon threshold is consistent with the standard disaggregation framework.]

$$
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)} =
\mathbf 1_{\{\varepsilon\ge\varepsilon^{*}(m_k,r_j)\}}
\,
\phi(\varepsilon)\,
f_{M,s}(m_k)\,
f_{R|M,s}(r_j|m_k)\,
\nu_{s},
$${#eq-disagg-rate}

$$
\lambda_{k,j,\ell}(i^{*})=
\sum_{s=1}^{N_{S}}
\int_{m_k}
\int_{r_j}
\int_{\varepsilon_\ell}
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)}
d\varepsilon\,dr\,dm
$${#eq-disagg-bin}

The conditional probability that exceedance of $i^*$ is produced by this bin is given by [@eq-disagg-prob]. The **modal scenario** is the $(k,j,\ell)$ bin for which $P_{kj\ell}(i^{*})$ attains its maximum. Hazard disaggregation applies Bayes' theorem to the joint distribution of scenario parameters and ground-motion exceedance as in [@eq-disagg-prob].
The marginal distribution for $\varepsilon$ quantifies the proportion of exceedance attributable to median or above-median ground-motion residuals. Marginal probabilities are obtained by double summation over the other indices as in [@eq-disagg-marginal-M], [@eq-disagg-marginal-R], [@eq-disagg-marginal-eps]:
^[Confidence: MEDIUM, Rationale: The definition of the modal scenario as the bin maximising $P_{kj\ell}(i^*)$ and the application of Bayes' theorem to obtain the conditional probability distribution are consistent with Bazzurro and Cornell (1999) [WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard]. However, several notation inconsistencies are present that reduce confidence in the mathematical rigour of this section: (1) the subscript notation $\theta_{j,k,l}$ uses a lowercase letter "l" in some locations while $\varepsilon_\ell$ uses the proper LaTeX $\ell$ symbol in others -- this inconsistency appears throughout the following equations (@eq-disagg-prob, @eq-disagg-marginal-M, @eq-disagg-marginal-R, @eq-disagg-marginal-eps); (2) in @eq-disagg-prob, the term $\lambda_{k,j\ell}$ is missing a comma separator (should be $\lambda_{k,j,\ell}$ for consistency with the triple-index notation used elsewhere); (3) the summation expression $\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1$ in @eq-disagg-prob appears malformed -- the sub-expression $[I>i^{*}]=1$ is not standard probability notation and the closing parenthesis of the summation is absent; the intended expression is likely the normalisation condition $\sum_{k}\sum_{j}\sum_{\ell}\theta_{k,j,\ell} = 1$. These inconsistencies do not affect the conceptual correctness of the method but represent notation errors that should be corrected [WEB:https://opensha.org/resources/PSHA_Primer_v2_0.pdf].]


$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}] = \theta_{j,k,l}=
\frac{\lambda_{k,j\ell}(i^{*})}{\lambda_{I}(i^{*})}
\qquad
\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1
$${#eq-disagg-prob}

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{j,k,l}
$${#eq-disagg-marginal-M}
$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{j,k,l}
$${#eq-disagg-marginal-R}
$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{j,k,l}
$${#eq-disagg-marginal-eps}

Disaggregation provides a data-driven basis required for rigorous scenario selection in engineering analysis. The *modal scenario* and the highest-probability bins identified through disaggregation correspond to the earthquake characteristics most responsible for exceedance at the design ground-motion level.
^[Confidence: HIGH, Rationale: The characterisation of disaggregation as providing a data-driven basis for scenario selection, and the identification of the modal scenario with the earthquake characteristics most responsible for exceedance, are standard conclusions of the disaggregation methodology well supported in the literature [WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard][WEB:https://opensha.org/resources/PSHA_Primer_v2_0.pdf]. This concluding paragraph is conceptually accurate and consistent with the Bazzurro and Cornell (1999) framework.]
