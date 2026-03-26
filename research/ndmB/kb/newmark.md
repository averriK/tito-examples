## SLOT 1: Problem Introduction

Pseudo-static slope stability analysis is the most widely employed method for evaluating the seismic adequacy of earth structures, embankments, and natural slopes. The method applies a constant horizontal force - expressed as the fraction $k$ of the gravitational acceleration - to the potential sliding mass and evaluates stability through a conventional limit-equilibrium calculation. The central challenge lies in selecting a value of $k$ that reflects both the seismic demand at the site and the displacement performance that constitutes acceptable behavior for the structure under consideration. A performance-based framework addresses this challenge by defining $k_{\max}$ through the statistical distribution of predicted Newmark-type displacements, thereby linking the pseudo-static coefficient to explicit displacement objectives rather than to prescriptive fractions of peak ground acceleration. The performance-based seismic coefficient $k_{\max}$ is defined as the minimum yield acceleration ratio for which the probability that permanent slope displacement exceeds an allowable threshold is controlled at a specified target level; its selection requires calibration against two independent engineering dimensions that together define a design objective consistent with site-specific seismic hazard and facility-specific consequence requirements. [@KBpbkmax][@KBnewmark]

**First Calibration Dimension: Target Seismic Intensity Level**

The first calibration dimension is the target seismic intensity level, linked directly to the consequence class of the structure. The allowable permanent displacement $D_n^{\star}$ is specified as a design criterion, and $k_{\max}$ is established as the minimum yield acceleration required to control the probability of exceeding that threshold at the prescribed hazard level. Facilities whose failure entails severe consequences - such as tailings storage facilities (TSF) and waste rock dumps (WRD) - require evaluation against infrequent ground-motion scenarios with annual exceedance probabilities (AEP) spanning approximately $1/2{,}475$ to $1/10{,}000$. Structures with lower failure consequences may be assessed against less extreme seismic return periods. The consequence class maps onto the hazard return period which, through probabilistic seismic hazard analysis (PSHA), specifies the site-specific intensity measures - including peak ground acceleration ($\mathrm{PGA}$), spectral acceleration $S_a(T)$, Arias intensity ($\mathrm{AI}$), and peak ground velocity ($\mathrm{PGV}$) - against which slope performance is evaluated. Seismic performance is characterized across a suite of service levels spanning AEP $1/100$ to AEP $1/10{,}000$, providing a comprehensive view of the sensitivity of slope behavior to seismic demand intensity. [@KBpbkmax][@KBnewmark][@ANCOLD2019]

Formally, let $D_n$ denote the random variable representing the Newmark-type displacement, incorporating all aleatory and epistemic uncertainties. For a given yield acceleration $k_y$, the exceedance probability is $p(k_y) = \mathbb{P}[D_n(k_y) > D_n^{\star}]$, and $k_{\max}$ is defined by the implicit relationship: [@KBpbkmax]

$$k_{\max}(p \mid D_n^{\star}) = \inf \left\{ k_y : \mathbb{P}[D_n(k_y) > D_n^{\star}] \leq p \right\}$$

This expression links $k_{\max}$ to the site-specific hazard, the displacement-based design objective, and the full statistical characterization of both ground-motion variability and displacement model uncertainty. For any given $p$, $k_{\max}$ represents the lowest value of $k_y$ for which the probability of exceeding the allowable displacement is controlled at the specified level, under the combined statistical effects of hazard, site amplification, and displacement model variability. Displacement values below a numerical floor are treated as negligibly small to maintain well-defined logarithmic operations. [@KBpbkmax]

**Second Calibration Dimension: Physical and Dynamic Characteristics**

The second calibration dimension encompasses the physical and dynamic characteristics of the slope. The yield acceleration $k_y = a_y/g$ - the horizontal acceleration ratio at which the limit-equilibrium factor of safety against sliding on the governing failure surface equals unity - quantifies the resistance of the slope to seismic loading and is determined from geotechnical analysis. It reflects the combined influence of slope geometry, material shear strength, and the kinematic mechanism of the potential failure surface. The fundamental period $T_n$ of the potential sliding mass characterizes the dynamic amplification behavior of the slope: stiff, shallow masses with short $T_n$ respond primarily to the peak ground acceleration, while softer, deeper masses with longer $T_n$ are governed by spectral accelerations at longer periods, subject to site-specific amplification effects. The shear modulus $G$ as a function of confining stress and void ratio controls the stiffness profile of the slope and thereby determines $T_n$ for deformable earth structures. [@KBnewmark][@KBnewmarkmodel][@KBsitemodel]

The predicted displacement distribution $D_n(k_y)$ further depends on whether the sliding mass is modeled as a rigid block responding to base excitation or as a flexible (deformable) system whose internal dynamic response governs displacement. Flexible-block models incorporate $T_n$ and spectral acceleration $S_a$ evaluated at periods proportional to $T_n$, capturing the resonant amplification of compliant slopes. Rigid-block models, by contrast, depend primarily on the ratio $k_y / \mathrm{PGA}$ and on duration-sensitive parameters such as $\mathrm{AI}$ and $\mathrm{PGV}$. The selection among model types - and their relative weighting in the ensemble - reflects an assessment of whether the sliding mass is better approximated as a stiff body responding to base excitation or as a compliant system whose internal dynamic response governs displacement. [@KBnewmark][@KBnewmarkmodel]

**Uncertainty Propagation**

The distribution $D_n(k_y)$ reflects the combined effects of ground-motion variability, model dispersion, and site-specific amplification uncertainty. Ground-motion intensity measures are sampled from their empirical quantile functions derived from PSHA, while each displacement model contributes its own lognormal standard deviation $\sigma_{\ln D}$. Model-to-model epistemic uncertainty is retained through logic-tree weights assigned prior to aggregation over all models in the ensemble. The site-response amplification model introduces an additional layer of uncertainty: the reference-rock hazard output carries the combined epistemic and aleatory uncertainty from the PSHA, and the amplification factor contributes its own dispersion $\sigma_{\ln F}$. Both contributions are propagated jointly by Monte Carlo simulation, ensuring that $k_{\max}$ is calibrated against the full uncertainty budget encompassing source, path, site, and model components. [@KBuncertaintymodel][@KBnewmark][@KBsitemodel]

## SLOT 2: Current State of Practice

The engineering practice of selecting a horizontal seismic coefficient for pseudo-static slope stability evaluation traces its methodological foundation to Newmark's 1965 Rankine Lecture [@Newmark1965]. Newmark conceptualized the sliding mass as a rigid block with a yield acceleration $k_y$; whenever the ground acceleration exceeded $k_y$, the block accumulated incremental downslope displacement, and cumulative permanent displacement served as the performance metric. This displacement-based representation constituted a substantial advance over earlier pseudo-static approaches, which provided information only about the onset of instability and offered no estimate of the magnitude of induced deformations.

**Prescriptive Approaches and Early Rationalization**

Early rationalization of the pseudo-static coefficient drew on parametric Newmark analyses of embankment dams. Hynes-Griffin and Franklin (1984), working under the U.S. Army Corps of Engineers, concluded that a seismic coefficient equal to one-half the peak ground acceleration ($k_h = 0.5\,\mathrm{PGA}/g$) was sufficient to limit deformations to minimal and acceptable levels in compacted embankment dams when the factor of safety in pseudo-static analysis exceeded 1.0 [@HynesGriffinFranklin1984]. This recommendation became a standard reference in dam engineering practice and was subsequently adopted, with minor modifications, by the Federal Highway Administration for the design of reinforced steep slopes. Although practical and conservative for the class of structures studied, the approach did not account for site-specific dynamic characteristics such as the fundamental period of the sliding mass or for project-specific displacement tolerances.

**Current Normative Frameworks**

Contemporary normative guidance reflects the shift from prescriptive to performance-based coefficient selection. Eurocode 8 specifies the horizontal seismic force for pseudo-static slope analysis as

$$F_H = 0.5\,\alpha\,S\,W$$

where $\alpha$ is the ratio of the design ground acceleration to gravitational acceleration, $S$ is a soil-dependent amplification parameter, and $W$ is the weight of the sliding mass [@CEN2004]. Vertical inertia forces are applied conditionally: $F_V = \pm 0.5\,F_H$ when the ratio of vertical to horizontal design acceleration exceeds 0.6, and $F_V = \pm 0.33\,F_H$ otherwise. Pseudo-static methods are permitted where surface topography and soil stratigraphy do not present abrupt irregularities; soils susceptible to elevated pore-water pressures or significant cyclic stiffness degradation require displacement-based or fully dynamic analysis.

**Performance-Based Coefficient Selection**

The transition to fully performance-based coefficient selection was advanced by Bray and Travasarou, who presented a semiempirical procedure deriving the seismic coefficient from site-specific hazard parameters and slope dynamic properties, calibrated against 688 recorded ground motions using a nonlinear fully coupled stick-slip displacement model [@BrayTravasarou2007]. Their central finding - that the coefficient cannot be determined rationally without specifying the allowable displacement and the seismic exposure of the site - became the organizing principle of current practice. In practical application, the engineer specifies a project-specific allowable displacement $D_n^{\star}$ and solves for the yield acceleration $k_y$ that controls the probability of exceeding that threshold, thereby eliminating the subjectivity inherent in prescriptive coefficient selection [@BrayTravasarou2009]. Macedo, Bray, Abrahamson, and Travasarou (2018) subsequently formalized a probabilistic framework integrating the full distribution of intensity measure values at the target hazard level, permitting direct computation of displacement exceedance probabilities without reference to a single representative ground-motion parameter [@MacedoEtAl2018]. Macedo and Candia (2020) extended this line of development through a probabilistic framework grounded in seismically induced displacement hazard curves, yielding pseudo-static coefficient estimates consistent with the allowable displacement level, slope dynamic properties, seismic demand, and hazard design level [@MacedoCandia2020].

**Tectonic-Source-Specific Displacement Models**

The development of tectonic-source-specific displacement models represents a significant methodological advance in the field. Bray, Macedo, and Travasarou (2017) developed a flexible-block displacement model for subduction zone interface earthquakes, calibrated against 810 two-component ground-motion recordings, recognizing that the long-duration, broad-band spectral characteristics of subduction events produce systematically higher displacements than shallow crustal events at equivalent peak acceleration levels [@BrayEtAl2017]. Bray and Macedo (2019) subsequently updated the shallow crustal earthquake model using 6,711 recordings from the NGA-West2 database, introducing peak ground velocity ($\mathrm{PGV}$) as an additional predictor for near-fault, high-amplitude ground motions [@BrayMacedo2019]. The concurrent application of event-specific models within a single probabilistic framework - with logic-tree weights assigned to reflect the relative contribution of each tectonic source to the site hazard - constitutes the appropriate treatment of source-type uncertainty in multi-tectonic settings.

**Synthesis**

In a retrospective review of seismic slope stability methods, Jibson (2011) observed that sliding-block analysis provides the greatest practical utility among available approaches: it is substantially simpler to apply than stress-deformation analysis while yielding significantly more informative results than pseudo-static analysis alone [@Jibson2011]. This assessment reinforces the contemporary practice of calibrating the pseudo-static coefficient against displacement-based performance objectives rather than relying on prescriptive fractions of peak ground acceleration. The convergence of normative guidance, regulatory frameworks, and technical literature toward a performance-based displacement approach reflects broad recognition that the seismic coefficient cannot be specified rationally without reference to three site-specific inputs: (1) the seismic hazard expressed through PSHA-derived intensity measures at the applicable return period, (2) the dynamic properties of the slope, and (3) an explicit allowable displacement threshold appropriate to the facility's consequence class and performance objectives. The methodology adopted in this work operationalizes this three-part calibration through a probabilistic simulation that propagates ground-motion uncertainty, site-amplification uncertainty, and displacement model uncertainty jointly.

## SLOT 3: Newmark Displacement Analysis Methods

The Newmark sliding-block method conceptualizes the seismically loaded slope as either a rigid or a flexible (compliant) block resting on an inclined frictional surface. When the driving acceleration component along the failure plane exceeds the yield acceleration $k_y g$, the block undergoes incremental downslope movement; relative motion ceases when the driving acceleration falls below this threshold. The total permanent displacement $D$ accumulates over all exceedance episodes throughout the duration of shaking.

In probabilistic applications, displacement is characterized using empirical regression relationships expressed in lognormal space. All models in the ensemble follow the general form:

$$\ln D = \mu_{\ln D}(\mathrm{IM},\,k_y,\,T_n,\,M_w) + \epsilon\,\sigma_{\ln D}$$

In this expression, $\mathrm{IM}$ denotes the set of ground-motion intensity measures specific to each model (e.g., $\mathrm{PGA}$, spectral acceleration $S_a$ at a reference period, Arias intensity $\mathrm{AI}$, or peak ground velocity $\mathrm{PGV}$); $T_n$ is the fundamental period of the sliding mass; $M_w$ is the earthquake moment magnitude where included as a model predictor; $\mu_{\ln D}$ is the model-predicted mean displacement in natural-log space; $\sigma_{\ln D}$ is the associated standard deviation in natural-log space; and $\epsilon \sim \mathcal{N}(0,1)$ is a standard-normal variate capturing record-to-record variability not explained by the regression. Where hazard is derived from a ground-motion model or site response analysis, spectral accelerations are evaluated at the periods required by each model, typically $S_a(\alpha T_n)$ with $\alpha$ in the range 1.3 to 1.5.

### Rigid-Block Models

The rigid-block idealization treats the sliding mass as an undistorted body that moves as a whole relative to the underlying ground. Dynamic amplification within the mass is negligible, and the response is governed entirely by the base excitation. This idealization is appropriate for shallow translational failure surfaces in relatively stiff materials whose fundamental period is short relative to the dominant periods of the input motion. The governing intensity measures are $\mathrm{PGA}$, supplemented in multi-parameter models by $\mathrm{AI}$ or $\mathrm{PGV}$ to capture duration and velocity effects. Four rigid-block models are retained in the ensemble:

- **Ambraseys and Menu (1988)** [@AmbraseysMenu1988]: expresses displacement as a function of the acceleration ratio $r = k_y / \mathrm{PGA}$, reflecting the foundational Newmark assumption that slide strength relative to peak ground acceleration is the primary controlling variable.
- **Yegian et al. (1991)** [@Yegian1991]: similarly employs $r = k_y / \mathrm{PGA}$ as the primary predictor.
- **Jibson (2007)** [@Jibson2007]: uses Arias intensity $\mathrm{AI}$ and the ratio $k_y / \mathrm{PGA}$ as predictors, capturing duration effects through the cumulative energy content of the ground motion; calibrated against 2,270 strong-motion records from 30 worldwide earthquakes.
- **Saygili and Rathje (2008)** [@SaygiliRathje2008]: a multi-parameter formulation incorporating both $\mathrm{PGA}$ and $\mathrm{AI}$ simultaneously, calibrated against a database exceeding 2,000 acceleration time-histories; the model standard deviation is displacement-dependent, increasing as $r$ decreases to reflect greater prediction uncertainty for weaker slopes.

### Flexible-Block Models

The flexible-block (compliant) idealization accounts for the dynamic response of the sliding mass as a deformable body by incorporating the fundamental period $T_n$ and spectral acceleration $S_a$ evaluated at a period proportional to $T_n$. This treatment captures the amplification or de-amplification of motion within the earth structure and introduces $T_n$ and $M_w$ as explicit predictors. Flexible-block models are appropriate for deeper-seated failure surfaces in earth dams, natural slopes, compacted fills, and waste embankments where the sliding mass has significant deformability. All three flexible-block models include an explicit dependence on $M_w$ to account for the influence of earthquake duration on accumulated displacement. Three flexible-block models are employed:

- **Bray and Travasarou (2007)** [@BrayTravasarou2007]: evaluates $S_a$ at $1.5\,T_n$; incorporates $k_y$, $T_n$, and $M_w$ as predictors; calibrated against 688 ground-motion recordings spanning diverse tectonic environments.
- **Bray, Macedo, and Travasarou (2017)** [@BrayEtAl2017]: evaluates $S_a$ at $1.5\,T_n$ with piecewise coefficients distinguishing short-period ($T_n < 0.1$ s) from longer-period sliding masses; calibrated specifically for subduction-zone interface earthquakes using 810 two-component recordings, with $M_w$ included to account for the long duration of subduction events.
- **Bray and Macedo (2019)** [@BrayMacedo2019]: evaluates $S_a$ at $1.3\,T_n$; calibrated for shallow crustal earthquakes using 6,711 recordings from the NGA-West2 database; incorporates an additional correction for high peak ground velocities ($\mathrm{PGV} > 115$ cm s$^{-1}$).

## SLOT 4: Appendix - Newmark Displacement Equations

The following presents the complete predictive equations for each Newmark displacement model included in the ensemble. The notation applies throughout [@KBnewmarkmodel]: $D$ denotes permanent displacement in centimeters; $k_y = a_y/g$ is the dimensionless yield-acceleration ratio; $\mathrm{PGA}$ is peak ground acceleration in units of $g$; $\mathrm{PGV}$ is peak ground velocity in cm s$^{-1}$; $\mathrm{AI}$ is Arias intensity in m s$^{-1}$; $T_n$ is the fundamental period of the sliding mass in seconds; $S_a$ is spectral acceleration in $g$ evaluated at a model-specific period; $M_w$ is moment magnitude; and $r = k_y/\mathrm{PGA}$ is the critical acceleration ratio. All dispersions $\sigma$ are one-standard-deviation values in natural-log space unless otherwise noted.

### A.1 Bray, Macedo, and Travasarou (2017) - Flexible-Block, Subduction Zone Earthquakes

The Bray, Macedo, and Travasarou (2017) model [@BrayEtAl2017] is a flexible-block formulation calibrated for subduction zone interface and intraslab earthquakes against 810 two-component ground-motion recordings. The model is applicable to earth dams, natural slopes, and engineered embankments with both planar and non-planar failure surfaces. Spectral acceleration is evaluated at the undegraded fundamental period $T_n$ of the sliding mass. The mean log-displacement and coefficient definitions are:

$$\begin{aligned}
\mu_{\ln D} &= a_0 + a_1\ln S_a + a_2(\ln S_a)^2 \\[6pt]
a_0 &= \begin{cases}
-5.864 + 0.550\,M_w - 9.421\,T_n - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n < 0.1 \\
-6.896 + 0.550\,M_w + 3.081\,T_n - 0.803\,T_n^2 - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n \geq 0.1
\end{cases} \\[6pt]
a_1 &= 3.060 + 0.538\ln k_y, \qquad a_2 = -0.225
\end{aligned}$$

The residual standard deviation is $\sigma_{\ln D} = 0.73$.

### A.2 Bray and Macedo (2019) - Flexible-Block, Shallow Crustal Earthquakes

The Bray and Macedo (2019) model [@BrayMacedo2019] employs the same functional structure as the 2017 formulation but with coefficients recalibrated for shallow crustal earthquakes using 6,711 two-component recordings from the NGA-West2 database. The model is applicable to flexible slope systems with both planar and non-planar failure surfaces. Spectral acceleration is evaluated at $1.3\,T_n$, and an additional correction applies for near-fault, high-amplitude motions when $\mathrm{PGV} > 115$ cm s$^{-1}$. The complete predictive equations are:

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

The residual standard deviation is $\sigma_{\ln D} = 0.74$. When $\mathrm{PGV}$ is not independently available, it may be estimated from $\mathrm{PGA}$.

### A.3 Bray and Travasarou (2007) - Flexible-Block

The Bray and Travasarou (2007) model [@BrayTravasarou2007] is a flexible-block formulation calibrated against 688 recorded ground motions spanning a range of tectonic environments using coupled stick-slip analyses of flexible sliding masses. The model is applicable to earth dams, natural slopes, compacted earth fills, and municipal solid-waste landfills subject to deviatoric shear-type deformations, covering both deep-seated and shallow failure surfaces in compliant slopes. Spectral acceleration is evaluated at $1.5\,T_n$. The mean log-displacement is:

$$\mu_{\ln D} = -1.10 - 2.83\ln k_y - 0.333(\ln k_y)^2 + 0.566\ln k_y\ln S_a + 3.04\ln S_a - 0.244(\ln S_a)^2 + 0.278(M_w - 7)$$

The residual standard deviation is $\sigma_{\ln D} = 0.66$.

### A.4 Jibson (2007) - Rigid-Block

The Jibson (2007) model [@Jibson2007] is a rigid-block formulation calibrated against 2,270 strong-motion records from 30 worldwide earthquakes, incorporating Arias intensity as a duration-sensitive predictor. The model is applicable to shallow, translational failure surfaces where the sliding mass may be approximated as infinitely stiff, and is widely employed in preliminary design evaluation and regional seismic landslide hazard assessment. Arias intensity is expressed in m s$^{-1}$ and may be estimated from $\mathrm{PGA}$ when direct measurements are unavailable. The predictive equation is:

$$\mu_{\ln D} = \left[0.561\log_{10}\mathrm{AI} - 3.833\log_{10}(k_y/\mathrm{PGA}) - 1.474\right]\ln 10$$

The regression residual in $\log_{10}$ space is $\sigma_{\log_{10}D} = 0.616$, equivalent to $\sigma_{\ln D} = 0.616\ln 10 \approx 1.419$.

### A.5 Saygili and Rathje (2008) - Rigid-Block, Multi-Parameter

The Saygili and Rathje (2008) model [@SaygiliRathje2008] is a multi-parameter rigid-block formulation developed from a database exceeding 2,000 acceleration time-histories, employing both Arias intensity and peak ground acceleration as simultaneous predictors. The model is applicable to stiff, shallow, translational failure surfaces. The dispersion is amplitude-dependent: the standard deviation increases as $r$ decreases, reflecting greater prediction uncertainty for slopes operating close to their yield threshold. The mean log-displacement and associated dispersion are:

$$\begin{aligned}
\mu_{\ln D} &= 2.39 - 5.24r - 18.78r^2 + 42.01r^3 - 29.15r^4 - 1.56\ln\mathrm{PGA} + 1.38\ln\mathrm{AI}, \qquad r = k_y/\mathrm{PGA} \\[6pt]
\sigma_{\ln D} &= 0.46 + 0.56\,r
\end{aligned}$$

### A.6 Ambraseys and Menu (1988) - Rigid-Block

The Ambraseys and Menu (1988) model [@AmbraseysMenu1988] is one of the earliest published Newmark-type regression relationships, calibrated against 50 strong-motion records from 11 earthquakes. The model uses the critical acceleration ratio $r = k_y/\mathrm{PGA}$ as the sole predictor and is applicable to rigid translational slides. The regression is expressed in $\log_{10}$ space:

$$\mu_{\log_{10}D} = 0.90 + \log_{10}\!\left[(1-r)^{2.53}\,r^{-1.09}\right]$$

The residual standard deviation is $\sigma_{\log_{10}D} = 0.30$, equivalent to $\sigma_{\ln D} = 0.30\ln 10 \approx 0.691$.

### A.7 Yegian, Marciano, and Varzaghian (1991) - Rigid-Block

The Yegian et al. (1991) model [@Yegian1991] is a rigid-block formulation expressed as a cubic polynomial in the critical acceleration ratio, calibrated from parametric sliding-block analyses. The model is applicable to rigid translational failure surfaces. The predictive equation is:

$$\mu_{\log_{10}D} = 0.22 - 10.12\,r + 16.38\,r^2 - 11.48\,r^3, \qquad r = k_y/\mathrm{PGA}$$

The residual standard deviation is $\sigma_{\log_{10}D} = 0.45$, equivalent to $\sigma_{\ln D} = 0.45\ln 10 \approx 1.036$.

