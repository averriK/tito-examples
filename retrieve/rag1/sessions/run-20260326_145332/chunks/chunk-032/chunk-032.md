Not all liquefaction-related instabilities involve flow and very large displacements. At the element level, cyclic mobility in the presence of a static shear stress can cause significant permanent shear strain to accumulate (Figure 9.29), even if the shear stresses are lower than the shear strength of the soil. Integrating the incremental strains over the spatial extent of the liquefied zone in a soil profile produces incremental deformations that, by the end of an earthquake, may result in significant permanent ground deformation and extensive damage.

**Figure 9.77** Lateral spreading: (a) typical deformation patterns in laterally spreading river bank soils (after [@Rauch1997]; [@Varnes1978]), and (b) ground cracking and damage to Pleasant Point Yacht Club along the Avon River during the February 2011 Christchurch earthquake. (Photo courtesy of M. Cubrinovski.)

Lateral spreading is an example of such a deformation failure. As illustrated in Figure 9.77, lateral spreading beneath a crust of unsaturated or non-liquefiable soil often causes the crust to break into blocks that progressively move downslope or toward a free face during earthquake shaking. The ground surface may develop fissures and scarps at the head of the lateral spread, shear zones along its lateral margins, and compression zones at the toe. Substantial amounts of soil may be ejected from these fissures, leading to further settlement of the original ground surface. The surficial blocks usually move irregularly in both horizontal and vertical directions; buildings and pipelines extending through the head of a lateral spread may be pulled apart, pipelines crossing the lateral margins may be sheared, and bridges or pipelines near the toe may be buckled. Deep foundations that extend through the laterally spreading soil may suffer bending failure (Figure 9.68). Lateral displacements usually range from a few centimeters to a meter or two, but may be larger if shaking is particularly strong or of long duration. Void redistribution may result in additional deformations that are of hydraulic/gravitational rather than inertial origin.

Lateral spreading is a complex phenomenon, not only due to the complexity of the stress-strain behavior of the soils that produce it, but also due to spatial variability, complex three-dimensional topography, and pore pressure and void redistribution which are sensitive to site characteristics that are difficult to quantify. A number of procedures have been proposed for estimation of deformations due to lateral spreading. These procedures generally fall into one of three categories: purely empirical, semi-empirical strain potential, and numerical.

### Purely Empirical Procedures

Several investigators have used databases of lateral spreading case histories to develop predictive equations for lateral spreading displacement. [@BartlettYoud1992] compiled a large database of lateral spreading case histories from Japan and the western United States. They identified a set of material, geometric, and loading parameters that correlated to lateral spreading displacement. [@YoudEtAl2002] used an expanded and corrected version of the 1992 database to develop a relationship to predict lateral spreading displacement from those parameters. The Youd et al. (2002) [@YoudEtAl2002] model requires that a slope be classified as either a free-face case (flat slope near a steep bank) or a ground-slope case (gently sloping ground). The lateral spreading displacement (in meters) can then be predicted from

$$\log D_H = b_0 + b_1 M + b_2 \log R^* + b_3 R + b_4 \log W + b_5 \log S + b_6 \log T_{15} + b_7 \log(100 - F_{15}) + b_8 \log(D50_{15} + 0.1\text{ mm}) \tag{9.79}$$

where $M$ = moment magnitude, $R^* = R + 10^{0.89M}$, $R$ = closest horizontal distance to the energy source, $W$ = free-face ratio, $S$ = ground slope inclination, $T_{15}$ = cumulative thickness of soil layers with corrected SPT resistance $(N_1)_{60}$ less than or equal to 15 in which liquefaction is expected to occur (i.e., $FS_L \leq 1.0$), $F_{15}$ = the average fines content (in percent) of the soil layers that contribute to $T_{15}$, and $D50_{15}$ = mean grain size (in mm) of the soil layers that contribute to $T_{15}$. The values of $W$ and $S$ can be determined as indicated in Figure 9.78, and the values of the coefficients are presented in Table 9.13. Table 9.14 presents the recommended ranges of predictive variables for which the [@YoudEtAl2002] model is considered valid.

**Figure 9.78** Slope Geometry Notation. ([@YoudEtAl2002].)

**Table 9.13** Coefficients for Youd et al. (2002) [@YoudEtAl2002] Model

Case: Ground slope — $b_0$: −16.213, $b_1$: 1.532, $b_2$: −1.406, $b_3$: −0.012, $b_4$: 0.338, $b_5$: 0.540, $b_6$: −0.795, $b_7$: 3.413

Case: Free face — $b_0$: −16.713, $b_1$: 1.532, $b_2$: −1.406, $b_3$: −0.012, $b_4$: 0.592, $b_5$: 0.540, $b_6$: −0.795, $b_7$: 3.413

**Table 9.14** Recommended Range of Variable Values for the Youd et al. (2002) [@YoudEtAl2002] Predictive Equation

- $T_{15}$: Equivalent thickness of saturated cohesionless soils (clay content ≤ 15%) — 1–15 m
- $M$: Moment magnitude of the earthquake — 6.0–8.0
- $Z_T$: Depth to top of shallowest layer contributing to $T_{15}$ — 1–15 m
- $W$: Free face ratio — 1%–20%
- $S$: Ground slope — 0.1%–6%
- $F_{15}$, $D50_{15}$: See figure

[@YoudEtAl2002] implicitly assumes that sands with $(N_1)_{60} > 15$, although they can liquefy under sufficiently strong shaking, will be too dilative at the shallow depths at which lateral spreading generally occurs to contribute to lateral spreading displacement. It also implies, however, that lateral spreading displacement is insensitive to $(N_1)_{60}$ values below 15, which is inconsistent with behavior observed in laboratory tests. Youd et al. (2002) [@YoudEtAl2002] reported that the great majority of lateral spreading displacement values given by Equation (9.79) were within a factor of 2 of the displacements observed at the case history sites. The variability in the Youd et al. (2002) [@YoudEtAl2002] predictions has been characterized by a logarithmic standard deviation $\sigma_{\log D_H} = 0.197$, which is equivalent to $\sigma_{\ln D_H} = 0.464$ [@FrankeKramer2014].

While detailed information on fines content and mean grain size is often not reported in available case history data, descriptive information regarding the soils that comprise $T_{15}$ is generally available. [@GillinsBartlett2014] found that the $T_{15}$ layer descriptions from the Youd et al. (2002) [@YoudEtAl2002] database fell into the five general soil index (SI) groups described in Table 9.15. [@GillinsBartlett2014] then proposed that lateral spreading displacements could be predicted using the relative amounts of each SI group that constituted the $T_{15}$ layer:

$$\log D_H = b_0 + b_w \log W + b_1 M + b_2 \log R^* + b_3 R + b_4 \log S + b_5 \log T_{15} + 0.683 - 0.200\,x_1 - 0.252\,x_2 + 0.040\,x_3 - 0.535\,x_4 + \cdots \tag{9.80}$$

where $x_i$ is the fraction of $T_{15}$ that is comprised of soils classified in SI group $i$ and the common terms with Equation (9.79) are defined in the same way; the coefficients are as shown in Table 9.16. The coefficients on the $x_i$ terms in Equation (9.80) indicate the relative contributions of each group to lateral spreading displacement; SI 3 soils can be seen to produce higher displacements than the other groups.

**Table 9.15** Descriptions of Soil Index Groups Found in Youd et al. (2002) [@YoudEtAl2002] Database ([@GillinsBartlett2014])

- GM: Silty gravel with sand, silty gravel, fine gravel
- GM-SP, SP: Very coarse sand, sand and gravel, gravelly sand, coarse sand, sand with some gravel
- SP-SM: Sand, medium to fine sand, sand with some silt
- SM, SM-ML: Fine sand, sand with silt, very fine sand, silty sand, dirty sand, silty/clayey sand
- ML: Sandy silt, silt with sand

**Table 9.16** Coefficients for [@GillinsBartlett2014] Model

Case: Ground slope — $b_0$: −8.208, $b_1$: 1.318, $b_2$: −1.073, $b_3$: −0.016, $b_4$: 0.337, $b_5$: 0.592

Case: Free face — $b_0$: −8.208, $b_1$: 1.308, $b_2$: −1.073, $b_3$: −0.016, $b_4$: 0.445, $b_5$: 0.592

### Example 9.6

The gently sloping site shown below consists of a 2-m-thick layer of silty clay overlying a 4 m thick layer of loose, saturated silty sand. The sand has an average fines content of about 3% and an average $D_{50} = 0.22$ mm. Subsurface investigations indicate that the corrected SPT resistance of the silty sand is quite consistent with an average value of 11 blows/ft. Estimate the permanent displacement of the slope due to a M6.5 earthquake occurring at a (horizontal source-site) distance of 30 km.

**Solution:**

Using the Youd et al. (2002) [@YoudEtAl2002] approach (Equation 9.79), the relevant parameters are $M = 6.5$, $S = \tan(2°) = 0.035 = 3.5\%$, $T_{15} = 4$ m, $F_{15} = 3$, and $D50_{15} = 0.22$ mm. Then, using the ground slope model coefficients from Table 9.13,

$$\log D_H = -16.213 + 1.532(6.5) + (-1.406)\log(30) + (-0.012)(30) + 0.338\log(3.5) + 0.540\log(4) + 3.413\log(97) + (-0.795)\log(0.22) = -1.471$$

So $D_H = 10^{-1.471} = 0.034$ m $= 3.4$ cm.

### Semi-Empirical Strain Potential Procedures

Another approach to lateral spreading displacement estimation makes use of laboratory test data to characterize potential cyclic strain amplitude as a function of soil density and loading amplitude. The predicted cyclic strain is integrated over the thickness of a liquefiable layer to produce a displacement index that reflects the densities and thicknesses of the liquefied layers in a soil profile. That index is then used in a regression with site geometric parameters (e.g., ground slope) from field case histories of lateral spreading to produce a predictive relationship for lateral spreading displacement. This approach has an advantage over purely empirical procedures in that it also provides a stronger physical basis for estimating both surface displacements and subsurface displacement patterns.

[@ZhangEtAl2004] used the laboratory test-based relationship shown in Figure 9.79 to develop a cumulative shear strain model for prediction of lateral spreading displacement. The maximum cyclic shear strains in Figure 9.79 were defined by [@IshiharaYoshimine1992] as the maximum shear strain (in any direction) under transient loading conditions. Figure 9.79 shows how cyclic shear strain amplitudes increase quickly for soils in which liquefaction is triggered (particularly at low relative densities), and how sensitive the strain amplitude is to the relative density of the soil. [@ZhangEtAl2004] capped the maximum cyclic shear strains by the limiting shear strains proposed by [@Seed1979] and used empirical relationships between relative density and penetration resistance,

$$D_r = f\!\left[(N_1)_{60}\right] \quad \text{for } (N_1)_{60} \leq (N_1)_{60,cs} \tag{9.81a}$$

$$D_r = 76\log\!\left(q_{c1Ncs}\right) \quad \text{for } q_{c1Ncs} \leq q_{c1Ncs,\text{lim}} \tag{9.81b}$$

to allow computation of a lateral displacement index by integrating the expected maximum shear strain over the thickness of the liquefiable layer,

$$\text{LDI} = \int_0^{Z_{\max}} \gamma_{\max}\, dz \tag{9.82}$$

**Figure 9.79** Variation of maximum cyclic shear strain with factor of safety and relative density. (After [@ZhangEtAl2004] with permission of ASCE.)

where $Z_{\max}$ is the depth below which all liquefaction-susceptible soils have $FS_L > 2.0$ or 23 m (whichever is shallower). The LDI value, therefore, accounts for the distribution of material properties (i.e., soil penetration resistance) at a site and their liquefaction response to ground motions. It does not, however, account for the initial shear stresses that drive actual displacements at ground slope and free-face sites. By calibrating the geometric parameters of Youd et al. (Figure 9.78) against empirical case history data, the expected lateral spreading displacement can be related to LDI as [@ZhangEtAl2004]:

$$D_H = \begin{cases} \text{LDI} \cdot (S + 0.2) & \text{ground slope case} \\ \text{LDI} \cdot (W - 0.8) & \text{free-face case} \end{cases} \tag{9.83}$$

where $S$ and $W$ are defined as indicated in Figure 9.78 and subject to the respective limits $0.2\% < S < 3.5\%$ and $4 < W < 40$. Care must be taken when using CPT data to estimate LDI in spatially variable soil deposits. Liquefiable soil deposits often have significant spatial variability, both in their texture and their density. While the vertical variability of liquefiable soils is readily seen in CPT tip resistance profiles, the soils are also variable in the horizontal direction (although the variability is not as rapid). Therefore, thin layers of loose, liquefiable soil may have limited lateral extents and exist as lenses bounded above, below, and to the sides by non-liquefiable soils. While such thin layers may liquefy, they may contribute little to lateral spreading deformations due to their isolated nature. The indiscriminate summation of all loose layers, no matter how thin, can lead to overestimation of LDI with consequent overestimation of lateral spreading displacement.

### Example 9.7

The sand layer in Example 9.6 was explored with a CPT rig that produced the following data and triggering analysis results.

Depth / Mean $q_{c1Ncs}$ / Mean $I_c$ / $FS_L$ / Susceptible?:
- 2–3 m: 2.3, Yes, 0.85
- 3–4 m: 2.4, Yes, 0.78
- 4–5 m: 2.9, No, n.a.
- 5–6 m: 1.9, Yes, 0.95

Estimate the lateral spreading displacement of the site using a semi-empirical procedure.

**Solution:**

The maximum cyclic shear strain for each sublayer can be determined from $FS_L$ and the relative density of the soil using Figure 9.78. Relative density is estimated from mean $q_{c1Ncs}$ using Equation (9.81). Since Layer 3 is non-susceptible, its contribution to LDI is zero. In tabular form:

Depth / $q_{c1Ncs}$ / $D_r$ (%) / $FS_L$ / $\gamma_{\max}$ (%) / $\text{LDI}_i$ / $D_{H,i}$:
- 2–3 m: 78.1, 0.85, 4.6, 0.046, 0.17
- 3–4 m: 73.0, 0.78, 6.2, 0.062, 0.23
- 4–5 m: 65.3, ∞ (non-susceptible)
- 5–6 m: 80.4, 0.95, 3.8, 0.038, 0.14

Then the total predicted displacement is the sum of the layer displacements, 0.54 m, or 54 cm.

### Numerical Procedures

Advances in understanding of liquefiable soil behavior, constitutive modeling of that behavior, and numerical analyses have made it possible to capture many of the most important aspects of the development of permanent deformations of soil profiles, including lateral spreading, in nonlinear effective stress analyses. That process, however, is complicated and can be sensitive to site characteristics that can be difficult to identify in advance. The ability of even the best of these procedures to consistently make accurate a priori predictions of lateral spreading displacements has not been demonstrated. They have advanced, however, to the point where they can show that a well-designed and constructed dam or embankment is unlikely to deform much, or that a poorly designed or constructed one will deform excessively. They can also be very useful for understanding the mechanism(s) and patterns of the expected deformations.

Any numerical analysis must solve the wave equation that governs the mechanical response of the model in one, two, or three dimensions. It is also desirable that the analysis solve the diffusion equation that governs the hydraulic response (i.e., pore pressure redistribution and dissipation) in the same number of dimensions. When the constitutive model is formulated in a critical state framework, this allows modeling of void redistribution effects. The analysis must also accurately model the constitutive behavior of the liquefiable soil in a manner that captures the primary behavior(s) of interest, and it is usually this aspect that distinguishes one numerical analysis from another.

A constitutive model used to estimate lateral spreading deformations should be able to model the pore pressure buildup that occurs prior to and at the triggering of liquefaction, and also capture cyclic mobility phenomena such as phase transformation behavior and fabric degradation that can occur near and after triggering. A critical aspect of the reliable use of numerical models is calibration of the constitutive model. Calibrated constitutive models should be checked at the element level to ensure that they produce rates of pore pressure generation, stress-strain behavior and strain amplitudes that are consistent with those observed in laboratory tests of representative soils of different densities subjected to different levels of static and cyclic loading under different effective confining stresses. For prediction of lateral spreading, it is particularly important to be able to model the effects of initial static shear stresses on pore pressure generation and post-triggering response.

A limited cyclic test dataset (five tests on sands) indicated that the shear strain per post-triggering cycle decreased exponentially with increasing relative density [@TasiopoulouEtAl2020] as

$$\Delta\gamma_{\text{cyc}} = \exp(-3.332\, D_r + 0.1) + 0.5\,\varepsilon \tag{9.84}$$

where $D_r$ is in percent and $\varepsilon$ is a standard normal variable (zero mean and unit standard deviation). This relationship allows calibration of constitutive models to better predict cyclic and permanent deformations of liquefiable soils.

After implementing a calibrated constitutive model into a numerical analysis program, the program should be validated by application to selected case histories and/or physical model (e.g., centrifuge) test results. These types of analyses are typically performed by model developers — [@ZiotopolouBoulanger2013] describe a thorough and methodical process of calibration/validation of the PM4sand constitutive model implemented into FLAC, Plaxis, and OpenSees. Other models capable of representing important aspects of liquefiable soil behavior in two-dimensional analyses include the Stress-Density Model ([@CubrinovskyIshihara1998a]; [@CubrinovskyIshihara1998b]) implemented in DIANA and OpenSees, UBCSAND [@ByrneEtAl2004] implemented in FLAC, PDMY [@ElgamalEtAl2002] and OpenSees, and multi-spring and cocktail glass models [@IaiEtAl2011] implemented in FLIP.

Many liquefaction-susceptible soils are deposited in manners that lead to significant spatial variability that can influence deformations. The development of significant deformations requires shear straining within and across the zone of soil associated with a deformation mechanism and thus depends on the distribution of soil properties (e.g., penetration resistance) within that zone.

While vertical property variability can be readily measured at the specific locations of explorations such as borings and CPT soundings, lateral variability is much more difficult to characterize. The effects of both vertical and lateral variability can be assessed in two- and three-dimensional numerical analyses in which randomized, spatially correlated soil properties are assigned to individual elements (Section 5.8.1). Establishment of stable estimates of mean response (and aleatory variability when needed), however, requires multiple analyses with different random realizations of the properties. As a result, it is more common to represent the effects of spatial variability by using uniform representative soil properties that produce response consistent with the mean response of spatially variable analyses.

[@PopescuEtAl1997] found that analyses with uniform 20th percentile properties produced pore pressures consistent with Monte Carlo analyses based on full property distributions. [@PopescuEtAl2005] found that maximum lateral displacements based on uniform 50th percentile properties were similar to those from Monte Carlo analyses. More recent analyses of lateral spreading of gently sloping ground suggest that representative properties ranging from 30th to 70th percentile values with the higher values corresponding to thinner crusts, thinner liquefiable layers, flatter slopes, and stronger levels of shaking [@MontgomeryBoulanger2016], with 33rd percentile values being considered appropriate for deterministic analyses in practice. Application of numerical analyses with spatially randomized properties to case histories with liquefiable soils [@BassalBoulanger2021][@PaullEtAl2021][@PaullEtAl2022] provides additional insight into the effects of spatial variability.

### Discussion

Lateral spreading is an extremely complex phenomenon that can be sensitive to factors that are difficult to characterize in advance of an earthquake. Available empirical methods characterize loading, geometry, and material behavior with simplistic metrics, so it is not unexpected that factors not captured by those metrics should lead to significant uncertainty in predicted displacements. Recent case histories (e.g., [@RussellEtAl2017]) suggest that lateral spreading hazards are also influenced by liquefiable layer continuity (vertical and horizontal), geomorphology, and sediment age, none of which are captured by existing empirical predictive models. Numerical analyses offer the ability to represent many of these factors and evaluate their effects on deformations, and their increasing use in practice is likely to continue.

Lateral spreading can have a profound effect on the performance of structures underlain by liquefiable soils. The ground surface movements associated with lateral spreading tend to be highly irregular and place severe demands on foundations and the structures they support. Structures supported by shallow foundations, particularly isolated foundation elements not tied together structurally, tend to be heavily damaged by lateral spreading (Figure 9.77b). The performance of such structures can be improved by various ground modification techniques described in Chapter 11. Structures known at the time of foundation design to be underlain by liquefiable soils, however, are often supported on deep foundations that extend through the liquefiable soil and penetrate sufficiently into denser and stiffer underlying soils to provide the required load capacity. Lateral spreading, however, imposes high kinematic demands on pile foundations that can cause excessive foundation movements (Figures 1.13 and 1.14) and damage to the piles themselves (Figure 9.68). Procedures for assessing the response of pile foundations to lateral spreading are presented in Section 8.5.2.2.

## 9.6.6 Settlement

The tendency of sands to densify when subjected to earthquake shaking is well documented and was discussed in Section 6.6.5. Subsurface densification is manifested at the ground surface in the form of settlement but lateral spreading can also have vertical components of ground movement. Earthquake-induced settlement frequently causes distress to structures supported on shallow foundations, damage to lifelines that are commonly buried at shallow depths, and damage to utilities that serve pile-supported structures.

Unsaturated sands tend to densify very quickly so their settlement is usually complete by the end of earthquake shaking. The settlement of a saturated sand deposit, however, requires more time since settlement occurs as earthquake-induced pore pressures dissipate. The time required for this settlement to occur depends on the permeability and compressibility of the liquefied soil, the permeability of the soils immediately above and below it, and on the length of the drainage path — it typically ranges from a few minutes up to a day or more. Estimation of earthquake-induced settlement of sands is difficult. Errors of 25%–50% are common in static settlement predictions; even less accuracy should be expected for the more complicated case of seismic loading. Nevertheless, laboratory-based procedures have been shown to produce results that agree reasonably well with many cases of observed field behavior under free-field conditions.

### 9.6.6.1 Free-Field Reconsolidation Settlement

Free-field settlement, i.e., settlement of level ground away from the influence of structures, results from the tendency of soil to contract, or densify, when shaken. Procedures for estimating the volumetric strain of dry and saturated clean sands subjected to cyclic loading were described in Section 6.6.5.4. Under level-ground conditions, one-dimensional compression is assumed, so the vertical strain, $\varepsilon_v$, is equal to the volumetric strain, $\varepsilon_{vol}$. Reconsolidation settlement is then calculated by integrating vertical strain over the thickness of the soil profile:

$$\Delta H = \int_0 \varepsilon_v\, dz \tag{9.85}$$

It is generally more practical to divide a soil profile into a series of sublayers, compute the settlement of each sublayer as the product of its vertical strain and thickness, and sum the sublayer settlements:

$$\Delta H = \sum_{i=1}^{N} \varepsilon_v(z_i)\, \Delta z_i \tag{9.86}$$

where $\varepsilon_v(z_i)$ = vertical strain in the $i$th of $n$ sublayers and $\Delta z_i$ = thickness of the $i$th sublayer. It should be noted that a one-dimensional integration of this form implicitly assumes infinite lateral homogeneity of soil layers, ignores arching effects that can exist in three-dimensional, spatially variable soil deposits, and assumes that volumetric strains at extremely large depths will contribute to settlement at the ground surface.

[@ZhangEtAl2002] used the laboratory-based vertical strain model of [@IshiharaYoshimine1992] and an empirical correlation between relative density and CPT tip resistance to estimate volumetric strain as a function of $q_{c1Ncs}$ and factor of safety against triggering of liquefaction (Figure 9.80). More recent volumetric strain relationships have been proposed by [@YoshimineEtAl2006], [@CetinEtAl2009], and [@OlayaBray2022]; the latter two of these include characterization of uncertainty in volumetric strain. Settlements computed by the [@ZhangEtAl2002] procedure were shown to agree well with observed settlements at sites in and near San Francisco in the 1989 Loma Prieta earthquake. However, settlements obtained by pure volumetric strain integration (Equation 9.85) were shown to underpredict smaller (less than about 6 cm) settlements and overpredict larger (greater than about 6 cm) settlements in the February 2011 Christchurch earthquake [@GeyinMaurer2019]; this bias was greatly reduced by applying a depth weighting factor of the form $(1.0 - 0.1z)$ to the volumetric strain where $z$ is depth in meters and volumetric strains at depths greater than 10 m are not considered to contribute to surface settlement.

**Figure 9.80** Relationship between post-liquefaction volumetric strain and clean sand CPT tip resistance for different factors of safety against triggering of liquefaction. ([@ZhangEtAl2002] with permission of Canadian Science Publishing.)

The volumetric strain relationship of [@ZhangEtAl2002] shown in Figure 9.80 can be approximated [@JuangEtAl2013] by the relationship

$$\varepsilon_v\,(\%) = \begin{cases} a_0 + a_1 q + \cdots & \text{for } FS_L \geq [\cdots] \\ \min\!\left(a_0 + a_1 q + \cdots,\; \ln(\ln FS_L)(a_2 + a_3 q)\right) & \text{for } [\cdots] < FS_L < [\cdots] \\ b_0 + b_1 q + b_2 q\ln(\ln FS_L) & \text{for } FS_L \leq [\cdots] \end{cases} \tag{9.87}$$

where $a_0 = 0.3773$, $a_1 = -0.0337$, $a_2 = 1.5672$, $a_3 = -0.1833$, $b_0 = 28.45$, $b_1 = -9.3372$, $b_2 = 0.7975$, and $q = q_{t1Ncs}$ in kg/cm².

### Example 9.8

Consider the level ground soil profile shown below. Calculate the free-field settlement that would be expected within a few weeks of an earthquake that produces the indicated factors of safety against triggering.

**Solution:**

Layers 1, 2, and 5 have high $I_c$ values and are therefore not susceptible to liquefaction; Layers 1 and 2 are also above the water table so they can be assumed not to trigger. While Layer 5 may generate some excess pore pressure that will result in settlement upon dissipation, it is likely sufficiently fine-grained that any such settlement would occur slowly. The vertical strains of the coarse-grained layers can be estimated using Equation (9.87), which then allows the calculation of the free-field settlement.

Depth / $q_{c1Ncs}$ / $FS_L$ / $\varepsilon_v$ (%) / $\Delta H_i$ (m):
- 0–1 m: ∞ (above water table)
- 1–2 m: ∞ (above water table)
- 2–3 m: 0.85, 1.05, 0.011
- 3–4 m: 0.78, 1.64, 0.016
- 4–5 m: ∞ (non-susceptible)
- 5–6 m: 0.95, 0.72, 0.007

Then the total predicted settlement is the sum of the layer settlements, 0.034 m, or 3.4 cm.

The observed tendency for the [@ZhangEtAl2002] procedure to overestimate large observed settlements led to the introduction of an indicator variable (= 1 for triggering of liquefaction, 0 if there is no possibility of liquefaction) applied to volumetric strains; the mean and standard deviation of the indicator variable are $P_L$ and $\sqrt{P_L(1-P_L)}$, respectively [@JuangEtAl2013]. Then, for a soil profile of $N$ layers, the ground surface settlement can be estimated by summing the probability-weighted contributions of each layer:

$$\mu_{\Delta H} = \sum_{i=1}^{N} \varepsilon_{v,i}\, \Delta z_i\, P_{L,i} \tag{9.88a}$$

$$\sigma_{\Delta H} = \sum_{i=1}^{N} \sqrt{P_{L,i}(1 - P_{L,i})}\; \varepsilon_{v,i}\, \Delta z_i \tag{9.88b}$$

where the $i$ subscript represents the $i$th layer of the profile. The probability of triggering can be estimated using the procedures in Section 9.5.4 or, in cases where only $FS_L$ is available, by a factor of safety mapping function [@KuEtAl2012] such as

$$P_L \approx \Phi\!\left(-\frac{0.102\ln FS_L}{0.276 + 0.9\, FS_L}\right) \tag{9.89}$$

which applies to factors of safety computed using the CPT procedures of [@RobertsonWride1998] or [@Robertson2009a][@Robertson2009b]. It should be recognized that the spatial variability of soils will influence the magnitude and pattern of post-liquefaction free-field settlement. When soil densities are measured or inferred from data measured in borings or CPT soundings, they represent the densities at those particular locations. The presence of looser or denser zones between such explorations can, depending on their size, depth, thickness, and nature, cause variability in total and differential settlements across a particular site.

### 9.6.6.2 Settlement Due to Ejecta

In a number of earthquakes, significant settlement has been caused by the ejection of soil from beneath the ground surface in the form of sand boils. When sand boils are formed, soils below the original ground surface end up above it, so the original ground surface settles. This often happens beneath or near the edges and corners of structures, where the resulting settlement can impose substantial demands on structures founded on shallow foundations. The amount of settlement due to ejecta cannot be quantified at this time, but a number of factors have been observed to influence it. As discussed in Section 9.6.2, the presence of surficial evidence of liquefaction (i.e., ejecta) is related to the relative thicknesses of liquefiable soil layers and the overlying, non-liquefiable crust. The nature of the crust appears to be important — thickness, grain size and plasticity characteristics, number of penetrations (utility trenches, power poles, foundations, etc.) can all influence ejecta volumes. The depth of the water table and thickness/size of the liquefied zone can have an effect as can underlying layers that, while not fully liquefying, can produce excess pore pressures whose dissipation sustains the upward flow of shallower liquefied layers. Lateral spreading not only creates cracks but also appears to dissipate pore pressure through lateral extension. At a number of locations in Christchurch, NZ, sites that experienced lateral spreading produced less ejecta than level-ground sites that did not spread. At this time, the settlement due to ejecta, $\Delta H_e$, is best estimated, albeit crudely, using manifestation severity indicators such as those described in Section 9.6.2 or by more recent quantitative procedures for estimating ejecta severity [@HutabaratBray2021a][@HutabaratBray2021b][@HutabaratBray2022], and by comparison to relevant case histories (e.g., [@BraySancio2009]; [@BrayEtAl2014]).

### 9.6.6.3 Settlement Due to Instability

Ground settlement can occur without significant volume change when shearing deformations occur via mechanisms that include coupled vertical and lateral movement. Embankments and levees that overlie liquefiable soils can settle when the soil beneath them moves laterally, in some cases being essentially squeezed out from beneath the higher ground (Figure 9.81). Simple, practical procedures for general cases do not exist at this time, but two- or three-dimensional, nonlinear, effective stress numerical analyses with a validated constitutive model can provide insight into likely deformation mechanisms and displacement levels.

**Figure 9.81** Chart for estimating crest settlement of dams. (After [@Swaisgood2003] with permission of J.R. Swaisgood.)

[@Swaisgood2003][@Swaisgood2014] compiled settlement data for 69 earth dam embankments and found that the average crest settlement, $\Delta$, could be estimated as

$$\Delta = 0.01\exp\!\left[6.07\, DH + AT + 0.57\, \text{PGA} + 8.0\, M_s\right] \tag{9.90}$$

where $DH$ = dam height, $AT$ = alluvium thickness (Figure 9.81) and PGA is expressed as fraction of $g$. This settlement was interpreted as being caused by both volume change and spreading of the embankment and soils beneath it. Based on actual settlement data, this relationship was developed from a collection of dams with different characteristics at different sites in different geologic/tectonic environments and provides only a very rough indication of the expected settlement of any particular dam.

### 9.6.6.4 Foundation Settlement Effects

Structures located in areas underlain by potentially liquefiable sites are often supported by deep foundations. However, some older structures and/or relatively lightweight structures may be supported on shallow foundations that are underlain by liquefiable soils. Other structures may have been designed and constructed before liquefaction hazards at their sites were recognized. Such structures, and the utilities that connect to them, must be designed or retrofitted to accommodate settlement. Deep foundations may also be adversely affected by liquefaction. The effects of lateral spreading on pile foundations is a complex soil-structure interaction problem that was discussed in Section 8.5.2.2. Pile foundations can also be affected by downdrag loads induced by post-earthquake settlement of liquefiable soils and the soils that overlie them.

#### Shallow Foundations

Structures supported by shallow foundations underlain by liquefiable soils have been observed to settle after earthquake shaking. Their settlement is typically greater than the free-field settlement of the surrounding soil because the soil beneath the foundation is not in a free-field situation. A structure supported by a shallow foundation will respond dynamically, and displace/rotate differently than soil in the free-field at the same depth. The horizontal displacement and rocking of the structure will impose additional shear stresses on the soil beneath it, particularly below its edges and corners. These stresses, and the strains they produce, can lead to additional pore pressure generation, additional fabric disturbance, and additional settlement. In some cases, evidence of liquefaction has been observed in the vicinity of a structure when it is not observed in the surrounding free-field area, indicating that the stresses from the building response caused liquefaction [@BrayEtAl2004][@TravasarouEtAl2006]. Early investigations of shallow foundation settlement following earthquakes at sites generally with thick, clean sands noted that the amount of settlement was related to the thickness of the liquefied soil and the width of the structure [@YoshimiTokimatsu1977][@LiuDobry1997]. Compilations of data from the 1964 Niigata and 1990 Luzon earthquakes (Figure 9.82) show that foundation settlement increased with increasing liquefied layer thickness and decreasing building width. Observations from more recent earthquakes in Turkey, Taiwan, Chile, New Zealand, and Japan, however, have shown more complex behavior with loss of ground from beneath foundations due to ejecta playing a significant role in producing settlement. More recent research (e.g., [@BrayMacedo2017]) has identified a number of mechanisms that can contribute to structure settlement through volumetric or shearing mechanisms. These include ejecta-induced settlement (Figure 9.83a), shear-related deformations (punching settlement and tilting) due to partial bearing failure (Figure 9.83b), ratcheting deformations due to SSI-induced cyclic loading near the edges and corners of the foundation (Figure 9.83c), and volumetric-related deformations from sedimentation (Figure 9.83d) and consolidation-induced volumetric strains associated with three-dimensional pore pressure dissipation (Figure 9.83e) including partial drainage due to intense, transient hydraulic gradients that can develop during shaking.

**Figure 9.82** Variation of average foundation settlement at thick, clean sand sites with building width and thickness of liquefied soil in two earthquakes. (After [@LiuDobry1997] with permission of ASCE.)

**Figure 9.83** Liquefaction-induced building displacement mechanisms: (a) ground loss due to soil ejecta; shear-induced settlement from (b) punching failure, or (c) soil-structure-interaction (SSI) ratcheting; and volumetric-induced settlement from (d) sedimentation or (e) post-liquefaction reconsolidation. ([@BrayMacedo2017].)

**Figure 9.84** Illustration of shallow foundation underlain by liquefiable soil. Liquefiable layer assumed to be sufficiently thick that its thickness, $D_2$, does not affect foundation settlement. (After [@BrayMacedo2017] with permission of Elsevier Science and Technology Journals.)

Centrifuge tests have shown that the interaction between a structure and underlying liquefiable soil is complex, and that it depends on the depth as well as thickness of the liquefiable soil; simple relationships such as that shown in Figure 9.82 do not apply when shearing mechanisms are more significant, such as cases where the structure is stiff or heavy or the liquefiable layer is thin or shallow. Shear-induced settlements increase with increasing liquefiable layer thickness up to a point beyond which they remain essentially constant, in contrast to the thickness proportionality implied in Figure 9.82.

An estimate of the liquefaction-induced settlement of buildings supported on shallow foundations can be made by predicting shear-induced settlement associated with a punching-type bearing capacity mechanism [@BrayMacedo2017]. This component of settlement is added to the previously described components (reconsolidation and ejecta) to estimate the total settlement of the structure. Idealizing the soil profile as a two-layer system (Figure 9.84) consisting of a shallow non-liquefied crust underlain by a layer in which liquefaction is determined to have been triggered, the factor of safety against bearing capacity failure can be calculated as

$$FS_{BC} = \frac{q_{ult}}{q} \tag{9.91}$$

where $q$ is the applied bearing pressure and the ultimate bearing capacity, $q_{ult}$, is computed [@MeyerhofHanna1978] as

$$q_{ult} = C_a D_f + \gamma \leq 5.14\,C + \gamma D_f \tag{9.92}$$

$$C_a = 0.612 + 0.96\left(\frac{C_a - C}{C}\right) - 0.58\left(\frac{C_a}{C}\right) \tag{9.93}$$

Factor of safety values less than 1.0, indicating bearing capacity failure, have been associated with unacceptable performance in past earthquakes [@BrayMacedo2017]. If bearing capacity failure is not indicated, a liquefaction-induced building settlement index, LBS, can be computed as

$$\text{LBS} = \sum_{i=1}^{n} W(z_i)\, \gamma_{\max,i}\, \Delta z_i \tag{9.94}$$

where the foundation-weighting factor $W = 0.0$ (for $z < D_f$) or $1.0$ (for $z > D_f$), $\gamma_{\max}$ is obtained from Figure 9.79, and index $i$ is for sublayers defined from the ground surface downward ($n$ in total). The shear-induced building settlement (in mm) can then be estimated from

$$\ln \Delta_s = c_1 + c_2\,\text{LBS} + 0.58\ln\!\tanh\!\left(\frac{H_L}{B}\right) + 4.59\ln q - 0.42\ln q + 0.84\ln(\text{CAV}_{dp}) + 0.41\ln(S_a(1.0)) + \varepsilon \tag{9.95}$$

where $c_1 = -8.35$ and $c_2 = 0.072$ for LBS $\leq 16$ and $c_1 = -7.48$ and $c_2 = 0.014$ otherwise, $H_L$ is the cumulative thickness of liquefiable layers in meters, $q$ is the applied bearing (contact) pressure in kPa, $B$ is the building width in meters, $\text{CAV}_{dp}$ is a standardized version of cumulative absolute velocity [@CampbellBozorgnia2011] (Section 3.3.4.2) in g-sec, $S_a(1.0)$ is the 5%-damped spectral acceleration at $T = 1.0$ sec in g, and $\varepsilon$ is a normally distributed random variable with zero mean and standard deviation of 0.50 in ln units.

### Example 9.9

An office building with a 30 m × 30 m stiff mat foundation is underlain by the soil profile shown below. The building imposes a bearing pressure of 100 kPa on the supporting soils. Estimate the median shear-induced settlement that would result from a ground motion with $S_a(1.0) = 0.30$ g and $\text{CAV}_{dp} = 0.58$ g-sec. Triggering analyses for free-field conditions produced the average $FS_L$ values for each soil layer as provided in the figure.

**Solution:**

Based on the $FS_L$ values and relative densities, free-field maximum cyclic shear strains are estimated using Figure 9.79. The liquefaction-induced building settlement index layer components (LBS) are then computed using Equation (9.94).

Depth ($z_i$, m) / Layer Thickness (m) / $\gamma_{\max,i}$ (%) / LBS:
- 1.0: n.a.
- 3.5: 4.0, 3.43
- 6.0: 1.8, 0.60
- 9.0: 7.1, 3.16
- 12.5: 2.5, 0.60

The layer components can be summed to produce LBS = 7.79. With that value established, the settlement can be computed using Equation (9.95):

$$\ln \Delta_s = -8.35 + 0.072(7.79) + \cdots + 4.59\ln(100) + \cdots$$
