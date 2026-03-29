## SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

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

