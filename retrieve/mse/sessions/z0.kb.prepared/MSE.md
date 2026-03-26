## Review of MSE Wall Seismic Design Criteria

### Introduction

The Kitimat LNG project is located in Bish Cove, near Kitimat, British Columbia, adjacent to a local community industrial zone and the drainage system that provides natural gas from the Western Canadian Sedimentary Basin. The project site is at elevation E.L. +26.00 and requires construction of a Mechanically Stabilized Earth (MSE) wall approximately 18.0m in height.

SRK Consulting was contracted to perform the seismic analysis and verification of the MSE wall and the Deep Soil Mixing (DSM) columns. This memo has the following objectives:

1. Review and identify information relevant to the analysis and seismic design of the MSE wall and the DSM columns.
2. Identify current seismic design practice for retaining structures in general and the specific considerations required for MSE walls.
3. Revise the available methodologies to determine the horizontal seismic coefficient to be considered in the internal and external stability verifications.

This preliminary report is limited to the revision of the following reference documents:

- Seismic Design Criteria (KNG-0000-STR-BOD-CHV-0000-00001-00H)(24/10/2013)
- MSE Walls Design Criteria (KNG-0000-GEO-BOD-CHV-0000-00001-00H)(24/10/2013)
- Deep Mixing Ground Improvement for R1 and R2 MSE Walls (Golder - 22/05/2013)

Additionally, complementary references have been included regarding the state of practice in the analysis and seismic design of retention structures, including numerous investigation works, reports and standards that are listed in the references of this document.

## MSE Wall Seismic Design Criteria

### Seismic Design Criteria

This document states the general design criteria for structures and systems involved in the Kitimat LNG project. The document prescribes the application of codes, regulations and other relevant reference documents for seismic design and establishes minimum requirements without precedence over local and national codes and regulations. MSE walls, slopes, embankments and DSM columns are identified and classified as Seismic Category I [@CSA2011] for which seismic design based on two serviceability levels (OBE and SSE) is required according to performance-based seismic design [@Kramer2011][@Fardis2007].

The Operating Basis Earthquake (OBE) is a seismic event with an exceedance probability of 10% in a 50-year period (return period of 475 years). For this condition all structures, components and systems must be operational before and after the OBE event. With regards to MSE walls and DSM columns, no permanent lateral displacements or settlements are permitted. The maximum service level is defined by a Safe Shutdown Earthquake (SSE) event which has an exceedance probability of 2% in a 50-year period (return period of 2,475 years). Moderate permanent deformations are permitted as long as they do not affect the performance of other structures, components or Category I or II systems. Values of maximum permanent displacements are detailed in the document [@KitimatMSE2013]. Finally, a third serviceability level is established exclusively for secondary retaining structures in LNG storage tanks. Their performance objective is to tolerate, with maximum operational volume, an Aftershock Level Earthquake (ALE) replica with the same exceedance probability of SSE events and half of the seismic demand.

In Chapter 5, minimum values of the design spectra and response required for the analysis methodology based on forces (pseudo-static methods) are established. The seismic demand, in terms of pseudo-accelerations and periods of an equivalent SDOF system, are established for hard soil (A) and for each service level as the envelope of the design spectra analysis of the seismic hazard of the 2011 site review [@StantecKitimat2011], that follow the NBCC standard procedure and the 2013 analysis revision. Additionally, the required correction factors are defined for each service level, by soil type and level of dampening. At this stage, the conversion factors to obtain the vertical response spectra for the seismic design of the tanks are established and, additionally, the values of dampening to be considered in the analysis models (linear).

In Chapter 6, the design criteria in terms of permanent deformations and displacements for limit service states are defined. At the SSE level, limits and conditions for the geomechanic parameters and requirements for cohesive soil constitutive models (strain-softening) are established. For the specific case of MSE walls, a maximum permanent horizontal displacement of 300mm is established for the wall crest. Additional design criteria are incorporated from the client's documentation, specifically in the particular design considerations of MSE walls and embankments [@KitimatMSE2013].

The document's design directives reflect state-of-the-art practice for the design of retaining structures and MSE walls, and allow for the development of all of the seismic design stages based on pseudo-static methodologies. Nevertheless, there is no criterion or directives related to the selection and scaling of design earthquakes for non-linear dynamic analyses. The seismic hazard analysis for the site location defines the OBE and SSE events with exceedance probabilities of 10% and 2%, respectively, and with an exposure period of 50 years resulting in return periods of 475 and 2,500 years in accordance with the BCBC [@BCBC2012]. Nevertheless, the seismic design criteria from 2011 [@KitimatSeismic2013] defines a 75 years design life for MSE walls and DSM fills. To maintain the same probability of exceedance as category II and III structures, whose design life are 50 years, MSE walls and DSM fills should be considered with a corrected seismic demand, equivalent to return periods of 700 and 3,700 years for OBE and SSE events respectively.

### MSE Walls Design Criteria

This document establishes the performance objectives for MSE walls according to serviceability and strength limit states.

The serviceability limit state establishes the maximum allowable permanent displacements for the crest and required static and dynamic safety factors. The performance objectives define the maximum horizontal permanent displacement for the crest for OBE and SSE events as 150mm and 300mm, respectively. In the same directive, it is specified that displacements values obtained from any analysis must be compared to the values proposed by the reference [@Bray2007]. The directive states values of 1.3 and 1.5 as minimum static safety factors for short and long-term conditions, respectively. In a seismic case, the minimum required safety factor for a limit pseudo-static equilibrium state is 1.1. The strength limit states are defined in terms of internal and external stability and are referred to by the AASHTO limit equilibrium method [@AASHTO2012]. The directives establish that, for external stability verifications, in zones where MSE walls interact with DSM columns, the relative friction coefficient should be adopted based on known values from literature or usual practice when no information is available from site tests.

Due to the limitations of the Bray model, which was formulated for embankments of general incoherent materials and not for MSE walls, the obtained values with this methodology should be used only as minimum reference values for the validation of results obtained by numerical methods and never should be considered as final estimations. For operative scenarios (OBE) it is expected that permanent displacements greater than 30% of the defined values for serviceability limit states will not be obtained. This estimation arises from the consideration of realistic values of the actual amplification and effective flow acceleration that might be expected on the DSM fill.

### Deep Mixing Method of Ground Improvement Design Criteria

This document establishes the particular design criteria for the DSM fill that will be constructed in the zone where walls R1 and R2 will be placed. In the first section the performance conditions to be verified during the seismic intensity levels are established as defined by document [@KitimatSeismic2013] and as summarized previously. The maximum permanent (plastic) deformations measured on the superior point of the DSM column are defined for OBE and SSE events, respectively. These seismic performance criteria must be verified with non-linear 2D dynamic analyses for the section with the largest expected displacement (the section with the least flow acceleration and/or the largest mean peak acceleration).

Chapter 6 defines directives related to non-linear dynamic models. It specifies that dynamic analyses must be performed with uncertainty incorporated into the determination of the mechanical parameters of the soil layers including the lower, upper and average values for each parameter. This dynamic analysis must be compared to a 1D conventional wave propagation analysis (Site Response Analysis, SRA) to ensure the correct implementation of finite element models, specifically of the mesh boundary conditions and the layers damping. It is prescribed that at least three different seismic histories should be analyzed for each scenario considered. Additionally, for SSE events, all the necessary pseudo-static analyses should be performed to evaluate the stability factor of safety considering a possible reduction of soil's strength due to liquefaction effects. In this manner, the soil's mechanical parameters should be chosen taking into account the layers' factors of safety for liquefaction [@Cetin2004][@Moss2006]. In models based on pseudo-static methods, the horizontal seismic coefficient ($k_{h0}$) must be calculated with a site response analysis (SRA) as the mean acceleration just above the displacement plane utilizing at least seven seismic records provided by the client. If the liquefaction potential of soils during seismic events is proven, the liquefaction analyses must also be performed during the non-linear 2D dynamic analyses.

## Pseudo-Static Analysis

### Performance Objectives and Limit States

The project design criteria establish a series of verifications to be performed on the final design of MSE walls, for two seismic performance criterion established according to the standards CSA Z276 [@CSA2011] and BCBC [@BCBC2012]. The seismic performance criteria are defined based on two limit states: serviceability limit state and Strength Limit State.

Serviceability limit states establish performance criteria through maximum values for acceptable damages, in terms of permanent displacements and settlements of walls and fills. According to MSE wall design criteria [@KitimatMSE2013][@KitimatDSM2013], maximum values of 150mm and 300mm are prescribed for the permanent horizontal crown displacement for OBE and SSE events and for DSM fill 40mm and 75mm is prescribed for the maximum permanent settlement. Values of plastic deformations and permanent settlements should be calculated with non-linear dynamic analyses (time-history) that are capable of reasonably predicting instantaneous and accumulated plastic deformations for an acceleration history from a properly selected and scaled seismic record. The values obtained from these methodologies should be validated with analytical models for the estimation of permanent displacements such as Bray [@Bray2007] or others. The most important design considerations for these limit states are related to the selection of the seismic records which control the displacement demand on MSE walls.

The strength limit states establish performance criteria based on minimum safety factors in the stability analyses. The internal and external stability of MSE walls is evaluated with limit equilibrium pseudo-static methods such as Mononobe-Okabe and following the AASHTO recommendations [@AASHTO2012].

### Strength Limit States

In general, the methodology used to obtain a horizontal seismic coefficient for an arbitrary problem of embankments or slopes is based on Newmark's sliding block analysis of a MSE wall where the final maximum permanent accumulated displacements at the end of a seismic event are correlated to the maximum registered acceleration on the failure plane. This requires the knowledge of the spatial instantaneous acceleration distribution within the soil mass and the determination of the potential failure plane for an active wedge. The Newmark's sliding block concept was introduced for the design of retaining walls during the 1980's in the work of Richards and Elms [@Richards1979] where it was established that in a Mononobe-Okabe analysis, an horizontal seismic force coefficient of $k_h \approx 0.5$ was adequate for a pseudo-static limit equilibrium design that supports a horizontal wall displacement equal to $D_a = 10(\text{PGA}/g)$ (inches) where $D_a$ is the displacement of the wall in inches and PGA is the peak ground acceleration at the base of the sliding block.

The state-of-the-practice of retaining wall seismic design suggests that for short walls ($h < 6$m) the concept of an active wedge considered as a rigid block is reasonable. Nevertheless, for walls higher than 6m, accelerations will not be uniform and the rigid block concept does not apply for the analysis. The AASHTO standard [@AASHTO2012] and the NCHRP recommendations [@NCHRP2008] suggest that for walls with heights between 6m and 18m, reduced seismic coefficients should be used, depending on the wall's height. Different expressions for this coefficient have been proposed. The project design directives [@KitimatSeismic2013][@KitimatMSE2013] prescribe that displacements obtained with numerical methods must be validated against formulas detailed in [@Bray2007]. For walls with heights greater than 18m, standards recommend that soil-structure dynamic interaction (SSI) analysis methods should be performed considering the distribution of acceleration over the height of the wall, coupled with the deformation of the internal failure wedge.

### Seismic Coefficient Estimation

The following paragraphs detail the formulas that can be utilized to estimate the horizontal seismic coefficient in a MSE wall. Reference values are calculated for an 18m high example MSE wall founded on a "C" soil type (according to the NBCC standard) with a material for the stabilized fill with $V_s = 280$ m/s (shear wave velocity), with an allowable maximum displacement of 150mm and 300mm for OBE and SSE events respectively.

**Kavazanjian - FHWA, AASHTO**

$$k_h = 1.66 \left( \frac{a_h}{D} \right)^{0.25} (k_{h0} - 0.396 k_{h0}^{1.45})$$

**Anderson - NCHRP, AASHTO**

$$k_h = \frac{1}{2} \left[ F_v S_1 + k_{h0} \left(1 - \frac{k_y}{k_{h0}}\right)\right]$$

**Bray - AASHTO**

$$k_h = \exp[0.66 - a + b]$$

In the previous formulas, $k_{h0} = \kappa \text{PGA}/g$ is the maximum acceleration coefficient at the base of the wall, $\kappa$ is a factor that depends on the soil type (equal to 1 for firm soil), $S_a(T_s=1)$ is the spectral pseudo-acceleration at the base of the sliding wall (adjusted by the soil type), for $T=1$s, and $S_a(T=1.5T_s)$ is the spectral pseudo-acceleration for $T=1.5T_s$ where $T_s = 4H/V_s$ is the natural period of the reinforced fill and the parameters $a$ and $b$ are defined by the following expressions:

$$a = 2.83 - 0.566 \ln[S_{a,1.5}]$$

$$b = 1.33 \ln(D_a) - 1.10 + 3.04\ln(S_{a,1.5}) - 0.244(\ln[S_{a,1.5}])^2 + (0.278)(M_w - 7)$$

Where, for Anderson's formula, the value of $k_y = k_y(D_a, k_{h0}, \text{PGV})$ is numerically obtained as the root of the expression:

$$\ln(D_a) - 1.51 - 0.74\log\left(1 - \frac{k_y}{k_{h0}}\right) + 3.27\log(k_y) - 0.80\log\left(1 - \frac{k_y}{k_{h0}}\right)\log(\text{PGV}) + 1.59\log(k_y) = 0$$

Accepting the base maximum acceleration values equal to $k_{h0}(g) = 0.12$ (OBE) and $k_{h0}(g) = 0.20$ (SSE) for 700 and 3700 years respectively and "C" soil type, the values for the horizontal seismic coefficient lie between $k_h = 0.4 \cdot k_{h0} = 0.046g$ (OBE) and $k_h = 0.35 \cdot k_{h0} = 0.07g$ (SSE) and can be considered as design values in pseudo-static analyses.

The validity of the horizontal seismic coefficient requires that evaluations of the safety factor against pull-out and MSE wall reinforcement failure (Internal Stability) are sufficiently high to guarantee the rigid body behavior sliding on a horizontal failure plane during a seismic event. For that reason, AASHTO [@AASHTO2012] establishes that the seismic coefficient ($k_h$) utilized in the internal stability analysis of the wall should be consistent with the coefficient employed for the external stability analysis.

### Serviceability Limit States

The performance criteria based on serviceability limit states prescribe maximum permanent displacements which can only be determined with a non-linear dynamic analysis coupled with Finite Element Models (FEM). For each serviceability level (OBE and SSE) the seismic design criteria prescribe that a minimum of three seismic records (accelerograms) should be used.

The frequency content significantly affects the problem's inelastic response [@WatsonLamprey2006][@Bray2010][@Buratti2008] and specific intensity measures related to the intensity, duration and frequency content should be used in combination with PGA/Sa for scaling/selection records. The design directives indicate that the acceleration records to be utilized in future dynamic analyses will be provided by the client. The validity of FEM models for non-linear dynamic analysis will depend on the seismic record selection methodology. A procedure based on standard practice on record seismic selection has been proposed in a separate document (51-3006-R02-ENG-A.PDF).

## Conclusions

1. The seismic hazard analyses for the construction site defines exceedance probabilities for the OBE and SSE events equal to 10% and 2%, respectively, and, for an exposure time of 50 years, result in return periods of 475 and 2,500 years which are consistent with Canadian standards such as BCBC [@BCBC2012] and the CSA LNG-11 [@CSA2011]. Nevertheless, seismic design criteria [@KitimatSeismic2013] establish a 75 year design life for MSE walls and DSM fills. To maintain the exceedance probability required for OBE and SSE events, MSE walls and DSM fill will have to be considered with a corrected seismic demand (greater accelerations) equivalent to return periods of 700 and 3,700 years, respectively.

2. The estimated values for the horizontal seismic coefficient lie between 0.35 and 0.40 for OBE and SSE events, respectively, and can be considered as a (conservative) lower boundary for the definitive values to be used in pseudo-static analyses. In order to consider these simplified formulations as valid, it is necessary to use safety factors against pull-out and internal reinforcement failure that are large enough to guarantee that, during seismic events, the MSE wall behaves as a rigid block sliding on a horizontal plane and does not generate a non-planar failure surface.

3. The combination of the directives that establish the use of minimum, mean and maximum probable geotechnical parameters together with the consideration of seven seismic records for an SRA analysis on OBE and SSE events result in more than 40 cases of non-linear calculations. Using FEM models for this type of analysis is not feasible or compatible with the project's delivery schedule. This situation can be solved by selecting, with the client, a simplified numerical model that can reasonably capture the ground amplification.

4. The project's design directives prescribe the use of three seismic records for each service level and reference a specific document where guidelines are mentioned for the development of accelerograms (KNG-0000-GEO-SPC-CHV-0000-00003-00H Guideline for Ground Motion Development). Nevertheless, this document was not received to the delivery date of the present report.

5. The design directives indicate that the acceleration records to be considered in future dynamic analyses will be delivered by the client. Records delivered by the client should be selected according to adequate methodologies for soil-structure interaction problems, to guarantee the validity of the non-linear dynamic FEM analysis (Time History Analysis).

## Appendix A: Horizontal Seismic Coefficient

### Seismic Coefficient For an Embankment Over Rock ("B")

The calculation methodology of the horizontal seismic coefficient is associated to limit equilibrium pseudo-static verifications that apply to walls and embankments. In the particular case of embankments, the calculations are similar to the ones presented previously with slight modifications to each of the model parameters.

Calculation example: Incoherent material embankment (rockfill) of 40m in height, slopes of 2V:1H (63 degrees), material with a triaxial friction angle of 35 degrees and a shear wave velocity approximately equal to 280m/s. The natural period of the embankment can be estimated as $T_s = 2.6H/V \approx 0.167$s and the degraded period is estimated as $T = 1.5T_s = 0.251$s. Assuming a type "B" foundation soil from the seismic hazard analysis for the construction site, the PGA values for OBE and SSE events are calculated as 0.08g and 0.15g, respectively.

**AASHTO (Bray & Travasarou)**

According to Bray's methodology, the horizontal seismic force coefficient $k_h$ is determined from the expression:

$$k_h = \exp[0.66 - a + b]$$

Considering a type "B" (700-1500) foundation soil layer, the spectral pseudo-acceleration for the degraded period is equal to $S_a \approx 0.141g$ for an OBE event and equal to $S_a \approx 0.302g$ for an SSE event. Given the pseudo-acceleration, the "a" parameter is defined by:

$$a = 2.83 - 0.566\ln[S_a] = \begin{cases} 3.94 & \text{(OBE)} \\ 3.508 & \text{(SSE)} \end{cases}$$

The "b" parameter depends on various factors: 1) the design seismic record characteristic magnitude, that can be tentatively adopted as $M_w = 5.5$ and $M_w = 6.5$ for OBE and SSE events, respectively, and the allowable permanent displacements for the embankment, which are different to the values established in the serviceability limit states for MSE walls.

$$b = 1.33\ln(D_a) - 1.10 + 3.04\ln(S_a) - 0.244[\ln(S_a)]^2 + (0.278)(M_w - 7)$$

The values of the "b" parameter and the horizontal force coefficient will depend on the allowed values for the slope's permanent displacement after the seismic event. Without specific project design criteria, 150mm and 75mm (3") can be assumed as maximum allowable values for SSE and OBE events, respectively. In this case, the "b" parameters obtained are equal to 2.958 and 2.86, respectively, and the horizontal seismic force coefficient is:

$$k_h = \begin{cases} 0.414 \cdot k_{h0} = 0.033g & \text{(OBE)} \\ 0.444 \cdot k_{h0} = 0.067g & \text{(SSE)} \end{cases}$$

**FHWA, NCHRP, NBCC**

According to the FHWA recommendations, which are in agreement with the NBCC's recommendations, the value of the coefficient is estimated from the following relationship:

$$k_h = \frac{1}{2}\left[F_v S_1(T=1\text{s}) + k_{h0}\left(1 - \frac{k_{h0}}{2}\right)\right] = \begin{cases} 0.298 \cdot k_{h0} = 0.024g & \text{(OBE)} \\ 0.294 \cdot k_{h0} = 0.044g & \text{(SSE)} \end{cases}$$

Where $S_a(T=1\text{s}) = 0.05g$ and $S_a(T=1\text{s}) = 0.091g$ is the spectral pseudo-acceleration evaluated in $T=1$s, for foundation soil type "b" and OBE and SSE events.

The mean estimated values of the horizontal seismic coefficient are in the range of approximately 0.03g for OBE events and 0.07g for SSE events.
