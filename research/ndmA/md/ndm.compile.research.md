## SLOT 1: Problem Introduction - Performance-Based Seismic Coefficient Selection

Pseudo-static slope stability analysis represents the standard method in geotechnical engineering
practice for evaluating the seismic performance of earth structures, including natural slopes,
embankments, tailings storage facilities (TSFs), and waste rock dumps (WRDs). In this method, the
dynamic effect of earthquake loading is represented as an equivalent static horizontal force equal
to the product of a dimensionless seismic coefficient $k_h$ and the weight $W$ of the potentially
sliding mass; a limit-equilibrium analysis is then conducted to compute the factor of safety under
the combined action of gravity and the imposed inertial force. The validity of this approach
depends critically on the selection of an appropriate $k_h$ value, which must represent seismic
demand consistent with the structure's performance objective rather than being assigned by
precedent or convention [@KBnewmark].

The performance-based framework reconceptualizes $k_h$ selection as an inverse problem defined by
an explicit displacement performance objective. The design coefficient $k_{\max}$ is the minimum
yield acceleration ratio $k_y = a_y/g$ for which the probability of the ensemble-predicted
permanent co-seismic displacement exceeding an allowable threshold $D_n^{\star}$ is controlled at
a specified target exceedance probability $p$:

$$k_{\max}(p \mid D_n^{\star}) = \inf\{k_y : P[D_n(k_y) > D_n^{\star}] \leq p\}$$

where $a_y$ is the critical (yield) acceleration, $g$ is gravitational acceleration, $D_n$ is the
ensemble-predicted Newmark displacement, and $p$ is the target exceedance probability [@KBpbkmax].

The coefficient is calibrated to two interrelated groups of parameters. The first group defines the
target ground-motion intensity level, expressed as an annual exceedance probability (AEP) linked to
the consequence class of the structure. Facilities for which failure produces severe or irreversible
consequences are assigned more stringent hazard levels corresponding to lower AEPs. The framework
accommodates service levels spanning AEPs from $1/100$ per annum for routine operational loading to
$1/10{,}000$ per annum for extreme design scenarios applicable to high-consequence TSF and WRD
facilities [@KBpbkmax].

The second group characterizes the physical and dynamic properties of the slope. The yield
acceleration ratio $k_y = a_y/g$ - the minimum normalized horizontal acceleration required to
initiate permanent sliding along the critical failure surface - is established from geotechnical
analysis of the failure mechanism and material shear strength. The fundamental period of vibration
$T_n$ of the potentially sliding mass governs the portion of spectral demand that drives
displacement accumulation; its value depends on the shear stiffness and geometric extent of the
sliding body. Together, $k_y$ and $T_n$ define the mechanical response of the slope to a given
seismic excitation [@KBnewmark][@KBnewmarkmodel].

The methodology connects these two parameter groups through Newmark sliding-block displacement
regression models, which translate ground-motion intensity measures - including peak ground
acceleration (PGA), spectral acceleration $S_a(T)$, peak ground velocity (PGV), and Arias
intensity (AI) - into probability distributions of permanent residual displacement. Results are
aggregated across an ensemble of predictive models using logic-tree weighting, producing
displacement distributions that reflect the full range of model and parameter uncertainty. The
performance-based coefficient $k_{\max}$ is then identified by inverting this displacement
framework: for a given target AEP and allowable displacement threshold $D_n^{\star}$, the minimum
$k_y$ satisfying the prescribed performance criterion constitutes the design seismic coefficient
[@KBpbkmax][@KBnewmark].

## SLOT 2: Current State of Practice -- Standards, Guidelines, and Recommendations

> Confidence: MIXED -- This SLOT includes HIGH-confidence content plus selected MEDIUM-confidence structured details preserved to avoid dropping essential structure during compilation.

The seismic design of slopes, embankments, and earth dams has historically relied on the pseudo-static limit-equilibrium method, with the horizontal seismic coefficient $k_h$ assigned as a fixed fraction of the regional design peak ground acceleration -- commonly 0.10g to 0.15g -- or determined by engineering judgment. Over the past three decades, the profession has progressively transitioned toward performance-based procedures in which $k_h$ is linked to an explicit, project-specific displacement tolerance and a probabilistic hazard level reflecting the consequence class of the structure. This transition has been driven by advances in ground-motion databases, empirical displacement prediction models, and probabilistic seismic hazard analysis, which together make it feasible to define seismic design criteria in terms of quantified performance outcomes rather than nominal force levels [@USACE2003][@AndersonEtAl2008].

The limit-equilibrium method remains the predominant analytical framework for slope stability assessment in both static and seismic conditions. In seismic applications, pseudo-static analysis augments this framework by introducing horizontal inertia forces proportional to $k_h$ and the weight of the sliding mass, with the factor of safety defined as the ratio of available shear resistance to seismic shear demand along a potential failure surface [@UpCodes2025a][@UpCodes2025b]. The Newmark sliding-block method has become the cornerstone of displacement-based seismic slope design; advances over the past two decades have introduced flexible-block formulations that capture dynamic compliance of the sliding mass, duration-sensitive models incorporating peak ground velocity and Arias intensity, and reliability-based allowable-displacement procedures that are more robust than traditional pseudo-static factor-of-safety approaches [@KBnewmarkmodel][@UBCThesis].

### Regulatory and Code-Based Frameworks

The U.S. Army Corps of Engineers Engineer Manual EM 1110-2-1902 endorses pseudo-static limit-equilibrium analysis as one of several acceptable methods and addresses the Newmark sliding-block approach for estimating permanent seismic deformation. Neither EM 1110-2-1902 nor the companion manual EM 1110-2-2100 prescribes a universal coefficient value; both direct the engineer to consider site-specific seismic hazard and acceptable performance criteria when selecting $k_h$, establishing the principle that coefficient selection must reflect project-specific conditions [@USACE2003][@USACE2005]. The companion Engineer Regulation ER 1110-2-1806 defines earthquake levels in terms of the Operating Basis Earthquake (OBE), characterized by a 50% probability of exceedance in 100 years, and the Maximum Design Earthquake (MDE), with minimum factors of safety of 1.1 to 1.5 depending on the applicable load condition [@USACE1995].

NCHRP Report 611 constitutes a significant codification of displacement-based seismic design for transportation infrastructure [@AndersonEtAl2008]. The report recommends simplified Newmark displacement correlations for slope performance assessment and advocates a horizontal pseudo-static coefficient of approximately 0.5 times the site-adjusted PGA for limit-equilibrium analyses targeting a minimum factor of safety of 1.1. Indicative performance thresholds are provided: permanent displacements below approximately 100 mm correspond to stable serviceability conditions, while displacements exceeding approximately 300 mm are identified as potentially unacceptable, with acknowledgment that project-specific limits may differ.

Eurocode 8 (EN 1998-5) prescribes a pseudo-static horizontal coefficient tied to the design peak ground acceleration and the slope consequence class. Where the critical acceleration substantially exceeds the design PGA, the code permits Newmark displacement calculations as an alternative to pseudo-static analysis, recognizing that deformation-based performance verification is more rational for ductile earth structures [@CEN2004]. Most code-based recommendations restrict the pseudo-static method to conditions where the coefficient does not exceed approximately 0.3, above which dynamic amplification effects become non-negligible.

The International Commission on Large Dams classifies seismic stability assessment methods into three tiers: simplified pseudo-static methods, simplified dynamic methods (Newmark sliding-block), and full dynamic analysis using time-domain numerical formulations. For structures of moderate-to-high consequence, ICOLD Bulletin 148 endorses the Newmark displacement approach as the preferred simplified dynamic method and establishes a two-level design earthquake framework comprising an Operating Basis Earthquake and a Safety Evaluation Earthquake (SEE) [@ICOLD2016][@ANCOLD2012]. Return periods of 3,000 years and 1,000 years are specified for high-consequence and moderate-consequence structures, respectively.

### Performance-Based Professional Guidance

The foundational performance-based framework for pseudo-static seismic coefficient selection was established by Bray and Travasarou (2009), who demonstrated that $k_h$ should be derived by inverting the displacement-based design criterion rather than applying an arbitrary fraction of the free-field PGA [@BrayTravasarou2009]. By inverting the probabilistic displacement model of Bray and Travasarou (2007) [@BrayTravasarou2007], the procedure allows the design seismic coefficient required to limit the probability of exceeding a specified displacement threshold to be determined directly, given the site ground-motion demand, the fundamental period $T_n$ of the sliding mass, and the yield acceleration. This approach formally accounts for the dynamic response of the sliding mass and yields project-specific rather than code-uniform design values; in many practical cases the resulting coefficient amounts to 25% to 50% of the free-field PGA for slopes that can accommodate 25 to 50 mm of permanent seismic displacement [@BrayTravasarou2009]. The framework was subsequently extended to cover shallow-crustal and subduction-zone tectonic environments separately [@BrayMacedo2017][@BrayMacedo2019].

Macedo et al. (2018) extended this framework into a fully probabilistic performance-based earthquake engineering (PBEE) procedure, integrating PSHA-derived seismic hazard with Newmark displacement models to produce hazard-consistent estimates of seismic slope performance across a range of return periods [@MacedoEtAl2018]. A subsequent study confirmed that the performance-based approach yields pseudo-static coefficients systematically lower than those from prescriptive 50%-PGA rules for ductile slopes, with quantified sensitivity to hazard level, slope period, and allowable displacement threshold [@MacedoEtAl2020].

### Dam Safety and Mining Sector Practice

The Canadian Dam Association Technical Bulletins prescribe a performance-based approach in which earthquake return periods and acceptable damage states are linked to the consequence classification of the dam, applicable to all dam types including mine tailings impoundments [@CDA2019]. FEMA Guideline P-65 provides complementary guidance on site-specific hazard studies, ground-motion selection, and deformation-based performance evaluation in the context of dam safety [@FEMA2005]. ICOLD Bulletin 148 recommends Newmark-type deformation analyses for detailed performance evaluation at the SEE level for embankment-type structures [@ICOLD2016].

For tailings storage facilities and waste rock dumps, regulatory guidance in Canada -- including Canadian Dam Safety Association guidelines and Mining Association of Canada guidelines for tailings facilities management -- requires seismic stability assessment under consequence-category-specific design earthquake levels. Extreme-consequence structures are assigned design return periods of 10,000 years or longer; pseudo-static analysis serves as a screening-level tool only, with deformation-based methods required for final design verification in moderate-to-high seismicity regions [@UBCThesis].

### Convergence of Current Practice

Across the frameworks surveyed, current practice converges on the principle that $k_h$ should be determined through a performance-based analysis in which an allowable permanent displacement is specified and the seismic coefficient is back-calculated to satisfy that limit at the appropriate hazard level. Residual displacement thresholds are typically in the range of 100 mm to 300 mm for operational performance objectives and may be substantially lower for critical or consequence-category facilities. The methodology described in this memorandum is fully consistent with this state of practice, extending it through a multi-model ensemble displacement prediction framework that formally propagates epistemic uncertainty across a suite of calibrated predictive models [@KBnewmark][@KBpbkmax].

## SLOT 3: Newmark Displacement Analysis Methodologies - Rigid and Flexible Block Models

The Newmark (1965) sliding-block method provides the analytical foundation for all displacement
prediction models employed in the present framework. A potentially unstable slope is conceptualized
as a discrete mass resting on a frictional inclined surface. When earthquake-induced ground
acceleration exceeds the critical yield acceleration $k_y g$ - the minimum horizontal acceleration
at which driving forces along the failure surface equal the resisting forces - the block begins to
slide downslope. Permanent displacement $D$ accumulates as the double integral of the excess
acceleration over each interval during which the ground acceleration exceeds $k_y g$, with the
total displacement representing the cumulative downslope movement over the full earthquake record.
Two distinct physical idealizations of the sliding mass govern the selection of applicable
displacement prediction models: the rigid-block model and the flexible-block model. [@KBnewmark]

**Rigid-Block Idealization.** The rigid-block formulation treats the sliding mass as internally
rigid: all points within the mass accelerate coherently with the base until the yield threshold is
exceeded, whereupon the mass displaces as a unit. This idealization is physically appropriate when
the sliding mass is stiff relative to the frequency content of the ground motion - specifically when
the fundamental period $T_n$ is substantially shorter than the dominant period of the input motion,
generally $T_n < 0.1$ s - or when the failure surface is shallow and translational in character.
The model requires only the yield acceleration $k_y$ and one or more scalar ground-motion intensity
measures, typically the peak ground acceleration ($\mathrm{PGA}$), the Arias intensity
($\mathrm{AI}$), the peak ground velocity ($\mathrm{PGV}$), or the dimensionless critical
acceleration ratio $r = k_y / \mathrm{PGA}$, making it computationally efficient and well suited
to preliminary screening. The rigid-block models employed in the present ensemble are those of
Ambraseys and Menu [@AmbraseysMenu1988], Yegian, Marciano, and Ghahraman [@Yegian1991], Jibson
[@Jibson2007], and Saygili and Rathje [@SaygiliRathje2008]. The Jibson (2007) model was calibrated
on 2270 strong-motion records from 30 worldwide earthquakes and incorporates Arias intensity as the
primary predictor alongside the critical acceleration ratio $r$, improving the capture of duration
and energy-content effects not fully represented by $\mathrm{PGA}$ alone [@Jibson2007]. The Saygili
and Rathje (2008) formulation combines $\mathrm{AI}$ and $\mathrm{PGA}$ within a heteroscedastic
dispersion structure that accounts for increasing prediction uncertainty as the slope approaches its
critical condition. [@KBnewmarkmodel]

**Flexible-Block Idealization.** The flexible-block formulation extends the Newmark framework to
account for the dynamic response of a deformable sliding mass. In this idealization, the mass
possesses finite stiffness characterized by its fundamental period $T_n$, and the seismic demand
experienced at the failure surface reflects both the input ground motion and the dynamic
amplification or de-amplification within the mass. Spectral acceleration evaluated at a constant
multiple of $T_n$ - typically $1.3\,T_n$ to $1.5\,T_n$, reflecting the period elongation
associated with inelastic yielding and shear strain softening under design-level shaking - serves
as the primary ground-motion intensity measure. Moment magnitude $M_w$ is also included as a
predictor in flexible-block formulations because it governs the duration of strong shaking, which
exerts a controlling influence on cumulative displacement for masses with non-negligible fundamental
periods. The flexible-block idealization is physically appropriate for deep-seated rotational
slides, engineered embankments, and thick earth fills where the mass exhibits measurable dynamic
response. The fundamental period $T_n$ is estimated from the geometry and shear stiffness of the
embankment or fill using the empirical Ishihara (1997) shear modulus formulation as a function of
void ratio and confining stress; $T_n$ is subsequently updated to account for shear strain softening
under the design seismic demand. The flexible-block models employed in the ensemble are Bray and
Travasarou [@BrayTravasarou2007], applicable to general tectonic settings, and the
tectonic-regime-specific formulations of Bray and Macedo for subduction-zone earthquakes
[@BrayMacedo2017] and shallow-crustal earthquakes [@BrayMacedo2019]. The Bray and Macedo (2019)
model incorporates a $\mathrm{PGV}$ correction term applicable when $\mathrm{PGV} > 115$ cm/s to
address near-fault velocity pulse conditions. The threshold $T_n = 0.1$ s formally demarcates the
rigid-block and flexible-block regimes; both Bray and Macedo (2017) and Bray and Macedo (2019)
employ piecewise coefficient definitions at this threshold. [@KBnewmarkmodel]

**General Probabilistic Structure.** All displacement prediction models within the framework,
regardless of block idealization, are cast in the following lognormal regression form
[@KBnewmark]:

$$
\ln D = \mu_{\ln D}(\mathrm{IM},\, k_y,\, T_n,\, M_w) + \epsilon\,\sigma_{\ln D}
$$

where $D$ is the predicted permanent displacement in centimeters, $\mathrm{IM}$ denotes the set of
ground-motion intensity measures specific to each model (e.g., $\mathrm{PGA}$, spectral
acceleration $S_a$ at a model-specific period, Arias intensity $\mathrm{AI}$, or peak ground
velocity $\mathrm{PGV}$), $\mu_{\ln D}$ is the model-predicted mean in natural-log space,
$\sigma_{\ln D}$ is the associated log-space standard deviation representing within-model aleatory
variability, and $\epsilon$ is a standard normal random variate capturing residual scatter not
explained by the regression predictors. This common probabilistic structure permits all seven
models to be integrated consistently within the ensemble.

Ground-motion intensity measures required by the displacement models are obtained from
probabilistic seismic hazard analysis (PSHA) or site-specific response calculations. Spectral
accelerations are evaluated at the model-specific reference periods, typically $S_a(\alpha T_n)$
with $\alpha$ in the range 1.3 to 1.5. When the required spectral ordinates are not available at
the exact periods from the hazard output, logarithmic interpolation in period is applied. Where the
site hazard is referenced to rock conditions, period-dependent site amplification factors are
applied to translate reference-rock ground motions to site-specific values, with amplification
model uncertainty propagated as a lognormal variable within the Monte Carlo simulation.
[@KBnewmark]

## Appendix A: Newmark Displacement Equations, Calibration, and Error Terms

The following notation applies throughout this appendix. $D$ denotes permanent (residual) displacement in centimeters. $k_y = a_y/g$ is the dimensionless yield-acceleration ratio. $r = k_y/\mathrm{PGA}$ is the critical acceleration ratio. $T_n$ is the fundamental period of the sliding mass in seconds. $M_w$ is the earthquake moment magnitude. $S_a$ denotes spectral acceleration in units of $g$ at the period specified for each model. $\mathrm{PGA}$ is peak ground acceleration in $g$. $\mathrm{PGV}$ is peak ground velocity in centimeters per second. $\mathrm{AI}$ is Arias intensity in meters per second. All dispersion terms $\sigma$ are one-standard-deviation values in natural-log space unless explicitly identified as $\log_{10}$-space values. [@KBnewmarkmodel]

### A.1 Bray and Macedo (2017) - Flexible-Block Model, Subduction Earthquakes

This model was developed from ground-motion records of subduction zone earthquakes, encompassing Chilean and Japanese seismic events, and is calibrated for deep subduction interface and intraslab tectonic settings [@BrayMacedo2017][@KBnewmarkmodel]. The flexible-block idealization is employed, and the model is applicable to both shallow translational and deep rotational failure geometries in which the sliding mass exhibits a measurable fundamental period. Spectral acceleration is evaluated at the fundamental period $T_n$ of the sliding mass.

The mean log-displacement is expressed as a quadratic polynomial in $\ln S_a$:

$$\mu_{\ln D} = a_0 + a_1 \ln S_a + a_2 (\ln S_a)^2$$

with period-dependent and magnitude-dependent coefficients:

$$\begin{aligned}
a_0 &=
\begin{cases}
-5.864 + 0.550\,M_w - 9.421\,T_n - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n < 0.1 \\
-6.896 + 0.550\,M_w + 3.081\,T_n - 0.803\,T_n^{2} - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n \geq 0.1
\end{cases}\\[4pt]
a_1 &= 3.060 + 0.538\ln k_y, \qquad a_2 = -0.225
\end{aligned}$$

$$\sigma_{\ln D} = 0.73$$

The piecewise definition of $a_0$ distinguishes between very stiff sliding masses ($T_n < 0.1$ s) and more flexible ones, reflecting the transition in dynamic response characteristics. This model is the preferred formulation for sites where seismic hazard is dominated by subduction interface or intraslab events. [@BrayMacedo2017][@KBnewmarkmodel]

### A.2 Bray and Macedo (2019) - Flexible-Block Model, Shallow-Crustal Earthquakes

This model follows the same quadratic-in-$\ln S_a$ functional form as the 2017 subduction model but is calibrated for shallow-crustal tectonic environments typical of active plate margins [@BrayMacedo2019][@KBnewmarkmodel]. Spectral acceleration is evaluated at $1.3\,T_n$ rather than $T_n$, reflecting the period elongation associated with yielding under strong crustal shaking. A peak ground velocity correction term is incorporated for ground motions with $\mathrm{PGV} > 115$ cm/s, capturing near-fault directivity effects on cumulative displacement accumulation.

$$\begin{aligned}
a_0 &=
\begin{cases}
-4.551 + 0.607\,M_w - 9.690\,T_n - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n < 0.1 \\
-5.894 + 0.607\,M_w + 3.152\,T_n - 0.910\,T_n^{2} - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n \geq 0.1
\end{cases}\\[4pt]
&\quad +\;
\begin{cases}
0, & \mathrm{PGV} \leq 115\;\text{cm/s} \\
\ln\mathrm{PGV} - 4.75, & \mathrm{PGV} > 115\;\text{cm/s}
\end{cases}\\[4pt]
a_1 &= 2.703 + 0.344\ln k_y, \qquad a_2 = -0.089
\end{aligned}$$

$$\sigma_{\ln D} = 0.74$$

When $\mathrm{PGV}$ is not directly available from the hazard analysis, it may be estimated from $\mathrm{PGA}$ using an empirical predictive relationship. The model is applicable to both translational and rotational failure geometries in flexible sliding masses within shallow-crustal seismic regimes. [@BrayMacedo2019][@KBnewmarkmodel]

### A.3 Bray and Travasarou (2007) - Flexible-Block Model, General Tectonic Setting

This model was calibrated using 688 recorded ground motions from 41 worldwide earthquakes spanning a broad magnitude range and multiple tectonic environments [@BrayTravasarou2007][@KBnewmarkmodel]. It does not distinguish between subduction and shallow-crustal settings, providing general-purpose displacement predictions applicable across tectonic regimes. Spectral acceleration is evaluated at $1.5\,T_n$. The model is applicable to both shallow translational and rotational failure geometries in deformable sliding masses.

$$\mu_{\ln D} = -1.10 - 2.83\ln k_y - 0.333(\ln k_y)^2 + 0.566\ln k_y \ln S_a + 3.04\ln S_a - 0.244(\ln S_a)^2 + 0.278(M_w - 7)$$

$$\sigma_{\ln D} = 0.66$$

The interaction term $0.566\ln k_y \ln S_a$ captures the nonlinear coupling between slope resistance and ground-motion intensity. The magnitude scaling term $0.278(M_w - 7)$ accounts for duration effects, whereby larger-magnitude events produce greater displacement for an equivalent spectral demand. [@BrayTravasarou2007][@KBnewmarkmodel]

### A.4 Jibson (2007) - Rigid-Block Model

The Jibson (2007) model was calibrated using 2,270 strong-motion records from 30 worldwide earthquakes, constituting one of the largest calibration datasets among the rigid-block formulations [@Jibson2007][@KBnewmarkmodel]. Arias intensity $\mathrm{AI}$ serves as the primary ground-motion descriptor, capturing both the amplitude and the cumulative energy content of the motion and thereby encoding an implicit sensitivity to shaking duration. The model is applicable to shallow translational failure surfaces for which the rigid-block assumption is physically appropriate.

The mean log-displacement, expressed in natural-log space after conversion, is:

$$\mu_{\ln D} = \left[\,0.561\log_{10}\mathrm{AI} - 3.833\log_{10}\!\left(\frac{k_y}{\mathrm{PGA}}\right) - 1.474\right]\ln 10$$

$$\sigma_{\log_{10} D} = 0.616 \qquad (\sigma_{\ln D} = 0.616\ln 10 \approx 1.418)$$

This dispersion value is the largest among the ensemble models, reflecting the greater residual scatter inherent in single-parameter rigid-block predictors. When $\mathrm{AI}$ is not available from the site hazard analysis, it may be estimated empirically from $\mathrm{PGA}$. [@Jibson2007][@KBnewmarkmodel]

### A.5 Saygili and Rathje (2008) - Rigid-Block Model, Multi-Parameter

This multi-parameter rigid-block model was calibrated against over 2,000 acceleration time histories from shallow-crustal earthquakes and was designed to reduce the aleatory variability inherent in single-intensity-measure predictors by combining $\mathrm{PGA}$, Arias intensity $\mathrm{AI}$, and the critical acceleration ratio $r$ [@SaygiliRathje2008][@KBnewmarkmodel]. The model is calibrated for shallow translational failure geometries.

$$\mu_{\ln D} = 2.39 - 5.24\,r - 18.78\,r^2 + 42.01\,r^3 - 29.15\,r^4 - 1.56\ln\mathrm{PGA} + 1.38\ln\mathrm{AI}, \qquad r = \frac{k_y}{\mathrm{PGA}}$$

Unlike the other ensemble models, the dispersion is not constant but varies with the critical acceleration ratio:

$$\sigma_{\ln D} = 0.46 + 0.56\,r$$

This heteroscedastic formulation reflects the physical observation that slopes with higher yield-to-demand ratios exhibit greater relative scatter in displacement predictions. [@SaygiliRathje2008][@KBnewmarkmodel]

### A.6 Ambraseys and Menu (1988) - Rigid-Block Model

This classical rigid-block regression was developed from 50 strong-motion records obtained at near-fault distances from 11 earthquakes in the moment magnitude range $M_w = 6.6$ to $7.3$, representing one of the earliest quantitative regression-based rigid-block displacement predictors [@AmbraseysMenu1988][@KBnewmarkmodel]. The model expresses the mean $\log_{10}$ displacement as a function of the critical acceleration ratio $r$ only, making it applicable when only $\mathrm{PGA}$ and $k_y$ are available. The restricted calibration database warrants caution when applying the model to subduction or deep-focus events outside the original tectonic and distance range.

$$\mu_{\log_{10} D} = 0.90 + \log_{10}\!\left[(1 - r)^{2.53}\,r^{-1.09}\right], \qquad r = \frac{k_y}{\mathrm{PGA}}$$

$$\sigma_{\log_{10} D} = 0.30 \qquad (\sigma_{\ln D} = 0.30\ln 10 \approx 0.691)$$

The functional form exhibits nonlinear dependence on $r$, with asymptotic behavior as $r \to 1$ (onset of failure) and as $r \to 0$ (very low relative strength demand). Its small calibration dataset and restricted tectonic and distance range result in a lower ensemble weight compared to models calibrated on larger, more diverse ground-motion databases. [@AmbraseysMenu1988][@KBnewmarkmodel]

### A.7 Yegian, Marciano, and Ghahraman (1991) - Rigid-Block Model

The Yegian et al. (1991) model expresses the mean $\log_{10}$ displacement as a cubic polynomial in the critical acceleration ratio $r$, calibrated from rigid-block time-history integrations performed using recorded earthquake acceleration time histories within a probabilistic framework for estimating earthquake-induced permanent deformations of earth dams and embankments [@Yegian1991][@KBnewmarkmodel]. The model is applicable to shallow translational failure geometries.

$$\mu_{\log_{10} D} = 0.22 - 10.12\,r + 16.38\,r^2 - 11.48\,r^3, \qquad r = \frac{k_y}{\mathrm{PGA}}$$

$$\sigma_{\log_{10} D} = 0.45 \qquad (\sigma_{\ln D} = 0.45\ln 10 \approx 1.036)$$

The computationally efficient polynomial form in $r$ provides continuity with established dam engineering practice. As with the Ambraseys and Menu (1988) formulation, the relatively small calibration dataset and the absence of duration-sensitive predictors result in a lower ensemble weight compared to models calibrated against larger and more diverse ground-motion databases. [@Yegian1991][@KBnewmarkmodel]

---

All models are formulated or transformed into lognormal space to accommodate the skewed, positive-definite nature of displacement data and to permit probabilistic analysis through standard normal random variates. The $\sigma_{\ln D}$ terms capture both the regression error from the original model calibration and the inherent variability in earthquake response not explained by the selected intensity measures. For models reported in $\log_{10}$ space, conversions to natural-log space use the identity $\sigma_{\ln D} = \sigma_{\log_{10} D} \cdot \ln 10$. When intensity measures required by a given model are not directly available from the hazard output, empirical estimation or logarithmic interpolation in period space may be applied to obtain the required spectral ordinates. [@KBnewmarkmodel]

## 5. Ensemble Numerical Model: Weighted Sum of Displacement Predictions

The displacement prediction methodology employs a weighted ensemble combining all seven Newmark
models documented in the preceding appendix. Rather than relying on a single displacement
predictor, the ensemble approach retains epistemic uncertainty across the full suite by assigning
each model a logic-tree weight and aggregating the resulting displacement realizations into a
combined distribution. This structure is analogous to the multi-model logic-tree treatment of
ground-motion prediction equations in probabilistic seismic hazard analysis: the weighted
combination acknowledges that no single model constitutes a definitive predictor of sliding
displacement, and the dispersion of predictions across the ensemble constitutes a meaningful
component of the total uncertainty budget. The ensemble captures both the within-model aleatory
variability - represented by each model's $\sigma_{\ln D}$ - and the between-model epistemic
uncertainty - represented by the scatter of weighted predictions across the suite.
[@KBnewmark][@KBuncertainty]

The logic-tree weighting scheme assigns proportionally greater influence to models calibrated on
larger and more comprehensive ground-motion databases. The Bray and Macedo (2017)
[@BrayMacedo2017] and Bray and Macedo (2019) [@BrayMacedo2019] flexible-block models, calibrated
on extensive datasets that incorporate a wider range of magnitude-distance-site combinations with
explicit treatment of duration effects, receive higher weights in the ensemble than the Ambraseys
and Menu (1988) [@AmbraseysMenu1988] and Yegian et al. (1991) [@Yegian1991] rigid-block
formulations, which were developed from comparatively limited record sets. This weighting
philosophy reflects the principle that models with broader empirical support and more explicit
treatment of ground-motion characteristics should dominate the ensemble prediction.
[@KBnewmarkmodel][@KBnewmark]

The ensemble framework serves two complementary objectives. First, it reduces sensitivity to the
idiosyncratic features of any individual regression dataset or functional form, mitigating the
risk that a single model's extrapolation behavior outside its calibration domain dominates the
result. Second, it preserves the epistemic uncertainty associated with displacement model
selection, representing it explicitly through the spread of model predictions rather than
collapsing all candidates into a single best-estimate formula. This between-model epistemic
component supplements the within-model aleatory variability captured by each model's standard
deviation $\sigma_{\ln D}$. [@KBuncertainty]

For each Monte Carlo realization, the log-space displacement from model $i$ is computed as:

$$\ln D_i = \mu_{\ln D_i}(\mathrm{IM},\, k_y,\, T_n,\, M_w) + \epsilon_i\,\sigma_{\ln D_i}$$

where $\epsilon_i \sim \mathcal{N}(0,1)$ is drawn independently for each model $i$, preserving
within-model aleatory variability. The ensemble log-displacement for that realization is the
weighted sum:

$$\ln D_{\mathrm{ens}} = \sum_{i=1}^{N} w_i\,\ln D_i
  = \sum_{i=1}^{N} w_i\!\left[\mu_{\ln D_i} + \epsilon_i\,\sigma_{\ln D_i}\right]$$

where $N = 7$ is the total number of models in the ensemble and $w_i > 0$ are the logic-tree
weights satisfying $\sum_{i=1}^{N} w_i = 1$. No model is excluded from the ensemble; all seven
contribute weighted predictions to the final result. [@KBnewmark][@KBuncertainty]

The full simulation iterates across a predefined grid of material scenarios, geometric
configurations, and seismic service levels. For each combination of yield acceleration $k_y$,
material scenario, and hazard level, the displacement distribution is assembled from all Monte
Carlo realizations, each of which draws sampled intensity measures from the empirical hazard
quantile functions, applies period-specific site amplification factors with their associated
uncertainties, and evaluates all seven displacement models. Quantiles of the resulting ensemble
distribution - including the median, 84th percentile, and 95th percentile - are extracted
directly from the assembled empirical realizations. The distribution reflects the joint effect of
ground-motion variability (sampled from probabilistic seismic hazard analysis quantile
functions), site amplification uncertainty (propagated through the lognormal amplification
model), and displacement model uncertainty (represented by the weighted logic-tree ensemble).
This probabilistic characterization of permanent displacement as a function of $k_y$ provides
the statistical basis for the seismic coefficient derivation presented in Section 6.
[@KBnewmark][@KBuncertainty]

---

## SLOT 6: Seismic Coefficient Derivation from Target Residual Displacement

The ensemble displacement distribution established in Section 5 provides the direct input to
seismic coefficient derivation. Given the full statistical characterization of permanent
displacement $D_n(k_y)$ as a function of trial yield acceleration, the performance-based seismic
coefficient $k_{\max}$ is obtained by numerical inversion of a displacement performance criterion.

For a given trial yield acceleration $k_y$, the exceedance probability is defined as:

$$p(k_y) = \mathbb{P}\!\left[D_n(k_y) > D_n^{\star}\right]$$

where $D_n(k_y)$ is the random variable representing the ensemble-predicted Newmark displacement,
conditional on the selected value of $k_y$ and incorporating all aleatory and epistemic
uncertainties from the ground-motion hazard, the site amplification model, and the displacement
prediction models. The allowable displacement $D_n^{\star}$ is the project-level design criterion
for permanent seismic ground deformation. [@KBpbkmax]

The function $p(k_y)$ is monotonically non-increasing in $k_y$: greater yield strength
consistently reduces the probability of exceeding any fixed displacement threshold. The
performance-based seismic coefficient is defined by the implicit relationship:

$$k_{\max}(p \mid D_n^{\star}) = \inf\!\left\{k_y : \mathbb{P}\!\left[D_n(k_y) > D_n^{\star}\right] \leq p\right\}$$

This expression identifies the smallest yield acceleration for which the probability of exceeding
the allowable displacement is controlled at the specified level. The equation directly links
$k_{\max}$ to three independently specified quantities: the target exceedance probability $p$
(reflecting the consequence category and return period assigned to the structure), the allowable
displacement $D_n^{\star}$ (reflecting the tolerable permanent deformation of the slope), and the
full statistical characterization of displacement through the ensemble model. The resulting
$k_{\max}$ is hazard-consistent, incorporating variability in ground-motion intensity measures,
site amplification, and displacement model prediction. [@KBpbkmax]

The inversion is implemented numerically by evaluating $p(k_y)$ over a discrete grid of candidate
$k_y$ values. For each grid point, $p(k_y)$ is estimated as the fraction of Monte Carlo
realizations for which the ensemble-predicted displacement exceeds $D_n^{\star}$. Each realization
represents a fully correlated draw of ground-motion intensity measures from PSHA hazard quantile
functions, site amplification factors sampled from the lognormal amplification model, and
displacement model residuals drawn through the standard normal variate $\epsilon_i$ applied to
each model's $\sigma_{\ln D}$. The value of $k_y$ at which the empirical fraction falls at or
below $p$ is identified as $k_{\max}$, resolved to the desired precision by bisection or direct
grid search. Displacement values below a minimum threshold are floored at $10^{-16}$ m to
maintain well-defined logarithmic operations; this floor is negligible relative to engineering-
scale displacements. [@KBpbkmax][@KBuncertainty]

Performance-based seismic coefficients are reported across service levels corresponding to annual
exceedance probabilities (AEPs) from $1/100$ to $1/10{,}000$ per annum, for each combination of
material scenario and geometric configuration representative of the facility under assessment.
Separate $k_{\max}$ values are derived for each service level and scenario, expressed in units of
gravitational acceleration ($g$). These coefficients are applied as the design horizontal seismic
coefficient $k_h = k_{\max}$ in pseudo-static limit-equilibrium stability analysis, completing
the performance-based cycle from seismic hazard characterization through site response, Newmark
displacement estimation, and design coefficient derivation. [@KBpbkmax]
