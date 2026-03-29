$$\frac{G}{G_{\max}} = \frac{1}{1 + \gamma/\gamma_{\text{ref}}} \tag{6.89}$$

The degree of nonlinearity is therefore controlled by the reference strain and hence is influenced by the shear strength. However, a commonly encountered difficulty is that the shear strength that is mobilized at high strain levels is poorly correlated to the small strain soil behavior that controls modulus reduction curve values at strain levels of common engineering interest (about 0.1%–1.0%). The modeling of modulus reduction behavior can be significantly improved by the use of a three-parameter modified hyperbolic backbone curve as

$$\tau = \frac{G_{\max}\,\gamma}{1 + (\gamma/\gamma_r)^a} \tag{6.90}$$

where $\gamma_r$ is a pseudo-reference strain defined as the strain at which $G/G_{\max} = 0.5$ and $a$ is an additional fitting parameter that influences the curvature of the backbone curve. This relationship produces modulus reduction curves of the form

$$\frac{G}{G_{\max}} = \frac{1}{1 + (\gamma/\gamma_r)^a} \tag{6.91}$$

Figure 6.87 shows that pseudo-reference strain is the dominant parameter controlling the modulus reduction curves; as $\gamma_r$ increases, the curves shift to the right, which models the soil behavior as being more linear. Figure 6.88 shows that the exponent $a$ controls the slope of the modulus reduction curve, and hence how rapidly the stiffness of the soil decreases once yielding begins; for example, at $\gamma = \gamma_r$, increases in $a$ increase the slope of the modulus reduction curve. The plots in Figures 6.87 and 6.88 also show the effect of $\gamma_r$ and $a$ on the large-strain behavior implied by the form of the modified hyperbolic function. Increases in $\gamma_r$ and decreases in $a$ lead to higher shear stresses at large strains. The shear strengths implied by modified hyperbolic model (Equation 6.90) parameters that match the low-strain (less than ~1%) behavior are typically inconsistent with the strengths measured at large strains in laboratory tests. Put another way, just as the small-strain portion of the backbone curve was poorly represented by strength-based reference strain, $\gamma_{\text{ref}}$, large strain behavior tends to be poorly represented by the modified hyperbolic model. In short, classical hyperbolic models of the sort in Equations (6.88) and (6.90), although quite simple, have a limited ability to model observed laboratory behavior of soils over wide ranges of shear strain. Procedures for adjusting modulus reduction and backbone curves for consistency with large strain (e.g., shear strength) behavior are described in Section 6.6.3.3.

**FIGURE 6.87** Influence of pseudo-reference strain, $\gamma_r$, on (a) modulus reduction curve, and (b) backbone curve.

**FIGURE 6.88** Influence of exponent, $a$, on (a) modulus reduction curve and (b) backbone curve.

### 6.6.3.1 Direct Laboratory Measurement

Laboratory shear moduli can be measured over a wide range of shear strain amplitudes using resonant column and torsional shear devices. The basic testing procedure, in which strain amplitudes begin at very low values and increase to high values, was described in Sections 6.5.4.2 and 6.5.4.3. The results of such a test can be described in terms of a laboratory modulus curve that shows the variation of secant shear modulus with cyclic strain amplitude. For soils, the low-strain laboratory shear modulus, $G_{\max,\text{lab}}$, will generally be lower than the maximum shear modulus, $G_{\max,\text{field}}$, obtained from field shear wave velocity measurements [@AndersonWoods1975] using Equation (6.76), with differences increasing with increasing stiffness, decreasing plasticity, and increasing depth [@ChiaraStokoe2006]. For the case of clays sampled using relatively high-quality samplers, these differences have been postulated to result from pseudo-overconsolidation from secondary compression [@TrudeauEtAl1974], which is lost in sampling. Because field measurements of low-strain stiffness are more accurate than laboratory measurements, laboratory secant shear moduli should be corrected as

$$G(\gamma)_{\text{field}} = C_r \cdot G_{\max,\text{field}} \cdot \frac{G(\gamma)_{\text{lab}}}{G_{\max,\text{lab}}} \tag{6.92}$$

In practice, the quantity $C_r$ is frequently taken to be 1.0, which means that the modulus values are simply scaled upward by a constant factor at all strain levels; the laboratory modulus reduction curve itself remains unchanged. Carlton and Pestana (2016) [@CarltonPestana2016] found that $G_{\max,\text{field}}$ could be related to $G_{\max,\text{lab}}$ as

$$\ln G_{\max,\text{field}} = 1.10\,\ln G_{\max,\text{lab}} - 0.78 \tag{6.93}$$

with $\sigma_{\ln G_{\max,\text{field}}} = 0.36$. Ishihara (1996) [@Ishihara1996] proposed, on the basis of cyclic tests performed on specimens obtained by different sampling methods including ground freezing, that $C_r$ should vary with strain amplitude and the type of sampling (Figure 6.89). This approach implies a correction to the shape of the modulus reduction curve as well as to $G_{\max}$.

**FIGURE 6.89** Strain-dependent correction factor for field shear moduli. (After Ishihara, 1996; used with permission of Oxford University Press.)

### 6.6.3.2 Empirical Correlations

Resonant column and direct simple shear tests have been performed on many soils with different grain size characteristics, plasticity characteristics, stress histories, etc. Systematic interpretation of these tests has revealed the soil parameters that most strongly affect shear modulus reduction behavior. These results can be expressed in terms of modulus reduction or backbone curves of a general form described by parameters that are more readily measured than the shear moduli themselves. This approach can be used to estimate shear modulus reduction behavior for typical soils, or classes of soils. In the early years of geotechnical earthquake engineering, the modulus reduction behaviors of coarse- and fine-grained soils were treated separately, and modulus reduction and damping curves were made available for broad soil classes such as sand and clay (e.g., Seed and Idriss, 1970) [@SeedIdriss1970]. Later research, however, revealed a gradual transition between the modulus reduction behavior of non-plastic coarse-grained soil and plastic fine-grained soil. Zen et al. (1978) [@ZenEtAl1978] and Kokushu et al. (1982) [@KokushuEtAl1982] first noted the influence of soil plasticity on the shape of the modulus reduction curve; the shear modulus of highly plastic soils was observed to reduce more slowly with shear strain than did low-plasticity soils. After reviewing experimental results from a broad range of materials following the 1985 Mexico City earthquake, in which highly linear response was measured in the very plastic (PI ≈ 200) Mexico City clay, Dobry and Vucetic (1987) [@DobryVucetic1987] and Sun et al. (1988) [@SunEtAl1988] concluded that the shape of the modulus reduction curve was strongly influenced by the plasticity index of the soil. PI-dependent modulus reduction curves proposed by Vucetic and Dobry (1991) [@VuceticDobry1991] are shown in Figure 6.90. Modulus reduction behavior has also been found to be influenced by effective confining pressure, particularly for soils of low plasticity [@IwasakiEtAl1978][@Kokoshu1980][@IshibashiZhang1993]. The Electric Power Research Institute sponsored an investigation of the dynamic properties of soils of unspecified plasticity [@EPRI1993] that verified the effects of effective confining pressure on nonlinearity and presented modulus reduction curves in terms of different depth ranges (Figure 6.91). The EPRI curves are based on laboratory testing and comparisons of site response simulations to recorded ground motions.

**FIGURE 6.90** Modulus reduction curves of Vucetic and Dobry (1991).

**FIGURE 6.91** Depth-dependent modulus reduction curves of EPRI (1993); used with permission of EPRI.

Darendeli (2001) [@Darendeli2001] supplemented multiple sets of published data with additional resonant column and torsional shear tests on soil samples from multiple sites in California, South Carolina, and Taiwan to develop a database that covers a wide range of soil types, depths, densities, plasticity characteristics, and stress histories. The modified hyperbolic model (Equation 6.91) was found to fit the experimental results well with

$$\gamma_r(\%) = \bigl(0.0352 + 0.0010\,\mathrm{PI}\bigr) \cdot \mathrm{OCR}^{0.3246} \cdot \left(\frac{\sigma'_m}{p_a}\right)^{0.3483} \tag{6.94a}$$

$$a = 0.92 \tag{6.94b}$$

where $\gamma_r$ is expressed in %, $\sigma'_m$ is the mean effective stress prior to the onset of cyclic loading in the same units as $p_a$, $p_a$ is atmospheric pressure, and PI is in %. Because increasing $\gamma_r$ indicates increasing soil linearity, the degree of linearity can be seen to increase with increasing PI, OCR, and $\sigma'_m$. Figure 6.92 shows modulus reduction behavior for different ranges of PI and $\sigma'_m$. For cohesionless soils, the Darendeli model has been superseded by a similarly formulated modified hyperbolic model by Menq (2003) [@Menq2003], as described further below. The relationship of Equation (6.94) applies to cyclic shear strain amplitudes up to 0.5%, which is the approximate upper bound of the range of strains used in the laboratory testing from which the data was derived. As discussed in Section 6.4.4.2, pore pressure generation and structural changes can cause the shear strain amplitude of a soil specimen to increase with increasing number of cycles of stress-controlled harmonic loading. For cohesive soils, the value of the shear modulus after $N$ cycles, $G_N$, can be related to its value in the first cycle, $G_1$, by the degradation index, $\delta$ (Equation 6.37). The effects of stiffness degradation on modulus reduction behavior are shown in Figure 6.93. Note that no degradation is predicted for clays with PI ≥ 100.

**Cohesionless Soils** Tests of a number of coarse sandy ($D_{50}$ greater than about 0.3 mm) and gravelly soils [@Menq2003] showed that their modulus reduction behavior could be characterized by the modified hyperbolic model (Equation 6.91) with

$$\gamma_r(\%) = 0.12\,C_u^{-0.6} \left(\frac{\sigma'_v}{p_a}\right)^{0.5\,C_u^{-0.15}} \tag{6.95a}$$

**FIGURE 6.92** Modulus reduction curves using modified hyperbolic model of Equation (6.94) with coefficient set by models of Darendeli (2001): (a) effects of PI at low vertical effective stress, and (b) effects of vertical effective stress for nonplastic soil.

**FIGURE 6.93** Effect of cyclic degradation on shear modulus. (After Vucetic and Dobry, 1989; used with permission of ASCE.)

$$a = 0.86 + 0.1\log(\sigma'_v/p_a) \tag{6.95b}$$

where $C_u$ = coefficient of uniformity, $\sigma'_v$ = initial vertical effective stress, and $p_a$ = atmospheric pressure in the same units as $\sigma'_v$. Note that soil nonlinearity in this model is unrelated to grain size ($D_{50}$), but decreases with increasing effective stress and increases with increasing $C_u$. Earlier work had found an effect of grain size, with coarser soils such as gravels being more linear (i.e., higher $\gamma_r$) than those for sands [@SeedEtAl1986][@YasudaMatsumoto1993][@RollinsEtAl1998]. Figure 6.94 illustrates the influence of coefficient of uniformity and initial effective stress on modulus reduction behavior.

**Organic Soils** A number of investigations of modulus reduction behavior for highly organic soils and peats have been performed [@SeedIdriss1970][@StokoeEtAl1994][@BoulangerEtAl1998][@Kramer2000][@WehlingEtAl2003][@TokimatsuSekiguchi2007][@KishidaEtAl2009a]. As shown in Figure 6.95, a compilation of results from several of these studies shows a very wide range of modulus reduction curves, with effective stress having a major effect on the degree of nonlinearity. Kishida et al. (2009b) [@KishidaEtAl2009b] combined data from several laboratory investigations to develop a regression model that predicts secant shear modulus as a function of cyclic strain amplitude, $\gamma_c$, initial vertical effective stress $\sigma'_v$, organic content, OC, and a laboratory consolidation ratio, LCR, defined as the in situ $\sigma'_v$ divided by the vertical effective stress in the laboratory. Figure 6.96 shows the influence of organic content and effective stress on modulus reduction curves at a particular vertical effective stress level along with curves for high plasticity clay. Soil linearity was observed to increase with increasing organic content, similar to the effect of PI for clays, but the effect of increasing effective stress was much smaller than was observed in prior studies. Whereas modulus reduction models for sands and clays are now considered fairly well established, the current state of knowledge for peat remains somewhat in flux, especially with regard to the effect of effective stress.

**FIGURE 6.94** Modulus reduction curves of Menq (2003): (a) variation with $\sigma'_{v0}$ for given $C_u = 5$ and (b) variation with $C_u$ for $\sigma'_{v0} = 1$ atm.

**Municipal Solid Waste** In some locations, large deposits of human-derived materials such as municipal solid waste (MSW) may require the attention of geotechnical earthquake engineers. MSW can consist of many different types of materials, a number of which are so large or fibrous as to complicate their testing in the laboratory. Laboratory testing of MSW materials has generally involved the use of large-scale testing equipment [@MatasovicEtAl1998][@TowhataEtAl2004][@ZekkosEtAl2008a][@ZekkosEtAl2008b][@TowhataUno2008] and/or scalped test specimens [@AthanasopoulosZekkos2008]. These tests have shown that waste composition is important, and that composition can be at least approximately characterized by the amount of fibrous material (i.e., paper, plastic, and wood longer than 20 mm) they contain. Due to the difficulty of testing such materials, a number of investigators [@MatasovicEtAl1995][@IdrissEtAl1995][@AugelloEtAl1998][@MatasovicKavazanjian1998][@ElgamalEtAl2004] have attempted to back-calculate modulus reduction curves from the recorded response of MSW landfills. Zekkos et al. (2008a) [@ZekkosEtAl2008a] proposed the generalized modulus reduction curves for MSW shown in Figure 6.97, which is based on limited available laboratory data. MSW can be seen to exhibit more linear behavior with increasing fractions of fibrous (> 20 mm) material and with increasing effective stress.

**FIGURE 6.95** Laboratory test results for peats and organic soils showing strong effect of vertical effective stress prior to onset of cyclic loading, $\sigma'_{v0}$. (From Wehling et al., 2003; used with permission of ASCE.)

**FIGURE 6.96** Modulus reduction behavior for organic soils from Kishida et al. (2009b) showing (a) effect of organic content, with clay curves of Vucetic and Dobry (1991) included for reference and (b) effect of effective stress at 65% organic content. (After Kishida et al., 2009b; used with permission of ASCE.)

**FIGURE 6.97** Generalized modulus reduction curves for MSW of different compositions (a) for mean confining stress less than 125 kPa and (b) for higher confining stresses for MSW with 62%–76% fibrous material < 20 mm. (After Zekkos et al., 2008a; used with permission of Canadian Science Publishing.)

### 6.6.3.3 Strength Considerations

As indicated in Section 6.6.1.2, a backbone curve can be computed from $G_{\max}$ and a modulus reduction curve. Since resonant column tests are usually limited to shear strains up to about 0.5%–1% (e.g., the Darendeli 2001 model is based on a data set with upper bound strains of about 0.5%), some degree of extrapolation is required if larger strain levels are expected to be induced in the soil. In some cases, this extrapolation is accomplished by selecting some analytical form, such as the modified hyperbola (Equation 6.91), for the backbone or modulus reduction curve. The extrapolation may imply shearing resistances that are significantly lower or significantly greater than the actual strength of the soil. While the effects of alternate representations of large-strain behavior are often nearly invisible in modulus reduction curves (e.g., see Figure 6.88a for $\gamma_c > 1\%$), they can be obvious in the corresponding backbone curves (Figure 6.88b for $\gamma_c > 1\%$). These considerations are important under strong shaking conditions because the high strain portion of the curve influences the level of shear stress induced in the soil, which in turn affects ground motion characteristics [@YeeEtAl2013]. To overcome this problem, it is possible to apply a hybrid approach in which a suitable low-strain model is used up to a limiting strain level, $\gamma_1$, and larger strain behavior is then captured using a classical hyperbolic model that is asymptotic to the actual shear strength. The classical hyperbolic model has its origin at $(\tau_1, \gamma_1)$ with an initial stiffness (i.e., at $\gamma = \gamma_1$) equal to the tangent of the backbone curve at that point. If the low-strain behavior is described by a modified hyperbolic backbone curve (Equation 6.91), the modulus reduction curve for strains $\gamma > \gamma_1$ can then be expressed as [@YeeEtAl2013]:

$$\frac{G}{G_{\max}} = \frac{\displaystyle\frac{G_{\gamma_1}}{G_{\max}} \cdot \frac{(\gamma - \gamma_1)/\gamma'_{\text{ref}}}{1 + (\gamma - \gamma_1)/\gamma'_{\text{ref}}} + \frac{G_{\gamma_1}}{G_{\max}} \cdot \frac{(\gamma/\gamma_r)^a}{1 + (\gamma/\gamma_r)^a}}{\gamma/\gamma_{\max}} \tag{6.96}$$

where $\gamma_r$ and $a$ are the parameters used in the modified hyperbolic model, $G_{\gamma_1}$ is the secant shear modulus at $\gamma = \gamma_1$. The modulus reduction ratio at $\gamma = \gamma_1$ is given by

$$\frac{G_{\gamma_1}}{G_{\max}} = \frac{a(\gamma_1/\gamma_r)^{a-1}(1-a) + a}{(1 + (\gamma_1/\gamma_r)^a)^2} \tag{6.97}$$

This approach results in a smooth and continuous, two-part backbone curve (Figure 6.98) and modulus reduction curve. As an alternative to the modified hyperbola approach, Groholski et al. (2016) [@GroholskiEtAl2016] approximated small- and large-strain behavior using a quadratic equation to approximately fit both the modulus reduction curve at small strains and a target shear strength at large strains, while Yniesta and Brandenberg (2017) [@YniestaBrandenberg2017] developed a procedure that allows for any user-defined backbone curve shape.

**FIGURE 6.98** Backbone curve controlled by modulus reduction behavior at low strains and hyperbola asymptotic to shear strength at large strains.

### 6.6.3.4 Uncertainty in Modulus Reduction Ratio

Darendeli (2001) [@Darendeli2001] characterized the dispersion in the data from which his modulus reduction model was developed. Assuming a normal distribution for the modulus reduction ratio at a particular strain level, the standard deviation of that ratio was expressed as

$$\sigma_{G/G_{\max}} = 0.015 + 0.16\,(G/G_{\max})^{0.25}(1 - G/G_{\max})^{0.5} \tag{6.98}$$

This value reaches its maximum of 0.095 at $G/G_{\max} = 0.5$ and tapers down to values of 0.015 at $G/G_{\max} = 1.0$ and 0.0. Zhang et al. (2008) [@ZhangEtAl2008] used a point estimation [@Rosenblueth1975][@Harr1987] technique to propagate uncertainties in reference strain and curvature parameter through a modified hyperbolic model (Equation 6.91) for three different geologic groups (Quaternary, Tertiary and older, and residual (saprolite) soils). The resulting uncertainties varied with soil type, shear strain amplitude, and soil plasticity and had peak values ranging from about 0.13 to 0.31.

### 6.6.4 Damping

A number of phenomena can cause the amplitude of a wave to decrease as it travels through a material and the term "damping" is often used to describe these phenomena. It is important to recognize, however, that the mechanisms of these phenomena are different, and that those differences may cause the effects of the phenomena to be affected by different factors. Geometric spreading (Sections 3.4.2.1 and C.5.2) produces attenuation as a result of energy spreading out in space and is not affected by material properties or frequency. Wave scattering (Section C.5.3) is affected by material properties and increases with increasing frequency. Material damping, the subject of this section, results from inelastic material behavior and, for most soils, is independent of frequency. Most practical problems will involve more than one form of damping or attenuation, hence any single damping formulation will seldom be useful in isolation. While some attempts at field measurement of soil damping have been made [@HenkeHenke1991][@RiemerCobosRoa2007], none have yet been proven sufficiently reliable to be used for design purposes. As a result, material damping behavior is generally obtained from laboratory tests.

### 6.6.4.1 Low-Strain Damping

At low strain levels ($\gamma < 0.001\%$), soils exhibit generally linear elastic behavior, which implies no energy dissipation. Experiments have shown, however, that cyclic loading does dissipate some energy, even though the mechanism(s) of dissipation is not always clear. The material damping at these low strains is referred to as a minimum damping ratio, $\xi_{\min}$. Like the low-strain shear modulus $G_{\max}$, the minimum damping ratio is affected by effective confining pressure, plasticity index, overconsolidation ratio, and frequency. In general, $\xi_{\min}$ increases with decreasing effective confining pressure, increasing plasticity index, decreasing overconsolidation ratio, and increasing loading frequency. Based on resonant column test data, Darendeli (2001) [@Darendeli2001] proposed that $\xi_{\min}$ be estimated as

$$\xi_{\min} = \bigl(0.8005 + 0.0129\,\mathrm{PI}\cdot\mathrm{OCR}^{-0.1069}\bigr)\cdot\left(\frac{\sigma'_m}{p_a}\right)^{-0.2889} \cdot (1 + 0.2919\ln f) \tag{6.99}$$

Figure 6.99 shows the variation of $\xi_{\min}$ with effective confining pressure and plasticity index for normally consolidated soils loaded at a frequency of 1 Hz. Note that the low-strain damping ratios at a given effective confining pressure are higher for high PI than low PI values. Menq (2003) [@Menq2003] found that the minimum damping ratio for dry coarse-grained soils was primarily affected by grain size distribution and effective stress level, and could be estimated as

$$\xi_{\min} = 0.55\,C_u^{-0.1}\,D_{50}^{0.3}\,(\sigma'_v/p_a)^{-0.08} \tag{6.100}$$

Values of $\xi_{\min}$ were noted as potentially increasing "several fold" as water is added to the soil, but quantitative values were not presented.

**FIGURE 6.99** Variation of low-strain damping ratio with plasticity index and mean effective stress. (After Darendeli, 2001.)

Several studies of site response using weak motion data from vertical arrays [@ElgamalEtAl2001][@TsaiHashash2009][@YeeEtAl2013][@CabasEtAl2017][@AfshariStewart2019][@TaoRathje2019] have found that the small-strain damping mobilized under field conditions exceeds that from laboratory-based material damping models such as those by Darendeli (2001) [@Darendeli2001] and Menq (2003) [@Menq2003]. This additional damping is thought to arise from wave scattering phenomena, which are present under field conditions but not in small-scale laboratory tests. While small strain damping ratios of about 5% have been found to be effective in some of this prior work, it has not yet been possible to develop general recommendations for how (or if) to modify $\xi_{\min}$ predictions from models of the type discussed in this section to better match field data. Scattering effects are discussed in more detail in Section 7.5.6.2.

### 6.6.4.2 Higher-Strain Damping

Damping ratios at higher strain levels result from inelasticity and are also affected by soil plasticity and effective stress level. Factors that tend to increase linearity, such as increased plasticity and increased effective stress level, lead to reduced damping ratios. Mirroring the trends observed for modulus reduction, damping ratio has been observed (Figure 6.100) to decrease substantially with increasing plasticity index at a particular strain level [@SunEtAl1988][@VuceticDobry1991]. Others have shown (Figure 6.101) that damping ratio also decreases with increasing initial vertical effective stress or increasing depth [@IshibashiZhang1993][@EPRI1993]. Under harmonic loading conditions, stress-strain behavior is frequently modeled using the Masing rules (Section 6.4.5.2) in which the shapes of the unloading and reloading curves are scaled versions of the backbone curve. A scale factor of 2.0 (Equation 6.42) produces closed hysteresis loops for symmetric loading. The shape of the hysteresis loop, and consequently the damping ratio, is controlled by the shape of the backbone curve. For the simple hyperbolic model of Equation (6.88), which is equivalent to the modified hyperbolic model of Equation (6.90) with $a = 1$, the area of the hysteresis loop is given by

$$A_{\text{loop}} = \int_0^{\gamma} \tau\, d\gamma - \tau\gamma \tag{6.101}$$

**FIGURE 6.100** Variation of damping ratio with cyclic shear strain and plasticity index. (After Vucetic and Dobry, 1991; used with permission of ASCE.)

**FIGURE 6.101** Variation of damping ratio with cyclic shear strain and depth. (After EPRI, 1993; used with permission of the Electric Power Research Institute.)

Using Equation (B.72), the corresponding damping ratio can be shown [@Ishihara1996] to be

$$\xi_{M,\gamma}(\%) = \frac{100}{\pi} \cdot 4\left[\frac{\gamma_r}{\gamma}\left(1 + \frac{\gamma_r}{\gamma}\right)\ln\left(\frac{\gamma_r}{\gamma} + 1\right) - 1\right] \tag{6.102}$$

The Masing damping ratio, which is a function of pseudo-reference strain as shown by Equation (6.102), is often taken as a reference level in models for strain-dependent damping. Larger values of $\gamma_r$, which have been shown (Section 6.6.3) to produce higher $G/G_{\max}$ values (i.e., more linear response), also produce lower damping ratios. For $a \neq 1$, the integral in Equation (6.101) cannot generally be solved analytically, but can be approximated by numerical integration resulting in

$$\xi(\%) = c_1\,\xi_{\text{Masing},a} + c_2\,\xi^2_{\text{Masing},a} + c_3\,\xi^3_{\text{Masing},a} \tag{6.103}$$

where $c_1 = 0.2523 + 1.8618a - 1.1143a^2$, $c_2 = -0.0095 - 0.0710a + 0.0805a^2$, and $c_3 = 0.0003 + 0.0002a - 0.0005a^2$. For the value of $a = 0.92$ obtained by Darendeli (2001) [@Darendeli2001],

$$\xi(\%) = 1.0213\,\xi_{\text{Masing},a} - 0.0067\,\xi^2_{\text{Masing},a} + 0.000061\,\xi^3_{\text{Masing},a} \tag{6.104}$$

Darendeli (2001) [@Darendeli2001] proposed that the total damping ratio could be expressed as

$$\xi = \xi_{\min} + \xi_{\text{Masing}}\left(0.6329 - 0.0057\ln N\right)\left(\frac{G}{G_{\max}}\right)^{0.1} \tag{6.105}$$

where $G/G_{\max}$ is obtained from Equation (6.91) with $\gamma_r$ and $a$ given by Equations (6.94), and $N$ = number of loading cycles. The total damping ratio curves of Darendeli (2001) are illustrated in Figures 6.102 and 6.103. Factors that tend to cause more linear behavior (higher $G/G_{\max}$ values), e.g., increasing PI and/or effective stress level, lead to lower damping ratios. At low strain levels, however, the trend is reversed with higher plasticities leading to higher damping ratios. Thus, the damping ratio curves for different PI values tend to cross each other at low to intermediate strain levels. Menq (2003) [@Menq2003] found that the higher-strain damping of coarse-grained soils was accurately represented by the relationship of Darendeli (2001) and suggested that the Darendeli relationship for $\xi - \xi_{\min}$ be added to the Menq (2003) expressions for $\xi_{\min}$ (Equation 6.100) to obtain the total damping.

**Organic Soils** As shown in Figure 6.104, testing of a variety of peats and organic soils has revealed a wide range of damping ratios, with initial effective stress (and potentially age) being controlling parameters. Figure 6.105 shows predictions of a damping model by Kishida et al. (2009b) [@KishidaEtAl2009b], that provides estimates of damping curves based on $\sigma'_{v0}$ and organic content, OC. As was the case with modulus reduction behavior, the effect of $\sigma'_{v0}$ is low, in contrast with other test data. Note that the low-strain damping $\xi_{\min}$ is higher, at approximately 3%, than values for most inorganic soils.

**Municipal Solid Waste** The damping behavior of MSW has been shown, like modulus reduction behavior, to be influenced by waste composition and, to a lesser degree, effective stress level. Figure 6.106 illustrates the effects of these parameters on damping ratio. Note that the low-strain damping ratios are quite high relative to those of inorganic soils.

**FIGURE 6.102** Variation of damping ratio with cyclic shear strain and plasticity index for soil at $\sigma'_m = 25$ kPa according to Darendeli (2001).

**FIGURE 6.103** Variation of damping ratio of nonplastic soil with cyclic shear strain and initial vertical effective stress according to Darendeli (2001).

### 6.6.4.3 Uncertainty in Damping Ratio

Darendeli (2001) [@Darendeli2001] characterized uncertainty in damping ratio and its relationship to uncertainty in modulus reduction ratio. Assuming damping ratio to be lognormally distributed, Darendeli proposed that

$$\sigma_{\ln\xi} = 0.0067 + 0.78\,\xi \tag{6.106}$$

**FIGURE 6.104** Damping ratio for peat and organic soils as identified from a variety of material-specific tests at various initial confining effective stresses. (After Wehling et al., 2003; used with permission of ASCE.)

**FIGURE 6.105** Damping ratio for organic soils from Kishida et al. (2009b) compared with that of inorganic soils according to Vucetic and Dobry (1991); used with permission of ASCE.

where $\xi$ is the mean damping ratio from Equation (6.105). Because $\xi$ increases with shear strain amplitude, so too does its uncertainty as given by Equation (6.106). Zhang et al. (2008) [@ZhangEtAl2008] used point estimation procedures to estimate uncertainties in damping ratio as a function of soil type, shear strain amplitude, and soil plasticity with maximum standard deviation values ranging from about 2.5% to 7%. Because increasing linearity corresponds to decreasing damping, the modulus reduction ratio and damping ratio should be negatively correlated to each other, i.e., an above average modulus reduction ratio should correspond to a below average damping ratio. Kottke and Rathje (2008) [@KottkeRathje2008] recommend using a correlation coefficient

$$\rho_{\xi,\,G/G_{\max}} = -0.5 \tag{6.107}$$

Procedures for generating pairs of correlated random variables, which can be used to generate negatively correlated modulus reduction and damping curves to be used in randomized site response analyses of the types discussed in Section 7.5.7, are presented in Section D.9.3.3. Figure 6.107 shows examples of simulated modulus reduction and damping curves.

**FIGURE 6.106** Generalized damping curves for MSW of different compositions (a) for mean confining stress less than 125 kPa and (b) for higher confining stresses for MSW with 62–76% fibrous material < 20 mm. (After Zekkos et al., 2008a; used with permission of Canadian Science Publishing.)

**FIGURE 6.107** (a and b) 20 randomized sets of modulus reduction and damping curves for soil with PI = 30 and $\sigma'_{v0}$ = 100 kPa using the procedure of Darendeli (2001).

### 6.6.5 Volume Change Behavior

The degree to which a soil tends to contract or dilate when sheared is important in many geotechnical earthquake engineering applications – indeed, it controls the behavior of soils that are susceptible to liquefaction (Chapter 9). Therefore, the characterization of that tendency is extremely important. As discussed in Section 6.4.4.4, all dry or partially saturated sands, whether loose or dense, will initially contract when sheared. Loose sands will continue to contract as strain levels increase, but dense sands will begin to dilate at larger strains so the states of both will move (by contraction for the loose sand and dilation for the dense one) to the steady state under monotonically increasing shear stress. Under cyclic loading inducing low to moderate strain amplitudes, however, both loose and dense sands continue to contract and can cross or move away from the steady state line (SSL). If sheared monotonically after cyclic shearing, however, all but the very loosest will dilate back toward the steady state.

As described in Section 6.4.4.4, the contractive volumetric strain that develops when dry or partially saturated sands are cyclically sheared is known as seismic compression. If the soil were saturated and sheared under undrained conditions, no volume change would occur, but the tendency for volume change would cause changes in pore pressure. The pore pressure change is positive when the soil responds in a contractive manner. Both soils initially above and below the SSL (i.e., having positive or negative values of state parameter, $\Psi$ or relative state parameter index, $\xi_R$) contract over some range of shear strain. If saturated, no volume change can occur, and both will generate positive pore pressure over the limited range of strain often induced by seismic loading. Due to the important effects of soil dilatancy on the response of both saturated and unsaturated soils, geotechnical engineers have long sought to characterize this aspect of soil behavior. While relative density has historically been used, volume change behavior is known to be more closely related to metrics of soil state relative to the steady state line (SSL), including the state parameter and relative state parameter index (Section 6.4.3.6). Because the in situ density and position of the steady state line for coarse-grained soils are difficult to measure, procedures for estimation of state parameter and relative state parameter index have focused on their correlation to more easily measured in situ penetration test results. A number of procedures for estimating these metrics from penetration test results are available.

### 6.6.5.1 Estimation of Relative Density

Relative density, $D_r$ (Equation 6.31), has historically been used as an indication of the state of a granular soil, but it is an incomplete indicator because it does not account for effective stress level, which affects volume change tendency. Nevertheless, a number of predictive models make use of relative density and correlations of relative density to parameters that can be measured in the field allow comparison of laboratory and field data. Correlations of relative density to SPT resistance going back to the work of Meyerhof (1957) [@Meyerhof1957] have generally been expressed in the form

$$D_r^2 = \frac{N}{C_d} \tag{6.108}$$

where $N$ and $C_d$ have taken various forms. Meyerhof (1957) [@Meyerhof1957] proposed the use of Equation (6.108) with $N$ taken as the measured SPT resistance without overburden correction, $N_m$, and $C_d = 24(1 + \sigma'_v/P_a)$. Skempton (1986) [@Skempton1986] recommended that Equation (6.108) be used with

$$N_{1,60} = N_m \cdot \frac{\mathrm{ER}/60}{1 + \sigma'_v/100} \quad \text{for fine sand} \tag{6.109a}$$

$$N_{1,60} = N_m \cdot \frac{\mathrm{ER}/60}{1 + \sigma'_v/100} \quad \text{for coarse sand} \tag{6.109b}$$

where ER = energy ratio (in percent), $\sigma'_v$ = initial vertical effective stress in kPa, and $C_d \approx 60$ for natural soils (age > 100 years), $C_d \approx 40$ for recent fills (age ~10 years), and $C_d \approx 35$ for laboratory tests (age ~0.01 years).

Cubrinovski and Ishihara (1999) [@CubrinovskiIshihara1999] proposed that Equation (6.109) could be used with $N = (N_1)_{60}$ and

$$C_d = \frac{6.923}{(e_{\max} - e_{\min})^{1.7}} \tag{6.110}$$

For cases where minimum and maximum void ratios cannot be measured, Cubrinovski and Ishihara (1999) [@CubrinovskiIshihara1999] suggested that the void ratio range be estimated as $e_{\max} - e_{\min} \approx 0.23 + 0.06/D_{50}$ and listed approximate $e_{\max} - e_{\min}$ values of 0.625 for sand with fines (FC ~ 20%), 0.41 for clean sand, and 0.30 for gravelly sand/coarse sand. Idriss and Boulanger (2007) [@IdrissEBoulanger2007] considered the data presented by Cubrinovski and Ishihara (1999) and judged that a value of $C_d = 46$, which would correspond to $D_r = 81\%$ for $N = (N_1)_{60} \approx 30$, was reasonable for clean sand (at depths consistent with observations of liquefaction) at $\sigma'_v = 100$ kPa. Idriss and Boulanger (2007) [@IdrissEBoulanger2007] also proposed that relative density could be estimated from CPT tip resistance as

$$D_r = 0.478\,q_{c1N}^{0.264} - 1.063 \tag{6.111}$$

where $q_{c1N}$ is the dimensionless, overburden-normalized tip resistance given in Equation (9.19).

### 6.6.5.2 Estimation of State Parameter

Measurement of the state parameter, defined in Equation (6.32) as $\psi = e - e_{ss}$, might seem, at first glance, to be relatively straightforward – one would obtain undisturbed samples of the soil from which (1) in situ void ratio would be determined and (2) shear test results would be used to determine the position of the SSL. In reality, however, direct measurement of the state parameter is extremely difficult – the successful retrieval of samples of cohesionless soils from below the water table is difficult, and the act of sampling usually changes the density of such soils. Furthermore, the position of the SSL is not easily measured in the laboratory since the steady state is reached at strain levels above that which can be reliably measured in most laboratory tests. As a result of these factors, state parameter is usually estimated by correlation to CPT or SPT resistance. A strong advantage of the CPT for this application is that cavity expansion theory can be used to provide a mechanics-based interpretation of its measurements. CPT tip resistance can be expressed in different ways, but is usually made dimensionless by normalizing with respect to some measure of effective stress. Letting

$$Q_p = \frac{q_t - p_0}{p'_0} \tag{6.112}$$

where $q_t$ = tip resistance after correction for unequal area effect, $p_0$ = mean total stress, and $p'_0$ = mean effective stress. Then, for level-ground conditions, $Q_p$ can be related to the normalized tip resistance based on vertical effective stresses,

$$Q_p \approx \frac{Q_t}{1 + K_0} \tag{6.113}$$

where $K_0$ is the at-rest earth pressure coefficient under level-ground conditions (assuming $\sigma'_v = \sigma'_h / K_0$ and $\sigma'_m = \sigma'_v(1+2K_0)/3$) and the approximation results from lack of consideration of the difference between total mean stress and total vertical stress. Been and Jefferies (1992) [@BeenJefferies1992] found that cavity expansion theory predictions of CPT resistance could be well approximated by the simple relationship

$$Q_p = k(1 - B_q)\exp(-m\psi) \tag{6.114}$$

where $k$ and $m$ are sand-specific functions of the rigidity of the soil and $B_q$ is defined in Equation (6.56). Solving for the state parameter,

$$\psi = -\frac{1}{m}\ln\left(\frac{Q_p}{k(1-B_q)}\right) \tag{6.115}$$

Using calibration chamber test results, Been and Jefferies (1992) [@BeenJefferies1992] related rigidity to the soil classification index $I_c^{BJ}$ as defined in Equation (6.59). The soil classification index can be used to compute

$$k = 34 - (I_c^{BJ} - 0.85)^{34} \tag{6.116}$$

$$m = 34 - 13.3\,(I_c^{BJ} - 11.9/34) \tag{6.117}$$

where

$$M = \frac{(q_t - \sigma_v)/\sigma'_v}{(\sigma'_v + \sigma'_h + \sigma'_z)/(3\sigma'_m)} \tag{6.118}$$

Under level-ground conditions,

$$M = \frac{q_t - \sigma_v}{\sigma'_v(1 + K_0)} \tag{6.119}$$

Robertson (2009) [@Robertson2009] used data from Wride et al. (2000) [@WrideEtAl2000], Jefferies and Been (2006) [@JefferiesBeen2006], and Shuttle and Cunning (2007) [@ShuttleCunning2007] to estimate contours of state parameter for uncemented Holocene-age soils in $Q_{tn}$–$F_r$ space. The contours are noted as being approximate since factors other than $Q$ and $F$ (e.g., stress state and plastic hardening for coarse-grained soils and sensitivity for fine-grained soils) can also affect state estimates. Letting

$$Q_{tn,cs} = K_c \cdot Q_{tn} \tag{6.120}$$

where $Q_{tn}$ is as given in Equation (6.61) and

$$K_c = \begin{cases} 1.0 & \text{for } I_c \leq 1.64 \\ -0.403\,I_c^4 + 5.581\,I_c^3 - 33.75\,I_c^2 + 17.88\,I_c - 11.9 + 13.3 & \text{for } I_c > 1.64 \end{cases} \tag{6.121}$$

Robertson (2010) [@Robertson2010] proposed the simplified approximate relationship to estimate $\psi$ from $Q_{tn,cs}$

$$\psi = 0.56 - 0.33\log Q_{tn,cs} \tag{6.122}$$

Figure 6.108 shows contours of state parameter superimposed upon the soil behavior types of Robertson (2012) [@Robertson2012].

**FIGURE 6.108** Contours of state parameter as functions of normalized cone tip resistance and friction ratio. (After Robertson, 2012; courtesy of P.K. Robertson.)

### 6.6.5.3 Estimation of Relative State Parameter Index

As discussed in Section 6.4.3.6, the relative state parameter index, $\xi_R$, of Boulanger (2003a) [@Boulanger2003a] uses a relative density-based relative dilatancy index [@Bolton1986] to relate state parameter to relative density, a parameter that is both familiar and frequently measured. Combining Equation (6.35) with the $D_r$ relations given earlier in this section, and setting $R = 1$ and $Q = 10$, the SPT-based relative state parameter index can be described as

$$\xi_R = \frac{(N_1)_{60}}{46} - \ln(100\,p'/p_a) \tag{6.123}$$

where $p'$ = mean effective stress in same units as $p_a$. A similar relationship based on CPT resistance is

$$\xi_R = \frac{Q_{tn}}{0.334} - \ln(100\,p'/p_a) - 0.086 \tag{6.124}$$

It should be recognized that, being based on data from many different sands tested in different investigations, the correlations of Equations (6.123) and (6.124) correspond to the average behavior of sands in that database, and may not accurately represent the behavior of a specific sand whose characteristics differ significantly from the average of that population.

### 6.6.5.4 Element-Level Effects of Volume Change Behavior

The tendency of a soil to contract or dilate upon shearing leads to the development of volumetric strain, which can be positive (in the case of contraction) or negative (in the case of dilation). Under seismic loading, the shear strains induced in the soil at level-ground sites are usually small enough that only contraction occurs. Under drained conditions, this contraction leads to densification of the soil which is manifested at the ground surface in the form of settlement. Under the undrained conditions that exist in saturated soils subjected to earthquake shaking, the tendency for contraction leads to the development of positive excess pore pressure with resultant reduction of effective stress. After the earthquake, dissipation of the generated pore pressure will lead to contractive volume change. This section describes the effects of volume change behavior on a single element of soil under both drained and undrained conditions; the implications of those behaviors on soil deposits in the field are discussed in Section 9.6.5.

**Drained Conditions** Because air is so much more compressible than water, cyclic loading generally causes dry and partially saturated soils to contract without generation of pore fluid (air or water) pressure. The densification of clean sand subjected to cyclic simple shear loading has been found to be influenced by the density of the sand, the amplitude of the cyclic shear strain induced in the sand, and the number of cycles of shear strain applied to the soil [@SilverSeed1971][@Youd1972][@SeedSilver1972]. Figure 6.109 shows how the volumetric strain after 15 cycles increases with increasing strain amplitude and decreasing relative density; most of this volumetric strain occurs in the first few cycles. Shaking tables have been used to excite large simple shear-like test specimens with uni-directional, bi-directional (two orthogonal horizontal directions), and tri-directional (two horizontal plus vertical) shaking. Pyke et al. (1975) [@PykeEtAl1975] found that bi-directional shaking produced volumetric strains approximately equal to the sum of the strains that would occur if each of the loading histories had been applied uni-directionally, and that adding a vertical component of acceleration resulted in an increase in volumetric strains of up to approximately 50%. Volumetric strains in 16 sands with $D_{50}$ values ranging from 0.13 to 1.60 mm were observed to be strongly influenced by relative density and total overburden stress, but not by gradation, particle angularity, soil fabric, mineralogy, saturation, or age [@DukuEtAl2008]. Fill materials are often granular with some amount of fines, and have been observed to settle in earthquakes [@SeedLee1967][@McClure1973][@Slosson1975][@StewartEtAl2001]. Whang et al. (2004) [@WhangEtAl2004] found that compacted plastic soils developed lower volumetric strain than clean sands, and that plastic soils developed smaller strains when compacted wet of optimum than when compacted dry of optimum. Tsukamoto et al. (2004) [@TsukamotoEtAl2004] performed cyclic triaxial tests on sands containing about 20% nonplastic fines prepared at consistent void ratios but at different degrees of saturation. The specimens with lower degrees of saturation were found to develop most of their volumetric strain during cyclic loading while the more highly saturated specimens developed most of theirs after cyclic loading had ended. The total volumetric strain levels, however, were about the same, which indicated that the degree of saturation had little effect on the final volumetric strain of the soil. Whang et al. (2005) [@WhangEtAl2005] tested sand with nonplastic fines (rock flour) and found volumetric strains to be higher than those of clean sand. They also found that volumetric strain decreased with increasing degree of saturation up to $S = 30\%$, and then increased at higher degrees of saturation; the reduction in volumetric strain resulted from matric suction [@YeeEtAl2014]. A simplified procedure for the estimation of volumetric strain based on tests performed on one clean sand [@SilverSeed1971] was developed by Tokimatsu and Seed (1987) [@TokimatsuSeed1987]. Since that time, a number of researchers [@WhangEtAl2004][@WhangEtAl2005][@TsukamotoEtAl2004][@DukuEtAl2008][@YeeEtAl2014] have tested a wider variety of soils under a wider variety of conditions. These data have allowed the development of volumetric strain models that predict the volumetric strain resulting from a given number of cycles of a particular cyclic shear strain amplitude. The mean volumetric strain resulting from 15 cycles of shear strain, which is considered to be representative of that produced by a $M_w$ 7.5 earthquake, can be expressed as

$$\varepsilon_{\text{vol}} = \begin{cases} 0 & \gamma_{\text{cyc}} \leq \gamma_{tv} \\ a\,(\gamma_{\text{cyc}} - \gamma_{tv})^b & \gamma_{\text{cyc}} > \gamma_{tv} \end{cases} \tag{6.125}$$

where $\gamma_{\text{cyc}}$ = cyclic shear strain amplitude, $\gamma_{tv}$ = volumetric threshold shear strain (Section 6.4.3.1) below which no volumetric strain occurs, $a$ and $b$ are coefficients that are ideally determined from high quality, material-specific laboratory tests, and all strains are in percent. An example of the variation of $\varepsilon_{v,N=15}$ with shear strain amplitude in cyclic simple shear tests is shown in Figure 6.110a. The majority of the volumetric strain occurs in the early cycles after which the rate of volume change slows. For numbers of cycles other than 15, the volumetric strain can be computed as

$$\varepsilon_{v,N} = C_{\varepsilon_v}(N)\,\varepsilon_{v,N=1} \tag{6.126}$$

where $C_{\varepsilon_v}(N) = 1 + R_{\varepsilon_v}\ln(N/15)$ and $R_{\varepsilon_v}$ is the rate of change of $\varepsilon_v$ with respect to $N$ obtained from laboratory testing (e.g., Figure 6.110b). In the absence of such testing, laboratory investigations of clean sand [@DukuEtAl2008] and low-plasticity (PI ≤ 7) silty sands [@YeeEtAl2014] indicated that these coefficients can be estimated as

$$a \approx 5.38\exp(-0.023\,D_r)\,K_{\sigma,\varepsilon}\,K_S\,K_{FC} \tag{6.127a}$$

$$b \approx 1.2 \tag{6.127b}$$

where $K_{\sigma,\varepsilon}$, $K_S$, and $K_{FC}$ are adjustment factors for total overburden stress, degree of saturation, and fines content, respectively, and $D_r$ is given in percent. The values of those adjustment factors are shown in Table 6.12. Equation (6.127a) shows that the $a$ parameter, which controls the overall level of vertical strains from seismic compression, decreases as relative density increases and as the total vertical stress, $\sigma_v$, increases. The relative density effect results from increased dilatancy at the reference total stress of 1 atm, while the overburden effect is thought to result from the increase of bulk moduli (which control volumetric strain responses at modest shear strain levels) with increasing overburden pressure.

**FIGURE 6.109** Relationship between volumetric strain and cyclic shear strain for a sand of different relative densities. (After Tokimatsu and Seed, 1987; used with permission of ASCE.)

**Table 6.12** Adjustment Factors for Volumetric Strain Estimation for Clean Sand and Low-Plasticity Silty Sand.

Total overburden stress ($K_{\sigma,\varepsilon}$): $(\sigma_v/P_a)^{-0.29}$ for both clean sand [@DukuEtAl2008] and silty sand [@YeeEtAl2014].

Degree of saturation ($K_S$) for clean sand: $K_S = 1.0 - 0.0175\,S$ for $S < 30\%$; $K_S = 0.5$ for $30\% \leq S < 50\%$; $K_S = 0.05\,S - 2.0$ for $50\% \leq S < 60\%$; $K_S = 1.0$ for $S \geq 60\%$. Silty sand values listed separately.

Fines content ($K_{FC}$, %): $K_{FC} = 1.0$ for $\mathrm{FC} \leq 10\%$; $K_{FC} = \exp[-0.041(\mathrm{FC} - 10)]$ for $\mathrm{FC} > 10\%$.

Number of cycles ($C_{N\varepsilon_v}$): Similar to that for sand; $C_{N\varepsilon_v} = 1 + R\ln(N/15)$, with $R \approx 0.29$.

$S$ and FC are expressed in percent.

**FIGURE 6.110** Volumetric strain material model fit to test results for Silica #2 sand material prepared to $D_r = 60\%$. (a) vertical strain at 15 cycles vs $\gamma_c$; (b) variation of vertical strain with the number of loading cycles $N$. (After Duku et al., 2008; used with permission of ASCE.)

**Undrained Conditions** When saturated soils are subject to earthquake shaking, the undrained loading conditions lead to generation of excess pore pressures, the subsequent dissipation of which can lead to compression. As illustrated schematically in Figure 6.111, generation of excess pore pressure causes the state of the soil to move from the consolidation curve (Point A) to a point at a lower effective stress (Point B) with the same void ratio. As the excess pore pressure dissipates, however, the sample will reconsolidate until the effective stress returns to its original value; the state of the soil will move from Point B to Point C, which will be at a lower void ratio than existed before earthquake shaking. The soil undergoes a volumetric strain, $\varepsilon_v = \Delta e/(1 + e_0)$. Martin et al. (1975) [@MartinEtAl1975] took the change in effective stress to be the product of the volumetric strain and the unloading-reloading modulus of the soil skeleton to develop a very early pore pressure model, which is discussed in more detail in Sections 6.6.5.4 and 9.5.7.1.

**FIGURE 6.111** Process of earthquake-induced settlement from dissipation of earthquake-induced excess pore pressure.

**FIGURE 6.112** Development of post-cyclic volumetric strain in cyclic simple shear tests on clean sands. (After Ishihara, 1996; used with permission of Oxford University Press.)

Laboratory experiments have shown that the post-earthquake densification of saturated sand is influenced by the density of the sand, the maximum shear strain induced in it, and the amount of excess pore pressure generated by the earthquake. As would be expected, volumetric strains approach a limiting value that decreases with increasing relative density, as shown in Figure 6.112.

### 6.6.6 Shear Strength

The shear strength of soil is a critical parameter for many geotechnical earthquake engineering applications including stability problems (e.g., slope stability, bearing capacity of foundations) and large-strain site response. For some of these applications (e.g., site response, Newmark-type displacement analysis), the shear strength that can be mobilized during earthquake shaking is of interest. For other applications (e.g., flow sliding), the strength that is available following cyclic loading is of interest, especially when the soil is degraded as a result of changes in pore pressure or soil fabric. The strength of nonplastic, cohesionless soils is inextricably tied to the phenomenon of liquefaction, a problem so important in geotechnical earthquake engineering that it is treated in a separate chapter (Chapter 9). Some fine-grained soils can also show significant degradation of stiffness and/or strength during earthquake shaking through cyclic softening, and their behavior under cyclic loading is also discussed in Chapter 9. The shear strength of soils subjected to monotonic loading was described in Section 6.4.3. This section briefly reviews shear strength under typical drained and undrained conditions, and then discusses the effects of the deviations from those conditions that exist under earthquake loading. These definitions include the effects of rapid loading rates and cyclic degradation. Uncertainty in shear strength is also discussed.

### 6.6.6.1 Drained and Undrained Shear

During earthquakes, the rapid nature of loading will cause soils below the water table to respond under undrained conditions (Section 6.2.4) and mobilize undrained strengths. In such cases, the undrained strength is appropriate for seismic analysis even if a drained strength was found to be critical for non-seismic applications. Saturated soils below the water table can suffer cyclic strength degradation from pore pressure development and changes in fabric. In particular, sandy soils can liquefy and experience a dramatic loss of strength. This subject, including procedures for the assignment of undrained shear strengths for post-liquefaction conditions, is presented in Chapter 9. If sands below the water table are found to have a high resistance to liquefaction, then significant pore pressure generation is not expected and dilation may cause a reduction of pore pressure after cyclic loading has ended. Under such conditions, drained strengths developed from pre-event effective stresses can be appropriate. Drained strengths should be used for dry or partially saturated soils.

### 6.6.6.2 Monotonic Shear Strength Evaluation at Ordinary Strain Rates

For clayey materials, undrained strengths can be measured using in situ vane shear (Section 6.5.3.4) or pressuremeter testing (Section 6.5.3.5), or with sampling and undrained testing in the laboratory (Section 6.5.4.3). To minimize disturbance effects, samples should be taken with thin-walled tube samplers (Shelby tube or similar). Samplers that have thick walls and are driven into the soil in a manner similar to the SPT produce excessive soil disturbance that can bias shear strengths measured in tests using the retrieved specimens.

### 6.6.6.3 Effects of Cyclic Degradation

Both sands and clays can experience cyclic degradation from pore pressure generation. In the case of sands, this behavior is evaluated in the context of liquefaction analysis procedures presented in Chapter 9. In the case of clays, the level of peak pore pressure ratio, $r_{u,\max}$, that can be experienced during cyclic loading is less than that for sands, generally not approaching the value of $r_u = 1.0$ associated with initial liquefaction. Nonetheless, this pore pressure generation, combined with possible soil fabric change, can significantly reduce the shearing resistance that is available during cyclic loading and post-cyclic monotonic shear. The loss of stiffness during cyclic loading due to pore pressure increase and related effects is known as cyclic softening [@BoulangerIdriss2007]. Procedures for analysis of these effects are also presented in Chapter 9. This section focuses on the effects of cyclic loading on post-cyclic monotonic shear behavior. The degradation of clay from cyclic pore pressure generation reduces the effective stress below its initial value, causing the clay to enter a state of "apparent overconsolidation" [@MatsuiEtAl1992]. Moreover, since shear modulus is related to effective stress (Section 6.6.2), the stiffness of the soil can be expected to have decreased. These shear modulus reductions, in turn, tend to increase cyclic shear strains, which can be particularly impactful for sensitive soils that also undergo fabric change. As pointed out by Castro and Christian (1976) [@CastroChristian1976], the ultimate (residual, high-strain) undrained shear strength of a saturated soil is controlled by its void ratio and fabric. While cyclic degradation does not affect void ratio, it can affect fabric, particularly when soils are sensitive and the cyclic loading produces large strains. In extreme cases, the shear strength can be reduced from the undrained strength to the remolded undrained shear strength. Consider first the case of saturated clays with low sensitivity. Such a clay material at a particular void ratio will mobilize a specific undrained strength, with little influence of the history of stresses and strains by which that strength is arrived at. For such soil conditions, the undrained strength after cyclic loading would be expected to be equal to the undrained strength before undrained loading (if tested at the same strain rate). The six triaxial specimens shown in Figure 6.113 had similar void ratios (except specimen 6, which had a somewhat higher void ratio than the rest) at the end of consolidation. Specimen 1 was sheared monotonically immediately after consolidation and is shown in Figure 6.113 to have a sensitivity of about 1.0 (at least for axial strains ≤ 4%). Specimen 1 contracted initially but then dilated at larger strain amplitudes. Specimens 2 to 6 were first subjected to varying levels of cyclic loading, which were followed by monotonic shear without allowing drainage. Since the void ratios were nearly the same, the specimens would therefore be expected to have similar monotonic strengths. As shown by the stress-strain curves and stress paths, they behaved largely as would be expected. After being subjected to different levels of cyclic strain, all exhibited dilative behavior upon monotonic loading since their effective stresses at the end of cyclic loading were lower than their preconsolidation pressures. Their ultimate (large strain) strengths, however, were similar (except specimen 6, which was lower than the others) since they had similar effective stresses at the critical state they dilated toward. Differences in the ultimate strength can be explained by small differences in the void ratios and also by differences in the extent of structural (fabric) disturbance induced by the cyclic loading. Also evident in Figure 6.113 is reduced stiffness in the early stages of monotonic undrained loading (as compared to Specimen 1) for the elements that had previously been loaded cyclically.

**FIGURE 6.113** Effect of cyclic loading on subsequent monotonic undrained loading behavior of triaxial specimens of slightly plastic silt: (a) stress-strain behavior; (b) effective stress path behavior. Specimen 1 was tested in conventional CU test with no prior cyclic loading. Specimens 2 to 6 were subjected to different levels of cyclic loading prior to monotonic loading. Note the dilative nature of the stress paths of specimens 2–6 compared to specimen 1. (After Castro and Christian, 1976.)

Post-cyclic strength can also be influenced by mineralogy [@AjmeraEtAl2019]. Simple shear tests performed on mixtures of clay minerals and ground quartz and on natural soils with monotonic loading applied after cyclic loading sufficient to cause 10% double-acting shear strain showed that induced pore pressures were higher when the clay mineral was kaolinite than when it was montmorillonite. The degradation ratio, i.e., the ratio of post-cyclic to static undrained strength, increased with plasticity index for kaolinite mixtures, but was relatively insensitive to plasticity index for montmorillonite mixtures; the strengths of the montmorillonite mixtures, however, were sensitive to the applied cyclic stress ratio (Figure 6.114). When the tests were interpreted in terms of effective stresses after cyclic loading, the degradation ratio was found to vary with pore pressure ratio at the end of cyclic loading as

$$\delta = \frac{s_{u,pc}}{s_u} = (1 - r_{u,\text{cyc}})^{0.247} \tag{6.128}$$

where $s_{u,pc}$ is the post-cyclic undrained strength, $s_u$ is the static undrained strength and $r_{u,\text{cyc}}$ is the pore pressure ratio at the end of cyclic loading. The relationship of Equation (6.128) was found to be applicable to all of the tested soils (kaolinite and montmorillonite mixtures and natural soils) but with a significant degree of variability in the data. For sensitive soils, the extent to which soil fabric is disturbed has most commonly been assumed to be influenced by the relationship between the cyclic strain amplitude and the strain at which failure occurs under monotonic loading conditions [@ThiersSeed1978]. Substantial structural disturbance can modify the stress-strain behavior and reduce the monotonic shear strength. Thiers and Seed (1978) [@ThiersSeed1978] found that the ultimate strengths of three sensitive clays decreased by less than 10% when the cyclic strain amplitude was less than one-half of the failure strain from monotonic tests. At higher cyclic strain amplitudes, however, the reduction in strength was more dramatic, as illustrated in Figure 6.115. Similar results have been obtained by others [@Koutsoftas1978][@RamanujamEtAl1978][@ByrneEtAl1984][@ErkanUlker2008a][@ErkanUlker2008b]. Various investigators have identified factors beyond void ratio and strain amplitude that influence post-cyclic shear strength.

**FIGURE 6.114** Variation of undrained strength degradation factor with plasticity index for soil mixtures and three natural soils. (After Ajmera et al., 2019; used with permission of ASCE.)

**FIGURE 6.115** Effect of peak cyclic strain on monotonic strength of three clays after cyclic loading. (After Thiers and Seed, 1969.)

**FIGURE 6.116** Reduction of undrained strength after cyclic loading as functions of (a) strain and initial stress ratio and (b) dissipated energy. (After Jitno, 1990.)

Jitno (1990) [@Jitno1990] found that the post-cyclic shear strength was also influenced by the cyclic shear stress amplitude with lower cyclic shear stress amplitudes (hence, more cycles) for a given peak shear strain producing a greater strength loss than higher cyclic stress amplitudes (Figure 6.116a). Jitno (1990) [@Jitno1990] also suggested that undrained strength loss was most closely correlated to absorbed energy, or hysteretic work (Figure 6.116b). Hyde and Ward (1985) [@HydeWard1985] found the difference between original and post-cyclic monotonic strength of a silty clay (LL = 36, PL = 19) to be influenced by stress history. Specimens were consolidated one-dimensionally from a slurry, isotropically unloaded to different overconsolidation ratios, and then subjected to 10,000 cycles of loading at shear stress amplitudes ranging from 13% to 42% of the equivalent pressure (defined as the effective stress on the isotropic virgin compression curve at the void ratio of the soil following consolidation). The post-cyclic strengths of the normally and lightly overconsolidated specimens were found to be up to about 20% lower than the strengths of specimens not subjected to cyclic loading. For more heavily overconsolidated (and, hence, more dilative) specimens (typically OCR > 2.5–3.0), no significant reduction in strength due to cyclic loading was observed. Yasuhara (1994) [@Yasuhara1994] developed an approximate method to predict the effects of post-cyclic strength loss. Yasuhara (1994) used consolidation theory and normalized strength properties to define an apparent OCR based on the pore pressure generated by cyclic loading. That OCR was used to define a ratio of undrained strength after cyclic loading (but with no time for pore pressure dissipation) to undrained strength of a monotonically loaded normally consolidated clay
