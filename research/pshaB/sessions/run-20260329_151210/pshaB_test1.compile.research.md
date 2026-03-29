# Probabilistic Seismic Hazard Analysis: Annual Exceedance Rate and Canonical Hazard Equations for a Single Circular Areal Source

## 1. Derivation of the particularized annual exceedance rate in epsilon form

The particularization of the general PSHA hazard integral to the single circular areal source identifies four components of the integrand: the annual occurrence rate $\nu_0$, the truncated Gutenberg-Richter magnitude probability density function $f_M(m)$, the conditional ground-motion exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$ appropriate to the circular source geometry. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, minimum engineering magnitude $M_{\min}$, maximum magnitude $M_{\max}$, and a uniform spatial distribution of seismicity over a disk of radius $R$ centered on the study site; contributions from beyond radius $R$ are negligible by assumption, and the distance integration domain reduces to $[0, R]$. No site effects are included; the analysis applies to reference rock conditions throughout, with no specific ground motion prediction equation assumed [@KBhazard][@Baker2013][@Kramer1996].

Reducing the general multi-source hazard sum to the single circular source, the particularized annual exceedance rate takes the form [@KBhazard]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

where $R_{\min} = 0$ and $R_{\max} = R$ are the integration limits imposed by the circular source geometry centered on the site.

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence law $\log_{10} N(M) = a - bM$, where $N(M)$ is the mean annual number of earthquakes at or above magnitude $M$, evaluated at the engineering minimum magnitude $M_{\min}$ yields the scalar annual occurrence rate [@KBhazard]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

where $a$ and $b$ are the Gutenberg-Richter activity rate and slope parameters. The rate $\nu_0$ counts the mean annual number of seismically relevant events on the source and is factored outside all subsequent integrals.

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude probability density function over the engineering range $[M_{\min}, M_{\max}]$ is obtained by normalizing the Gutenberg-Richter density over the support and canceling common factors [@KBhazard][@Kramer1996]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ is the normalization constant ensuring that $f_M(m)$ integrates to unity over $[M_{\min}, M_{\max}]$.

**Component (iii): Distance probability density function.** For a site at the center of the circular areal source with spatially uniform seismicity, the probability that an earthquake originates in a thin annulus of width $dr$ at epicentral distance $r$ is proportional to the annular area $2\pi r\, dr$ divided by the total disk area $\pi R^2$, giving [@KBhazard][@Baker2013]:

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

The density is monotonically increasing in $r$, reflecting the fact that more source area lies at larger epicentral distances from the central site. Under the uniform seismicity assumption, epicenter location and earthquake magnitude are spatially independent, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R|M}(r|m) = f_R(r)$. This independence carries through all subsequent integrals without modification.

**Component (iv): Conditional exceedance probability.** No specific GMPE is assumed. The ground-motion intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m, r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions. The conditional probability of exceeding intensity $i^*$ given magnitude $m$ and distance $r$ is [@KBhazard][@Kramer1996]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. When $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly 0.5; exceedance becomes increasingly improbable as the argument of $\Phi$ increases.

**Epsilon reformulation.** The critical standardized residual threshold for scenario $(m, r)$ is defined as [@KBhazard]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

This quantity is the number of logarithmic standard deviations by which the target intensity $i^*$ lies above the GMPE median for scenario $(m, r)$, so that $P[I > i^* \mid m, r] = 1 - \Phi(\varepsilon^*(m,r))$. The complementary normal CDF is represented as a tail integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$:

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon$$

This identity converts the two-dimensional hazard integral into a triple integral over $(m, r, \varepsilon)$, with $\varepsilon$ integrated from the scenario-dependent lower limit $\varepsilon^*(m,r)$ to $+\infty$, making explicit the convolution structure of the hazard integral [@KBhazard].

**Assembly: particularized annual exceedance rate in epsilon form.** Substituting $f_R(r) = 2r/R^2$, $f_M(m)$, $\nu_0$, and the tail-integral representation into the general single-source hazard integral yields the intermediate epsilon form [@KBhazard][@Baker2013]:

$$\lambda_I(i^*) = \frac{2\nu_0}{R^2} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

with $R_{\min} = 0$ and $R_{\max} = R$. Substituting the explicit form of $f_M(m)$ and factoring all constant terms outside the triple integral produces the fully factored particularized annual exceedance rate in epsilon form [@KBhazard][@Baker2013]:

$$\lambda_I(i^*) = \frac{2\,\nu_0\, b\ln 10}{R^2\!\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} 10^{-b(m-M_{\min})}\, \phi(\varepsilon)\; r\; d\varepsilon\; dr\; dm$$

All terms outside the triple integral are constants determined by the source parameters $a$, $b$, $M_{\min}$, $M_{\max}$, and radius $R$, with $\nu_0 = 10^{a - b\,M_{\min}}$ substituted explicitly. The core integrand $10^{-b(m-M_{\min})} \cdot \phi(\varepsilon) \cdot r$ constitutes a convolution of the standard normal PDF $\phi(\varepsilon)$ with the unnormalized Gutenberg-Richter magnitude distribution $10^{-b(m-M_{\min})}$, modulated by the geometric weight $r$ from the circular source distance PDF. The explicit integration limits are $R_{\min} = 0$, $R_{\max} = R$, $M_{\min}$, and $M_{\max}$; the lower limit of the $\varepsilon$ integral, $\varepsilon^*(m,r)$, depends on both $m$ and $r$ through the GMPE median $\hat{\eta}_I(m,r)$. The integrand is non-negative throughout the domain, approaches zero as $r \to 0$ because $f_R(r) = 2r/R^2 \to 0$, and decays to zero as $i^*$ grows large relative to $\hat{\eta}_I(m,r)$ for all $(m, r)$ in the domain. For a general GMPE $\hat{\eta}_I(m,r)$, this dependence on $(m,r)$ prevents closed-form evaluation, and numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [0, R]$ is required [@KBhazard][@Baker2013].

## 2. Canonical hazard equations for MCE and disaggregation

The particularized annual exceedance rate derived in Section 1 supports two canonical downstream applications: (a) determination of the Maximum Considered Earthquake (MCE) ground-motion intensity, and (b) seismic hazard disaggregation. Both formulations are expressed in terms of the standard normal probability density function $\phi(\varepsilon)$ associated with the GMPE residual variable $\varepsilon$, with the critical residual threshold $\varepsilon^*(m, r)$ introduced in Section 1 defining the exceedance condition for each scenario $(m, r)$ [@KBhazard].

### (a) Maximum Considered Earthquake

The MCE ground-motion intensity $i^*_{\text{MCE}}$ is the intensity level at which the annual exceedance rate $\lambda_I(i^*)$ equals a prescribed target rate linked to a design return period $T_R$. Under the Poisson occurrence assumption, the one-year and multi-year exceedance probabilities are related to the rate by [@KBhazard][@Baker2013]:

$$P_{1\,\text{yr}}\!\left[I > i^*\right] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

$$P_{T_R}\!\left[I > i^*\right] = 1 - \exp\!\left[-\lambda_I(i^*)\, T_R\right]$$

Setting the annual exceedance probability equal to $\text{AEP} = 1/T_R$ and inverting for the target rate yields the canonical MCE hazard equation [@KBhazard]:

$$\lambda_I(i^*_{\text{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ is accurate for large return periods and is standard in PSHA practice. The MCE intensity $i^*_{\text{MCE}}$ is defined implicitly as the solution to $\lambda_I(i^*_{\text{MCE}}) = \lambda^*$; because the full hazard integral requires numerical evaluation for a general GMPE, the inversion of the hazard curve likewise requires numerical methods [@KBhazard].

For the MCE scenario, the ground motion is conditioned on the maximum magnitude $M_{\max}$ at a representative source-to-site distance $r$. The conditional exceedance probability expressed as a tail integral over $\varepsilon$ is [@KBhazard]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max},\, r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

Setting this probability equal to the target AEP and inverting the standard normal CDF yields the critical MCE epsilon level [@KBhazard]:

$$\varepsilon^*_{\text{MCE}} = \Phi^{-1}\!\left(1 - \mathrm{AEP}\right) = \Phi^{-1}\!\!\left(1 - \frac{1}{T_R}\right)$$

The closed-form MCE ground-motion intensity is then expressed directly in terms of $\varepsilon^*_{\text{MCE}}$ [@KBhazard][@McGuire1995]:

$$i^*_{\text{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\varepsilon^*_{\text{MCE}}\right]$$

The quantity $\varepsilon^*_{\text{MCE}} = \Phi^{-1}(1 - 1/T_R)$ is positive for all practically relevant return periods and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995][@KBhazard]. The representative distance $r$ requires explicit specification. For the circular source, the mean epicentral distance provides a geometrically consistent choice derived directly from the circular source distance PDF [@KBhazard]:

$$\bar{r} = \int_0^R r\, f_R(r)\, dr = \int_0^R \frac{2r^2}{R^2}\, dr = \frac{2R}{3}$$

Alternatively, the modal magnitude-distance scenario identified by hazard disaggregation provides a hazard-consistent representative distance; the selection criterion must be stated explicitly in any specific application.

### (b) Seismic hazard disaggregation: M-R plane

Seismic hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from individual scenario bins defined by magnitude, distance, and optionally GMPE residual, producing the conditional distribution over seismic scenarios given that intensity $i^*$ is exceeded. The critical residual threshold for scenario $(m, r)$ is [@KBhazard][@BazzurroCornell1999]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized residual $\varepsilon \geq \varepsilon^*(m, r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute negligibly to the hazard at intensity level $i^*$.

The joint exceedance rate for magnitude bin $m_k$ and distance bin $r_j$, expressed in full epsilon form with $f_R(r) = 2r/R^2$, is [@KBhazard][@BazzurroCornell1999]:

$$\lambda_{k,j}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

The fractional contribution of bin $(m_k, r_j)$ to the total annual exceedance rate is [@KBhazard][@BazzurroCornell1999]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights satisfy $\sum_k \sum_j \theta_{k,j} = 1$ by construction. Both $\lambda_{k,j}(i^*)$ and $\lambda_I(i^*)$ require numerical integration for a general GMPE. The modal scenario $(m_k^*, r_j^*)$ is the bin for which $\theta_{k,j}$ attains its maximum, identifying the magnitude-distance combination that contributes most to hazard at intensity $i^*$.

### (c) Seismic hazard disaggregation: full $(M, R, \varepsilon)$ form

The exceedance rate contribution from bin $(m_k, r_j, \varepsilon_\ell)$ with $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ is, in canonical epsilon form [@KBhazard][@BazzurroCornell1999]:

$$\lambda_{k,j,\ell}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\, f_M(m) \int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, d\varepsilon\, dr\, dm$$

The inner integral over the epsilon bin admits closed-form evaluation as a difference of standard normal CDF values [@KBhazard][@BazzurroCornell1999]:

$$\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\,\phi(\varepsilon)\,d\varepsilon = \Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right), \quad \varepsilon_\ell^{\rm hi} > \varepsilon^*(m,r)$$

and equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m,r)$, because no residual in the bin is sufficient to produce exceedance. The remaining integrals over $m$ and $r$ within each bin require numerical quadrature for a general GMPE.

The joint conditional probability for bin $(m_k, r_j, \varepsilon_\ell)$, normalized by the total exceedance rate, is [@KBhazard][@BazzurroCornell1999]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k \sum_j \sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal conditional distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining bin indices [@KBhazard]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j}\, \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger epicentral distances, while the GMPE attenuates exceedance probability with increasing distance; the marginal conditional distribution $P[R \in r_j \mid I > i^*]$ reflects the balance of these competing effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE [@KBhazard][@BazzurroCornell1999].
