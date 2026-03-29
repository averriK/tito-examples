### Example 6.6

A 6-in.-high specimen of soft silty clay with a unit weight of 105 lb/ft³ is tested in a resonant column device with $I/I_0 = 0.4$. From the frequency response curve shown in Figure E6.6, determine the shear modulus and damping ratio of the specimen.

**FIGURE E6.6**

**Solution:**

The maximum amplitude of the accelerometer output occurs at the fundamental frequency of the specimen, determined graphically to be $f_n = 41$ Hz. Then Equation (6.69) can be written as $\omega_n h / V_s = \tan(0.4\, I/I_0)$, which is satisfied when $\omega_n h / V_s = 0.593$. Then

$$V_s = \frac{2\pi f_n h}{0.593} = \frac{2\pi(41)(0.5)}{0.593} = 212 \text{ ft/s}$$

$$G = \rho V_s^2 = \frac{105 \text{ lb/ft}^3}{32.2 \text{ ft/s}^2}(212 \text{ ft/s})^2 = 146{,}557 \text{ lb/ft}^2$$

Using the half-power bandwidth method, the half-power level is equal to $74.3\,\text{mV}/\sqrt{2} = 52.6\,\text{mV}$. The upper and lower frequencies at that level are 43.0 and 38.5 Hz, respectively. The damping ratio is then estimated as

$$\xi = \frac{f_{\text{upper}} - f_{\text{lower}}}{2 f_n} = \frac{43.9 \text{ Hz} - 38.5 \text{ Hz}}{2(41 \text{ Hz})} = 0.066 = 6.6\%$$

The resonant column test allows stiffness and damping characteristics to be measured under controlled conditions. The effects of effective confining pressure, strain amplitude, and time can readily be investigated. However, measurement of porewater pressure is difficult, and the material properties are usually measured at frequencies above those of most earthquake motions.

**Bender Element Test**

Another type of test that allows measurement of shear wave velocity on laboratory specimens makes use of piezoelectric bender elements (Shirley and Anderson, 1975; De Alba et al., 1984; Dyvik and Madshus, 1985; Da Fonseca et al., 2009). Bender elements are constructed by bonding two piezoelectric materials together in such a way that a voltage applied to their faces causes one to expand while the other contracts, causing the entire element to bend as shown in Figure 6.76. Similarly, a lateral disturbance of the bender element will produce a voltage, so the bender elements can be used as both s-wave transmitters and receivers. In most setups, the bender elements protrude into opposite ends of a soil specimen. A voltage pulse is applied to the transmitter element, which causes it to produce an s-wave. When the s-wave reaches the other end of the specimen, distortion of the receiver element produces another voltage pulse. The time difference between the two voltage pulses is measured with an oscilloscope and divided into the distance between the tips of the bender elements to give the s-wave velocity of the specimen. Piezoelectric bender elements have been incorporated into conventional and cubical triaxial devices, direct simple shear devices, oedometers, and model tests. Since the specimen is not disturbed during the bender element test, it can be subsequently tested for other soil characteristics.

### 6.5.4.3 High Strain Element Tests

At high shear strain amplitudes (greater than the volumetric threshold strain, $\gamma_{tv}$), soils generally exhibit volume change tendencies (Section 6.4.1.3). Under drained loading conditions, these tendencies are manifested in the form of volumetric strain, but under undrained conditions they result in changes in pore pressure (and, hence, effective stress). Since soil behavior is governed by effective stresses, all methods of testing soils at high strain levels must be capable of controlling porewater drainage from the specimen and measuring volume changes and/or pore pressures accurately. The problem of system compliance (volume changes due to compliance of the testing apparatus rather than the soil), which can lead to errors in volume change/pore pressure measurement, is important in the interpretation of high-strain test results. Membrane penetration in coarse-grained soil is an important contributor to system compliance.

**FIGURE 6.76** Piezoelectric bender element. Positive voltage causes element to bend one way, negative voltage causes it to bend the other.

**Cyclic Triaxial Test**

Just as the triaxial compression test is the most commonly used laboratory test for the measurement of soil properties under static loading conditions, the cyclic triaxial test has historically been the most commonly used test for the measurement of dynamic soil properties of both plastic and nonplastic soils at high strain levels. In the triaxial test, a cylindrical specimen is placed between top and bottom loading platens and surrounded by a thin rubber membrane (Figure 6.77). Prior to cyclic loading, the specimen is subjected to a radial stress, usually applied pneumatically, and an axial stress. The radial stress is applied by pressurized fluid in a cell, and hence also acts vertically on the top cap of the specimen. Additional axial stress can be applied through a rod connected to a load cell, as shown in Figure 6.77. By virtue of these boundary conditions, the principal stresses in the specimen are always vertical and horizontal. The difference between the axial stress and the radial stress is called the deviator stress. In the cyclic triaxial test, the deviator stress is applied cyclically, either under stress-controlled conditions (typically by pneumatic or hydraulic loaders), or under strain-controlled conditions (by servo-hydraulic or mechanical loaders). Cyclic triaxial tests are most commonly performed with the radial stress held constant and the axial stress cycled at a frequency of about 1 Hz. The amplitude of loading in a cyclic triaxial test is often expressed in the normalized form of a cyclic stress ratio, CSR, taken as the ratio of half the deviator stress normalized by minor principal effective stress to which the soil was consolidated prior to the onset of cyclic loading:

$$\text{CSR} = \frac{\sigma_{dc}}{2\sigma'_c} \tag{6.72}$$

where $\sigma'_c$ is the minor principal effective stress during consolidation, and $\sigma_{dc}$ is the cyclic deviator stress. The quantity $\sigma_{dc}/2$ corresponds to the maximum cyclic shear stress on any plane in the specimen. As with the static triaxial test, the cyclic triaxial test can be performed under isotropically consolidated or anisotropically consolidated conditions, thereby producing the stress paths shown in Figure 6.78.

**FIGURE 6.77** Typical triaxial apparatus.

**FIGURE 6.78** Time series of deviator stress and total stress paths for (a) isotropically consolidated conditions, (b) anisotropically consolidated conditions with cyclic deviator stress amplitude greater than deviator stress during consolidation (producing stress reversals), and (c) anisotropically consolidated conditions with cyclic deviator stress amplitude less than deviator stress during consolidation (no stress reversals).

Figure 6.78a shows the cyclic deviator stress and total stress path for an isotropically consolidated specimen. Isotropically consolidated tests are commonly used to represent level-ground sites where no initial shear stresses exist on horizontal planes. The test begins with zero deviator (shear) stress (point A) and the deviator stress is initially increased. Since the axial stress is then greater than the radial stress, the major and minor principal stress axes are vertical and horizontal, respectively. After the deviator stress reaches its maximum value (point B), it decreases and approaches a value of zero (point C). Just before it reaches point C, the major principal stress axis is still vertical, but it rotates instantaneously to horizontal as point C is passed and the deviator stress becomes negative. At point C, no shear stress exists on the specimen. This process of stress reversal repeats itself throughout the test, with instantaneous 90° rotations of the principal stress axes occurring every time the deviator stress passes through zero. To model conditions in and beneath slopes where initial static shear stresses exist, anisotropically consolidated triaxial tests can be performed. Figure 6.78b refers to an anisotropically consolidated specimen for which the cyclic deviator stress amplitude is greater than the deviator stress during consolidation. Stress reversals also exist in this situation, even though the cyclic deviator stress is no longer symmetric about the p-axis. If the cyclic deviator stress amplitude is smaller than the deviator stress during consolidation (Figure 6.78c), no stress reversals will occur. For this case, the principal stress axes will not rotate and the specimen will never reach the zero shear stress condition. The stress paths in Figure 6.78 are obviously different with respect to initial stress conditions, stress path, and principal stress axis rotation than those imposed on the element of soil subjected to vertically propagating s-waves shown in Figure 6.7. These differences illustrate the fundamental difficulty in the direct application of properties obtained from the cyclic triaxial test to actual wave propagation problems. In some cases, the cell pressure is also applied cyclically. By decreasing (or increasing) the cell pressure by the same amount that the deviator stress is increased (or decreased) by, the Mohr circle can be made to expand and contract about a constant center point. The resulting stress path will then oscillate vertically, much like that shown for the case of vertically propagating s-waves (Figure 6.7). Although the stress path of such a triaxial test can be made to match that induced by a vertically propagating s-wave, the principal stresses in the triaxial test remain constrained to the vertical and horizontal direction rather than rotating continuously as caused by the s-wave.

The stresses and strains measured in the cyclic triaxial test can be used to compute the shear modulus and damping ratio (Sections 6.6.3 and 6.6.4). The cyclic triaxial test allows stresses to be applied uniformly, although stress concentrations can exist in the specimen near the cap and base. The test also allows drainage conditions to be controlled (when the potential effects of membrane penetration are mitigated). It requires only minor modification of standard triaxial testing equipment. On the other hand, the cyclic triaxial test cannot model stress conditions that exist in most actual seismic wave propagation problems. Bedding errors and system compliance effects generally limit measurements to shear strains greater than about 0.01%, although local strain measurement (e.g., Burland and Symes, 1982; Ladd and Dutko, 1985; Goto et al., 1991; Yimsiri and Soga, 2002) can produce accurate measurements at strain levels as small as 0.0001%. Membrane penetration effects can be important in cyclic triaxial tests of coarse sands and gravels. After consolidation, the thin triaxial membrane will penetrate the perimeter voids of coarse sand and gravel specimens. As excess pore pressures develop during cyclic loading, the net pressure on the membrane decreases and its penetration decreases. When this happens, the effective volume of the voids increases and the excess pore pressure drops below the level it would have had if true constant-volume conditions had been maintained. Because they allow the effective stresses to be higher than they would be under constant-volume conditions, membrane penetration effects can lead to inaccurate stiffness and damping measurements and unconservative estimation of liquefaction resistance (Chapter 9). Procedures have been developed for measurement (Vaid and Negussey, 1984; Kramer and Sivaneswaran, 1989a), minimization (Lade and Hernandez, 1977; Raju and Venkataramana, 1980), compensation (Seed and Anwar, 1986; Tokimatsu and Nakamura, 1986), and post-test correction (Martin et al., 1978; Kramer and Sivaneswaran, 1989b) of membrane penetration effects. Undrained cyclic triaxial tests on loose, saturated, nonplastic soils can also be complicated by specimen nonuniformity. As high pore pressures develop in a cyclic triaxial test specimen, the soil grains tend to settle causing densification of the lower part and loosening of the upper part of the specimen. The nonuniform density leads to nonuniform strain, and eventually to thinning or necking of the upper portion of the specimen. This nonuniformity can cause considerable uncertainty in the application of cyclic triaxial test results to field conditions.

### Example 6.7

A cyclic triaxial test on a saturated clay specimen produces the stress-strain loop shown in Figure E6.7. Determine the secant shear modulus and damping ratio.

**FIGURE E6.7**

**Solution:**

Graphically, the slope of a straight line between the ends of the stress-strain curve shows that

$$E_{\sec} = \frac{472 \text{ kPa}}{0.028} = 16{,}857 \text{ kPa}$$

Then, assuming that the saturated clay is loaded under undrained conditions, $\nu = 0.5$, so

$$G = \frac{E_{\sec}}{2(1 + \nu)} = \frac{16{,}857 \text{ kPa}}{2(1 + 0.5)} = 5{,}619 \text{ kPa}$$

The area of the hysteresis loop is 4.52 kPa and the area of the triangle denoting the maximum strain energy is 1.65 kPa. Then

$$\xi = \frac{1}{4\pi} \cdot \frac{\text{Area of hysteresis loop}}{\text{Area of triangle}} = \frac{4.52 \text{ kPa}}{4\pi(1.65 \text{ kPa})} = 0.218 = 21.8\%$$

**Cyclic Direct Simple Shear Test**

The cyclic direct simple shear test is capable of reproducing the common stress conditions associated with vertically propagating shear waves much more accurately than the cyclic triaxial test. It is therefore particularly useful for liquefaction, cyclic softening, and seismic compression evaluations. In the cyclic direct simple shear test, a short, cylindrical specimen is restrained against lateral expansion by rigid boundary platens (Cambridge-type device), a wire-reinforced membrane (NGI-type device), or a series of stacked rings (SGI-type device). By applying cyclic horizontal shear stresses to the top or bottom of the specimen, the test specimen is deformed (Figure 6.79) in much the same way as an element of soil subjected to vertically propagating s-waves (Figure 6.7a). The amplitude of cyclic simple shear loading can also be expressed in dimensionless form by normalizing the cyclic shear stress, $\tau_{cyc}$, by the effective stress on the plane of maximum shear stress, $\sigma'_{v0}$. Since that plane is horizontal in the cyclic simple shear test, the cyclic stress ratio is

$$\text{CSR} = \frac{\tau_{cyc}}{\sigma'_{v0}} \tag{6.73}$$

**FIGURE 6.79** NGI cyclic simple shear apparatus. Soil specimen is contained within wire-reinforced rubber membrane (After Airey and Wood, 1987).

The simple shear apparatus, however, applies shear stresses only on the top and bottom surfaces of the specimen. Since no complementary shear stresses are imposed on the vertical sides, the moment caused by the horizontal shear stresses must be balanced by nonuniformly distributed shear and normal stresses. The effects of stress nonuniformity can be reduced by increasing the diameter/height ratio of the specimen; such effects are small at diameter/height ratios greater than about 8:1 (Kovacs and Leo, 1981), although ratios of 4:1 are commonly used. Most simple shear apparatuses are limited by their inability to impose initial stresses other than those corresponding to $K_0$ conditions and apply cyclic loading slowly and in only one horizontal direction. Modern devices can apply bi-directional loading over a wide range of frequencies under either constant height (corresponding to undrained) or constant vertical load (drained) conditions (Boulanger et al., 1993; Shafiee et al., 2017). Because the cyclic simple shear and cyclic triaxial tests impose different loading on soil specimens, their cyclic stress ratios are not equivalent. For liquefaction testing, the two are usually related by

$$\text{CSR}_{ss} = c_r\, \text{CSR}_{tx} \tag{6.74}$$

where the correction factor $c_r$ is estimated from Table 6.5. Laboratory-measured liquefaction resistance can be expressed in terms of cyclic strength curves, i.e., plots of cyclic stress ratio versus number of cycles to liquefaction, such as those shown in Figure 9.23.

**Cyclic Torsional Shear Test**

Some of the difficulties associated with the cyclic triaxial and cyclic direct simple shear tests can be avoided by loading cylindrical soil specimens in torsion. Cyclic torsional shear tests allow isotropic or anisotropic initial stress conditions and can impose cyclic shear stresses on horizontal planes with continuous rotation of principal stress axes. They are most commonly used to measure stiffness and damping characteristics over a wide range of strain levels. Ishihara and Li (1972) developed a torsional triaxial test that used solid specimens. Dobry et al. (1985) used strain-controlled cyclic torsional loading along with stress-controlled axial loading of solid specimens to develop a CyT-CAU test for the measurement of liquefaction behavior. Torsional testing of solid specimens, however, produces shear strains that range from zero along the axis of the specimen to a maximum value at the outer edge. To increase the radial uniformity of shear strains, others (e.g., Drnevich, 1967, 1972) developed hollow cylinder cyclic torsional shear apparatuses (Figure 6.80). While hollow cylinder tests offer perhaps the best uniformity and control over stresses and drainage, specimen preparation can be difficult and testing of specimens from the field is nearly impossible. For this reason, this testing is relatively uncommon and the equipment is not widely available.

**TABLE 6.5** Expressions for Correction Factor Relating Cyclic Triaxial and Simple Shear Cyclic Stress Ratios

$c_r = (1 + K_0)/2$, Finn et al. (1971): $K_0 = 0.4 \Rightarrow c_r = 0.70$; $K_0 = 1.0 \Rightarrow c_r = 1.00$

Seed and Peacock (1971): varies; $K_0 = 0.4 \Rightarrow c_r = 0.55$–$0.72$; $K_0 = 1.0 \Rightarrow c_r = 1.00$

$c_r = 2(1 + 2K_0/3)/3$, Castro (1975): $K_0 = 0.4 \Rightarrow c_r = 0.69$; $K_0 = 1.0 \Rightarrow c_r = 1.15$

**FIGURE 6.80** Hollow cylinder apparatus. The specimen is enclosed within internal and external membranes on which internal and external pressures can be applied independently. Application of cyclic torque induces cyclic shear stresses on horizontal planes.

### 6.5.4.4 Physical Model Tests

In contrast to element tests, physical model tests usually attempt to reproduce the boundary conditions of a particular problem by subjecting a small-scale physical model of a full-scale prototype structure to cyclic loading. Model tests may be used to evaluate the performance of a particular prototype or to study the effects of different parameters on a general problem. Model testing is generally considered to be most effective for the identification of important phenomena and deformation mechanisms and for the verification of predictive theories. It is generally not used for the design of significant structures or facilities. The behavior of soils is sensitive to stress level; soils that exhibit contractive behavior under high normal stresses may exhibit dilative behavior at lower stress levels. One of the most significant challenges in model testing, therefore, is the problem of testing models whose stress dependency matches that of a full-scale prototype. Because this is very difficult under the gravitational field of the Earth, one common approach involves testing under increased gravitational fields. Model tests can therefore be divided into those performed under the gravitational field of the Earth (1g model tests) and those performed under higher gravitational accelerations. The 1g tests are most commonly performed with the use of shaking tables; tests under increased gravitational fields are usually performed in a geotechnical centrifuge. Both shaking table and centrifuge model tests have certain limitations, among the most important of which are similitude and boundary effects. The model scale factor, N, is taken as the ratio of prototype/model dimensions for 1g tests and as the acceleration level applied in centrifuge tests normalized by the Earth's gravitational acceleration (g). Scaling laws describe how various soil properties vary with N and are generally different for 1g vs centrifuge tests. For a given type of test, different soil properties will have different scaling laws, which means that similitude cannot be assured for all parameters simultaneously. Also, boundary effects (at the base and sides of the model) may not realistically capture prototype conditions, with artificial restraint of soil deformation or generation of reflected waves being the most common physical model boundary condition problems.

**Shaking Table Tests**

In the early years of geotechnical earthquake engineering, virtually all physical model testing was performed on shaking tables. Shaking table research has provided valuable insight into liquefaction, post-earthquake settlement, foundation response, and lateral earth pressure problems. Most shaking tables utilize a single horizontal translation degree of freedom but shaking tables with multiple degrees of freedom have also been developed. Shaking tables are usually driven by servo-hydraulic actuators (Figure 6.81); their dynamic loading capacities are controlled by the capacity of the hydraulic pumps that serve the actuators. Large pumps, actuators, and hydraulic accumulators are required to produce large displacements of heavy models at moderate or high frequencies. Shaking table specimens have stiff lateral restraints that are intended to mimic $K_0$ boundary conditions (Figure 6.81). Shaking tables of many sizes have been used for geotechnical earthquake engineering research. Some are quite large, allowing models with dimensions of several meters to be tested. Thus shaking tables can often utilize actual, prototype soils rather than resorting to the smaller particle sizes often required for smaller scale model tests. For these large models, soils can be placed, compacted, and instrumented relatively easily. Shaking table models can be readily viewed from different perspectives during testing. The principal limitation of shake table testing for geotechnical applications is that high gravitational stresses cannot be produced. This may cause, for example, a sand that is contractive at the high overburden stresses that exist under prototype conditions to be dilatant in a small 1g model where stresses are much lower. Although correction procedures (e.g., Hettler and Gudehus, 1985; Iai, 1989) have been developed to aid in the interpretation of shaking table test results, in general shake-table experiments involving sands are generally not a preferred method of testing. Shake table experiments involving clays can be more meaningful, provided stress history effects between model and prototype are consistent.

**FIGURE 6.81** Typical shaking table configuration: (a) schematic illustration (used by permission of Carleton University Geoengineering Research Group) and (b) large-scale (15 ft high, 21.5 ft wide), biaxial laminar soil box at University of Nevada, Reno. (Courtesy of R. Motamed.)

**Centrifuge Tests**

In a centrifuge test, a 1/N-scale model located at a distance, $r$, from the axis of a centrifuge ($\Omega = \sqrt{Ng/r}$, Figure 6.82) is spun at a rotational frequency sufficient to raise the acceleration field at the location of the model to $N$ times the acceleration of gravity, $g$. In principle, the stress conditions at any point in the model should then be identical to those at the corresponding point in the full-scale prototype. Centrifuge tests are restricted to much smaller models than even moderate-sized shaking tables. Since the gravitational field increases with radial distance, the gravitational acceleration at the top of the model is lower than that at the bottom of the model. Since the gravitational field acts in the radial direction, the horizontal plane is curved (O'Reilly, 1991) by an amount that decreases with increasing centrifuge radius. Similitude considerations are very important in the planning and interpretation of centrifuge tests. Scaling factors for a number of parameters are shown in Table 6.6. The scaling factors show how the speed of dynamic events is increased in the centrifuge. For example, the stresses and strains in a 30-m high prototype earth dam could be modeled with a 30-cm high centrifuge model accelerated to 100g. A common misconception of centrifuge tests is that particle sizes are also increased by N (100 in this example), although that is not the case. The particle sizes simply reflect the actual material comprising the model, there are just many fewer of them in the model than in the prototype, even if the stress conditions match. A harmonic 1-Hz base motion lasting 10 sec at the prototype scale would be modeled by a 100-Hz motion lasting 0.1 sec in the model. Because time for pore water pressure dissipation scales with length-squared, it will occur at $N^2$ the rate in the model as in prototype if pore fluids of the same viscosity are used (a factor of 10,000 in the present example). This faster dissipation is one of the few problems causing failure mechanisms in centrifuge models to differ from those in prototypes; otherwise, this method of model testing is considered quite effective at modeling system behaviors. Pore pressure dissipation rate effects can be more accurately modeled by using viscous fluids such as glycerin or silicon oil as pore fluids. High-speed transducers, data acquisition systems, and cameras are required to obtain useful results in dynamic centrifuge tests. Because the scaling laws apply to all parts of the model, miniaturized transducers and cables are required to minimize their influence on the response of the model.

**TABLE 6.6** Scaling Factors for Centrifuge Modeling (Model Dimension / Prototype Dimension). Source: After Kutter and James (1989). Values are based on the assumption that the same soils and fluid are used in the model and the prototype, and that the soil properties are not rate-dependent.

All events — Stress: 1; Strain: 1; Length: 1/N; Mass: 1/N³; Density: 1; Force: 1/N²; Gravity: N.

Dynamic events — Time: 1/N; Frequency: N; Acceleration: N; Strain Rate: N.

Diffusion events — Time: 1/N²; Strain Rate: N².

**FIGURE 6.82** (a) Geotechnical centrifuge (courtesy of Network Rail) and (b) schematic illustration of laminar box.

### 6.5.4.5 Interpretation of Observed Response of Earth Systems

Interpretation of the response of instrumented, full-scale structures subjected to dynamic loading or earthquakes can provide invaluable information on how soils and soil-structure systems behave under realistic dynamic loading and boundary conditions. Because a real, full-scale system rather than a model is being measured, the observed response of such systems is particularly useful for understanding various phenomena in geotechnical earthquake engineering and the validation of modeling approaches. This approach requires a good degree of instrumentation so that the levels of shaking and site response are known. Most typically this is accomplished with vertical arrays (Section 3.2.4.2), preferably with the deepest instrument located below any significant impedance contrasts in bedrock or in stiff soils with high seismic velocities. Vertical arrays may also include pore pressure transducers, inclinometer casings, and other forms of instrumentation. Recorded motions at vertical array sites can be used with a suitable ground response model (Chapter 7) to: (1) evaluate site conditions for which 1D ground response methods provide good estimates of observed site response (e.g., Thompson et al., 2012) or whether 2D or 3D analyses are required; (2) identify the dynamic soil properties (specifically, shear modulus and damping) that produce the best agreement between predicted and actual motions (e.g., Zeghal et al., 1995; Elgamal et al., 2001; Tsai and Hashash, 2009); and (3) study the relative effectiveness of alternative methods of soil behavior modeling, including equivalent linear and nonlinear methods of analysis (e.g., Kaklamanos et al., 2013, 2015; Zalachoris and Rathje, 2015; Kim et al., 2016). At sites where soils within the domain of vertical arrays are potentially liquefiable, pore pressure transducers are very useful for understanding pore pressure generation/dissipation up to, during, and following liquefaction as well as ground motions in liquefied soil (Zeghal and Elgamal, 1994; Bonilla et al., 2005; Kramer et al., 2011). Aside from ground response, field instrumentation is also extremely useful for understanding the response of geotechnical systems including earth dams (Wieland, 2004), levees (Kishida et al., 2009c), and soil-structure systems (Stewart and Fenves, 1998; Tileylioglu et al., 2011). As vertical arrays and instrumented geotechnical structures become more common worldwide (e.g., Section 3.2.4.2), the amount of data at small and large strain conditions produced as earthquakes occur is growing rapidly. Examples of observed ground response from which dynamic soil properties can be identified are presented in Section 7.2.2.

## 6.6 Behavior of Cyclically Loaded Soils

The mechanical behavior of soils can be quite complex under static, let alone seismic, loading conditions. As discussed in Section 6.4.1, soils exhibit nonlinear, inelastic stress-strain behavior. In addition, some soils exhibit rate dependence, cyclic degradation, and/or coupling between their volumetric and deviatoric responses to loading. The propagation of waves through elastic solids has been shown (Appendix C) to be controlled by the density, stiffness, and damping characteristics of the solid. Those characteristics are also important for wave propagation in particulate materials like soils. Accounting for nonlinear, inelastic behavior of soils in the solution of response and ground failure problems, however, also requires characterization of strain-dependent stiffness and damping, volume change (dilation/contraction), and cyclic shear strength behavior of the soil.

### 6.6.1 Characterization of Soil Behavior

The behavior of soils in response to cyclic loading can be characterized in a number of different ways, but a standard framework has emerged over the past 50 years. The framework is rooted in the historical use of equivalent linear analyses (Section 7.5.2) but can be transformed to a framework that is convenient for nonlinear analyses. The equivalent linear framework can characterize the stiffness, strength, and damping behavior of cyclically loaded soils. That behavior, however, can also be strongly influenced by volume change (contraction/dilation) characteristics.

#### 6.6.1.1 Density

As mentioned in Section 6.5.1, with the general exception of liquefiable soils, soil densities are usually relatively easy to measure at the levels of resolution required for geotechnical earthquake engineering applications. For planning or initial calculation purposes, however, typical densities for different types of soils are presented in Table 6.7. Note that the densities of organic soils and waste materials (which often contain significant fractions of organics) are much lower than those of conventional inorganic soils. Well-graded granular soils and overconsolidated fine-grained soils tend toward the upper ends of the density ranges given.

**TABLE 6.7** Typical Ranges of Density and Unit Weight for Different Soil Types. Source: After Holtz et al. (2011).

Columns: Soil Type | $\rho_d$ (Mg/m³) | $\gamma_d$ (kN/m³) | $\gamma_d$ (lb/ft³) | $\rho_{\text{sat}}$ (Mg/m³) | $\gamma_{\text{sat}}$ (kN/m³) | $\gamma_{\text{sat}}$ (lb/ft³)

Sands and gravels: 1.5–2.3, 14.7–22.6, 94–144, 1.9–2.4, 18.6–23.5, 118–150
Silts and clays: 0.6–1.8, 5.9–17.7, 37–112, 1.4–2.1, 13.7–20.6, 87–131
Glacial tills: 1.7–2.3, 16.7–22.6, 106–144, 2.1–2.4, 20.6–23.5, 131–150
Crushed rock: 1.5–2.0, 14.7–19.6, 94–125, 1.9–2.2, 18.1–21.6, 118–137
Peats: 0.1–0.3, 4.9–14.7, 6–19, 1.0–1.1, 9.8–10.8, 62–69
Organic silts and clays: 0.5–1.5, 4.9–14.7, 31–94, 1.3–1.8, 12.7–17.7, 81–112

#### 6.6.1.2 Stiffness Behavior

Figure 6.13c showed that soil stiffness tends to decrease with increasing shear strain amplitude. Figure 6.83a shows the nonlinear stress-strain, or backbone, curve from a monotonic direct simple shear test on a typical soil — the shear modulus decreases from its maximum value, $G_{\max}$, which is mobilized at very low strains, to lower values at moderate and higher strains. At very large strains, the shear strength of the soil is fully mobilized. Defining a secant shear modulus, $G_{\sec}$, as the ratio of shear stress to shear strain, the backbone curve can be represented as

$$\tau = G_{\sec}\,\gamma = G_{\max} \cdot \frac{G_{\sec}}{G_{\max}} \cdot \gamma \tag{6.75}$$

Hence, the overall stiffness behavior of the soil can be described in terms of the maximum shear modulus that describes low-strain stiffness, and a modulus reduction ratio ($G_{\sec}/G_{\max}$, usually written as $G/G_{\max}$) that describes the larger-strain stiffness behavior. A plot of modulus reduction ratio vs. shear strain, as shown in Figure 6.83b, is referred to as a modulus reduction curve. Stiffness behavior is described in detail in Sections 6.6.2 and 6.6.3.

**FIGURE 6.83** Illustration of soil nonlinearity: (a) hyperbolic stress-strain (backbone) curve, and (b) corresponding modulus reduction curve.

#### 6.6.1.3 Strength Behavior

The degradation of soil stiffness occurs at very low shear strain levels and is usually described by modulus reduction curves typically obtained from laboratory tests that are limited to shear strain amplitudes less than about 0.5%–1.0%. The shear strength of the soil, i.e., the limiting shearing resistance, is typically mobilized at shear strains of 5%–20%. As a result, there is a large range of intermediate strain levels over which the stress-strain behavior is not well defined. In many cases, engineers have extrapolated modulus reduction curves beyond the range constrained by laboratory data without considering the effects of that extrapolation on the corresponding backbone curves. The result of this approach can be a modulus reduction curve that smoothly decreases in what appears to be a reasonable manner, but which implies shearing resistances at large strains that may grossly exceed, or fall below, the actual strength of the soil. Therefore, procedures to extrapolate the low-strain behavior obtained from dynamic laboratory tests to large-strain behavior that is consistent with measured shear strengths (Section 6.6.3.3) are required. In this way, modulus reduction curves and $G_{\max}$ values can also be used to characterize the shear strength of a soil. Strength behavior is described in detail in Section 6.6.6.

#### 6.6.1.4 Damping Behavior

The inelastic behavior of cyclically loaded soils gives rise to energy dissipation through hysteretic behavior. Experimental evidence shows that the shapes of hysteresis loops are influenced by strain amplitude — as the shear strain amplitude increases, the loops become broader (Figure 6.84a), which indicates that the damping ratio of the soil increases with increasing strain amplitude (Figure 6.84b). Damping behavior is described in detail in Section 6.6.4.

**FIGURE 6.84** Illustration of soil inelasticity: (a) stress-strain loops at low and high strain levels, and (b) damping curve.

#### 6.6.1.5 Volume Change Behavior

As discussed in Section 6.4.3.2, monotonically loaded soils tend to be contractive (generally loose granular soils or normally consolidated fine-grained soils) or, following initial contraction at small strains, dilative (dense granular soils or heavily overconsolidated fine-grained soils) at large strains. Under cyclic loading, shear strains are often so small that they produce contractive behavior in all soils, leading to densification under drained conditions and increased pore pressure under undrained conditions. Volume change behavior can be characterized in different ways for both drained and undrained conditions, as described in Section 6.6.5.

### 6.6.2 Low-Strain Stiffness

The shear modulus of a linear material is constant, i.e., it has the same value at high strain levels as it does at low strain levels. Soils, however, are known to be strongly nonlinear with shear moduli that decrease with increasing strain level, as shown in Figure 6.83. Laboratory tests have shown that soil stiffness can also be influenced by void ratio, mean principal effective stress, plasticity index, overconsolidation ratio, and other factors. The low-strain shear modulus, $G_{\max}$, is an extremely important parameter, both due to its direct influence on wave propagation at low strain levels and its role in normalizing the shear modulus at higher strain levels in modulus reduction curves. The low-strain stiffness should, whenever possible, be obtained from direct, in situ measurement of shear wave velocity using the types of tests described in Section 6.5.2; the equipment for performing these tests is readily available in most areas. In the event that they are not available, or for making preliminary estimates, shear wave velocities can also be obtained by empirical correlation to other commonly measured parameters. Such correlations, however, introduce significant uncertainty into the estimated low-strain stiffness.

#### 6.6.2.1 Direct Shear Wave Velocity Measurement

The maximum shear modulus describes the stiffness of the soil at extremely low strain levels. Since most seismic geophysical tests induce shear strains lower than about $3 \times 10^{-4}$%, the shear wave velocities measured in the field can be used to compute $G_{\max}$ as

$$G_{\max} = \rho V_s^2 \tag{6.76}$$

It should be noted that Equation (6.76) was obtained from the derivation of the wave equation (Section C.2.1). In that derivation, the density affects the inertial force required to ensure dynamic equilibrium, hence, it should include the masses of all phases within a soil that accelerate as a wave passes through it. For virtually all soils, the porewater in the soil will move with the soil particles, so the total density should be used in Equation (6.76). The use of measured shear wave velocities is the most reliable means of evaluating the in situ value of $G_{\max}$ for a particular soil deposit, and the seismic geophysical tests described in Section 6.5.2 are commonly used for that purpose. When measured in the field at a particular site, the stiffness of soil or rock will generally increase with depth as shown in Figure 6.85a. The increase in stiffness can be due to increased confining pressures, particle cementation, decreased weathering, increasing geologic age, or some combination of these and other factors. As a result, shear wave velocity profiles are generally observed to increase with depth. The nature of that increase, however, varies from site to site — at some sites, $V_s$ may increase smoothly over an extended depth range, while in others it may increase in steps characterized by individual layers with relatively constant velocities. At some sites, softer soils may be covered by stiffer soils, either naturally deposited or placed as compacted fill; such conditions are referred to as velocity inversions. Shear wave velocities at shallow depths can vary seasonally as changes in soil moisture affect effective stresses (Roumelioti et al., 2020). For site response problems (Section 3.4.3), ground response is influenced more strongly by low-velocity layers than high-velocity layers. In such cases, plots of slowness profiles, where slowness is defined as the reciprocal of velocity, can help emphasize the most important layers and aid in comparisons of different profiles measured at the same site (Brown et al., 2002). Figure 6.85 shows shear wave velocity and slowness plots for two profiles; the enhanced resolution of the softer portion of the profile in the slowness profile is apparent.

**Uncertainty in Low-Strain Stiffness**

Because low-strain stiffness is commonly obtained from measured shear wave velocity, uncertainty in low-strain stiffness is best expressed in terms of uncertainty in shear wave velocity. This uncertainty can be evaluated when multiple $V_S$ profiles are measured at different locations at a given site, which in general will not match. These variations in measured velocities, when based on reliable geophysical methods, represent the variability of the geologic structure of the site. Such variations are always present to varying degrees and give rise to variability in site response. If the variations in $V_S$ can be measured at a site using multiple profiles, a mean and standard deviation of $V_S$ can be quantified on a site-specific basis. This is desirable because such a characterization would presumably reflect the local geologic conditions. However, in many cases only a single profile is available, and is generally assumed to represent the mean. In such situations, it is necessary to estimate the variability of $V_S$ from relationships derived from data at sites where many $V_S$ profiles have been measured. Because these relationships are relatively generic, they will not necessarily represent the local geologic conditions at a particular site very well.

**FIGURE 6.85** (a) Increase of shear wave velocity with depth at site with approximately 29 m of soil overlying weathered rock; (b) variation with depth of slowness for the same site. Slowness profile emphasizes characteristics of softer layers that often play the most important role in site response.

One such set of statistical relations based on $V_S$ profiles in California and Georgia was given by Toro (1995). For a given depth, $V_S$ is typically found to be lognormally distributed with a depth-dependent standard deviation ($\sigma_{\ln V_s}$). As shown in Figure 6.86, values of $\sigma_{\ln V_s}$ are provided for "generic" and "site-specific" applications. The generic results apply for horizontal separation distances between profiles on the order of several hundred meters to a few km or more, whereas the separation distances for site-specific range from 2 to 800 m. The generic $\sigma_{\ln V_s}$ is based on statistics for many sites within broadly defined NEHRP (Dobry et al., 2000) or Geomatrix (Chiou et al., 2008) site classes — they are intended for use with generic median $V_S$ profiles for each site class. The site-specific standard deviations are intended for use with a measured $V_S$ profile, which is generally taken as the mean for the site. The two site-specific profiles of $\sigma_{\ln V_s}$ in Figure 6.86 reflect attributes of velocity clusters (Stewart et al., 2014) and mid-layer velocities (EPRI, 2013 and Toro, 2022). The intra- and inter-method variabilities of SASW, MASW, and ReMi techniques from five arrays have been investigated at a single site with a relatively simple velocity profile (Cox and Wood, 2011). The mean shear wave velocity profiles at the site were generally within about 12% of each other in the upper 5 m of the profile and within 20%–30% at greater depths. When the analyses were repeated using a common water table depth (obtained from p-wave velocity measurements in the MASW test), the inter-method variability dropped from a maximum of 30% to approximately 10%, which reinforces the need for accurate knowledge of groundwater conditions. More complex sites would likely show greater inter-method variability. As described previously (Section 6.5.2.2), variations of phase velocities obtained by the ReMi method, related to different array orientations and active vs. passive energy sources, can reach 100% (Cox and Beekman, 2011). The potential also exists for significant bias with that method. Investigations of intra- and inter-method variability of invasive and non-invasive methods (e.g., Garofalo et al., 2016a) have shown that $V_s$ coefficients of variation (COV) for invasive methods were generally, but not always, lower than for non-invasive methods. COV values were typically larger near the surface and on the order of 0.2–0.35 for soil sites, and then decreased with depth to values of approximately 0.1–0.2. However, larger values of COV were calculated for a rock site, with COV values as high as 0.4–0.6 at the surface.

**Uncertainty in $V_{S30}$**

The uncertainty in $V_{S30}$ (Section 3.4.3.1) from measured velocity profiles has been evaluated from sites with clusters of profiles, typically spaced on the order of 10 to about 100 m. This uncertainty, denoted $\sigma_{\ln V_{S30}}$, is useful for uncertainty propagation in ground motion predictions that utilize $V_{S30}$-based site response models (Section 3.5.2.3). This uncertainty can in general be influenced by variations among $V_S$ measurement types (generally small when reliable data providers are used) and natural heterogeneity in the site conditions. Based on data compilations by Moss (2008), Seyhan et al. (2014), and Yust et al. (2018), ranges of $\sigma_{\ln V_{S30}}$ were approximately 0.02–0.12. For sites without strongly variable geological conditions, averages of about 0.06–0.07 have been found. Values of 0.1 are often applied in practice.

**FIGURE 6.86** Variation of standard deviation of $V_S$ with depth for generic and site-specific conditions. (Adapted from Toro, 1995, Stewart et al., 2014, and Toro, 2022.)

#### 6.6.2.2 Empirical Correlation

The maximum shear modulus can also be estimated by empirical correlation to commonly measured in situ test parameters. In general, $G_{\max}$ increases with increasing soil density as do SPT and CPT penetration resistances, so it is logical to expect some correlation between $G_{\max}$ (or $V_s$) and penetration resistance. It should be recognized, however, that $G_{\max}$ is a low-strain parameter that can be influenced by factors such as particle cementation (generally related to the age of the deposit) and soil fabric, which are destroyed at the large strain levels (DeJong et al., 2006) induced by penetration testing. A number of empirical relationships between $G_{\max}$ and various in situ test parameters have been developed. Many of these correlations can be expressed as functions of penetration resistance, depth or effective stress, and material type, e.g., as

$$\ln V_s = c_0 + c_1 \ln(\text{PR}) + c_2 \ln(f_z) + c_3 f_m + \varepsilon\,\sigma_{\ln V_s} \tag{6.77}$$

where PR = penetration resistance, $f_z$ = depth or effective stress parameter, $f_m$ = material parameter, $\varepsilon$ = standard normal variate, and $\sigma_{\ln V_s}$ = standard deviation of $\ln V_s$; not all relationships include all of these terms. Values of the coefficients for Equation (6.77) are shown in Table 6.8.

**TABLE 6.8** Coefficients for Shear Wave Velocity (m/s) Prediction Models. Source: After BSSC (2020). Column $f_z$: $\sigma'_{v0}$ = vertical effective stress in kPa; $z$ = depth in meters.

Sand (Brandenberg et al., 2010): PR = $N_{60}$; $f_z = \sigma'_{v0}$; $c_0$ = 4.045, $c_1$ = 0.096, $c_2$ = 0.236, $c_3$ = 0.0; $\sigma_{\ln V_s}$: $\tau = 0.217$, $\sigma = \min(0.20,\, 0.57 - 0.07\ln\sigma'_{v0})$, $\sigma_{\ln V_s} = \sqrt{\tau^2 + \phi^2}$

Silt (Brandenberg et al., 2010): PR = $N_{60}$; $f_z = \sigma'_{v0}$; $c_0$ = 3.783, $c_1$ = 0.178, $c_2$ = 0.231, $c_3$ = 0.0; $\tau = 0.227$, $\sigma = \min(0.15,\, 0.31 - 0.03\ln\sigma'_{v0})$, $\sigma_{\ln V_s} = \sqrt{\tau^2 + \phi^2}$

Clay (Brandenberg et al., 2010): PR = $N_{60}$; $f_z = \sigma'_{v0}$; $c_0$ = 3.996, $c_1$ = 0.230, $c_2$ = 0.164, $c_3$ = 0.0; $\tau = 0.227$, $\sigma = \min(0.16,\, 0.21 - 0.01\ln\sigma'_{v0})$, $\sigma_{\ln V_s} = \sqrt{\tau^2 + \phi^2}$

$I_c < 2.6$ (Hegazy and Mayne, 2006): PR = $q_t/p_a$; $f_z = p_a/\sigma'_{v0}$; $f_m = e^{1.786 I_c}$; $c_0$ = –2.488, $c_1$ = 1.0, $c_2$ = 0.25, $c_3$ = 1.0

$I_c > 2.6$ (Hegazy and Mayne, 2006): PR = $q_t/p_a$; $f_z = p_a/\sigma'_{v0}$; $f_m = e^{1.786 I_c}$; $c_0$ = –2.488, $c_1$ = 1.0, $c_2$ = 0.50, $c_3$ = 1.0

Holocene (Andrus et al., 2007): PR = $q_t/p_a$; $f_z = z$; $f_m = I_c$; $c_0$ = 2.699, $c_1$ = 0.395, $c_2$ = 0.124, $c_3$ = 0.912

Pleistocene (Andrus et al., 2007): PR = $q_t/p_a$; $f_z = z$; $f_m = I_c$; $c_0$ = 2.896, $c_1$ = 0.395, $c_2$ = 0.124, $c_3$ = 0.912

Holocene and Pleistocene sands (Robertson, 2012): PR = $(q_t - \sigma_v)/p_a$; $f_z = \sigma'_{v0}/p_a$; $f_m = e^{I_c}$; $c_0$ = 1.93, $c_1$ = 0.5, $c_2$ = 0.25, $c_3$ = 0.63

Christchurch soils (McGann et al., 2015): PR = $q_t/p_a$; $f_z$ = $f_s/p_a$; $c_0$ = 3.959, $c_1$ = 0.144, $c_2$ = 0.278, $c_3$ = 0.0832; $z_i$; $\sigma_{\ln V_s}$ = 0.162 for $z < 5$ m; = $0.216 - 0.0108z$ for $5\text{ m} < z < 10\text{ m}$; = 0.108 for $z > 10$ m

**Correlations Based on Laboratory Tests**

Menq (2003) tested multiple granular soils ranging from sands to gravels and found that $G_{\max}$ was influenced by grain size characteristics as well as soil density and effective confining pressure. Regression on test data from these materials suggested that $G_{\max}$ could be estimated as

$$G_{\max,\text{lab}} = \frac{C_1}{C_u^{0.2}}\, e^x \left(\frac{\sigma'_v}{p_a}\right)^{n_G} \tag{6.78}$$

where $C_1$ = 67.1 MPa (1,400 ksf), $C_u$ = coefficient of uniformity, $e$ = void ratio, $x = -1 - (D_{50}/20)^{0.75}$, $D_{50}$ = mean grain size in mm, and $n_G = 0.09 + 0.48/C_u$. This relationship indicates that $G_{\max}$ increases with increasing $D_{50}$, $C_u$, and $\sigma'_v$, and with decreasing void ratio. For fine-grained soils, preliminary estimates of $G_{\max}$ can be obtained from undrained strength, plasticity index, and overconsolidation ratio (Table 6.9). Because undrained strengths are highly variable and because shear moduli and undrained strength do not vary in the same way with effective confining pressure, these results must be used carefully. Highly organic soils and peats can behave differently than conventional inorganic soils. Their low-strain stiffnesses have been found to be affected by effective stress level, overconsolidation ratio, and organic content. Based on testing of laboratory specimens of organic soils, Kishida et al. (2009a) proposed that $G_{\max}$ could be estimated as

$$G_{\max,\text{lab}} = A \left(\frac{\sigma'_v}{p_a}\right)^n \text{OCR}^m \tag{6.79}$$

where $p_a$ = atmospheric pressure and $A$, $n$, and $m$ are empirical coefficients related to organic content, OC (in percent), by

$$A \approx 121.31 - 0.9354\,\text{OC} + 0.0036\,\text{OC}^2 \tag{6.80}$$

$$n = 0.37 / [1 + \exp(-\text{OC}/23)] \tag{6.81}$$

$$m = -0.8 + 0.4 / [1 + \exp(-\text{OC}/23)] \tag{6.82}$$

Comparisons of laboratory and field measurements of $V_s$ on the same soil indicate an under-prediction bias from the laboratory-based model, likely due primarily to disturbance effects in the laboratory samples. Kishida et al. (2009b) recommended that the bias be removed as follows:

$$G_{\max,\text{field}} = 1.19\, G_{\max,\text{lab}} \tag{6.83}$$

**TABLE 6.9** Values of $G_{\max}/s_u$ (undrained strength measured in CU triaxial compression). Source: After Weiler (1988).

Plasticity Index, PI: 15–20 → $G_{\max}/s_u$ = 1,100; PI: 20–25 → 35–45 (overconsolidation ratio dependent; see source for full table).

**Correlations for $V_{S30}$**

Measuring shear wave velocities is standard practice for contemporary site-specific subsurface investigations in seismically active areas. In areas where shear wave velocities cannot be, or have not yet been measured, several proxies for $V_{S30}$ have been proposed. Proxies, i.e., descriptors of site condition that can be readily obtained and that have some correlation to low-strain stiffness, which have been used for this purpose include (1) mapped surface geology (e.g., Wills and Clahan, 2006); (2) geotechnical site categories (sometimes called Geomatrix site classes, Chiou et al., 2008); (3) ground slope only (Wald and Allen, 2007); (4) surface geology in combination with ground slope (Thompson et al., 2014; Wills et al., 2015; Parker et al., 2017; Ahdi et al., 2017); and (5) geomorphic terrain categories that consider ground slope, surface roughness, and convexity (Yong et al., 2012; Yong, 2016). Ground slope correlations are based on the idea that the stiffness of geologic materials is positively correlated to their strength, and that materials comprising steeper slopes are generally stronger than materials found at flat sites. As an example of proxy-based estimation of $V_{S30}$, Table 6.10 shows recommended values for five geotechnical site classes, based on 441 $V_S$ profiles from California. Note that $V_{S30}$ carries a much larger uncertainty when estimated from proxies than when measured on-site ($\sigma_{\ln V_{S30}}$ from proxies generally exceed 0.3, whereas those from measurements are generally about 0.1). Seyhan et al. (2014) found the proxies based on surface geology with slope and geotechnical conditions to provide the best performance relative to data from California, Japan, and Taiwan. $V_{S30}$ has also been correlated to the fundamental mode Rayleigh wave phase velocity at a wavelength of 40 m, i.e., $V_{r40}$ (Brown et al., 2000; Martin and Diehl, 2004).

**TABLE 6.10** Estimates of the Mean and Natural Log Standard Deviation of $V_{S30}$ Using the Geotechnical Site Category Proxy of Chiou et al. (2008). Numerical values are for California data as compiled by Seyhan et al. (2014).

Site Category A — Rock, exposed at surface or < 5 m soil over rock: $\sigma_{\ln V_{S30}}$ = 0.41

Site Category B — Shallow (stiff) soil, profile thickness up to 20 m thick overlying rock: $\sigma_{\ln V_{S30}}$ = 0.43

Site Category C — Deep narrow soil, profile at least 20 m thick overlying rock, in a narrow canyon or valley no more than several km wide: $\sigma_{\ln V_{S30}}$ = 0.20

Site Category D — Deep broad soil, profile at least 20 m thick overlying rock, in a broad valley: $\sigma_{\ln V_{S30}}$ = 0.34

Site Category E — Soft deep soil, instrument on/in deep soil profile with average $V_s$ < 150 m/s: $\sigma_{\ln V_{S30}}$ = 0.25

$V_{S30}$ has also been correlated to the fundamental mode Rayleigh wave phase velocity at a wavelength of 40 m, i.e., $V_{r40}$ (Brown et al., 2000; Martin and Diehl, 2004).

#### 6.6.2.3 Other Factors

A number of additional factors can affect the measurement of low-strain stiffness, or its interpretation from available measurements. Evaluation of shear modulus can be complicated by rate and time effects (Anderson and Woods, 1975, 1976; Anderson and Stokoe, 1978; Isenhower and Stokoe, 1981).

**Rate Effects**

Rate effects can cause $G_{\max}$ to increase with increasing strain rate; consequently, $G_{\max}$ can increase with increasing frequency under cyclic loading. The influence of strain rate on $G_{\max}$ increases with increasing soil plasticity; for San Francisco Bay mud (PI ≈ 30–45), $G_{\max}$ increases about 4% per tenfold increase in strain rate. Rate effects can be significant when comparing $G_{\max}$ values obtained from field shear wave velocity measurements (usually made with the use of impulsive disturbances which produce relatively high frequencies) with values obtained from laboratory tests; suspension logging tests, for example, involve particularly high frequencies.

**Time Effects**

The shear wave velocity, and hence $G_{\max}$, increases approximately linearly with the logarithm of time past the end of primary consolidation to an extent that cannot be attributed solely to the effects of secondary compression. The change of stiffness with time can be described by

$$\Delta G_{\max} = N_G (G_{\max})_{1000} \tag{6.84}$$

where $\Delta G_{\max}$ is the increase in $G_{\max}$ over one log cycle of time and $(G_{\max})_{1000}$ is the value of $G_{\max}$ at a time of 1,000 minutes past the end of primary consolidation. $N_G$ increases with increasing plasticity index, PI, and decreases with increasing OCR (Kokushu et al., 1982). For normally consolidated clays, they found that $N_G$ can be estimated as

$$N_G \approx 0.027\, \text{PI} \tag{6.85}$$

where PI is in percent. Anderson and Woods (1975) showed that some of the discrepancy between $G_{\max}$ values from field and laboratory tests could be explained by time effects, and that $N_G$ could be used to correct the $G_{\max}$ values from laboratory tests to better represent actual in situ conditions.

**Anisotropy Effects**

Although usually treated as isotropic, low-strain stiffness (and shear wave velocity) can also be affected by soil anisotropy. Soils can exhibit inherent anisotropy, which is due to the depositional fabric or structure of the soil skeleton and exists even under isotropic stress conditions, and/or induced anisotropy, which results from anisotropy of the existing (or historical) stress state. For critical problems, soils can be modeled as cross-anisotropic, in which their behavior is described by five parameters (White, 1965) usually determined by laboratory testing on reconstituted specimens (e.g., Stokoe et al., 1991; Kuwano and Jardine, 2002; Lee and Stokoe, 1986; Bellotti et al., 1996).

**Summary**

A brief summary of the effects of environmental and loading conditions on the maximum shear modulus of normally and moderately overconsolidated soils is presented in Table 6.11.

**TABLE 6.11** Effect of Environmental and Loading Conditions on Maximum Shear Modulus of Normally Consolidated and Moderately Overconsolidated Soils. Source: After Dobry and Vucetic (1987).

Effective confining pressure, $\sigma'_m$: $G_{\max}$ increases with $\sigma'_m$
Void ratio, $e$: $G_{\max}$ increases with $e$
Geologic age, $t_g$: $G_{\max}$ increases with $t_g$
Cementation, $c$: $G_{\max}$ increases with $c$
Overconsolidation ratio, OCR: $G_{\max}$ increases with OCR
Plasticity index, PI: $G_{\max}$ increases with PI
Strain rate, $\dot{\gamma}$: No effect for nonplastic soils; increases with $\dot{\gamma}$ for plastic soils (up to ~10% increase per log cycle increase in $\dot{\gamma}$)
Number of loading cycles, $N$: Decreases after $N$ cycles of large $\gamma_c$, but recovers later in time in clays; increases with $N$ for sands.

### 6.6.3 Higher-Strain Stiffness

The secant and tangent shear moduli (Figure 6.12c) of an element of soil both vary with cyclic shear strain amplitude. At low strain amplitudes, both shear moduli are high, but decrease as strain amplitudes increase. As described in Section 6.6.1.2, the variable stiffness of an element of soil, therefore, can be characterized by its backbone curve (Equation 6.41) or by $G_{\max}$ and a modulus reduction curve. Since the secant modulus $G = \tau/\gamma$, a backbone curve can be constructed from a modulus reduction curve using Equation (6.75). Likewise, a modulus reduction curve can be obtained from a backbone curve as

$$\frac{G}{G_{\max}} = \frac{\tau}{\gamma\, G_{\max}} \tag{6.86}$$

While the nonlinear behavior of a soil can be characterized equally well by a backbone curve or $G_{\max}$ and a modulus reduction curve, the latter approach offers some advantages in terms of familiarity, isolation of significant factors, and direct use in certain types of response analyses (Chapter 7), and will therefore be emphasized in the remainder of this chapter. The shear strength of a typical soil, however, is mobilized at larger strains than those typically well constrained by modulus reduction curves (Section 6.6.1.2). Using Equation (6.86), the value of $G/G_{\max}$ when the shear strength, $\tau_{\max}$, has been mobilized is

$$\frac{G}{G_{\max}}\bigg|_{\tau_{\max}} = \frac{\tau_{\max}}{\gamma\, G_{\max}} \tag{6.87}$$

In order to produce shear stresses consistent with the shear strength at large strain levels, the modulus reduction curve should be transitioned to the strength-based modulus reduction curve of Equation (6.87) at higher strain levels. The transition may be more easily accomplished in terms of the backbone curve, and then converted back to equivalent modulus reduction curve ordinates at large shear strains, as described further below. Modulus reduction curves can, in principle, be measured in situ, measured from laboratory tests for site-specific soil materials, or derived from empirical correlations. In situ measurement of shear moduli at high strain levels is difficult and requires specialized equipment (Cox et al., 2009) that is not practical for routine projects. Higher strain dynamic soil properties are therefore measured in the laboratory, most commonly using resonant column testing. For critical projects, site-specific relations for modulus reduction as a function of shear strain may be obtained by a laboratory testing program (Section 6.6.3.1). In most cases, however, shear modulus behavior at higher strain levels is obtained through the use of empirical correlations to other, more easily measured soil properties that have been shown to affect modulus reduction behavior (Section 6.6.3.2). While the shear strains mobilized during weak shaking may be low enough that $G \approx G_{\max}$ (i.e., linear response), problems of interest usually involve larger strains at which soils exhibit nonlinear behavior. Figure 6.83a shows a two-parameter backbone curve that takes the form of a simple hyperbola. As given previously in Equation (6.41), this hyperbola is completely described by the limiting shear stress $\tau_{\max}$ (i.e., the nominal shear strength of the soil) and the initial shear modulus $G_{\max}$. It is convenient to re-write Equation (6.41) for positive shear strain as:

$$\tau = \frac{G_{\max}\,\gamma}{1 + \gamma/\gamma_{\text{ref}}} \tag{6.88}$$

where $\gamma_{\text{ref}} = \tau_{\max}/G_{\max}$ is referred to as the reference strain (Hardin and Drnevich, 1972a, 1972b). In this simple model, the reference strain is the shear strain at $\tau = \tau_{\max}/2$.
