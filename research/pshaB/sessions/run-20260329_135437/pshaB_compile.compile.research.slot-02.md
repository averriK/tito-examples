## SLOT 2: Canonical hazard equations for MCE and disaggregation

The particularized hazard integral from Slot 1 supports two canonical downstream applications for the single circular areal source: determination of the Maximum Considered Earthquake (MCE) ground-motion intensity and seismic hazard disaggregation. Both formulations are expressed in terms of the normalized standard normal probability density function $\phi(\varepsilon)$ and the critical residual threshold $\varepsilon^*(m, r)$ introduced in Slot 1 [@KBhazard].

### (a) Maximum Considered Earthquake Determination

Under the Poisson occurrence assumption, the annual exceedance probability (AEP) is related to the annual exceedance rate by [@Baker2013][@KBhazard]:

$$\mathrm{AEP} = P_{1\,\mathrm{yr}}\!\left[I > i^*\right] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

For a target return period $T_R$, inverting this relation yields the corresponding target annual exceedance rate [@KBhazard]:

$$\lambda_I(i^*_{\mathrm{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ holds for large return periods and is standard in engineering practice. This relation defines $i^*_{\mathrm{MCE}}$ implicitly as the hazard curve ordinate at which the annual exceedance rate equals the target value; because the full particularized hazard integral requires numerical evaluation for a general GMPE, the inversion of the hazard curve to recover $i^*_{\mathrm{MCE}}$ likewise requires numerical methods.

The canonical MCE hazard equation in epsilon form conditions on an event of magnitude $M_{\max}$ at a representative source-to-site distance $r$. The conditional exceedance probability expressed as a tail integral over $\varepsilon$ is [@KBhazard]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max},\, r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

Setting this probability equal to the target AEP and inverting the standard normal CDF yields the critical MCE epsilon level and the closed-form MCE ground-motion intensity [@McGuire1995][@KBhazard]:

$$\varepsilon^*_{\mathrm{MCE}} = \Phi^{-1}\!\left(1 - \frac{1}{T_R}\right)$$

$$i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\varepsilon^*_{\mathrm{MCE}}\right]$$

The quantity $\varepsilon^*_{\mathrm{MCE}}$ is positive for all practically relevant return periods and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995]. The representative distance $r$ in the MCE formulation requires explicit specification; the mean epicentral distance:

$$\bar{r} = \int_0^R r\, f_R(r)\, dr = \int_0^R \frac{2r^2}{R^2}\, dr = \frac{2R}{3}$$

is one geometrically consistent choice derived directly from the circular source distance PDF, while the modal magnitude-distance scenario identified by hazard disaggregation provides a hazard-consistent alternative; the selection criterion must be stated explicitly in any specific application [@KBhazard].

### (b) Seismic Hazard Disaggregation: M-R Plane

Seismic hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from discrete scenario bins indexed by magnitude $m_k$ and distance $r_j$, producing the conditional probability distribution over seismic scenarios given that intensity $i^*$ is exceeded. The critical GMPE residual threshold for scenario $(m, r)$ - the minimum residual for which intensity exceeds $i^*$ - is [@BazzurroCornell1999][@KBhazard]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized residual $\varepsilon \geq \varepsilon^*(m, r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute negligibly to the total hazard at intensity level $i^*$. The joint exceedance rate for magnitude bin $m_k$ and distance bin $r_j$, expressed in epsilon form using $f_R(r) = 2r/R^2$, is [@BazzurroCornell1999][@KBhazard]:

$$\lambda_{k,j}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

The fractional contribution of bin $(m_k, r_j)$ to the total annual exceedance rate is [@BazzurroCornell1999][@KBhazard]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights satisfy $\sum_k\sum_j \theta_{k,j} = 1$ by construction. Both $\lambda_{k,j}(i^*)$ and $\lambda_I(i^*)$ require numerical quadrature for a general GMPE. The modal scenario $(m_k^*, r_j^*)$ is identified as the bin pair maximizing $\theta_{k,j}$, representing the magnitude-distance combination that contributes most to hazard at intensity level $i^*$.

### (c) Seismic Hazard Disaggregation: Full $(M, R, \varepsilon)$ Form

For the full three-dimensional disaggregation retaining the residual dimension, the exceedance rate contribution from bin $(m_k, r_j, \varepsilon_\ell)$ with $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ is, in canonical epsilon form [@BazzurroCornell1999][@KBhazard]:

$$\lambda_{k,j,\ell}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\, f_M(m) \int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, d\varepsilon\, dr\, dm$$

The inner integral over the epsilon bin $[\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ admits a closed-form evaluation in terms of the standard normal CDF [@BazzurroCornell1999][@KBhazard]:

$$\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\,\phi(\varepsilon)\,d\varepsilon = \Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right), \qquad \varepsilon_\ell^{\rm hi} > \varepsilon^*(m,r)$$

and equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m,r)$, because no residual in the bin is sufficient to produce exceedance. The closed-form evaluation of the $\varepsilon$ integral reduces the three-dimensional problem to a double integral over $(m, r)$ within each bin, which requires numerical quadrature for a general GMPE.

The joint conditional disaggregation probability for bin $(m_k, r_j, \varepsilon_\ell)$, normalized by the total exceedance rate, is [@BazzurroCornell1999][@KBhazard]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k\sum_j\sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal conditional distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining bin indices [@KBhazard]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j}\, \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger epicentral distances, while the GMPE attenuates exceedance probability with increasing distance; the marginal conditional distribution $P[R \in r_j \mid I > i^*]$ reflects the balance of these competing geometric and attenuation effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE [@BazzurroCornell1999][@KBhazard].
