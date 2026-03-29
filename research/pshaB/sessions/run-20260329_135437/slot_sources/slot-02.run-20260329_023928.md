## SLOT 2: Canonical hazard equations for MCE and disaggregation

The particularized hazard integral from Slot 1 supports two canonical downstream applications for the single circular areal source: determination of the Maximum Considered Earthquake ground-motion intensity and seismic hazard disaggregation. Both formulations are expressed in terms of the normalized standard normal probability density function $\phi(\varepsilon)$ associated with the ground motion prediction model, building on the epsilon variable $\varepsilon^*(m,r)$ introduced in Slot 1. [KB:hazard.md]^[Confidence: HIGH, Rationale: The KB develops both the MCE formulation and the disaggregation framework as downstream applications of the hazard integral in separate dedicated sections; both use $\varepsilon^*(m,r)$ and $\phi(\varepsilon)$ as the central quantities, consistent with the Slot 1 derivation.]

**(a) Maximum Considered Earthquake.** The Maximum Considered Earthquake ground-motion intensity $i^*_{\text{MCE}}$ is the intensity level on the hazard curve at which the annual exceedance rate $\lambda_I(i^*)$ equals a prescribed target rate $\lambda^*$ linked to a design return period $T_R$. Under the Poisson occurrence assumption, the annual exceedance probability is related to the rate by [KB:hazard.md] [@Baker2013]:

$$P_{1\text{yr}}[I > i^*] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

For a target return period $T_R$, the multi-year exceedance probability follows from the same Poisson model [KB:hazard.md]:

$$P_{T_R}[I > i^*] = 1 - \exp\!\left[-\lambda_I(i^*)\, T_R\right]$$

Setting the annual exceedance probability to $\text{AEP} = 1/T_R$ and inverting for the target rate yields [KB:hazard.md]:

$$\lambda^* \equiv -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ is accurate for return periods large compared to unity and constitutes the standard engineering approximation in PSHA. The MCE intensity $i^*_{\text{MCE}}$ is defined implicitly as the solution to $\lambda_I(i^*_{\text{MCE}}) = \lambda^*$; because the full hazard integral from Slot 1 requires numerical evaluation for a general GMPE, the inversion of the hazard curve to recover $i^*_{\text{MCE}}$ likewise requires numerical methods. [KB:hazard.md]^[Confidence: HIGH, Rationale: The Poisson AEP-rate relationship, the multi-year exceedance probability, and the return period approximation are all stated in the KB; the implicit definition of $i^*_{\text{MCE}}$ and the need for numerical inversion follow from the non-closed-form character of the hazard integral established in Slot 1.]

The canonical MCE hazard equation in epsilon form conditions on an event of magnitude $M_{\max}$ at a representative source-to-site distance $r$. The conditional exceedance probability expressed as a tail integral over $\varepsilon$ is [KB:hazard.md]:

$$P\!\left[I > i^* \mid M_{\max}, r\right] = \int_{\varepsilon^*(M_{\max}, r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon = 1 - \Phi\!\left(\varepsilon^*(M_{\max}, r)\right)$$

where $\varepsilon^*(M_{\max}, r) = (\ln i^* - \ln\hat{\eta}_I(M_{\max}, r))/\sigma_{\ln I}$. Setting this probability equal to the target AEP $= 1/T_R$ and inverting the standard normal CDF relationship yields the closed-form MCE expression [@McGuire1995] [KB:hazard.md]:

$$i^*_{\text{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\Phi^{-1}\!\!\left(1 - \frac{1}{T_R}\right)\right]$$

The quantity $\varepsilon^*_{\text{MCE}} = \Phi^{-1}(1 - 1/T_R)$ is the number of logarithmic standard deviations above the median prediction at which $i^*_{\text{MCE}}$ lies; for large $T_R$ this value is positive and increases monotonically with $T_R$, consistent with the expectation that rarer ground-motion levels correspond to above-median GMPE residuals [@McGuire1995]. The representative distance $r$ in the MCE formulation requires explicit specification; the mean epicentral distance $\bar{r} = 2R/3$, obtained by integrating $r$ against $f_R(r) = 2r/R^2$ over $[0, R]$, is one geometrically consistent choice derived directly from the circular source distance PDF, while the modal magnitude-distance scenario from disaggregation provides a hazard-consistent alternative. [KB:hazard.md]^[Confidence: HIGH, Rationale: The closed-form MCE expression is derived algebraically from the lognormal exceedance probability and stated in the KB with attribution to McGuire (1995); the mean epicentral distance $\bar{r} = 2R/3$ is computed in the KB by integrating $r$ against the circular source distance PDF. The epsilon interpretation is consistent throughout the KB.]

**(b) Seismic hazard disaggregation: M-R plane.** Seismic hazard disaggregation decomposes the total annual exceedance rate $\lambda_I(i^*)$ into contributions from individual scenario bins defined by magnitude, distance, and GMPE residual, producing the conditional distribution over seismic scenarios given that intensity $i^*$ is exceeded. For the single circular source, the critical GMPE residual threshold for scenario $(m, r)$ - the minimum residual for which intensity exceeds $i^*$ - is [KB:hazard.md]:

$$\varepsilon^*(m, r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

Exceedance of $i^*$ from scenario $(m, r)$ is possible only when the realized residual $\varepsilon \geq \varepsilon^*(m, r)$; scenarios for which $\varepsilon^*(m,r)$ is large contribute little to the hazard at intensity level $i^*$. The joint exceedance rate for magnitude bin $m_k$ and distance bin $r_j$, expressed in full epsilon form using $f_R(r) = 2r/R^2$, is [@BazzurroCornell1999] [KB:hazard.md]:

$$\lambda_{k,j}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\; f_M(m) \int_{\varepsilon^*(m,r)}^{+\infty} \phi(\varepsilon)\, d\varepsilon\; dr\, dm$$

The fractional contribution of bin $(m_k, r_j)$ to the total annual exceedance rate $\lambda_I(i^*)$ is [@BazzurroCornell1999] [KB:hazard.md]:

$$\theta_{k,j} = \frac{\lambda_{k,j}(i^*)}{\lambda_I(i^*)}$$

The weights $\theta_{k,j}$ satisfy $\sum_k \sum_j \theta_{k,j} = 1$ by construction. Both the bin rate $\lambda_{k,j}(i^*)$ and the total rate $\lambda_I(i^*)$ require numerical integration for a general GMPE; the modal scenario $(m_k^*, r_j^*)$ is the bin for which $\theta_{k,j}$ attains its maximum, identifying the magnitude-distance combination that contributes most to hazard at intensity level $i^*$. [KB:hazard.md]^[Confidence: HIGH, Rationale: The M-R disaggregation expressions are reproduced directly from the KB with attribution to Bazzurro and Cornell (1999); the epsilon form is obtained by applying the same tail-integral substitution used in Slot 1. The normalization property and the modal scenario identification are explicitly stated in the KB.]

**(c) Seismic hazard disaggregation: full $(M, R, \varepsilon)$ form.** For the full three-dimensional disaggregation including the GMPE residual dimension, the exceedance rate contribution from bin $(m_k, r_j, \varepsilon_\ell)$ with $\varepsilon_\ell = [\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ is, in canonical epsilon form [@BazzurroCornell1999] [KB:hazard.md]:

$$\lambda_{k,j,\ell}(i^*) = \frac{2\nu_0}{R^2} \int_{m_k}\!\int_{r_j} r\, f_M(m) \int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, d\varepsilon\, dr\, dm$$

The inner integral over the epsilon bin $[\varepsilon_\ell^{\rm lo}, \varepsilon_\ell^{\rm hi}]$ admits a closed-form evaluation in terms of the standard normal CDF [@BazzurroCornell1999] [KB:hazard.md]:

$$\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\,\phi(\varepsilon)\,d\varepsilon = \Phi\!\left(\varepsilon_\ell^{\rm hi}\right) - \Phi\!\left(\max\!\left(\varepsilon_\ell^{\rm lo},\, \varepsilon^*(m,r)\right)\right), \quad \varepsilon_\ell^{\rm hi} > \varepsilon^*(m,r)$$

and equals zero when $\varepsilon_\ell^{\rm hi} \leq \varepsilon^*(m,r)$, because no residual in the bin is sufficient to produce exceedance. The remaining integrals over $m$ and $r$ within each bin require numerical quadrature. [KB:hazard.md]^[Confidence: HIGH, Rationale: The three-dimensional disaggregation rate and the closed-form evaluation of the epsilon-bin integral are reproduced exactly from the KB; the zero result for bins entirely below the critical threshold is a direct consequence of the indicator function and is confirmed in the KB.]

The joint conditional disaggregation probability for bin $(m_k, r_j, \varepsilon_\ell)$, normalized by the total exceedance rate, is [@BazzurroCornell1999] [KB:hazard.md]:

$$\theta_{k,j,\ell} = P\!\left[M \in m_k,\, R \in r_j,\, \varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$

The completeness condition $\sum_k \sum_j \sum_\ell \theta_{k,j,\ell} = 1$ holds by construction. Marginal conditional distributions over magnitude, distance, and residual are obtained by summing $\theta_{k,j,\ell}$ over the remaining bin indices [KB:hazard.md]:

$$P\!\left[M \in m_k \mid I > i^*\right] = \sum_{j}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[R \in r_j \mid I > i^*\right] = \sum_{k}\sum_{\ell}\, \theta_{k,j,\ell}$$

$$P\!\left[\varepsilon \in \varepsilon_\ell \mid I > i^*\right] = \sum_{k}\sum_{j}\, \theta_{k,j,\ell}$$

For the circular source, the distance PDF $f_R(r) = 2r/R^2$ concentrates probability at larger epicentral distances, while the GMPE attenuates exceedance probability with increasing distance; the marginal conditional distribution $P[R \in r_j \mid I > i^*]$ reflects the balance of these competing geometric and attenuation effects and is generally peaked at some intermediate distance, requiring numerical evaluation for any specific GMPE. [KB:hazard.md] [@BazzurroCornell1999]^[Confidence: HIGH, Rationale: The marginal summation formulas and the completeness condition are reproduced exactly from the KB; the competing-effects observation on the conditional distance distribution is stated in the KB and follows directly from the mathematical structure of the integrand, where $f_R(r) \propto r$ and the GMPE-based exceedance probability decreases with distance.]
