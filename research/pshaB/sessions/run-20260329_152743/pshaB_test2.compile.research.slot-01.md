## SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

The general PSHA hazard integral is particularized to a single circular areal source of radius $R$ centered on the study site. Seismicity within the source is spatially uniform, and contributions from beyond radius $R$ are negligible; the distance integration domain reduces to $[0, R]$. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, engineering minimum magnitude $M_{\min}$, and maximum magnitude $M_{\max}$. Four components of the integrand require explicit specification: the annual occurrence rate $\nu_0$, the truncated Gutenberg-Richter magnitude probability density function $f_M(m)$, the conditional ground-motion exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$ appropriate to the circular source geometry. No specific ground motion prediction equation is assumed; the ground-motion intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m,r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions throughout. [@Baker2013][@Kramer1996][@HazardKB]

Reducing the general multi-source hazard sum to the single circular source, the particularized annual exceedance rate takes the form [@HazardKB]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

where $R_{\min} = 0$ and $R_{\max} = R$ are the inner and outer radial limits imposed by the circular source geometry centered on the site. [@HazardKB]

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence relation $\log_{10} N(M) = a - bM$, where $N(M)$ is the mean annual number of earthquakes at or above magnitude $M$, is evaluated at the engineering minimum magnitude $M_{\min}$ to yield the annual occurrence rate [@HazardKB]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

The parameters $a$ and $b$ are the activity rate and slope of the Gutenberg-Richter relation for the source. The rate $\nu_0$ counts the mean annual number of seismically relevant events on the source and is factored outside all subsequent integrals. [@HazardKB]

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude density is obtained by normalizing the Gutenberg-Richter density over the engineering support $[M_{\min}, M_{\max}]$. Evaluating the normalization denominator and canceling common factors yields the closed-form truncated Gutenberg-Richter PDF [@Kramer1996][@HazardKB]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ is the normalization constant ensuring that $f_M(m)$ integrates to unity over $[M_{\min}, M_{\max}]$. [@HazardKB]

**Component (iii): Distance PDF for the circular source.** For a site at the center of a circular areal source with spatially uniform seismicity, the probability that an earthquake originates within the annular ring at distance $r$ from the site is proportional to the ring area $2\pi r\,dr$ divided by the total disk area $\pi R^2$, yielding [@Baker2013][@HazardKB]:

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

The density is monotonically increasing in $r$, reflecting the geometric fact that more source area lies at larger epicentral distances from the central site. Under the uniform seismicity assumption, earthquake locations are spatially independent of earthquake magnitude, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R|M}(r|m) = f_R(r)$. This independence property carries through the full magnitude-distance integral without modification. [@HazardKB]

**Component (iv): Conditional exceedance probability.** The conditional probability that intensity $I$ exceeds target level $i^*$ given magnitude $m$ and distance $r$ is [@Kramer1996][@HazardKB]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. The signed logarithmic residual threshold $\varepsilon^*(m, r)$, defined as the argument of $\Phi$ above, quantifies the number of logarithmic standard deviations by which the target intensity $i^*$ lies above the GMPE median for scenario $(m, r)$ [@HazardKB]:

$$\varepsilon^*(m, r) \equiv \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

When $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly 0.5; exceedance becomes increasingly improbable as $\varepsilon^*(m,r)$ increases. [@HazardKB]

**Epsilon reformulation.** The key step in the epsilon form of the hazard integral is the replacement of the complementary standard normal CDF by the tail integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$. This identity is exact for all finite values of the threshold [@HazardKB]:

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon$$

Substituting this representation converts the two-dimensional hazard integral into a triple integral over the domain $(m, r, \varepsilon)$, with $\varepsilon$ integrated from the scenario-dependent lower limit $\varepsilon^*(m,r)$ to $+\infty$. This formulation makes explicit the convolution structure of the hazard integral: for each $(m, r)$ pair the contribution to $\lambda_I(i^*)$ is a weighted integral of the standard normal PDF $\phi(\varepsilon)$ over the exceedance region, with the joint kernel $f_M(m) \cdot f_R(r)$ providing the weighting. [@HazardKB]

**Assembly: particularized annual exceedance rate in epsilon form.** Substituting the epsilon tail-integral representation of the exceedance probability and the circular source distance PDF $f_R(r) = 2r/R^2$ into the particularized double integral, and noting $R_{\min} = 0$ and $R_{\max} = R$, yields [@HazardKB][@Baker2013]:

$$\lambda_I(i^*) = \frac{2\nu_0}{R^2} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

Substituting the explicit truncated Gutenberg-Richter density for $f_M(m)$ and factoring all remaining constant terms outside the triple integral produces the final particularized annual exceedance rate in epsilon form [@HazardKB][@Baker2013]:

$$\lambda_I(i^*) = \frac{2\,\nu_0\, b\ln 10}{R^2\!\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\; 10^{-b(m-M_{\min})}\; r\; d\varepsilon\; dr\; dm$$

All terms outside the triple integral are constants determined by the source parameters $a$, $b$, $M_{\min}$, $M_{\max}$, and source radius $R$, with $\nu_0 = 10^{a - b\,M_{\min}}$ substituted explicitly. The core integrand constitutes a convolution of the standard normal PDF $\phi(\varepsilon)$ with the unnormalized Gutenberg-Richter magnitude distribution function $10^{-b(m-M_{\min})}$, modulated by the geometric weight $r$ from the circular source distance PDF. The explicit integration limits are $R_{\min} = 0$, $R_{\max} = R$, $M_{\min}$, and $M_{\max}$; the lower limit of the $\varepsilon$ integral, $\varepsilon^*(m,r)$, depends on both $m$ and $r$ through the GMPE median $\hat{\eta}_I(m,r)$. For a general GMPE, this dependence prevents closed-form evaluation and numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [0, R]$ is required. [@Baker2013][@HazardKB]
