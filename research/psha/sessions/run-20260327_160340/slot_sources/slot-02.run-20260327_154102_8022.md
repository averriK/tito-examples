## SLOT 2: Particularized annual exceedance rate for the single circular source

The general annual exceedance rate for ground-motion level $i^*$ at a site is given by the hazard integral, which integrates over all possible earthquake magnitudes and distances weighted by their respective probability densities and the conditional probability of exceeding the intensity level. For the particularized case of a single circular areal source with uniform seismicity, the hazard integral takes on a specific form that incorporates the distance probability density function derived in Slot 1 and the magnitude distribution defined by the Gutenberg-Richter relation. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This description synthesizes the general PSHA framework from KB:hazard.qmd with the specific source geometry. The approach of particularizing the general integral to specific source models is consistent with standard PSHA methodology.]

The annual occurrence rate of earthquakes above the minimum engineering magnitude $M_{\min}$ for the source is defined as follows. [KB:uncertainty_model.qmd]

^[Confidence: HIGH, Rationale: The framework for defining occurrence rates is established in KB:uncertainty_model.qmd, which provides the foundation for the Gutenberg-Richter relationship used in the next equation.]

$$
\nu_0 = 10^{a - b\,M_{\min}},
$$

where $a$ and $b$ are the Gutenberg-Richter parameters characterizing the seismicity of the source, and the relationship $\nu_0 = N(M_{\min})$ gives the mean number of earthquakes per year exceeding magnitude $M_{\min}$. [KB:uncertainty_model.qmd]

^[Confidence: HIGH, Rationale: This is the standard Gutenberg-Richter occurrence rate formula (eq-branch-rate in KB:uncertainty_model.qmd). The parameters $a$ and $b$ are the standard activity and b-value parameters of the Gutenberg-Richter relation, and this formulation is fundamental to seismic hazard analysis. The definition of $\nu_0$ as the annual rate above $M_{\min}$ is consistent with the PSHA framework.]

The magnitude probability density function, accounting for truncation at the maximum earthquake magnitude $M_{\max}$, follows the truncated Gutenberg-Richter model as formulated in the uncertainty framework. [KB:uncertainty_model.qmd]

^[Confidence: HIGH, Rationale: KB:uncertainty_model.qmd provides the framework for magnitude distributions in PSHA, including the truncation at $M_{\max}$ which is necessary for bounded recurrence relations.]

$$
f_M(m) = \frac{b\ln 10 \cdot 10^{a - b m}}{\displaystyle\int_{M_{\min}}^{M_{\max}} 10^{a - b u}\,du}, \quad M_{\min} \le m \le M_{\max}.
$$

This is the exact formulation provided in KB:uncertainty_model.qmd (eq-branch-pdf), which represents the normalized truncated Gutenberg-Richter magnitude distribution. It integrates to unity over the domain $[M_{\min}, M_{\max}]$, ensuring proper probabilistic interpretation.

^[Confidence: HIGH, Rationale: The mathematical normalization and integration properties of this distribution are straightforward to verify. The formulation matches the source citation exactly.]

The conditional exceedance probability for ground-motion parameter $I$ at intensity level $i^*$, given an earthquake of magnitude $m$ at distance $r$, is expressed through a generic ground-motion prediction equation (GMPE). Following standard PSHA formulations, this probability is: [KB:uncertainty_model.qmd]

^[Confidence: HIGH, Rationale: The conditional exceedance probability framework is standard in PSHA and is documented in KB:uncertainty_model.qmd. Using a generic GMPE formulation allows the derivation to remain general.]

$$
P[I > i^* \mid m, r] = 1 - \Phi\!\left(\frac{\ln i^* - \ln \hat{\eta}_I(m,r)}{\sigma_{\ln I}}\right),
$$

where $\hat{\eta}_I(m,r)$ is the median ground-motion intensity predicted by the GMPE for magnitude $m$ and distance $r$, $\sigma_{\ln I}$ is the logarithmic standard deviation (dispersion) characterizing the aleatory variability in ground-motion prediction, and $\Phi(\cdot)$ is the standard normal cumulative distribution function. [KB:uncertainty_model.qmd]

^[Confidence: HIGH, Rationale: This formulation (eq-branch-exc in KB:uncertainty_model.qmd) expresses the exceedance probability using the log-normal cumulative distribution function. All variables are properly defined and the relationship is consistent with standard GMPE usage in PSHA.]

The particularized hazard integral for the single circular areal source is obtained by substituting the distance probability density function $f_R(r) = 2r/R^2$, the magnitude probability density function $f_M(m)$, and the conditional exceedance probability into the general hazard integral. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This description of the substitution process is consistent with how the general PSHA integral (eq-hazard-integral in KB:hazard.qmd) is particularized to specific source geometries and magnitude distributions.]

$$
\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_0^R P[I > i^* \mid m, r]\, f_M(m)\, f_R(r)\,dr\,dm.
$$

The result is obtained by direct substitution of the three density functions and occurrence rate into the framework established by KB:hazard.qmd.

^[Confidence: HIGH, Rationale: This is the direct particularization of the general hazard integral (eq-hazard-integral from KB:hazard.qmd) to the circular source case. The limits of integration over distance are $[0, R]$ corresponding to the circular source radius, and the distance PDF $f_R(r) = 2r/R^2$ replaces the general distance distribution. The magnitude integral remains over $[M_{\min}, M_{\max}]$. This formulation preserves the structure and interpretation of the general PSHA integral while specializing it to the uniform circular source geometry.]

Expanding this expression and recognizing that $f_R(r) = 2r/R^2$, the annual exceedance rate becomes: [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: The algebraic expansion extracts the geometric factor from the distance PDF, making the structure of the hazard integral more explicit.]

$$
\lambda_I(i^*) = \frac{2\nu_0}{R^2} \int_{M_{\min}}^{M_{\max}} \int_0^R P[I > i^* \mid m, r]\, f_M(m)\, r\,dr\,dm.
$$

This form explicitly shows the geometric factor $2/R^2$ arising from the uniform circular source geometry, combined with the radial weighting $r$ in the integral. The integral must be evaluated numerically for realistic GMPEs, as the conditional exceedance probability $P[I > i^* \mid m, r]$ is typically specified through empirical or semi-empirical functions that do not permit closed-form integration in general. For specific GMPE functional forms and magnitude-distance relationships, partial analytical solutions may be possible, but the general form requires numerical integration.

^[Confidence: HIGH, Rationale: The algebraic transformation is correct and the observation about numerical integration requirements is consistent with standard PSHA practice. Most realistic GMPEs involve transcendental functions that prevent closed-form analytical integration.]

