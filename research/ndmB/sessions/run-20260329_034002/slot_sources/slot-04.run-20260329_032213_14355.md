## SLOT 4: Detailed Newmark Displacement Estimation Methods

The following section presents the complete predictive equations for each Newmark displacement model retained in the ensemble. Throughout, $D$ denotes permanent displacement in centimeters; $k_y = a_y/g$ is the dimensionless yield-acceleration ratio; $\mathrm{PGA}$ is peak ground acceleration in units of $g$; $\mathrm{PGV}$ is peak ground velocity in cm s$^{-1}$; $\mathrm{AI}$ is Arias intensity in m s$^{-1}$; $T_n$ is the fundamental period of the sliding mass in seconds; $S_a$ is spectral acceleration in $g$ evaluated at a model-specific period; $M_w$ is moment magnitude; and $r = k_y/\mathrm{PGA}$ is the critical acceleration ratio. All dispersions $\sigma$ are one-standard-deviation values in natural-log space unless otherwise noted. [@KBnewmarkmodel][KB:newmark.md]^[Confidence: HIGH, Rationale: The notation conventions are directly stated in the KB (newmark.md, Appendix section). The parameter definitions are internally consistent with standard notation in the Newmark displacement literature and all symbols are unambiguously defined in the source.]

### Rigid-Block Models

The rigid-block idealization treats the sliding mass as an undistorted body that moves as a whole relative to the underlying ground. Dynamic amplification within the mass is negligible, and the response is governed entirely by the base excitation. This idealization is appropriate for shallow translational failure surfaces in relatively stiff materials whose fundamental period is short relative to the dominant periods of the input motion. Four rigid-block models are retained in the ensemble: Ambraseys and Menu (1988), Yegian et al. (1991), Jibson (2007), and Saygili and Rathje (2008). [KB:newmark.md]^[Confidence: HIGH, Rationale: The characterization of rigid-block models and their applicability to shallow, stiff slopes is directly stated in the KB (newmark.md). The four retained models are explicitly identified in the source.]

**Ambraseys and Menu (1988)**: The Ambraseys and Menu (1988) model [@AmbraseysMenu1988] is among the earliest published Newmark-type regression relationships, calibrated against 50 strong-motion records from 11 earthquakes. The model employs the critical acceleration ratio $r = k_y/\mathrm{PGA}$ as the sole predictor and is applicable to rigid translational slides. The regression is expressed in $\log_{10}$ space, with the residual standard deviation $\sigma_{\log_{10}D} = 0.30$, equivalent to $\sigma_{\ln D} = 0.30\ln 10 \approx 0.691$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The Ambraseys and Menu (1988) model description, calibration dataset size, sole-predictor structure, and dispersion value are directly stated in the KB (newmark.md).]

$$\mu_{\log_{10}D} = 0.90 + \log_{10}\!\left[(1-r)^{2.53}\,r^{-1.09}\right]$$

**Yegian, Marciano, and Varzaghian (1991)**: The Yegian et al. (1991) model [@Yegian1991] is a rigid-block formulation expressed as a cubic polynomial in the critical acceleration ratio, calibrated from parametric sliding-block analyses. The model is applicable to rigid translational failure surfaces. The residual standard deviation is $\sigma_{\log_{10}D} = 0.45$, equivalent to $\sigma_{\ln D} = 0.45\ln 10 \approx 1.036$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The Yegian et al. (1991) model description and dispersion are directly stated in the KB (newmark.md). The cubic polynomial structure is confirmed by the equation.]

$$\mu_{\log_{10}D} = 0.22 - 10.12\,r + 16.38\,r^2 - 11.48\,r^3, \qquad r = k_y/\mathrm{PGA}$$

**Jibson (2007)**: The Jibson (2007) model [@Jibson2007] is a rigid-block formulation calibrated against 2,270 strong-motion records from 30 worldwide earthquakes, incorporating Arias intensity as a duration-sensitive predictor. The model is applicable to shallow, translational failure surfaces where the sliding mass may be approximated as infinitely stiff, and is widely employed in preliminary design evaluation and regional seismic landslide hazard assessment. Arias intensity is expressed in m s$^{-1}$ and may be estimated from $\mathrm{PGA}$ when direct measurements are unavailable. The regression residual in $\log_{10}$ space is $\sigma_{\log_{10}D} = 0.616$, equivalent to $\sigma_{\ln D} = 0.616\ln 10 \approx 1.419$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The calibration database size (2,270 records from 30 earthquakes) and applicability description for the Jibson (2007) model are directly stated in the KB (newmark.md). The dispersion conversion is mathematically exact.]

$$\mu_{\ln D} = \left[0.561\log_{10}\mathrm{AI} - 3.833\log_{10}(k_y/\mathrm{PGA}) - 1.474\right]\ln 10$$

**Saygili and Rathje (2008)**: The Saygili and Rathje (2008) model [@SaygiliRathje2008] is a multi-parameter rigid-block formulation developed from a database exceeding 2,000 acceleration time-histories, employing both Arias intensity and peak ground acceleration as simultaneous predictors. The model is applicable to stiff, shallow, translational failure surfaces. The dispersion is amplitude-dependent: the standard deviation increases as $r$ decreases, reflecting greater prediction uncertainty for slopes operating close to their yield threshold. [KB:newmark.md]^[Confidence: HIGH, Rationale: The multi-parameter formulation, the database size, and the amplitude-dependent dispersion of the Saygili and Rathje (2008) model are directly stated in the KB (newmark.md). The interpretation of increasing uncertainty at low $r$ values is consistent with the model structure.]

$$\begin{aligned}
\mu_{\ln D} &= 2.39 - 5.24r - 18.78r^2 + 42.01r^3 - 29.15r^4 - 1.56\ln\mathrm{PGA} + 1.38\ln\mathrm{AI}, \qquad r = k_y/\mathrm{PGA} \\[6pt]
\sigma_{\ln D} &= 0.46 + 0.56\,r
\end{aligned}$$

### Flexible-Block Models

Flexible-block models account for the dynamic response of the sliding mass as a deformable body by incorporating the fundamental period $T_n$ and spectral acceleration $S_a$ evaluated at a period proportional to $T_n$. All three flexible-block models include an explicit dependence on $M_w$ to account for the influence of earthquake duration on accumulated displacement. These models are appropriate for deeper-seated failure surfaces in earth dams, natural slopes, compacted fills, and waste embankments where the sliding mass has significant deformability. [KB:newmark.md]^[Confidence: HIGH, Rationale: The characterization of flexible-block models, their use of $T_n$ and $S_a$, their $M_w$ dependence, and their applicability to deeper-seated failures in deformable earth structures are directly stated in the KB (newmark.md).]

**Bray, Macedo, and Travasarou (2017)**: The Bray, Macedo, and Travasarou (2017) model [@BrayEtAl2017] is a flexible-block formulation calibrated for subduction zone interface and intraslab earthquakes against 810 two-component ground-motion recordings. Spectral acceleration is evaluated at the undegraded fundamental period $T_n$ of the sliding mass, and the coefficient $a_0$ takes a piecewise form distinguishing short-period ($T_n < 0.1$ s) from longer-period sliding masses. The residual standard deviation is $\sigma_{\ln D} = 0.73$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The BET (2017) model applicability (subduction zone, 810 recordings), the spectral acceleration evaluation at $T_n$, the piecewise structure of $a_0$, and the dispersion are directly stated in the KB (newmark.md).]

$$\begin{aligned}
\mu_{\ln D} &= a_0 + a_1\ln S_a + a_2(\ln S_a)^2 \\[6pt]
a_0 &= \begin{cases}
-5.864 + 0.550\,M_w - 9.421\,T_n - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n < 0.1 \\
-6.896 + 0.550\,M_w + 3.081\,T_n - 0.803\,T_n^2 - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n \geq 0.1
\end{cases} \\[6pt]
a_1 &= 3.060 + 0.538\ln k_y, \qquad a_2 = -0.225
\end{aligned}$$

**Bray and Macedo (2019)**: The Bray and Macedo (2019) model [@BrayMacedo2019] employs the same functional structure as the 2017 formulation but with coefficients recalibrated for shallow crustal earthquakes using 6,711 two-component recordings from the NGA-West2 database. Spectral acceleration is evaluated at $1.3\,T_n$, and an additional correction applies for near-fault, high-amplitude motions when $\mathrm{PGV} > 115$ cm s$^{-1}$. The residual standard deviation is $\sigma_{\ln D} = 0.74$. When $\mathrm{PGV}$ is not independently available, it may be estimated from $\mathrm{PGA}$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The BM (2019) model description, calibration database size, spectral period factor of $1.3\,T_n$, PGV correction threshold, and dispersion are directly stated in the KB (newmark.md).]

$$\begin{aligned}
\mu_{\ln D} &= a_0 + a_1\ln S_a + a_2(\ln S_a)^2 \\[6pt]
a_0 &= \begin{cases}
-4.551 + 0.607\,M_w - 9.690\,T_n - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n < 0.1 \\
-5.894 + 0.607\,M_w + 3.152\,T_n - 0.910\,T_n^2 - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n \geq 0.1
\end{cases} \\[6pt]
&\quad + \begin{cases}
0, & \mathrm{PGV} \leq 115\;\text{cm s}^{-1} \\
\ln\mathrm{PGV} - 4.75, & \mathrm{PGV} > 115\;\text{cm s}^{-1}
\end{cases} \\[6pt]
a_1 &= 2.703 + 0.344\ln k_y, \qquad a_2 = -0.089
\end{aligned}$$

**Bray and Travasarou (2007)**: The Bray and Travasarou (2007) model [@BrayTravasarou2007] is a flexible-block formulation calibrated against 688 recorded ground motions spanning a range of tectonic environments using coupled stick-slip analyses. The model is applicable to earth dams, natural slopes, compacted earth fills, and municipal solid-waste landfills subject to deviatoric shear-type deformations, covering both deep-seated and shallow failure surfaces in compliant slopes. Spectral acceleration is evaluated at $1.5\,T_n$. The residual standard deviation is $\sigma_{\ln D} = 0.66$. [KB:newmark.md]^[Confidence: HIGH, Rationale: The BT (2007) model applicability, calibration dataset size, spectral period factor of $1.5\,T_n$, and dispersion are directly stated in the KB (newmark.md). The model remains the most generally applicable flexible-block formulation given its broad tectonic calibration base.]

$$\mu_{\ln D} = -1.10 - 2.83\ln k_y - 0.333(\ln k_y)^2 + 0.566\ln k_y\ln S_a + 3.04\ln S_a - 0.244(\ln S_a)^2 + 0.278(M_w - 7)$$


