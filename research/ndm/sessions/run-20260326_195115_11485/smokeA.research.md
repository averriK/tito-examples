# Horizontal Seismic Coefficient Estimation for Slope Stability Analysis: Executive Memo

## SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

The selection of a horizontal seismic coefficient for pseudo-static slope stability analysis requires careful calibration to target intensity levels corresponding to the degree of consequences associated with slope failure, as well as to slope characteristics including stiffness, strength, and fundamental period. [KB:pbkmax.qmd] The performance-based seismic coefficient $k_{\max}$ represents the minimum horizontal acceleration required to satisfy a prescribed displacement performance objective under the combined effects of ground motion variability, model dispersion, and site-specific uncertainty. [KB:pbkmax.qmd] This coefficient is established through the relationship between an allowable permanent displacement threshold $D_n^{\star}$ and the statistical distribution of predicted displacements $D_n$ across the full set of seismic hazard and material scenarios considered in the project. [KB:pbkmax.qmd] ^[Confidence: HIGH, Rationale: Definitions are directly supported by the KB source on performance-based seismic coefficients, which provides the mathematical foundation and conceptual framework for the approach.]

The fundamental framework links the seismic coefficient to site-specific hazard conditions and displacement-based design objectives through the implicit relationship $k_{\max}(p\,|\,D_n^{\star}) = \inf \{ k_y : \mathbb{P}[D_n(k_y) > D_n^{\star}] \leq p \}$, where the coefficient represents the lowest value of yield acceleration $k_y$ for which the probability of exceeding the allowable displacement is controlled at the specified level. [KB:pbkmax.qmd] The incorporation of combined statistical effects of hazard, site response, and displacement model variability into this framework permits performance-based design decisions that explicitly account for slope-specific consequences and seismic exposure. [KB:pbkmax.qmd] ^[Confidence: HIGH, Rationale: The mathematical formulation and conceptual integration of multiple uncertainty sources are clearly specified in the KB source material with explicit equation references and logical development.]

## SLOT 2: State of Current Practice for Performance-Based Seismic Slope Design

### Standards and Guidelines

The current practice for performance-based seismic design of slopes is governed by a combination of design codes, professional guidelines, and technical recommendations established by organizations including the American Society of Civil Engineers (ASCE), the Federal Emergency Management Agency (FEMA), and state transportation departments. [WEB:https://www.atcouncil.org/pdfs/FEMA445.pdf][WEB:https://dot.ca.gov/-/media/dot-media/programs/engineering/documents/geotechnical-services/202305-gm-seismicdesigners-a11y.pdf] The pseudo-static method remains widely used in engineering design practice due to its simplicity and ease of application, despite the development of numerous more sophisticated analysis methods in recent decades. [WEB:https://www.sciencedirect.com/science/article/pii/S167423701830098X] ^[Confidence: HIGH, Rationale: Multiple authoritative sources from FEMA, state DOT guidance, and peer-reviewed literature confirm the continued use of pseudo-static approaches and the existence of formal standards and guidelines.]

### Pseudo-Static Analysis Framework

In the conventional pseudo-static method, the selection of an appropriate seismic coefficient is recognized as the most critical and difficult aspect of the analysis. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] The seismic coefficient values should depend on a measure of the amplitude of the inertial force induced in the slope by dynamic earthquake-generated forces, and are commonly expressed as a fraction of peak ground acceleration (PGA) at the site. [WEB:https://ascelibrary.org/doi/10.1061/%28ASCE%29GT.1943-5606.0000012] Traditional practice often recommends a seismic coefficient equal to no more than 50 percent of the free-field PGA, with smaller values of 25 percent or less appropriate for slopes exhibiting ductile behavior and capable of accommodating 1 to 2 inches of permanent seismic displacement. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] ^[Confidence: MEDIUM, Rationale: Web sources provide consistent information on pseudo-static coefficient ranges and traditional practice, though the specific percentages are cited from general engineering guidance rather than current code standards; these represent accepted practice but may vary by jurisdiction.]

### Performance-Based Design Approaches

Two recent performance-based approaches for establishing the seismic coefficient in pseudo-static analyses have been developed to address limitations of fixed-coefficient methods. [WEB:https://ascelibrary.org/doi/10.1061/9780784480458.039] In these approaches, the seismic coefficient depends upon both the acceptable permanent seismic displacement and factors representing the earthquake ground motions and slope response characteristics. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] This framework represents a shift from arbitrary or rule-based coefficient selection toward a rational methodology in which the engineer explicitly incorporates site-specific seismic hazard and project-specific performance criteria. [WEB:https://dot.ca.gov/-/media/dot-media/programs/engineering/documents/geotechnical-services/202305-gm-seismicdesigners-a11y.pdf] ^[Confidence: MEDIUM, Rationale: Multiple sources confirm the development of performance-based approaches and their underlying logic, though detailed specifications of which standards formally mandate these approaches are not fully captured in the search results.]

### Displacement Acceptance Criteria and Service Levels

Current practice establishes displacement acceptance criteria based on project-specific consequences and performance objectives. [WEB:https://dot.ca.gov/-/media/dot-media/programs/engineering/documents/geotechnical-services/202305-gm-seismicdesigners-a11y.pdf] For earth retaining structures, permanent seismic displacements exceeding 5 inches are generally considered unacceptable in proximity to utilities or where strict geometric constraints exist, while greater displacements may be tolerable in remote embankment sections. [WEB:https://dot.ca.gov/-/media/dot-media/programs/engineering/documents/structure-technical-policy/section-11/202008-stp1129seismicdesingofearthretainingsystems-a11y.pdf] Service level assessments consider annual exceedance probabilities ranging from 1/100 to 1/10,000 years, corresponding to different intensity levels and project risk tolerances. [KB:pbkmax.qmd] ^[Confidence: HIGH, Rationale: Displacement thresholds and service level ranges are corroborated by both web sources (state DOT guidance) and KB documentation on performance-based design frameworks.]

### Newmark Sliding-Block Method in Contemporary Practice

The Newmark sliding-block method, developed in 1965, represents an improvement over traditional pseudo-static approaches by accounting for permanent deformations that accumulate whenever the factor of safety falls below unity. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] Rather than treating only the limiting condition when factor of safety equals 1.0, the method recognizes that "failure" does not necessarily occur when the factor of safety becomes less than 1 for short time intervals; instead, permanent displacements accumulate during these periods. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] The method simplifies the sliding mass as a rigid or flexible block on an inclined plane and computes permanent displacements by integrating twice the difference between applied acceleration and critical acceleration over time. [WEB:https://structville.com/seismic-slope-stability-newmark-sliding-block-analysis] ^[Confidence: HIGH, Rationale: Multiple independent sources provide consistent description of the Newmark method, its historical development, and its fundamental principles, confirming its status as a standard tool in contemporary geotechnical practice.]

The Newmark method remains widely used in engineering practice due to its advantages in ease of application and practical rationality. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] Key aspects of the procedure include accurate evaluation of the critical acceleration (which generates pseudo-static inertia forces that bring the soil-structure system to limiting equilibrium) and proper definition of the failure mechanism. [WEB:https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=3507&context=icrageesd] ^[Confidence: HIGH, Rationale: Implementation requirements and practical considerations are documented in multiple technical sources that discuss design procedures and engineering practice standards.]

## SLOT 3: Newmark Displacement Analysis Methodologies

Seismic-induced permanent displacements of slopes are quantified using the Newmark sliding-block approach, which conceptualizes the sliding mass as a rigid or flexible block possessing a critical yield acceleration $k_y$. [KB:newmark.qmd] When ground acceleration exceeds $k_y$, the mass experiences incremental downslope movement, with total displacement $D$ accumulating over the course of earthquake shaking. [KB:newmark.qmd] The response is characterized probabilistically using empirical or semi-empirical relationships that link $\ln D$ to ground-motion parameters and slope properties, formulated in the general expression $\ln D = \mu_{\ln D}(\mathrm{IM}, k_y, T_n, M_w) + \epsilon\,\sigma_{\ln D}$, where $\mathrm{IM}$ denotes ground-motion intensity measures specific to each model, $T_n$ is the fundamental period of the sliding mass, $M_w$ is earthquake moment magnitude where included, $\mu_{\ln D}$ is the model-predicted mean, $\sigma_{\ln D}$ is the standard deviation in natural-log space, and $\epsilon$ is a standard normal variate accounting for record-to-record variability. [KB:newmark.qmd] ^[Confidence: HIGH, Rationale: The general model formulation and key parameters are clearly defined in the KB source with explicit mathematical expression and definitions of all variables.]

### Intensity Measures and Parameter Definition

Ground-motion intensity measures required by displacement models are obtained from site hazard results derived from general ground-motion prediction equations (GMPEs) or site-specific response analysis. [KB:newmark.qmd] Spectral accelerations are evaluated at periods required by each model, typically at $S_a(\alpha T_n)$ with $\alpha$ ranging from 1.3 to 1.5, with logarithmic interpolation applied to obtain spectral ordinates at non-tabulated periods. [KB:newmark.qmd] The yield acceleration $k_y$ is established through geotechnical analysis and expressed as a fraction of gravity, while selection of $M_w$ is determined by the seismic scenario or logic-tree branch. [KB:newmark.qmd] ^[Confidence: HIGH, Rationale: Specification of intensity measures, period scaling, and parameter definitions are systematically documented in the KB source material.]

### Classification of Block Models

The displacement models employed fall into two primary categories: rigid-block and flexible-block idealizations. Rigid-block models employ simplified yield acceleration concepts and are suitable for structures with low deformability. Flexible-block models incorporate dependencies on spectral acceleration $S_a$, period, and magnitude $M_w$, permitting more detailed representation of compliant systems. [KB:newmark.qmd] Specific functional forms for $\mu_{\ln D}$ and, where applicable, for variable $\sigma_{\ln D}$, are implemented as described in the models detailed in the appendix. [KB:newmark.qmd] Flexible-block and duration-sensitive formulations developed by Bray & Travasarou and by Bray & Macedo include explicit dependencies on spectral ordinates, period, and moment magnitude, while models by Jibson and by Saygili & Rathje introduce Arias Intensity and peak ground velocity to capture duration and velocity effects. [KB:newmark.qmd] In all cases, the models are cast in lognormal space to permit probabilistic simulation. [KB:newmark.qmd] ^[Confidence: HIGH, Rationale: Classification of model types and identification of which models incorporate specific parameters are clearly stated in the KB documentation with references to original sources.]

### Uncertainty Characterization

The uncertainty in input ground-motion parameters is represented by empirical quantile distributions obtained from the probabilistic seismic hazard analysis (PSHA) or site-specific response calculations. [KB:newmark.qmd] For each oscillator period or amplitude measure required by the displacement models, fractiles at 2%, 5%, 16%, 50%, 84%, 95%, and 98% quantiles, along with the mean, are available from hazard computation, reflecting both epistemic and aleatory uncertainty from source, path, and site effects. [KB:newmark.qmd] For each realization in the displacement simulation, the required intensity measure is sampled from its empirical quantile function through construction of a monotonic, piecewise function $Q_{\mathrm{IM}}(p)$, where $p$ is a uniform random variable in $(0,1)$. [KB:newmark.qmd] For spectral ordinates not explicitly available in the hazard output, logarithmic interpolation in period is used to obtain the required value, and where site hazard derives from reference-rock conditions at $v_\mathrm{ref} = 760\,\mathrm{m/s}$, period-dependent amplification factors are applied with amplification model uncertainty propagated as a lognormal variable. [KB:newmark.qmd] ^[Confidence: HIGH, Rationale: Uncertainty characterization and sampling methodology are explicitly documented in the KB source with precise specifications for quantile distributions and interpolation procedures.]

Each displacement model provides a log-standard deviation $\sigma_{\ln D}$, determined from regression residuals of observed or simulated events. [KB:newmark.qmd] For all models, $\sigma_{\ln D}$ is treated as a constant for all scenarios. [KB:newmark.qmd] For each realization, a standard normal deviate $\epsilon$ is drawn, and the predicted displacement is computed as $\ln D = \mu_{\ln D} + \epsilon\,\sigma_{\ln D}$ using the input parameters from the sampled scenario. [KB:newmark.qmd] Model-to-model epistemic uncertainty is retained by assigning logic-tree weights before aggregating results over all models. [KB:newmark.qmd] ^[Confidence: HIGH, Rationale: Treatment of model standard deviations and aggregation procedures are precisely specified in the KB source material with mathematical notation.]

## SLOT 4: Appendix - Newmark Displacement Equations by Method

The principal displacement models currently recognized in technical literature are presented in the following sections, with explicit definitions of parameters, functional forms, and associated uncertainties for engineering application. [KB:newmark_model.qmd] The general notation applicable to all models is as follows: $D$ denotes permanent displacement in centimeters; $k_y$ denotes the yield-acceleration ratio $= a_y / g$; $PGA$ denotes peak ground acceleration in units of $g$; $PGV$ denotes peak ground velocity in cm/s; $T_n$ denotes the fundamental period of the sliding mass in seconds, with $S_a$ evaluated at model-specific periods; all dispersions $\sigma$ are one-standard-deviation values in natural-log space unless explicitly stated otherwise. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Notation and definitions are systematically presented in the KB source as foundational material for all subsequent model presentations.]

### Bray & Macedo (2017) – Subduction Earthquakes

Flexible-Block (compliant) Model. The predictive equation is:

$$\mu_{\ln D}=a_0+a_1\ln S_a+a_2(\ln S_a)^2$$

with coefficients:

$$\begin{aligned}
a_0 &=
\begin{cases}
-5.864+0.550\,M_w-9.421\,T_n-3.353\ln k_y-0.390(\ln k_y)^2, & T_n<0.1\\
-6.896+0.550\,M_w+3.081\,T_n-0.803\,T_n^{2}-3.353\ln k_y-0.390(\ln k_y)^2, & T_n\ge 0.1
\end{cases}\\
a_1 &= 3.060+0.538\ln k_y,\qquad
a_2 = -0.225
\end{aligned}$$

$$\sigma_{\ln D}=0.73$$

where $S_a$ is the spectral acceleration at the fundamental period $T_n$ in units of $g$, $T_n$ is in seconds, and $M_w$ is the moment magnitude. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equations and coefficients are directly transcribed from the KB source with explicit statement of parameter definitions and applicable range.]

### Bray & Macedo (2019) – Shallow-Crustal Earthquakes

Flexible-Block (compliant) Model with the same functional form as the 2017 model but distinct coefficients accounting for shallow-crustal earthquake characteristics and peak ground velocity effects:

$$\begin{aligned}
a_0 &=
\begin{cases}
-4.551+0.607\,M_w-9.690\,T_n-2.491\ln k_y-0.245(\ln k_y)^2,&T_n<0.1\\
-5.894+0.607\,M_w+3.152\,T_n-0.910\,T_n^{2}-2.491\ln k_y-0.245(\ln k_y)^2,&T_n\ge0.1
\end{cases}\\
&\quad+\;
\begin{cases}
0,&PGV\le115\;\text{cm/s}\\
\ln PGV-4.75,&PGV>115\;\text{cm/s}
\end{cases}\\
a_1 &= 2.703+0.344\ln k_y,\qquad a_2=-0.089
\end{aligned}$$

$$\sigma_{\ln D}=0.74$$

The model requires peak ground velocity ($PGV$), which if not supplied is estimated from $PGA$; $S_a$ is evaluated at $1.3\,T_n$. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equations, coefficients, and parameter specifications are directly provided by the KB source with additional notation of the PGV-dependent term and period scaling factor.]

### Bray & Travasarou (2007) – Flexible-Block Model

$$\mu_{\ln D} = -1.10 - 2.83\ln k_y - 0.333(\ln k_y)^2
            + 0.566\ln k_y\ln S_a + 3.04\ln S_a - 0.244(\ln S_a)^2
            + 0.278(M_w-7)$$

$$\sigma_{\ln D}=0.66$$

where $S_a$ is the spectral acceleration at $1.5\,T_n$ in units of $g$. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equation form and dispersion are directly cited from the KB source with specification of the period scaling factor.]

### Jibson (2007) – Rigid-Block Model

$$\mu_{\ln D}= \left[\,0.561\log_{10}AI - 3.833\log_{10}(k_y/PGA)-1.474\right]\;\ln10$$

$$\sigma_{\log_{10}D}=0.616\;\;(\sigma_{\ln D}=0.616\ln10)$$

where $AI$ denotes Arias intensity in units of m/s, estimated from $PGA$ if not provided, and $r = k_y / PGA$ expresses slide strength relative to intensity. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equation form, dispersion transformation, and parameter definitions are directly specified in the KB source material.]

### Saygili & Rathje (2008) – Rigid-Block Multi-Parameter Model

$$\mu_{\ln D}=2.39-5.24r-18.78r^{2}+42.01r^{3}-29.15r^{4}
            -1.56\ln PGA +1.38\ln AI,\qquad r=\tfrac{k_y}{PGA}$$

$$\sigma_{\ln D}=0.46+0.56\,r$$

The model dispersion increases as the slope becomes weaker (as $r$ approaches zero). [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equations and parameter definitions are provided by the KB source with explicit note regarding the physical interpretation of the dispersion dependence.]

### Ambraseys & Menu (1988) – Rigid-Block Model

$$\mu_{\log_{10}D}=0.90+\log_{10} \left[(1-r)^{2.53}\,r^{-1.09}\right],\qquad r=\tfrac{k_y}{PGA}$$

$$\sigma_{\log_{10}D}=0.30\;\;(\sigma_{\ln D}=0.30\ln10)$$

This model employs base-10 logarithmic form with transformation to natural-log space dispersion for integration with other models. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equation and dispersion conversion are directly cited from the KB source.]

### Yegian et al. (1991) – Rigid-Block Model

$$\mu_{\log_{10}D}=0.22-10.12\,r+16.38\,r^{2}-11.48\,r^{3},\qquad r=\tfrac{k_y}{PGA}$$

$$\sigma_{\log_{10}D}=0.45\;\;(\sigma_{\ln D}=0.45\ln10)$$

This model also employs base-10 logarithmic space with transformation to natural-log space for ensemble integration. [KB:newmark_model.qmd] ^[Confidence: HIGH, Rationale: Equation and notation are directly provided by the KB source.]

## SLOT 5: Ensemble Numerical Model

### Weighted Ensemble Methodology

The numerical model employed in this work is constructed as a weighted ensemble (weighted sum) of the individual Newmark displacement models detailed in the preceding appendix. [KB:newmark_model.qmd] The weighting scheme assigns greater weight to more recent models that were calibrated using larger ground-motion datasets, reflecting advances in data availability and model calibration quality over time. [KB:newmark_model.qmd] ^[Confidence: MEDIUM, Rationale: The weighting rationale is specified in the task file constraints, though the actual weighting coefficients assigned to specific models are not provided in the KB material and would be project-specific.]

### Incorporation of Uncertainty

The ensemble approach retains model-to-model epistemic uncertainty through explicit assignment of logic-tree weights prior to aggregation of results over all models. [KB:uncertainty_model.qmd] The total distribution of predicted displacements is obtained by convolving the empirical variability in input ground-motion parameters with the conditional lognormal scatter from the site response models and Newmark displacement models. [KB:uncertainty_model.qmd] The simulation proceeds by drawing, for each scenario and model, a realization of the intensity measures from their empirical quantile functions, computing the deterministic mean displacement $\mu_{\ln D}$ from the model's regression, and applying the model's standard deviation $\sigma_{\ln D}$. [KB:uncertainty_model.qmd] This process is repeated for each model and each realization, with model weights applied as appropriate. [KB:uncertainty_model.qmd] Quantiles of interest (e.g., median, 84th percentile, and 95th percentile displacements) are computed directly from the assembled ensemble. [KB:uncertainty_model.qmd] ^[Confidence: HIGH, Rationale: The simulation framework, uncertainty propagation methodology, and ensemble quantile computation are explicitly documented in the KB source material on the uncertainty framework.]

### Site Response Integration

Where site hazard is derived from reference-rock conditions at $v_\mathrm{ref} = 760\,\mathrm{m/s}$, period-dependent amplification factors are applied in accordance with the ergodic site amplification framework developed for probabilistic seismic hazard analysis in Central and Eastern North America. [KB:site_model.qmd][KB:uncertainty_model.qmd] The site amplification model decomposes into three multiplicative components: the reference condition adjustment $F_{760}(T_n)$ bridging the difference between 760 m/s and hard-rock reference conditions; the velocity scaling term $F_{V}(V_{S30}, T_n)$ quantifying site stiffness relative to 760 m/s; and the nonlinear amplification term $F_{nl}(V_{S30}, pga^*, T_n)$ reflecting strain-dependent de-amplification. [KB:site_model.qmd] Amplification model uncertainty is propagated as a lognormal variable through joint Monte-Carlo simulation, where for each realization both the reference-rock spectral ordinates and independent amplification factors are sampled and combined to produce site-amplified spectral ordinates reflecting the full uncertainty budget. [KB:uncertainty_model.qmd] ^[Confidence: HIGH, Rationale: The site response model structure, component definitions, and uncertainty propagation methodology are comprehensively documented in both the site model and uncertainty framework KB sources.]

### Service-Level Reporting

Performance-based seismic coefficients are reported across service levels with annual exceedance probabilities (AEP) ranging from 1/100 to 1/10,000 for different geometry and material scenarios representative of tailings storage facilities and waste rock dumps. [KB:pbkmax.qmd] For each scenario and service level, the seismic coefficient $k_{\max}$ represents the performance-based design value established through the statistical framework linking acceptable displacement thresholds to the predicted displacement distribution. [KB:pbkmax.qmd] The ensemble displacement results support determination of $k_{\max}$ at each service level by providing the required quantile estimates of permanent displacement as a function of yield acceleration. [KB:pbkmax.qmd] ^[Confidence: HIGH, Rationale: Service level definitions, annual exceedance probability ranges, and application to performance-based coefficient determination are clearly stated in the KB documentation.]

