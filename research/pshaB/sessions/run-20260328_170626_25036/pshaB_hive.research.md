# PSHA Equations for a Single Circular Areal Source

## SLOT 1: Derivation of the Particularized Annual Exceedance Rate in Epsilon Form

The configuration examined is a stable continental crust region in which seismicity is represented by a single circular areal source of radius $R$ centered on the study site. Seismicity within the source is spatially uniform, and contributions from beyond radius $R$ are negligible. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, engineering minimum magnitude $M_{\min}$, and maximum earthquake magnitude $M_{\max}$. The general PSHA hazard integral is particularized to this geometry by substituting the distance probability density function appropriate to the circular source geometry, the truncated Gutenberg-Richter magnitude probability density function, and a lognormal conditional exceedance model expressed generically in terms of the GMPE median $\hat{\eta}_I(m,r)$ and logarithmic standard deviation $\sigma_{\ln I}$, with no specific ground motion prediction equation assumed and no site effects included (reference rock conditions throughout) [@Baker2013] [@Kramer1996] [KB:hazard.md].^[Confidence: HIGH, Rationale: The source configuration, uniform seismicity assumption, and Gutenberg-Richter parameterization are all established in [KB:hazard.md]. The generic GMPE treatment and reference rock conditions are stated as constraints consistent with the particularized hazard derivation in [KB:hazard.md]. No claims extend beyond what is directly stated in the KB.]

Reducing the general multi-source hazard sum to the single circular source, the particularized annual exceedance rate takes the form [KB:hazard.md]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

where $R_{\min} = 0$ and $R_{\max} = R$ are the inner and outer radial integration limits imposed by the circular source geometry centered on the site. Four components require explicit specification: the annual occurrence rate $\nu_0$, the magnitude probability density function $f_M(m)$, the conditional exceedance probability $P[I > i^* \mid m, r]$, and the distance probability density function $f_R(r)$. Each is developed in turn below. [KB:hazard.md]^[Confidence: HIGH, Rationale: The reduction to a single-source double integral and the identification of four components are stated explicitly in [KB:hazard.md] in the section on the particularized annual exceedance rate. The integration limits $R_{\min} = 0$ and $R_{\max} = R$ follow directly from the circular source geometry described in [KB:hazard.md].]

**Component (i): Annual occurrence rate.** The Gutenberg-Richter recurrence relation $\log_{10} N(M) = a - bM$, where $N(M)$ is the mean annual number of earthquakes at or above magnitude $M$, is evaluated at the engineering minimum magnitude $M_{\min}$ to yield the annual occurrence rate [KB:hazard.md]:

$$\nu_0 = 10^{a - b\,M_{\min}}$$

The parameters $a$ and $b$ are the activity rate and slope of the Gutenberg-Richter relation for the source. [KB:hazard.md]^[Confidence: HIGH, Rationale: The expression $\nu_0 = 10^{a - b M_{\min}}$ is given verbatim in [KB:hazard.md] as Component (i) in the particularized hazard derivation, consistent with the standard Gutenberg-Richter recurrence law.]

**Component (ii): Truncated Gutenberg-Richter magnitude PDF.** The magnitude density is obtained by normalizing the Gutenberg-Richter density over the engineering support $[M_{\min}, M_{\max}]$. Evaluating the normalization denominator and canceling common factors yields the closed-form truncated Gutenberg-Richter PDF [@Kramer1996] [KB:hazard.md]:

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

Integration of $f_M(m)$ over its support $[M_{\min}, M_{\max}]$ yields unity, confirming proper normalization. The denominator $1 - 10^{-b(M_{\max}-M_{\min})}$ accounts for the finite truncation of the magnitude range at $M_{\max}$. [KB:hazard.md]^[Confidence: HIGH, Rationale: The truncated Gutenberg-Richter PDF is given verbatim in [KB:hazard.md] as Component (ii), attributed to [@Kramer1996]. The normalization property is confirmed in [KB:hazard.md] and follows directly from integrating the expression over the stated support.]

**Component (iii): Distance PDF for the circular source.** For a site at the center of a circular areal source with spatially uniform seismicity, the probability that an earthquake originates within the annular ring at distance $r$ from the site is proportional to the ring area $2\pi r\, dr$ divided by the total disk area $\pi R^2$. This ratio directly yields the distance probability density function [@Baker2013] [KB:hazard.md]:

$$f_R(r) = \frac{2r}{R^2}, \qquad R_{\min} \leq r \leq R_{\max}$$

The density is monotonically increasing in $r$, reflecting the geometric fact that more source area lies at larger epicentral distances from the central site. Under the uniform seismicity assumption, earthquake locations are spatially independent of earthquake magnitude, so the conditional distance distribution given magnitude reduces to the unconditional form: $f_{R|M}(r|m) = f_R(r)$. This spatial independence carries through to all subsequent integrals and is used without further qualification. [KB:hazard.md]^[Confidence: HIGH, Rationale: The derivation of $f_R(r) = 2r/R^2$ from the annular ring area ratio, its monotonicity interpretation, and the spatial independence property $f_{R|M}(r|m) = f_R(r)$ are all stated explicitly in [KB:hazard.md] in the distance PDF section, attributed to [@Baker2013]. No claims extend beyond the KB.]

**Component (iv): Conditional exceedance probability.** No specific GMPE is assumed. The ground-motion intensity $I$ is treated as lognormally distributed with median $\hat{\eta}_I(m, r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions. The conditional probability that intensity $I$ exceeds target level $i^*$ given magnitude $m$ and source-to-site distance $r$ is [@Kramer1996] [KB:hazard.md]:

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. The argument of $\Phi$ is the signed number of logarithmic standard deviations by which $i^*$ lies above the median prediction $\hat{\eta}_I(m,r)$; when $i^* = \hat{\eta}_I(m,r)$ the exceedance probability equals exactly 0.5. [KB:hazard.md]^[Confidence: HIGH, Rationale: The lognormal conditional exceedance probability and its interpretation are given verbatim in [KB:hazard.md] as Component (iii) in the particularized hazard derivation, attributed to [@Kramer1996]. The 0.5 exceedance value at the median is confirmed by [KB:hazard.md].]

The reformulation in terms of the standardized GMPE residual $\varepsilon$ proceeds by introducing the critical threshold:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

This quantity is the number of logarithmic standard deviations by which the target intensity $i^*$ lies above the GMPE median for scenario $(m, r)$. The complementary normal CDF is then represented as an integral of the standard normal probability density function $\phi(\varepsilon) = (2\pi)^{-1/2}\exp(-\varepsilon^2/2)$ over the half-line $[\varepsilon^*(m,r), +\infty)$:

$$1 - \Phi\!\left(\varepsilon^*(m, r)\right) = \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\, d\varepsilon$$

This representation makes explicit the role of $\varepsilon$ as the integration variable, with the lower limit $\varepsilon^*(m,r)$ depending on both $m$ and $r$ through the GMPE median. [KB:hazard.md]^[Confidence: HIGH, Rationale: The epsilon threshold $\varepsilon^*(m,r)$ is defined in [KB:hazard.md] in the disaggregation section and is consistent with the conditional exceedance model in Component (iv). The integral representation of $1 - \Phi(\varepsilon^*)$ is a standard identity: since $\Phi(x) = \int_{-\infty}^x \phi(u)\, du$, the complementary CDF satisfies $1 - \Phi(x) = \int_x^{\infty} \phi(u)\, du$ by the normalization of $\phi$.]

Substituting the integral representation of $1 - \Phi(\varepsilon^*(m,r))$, the distance PDF $f_R(r) = 2r/R^2$, and the spatial independence $f_{R|M}(r|m) = f_R(r)$ into the particularized double integral yields the triple-integral epsilon form of the hazard rate [KB:hazard.md]:

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\; f_M(m)\; \frac{2r}{R^2}\; d\varepsilon\; dr\; dm$$

Substituting the explicit form of $f_M(m)$ and factoring all constant terms outside the triple integral produces the final particularized annual exceedance rate in epsilon form [KB:hazard.md]:

$$\lambda_I(i^*) = \frac{2\,\nu_0\, b\ln 10}{R^2\!\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\; 10^{-b(m-M_{\min})}\; r\; d\varepsilon\; dr\; dm$$

All terms outside the triple integral are constants determined by the source parameters $a$, $b$, $M_{\min}$, $M_{\max}$, and source radius $R$, with $\nu_0 = 10^{a - b\,M_{\min}}$ substituted explicitly. The core integrand $\phi(\varepsilon) \cdot 10^{-b(m-M_{\min})} \cdot r$ constitutes a convolution of the standard normal PDF $\phi(\varepsilon)$ with the unnormalized Gutenberg-Richter magnitude distribution function $10^{-b(m-M_{\min})}$, modulated by the geometric weight $r$ from the circular source distance PDF. The explicit integration limits are $R_{\min} = 0$, $R_{\max} = R$, $M_{\min}$, and $M_{\max}$; the lower limit of the $\varepsilon$ integral, $\varepsilon^*(m,r)$, depends on both $m$ and $r$ through the GMPE median $\hat{\eta}_I(m,r)$. For a general GMPE $\hat{\eta}_I(m,r)$, this dependence prevents closed-form evaluation, and numerical quadrature over the rectangle $[M_{\min}, M_{\max}] \times [R_{\min}, R_{\max}]$ is required to evaluate the integral. [@Baker2013] [KB:hazard.md]^[Confidence: HIGH, Rationale: The factored epsilon form is derived by substituting all four components from [KB:hazard.md] and applying standard algebraic factorization; the intermediate triple-integral step appears in [KB:hazard.md] in the disaggregation section. The requirement for numerical quadrature for a general GMPE is explicitly stated in [KB:hazard.md]. The identification of the core integrand as a convolution of the standard normal PDF with the magnitude distribution is consistent with the factored structure of the equation.]

---

## SLOT 2: Canonical Hazard Equations for MCE and Disaggregation

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
