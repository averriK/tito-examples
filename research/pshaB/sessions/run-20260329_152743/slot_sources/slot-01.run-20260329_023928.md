## SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

The particularization of the general PSHA hazard integral to the single circular areal source begins by identifying four components of the integrand: the annual occurrence rate $\nu_0$, the truncated Gutenberg-Richter magnitude probability density function $f_M(m)$, the conditional ground-motion exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$ appropriate to the circular source geometry. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, minimum engineering magnitude $M_{\min}$, maximum magnitude $M_{\max}$, and a uniform spatial distribution of seismicity over a disk of radius $R$ centered on the study site; contributions from any source beyond radius $R$ are negligible by assumption, and the integration domain in distance reduces to $[0, R]$. [KB:hazard.md]^[Confidence: HIGH, Rationale: The source characterization and the enumeration of the four integrand components are stated identically in the KB section "Particularized Annual Exceedance Rate for the Single Circular Source"; all parameters are defined consistently with the task context and with standard PSHA methodology.]

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence law $\log_{10} N(M) = a - bM$ specifies the mean annual number of earthquakes $N(M)$ at or above magnitude $M$. Evaluating at the engineering minimum magnitude $M_{\min}$ yields the scalar prefactor that multiplies the full magnitude-distance integral [KB:hazard.md]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

where $a$ and $b$ are the Gutenberg-Richter activity rate and slope parameters. The rate $\nu_0$ counts the mean annual number of seismically relevant events on the source; it is dimensionally the only quantity with units of events per year and is factored outside all subsequent integrals. [KB:hazard.md]^[Confidence: HIGH, Rationale: The expression for $\nu_0$ is reproduced exactly from the KB and follows directly from evaluating the Gutenberg-Richter law at $M_{\min}$; the factoring step is algebraically exact with no approximation.]

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude probability density function over the engineering range $[M_{\min}, M_{\max}]$ is the truncated Gutenberg-Richter density obtained by normalizing the unnormalized density $10^{-bm}$ over the support and canceling the common factor $10^a$ [@Kramer1996] [KB:hazard.md]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ is the normalization constant ensuring that $f_M(m)$ integrates to unity over $[M_{\min}, M_{\max}]$, confirming proper normalization as a probability density. [KB:hazard.md]^[Confidence: HIGH, Rationale: The truncated G-R magnitude PDF is stated verbatim in the KB with attribution to Kramer (1996); the normalization is confirmed by integrating the expression over the support, yielding unity by construction.]

**Component (iii): Distance probability density function.** The distance probability density function for the circular areal source with the study site at its center is derived from the uniform seismicity assumption: the probability that an earthquake originates in a thin annulus of width $dr$ at epicentral distance $r$ is proportional to the annular area $2\pi r\, dr$ divided by the total disk area $\pi R^2$, giving [@Baker2013] [KB:hazard.md]:

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

Under the uniform seismicity model, epicenter location and earthquake magnitude are spatially independent, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R\mid M}(r\mid m) = f_R(r) = 2r/R^2$. This independence property carries through the full magnitude-distance integral without modification. [KB:hazard.md]^[Confidence: HIGH, Rationale: The distance PDF derivation and the independence property are both established in the KB from first principles; the derivation is geometrically exact for the stated uniform seismicity assumption and is confirmed by Baker (2013) as cited in the KB.]

**Component (iv): Conditional exceedance probability and the epsilon variable.** No specific ground motion prediction equation is assumed; the site-intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m, r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions with no site effects included. The conditional probability of exceeding intensity $i^*$ given an event of magnitude $m$ at distance $r$ is [@Kramer1996] [KB:hazard.md]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. The signed logarithmic residual threshold $\varepsilon^*(m, r)$, defined as the argument of $\Phi$ above, quantifies the minimum number of logarithmic standard deviations above the median prediction at which $i^*$ lies for scenario $(m, r)$ [KB:hazard.md]:

$$\varepsilon^*(m, r) \equiv \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

so that $P[I > i^* \mid m, r] = 1 - \Phi(\varepsilon^*(m, r))$. When $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly $0.5$; exceedance becomes increasingly improbable as $\varepsilon^*(m,r)$ increases. [KB:hazard.md]^[Confidence: HIGH, Rationale: The lognormal ground-motion model and the resulting conditional exceedance probability are stated in the KB and represent standard PSHA methodology; the epsilon notation is introduced consistently with the KB sections on MCE and disaggregation, where $\varepsilon^*(m,r)$ appears as the critical residual threshold throughout.]

**Epsilon reformulation of the exceedance probability.** The key step in the epsilon form of the hazard integral is the replacement of the complementary standard normal CDF by the tail integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$. This identity is exact for all finite values of the threshold [KB:hazard.md]:

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon$$

Substituting this representation into the conditional exceedance probability converts the two-dimensional hazard integral into a triple integral over the domain $(m, r, \varepsilon)$, with $\varepsilon$ integrated from the scenario-dependent lower limit $\varepsilon^*(m,r)$ to $+\infty$. The resulting expression makes explicit the convolution structure of the hazard integral: for each $(m, r)$ pair the contribution to $\lambda_I(i^*)$ is a weighted integral of the standard normal PDF $\phi(\varepsilon)$ over the exceedance region, with the joint kernel $f_M(m) \cdot f_R(r)$ providing the weighting. [KB:hazard.md]^[Confidence: HIGH, Rationale: The tail-integral identity is an exact relation for the standard normal CDF; the interpretation of the resulting triple integral as a convolution of $\phi(\varepsilon)$ with the magnitude-distance kernel follows algebraically and is consistent with the disaggregation framework developed in the KB.]

**Assembly: particularized annual exceedance rate in epsilon form.** Substituting $f_R(r) = 2r/R^2$, the truncated G-R density $f_M(m)$, the rate $\nu_0 = 10^{a - bM_{\min}}$, and the tail-integral representation of the exceedance probability into the general single-source hazard integral, and noting $R_{\min} = 0$ and $R_{\max} = R$ for the circular source, gives the particularized annual exceedance rate in epsilon form [KB:hazard.md] [@Baker2013]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\; f_M(m)\; \frac{2r}{R^2}\, d\varepsilon\, dr\, dm$$

with $R_{\min} = 0$, $R_{\max} = R$, and $\nu_0 = 10^{a - b\,M_{\min}}$. Factoring the geometric constant $2/R^2$ outside the integral together with $\nu_0$ exposes the core convolution of the standard normal PDF $\phi(\varepsilon)$ with the magnitude distribution kernel $r\,f_M(m)$ over the integration rectangle $[M_{\min}, M_{\max}] \times [R_{\min}, R_{\max}]$. The factored epsilon form is [KB:hazard.md] [@Baker2013]:

$$\lambda_I(i^*) = \frac{2\nu_0}{R^2} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

with $R_{\min} = 0$, $R_{\max} = R$, and $f_M(m)$ given by the truncated G-R expression. For a general GMPE $\hat{\eta}_I(m,r)$, the double integral over $m$ and $r$ does not admit a closed-form solution; numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [0, R]$ is required. The integrand is non-negative throughout the domain, approaches zero as $r \to 0$ because $f_R(r) = 2r/R^2 \to 0$, and decays to zero as $i^*$ grows large relative to $\hat{\eta}_I(m, r)$ for all $(m, r)$ in the domain. [KB:hazard.md] [@Baker2013]^[Confidence: HIGH, Rationale: The assembly of the four components is algebraically exact; the factored form, the explicit integration limits, and the statement that numerical quadrature is required for a general GMPE are all reproduced directly from the KB, which provides the complete assembled expression and describes its boundary behavior.]

---

