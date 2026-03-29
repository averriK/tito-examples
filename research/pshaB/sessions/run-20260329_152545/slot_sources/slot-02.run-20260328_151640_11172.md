## SLOT 2: Canonical hazard equations for MCE and disaggregation

For a target annual exceedance probability (AEP) or return period $T_R$, the MCE ground motion level $i^*_{\mathrm{MCE}}$ is defined implicitly by setting the annual exceedance rate from the epsilon-form hazard integral equal to $-\ln(1-\mathrm{AEP})$, so the MCE value is obtained by numerical inversion of the hazard curve for a general GMPE.[KB:hazard.md]^[Confidence: HIGH, Rationale: The KB defines the AEP relation to the annual exceedance rate and states that numerical evaluation and inversion are required for the general hazard integral, which directly supports the statement.]

$$\lambda_I(i^*_{\mathrm{MCE}}) = \frac{2\nu_0\, b\ln 10}{R^2\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{0}^{R} \int_{\varepsilon^*(m,r)}^{\infty} 10^{-b(m - M_{\min})}\, \phi(\varepsilon)\, r\, d\varepsilon\, dr\, dm$$

$$\lambda_I(i^*_{\mathrm{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right)$$

For a conditional MCE scenario at magnitude $M_{\max}$ and distance $r$, the lognormal GMPE gives a closed-form expression in terms of the residual quantile, with $\varepsilon_{\mathrm{MCE}} = \Phi^{-1}(1-\mathrm{AEP})$ and $i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max},r)\exp\!\left(\sigma_{\ln I}\varepsilon_{\mathrm{MCE}}\right)$; any application must still specify the representative distance $r$.[KB:hazard.md][@McGuire1995]^[Confidence: HIGH, Rationale: The KB provides the closed-form inversion for a lognormal GMPE at $M_{\max}$, defines the residual quantile, and notes the need to specify a representative distance, supporting this paragraph.]

$$\varepsilon_{\mathrm{MCE}} = \Phi^{-1}\!\left(1 - \mathrm{AEP}\right) = \Phi^{-1}\!\left(1 - \frac{1}{T_R}\right)$$

$$i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max},r)\exp\!\left(\sigma_{\ln I}\varepsilon_{\mathrm{MCE}}\right)$$

The canonical disaggregation equation in epsilon form defines the exceedance threshold $\varepsilon^*(m,r)$ and the differential contribution of a scenario $(m,r,\varepsilon)$ using the standard normal PDF, the magnitude density, and the circular distance density.[KB:hazard.md][@BazzurroCornell1999]^[Confidence: HIGH, Rationale: The KB disaggregation section defines the epsilon threshold and the differential exceedance rate using the standard normal PDF and the joint magnitude-distance densities for the circular source.]

$$\varepsilon^*(m,r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

$$\Delta\lambda_I(i^*, m, r, \varepsilon) = \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, f_M(m)\, \frac{2r}{R^2}\, \nu_0$$

Disaggregation over magnitude, distance, and residual bins is obtained by integrating the differential rate over bin ranges and normalizing by the total hazard; the remaining integrals over $m$ and $r$ require numerical quadrature for a generic GMPE.[KB:hazard.md][@BazzurroCornell1999]^[Confidence: HIGH, Rationale: The KB provides the bin-integrated disaggregation rates and the normalized conditional probabilities and notes numerical integration requirements, supporting the paragraph.]

$$\lambda_{k,j,\ell}(i^*) = \nu_0 \int_{m_k}\!\int_{r_j}\!\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, f_M(m)\, \frac{2r}{R^2}\, d\varepsilon\, dr\, dm$$

$$\theta_{k,j,\ell} = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$
