# PSHA Equations for a Single Circular Areal Source

## SLOT 1: Derivation of the Particularized Annual Exceedance Rate in Epsilon Form

The particularization of the general PSHA hazard integral to the single circular areal source begins by identifying four components of the integrand: the annual occurrence rate $\nu_0$, the truncated Gutenberg-Richter magnitude probability density function $f_M(m)$, the conditional ground-motion exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$ appropriate to the circular source geometry. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, minimum engineering magnitude $M_{\min}$, maximum magnitude $M_{\max}$, and a uniform spatial distribution of seismicity over a disk of radius $R$ centered on the study site; contributions from any source beyond radius $R$ are negligible by assumption, and the integration domain in distance reduces to $[0, R]$. [@Ref001]

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence law $\log_{10} N(M) = a - bM$ specifies the mean annual number of earthquakes $N(M)$ at or above magnitude $M$. Evaluating at the engineering minimum magnitude $M_{\min}$ yields the scalar prefactor that multiplies the full magnitude-distance integral [@Ref001]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

where $a$ and $b$ are the Gutenberg-Richter activity rate and slope parameters. The rate $\nu_0$ counts the mean annual number of seismically relevant events on the source; it is dimensionally the only quantity with units of events per year and is factored outside all subsequent integrals. [@Ref001]

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude probability density function over the engineering range $[M_{\min}, M_{\max}]$ is the truncated Gutenberg-Richter density obtained by normalizing the unnormalized density $10^{-bm}$ over the support and canceling the common factor $10^a$ [@Kramer1996] [@Ref001]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ is the normalization constant ensuring that $f_M(m)$ integrates to unity over $[M_{\min}, M_{\max}]$, confirming proper normalization as a probability density. [@Ref001]

**Component (iii): Distance probability density function.** The distance probability density function for the circular areal source with the study site at its center is derived from the uniform seismicity assumption: the probability that an earthquake originates in a thin annulus of width $dr$ at epicentral distance $r$ is proportional to the annular area $2\pi r\, dr$ divided by the total disk area $\pi R^2$, giving [@Baker2013] [@Ref001]:

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

Under the uniform seismicity model, epicenter location and earthquake magnitude are spatially independent, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R\mid M}(r\mid m) = f_R(r) = 2r/R^2$. This independence property carries through the full magnitude-distance integral without modification. [@Ref001]

**Component (iv): Conditional exceedance probability and the epsilon variable.** No specific ground motion prediction equation is assumed; the site-intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m, r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions with no site effects included. The conditional probability of exceeding intensity $i^*$ given an event of magnitude $m$ at distance $r$ is [@Kramer1996] [@Ref001]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. The signed logarithmic residual threshold $\varepsilon^*(m, r)$, defined as the argument of $\Phi$ above, quantifies the minimum number of logarithmic standard deviations above the median prediction at which $i^*$ lies for scenario $(m, r)$ [@Ref001]:

$$\varepsilon^*(m, r) \equiv \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

so that $P[I > i^* \mid m, r] = 1 - \Phi(\varepsilon^*(m, r))$. When $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly $0.5$; exceedance becomes increasingly improbable as $\varepsilon^*(m,r)$ increases. [@Ref001]

**Epsilon reformulation of the exceedance probability.** The key step in the epsilon form of the hazard integral is the replacement of the complementary standard normal CDF by the tail integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$. This identity is exact for all finite values of the threshold [@Ref001]:

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon$$

Substituting this representation into the conditional exceedance probability converts the two-dimensional hazard integral into a triple integral over the domain $(m, r, \varepsilon)$, with $\varepsilon$ integrated from the scenario-dependent lower limit $\varepsilon^*(m,r)$ to $+\infty$. The resulting expression makes explicit the convolution structure of the hazard integral: for each $(m, r)$ pair the contribution to $\lambda_I(i^*)$ is a weighted integral of the standard normal PDF $\phi(\varepsilon)$ over the exceedance region, with the joint kernel $f_M(m) \cdot f_R(r)$ providing the weighting. [@Ref001]

**Assembly: particularized annual exceedance rate in epsilon form.** Substituting $f_R(r) = 2r/R^2$, the truncated G-R density $f_M(m)$, the rate $\nu_0 = 10^{a - bM_{\min}}$, and the tail-integral representation of the exceedance probability into the general single-source hazard integral, and noting $R_{\min} = 0$ and $R_{\max} = R$ for the circular source, gives the particularized annual exceedance rate in epsilon form [@Ref001] [@Baker2013]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\; f_M(m)\; \frac{2r}{R^2}\, d\varepsilon\, dr\, dm$$

with $R_{\min} = 0$, $R_{\max} = R$, and $\nu_0 = 10^{a - b\,M_{\min}}$. Factoring the geometric constant $2/R^2$ outside the integral together with $\nu_0$ exposes the core convolution of the standard normal PDF $\phi(\varepsilon)$ with the magnitude distribution kernel $r\,f_M(m)$ over the integration rectangle $[M_{\min}, M_{\max}] \times [R_{\min}, R_{\max}]$. The factored epsilon form is [@Ref001] [@Baker2013]:

$$\lambda_I(i^*) = \frac{2\nu_0}{R^2} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

with $R_{\min} = 0$, $R_{\max} = R$, and $f_M(m)$ given by the truncated G-R expression. For a general GMPE $\hat{\eta}_I(m,r)$, the double integral over $m$ and $r$ does not admit a closed-form solution; numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [0, R]$ is required. The integrand is non-negative throughout the domain, approaches zero as $r \to 0$ because $f_R(r) = 2r/R^2 \to 0$, and decays to zero as $i^*$ grows large relative to $\hat{\eta}_I(m, r)$ for all $(m, r)$ in the domain. [@Ref001] [@Baker2013]

---

## SLOT 2: Canonical Hazard Equations for MCE and Disaggregation

The particularized hazard integral from Slot 1 supports two canonical downstream applications for the single circular areal source: determination of the Maximum Considered Earthquake ground-motion intensity and seismic hazard disaggregation. Both formulations are expressed in terms of the normalized standard normal probability density function $\phi(\varepsilon)$ associated with the ground motion prediction model, building on the epsilon variable $\varepsilon^*(m,r)$ introduced in Slot 1. [@Ref001]

**(a) Maximum Considered Earthquake.** The Maximum Considered Earthquake ground-motion intensity $i^*_{\text{MCE}}$ is the intensity level on the hazard curve at which the annual exceedance rate $\lambda_I(i^*)$ equals a prescribed target rate $\lambda^*$ linked to a design return period $T_R$. Under the Poisson occurrence assumption, the annual exceedance probability is related to the rate by [@Ref001] [@Baker2013]:

$$P_{1\text{yr}}[I > i^*] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

For a target return period $T_R$, the multi-year exceedance probability follows from the same Poisson model [@Ref001]:

$$P_{T_R}[I > i^*] = 1 - \exp\!\left[-\lambda_I(i^*)\, T_R\right]$$

Setting the annual exceedance probability to $\text{AEP} = 1/T_R$ and inverting for the target rate yields [@Ref001]:

$$\lambda^* \equiv -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ is accurate for return periods large compared to unity and constitutes the standard engineering approximation in PSHA. The MCE intensity $i^*_{\text{MCE}}$ is defined implicitly as the solution to $\lambda_I(i^*_{\text{MCE}}) = \lambda^*$; because the full hazard integral from Slot 1 requires numerical evaluation for a general GMPE, the inversion of the hazard curve to recover $i^*_{\text{MCE}}$ likewise requires numerical methods. [@Ref001]

The canonical MCE hazard equation in epsilon form conditions on an event of magnitude $M_{\max}$ at a representative source-to-site distance $r$. The conditional exceedance probability expressed as a tail integral over $\varepsilon$ is [@Ref001]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max}, r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

where $\varepsilon^*(M_{\max}, r) = (\ln i^* - \ln\hat{\eta}_I(M_{\max}, r))/\sigma_{\ln I}$. Setting this probability equal to the target AEP $= 1/T_R$ and inverting the standard normal CDF relationship yields the closed-form MCE expression [@McGuire1995] [@Ref001]:

$$i^*_{\text{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\Phi^{-1}\!\!\left(1 - \frac{1}{T_R}\right)\right]$$

The quantity $\varepsilon^*_{\text{MCE}} = \Phi^{-1}(1 - 1/T_R)$ is the number of logarithmic standard deviations above the median prediction at which $i^*_{\text{MCE}}$ lies; for large $T_R$ this value is positive and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995]. The representative distance $r$ in the MCE formulation requires explicit specification; the mean epicentral distance $\bar{r} = 2R/3$, obtained by integrating $r$ against $f_R(r) = 2r/R^2$ over $[0, R]$, is one geometrically consistent choice derived directly from the circular source distance PDF, while the modal magnitude-distance scenario from disaggregation provides a hazard-consistent alternative. [@Ref001]

**(b) Seismic hazard disaggregation: M-R plane.** Seismic hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from individual scenario bins defined by magnitude, distance, and GMPE residual, producing the conditional distribution over seismic scenarios given that intensity $i^*$ is exceeded. For the single circular source, the critical GMPE residual threshold for scenario $(m, r)$ - the minimum residual for which intensity exceeds $i^*$ - is [@Ref001]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized residual $\varepsilon \geq \varepsilon^*(m, r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute little to the hazard at intensity level $i^*$. The joint exceedance rate for magnitude bin $m_k$ and distance bin $r_j$, expressed in full epsilon form using $f_R(r) = 2r/R^2$, is [@BazzurroCornell1999] [@Ref001]:

$$\lambda_{k,j}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

The fractional contribution of bin $(m_k, r_j)$ to the total annual exceedance rate $\lambda_I(i^*)$ is [@BazzurroCornell1999] [@Ref001]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights $\theta_{k,j}$ satisfy $\sum_k \sum_j \theta_{k,j} = 1$ by construction. Both the bin rate $\lambda_{k,j}(i^*)$ and the total rate $\lambda_I(i^*)$ require numerical integration for a general GMPE; the modal scenario $(m_k^*, r_j^*)$ is the bin for which $\theta_{k,j}$ attains its maximum, identifying the magnitude-distance combination that contributes most to hazard at intensity level $i^*$. [@Ref001]

**(c) Seismic hazard disaggregation: full $(M, R, \varepsilon)$ form.** For the full three-dimensional disaggregation including the GMPE residual dimension, the exceedance rate contribution from bin $(m_k, r_j, \varepsilon_\ell)$ with $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ is, in canonical epsilon form [@BazzurroCornell1999] [@Ref001]:

$$\lambda_{k,j,\ell}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\, f_M(m) \int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, d\varepsilon\, dr\, dm$$

The inner integral over the epsilon bin $[\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ admits a closed-form evaluation in terms of the standard normal CDF [@BazzurroCornell1999] [@Ref001]:

$$\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\,\phi(\varepsilon)\,d\varepsilon = \Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right), \quad \varepsilon_\ell^{\rm hi} > \varepsilon^*(m,r)$$

and equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m,r)$, because no residual in the bin is sufficient to produce exceedance. The remaining integrals over $m$ and $r$ within each bin require numerical quadrature. [@Ref001]

The joint conditional disaggregation probability for bin $(m_k, r_j, \varepsilon_\ell)$, normalized by the total exceedance rate, is [@BazzurroCornell1999] [@Ref001]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k \sum_j \sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal conditional distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining bin indices [@Ref001]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j}\, \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger epicentral distances, while the GMPE attenuates exceedance probability with increasing distance; the marginal conditional distribution $P[R \in r_j \mid I > i^*]$ reflects the balance of these competing geometric and attenuation effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE. [@Ref001] [@BazzurroCornell1999]
