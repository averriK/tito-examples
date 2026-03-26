# Executive Memorandum: Horizontal Seismic Coefficient Estimation for Pseudo-Static Slope Stability Analysis

## SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

The pseudo-static method is the most widely applied technique for assessing seismic slope stability in engineering practice. Earthquake loading is represented as an equivalent static horizontal force equal to the product of a seismic coefficient $k$ and the weight of the potential sliding mass, and stability is evaluated by conventional limit-equilibrium analysis. The reliability of this method depends critically on the selection of the seismic coefficient, which must reflect the seismic hazard level at the site, the dynamic response characteristics of the slope, and the acceptable level of permanent deformation under design loading. [KB:pbkmax.qmd]^[Confidence: HIGH, Rationale: The description of the pseudo-static method and the centrality of the seismic coefficient selection are consistent with standard geotechnical engineering practice and are directly supported by the framework outlined in KB:pbkmax.qmd, which treats k_y as the primary design parameter.]

The performance-based seismic coefficient $k_{\max}$ is established as the minimum yield acceleration consistent with a prescribed displacement performance objective, incorporating the combined statistical effects of ground-motion variability, model dispersion, and site-specific uncertainty. The framework links the allowable permanent displacement threshold $D_n^{\star}$ directly to the statistical distribution of Newmark-type permanent displacements across the full set of seismic hazard and material scenarios considered for the project. [KB:pbkmax.qmd]^[Confidence: HIGH, Rationale: The definition of k_max as an infimum consistent with an allowable displacement objective is stated explicitly and consistently in KB:pbkmax.qmd, with no contradictions detected across KB sources.]

Let $D_n$ denote the random variable representing Newmark-type displacement, incorporating all aleatory and epistemic uncertainties as characterized in the seismic hazard and site response analyses. For a given yield acceleration $k_y$, the exceedance probability for the allowable displacement threshold is given by:^[Confidence: HIGH, Rationale: This paragraph directly introduces the probabilistic formulation from KB:pbkmax.qmd; all variables and terminology are consistent with that source, and the display equation that follows is reproduced without modification.]

$$p(k_y) = \mathbb{P}[D_n(k_y) > D_n^{\star}]$$

where $D_n(k_y)$ is the distribution of predicted displacements conditional on the selected value of $k_y$, reflecting variability in ground-motion parameters and model-specific scatter in displacement prediction. The performance-based seismic coefficient $k_{\max}$ for a target exceedance probability $p$ satisfies the implicit relationship $p = p(k_{\max})$, and is formally defined as:^[Confidence: HIGH, Rationale: The interpretation of D_n(k_y) as a conditional distribution and the implicit equation p = p(k_max) are stated in KB:pbkmax.qmd and are internally consistent with the display equation preceding this paragraph.]

$$k_{\max}(p\,|\,D_n^{\star}) = \inf \left\{ k_y : \mathbb{P}[D_n(k_y) > D_n^{\star}] \leq p \right\}$$

For any given $p$, $k_{\max}$ represents the lowest yield acceleration at which the probability of exceeding the allowable displacement is controlled at the specified level under the combined statistical effects of hazard, site amplification, and displacement model variability. Displacement values below a numerical threshold are floored at $10^{-16}$ m to maintain well-defined logarithmic operations within the displacement models. [KB:pbkmax.qmd]^[Confidence: HIGH, Rationale: The infimum definition of k_max and the numerical floor for displacement values are both stated explicitly in KB:pbkmax.qmd. No contradictions or ambiguities are detected relative to other KB sources.]

This seismic coefficient is calibrated to two sets of project-specific inputs: first, the target hazard intensity level, expressed as an annual exceedance probability (AEP) that reflects the degree of consequences associated with slope failure; and second, slope characteristics including material stiffness, shear strength, and the fundamental period of the potential sliding mass. Performance-based seismic coefficients are reported across service levels ranging from AEP 1/100 to 1/10,000 for geometry and material scenarios representative of tailings storage facilities (TSF) and waste rock dumps (WRD). [KB:pbkmax.qmd][KB:newmark.qmd]^[Confidence: HIGH, Rationale: Calibration to AEP service levels (1/100 to 1/10,000) and application to TSF and WRD scenarios are stated in KB:pbkmax.qmd. The slope characteristics (k_y, T_n, material properties) are defined in KB:newmark.qmd, and both KB sources are consistent on these points.]

## SLOT 2: State of Current Practice for Performance-Based Seismic Slope Design

Traditional seismic slope stability assessment relied on prescriptive, deterministic seismic coefficients derived from building-code provisions or regulatory convention. A fixed fraction of peak ground acceleration (PGA), typically applied uniformly across site conditions, was used as the horizontal pseudo-static force, and slope stability was judged solely by whether the factor of safety exceeded a prescribed minimum. These coefficients were established largely by precedent without explicit connection to allowable deformation or the dynamic characteristics of the slope. This approach has been widely recognized as incomplete because it does not capture the capacity of slopes to accommodate limited permanent deformation without reaching a serviceability limit state, nor does it account for the dependence of seismic demand on the fundamental period of the sliding mass. [WEB:https://ascelibrary.org/doi/10.1061/%28ASCE%29GT.1943-5606.0000012]^[Confidence: MEDIUM, Rationale: The characterization of traditional prescriptive approaches and their limitations is consistent with the published literature on pseudo-static seismic slope analysis and is supported by the ASCE reference. However, specific ranges for prescriptive coefficients vary by jurisdiction and document, and the KB does not provide a direct comparative statement on historical practice, so confidence is MEDIUM rather than HIGH.]

The modern state of practice has transitioned toward performance-based procedures in which the seismic coefficient is derived from displacement-based criteria. The foundational contribution to this transition is the procedure developed by Bray and Travasarou [@BrayTravasarou2007], which introduced a rational framework for computing the seismic coefficient from site-specific hazard, the allowable level of seismic displacement, and the dynamic response characteristics of the slope. This procedure established the principle that the design seismic coefficient should be based on the seismic hazard at the site and the displacement that constitutes satisfactory performance for the structure. [KB:newmark.qmd][WEB:https://fl-nzgs-media.s3.amazonaws.com/uploads/2016/07/Bray-2011-Pseudostatic-slope-stability-procedure-paper.pdf]^[Confidence: HIGH, Rationale: The Bray and Travasarou (2007) reference is cited in KB:newmark.qmd in the context of the flexible-block model and is corroborated by the external source describing the follow-up 2011 procedure paper; the characterization of this work as the basis for performance-based coefficient selection is consistent across both sources.]

Current guidance from major standards bodies reflects this evolution toward deformation-based acceptance criteria. The U.S. Army Corps of Engineers (USACE) and AASHTO/NCHRP guidance on seismic design of geotechnical structures recognize Newmark sliding-block analysis as the reference method for computing seismic deformation of embankments and slopes, and require that permanent deformation estimates be assessed against allowable displacement thresholds rather than a minimum factor of safety in isolation. [WEB:https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1902.pdf][WEB:https://www.ce.memphis.edu/7137/PDFs/Seismic%20Manual/nchrp_rpt_611.pdf]^[Confidence: MEDIUM, Rationale: The characterization of USACE EM 1110-2-1902 and NCHRP Report 611 as requiring deformation-based criteria is based on web sources accessed via search results. Both documents are well-known and authoritative, but specific provisions are summarized from search abstracts rather than direct document retrieval, introducing some uncertainty about exact wording and scope.]

For tailings storage facilities and mine waste structures, the application of performance-based seismic coefficients is of particular importance given the potential severity of failure consequences. Published research demonstrates that pseudo-static analyses for TSFs yield reliable results only when the seismic coefficient is derived from a rational displacement criterion, calibrated to the structure's dynamic characteristics and the acceptable deformation level, rather than from a fixed fraction of PGA selected without this connection. [WEB:https://www.researchgate.net/publication/323571904_Simplified_Calculation_of_Seismic_Displacements_on_Tailings_Storage_Facilities]^[Confidence: MEDIUM, Rationale: The claim about the reliability of pseudo-static analysis for TSFs conditional on rational coefficient selection is supported by the cited web source. Confidence is MEDIUM because this assertion draws on a single external reference rather than KB material or multiple independent authoritative sources.]

A performance-based probabilistic procedure for estimating the pseudo-static coefficient links the seismic coefficient directly to seismically induced displacement hazard curves, providing estimates consistent with the allowable displacement level, the properties of the sliding mass, the seismic demand at the site, and the design return period. Such procedures have been applied for multiple tectonic settings, including subduction and shallow-crustal earthquake environments. [WEB:https://www.sciencedirect.com/science/article/abs/pii/S0267726119309844]^[Confidence: MEDIUM, Rationale: The description of the probabilistic procedure linking k_max to displacement hazard curves is supported by the cited ScienceDirect source on performance-based assessment of pseudo-static coefficients. Confidence is MEDIUM because the supporting evidence is from an abstract summary rather than a full document retrieval, and the KB does not directly address the comparative state of practice.]

## SLOT 3: Newmark Displacement Analysis Methodologies

Seismic-induced permanent displacements of slopes are quantified using the Newmark sliding-block approach, which conceptualizes the sliding mass as a block with a critical yield acceleration $k_y$. When the ground acceleration exceeds $k_y$, the mass undergoes incremental downslope movement, and total displacement $D$ accumulates throughout the duration of shaking. The response is characterized probabilistically using empirical or semi-empirical regression relationships that link $\ln D$ to ground-motion parameters and slope properties. [KB:newmark.qmd]^[Confidence: HIGH, Rationale: The fundamental description of the Newmark approach - yield acceleration threshold, incremental displacement accumulation, and log-normal regression formulation - is stated consistently and explicitly in KB:newmark.qmd, with no contradictions detected.]

Two principal idealizations are employed depending on the dynamic stiffness of the sliding mass. In the rigid-block (decoupled) idealization, the sliding mass is assumed to be infinitely stiff relative to the underlying material, and the earthquake input motion is applied directly as the base acceleration without dynamic modification. The response is governed solely by the ratio $r = k_y / \mathrm{PGA}$. This idealization is appropriate for stiff, shallow failure surfaces where the fundamental period of the sliding mass is short relative to the dominant periods of the ground motion. The rigid-block models applied in this framework are those of Ambraseys and Menu [@AmbraseysMenu1988], Yegian et al. [@Yegian1991], Jibson [@Jibson2007], and Saygili and Rathje [@SaygiliRathje2008]. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: The definition of the rigid-block idealization, the governing parameter r = k_y/PGA, and the identification of four rigid-block models are directly supported by KB:newmark_model.qmd, which labels all four entries as Rigid-Block Models.]

In the flexible-block (compliant) idealization, the dynamic amplification of ground motion within the sliding mass is accounted for by incorporating the fundamental period $T_n$ of the potential failure volume. The seismic demand is characterized by the spectral acceleration $S_a$ evaluated at a period that captures the dynamic response of the sliding mass, rather than by $\mathrm{PGA}$ alone. This idealization is more appropriate for deeper or softer failure surfaces that undergo meaningful period-dependent amplification. The flexible-block models applied in this framework are those of Bray and Travasarou [@BrayTravasarou2007], Bray and Macedo [@BrayMacedo2017], and Bray and Macedo [@BrayMacedo2019]. [KB:newmark_model.qmd][KB:newmark.qmd]^[Confidence: HIGH, Rationale: The flexible-block concept, the role of T_n and S_a, and the three applicable models are directly supported by KB:newmark_model.qmd, which labels all three as Flexible-Block (compliant) models. KB:newmark.qmd further confirms S_a and T_n as key inputs for compliant formulations.]

All predictive models are formulated in the following general probabilistic form, where $D$ is permanent displacement in cm:^[Confidence: HIGH, Rationale: The general probabilistic form with ln D, mu_ln_D, and sigma_ln_D is stated explicitly and identically in KB:newmark.qmd. This paragraph introduces the display equation that follows without adding unsupported claims.]

$$\ln D = \mu_{\ln D}(\mathrm{IM}, k_y, T_n, M_w) + \epsilon\,\sigma_{\ln D}$$

Here $\mathrm{IM}$ denotes the set of ground-motion intensity measures specific to each model (e.g., $\mathrm{PGA}$, $S_a$ at a reference period, Arias intensity $\mathrm{AI}$, peak ground velocity $\mathrm{PGV}$), $T_n$ is the fundamental period of the sliding mass in seconds, and $M_w$ is the moment magnitude where included by the model. The term $\mu_{\ln D}$ is the model-predicted mean log-displacement as a function of these parameters, $\sigma_{\ln D}$ is the associated standard deviation in natural-log space, and $\epsilon$ is a standard normal variate that accounts for record-to-record variability not captured by the regression. [KB:newmark.qmd]^[Confidence: HIGH, Rationale: All symbol definitions (IM, T_n, M_w, mu_ln_D, sigma_ln_D, epsilon) are stated in identical terms in KB:newmark.qmd; this paragraph is a direct restatement of the KB notation legend.]

Ground-motion intensity measures are obtained from the site hazard results. Spectral accelerations are evaluated at periods required by each model, typically at $S_a(\alpha T_n)$ with $\alpha$ in the range 1.3 to 1.5 depending on the model specification. Where spectral ordinates are not explicitly available in the hazard output, logarithmic interpolation in period is applied. The yield acceleration $k_y$ is established by geotechnical analysis and expressed as a fraction of gravity, and the selection of $M_w$ follows the seismic scenario or logic-tree branch appropriate to the site. [KB:newmark.qmd]^[Confidence: HIGH, Rationale: The procedure for obtaining IM from site hazard, the alpha T_n range of 1.3 to 1.5, logarithmic interpolation, and M_w selection from the logic-tree are all stated in KB:newmark.qmd with consistent terminology and no contradictions detected.]

## SLOT 4: Appendix - Newmark Displacement Equations by Method

The following section presents the predictive equations for each Newmark displacement model included in the ensemble. For all models, $D$ denotes permanent displacement in cm, $k_y = a_y/g$ is the dimensionless yield-acceleration ratio, $\mathrm{PGA}$ is peak ground acceleration in $g$, $\mathrm{PGV}$ is peak ground velocity in cm/s, $T_n$ is the fundamental period of the sliding mass in seconds, and all dispersions $\sigma$ are one-standard-deviation values in natural-log space unless otherwise stated. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: The notation legend is directly stated in KB:newmark_model.qmd with identical parameter definitions, and is consistent with the general notation established in KB:newmark.qmd.]

### Bray and Macedo (2017) [@BrayMacedo2017]

*Flexible-Block (Compliant) Model - Subduction earthquakes.* This model is calibrated for subduction-zone earthquake environments and takes the functional form $\mu_{\ln D} = a_0 + a_1 \ln S_a + a_2 (\ln S_a)^2$, with coefficients:^[Confidence: HIGH, Rationale: Model type, tectonic setting, and functional form are stated in KB:newmark_model.qmd with no unsupported claims.]

$$\begin{aligned}
a_0 &=
\begin{cases}
-5.864 + 0.550\,M_w - 9.421\,T_n - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n < 0.1\\
-6.896 + 0.550\,M_w + 3.081\,T_n - 0.803\,T_n^{2} - 3.353\ln k_y - 0.390(\ln k_y)^2, & T_n \geq 0.1
\end{cases}\\
a_1 &= 3.060 + 0.538\ln k_y, \qquad a_2 = -0.225
\end{aligned}$$

$$\sigma_{\ln D} = 0.73$$

$S_a$ is evaluated at the fundamental period $T_n$ in $g$. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Coefficients a_0, a_1, a_2, and sigma are reproduced exactly from KB:newmark_model.qmd. Sa evaluated at T_n is stated in that source. No discrepancies detected.]

### Bray and Macedo (2019) [@BrayMacedo2019]

*Flexible-Block (Compliant) Model - Shallow-crustal earthquakes.* The functional form is identical to the 2017 subduction model, with updated coefficients reflecting calibration on shallow-crustal ground-motion data:^[Confidence: HIGH, Rationale: The description of identical functional form with different coefficients is stated in KB:newmark_model.qmd, which notes 'Same functional form as above, with coefficients'.]

$$\begin{aligned}
a_0 &=
\begin{cases}
-4.551 + 0.607\,M_w - 9.690\,T_n - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n < 0.1\\
-5.894 + 0.607\,M_w + 3.152\,T_n - 0.910\,T_n^{2} - 2.491\ln k_y - 0.245(\ln k_y)^2, & T_n \geq 0.1
\end{cases}\\
&\quad+\;
\begin{cases}
0, & \mathrm{PGV} \leq 115\;\text{cm/s}\\
\ln \mathrm{PGV} - 4.75, & \mathrm{PGV} > 115\;\text{cm/s}
\end{cases}\\
a_1 &= 2.703 + 0.344\ln k_y, \qquad a_2 = -0.089
\end{aligned}$$

$$\sigma_{\ln D} = 0.74$$

$S_a$ is evaluated at $1.3\,T_n$ in $g$. $\mathrm{PGV}$ is in cm/s; if not supplied it is estimated from $\mathrm{PGA}$. This model was calibrated using ground-motion recordings from the NGA-West2 database, capturing key sources of uncertainty in seismic slope displacement for shallow-crustal tectonic settings. [KB:newmark_model.qmd][DOI:10.1061/(ASCE)GT.1943-5606.0002143]^[Confidence: HIGH, Rationale: All coefficients and sigma are reproduced exactly from KB:newmark_model.qmd. The Sa evaluation at 1.3 T_n and PGV correction are stated there. The NGA-West2 calibration database is confirmed by the DOI source (ASCE JGGE 2019, Vol 145 No 12). No contradictions detected.]

### Bray and Travasarou (2007) [@BrayTravasarou2007]

*Flexible-Block (Compliant) Model.*^[Confidence: HIGH, Rationale: Model type is stated in KB:newmark_model.qmd as Flexible-Block (compliant). This is a one-line descriptor with no additional claims.]

$$\mu_{\ln D} = -1.10 - 2.83\ln k_y - 0.333(\ln k_y)^2 + 0.566\ln k_y \ln S_a + 3.04\ln S_a - 0.244(\ln S_a)^2 + 0.278(M_w - 7)$$

$$\sigma_{\ln D} = 0.66$$

$S_a$ is evaluated at $1.5\,T_n$ in $g$. The inclusion of moment magnitude $M_w$ as an additive term captures the influence of ground-motion duration on accumulated displacement, consistent with the compliant-block framework. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Equation coefficients, sigma, and Sa evaluation period are reproduced exactly from KB:newmark_model.qmd. The Mw term interpretation as a duration proxy is consistent with standard usage in flexible-block literature and is supported by KB:newmark.qmd, which identifies Bray and Travasarou as a 'duration-sensitive' formulation.]

### Jibson (2007) [@Jibson2007]

*Rigid-Block Model.*^[Confidence: HIGH, Rationale: Model type is stated as Rigid-Block Model in KB:newmark_model.qmd. One-line descriptor with no additional claims.]

$$\mu_{\ln D} = \left[0.561\log_{10} \mathrm{AI} - 3.833\log_{10}(k_y/\mathrm{PGA}) - 1.474\right] \ln 10$$

$$\sigma_{\log_{10} D} = 0.616 \quad (\sigma_{\ln D} = 0.616\,\ln 10)$$

$\mathrm{AI}$ is Arias intensity in m/s, estimated from $\mathrm{PGA}$ if not directly available. The ratio $r = k_y / \mathrm{PGA}$ expresses slope strength relative to seismic intensity. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Equation form, sigma, and parameter definitions are reproduced exactly from KB:newmark_model.qmd. The Arias-intensity-based formulation is specific to the Jibson (2007) model as labeled in that source.]

### Saygili and Rathje (2008) [@SaygiliRathje2008]

*Rigid-Block Model. Multi-parameter formulation requiring $\mathrm{AI}$ and $\mathrm{PGA}$.*^[Confidence: HIGH, Rationale: Model type and required inputs are stated in KB:newmark_model.qmd. One-line descriptor with no additional claims.]

$$\mu_{\ln D} = 2.39 - 5.24\,r - 18.78\,r^{2} + 42.01\,r^{3} - 29.15\,r^{4} - 1.56\ln \mathrm{PGA} + 1.38\ln \mathrm{AI}, \qquad r = \frac{k_y}{\mathrm{PGA}}$$

$$\sigma_{\ln D} = 0.46 + 0.56\,r$$

The dispersion is variable and increases with $r$, reflecting greater prediction uncertainty as the slope approaches its yield acceleration from below. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Polynomial coefficients, the variable sigma expression, and the note on increasing dispersion with r are reproduced exactly from KB:newmark_model.qmd, which states 'increases as the slope becomes weaker'. No discrepancies detected.]

### Ambraseys and Menu (1988) [@AmbraseysMenu1988]

*Rigid-Block Model.*^[Confidence: HIGH, Rationale: Model type is stated as Rigid-Block Model in KB:newmark_model.qmd. One-line descriptor with no additional claims.]

$$\mu_{\log_{10} D} = 0.90 + \log_{10}\!\left[(1-r)^{2.53}\,r^{-1.09}\right], \qquad r = \frac{k_y}{\mathrm{PGA}}$$

$$\sigma_{\log_{10} D} = 0.30 \quad (\sigma_{\ln D} = 0.30\,\ln 10)$$

This model is one of the earliest regression-based rigid-block formulations and was developed from a database of strong-motion records. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Equation form and sigma are reproduced exactly from KB:newmark_model.qmd. The characterization as an early formulation is supported by the 1988 publication date. The specific calibration database is not described in the KB for this model; the description here is conservative and does not introduce unsupported claims.]

### Yegian et al. (1991) [@Yegian1991]

*Rigid-Block Model.*^[Confidence: HIGH, Rationale: Model type is stated as Rigid-Block Model in KB:newmark_model.qmd. One-line descriptor with no additional claims.]

$$\mu_{\log_{10} D} = 0.22 - 10.12\,r + 16.38\,r^{2} - 11.48\,r^{3}, \qquad r = \frac{k_y}{\mathrm{PGA}}$$

$$\sigma_{\log_{10} D} = 0.45 \quad (\sigma_{\ln D} = 0.45\,\ln 10)$$

This polynomial regression model provides a parsimonious representation of the displacement-ratio relationship in terms of $r$ and was derived from normalized displacement analyses applied to a set of horizontal-component ground-motion records. [KB:newmark_model.qmd]^[Confidence: HIGH, Rationale: Polynomial coefficients and sigma are reproduced exactly from KB:newmark_model.qmd. The description as a polynomial regression from normalized displacement relationships is consistent with standard characterizations of this model in the geotechnical literature; the original paper is not directly accessible from the KB, but the equation match is exact.]

## SLOT 5: Ensemble Numerical Model

The displacement analysis is performed using a weighted ensemble that combines the full suite of individual Newmark displacement models described in the preceding appendix. For each simulation realization and scenario, the ensemble displacement distribution is assembled across all constituent models, with weights reflecting the relative epistemic credibility assigned to each formulation based on the recency of calibration and the size of the supporting ground-motion database. [KB:newmark.qmd][KB:uncertainty_model.qmd]^[Confidence: HIGH, Rationale: The use of a weighted ensemble with logic-tree weights across all Newmark models is stated explicitly in both KB:newmark.qmd and KB:uncertainty_model.qmd, with consistent terminology.]

The weighting scheme assigns greater weight to more recent models calibrated on larger ground-motion databases. The Bray and Macedo (2017) and Bray and Macedo (2019) models, calibrated respectively on modern subduction-zone and shallow-crustal records, receive the highest weights within their respective tectonic categories. Earlier formulations such as Ambraseys and Menu (1988) and Yegian et al. (1991), developed from more limited datasets, receive lower weights. The Bray and Travasarou (2007), Jibson (2007), and Saygili and Rathje (2008) models receive intermediate weights commensurate with their calibration scope and treatment of ground-motion duration and velocity effects. [KB:uncertainty_model.qmd][KB:newmark_model.qmd]^[Confidence: MEDIUM, Rationale: The general principle that more recent models with larger datasets receive greater weight is stated in KB:uncertainty_model.qmd. Explicit numerical weights for individual models are not specified in the KB; the relative ordering described here is an inference from that stated principle and from the calibration periods implied by the model publication dates. Confidence is therefore MEDIUM.]

For each realization in the displacement simulation, the following procedure is applied. The required intensity measures ($\mathrm{PGA}$, $S_a(T_n)$, $\mathrm{PGV}$, $\mathrm{AI}$) are sampled from their empirical quantile distributions obtained from the probabilistic seismic hazard analysis (PSHA) or site-specific response calculations. For spectral ordinates not tabulated in the hazard output, logarithmic interpolation in period is used. The deterministic mean log-displacement $\mu_{\ln D}$ is then computed for each model from the sampled intensity measures and slope parameters, and the stochastic residual is applied by drawing a standard normal variate $\epsilon$ and computing $\ln D = \mu_{\ln D} + \epsilon\,\sigma_{\ln D}$. For all models, $\sigma_{\ln D}$ is treated as constant across scenarios. [KB:newmark.qmd][KB:uncertainty_model.qmd]^[Confidence: HIGH, Rationale: The simulation procedure - quantile sampling, logarithmic interpolation, and per-realization random deviate - is stated consistently and in detail in both KB:newmark.qmd and KB:uncertainty_model.qmd, with no contradictions between the two sources.]

Model-to-model epistemic uncertainty is retained by assigning logic-tree weights prior to aggregating results over all models. The weighted ensemble preserves the full distribution of predicted displacements across both aleatory variability, captured by $\sigma_{\ln D}$ within each individual model, and epistemic uncertainty, represented by the spread across models under their assigned weights. Quantiles of the assembled ensemble distribution (median, 84th percentile, 95th percentile) are computed directly from the simulated displacement realizations. [KB:uncertainty_model.qmd]^[Confidence: HIGH, Rationale: The aggregation of models with logic-tree weights, the distinction between aleatory and epistemic uncertainty components, and the computation of quantiles from the ensemble are all explicitly stated in KB:uncertainty_model.qmd.]

The uncertainty in input ground-motion parameters is represented by empirical quantile distributions derived from the PSHA or site-specific response calculations. For each oscillator period or amplitude measure required by the displacement models, fractiles at 2%, 5%, 16%, 50%, 84%, 95%, 98%, and the mean are available from the hazard computation, reflecting the combined epistemic and aleatory uncertainty from source, path, and site effects. Where the site hazard is derived from reference-rock conditions ($v_{\mathrm{ref}} = 760$ m/s), period-dependent amplification factors are applied and amplification model uncertainty is propagated as a lognormal variable. [KB:newmark.qmd][KB:uncertainty_model.qmd]^[Confidence: HIGH, Rationale: The fractile set, PSHA-derived quantile distributions, 760 m/s reference rock condition, and lognormal amplification uncertainty propagation are all stated explicitly in KB:newmark.qmd, with supporting and consistent material in KB:uncertainty_model.qmd.]
