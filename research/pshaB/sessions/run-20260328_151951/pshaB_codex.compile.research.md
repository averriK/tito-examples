### SLOT 1: Particularized annual exceedance rate in epsilon form

For a single circular areal source of radius $R$ with uniform seismicity and no site effects, the particularized annual exceedance rate is written in terms of the annual occurrence rate, the truncated Gutenberg-Richter magnitude density, the circular distance density, and a generic lognormal GMPE exceedance model with median $\hat{\eta}_I(m,r)$ and logarithmic standard deviation $\sigma_{\ln I}$ under reference rock conditions.[@Ref001][@Baker2013][@Kramer1996]

$$\lambda_I(i^*) = \nu_0 \int_{M_{\min}}^{M_{\max}} \int_{0}^{R} P\!\left[I > i^* \mid m, r\right] f_M(m)\, f_R(r)\, dr\, dm$$

$$\nu_0 = 10^{a - b M_{\min}}$$

$$f_M(m) = \frac{b\ln 10\; 10^{-b(m - M_{\min})}}{1 - 10^{-b(M_{\max}-M_{\min})}}, \qquad M_{\min} \leq m \leq M_{\max}$$

$$f_R(r) = \frac{2r}{R^2}, \qquad 0 \leq r \leq R$$

$$P\!\left[I > i^* \mid m, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}\right)$$

Define the normalized residual $\varepsilon$ and the standard normal PDF $\phi(\varepsilon)$ so that the exceedance probability is expressed as a tail integral of $\phi(\varepsilon)$.[@Ref001]

$$\varepsilon^*(m,r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

$$\phi(\varepsilon) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{\varepsilon^2}{2}\right)$$

$$1 - \Phi\!\left(\varepsilon^*(m,r)\right) = \int_{\varepsilon^*(m,r)}^{\infty} \phi(\varepsilon)\, d\varepsilon$$

Factoring all constants outside the integral and expressing the exceedance probability in $\varepsilon$ form gives the convolution of the standard normal density with the magnitude distribution, with $R_{\min}=0$ and $R_{\max}=R$ for the circular source; the resulting triple integral over $m$, $r$, and $\varepsilon$ generally requires numerical quadrature for a generic GMPE.[@Ref001][@Baker2013][@Kramer1996]

$$\lambda_I(i^*) = \frac{2\nu_0\, b\ln 10}{R^2\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{R_{\min}}^{R_{\max}} \int_{\varepsilon^*(m,r)}^{\infty} 10^{-b(m - M_{\min})}\, \phi(\varepsilon)\, r\, d\varepsilon\, dr\, dm$$

### SLOT 2: Canonical MCE and disaggregation hazard equations

For a target annual exceedance probability (AEP) or return period $T_R$, the MCE ground motion level $i^*_{\mathrm{MCE}}$ is defined implicitly by setting the annual exceedance rate from the epsilon-form hazard integral equal to $-\ln(1-\mathrm{AEP})$, so the MCE value is obtained by numerical inversion of the hazard curve for a general GMPE.[@Ref001]

$$\lambda_I(i^*_{\mathrm{MCE}}) = \frac{2\nu_0\, b\ln 10}{R^2\left(1 - 10^{-b(M_{\max}-M_{\min})}\right)} \int_{M_{\min}}^{M_{\max}} \int_{0}^{R} \int_{\varepsilon^*(m,r)}^{\infty} 10^{-b(m - M_{\min})}\, \phi(\varepsilon)\, r\, d\varepsilon\, dr\, dm$$

$$\lambda_I(i^*_{\mathrm{MCE}}) = -\ln\!\left(1 - \mathrm{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right)$$

For a conditional MCE scenario at magnitude $M_{\max}$ and distance $r$, the lognormal GMPE gives a closed-form expression in terms of the residual quantile, with $\varepsilon_{\mathrm{MCE}} = \Phi^{-1}(1-\mathrm{AEP})$ and $i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max},r)\exp\!\left(\sigma_{\ln I}\varepsilon_{\mathrm{MCE}}\right)$; any application must still specify the representative distance $r$.[@Ref001][@McGuire1995]

$$\varepsilon_{\mathrm{MCE}} = \Phi^{-1}\!\left(1 - \mathrm{AEP}\right) = \Phi^{-1}\!\left(1 - \frac{1}{T_R}\right)$$

$$i^*_{\mathrm{MCE}} = \hat{\eta}_I(M_{\max},r)\exp\!\left(\sigma_{\ln I}\varepsilon_{\mathrm{MCE}}\right)$$

The canonical disaggregation equation in epsilon form defines the exceedance threshold $\varepsilon^*(m,r)$ and the differential contribution of a scenario $(m,r,\varepsilon)$ using the standard normal PDF, the magnitude density, and the circular distance density.[@Ref001][@BazzurroCornell1999]

$$\varepsilon^*(m,r) = \frac{\ln i^* - \ln\hat{\eta}_I(m, r)}{\sigma_{\ln I}}$$

$$\Delta\lambda_I(i^*, m, r, \varepsilon) = \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, f_M(m)\, \frac{2r}{R^2}\, \nu_0$$

Disaggregation over magnitude, distance, and residual bins is obtained by integrating the differential rate over bin ranges and normalizing by the total hazard; the remaining integrals over $m$ and $r$ require numerical quadrature for a generic GMPE.[@Ref001][@BazzurroCornell1999]

$$\lambda_{k,j,\ell}(i^*) = \nu_0 \int_{m_k}\!\int_{r_j}\!\int_{\varepsilon_\ell} \mathbf{1}_{\{\varepsilon \geq \varepsilon^*(m,r)\}}\, \phi(\varepsilon)\, f_M(m)\, \frac{2r}{R^2}\, d\varepsilon\, dr\, dm$$

$$\theta_{k,j,\ell} = \frac{\lambda_{k,j,\ell}(i^*)}{\lambda_I(i^*)}$$
