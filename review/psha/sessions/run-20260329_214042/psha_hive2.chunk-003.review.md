---
reference-location: section
link-citations: true                   # make in-text cites clickable
---


Probabilistic seismic hazard analysis (PSHA) aggregates the contributions of all plausible earthquake scenarios, obscuring the specific combinations of magnitude ($M$), source-to-site distance ($R$), and ground-motion residual ($\varepsilon$) that control site hazard. **Hazard disaggregation** quantifies the relative contribution of each scenario class—binned by magnitude $m_k$, distance $r_j$, and residual $\varepsilon_\ell$—to the annual frequency of exceedance at a specified ground-motion threshold $i^*$ [@Bazzurro1999]. ^[Confidence: HIGH, Rationale: The characterisation of PSHA as aggregating all scenario contributions and the description of hazard disaggregation as a procedure to identify the relative contributions of magnitude, distance, and residual bins to the annual exceedance frequency are accurate. The foundational reference [@Bazzurro1999] corresponds to Bazzurro and Cornell (1999), "Disaggregation of Seismic Hazard," Bulletin of the Seismological Society of America, 89(2):501-520, which introduced systematic disaggregation procedures [DOI:10.1785/BSSA0890020501][WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard]. The claim is well-supported.]

Disaggregation is performed at a target hazard level, defined by an annual exceedance probability or return period. This produces conditional probability distributions over scenario bins and identifies controlling scenario parameters responsible for site hazard [@Kramer1997]. The ground-motion exceedance probability and total annual exceedance rate are defined in the hazard analysis (see [@eq-hazard-integral], [@eq-epsilon-star]). The joint exceedance rate for scenario $(m_k, r_j, \varepsilon_\ell)$ from source $s$ is given in [@eq-disagg-rate], where $\phi$ is the standard normal probability density function and $\mathbf 1_{{\cdot}}$ is the indicator function. Integration over $\varepsilon$ yields the two-dimensional ($M$--$R$) formulation. Partitioning parameter space into magnitude bins $m_k$, distance bins $r_j$, and residual bins $\varepsilon_\ell$, the contribution from bin $(k,j,\ell)$ is in [@eq-disagg-bin]. ^[Confidence: MEDIUM, Rationale: The description of disaggregation as producing conditional probability distributions at a target hazard level and identifying controlling scenario parameters is accurate and consistent with Bazzurro and Cornell (1999) [DOI:10.1785/BSSA0890020501]. The reference [@Kramer1997] most likely corresponds to the widely cited textbook "Geotechnical Earthquake Engineering" by Steven L. Kramer; however, that textbook was published in 1996 (Prentice Hall), not 1997, suggesting a possible citation year error [WEB:https://www.resolutionmineeis.us/documents/cornell-1968]. If the citation year is incorrect, it reduces bibliographic accuracy. The mathematical framework that follows, using the standard normal PDF $\phi$ and indicator function $\mathbf{1}_{(\cdot)}$ to express the joint exceedance rate, is standard in the disaggregation literature [DOI:10.1785/BSSA0890020501]. Confidence is MEDIUM due to the potentially incorrect year in the Kramer citation.]

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
The marginal distribution for $\varepsilon$ quantifies the proportion of exceedance attributable to median or above-median ground-motion residuals. Marginal probabilities are obtained by double summation over the other indices as in [@eq-disagg-marginal-M], [@eq-disagg-marginal-R], [@eq-disagg-marginal-eps]: ^[Confidence: MEDIUM, Rationale: The definition of the modal scenario as the bin with the highest conditional probability is correct and standard in disaggregation practice [DOI:10.1785/BSSA0890020501]. The application of Bayes' theorem to obtain the conditional distribution of scenario parameters given exceedance is conceptually accurate [WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard]. However, the display math for [@eq-disagg-prob] that follows contains a notation inconsistency and a formatting defect: the normalization condition at the end of the equation appears as $\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1$, which has unmatched brackets and reads as ill-formed notation. The intended expression is presumably $\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}(I>i^{*}) = 1$, expressing that the conditional probabilities sum to unity. Additionally, the theta subscript introduced in [@eq-disagg-prob] is written as $\theta_{j,k,l}$ (distance-first order), while the bin indexing convention introduced in the preceding paragraph uses the order $(k,j,\ell)$ (magnitude-first). This inconsistency in subscript ordering persists in the marginal equations. These notation defects reduce precision and should be corrected for consistency. Confidence is MEDIUM.]


$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}] = \theta_{j,k,l}=
\frac{\lambda_{k,j\ell}(i^{*})}{\lambda_{I}(i^{*})}
\qquad
\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1
$${#eq-disagg-prob}

^[Confidence: LOW, Rationale: The conditional probability formula $P[\,\cdot\mid I>i^*] = \lambda_{k,j\ell}(i^*) / \lambda_I(i^*)$ is the correct Bayesian disaggregation expression [DOI:10.1785/BSSA0890020501]. However, two errors are present in this display math block. First, the normalization expression $\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1$ contains unmatched brackets and non-standard notation; the correct form is $\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}(I>i^{*}) = 1$. Second, the notation $\theta_{j,k,l}$ uses a subscript ordering (distance $j$, magnitude $k$, residual $l$) that is inconsistent with the $(k,j,\ell)$ ordering (magnitude, distance, residual) established in the surrounding text and in the bin definition equations [@eq-disagg-rate] and [@eq-disagg-bin]. This inconsistency propagates to the marginal equations below. These errors must be corrected for notational consistency and mathematical clarity.]

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{j,k,l}
$${#eq-disagg-marginal-M}
$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{j,k,l}
$${#eq-disagg-marginal-R}
$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{j,k,l}
$${#eq-disagg-marginal-eps}

Disaggregation provides a data-driven basis required for rigorous scenario selection in engineering analysis. The *modal scenario* and the highest-probability bins identified through disaggregation correspond to the earthquake characteristics most responsible for exceedance at the design ground-motion level. ^[Confidence: HIGH, Rationale: The statement that disaggregation provides the data-driven basis for scenario selection and that the modal scenario identifies the dominant earthquake characteristics is accurate and well-established in seismic hazard practice [DOI:10.1785/BSSA0890020501][WEB:https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/89/2/501/342641/Disaggregation-of-seismic-hazard]. This claim is unambiguous and fully supported by the founding literature on hazard disaggregation.]
