PGA, $\sigma'_{v0}$, $\sigma_{v0}$, $z$, $M$, $V_{s1}$, FC, $V_{s12}$

[@KayenEtAl2013] Prob. $V_s$. (a Det. = Deterministic; Prob. = Probabilistic. b I&B = Idriss and Boulanger. c B&I = Boulanger and Idriss.)

observations). Liquefaction is then considered to occur when the loading exceeds the resistance, or when the factor of safety against triggering of liquefaction,

$$FS_L = \frac{CRR}{CSR} \tag{9.7}$$

is less than 1.0. It turns out that both the CSR and CRR are influenced by a number of factors that can vary from site to site and from point to point at a particular site. In order for the factor of safety to provide a reliable indication of liquefaction potential, it is critical that these factors be accounted for so that the CSR and CRR values used to compute it are consistent with each other. Figure 9.34 illustrates the manner in which loading and resistance parameters can vary with depth within a soil profile. The loading, whether expressed in terms of cyclic shear stress or CSR, generally varies relatively smoothly with depth while the resistance (e.g., CRR) can vary irregularly due to stratigraphy and variations in soil density. The factor of safety drops below 1.0 when CRR < CSR; in this case indicating that liquefaction is expected to be triggered in a thin, shallow zone and a thick, deeper zone. As will be discussed in Section 9.6, the consequences of liquefaction are influenced by the depth, thickness, and density of layers that liquefy as well as the mechanical and hydraulic characteristics of non-liquefied layers [@CubrinovskiEtAl2017]. For reasons discussed in the following sections, important factors affecting CSR and CRR include earthquake magnitude, initial vertical effective stress, and initial, static shear stress. Because these factors can vary so much from one case to another, it is common to express both CSR and CRR in terms of standardized reference values that can then be adapted to site-specific conditions by a series of adjustment factors. The factor of safety can then be computed using the site-specific or corresponding standardized values, i.e., as

$$FS_L = \frac{CRR_{std,M,\sigma'_v,\alpha}}{CSR_{std,M}} \tag{9.8}$$

where $\alpha$ is a factor (Equation 9.32) that represents the initial, static shear stress acting on the soil element of interest.

FIGURE 9.34 Schematic illustration of variation of (a) induced and resisting shear stresses, (b) cyclic stress and resistance ratios, and (c) factor of safety against triggering with depth. Shaded zone indicates depths at which liquefaction is expected to be triggered.

### 9.5.4.1 Basic Framework

As discussed in Section 6.4.3.6, the level of contractiveness of a soil depends on its state, i.e., the combination of density and effective stress it exists under. Penetration tests have been shown to measure quantities that correlate well to the relative density of coarse-grained soils. Descriptions of cone penetration and standard penetration tests are presented in Section 6.5.3. Both tests measure resistance to the advancement of a penetrometer into the soil. The penetrometers have sufficient volume that soil must be displaced in order for the penetrometer to move downward; this deformation involves relatively large strains beneath and adjacent to the tip of the penetrometer during which the soil may contract or dilate depending on its initial state. The measured penetration resistance is strongly affected by the degree to which the soil contracts or dilates as it is sheared. Soil characteristics that lead to increased liquefaction resistance typically also lead to increased penetration resistance, which helps explain why penetration resistance is useful for the evaluation of liquefaction potential. Shear wave velocities are also correlated, though not as strongly, to relative density. Shear wave velocity has the advantage, however, of being measurable from the ground surface (e.g., by SASW or MASW). This feature allows shear wave velocity to be used in gravels or even coarser materials where conventional CPT or SPT testing is difficult. Shear wave velocity is related to shear modulus, which controls shear strain, and pore pressures are known to be closely related to cyclic shear strain amplitude (Section 9.5.5.2). These features have led to the use of shear wave velocity as an alternative soil parameter for characterization of liquefaction potential. A number of adjustment factors are required to obtain site- and layer-specific values of CSR and CRR, and some are different for different in situ test parameters, which leads to a large number of possible combinations of factors and parameters. The basic framework of cyclic stress procedures is illustrated in Figure 9.35 and culminates in the calculation of a factor of safety, $FS_L(z)$ or, alternatively, a probability of liquefaction, $P_L(z)$. The framework separates the liquefaction potential

FIGURE 9.35 Schematic illustration of typical steps in a cyclic stress- and penetration test-based liquefaction potential evaluation. Evaluation of loading and resistance, with various adjustments for site-specific conditions, results in calculation of factor of safety against liquefaction. Numbers in square brackets refer to equation numbers for CPT-based evaluation described in the following sections.

evaluation into loading and resistance calculations and includes three sets of adjustments: (1) CSR adjustments, (2) soil parameter adjustments, and (3) CRR adjustments. The remainder of this section will be organized in a manner consistent with Figure 9.35. It will begin with characterization of loading, followed by characterization of in situ soil parameters, and then characterization of resistance, and will do so for liquefaction potential procedures based on CPT resistance, SPT resistance, and shear wave velocity. It should be noted that numerous semi-empirical models for assessing the potential for triggering of liquefaction have been proposed and refined over the years. Each model has its own form with its own set of adjustment factors that are calibrated on its own case history database. Consequently, the adjustment factors are specific to the model; adjustment factors from different models should not be mixed and matched. It should further be noted that the case history-based approach to evaluation of triggering resistance is common but not universal. Current practice in Japan largely revolves around correlation of triggering resistance to the results of laboratory tests (e.g., Tokimatsu and Yoshimi, 1983 [@TokimatsuYoshimi1983]), often informed by testing of undisturbed samples obtained by ground freezing (Section 6.5.4.1). Upadhyaya et al. (2023) [@UpadhyayaEtAl2023] similarly propose a triggering model that distinguishes triggering from manifestation and is based solely on the results of cyclic laboratory tests.

### 9.5.4.2 Characterization of Earthquake Loading

Earthquake loading is characterized in terms of cyclic shear stress amplitude, which is related to the amplitude of the earthquake ground motion. The cyclic shear stress used in empirical procedures is the shear stress assumed to exist in the absence of pore pressure generation. While it may seem odd to evaluate liquefaction potential using stresses that do not actually exist in the soil being evaluated, it should be recognized that recorded ground motions (that would be influenced by pore pressure generation) are not available for the overwhelming majority of the case histories upon which empirical procedures are based. Therefore, the loading for case histories has historically been estimated from nearby recordings (at non-liquefied sites) or from GMMs that implicitly presume no pore pressure generation. As a result, and for consistency, the cyclic stresses in an empirical liquefaction potential evaluation should not be affected by pore pressure generation. The cyclic stresses can be predicted in two ways: by detailed, site-specific ground response analyses or with the use of a simplified approach.

**Site Response Analysis** Ground response analyses (Sections 7.5–7.6) can be used to predict shear stress histories at various depths within a soil deposit. The analyses require input motions, which are typically selected and scaled or otherwise modified to be consistent with a scenario- or PSHA-derived response spectrum for the site condition (Section 4.5) of interest and with the distribution of magnitudes that contribute to that spectrum. The resulting shear stress histories should then have amplitudes and durations that are consistent with those expected for the return period of interest. Since the shear stresses used in empirical liquefaction analyses are those expected to develop in the absence of pore pressure generation, total stress site response analyses should be used. Such analyses produce shear stress histories with the transient, irregular characteristics of actual earthquake motions. It should be noted that ground response analyses require proper site characterization, the development of representative input motions, and the use of a suitable computer program to perform the analysis. Obtaining this information requires some time and expense, but is part of a modern, high-quality liquefaction potential evaluation. As described in Chapter 7, site-specific ground response analyses can account for features of a particular site that cause it to systematically respond differently (more strongly or less strongly) than what is produced by standard (ergodic) models for site response, for example as contained in GMMs.

**Simplified Method** In the early years of liquefaction potential evaluation, personal computers and graphical user interfaces were not available, so performing site-specific ground response analyses was much more difficult than it is at present. To eliminate the need for site-specific analyses, Seed and Idriss (1971) [@SeedIdriss1971] developed a "simplified method" that could be used without a site-specific ground response analysis. The basis for the simplified method is shown in Figure 9.36. In a rigid soil profile, the shear stress for a given level of peak ground acceleration would increase linearly with depth (in a soil of constant density). Since real soil profiles are not rigid, however, shear stresses will increase with depth at a different rate – one that is related to the wavelengths present in the ground motion (shorter wavelengths correspond to faster reduction with depth). In the simplified method, the compliance, or flexibility, of the soil profile is accounted for by a depth reduction factor, $r_d$, defined as shown in Figure 9.36. The peak cyclic shear stress amplitude for the compliant soil can then be estimated [@SeedIdriss1971] as

$$\tau_{max} = \frac{a_{max}}{g}\,\sigma_{v0}\,r_d \tag{9.9}$$

where $a_{max}$ is the peak ground surface acceleration, $g$ is the acceleration of gravity, and $\sigma_{v0}$ is the total vertical stress at the depth of interest. The cyclic stress ratio at that depth is then given by

$$CSR = 0.65\,\frac{a_{max}}{g}\,\frac{\sigma_v}{\sigma'_v}\,r_d \tag{9.10}$$

Idriss and Boulanger (2008) [@IdrissBoulanger2008] used the results of analyses of multiple soil profiles subjected to multiple input motions [@Golesorkhi1989][@Idriss1999] to express the mean depth reduction coefficient as

$$r_d = \exp\!\left[\alpha(z) + \beta(z)\,M\right] \tag{9.11}$$

where

$$\alpha(z) = -1.012 - 1.126\sin\!\left(\frac{z}{11.73} + 5.133\right)$$

$$\beta(z) = 0.106 + 0.118\sin\!\left(\frac{z}{11.28} + 5.142\right)$$

FIGURE 9.36 (a) Calculation of peak shear stress at the base of rigid slice of soil, and (b) definition of depth reduction factor, $r_d$.

FIGURE 9.37 Variation of depth reduction factor, $r_d$, with depth. (After Idriss and Boulanger, 2010 [@IdrissBoulanger2010].)

and $z$ is depth in meters. The resulting variation of $r_d$ with depth is shown in Figure 9.37. The variation of $r_d$ with magnitude accounts to some extent for the increased low-frequency (hence long wavelength) characteristics of large magnitude earthquakes; this relationship does not, however, account for shear wave velocity which also affects wavelength. An alternative depth reduction factor model was developed from analyses of soil profiles consistent with soil profiles in the liquefaction case history database by Cetin et al. (2004) [@CetinEtAl2004] and used in the shear wave velocity model of Kayen et al. (2013) [@KayenEtAl2013],

$$r_d(z,\,a_{max},\,V_{S12},\,M) = \frac{\bigl[-23.013 + 2.949\,a_{max} + 0.999\,M + 0.0525\,V_{S12}\bigr] + \bigl[-0.341 + 0.0785\,z\,V_{S12} + 16.258\bigr]\cdot 0.201\,e^{(\cdot)}}{\bigl[-23.013 + 2.949\,a_{max} + 0.999\,M + 0.0525\,V_{S12}\bigr] + \bigl[0.341 + 0.0785\,V_{S12} + 7.586 + 16.258\bigr]\cdot 0.201\,e^{(\cdot)}} \tag{9.12}$$

where $V_{S12}$ is the time-averaged shear wave velocity in the upper 12 m of the site in m/sec. The uncertainty in $r_d$ increases with depth, so the use of site-specific ground response analyses can be preferable for estimation of CSR at depths greater than 10–12 m. However, the soil profiles used to develop Equation (9.11) were somewhat stiffer and more uniform than those encountered in typical liquefiable soil profiles, which led to $r_d$ values that are generally higher than those expected for typical liquefiable profiles [@CetinEtAl2004][@LasleyEtAl2016]. Because the liquefaction resistance models of Boulanger and Idriss (discussed subsequently) used Equation (9.11) to interpret the case histories, the effects of the bias are effectively canceled out when the same relationship is used to predict liquefaction. Some bias can be introduced, however, when site response analyses are used to compute CSR for profiles that differ from those used in model development.

**Magnitude Adjustment for Standardized CSR** As shown in Section 9.5.2.4, pore pressures in saturated soils build up incrementally with an increasing number of loading cycles in laboratory tests. The level of loading required to initiate liquefaction, therefore, is influenced by both the amplitude and duration of earthquake ground motion. In the era in which liquefaction triggering analyses were first being developed, the laboratory data from which liquefaction resistance was estimated were based on tests in which the cyclic shear stresses have uniform amplitudes. Therefore, comparison of earthquake-induced loading with laboratory-determined resistance required conversion of an irregular stress history to an equivalent series of uniform stress cycles. Seed et al. (1975a) [@SeedEtAl1975a] applied a weighting procedure to a set of shear stress time histories from recorded strong ground motions to determine the number of equivalent, uniform stress cycles, $N_{eq}$ (at an amplitude of 65% of the peak cyclic shear stress, i.e., $\tau_{cyc} = 0.65\,\tau_{max}$) that would produce an increase in pore pressure equivalent to that of the irregular time history.

Seed et al. (1975a) [@SeedEtAl1975a] considered motions from magnitude 7.5 earthquakes to have an average of 15 equivalent cycles of loading and used $M = 7.5$ as a standardized reference level for the effects of duration. Others (e.g., Liu et al., 2001 [@LiuEtAl2001]; Green and Terri, 2005 [@GreenTerri2005]) have developed more refined procedures for evaluating numbers of equivalent cycles. In all cases, the number of equivalent uniform stress cycles increases with increasing earthquake magnitude (just as strong-motion duration increases with increasing earthquake magnitude). The factor of 0.65 used by Seed et al. (1975a) [@SeedEtAl1975a] has been retained by custom since that time although other factors could just as easily be used (albeit with compensating changes in $N_{eq}$). Because liquefaction resistance at the time was related to the results of laboratory tests, those results needed to be related to some characteristic of the expected ground motion that reflected its duration (or $N_{eq}$). Early liquefaction triggering analyses were typically performed for specific earthquake scenarios (i.e., the assumption of an earthquake of a particular magnitude occurring at a particular distance) and durations could not be predicted. As a result, the magnitude of the scenario earthquake was commonly used as a proxy for duration (or number of loading cycles). That approach has persisted, even though current ground motion hazards typically reflect contributions from many different magnitudes and distances that can be obtained from PSHA disaggregations (Section 4.4.3.5). Using the concept of number of equivalent loading cycles, Seed et al. (1975a) [@SeedEtAl1975a] introduced a magnitude scaling factor (MSF) that was intended to account for the effects of the duration of an actual, transient earthquake loading history on pore pressure generation. The MSF, which was formulated as a decreasing function of magnitude, allowed the cyclic stress, $CSR_M$, to be expressed as an equivalent cyclic stress ratio for a particular magnitude of interest. Therefore,

$$CSR_M = \frac{r_e\,a_{max}\,r_d\,\sigma_v}{g\,\sigma'_v\,MSF} \tag{9.13}$$

where the equivalence ratio, $r_e$, is generally taken as 0.65. Expressions for MSF have generally been based on the results of laboratory tests involving multiple cycles of uniform loading. Numbers of equivalent cycles are usually computed using the Palmgren-Miner cumulative damage hypothesis [@Palmgren1924][@Miner1945] from the results of laboratory tests performed on specimens subjected to different loading amplitudes. Assuming a cyclic strength curve can be expressed using a power law, e.g.,

$$CRR = a\,N^{-b} \tag{9.14}$$

the relative number of uniform loading cycles required to initiate liquefaction at two stress ratios, $CSR_A$ and $CSR_B$, would be

$$\frac{N_A}{N_B} = \left(\frac{CSR_B}{CSR_A}\right)^{1/b} \tag{9.15}$$

This relationship allows the relative amounts of "damage" (i.e., pore pressure generation potential) from loading cycles of different amplitudes to be related to each other. Normalizing the amplitudes of all loading cycles by the amplitude of the strongest cycle, each cycle can be assigned a fraction of a loading cycle proportional to the damage it produces; summing the contributions of all loading cycles yields an equivalent number of loading cycles for the transient loading history. Selecting a magnitude of 7.5 provides a reference value of $N_{M=7.5}$ (generally 15) uniform loading cycles, the MSF can be defined as

$$MSF = \frac{N_{M=7.5}}{N_M} = \left(\frac{CSR_M}{CSR_{M=7.5}}\right)^b \tag{9.16}$$

The MSF relationship determined in this way is influenced by the parameter, $b$, which describes the slope of the cyclic strength curve (on a log-log plot of CSR vs. $N_L$).

The MSF has been interpreted by various users as a loading parameter (i.e., one that increases CSR as $M$ increases) or as a resistance parameter (that decreases CRR as $M$ increases). Mathematically, both interpretations are equivalent with respect to their effect on the computed factor of safety (dividing the numerator in Equation (9.7) by MSF is the same as multiplying the denominator by the same number). Another interpretation, however, is that magnitude is a descriptor of loading (used to account for the longer durations of ground motions caused by large magnitude earthquakes) that can also be related to liquefaction resistance (by correlation to the number of harmonic loading cycles in the laboratory test data that forms the basis for MSF). This alternative interpretation allows MSF to be defined by the laboratory-measured cyclic strength parameter slope, $b$ (Equation 9.14). By basing MSF on $b$ and considering the potential for $b$ to depend on penetration resistance, the MSF relationship of Equation (9.16) becomes a mixed function of loading and penetration resistance. Boulanger and Idriss (2014) [@BoulangerIdriss2014] observed differences in the slopes of cyclic strength curves in laboratory tests on soils of different densities. This density dependence is ambiguous, however [@UlmerEtAl2018], with some testing programs showing dependence and others showing none. In order to distinguish between loading and resistance effects for conceptual purposes in this text, the Boulanger and Idriss (2014) [@BoulangerIdriss2014] MSF expression (Equation 9.16) will be written as the product of two terms — a ground motion duration-related loading term for a soil with a standardized reference penetration resistance and a resistance term that accounts for the influence of the number of harmonic loading cycles on the laboratory test-based liquefaction resistances of soils with penetration resistances that differ from the standard value. This form also allows use of laboratory-measured, soil-specific $b$ parameters (Table 9.6) to be used in determination of CRR. The Boulanger-Idriss magnitude scaling factor, referred to here as $MSF_{BI}$, can then be written as

$$MSF_{BI} = MSF_L \cdot K_N \tag{9.17}$$

where the loading parameter, $MSF_L$, is the value of $MSF_{BI}$ for a soil of a reference penetration resistance, taken here as $q_{c1Ncs} = 110$ (or $(N_1)_{60cs} = 15$ blows/ft), and the resistance parameter, $K_N$, describes the effects of number of loading cycles (via magnitude) on the liquefaction resistance of soils of different penetration resistance. With this approach, the magnitude-corrected cyclic stress ratio can be written as

$$CSR_M = 0.65\,\frac{a_{max}}{g}\,\frac{\sigma_v}{\sigma'_v}\,\frac{r_d}{MSF_L} \tag{9.18}$$

and the $K_N$ term can be used to adjust the cyclic resistance ratio. The values of $MSF_L$ for CPT, SPT, and $V_s$-based liquefaction potential evaluation procedures are given in Table 9.3 and illustrated in Figure 9.38.

FIGURE 9.38 Magnitude scaling factor for loading.

The preceding discussion implicitly assumes free-field conditions, i.e., conditions far enough away from structures that the earthquake loading is not influenced by the presence of structures. It should be noted, however, that elements of soil beneath structures, and particularly near and beneath the corners and edges of structures, can be subjected to static shear stresses and considerably higher cyclic shear stresses induced by the inertial response of the structure itself as it moves laterally and rocks during earthquake shaking. Because of these high cyclic shear stresses and low static effective stresses [@TravasarouEtAl2006], soils just outside of the footprint of a building can be subjected to very high CSRs; these soils may liquefy and lead to building settlement (Section 9.6.6.4) even when soils in the free-field do not.

### Example 9.1

An investigation of a site located in California shows a liquefaction-susceptible layer of clean sand exists at 6–8 m depth. The liquefiable layer has a saturated unit weight of 20 kN/m³ and is overlain by 6 m of fill with a unit weight of 21.2 kN/m³. The groundwater table is at the fill/sand interface. A PSHA performed for the site indicates that a PGA of 0.58 g would have a return period of 2,475 years; disaggregation indicates a mean magnitude of 7.1 for that return period. Calculate the standardized CSR for the liquefiable sand layer, assuming it will be used with an SPT- or CPT-based triggering model.

**Solution:** Representing the liquefiable layer by the conditions at its center, the total and effective stresses at 7 m depth are

$$\sigma_v = (6\text{ m})(21.2\text{ kN/m}^3) + (1\text{ m})(20.0\text{ kN/m}^3) = 147.2\text{ kPa}$$

$$\sigma'_v = (6\text{ m})(21.2\text{ kN/m}^3) + (1\text{ m})(20.0\text{ kN/m}^3) - (1\text{ m})(9.81\text{ kN/m}^3) = 137.4\text{ kPa}$$

Using the mean magnitude from the PSHA, the MSF is given by (Table 9.3)

$$MSF_L = 0.5803 + 2.7368\exp(-7.1/4) = 1.044$$

The depth reduction factor at 7 m depth is calculated using Equation (9.11) as

$$\alpha(7.0) = -1.012 - 1.126\sin\!\left(\frac{7.0}{11.73} + 5.133\right) = -0.421$$

$$\beta(7.0) = 0.106 + 0.118\sin\!\left(\frac{7.0}{11.28} + 5.142\right) = 0.047$$

$$r_d = \exp\!\left[\alpha(z) + \beta(z)\,M\right] = \exp\!\left[-0.421 + (0.047)(7.1)\right] = 0.916$$

Finally, from Equation (9.18)

$$CSR_{std} = 0.65\,\frac{a_{max}}{g}\,\frac{\sigma_v}{\sigma'_v}\,\frac{r_d}{MSF_L} = 0.65\,\frac{(0.58)(147.2\text{ kPa})\,(0.916)}{(137.4\text{ kPa})(1.044)} = 0.354$$

TABLE 9.3 Magnitude Adjustment Factors for Cyclic Stress Ratio in CPT-, SPT-, and $V_s$-Based Triggering Models.

Model CPT, adjustment parameter $M$, reference value $M = 7.5$: $MSF_L = 0.5784 + 2.7495\exp(-M/4) \leq 1.32$.

Model SPT, adjustment parameter $M$, reference value $M = 7.5$: $MSF_L = 0.5803 + 2.7368\exp(-M/4) \leq 1.32$.

Model $V_s$, adjustment parameter $M$, reference value $M = 7.5$: $MSF_L = 15\,M^{-1.342}$.

### 9.5.4.3 Characterization of in situ Soil Parameters

While liquefaction potential is known to be related to the density of the soil, it is extremely difficult to measure the in situ density of a liquefaction-susceptible soil without changing it by vibration or disturbance. As a result, procedures for evaluation of liquefaction potential commonly use more easily measured proxies for soil density; the most common of these are penetration resistances but shear wave velocity has also been used for this purpose. These parameters comprise the soil density parameter, $S$, which is related to the resistance parameter, $R$, by the boundary curve in Figure 9.32. In situ test parameters can be influenced by material characteristics and environmental factors. The material characteristics are most important for evaluation of liquefaction potential, so it is important to separate them from the environmental characteristics to the greatest extent possible. The penetration test parameters commonly used for evaluation of liquefaction potential are affected by effective stress level and fines content, so standardized values are obtained by applying effective stress and fines content adjustments. $V_s$ is similarly adjusted for effective stress but is not adjusted for fines content in current procedures.

**Effective Stress Adjustments for Soil Parameters** Penetration resistances and shear wave velocities are affected by both soil density and effective stress – for example, a loose sand at a high effective stress can have the same measured penetration resistance as a denser sand at a lower effective stress level. The different densities, however, can be distinguished by normalizing the soil parameters to a reference effective stress level, typically taken as 1 atm for liquefaction potential evaluations (Section 6.5.3.3). The effective stress-adjusted in situ parameters are given by

$$q_{c1N} = C_N\,\frac{q_t - u_a}{P_a} \tag{9.19}$$

$$(N_1)_{60} = C_N\,N_{60} \tag{9.20}$$

$$V_{s1} = C_{Vs}\,V_s \tag{9.21}$$

(note that CPT-based liquefaction triggering models are commonly expressed in terms of $q_c$ rather than $q_t$; the two are related as indicated in Equation 6.53 and are virtually identical for sands). The effective stress adjustment factors have been developed with laboratory data and data from calibration chamber tests [@MarcusonBieganousky1977a][@MarcusonBieganousky1977b]. Boulanger (2003) [@Boulanger2003] and Idriss and Boulanger (2003, 2008) [@IdrissBoulanger2003][@IdrissBoulanger2008] proposed the CPT and SPT effective stress adjustment factors given in Table 9.4. Because the exponents used to compute $q_{c1N}$ and $(N_1)_{60}$ depend on $q_{c1N}$ and $(N_1)_{60}$, their values must be obtained iteratively.

TABLE 9.4 Effective Stress Adjustment Factors for CPT and SPT Resistances [@BoulangerIdriss2014] and for $V_s$ [@KayenEtAl2013].

CPT ($\sigma_{v0} = 1$ atm): $C_N = (P_a/\sigma'_v)^m \leq 1.7$, where $m = 1.338 - 0.249\,q_{c1Ncs}^{0.264}$.

SPT ($\sigma_{v0} = 1$ atm): $C_N = (P_a/\sigma'_v)^m \leq 1.7$, where $m = 0.784 - 0.0768\,(N_1)_{60}^{0.5}$.

$V_s$ ($\sigma_{v0} = 1$ atm): $C_{Vs} = (P_a/\sigma'_v)^{0.25}$.

**Fines Content Adjustments for Penetration Resistance** The presence of fines reduces the permeability and increases the compressibility of a sandy soil, both of which reduce penetration resistance when those soils are saturated. As a result, a silty sand will generally have a lower measured penetration resistance (or shear wave velocity) than a clean sand even if the sands are at the same relative density. Liquefaction resistance can also be influenced by the presence of fines. Laboratory tests have shown that the presence of fines actually decreases liquefaction resistance [@PolitoMartin2001][@CubrinovskiEtAl2010] for soils with the same relative density. Therefore, fines content adjustments are made to account for the combined effects of fines on penetration resistance and liquefaction resistance. No corresponding adjustment is made to the normalized shear wave velocity, $V_{s1}$, used in shear wave velocity-based triggering models (although fines content is, as discussed subsequently, considered to affect $V_s$-based liquefaction resistance). Fines-adjusted penetration resistances, often referred to as the equivalent "clean sand" penetration resistances, are computed as

$$q_{c1Ncs} = q_{c1N} + \Delta q_{c1N} \tag{9.22}$$

$$(N_1)_{60cs} = (N_1)_{60} + \Delta(N_1)_{60} \tag{9.23}$$

where the penetration resistance adjustments, $\Delta q_{c1N}$ and $\Delta(N_1)_{60}$, are given in Table 9.5 and illustrated in Figures 9.39 and 9.40. The "clean sand" penetration resistances given by Equations (9.22 and 9.23) represent the values that would produce the same CRR had the fines content of the soil been very low (<5%). Available data comes from tests on non-plastic fines and therefore apply to that condition; one would generally expect plastic fines to have greater effects than non-plastic fines, so the fines correction is generally applied to both cases with the recognition that it is likely somewhat conservative for plastic fines.

TABLE 9.5 Fines Adjustments for CPT- and SPT-Based Liquefaction Potential Evaluation Procedures.

CPT (reference condition FC = 0): $\Delta q_{c1N} = \left(11.9 + \dfrac{q_{c1N}}{14.6}\right)\exp\!\left(1.63 - \dfrac{9.7}{FC + 9.7} - \dfrac{15.7}{FC + 15.7}\right)$.

SPT (reference condition FC = 0): $\Delta(N_1)_{60} = \exp\!\left(1.63 + \dfrac{FC}{FC + 0.01} - \dfrac{FC}{FC + 0.01}\right)$.

FIGURE 9.39 Fines content adjustment factor for CPT results. (After Boulanger and Idriss, 2014 [@BoulangerIdriss2014].)

FIGURE 9.40 Fines content adjustment factor for SPT results. (After Boulanger and Idriss, 2014 [@BoulangerIdriss2014].)

Fines content should be measured directly whenever possible. When it cannot, it can be estimated, much more approximately, from the soil behavior type index, $I_c$ (Section 6.5.3.3), measured in a cone penetration test. Boulanger and Idriss (2014) [@BoulangerIdriss2014] proposed that

$$I_c = f(FC) + \varepsilon \tag{9.24}$$

where $\varepsilon$ is a normally distributed random variable with zero mean and a standard deviation of 0.29, and suggested that fines content could be estimated by inverting that equation, i.e.,

$$FC(\%) = f(I_c,\,C_{FC}) \tag{9.25}$$

where $C_{FC}$ is a fitting parameter that can be adjusted based on site-specific data when available or taken as zero to match the general trend of available case history and laboratory test data (Figure 9.41). A value of $C_{FC} = 0.07$, for example, approximates the relationship developed by Robinson et al. (2013) [@RobinsonEtAl2013] for liquefiable soils along the Avon River in Christchurch, New Zealand. The dashed lines in Figure 9.41 represent the mean ± one standard deviation values of $I_c$; examination of the data shows limited sensitivity of $I_c$ to FC, which implies a high sensitivity of FC to $I_c$. The corresponding standard deviation of FC estimates from Equation (9.25) is 23%. An updated FC to $I_c$ model based on a larger database in which the regression was targeted to estimate FC was presented by Hudson et al. (2024) [@HudsonEtAl2024], although for consistency Eq. (9.25) should be used with the Boulanger and Idriss (2014) [@BoulangerIdriss2014] model.

### Example 9.2

As indicated in Section 9.4.3, soils are considered to transition from sand-like to clay-like behavior at $I_c$ values of approximately 2.5–2.7. Compute the range of fines contents that correspond to that range of $I_c$ values for typical sandy soils.

**Solution:** Using Equation (9.25) with $C_{FC} = 0.0$,

$$FC = 63\% \quad \text{for } I_c = 2.5$$

$$FC(\%) = f(I_c,\,C_{FC})$$

$$FC = 79\% \quad \text{for } I_c = 2.7$$

Thus, the apparent fines content range corresponding to the $I_c$-based transition range is 63%–79%. The actual soil behavior, however, depends on the nature (e.g., plasticity) of the fines so, while the $I_c$-based fines correction of Equation (9.5) was developed within the context of the Boulanger and Idriss (2014) [@BoulangerIdriss2014] liquefaction triggering model (intended for application to non-plastic fines), its use is limited to that model.

FIGURE 9.41 Data and suggested relationship for estimation of fines content from soil behavior type index. (After Boulanger and Idriss, 2014 [@BoulangerIdriss2014].)

### 9.5.4.4 Characterization of Liquefaction Resistance

In the cyclic stress method, liquefaction resistance is characterized by the CRR, which is correlated to the in situ state of the soil of interest. This correlation is affected by a number of factors that are considered in different ways by different triggering models. Liquefaction resistance is expressed in terms of a standardized CRR that applies to a set of reference conditions with adjustment factors that account for deviations of site-specific conditions from the reference conditions. The standardized CRR relationship is represented in Figure 9.32, whereby the in situ soil parameter, $S$, is related to the standardized resistance parameter, $R$.

**Standardized Cyclic Resistance Ratio Relationships** Once the standardized penetration resistance or shear wave velocity has been determined, liquefaction resistance can be characterized in terms of a standardized CRR, which is equal to the CSR required to initiate liquefaction in a "standard" element of soil (i.e., a young, clean, saturated sand under level ground and subjected to shaking from a M7.5 earthquake, with $\sigma_{v0} = 1$ atm). The CRR value for any combination of magnitude, vertical effective stress, and static shear stress that may exist at a particular site can then be related to the CRR value for "standard" conditions of a magnitude 7.5 earthquake, a vertical effective stress of 1 atm, and level-ground (zero initial shear stress) conditions. Standardized CRR values and the various adjustments required to obtain site-specific values are described for CPT-, SPT-, and $V_S$-based liquefaction potential procedures in the following sections.

**CPT-Based Relationship** Boulanger and Idriss (2014) [@BoulangerIdriss2014] used both CPT and SPT data, principles of soil mechanics, and relevant experimental data within a relative state parameter index-based framework to develop deterministic standardized CRR relationships. The use of this framework ensures a level of consistency between CPT- and SPT-based evaluations of liquefaction potential. As the geotechnical engineering profession transitions from its historical use of SPT results for evaluation of liquefaction potential to CPT-based procedures, this approach helps protect against inconsistent

FIGURE 9.42 CPT-based liquefaction resistance (after Boulanger and Idriss, 2016 [@BoulangerIdriss2016]): (a) variation of CRR with corrected tip resistance for $M_w = 7.5$, $\sigma_{v0} = 1$ atm, and $\tau_{static} = 0$, and (b) variation of model and total uncertainty in CRR with corrected tip resistance.

predictions of liquefaction potential at a particular site. The standardized CRR values based on standardized CPT resistance is given by

$$CRR_{std} = \Phi\!\left[\frac{1}{\sigma_{\ln CRR}}\left(\frac{q_{c1Ncs}}{1{,}000} + \frac{q_{c1Ncs}^2}{1{,}000} - \frac{q_{c1Ncs}^3}{1{,}000} + \frac{q_{c1Ncs}^4}{1{,}000} - 2.60\right)\right] \tag{9.26}$$

where $P_L$ is the probability of liquefaction and $\sigma_{\ln CRR}$ is taken to have a minimum value of 0.2, representing model uncertainty, or larger values when total uncertainty is considered (Figure 9.42b). Boulanger and Idriss (2014) [@BoulangerIdriss2014] recommend that deterministic analyses be based on a cyclic resistance ratio one model uncertainty standard deviation below the mean, i.e., for $\Phi^{-1}(P_L) = -1.0$. The liquefaction resistance given by Equation (9.26) is shown graphically in Figure 9.42. The CRR can be seen to be sensitive to CPT resistance, particularly at $q_{c1Ncs}$ values greater than about 125.

### Example 9.3

A soil layer has an average $q_{c1Ncs}$ value of 120. Compute the standardized CRR values that would have a 95% probability of exceedance considering (1) only model uncertainty, and (2) total uncertainty.

**Solution:** From Equation (9.26), the median cyclic resistance ratio would be

$$CRR_{std,median} = \exp\!\left[\frac{120}{1{,}000} + \ldots - 2.60\right] = \exp\!\left[-1.565\right] = 0.209$$

The standard normal variate for a 95% probability of exceedance (or a 5% probability of non-exceedance) is $\Phi^{-1}(0.05) = -1.645$. From Figure 9.42b, the model and total standard deviations are 0.20 and 0.35, respectively. The standardized CRR values for the two uncertainty levels are then

$$CRR_{std} = \exp\!\left[-1.565 + (-1.645)(0.20)\right] = 0.150 \quad \text{(considering only model uncertainty)}$$

$$CRR_{std} = \exp\!\left[-1.565 + (-1.645)(0.35)\right] = 0.118 \quad \text{(considering total uncertainty)}$$

FIGURE 9.43 Variation of CRR with resistance parameter for $M_w = 7.5$, $\sigma_{v0} = 1$ atm, and $\tau_0 = 0$. (After Boulanger and Idriss, 2012 [@BoulangerIdriss2012].)

**SPT-Based Procedure** The standardized, SPT-based cyclic resistance ratio of Idriss and Boulanger (2008) [@IdrissBoulanger2008] and Boulanger and Idriss (2014) [@BoulangerIdriss2014] is given by

$$CRR_{std} = \Phi\!\left[\frac{1}{\sigma_{\ln CRR}}\left(\frac{(N_1)_{60cs}}{14.1} + \left(\frac{(N_1)_{60cs}}{...}\right)^2 - \left(\frac{(N_1)_{60cs}}{23.6}\right)^4 + \left(\frac{(N_1)_{60cs}}{25.4}\right)^6 - 2.60\right)\right] \tag{9.27}$$

and illustrated graphically in Figure 9.43. A value of $\sigma_{\ln CRR} = 0.20$ was recommended by Boulanger and Idriss (2014) [@BoulangerIdriss2014] and used with $\Phi^{-1}(P_L) = -1.0$ for the deterministic CRR value shown in Figure 9.43.

### $V_s$-Based
