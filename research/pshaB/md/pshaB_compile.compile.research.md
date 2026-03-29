# Probabilistic Seismic Hazard Analysis for a Single Circular Areal Source: Derivation and Canonical Hazard Equations

## SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

The particularization of the general PSHA hazard integral to the single circular areal source begins by identifying four components of the integrand: the annual occurrence rate $\nu_0$, the truncated Gutenberg-Richter magnitude probability density function $f_M(m)$, the conditional ground-motion exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$ appropriate to the circular source geometry. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, minimum engineering magnitude $M_{\min}$, maximum magnitude $M_{\max}$, and a uniform spatial distribution of seismicity over a disk of radius $R$ centered on the study site; contributions from any source beyond radius $R$ are negligible by assumption, and the integration domain in distance reduces to $[0, R]$. No specific ground motion prediction equation is assumed, and no site effects are included; the analysis applies to reference rock conditions throughout [@Baker2013][@Kramer1996][@KBhazard].

Reducing the general multi-source hazard sum to the single circular source, the particularized annual exceedance rate takes the form [@KBhazard]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

where $R_{\min} = 0$ and $R_{\max} = R$ are the inner and outer radial integration limits imposed by the circular source geometry centered on the site.

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence relation $\log_{10} N(M) = a - bM$, where $N(M)$ is the mean annual number of earthquakes at or above magnitude $M$, is evaluated at the engineering minimum magnitude $M_{\min}$ to yield the annual occurrence rate [@KBhazard]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

The parameters $a$ and $b$ are the activity rate and slope of the Gutenberg-Richter relation; $\nu_0$ is the only dimensioned quantity with units of events per year and is factored outside all subsequent integrals.

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude density is obtained by normalizing the Gutenberg-Richter density over the engineering support $[M_{\min}, M_{\max}]$. Evaluating the normalization denominator and canceling common factors yields the closed-form truncated Gutenberg-Richter PDF [@Kramer1996][@KBhazard]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ is the normalization constant ensuring that $f_M(m)$ integrates to unity over $[M_{\min}, M_{\max}]$, confirming proper normalization as a probability density.

**Component (iii): Distance PDF for the circular source.** For a site at the center of a circular areal source with spatially uniform seismicity, the probability that an earthquake originates within the annular ring at distance $r$ from the site is proportional to the ring area $2\pi r\, dr$ divided by the total disk area $\pi R^2$. This ratio directly yields the distance probability density function [@Baker2013][@KBhazard]:

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

The density is monotonically increasing in $r$, reflecting the geometric fact that more source area lies at larger epicentral distances from the central site. Under the uniform seismicity assumption, earthquake locations are spatially independent of earthquake magnitude, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R\mid M}(r\mid m) = f_R(r)$. This spatial independence carries through all subsequent integrals without modification.

**Component (iv): Conditional exceedance probability.** No specific GMPE is assumed. The ground-motion intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m, r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions. The conditional probability that intensity $I$ exceeds target level $i^*$ given magnitude $m$ and source-to-site distance $r$ is [@Kramer1996][@KBhazard]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. The signed logarithmic residual threshold is defined as:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

so that $P[I > i^* \mid m, r] = 1 - \Phi(\varepsilon^*(m, r))$. The quantity $\varepsilon^*(m, r)$ is the number of logarithmic standard deviations by which the target intensity $i^*$ lies above the GMPE median for scenario $(m, r)$. When $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly $0.5$; exceedance becomes increasingly improbable as $\varepsilon^*(m,r)$ increases.

**Epsilon reformulation of the exceedance probability.** The complementary standard normal CDF is represented as the tail integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$. This identity is exact for all finite threshold values [@KBhazard]:

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon$$

This representation converts the two-dimensional hazard integral into a triple integral over the domain $(m, r, \varepsilon)$, with $\varepsilon$ integrated from the scenario-dependent lower limit $\varepsilon^*(m,r)$ to $+\infty$. The resulting expression makes explicit the convolution structure of the hazard integral: for each $(m, r)$ pair the contribution to $\lambda_I(i^*)$ is a weighted integral of the standard normal PDF $\phi(\varepsilon)$ over the exceedance region, with the joint kernel $f_M(m) \cdot f_R(r)$ providing the weighting.

**Assembly: particularized annual exceedance rate in epsilon form.** Substituting $f_R(r) = 2r/R^2$, the truncated Gutenberg-Richter density $f_M(m)$, the rate $\nu_0 = 10^{a - bM_{\min}}$, and the tail-integral representation of the exceedance probability into the general single-source hazard integral, and noting $R_{\min} = 0$ and $R_{\max} = R$, gives the intermediate epsilon form [@Baker2013][@KBhazard]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\; f_M(m)\; \frac{2r}{R^2}\, d\varepsilon\, dr\, dm$$

Substituting the explicit form of $f_M(m)$ and factoring all constant terms outside the triple integral produces the fully factored particularized annual exceedance rate [@Baker2013][@KBhazard]:

$$\lambda_I(i^*) = \frac{2\,\nu_0\, b\ln 10}{R^2\!\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\; 10^{-b(m-M_{\min})}\; r\; d\varepsilon\; dr\; dm$$

with $R_{\min} = 0$ and $R_{\max} = R$. All terms outside the triple integral are constants determined by the source parameters $a$, $b$, $M_{\min}$, $M_{\max}$, and source radius $R$. The core integrand $\phi(\varepsilon) \cdot 10^{-b(m-M_{\min})} \cdot r$ constitutes a convolution of the standard normal PDF $\phi(\varepsilon)$ with the unnormalized Gutenberg-Richter magnitude distribution $10^{-b(m-M_{\min})}$, modulated by the geometric weight $r$ from the circular source distance PDF. The lower limit of the $\varepsilon$ integral, $\varepsilon^*(m,r)$, depends on both $m$ and $r$ through the GMPE median $\hat{\eta}_I(m,r)$; for a general GMPE this dependence prevents closed-form evaluation, and numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [0, R]$ is required. The integrand is non-negative throughout the domain, approaches zero as $r \to 0$ because $f_R(r) = 2r/R^2 \to 0$, and decays to zero as $i^*$ grows large relative to $\hat{\eta}_I(m, r)$ for all $(m, r)$ in the domain.

## SLOT 2: Canonical hazard equations for MCE and disaggregation

The epsilon-form hazard rate derived above supports two canonical downstream applications: determination of the Maximum Considered Earthquake (MCE) ground-motion intensity and seismic hazard disaggregation. Both formulations are expressed in terms of the normalized standard normal PDF $\phi(\varepsilon)$ and the critical residual threshold $\varepsilon^*(m, r)$ introduced in the preceding derivation [@KBhazard].

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
