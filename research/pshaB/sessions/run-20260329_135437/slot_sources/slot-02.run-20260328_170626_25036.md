## SLOT 2: Canonical hazard equations for MCE and disaggregation

The particularized hazard integral derived in Slot 1 is here expressed in canonical epsilon form for two applications: (a) determination of the Maximum Considered Earthquake (MCE) ground-motion intensity and (b) seismic hazard disaggregation. In both cases, the standard normal PDF $\phi(\varepsilon)$ associated with the GMPE residual variable $\varepsilon$ serves as the weighting kernel linking annual hazard contributions to the frequency of above-median ground-motion realizations, and the critical residual threshold $\varepsilon^*(m, r) = [\ln i^* - \ln\hat{\eta}_I(m,r)]/\sigma_{\ln I}$ plays a central role in defining the exceedance condition. [KB:hazard.md]^[Confidence: HIGH, Rationale: The two applications, MCE determination and hazard disaggregation, are both treated in [KB:hazard.md] as direct extensions of the particularized hazard integral. The central role of $\phi(\varepsilon)$ and $\varepsilon^*(m,r)$ is established by the epsilon-form reformulation in [KB:hazard.md] and is consistent with the Slot 1 derivation.]

### (a) Maximum Considered Earthquake Determination

Under the Poisson occurrence assumption, the annual exceedance probability (AEP) is related to the annual exceedance rate by [KB:hazard.md]:

$$\mathrm{AEP} = P_{1\,\mathrm{yr}}\!\left[I > i^*\right] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

For a target return period $T_R$, inverting this relation yields the corresponding target annual exceedance rate. [KB:hazard.md]^[Confidence: HIGH, Rationale: The Poisson AEP-rate relation is stated explicitly in [KB:hazard.md] in the MCE section. The inversion for $\lambda_I$ given a target AEP follows by applying the natural logarithm to both sides, which is a standard algebraic step confirmed by [KB:hazard.md].]

Solving for the annual exceedance rate that corresponds to the target AEP gives [KB:hazard.md]:

$$\lambda_I(i^*_{\mathrm{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ holds for large return periods and is widely used in practice. This relation defines $i^*_{\mathrm{MCE}}$ implicitly as the hazard curve ordinate at which the annual exceedance rate equals the target value. Because the full particularized hazard integral from Slot 1 requires numerical evaluation for a general GMPE, the inversion of the hazard curve to recover $i^*_{\mathrm{MCE}}$ likewise requires numerical methods. [KB:hazard.md]^[Confidence: HIGH, Rationale: The target rate expression, the large-$T_R$ approximation, and the requirement for numerical inversion of the hazard curve are all stated explicitly in [KB:hazard.md] in the MCE section. No claims extend beyond what is directly confirmed in [KB:hazard.md].]

For the MCE scenario, the ground motion is conditioned on the maximum magnitude $M_{\max}$ at a representative source-to-site distance $r$. The conditional exceedance probability in epsilon form, using the integral representation of the complementary normal CDF, is [KB:hazard.md]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max},\, r)}^{\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

Setting this probability equal to the target AEP and inverting the normal CDF yields the critical MCE epsilon level [KB:hazard.md]:

$$\varepsilon^*_{\mathrm{MCE}} = \Phi^{-1}\!\left(1 - \mathrm{AEP}\right) = \Phi^{-1}\!\!\left(1 - \frac{1}{T_R}\right)$$

The closed-form MCE ground-motion intensity is then expressed directly in terms of $\varepsilon^*_{\mathrm{MCE}}$ [@McGuire1995] [KB:hazard.md]:

$$i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\varepsilon^*_{\mathrm{MCE}}\right]$$

The quantity $\varepsilon^*_{\mathrm{MCE}} = \Phi^{-1}(1 - 1/T_R)$ is positive for all practically relevant return periods and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995] [KB:hazard.md]. For the circular source, a geometrically natural representative distance is the mean epicentral distance:

$$\bar{r} = \int_0^R r\, f_R(r)\, dr = \int_0^R \frac{2r^2}{R^2}\, dr = \frac{2R}{3}$$

Alternatively, the modal magnitude-distance scenario identified by hazard disaggregation provides a hazard-consistent representative distance; the selection criterion must be stated explicitly in any specific application. [KB:hazard.md]^[Confidence: HIGH, Rationale: The MCE epsilon formulation, including the inversion of the normal CDF, the closed-form expression for $i^*_{\mathrm{MCE}}$, and the monotonic increase of $\varepsilon^*_{\mathrm{MCE}}$ with $T_R$, are given explicitly in [KB:hazard.md] in the MCE section, attributed to [@McGuire1995]. The mean distance $\bar{r} = 2R/3$ is derived in [KB:hazard.md] by integrating $r$ against $f_R(r) = 2r/R^2$, and the alternative hazard-consistent selection from disaggregation is also discussed in [KB:hazard.md].]

### (b) Seismic Hazard Disaggregation

Hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from discrete scenario bins indexed by magnitude $m_k$, distance $r_j$, and optionally GMPE residual $\varepsilon_\ell$, producing the conditional probability distribution over seismic scenarios given that intensity $i^*$ is exceeded. The central quantity in the disaggregation is the critical residual threshold for scenario $(m, r)$, obtained by inverting the lognormal exceedance model [@BazzurroCornell1999] [KB:hazard.md]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized GMPE residual $\varepsilon \geq \varepsilon^*(m,r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute negligibly to the total hazard at intensity level $i^*$. [KB:hazard.md]^[Confidence: HIGH, Rationale: The disaggregation framework and the critical residual threshold $\varepsilon^*(m,r)$ are defined in [KB:hazard.md] in the disaggregation section, attributed to [@BazzurroCornell1999]. The interpretation that large-$\varepsilon^*$ scenarios contribute negligibly is also stated in [KB:hazard.md].]

The two-dimensional (M-R) disaggregation bin rate for bin $(m_k, r_j)$ is obtained by integrating the epsilon-form hazard integrand from Slot 1 over the bin domain, using the representation $1 - \Phi(\varepsilon^*(m,r)) = \int_{\varepsilon^*(m,r)}^{\infty}\phi(\varepsilon)\, d\varepsilon$ [@BazzurroCornell1999] [KB:hazard.md]:

$$\lambda_{k,j}(i^*) = \nu_0 \int_{m_k} \int_{r_j} \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\; f_M(m)\cdot \frac{2r}{R^2}\; d\varepsilon\; dr\; dm$$

The fraction of the total annual exceedance rate attributable to bin $(m_k, r_j)$ is [KB:hazard.md]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights satisfy $\sum_k\sum_j \theta_{k,j} = 1$ by construction. Both $\lambda_{k,j}(i^*)$ and $\lambda_I(i^*)$ require numerical quadrature for a general GMPE. The modal scenario $(m_k^*, r_j^*)$ is identified as the bin pair maximizing $\theta_{k,j}$, representing the magnitude-distance combination that contributes most to hazard at intensity $i^*$. [KB:hazard.md]^[Confidence: HIGH, Rationale: The M-R bin rate, the weight $\theta_{k,j}$, the completeness condition, and the modal scenario definition are all stated explicitly in [KB:hazard.md] in the disaggregation section, attributed to [@BazzurroCornell1999]. The numerical evaluation requirement follows from the general-GMPE constraint, also noted in [KB:hazard.md].]

The full three-dimensional $(M, R, \varepsilon)$ disaggregation retains the residual dimension explicitly. The contribution of residual bin $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ to scenario bin $(m_k, r_j)$ is obtained by restricting the $\varepsilon$ integral to the bin support. The inner integral over $\varepsilon$ admits closed-form evaluation as a difference of standard normal CDF values, yielding the bin rate [@BazzurroCornell1999] [KB:hazard.md]:

$$\lambda_{k,j,\ell}(i^*) = \nu_0 \int_{m_k}\int_{r_j} \left[\Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right)\right] f_M(m)\cdot\frac{2r}{R^2}\; dr\; dm$$

The bracket equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m, r)$, reflecting the condition that no exceedance of $i^*$ is possible from residual bin $\varepsilon_\ell$ for scenario $(m, r)$ when the entire bin lies below the threshold. The closed-form evaluation of the $\varepsilon$ integral reduces the three-dimensional problem to a double integral over $(m, r)$ within each bin, which requires numerical quadrature for a general GMPE. [KB:hazard.md]^[Confidence: HIGH, Rationale: The three-dimensional disaggregation bin rate and the closed-form evaluation of the inner $\varepsilon$ integral are given explicitly in [KB:hazard.md] in the disaggregation section, attributed to [@BazzurroCornell1999]. The zero-contribution condition and the reduction to a double integral are confirmed by [KB:hazard.md].]

The joint conditional probability attributed to bin $(m_k, r_j, \varepsilon_\ell)$ is [KB:hazard.md]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k\sum_j\sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining two indices [KB:hazard.md]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell} \theta_{k,j,\ell}, \qquad P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell} \theta_{k,j,\ell}, \qquad P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j} \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger distances, while GMPE attenuation reduces exceedance probability with increasing $r$; the marginal distance disaggregation $P[R \in r_j \mid I > i^*]$ reflects the competition between these two effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE. [@BazzurroCornell1999] [KB:hazard.md]^[Confidence: HIGH, Rationale: The completeness condition, marginal distribution expressions, and the qualitative description of competing geometric and attenuation effects on the distance marginal are all stated in [KB:hazard.md] in the disaggregation section, attributed to [@BazzurroCornell1999]. All claims are directly supported by [KB:hazard.md].]
