### SLOT 1: Particularized annual exceedance rate in epsilon form

For a single circular areal source of radius $R$ with uniform seismicity and no site effects, the particularized annual exceedance rate is written in terms of the annual occurrence rate, the truncated Gutenberg-Richter magnitude density, the circular distance density, and a generic lognormal GMPE exceedance model with median $\hat{\eta}_I(m,r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions.[KB:hazard.md][@Baker2013][@Kramer1996]^[Confidence: HIGH, Rationale: The paragraph restates the component definitions and modeling assumptions given in the KB for the circular source, magnitude PDF, distance PDF, and lognormal exceedance model, all directly supported by the cited KB content.]

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{0}^{R} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

$$\nu_0 = 10^{a - b M_{\min}}$$

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

Define the normalized residual $\varepsilon$ and the standard normal PDF $\phi(\varepsilon)$ so that the exceedance probability is expressed as a tail integral of $\phi(\varepsilon)$.[KB:hazard.md]^[Confidence: HIGH, Rationale: The KB explicitly defines the residual form and the use of the standard normal CDF for exceedance, which supports rewriting the exceedance term as a tail integral of the standard normal PDF.]

$$\varepsilon^*(m,r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

$$\phi(\varepsilon) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{\varepsilon^2}{2}\right)$$

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\, d\varepsilon$$

Factoring all constants outside the integral and expressing the exceedance probability in $\varepsilon$ form gives the convolution of the standard normal density with the magnitude distribution, with $R_{\min}=0$ and $R_{\max}=R$ for the circular source; the resulting triple integral over $m$, $r$, and $\varepsilon$ generally requires numerical quadrature for a generic GMPE.[KB:hazard.md][@Baker2013][@Kramer1996]^[Confidence: HIGH, Rationale: The KB provides the circular-source hazard integral, the distance PDF, the truncated Gutenberg-Richter density, and notes that numerical integration is required for a general GMPE, which supports this epsilon-form statement.]

$$\lambda_I(i^*) = \frac{2\nu_0\, b\ln 10}{R^2\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{\infty} 10^{-b(m - M_{\min})}\, \phi(\varepsilon)\, r\, d\varepsilon\, dr\, dm$$

### SLOT 2: Canonical MCE and disaggregation hazard equations

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
