## SLOT 2: Canonical hazard equations for MCE and disaggregation

The particularized hazard integral derived in Slot 1 supports two canonical downstream applications for the single circular areal source: determination of the Maximum Considered Earthquake (MCE) ground-motion intensity and seismic hazard disaggregation. Both formulations are expressed in terms of the normalized standard normal probability density function $\phi(\varepsilon)$ associated with the ground motion prediction model, building on the critical residual threshold $\varepsilon^*(m, r) = [\ln i^* - \ln\hat{\eta}_I(m,r)]/\sigma_{\ln I}$ introduced in Slot 1. [@HazardKB]

### (a) Maximum Considered Earthquake determination

Under the Poisson occurrence assumption, the annual exceedance probability (AEP) for intensity $I$ exceeding level $i^*$ is related to the annual exceedance rate by [@HazardKB][@Baker2013]:

$$\mathrm{AEP} = P_{1\,\mathrm{yr}}\!\left[I > i^*\right] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

For a target return period $T_R$, inverting this relation yields the corresponding target annual exceedance rate [@HazardKB]:

$$\lambda_I(i^*_{\mathrm{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ is accurate for large return periods and constitutes the standard engineering approximation in PSHA. The MCE intensity $i^*_{\mathrm{MCE}}$ is defined implicitly as the solution to $\lambda_I(i^*_{\mathrm{MCE}}) = -\ln(1 - 1/T_R)$; because the full hazard integral from Slot 1 requires numerical evaluation for a general GMPE, the inversion of the hazard curve likewise requires numerical methods. [@HazardKB]

For the MCE scenario conditioned on the maximum magnitude $M_{\max}$ at a representative source-to-site distance $r$, the conditional exceedance probability in epsilon form is [@HazardKB]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max},\, r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

Setting this probability equal to the target AEP and inverting the standard normal CDF relationship yields the critical MCE epsilon level and the closed-form MCE ground-motion intensity [@McGuire1995][@HazardKB]:

$$\varepsilon^*_{\mathrm{MCE}} = \Phi^{-1}\!\left(1 - \frac{1}{T_R}\right)$$

$$i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\varepsilon^*_{\mathrm{MCE}}\right]$$

The quantity $\varepsilon^*_{\mathrm{MCE}}$ is positive for all practically relevant return periods and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995][@HazardKB]. The representative distance $r$ requires explicit specification in any application. A geometrically consistent choice is the mean epicentral distance, obtained by integrating $r$ against the circular source distance PDF $f_R(r) = 2r/R^2$ over $[0, R]$ [@HazardKB]:

$$\bar{r} = \int_0^R r\, f_R(r)\, dr = \int_0^R \frac{2r^2}{R^2}\, dr = \frac{2R}{3}$$

Alternatively, the modal magnitude-distance scenario identified by hazard disaggregation provides a hazard-consistent choice; the selection criterion must be stated explicitly in any specific application. [@HazardKB]

### (b) Seismic hazard disaggregation

Hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from discrete scenario bins indexed by magnitude $m_k$, distance $r_j$, and optionally GMPE residual $\varepsilon_\ell$, producing the conditional distribution over seismic scenarios given that intensity $i^*$ is exceeded. For the single circular source, the critical residual threshold for scenario $(m, r)$ is [@BazzurroCornell1999][@HazardKB]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized residual $\varepsilon \geq \varepsilon^*(m, r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute negligibly to the total hazard at intensity level $i^*$. [@HazardKB]

**Two-dimensional M-R disaggregation.** The disaggregation bin rate for magnitude bin $m_k$ and distance bin $r_j$ is obtained by integrating the epsilon-form hazard integrand over the bin domain [@BazzurroCornell1999][@HazardKB]:

$$\lambda_{k,j}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

The fractional contribution of bin $(m_k, r_j)$ to the total annual exceedance rate is [@BazzurroCornell1999][@HazardKB]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights satisfy $\sum_k\sum_j \theta_{k,j} = 1$ by construction. The modal scenario $(m_k^*, r_j^*)$ is identified as the bin maximizing $\theta_{k,j}$, representing the magnitude-distance combination contributing most to hazard at intensity level $i^*$. Both $\lambda_{k,j}(i^*)$ and $\lambda_I(i^*)$ require numerical integration for a general GMPE. [@HazardKB]

**Full three-dimensional $(M, R, \varepsilon)$ disaggregation.** For the full disaggregation including the GMPE residual dimension, the exceedance rate contribution from bin $(m_k, r_j, \varepsilon_\ell)$ with $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ is, in canonical epsilon form [@BazzurroCornell1999][@HazardKB]:

$$\lambda_{k,j,\ell}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\, f_M(m) \int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, d\varepsilon\, dr\, dm$$

The inner integral over the epsilon bin $[\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ admits closed-form evaluation in terms of the standard normal CDF [@BazzurroCornell1999][@HazardKB]:

$$\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\,\phi(\varepsilon)\,d\varepsilon = \Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right), \quad \varepsilon_\ell^{\rm hi} > \varepsilon^*(m,r)$$

and equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m,r)$, because no residual in the bin is sufficient to produce exceedance of $i^*$. This closed-form evaluation reduces the three-dimensional integration problem to a double integral over $(m, r)$ within each bin, which requires numerical quadrature for a general GMPE. [@HazardKB]

The joint conditional disaggregation probability for bin $(m_k, r_j, \varepsilon_\ell)$, normalized by the total exceedance rate, is [@BazzurroCornell1999][@HazardKB]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k\sum_j\sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal conditional distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining bin indices [@HazardKB]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell}\, \theta_{k,j,\ell}, \qquad P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell}\, \theta_{k,j,\ell}, \qquad P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j}\, \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger epicentral distances, while GMPE attenuation reduces exceedance probability with increasing distance; the marginal conditional distribution $P[R \in r_j \mid I > i^*]$ reflects the competition between these effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE. [@BazzurroCornell1999][@HazardKB]
