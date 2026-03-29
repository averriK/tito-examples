The potential for triggering of liquefaction has also been correlated to shear wave velocity. There are a number of attractive features to this approach — shear wave velocity is commonly measured, it can be measured from the ground surface using techniques such as SASW and MASW, it can be measured in materials, such as gravelly and cobbly soils, for which conventional penetration testing is difficult, and shear wave velocity is related to shear modulus, which relates ground motion amplitude to shear strain amplitude, which fundamentally controls pore pressure development. The drawbacks are that shear wave velocity describes the very low-strain characteristics of the soil, which, although correlated to higher-strain behavior, may not accurately represent the characteristics of the soil at the strain levels associated with triggering of liquefaction. Shear wave velocities are known to be relatively insensitive to relative density, a characteristic of critical importance in determining the contractiveness of a soil and also to be influenced by particle size in granular soils. Many methods of shear wave velocity measurement have significant uncertainty and provide limited spatial resolution since they average velocities over significant depth intervals and/or horizontal distance ranges. Shear wave velocity is also insensitive to the presence of fines, at least up to the limiting fines content, which is typically about 35% (Section 6.3).

An early $V_s$-based procedure in the cyclic stress-based approach to evaluation of liquefaction potential [@AndrusStokoe2000][@AndrusEtAl2004] took the same basic form as the penetration resistance-based procedures with a magnitude-adjusted CSR and an effective stress-adjusted, $V_s$-based CRR that is also adjusted for age. The procedure indicated an upper bound of $V_{s1} = 215\ \text{m/sec}$ for clean sands ($FC \leq 5\%$) decreasing linearly to 200 m/sec for $FC \geq 35\%$. A subsequent model derived from an expanded database of 422 liquefaction case histories was developed [@KayenEtAl2013] by making shear wave velocity measurements at sites in the SPT [@CetinEtAl2004] and CPT [@MossEtAl2006] catalogs. In that model, CSR is defined as in Section 9.5.4.2 (with $r_d$ from Equation 9.12), and the standardized CRR can be taken as

$$\text{CRR}_\text{std} = \exp\!\left(\frac{5.2726\,V_{s1}^{0.4809} - 0.0073\,V_{s1} - 0.0028\,FC - 2.8011}{1.946}\right) \cdot \Phi^{-1}(P_L) \tag{9.28}$$

where $V_{s1}$ = corrected shear wave velocity (Equation 9.21) and $FC$ = fines content in percent. Unlike the Andrus and Stokoe relationship, the Kayen et al. (2013) [@KayenEtAl2013] CRR relationship (Figure 9.44) does not imply a specific upper bound $V_{s1}$ value above which liquefaction does not occur.

**Figure 9.44.** Median standardized cyclic resistance ratio according to Kayen et al. (2013) [@KayenEtAl2013] compared to M7.5 curve of Andrus and Stokoe (2000) [@AndrusStokoe2000].

### Uncertainty in CRR

There are many sources of uncertainty in a liquefaction hazard evaluation, and in the calculation of liquefaction potential using the cyclic stress approach. The total uncertainty can be divided into parametric uncertainty, i.e., uncertainties in the values of the parameters that go into the calculations, and model dispersion, which results from the inability of the model to accurately and completely represent the physical system of interest (Section D.8). Parametric uncertainty can be evaluated by considering the uncertainties in parameters in all of the case histories in the database upon which the liquefaction procedure was developed [@CetinEtAl2002][@CetinEtAl2004]. The developers of the CPT- and SPT-based models described in the preceding sections did not feel that individual case history data was sufficient to characterize parametric uncertainty, so those models do not account explicitly for parametric uncertainty, e.g., uncertainty in CPT tip resistance, or any of the adjustment factors that affect CSR and CRR. Accordingly, the standard deviation term of $\ln\text{CRR}$, $\sigma = 0.2$ given above, represents model dispersion that includes contributions from both model uncertainty and irreducible model variability. For application to a particular site, the influences of both parametric uncertainty and model dispersion should be carefully considered to form a more complete picture of the total uncertainty (e.g., Figure 9.42b) in evaluation of the triggering of liquefaction.

### Site-Specific Cyclic Resistance Ratio Adjustment Factors

The standardized CRR values (i.e., $\text{CRR}_\text{std}$) presented in the preceding section apply to the specific conditions of $M = 7.5$, $\sigma'_v = 1\ \text{atm}$, $\alpha = 0$, for young, saturated soils, which rarely exist in a given element of soil at a particular site. Deviations from standard conditions are accounted for using CRR adjustment factors so that a site- and layer-specific CRR can be expressed as

$$\text{CRR} = \text{CRR}_\text{std} \cdot K_N \cdot K_\sigma \cdot K_\alpha \cdot K_{DR} \cdot K_S \tag{9.29}$$

where $K_N$, $K_\sigma$, $K_\alpha$, $K_{DR}$, and $K_S$ are adjustments for number of loading cycles, effective stress, initial shear stress, diagenetic processes (e.g., age, cementation, stress history), and saturation, respectively, which are described in the following sections.

#### Number of Loading Cycles Adjustment

Boulanger and Idriss (2014) [@BoulangerIdriss2014] considered soils of different density to be affected differently by number of loading cycles (note that the slopes of the curves in Figure 9.26 are not equal) and proposed a MSF that combined loading and resistance effects. Using the approach described in the preceding section on magnitude adjustment for cyclic stress ratio, the density-dependent effect of number of loading cycles on resistance can be described by an adjustment factor, $K_N = \text{MSF}_{BI} / \text{MSF}_L$, which can be defined as indicated in Table 9.6 and shown graphically in Figure 9.45. The value of $K_N$ can be seen to reflect differences in the sensitivity of CRR to magnitude (as a proxy for number of loading cycles) for soils with CPT and SPT resistances other than 105 or 15, respectively. Table 9.6 also provides an expression for $\text{MSF}_\text{max}$ when laboratory testing has established the value of the $b$-parameter for a specific soil. In the case of the $V_S$-based model of Kayen et al. (2013) [@KayenEtAl2013], and most other liquefaction triggering models in the literature, $K_N = 1.0$ (i.e., the magnitude adjustment is made in the demand parameter through the $\text{MSF}_L$ term (Table 9.2)).

**Figure 9.45.** Magnitude adjustment factor for cyclic resistance ratio. Kinks in curves at low magnitude are due to limiting values in original Boulanger and Idriss relationship.

**Table 9.6.** Magnitude Adjustments to CRR for CPT- and SPT-Based Liquefaction Potential Evaluation Procedures.

CPT procedure — Reference condition: $q_{c1Ncs} = 105$, $M = 7.5$. Adjustment factor:

$$\text{MSF}_\text{max} = 1.09 + \frac{q_{c1Ncs}}{180} \leq 2.2 \tag{9.30a}$$

SPT procedure — Reference condition: $(N_1)_{60,cs} = 15$, $M = 7.5$. Adjustment factor:

$$\text{MSF}_\text{max} = 1.09 + \frac{(N_1)_{60,cs}}{31.5} \leq 2.2 \tag{9.30b}$$

Lab procedure — Reference condition: $M = 7.5$. Adjustment factor: $\text{MSF}_\text{max} = 0.65(20)^b \leq 2.2$, $b = 0.144$.

$$K_N = \frac{\text{MSF}_{BI}}{\text{MSF}_L} = \frac{\min\!\left[1 + \left(\text{MSF}_\text{max} - 1\right)\left(8.64\,\exp(-M/4) - 1.325\right),\ 2.2\right]}{0.5803 + 2.7368\,\exp(-M/4)} \tag{9.30}$$

#### Effective Stress Adjustment

As shown in Section 6.4.3.2, soils tend to become more contractive with increasing effective confining stress. Based on laboratory data and a relative state parameter index-based framework, and assuming a reference effective stress of 1 atm, Boulanger and Idriss (2014) [@BoulangerIdriss2014] proposed the effective stress adjustment factor for CPT- and SPT-based procedures given in Table 9.7. A similar factor is available for the $V_s$-based model from Kayen et al. (2013) [@KayenEtAl2013]; that factor, however, was obtained from data regression and is close to 1.0, which implies much less sensitivity to effective stress than is generally observed in laboratory tests. For the CPT- and SPT-based models, the upper bound on $K_\sigma$ was a modeling decision made by Boulanger and Idriss (2014) [@BoulangerIdriss2014] motivated by a lack of data at low effective stress levels (below about 0.4 atm) but is inconsistent with expected soil behavior. The variation of $K_\sigma$ with vertical effective stress is illustrated in Figure 9.46.

**Table 9.7.** Effective Stress Adjustments to CRR for CPT-, SPT-, and $V_S$-Based Liquefaction Potential Evaluation Procedures.

CPT procedure — Reference condition: $\sigma'_{v0} = 1\ \text{atm}$.

$$K_\sigma = 1 - C_\sigma \ln\!\left(\frac{\sigma'_v}{P_a}\right) \leq 1.1 \tag{9.31a}$$

where $C_\sigma = \dfrac{1}{37.3 - 8.27\,(q_{c1Ncs})^{0.264}} \leq 0.3$.

SPT procedure — Reference condition: $\sigma'_{v0} = 1\ \text{atm}$.

$$K_\sigma = 1 - C_\sigma \ln\!\left(\frac{\sigma'_v}{P_a}\right) \leq 1.1 \tag{9.31b}$$

where $C_\sigma = \dfrac{1}{18.9 - 2.55\,\sqrt{(N_1)_{60,cs}}} \leq 0.3$.

$V_s$ procedure — Reference condition: $\sigma'_{v0} = 1\ \text{atm}$.

$$K_\sigma = \left(\frac{\sigma'_v}{p_a}\right)^{-0.0099} \tag{9.31c}$$

**Figure 9.46.** Effective stress adjustment for CRR (after Boulanger and Idriss, 2014) [@BoulangerIdriss2014]. KEA13 indicates a relationship inferred from Kayen et al. (2013) [@KayenEtAl2013].

#### Static Shear Stress Adjustment

The presence of an initial, static shear stress can affect pore pressure generation in liquefaction-susceptible soils as discussed in Section 9.5.2.4. Laboratory studies show that pore pressures increase more rapidly when shear stress reversals occur, i.e., when the soil goes through an instant in which no shear stress exists. When a transient cyclic shear stress history is added to an existing static shear stress, fewer stress reversals may occur than would if the static shear stress did not exist; if the static shear stress is greater than the peak cyclic shear stress, no stress reversal will occur and initial liquefaction (zero effective stress) cannot occur. For very loose soils, however, increasing shear stress tends to bring the effective stress path closer to the FLS where pore pressures tend to increase more quickly. Thus increased static shear stress can tend to reduce the liquefaction resistance of very loose soils while it increases the liquefaction resistance of denser soils (Figure 9.47a). The initial shear stress is usually characterized in terms of a static shear stress ratio,

$$\alpha = \frac{\tau_h}{\sigma'_{v0}} \tag{9.32}$$

Adjustments for the effects of initial static shear stresses depend on the level of static stress and the state of the soil. Using cyclic simple shear test data [@VaidFinn1979][@BoulangerEtAl1991], Boulanger (2003) [@Boulanger2003] developed an expression for the adjustment factor, $K_\alpha$, as a function of the relative state parameter index (Section 6.4.3.6),

$$K_\alpha = a + \exp\!\left(-\frac{\xi_R}{b}\right) \tag{9.33}$$

where

$$a = 1267 + 636\,\alpha^2 - 634\,\exp(\alpha) - 632\,\exp(-1.11\,\alpha)$$

$$b = \exp\!\bigl(1.31\,\ln(\alpha + 0.0001) + 12.3\,\alpha^2\bigr)$$

$$c = 0.138 + 0.126\,\alpha + 2.52\,\alpha^3$$

**Figure 9.47.** Static shear stress adjustment factor for CRR of sands expressed in terms of: (a) relative density (Harder and Boulanger, 2007 [@HarderBoulanger2007] with permission of MCEER) and (b) relative state parameter index (Boulanger, 2003 [@Boulanger2003] with permission of ASCE).

The value of $K_\alpha$ can be computed from CPT and SPT resistances using the correlations

$$\xi_R = -0.086\,Q_{tn} - 0.334 \tag{9.34a}$$

where $Q_{tn} = \ln\!\!\left(\dfrac{q_c + 100 K_0 \sigma'_v / P_a}{P_a}\right)$, and

$$\xi_R = -\frac{(N_1)_{60}}{\ln\!\!\left(\dfrac{100 + K_0 \sigma'_v / P_a}{P_a}\right)} \tag{9.34b}$$

The adjustment factor for static shear stress is, compared to other adjustment factors, based on a limited amount of laboratory test data.

#### Age Adjustment

Liquefaction has been observed to occur more frequently in younger soil deposits such as man-made fills and Holocene natural deposits than in older (e.g., Pleistocene and older) deposits [@YoudHoose1977][@YoudPerkins1978][@ObermeierEtAl1990][@LewisEtAl1999]. Mechanisms such as cementation (chemical precipitation), particle reorientation under weak shaking in small earthquakes or other vibrations and increased lateral stresses may play roles in increased liquefaction resistance, but the actual mechanisms are not well understood [@Mitchell1986][@Mitchell2008][@Schmertmann1991]. Laboratory investigations of age effects are difficult because of the time involved and the difficulty of replicating aging mechanisms in the laboratory, but limited laboratory testing has shown that liquefaction resistance increases with age (Figure 9.48). Using both field and laboratory test data, Hayati and Andrus (2009) [@HayatiAndrus2009] proposed the use of an age-related deposit resistance adjustment factor, $K_{DR}$, intended to account for diagenetic processes (e.g., age, cementation, stress history) that affect low-strain behavior but are destroyed by larger strain deformations.

$$K_{DR} = 0.13\,\log t + 0.83 \tag{9.35}$$

where $t$ is time since deposition (or last critical disturbance) in years. This relation gives a value of $K_{DR} = 1.0$ at a reference time of 23 years, which was considered appropriate since many liquefaction case histories are associated with deposits with ages of 1–100 years at the time of shaking.

**Figure 9.48.** Relationship between strength gain and age. (Modified from Arango et al., 2000 [@ArangoEtAl2000] with permission of Elsevier Science and Technology Journals). Strength gain factor is relative to strengths obtained from laboratory tests performed very shortly after specimen preparation except for that of Hayati and Andrus (2009) [@HayatiAndrus2009] where the inclusion of laboratory data suggested a reference age of 23 years.

The deposit resistance factor is then applied to the reference-age CRR as

$$\text{CRR}_\text{aged} = \text{CRR}_\text{ref} \cdot K_{DR} \tag{9.36}$$

Since the actual age of a soil deposit is usually unknown, and because it can be reset to zero after liquefaction caused by a previous earthquake, Hayati and Andrus (2009) [@HayatiAndrus2009] proposed that the value of $K_{DR}$ could be obtained from shear wave velocity measurements. Since the aging processes thought to increase liquefaction resistance also tend to increase shear wave velocity, and available shear wave velocity correlations are based primarily on "young" sands, the measured to estimated velocity ratio, MEVR, defined as

$$\text{MEVR} = \frac{V_{s1,\,\text{measured}}}{V_{s1,\,\text{estimated}}} \tag{9.37}$$

was taken as an indicator of age with $V_{s1,\,\text{estimated}}$ obtained by correlation to CPT or SPT resistance, using Equation (6.77). The value of MEVR can then be used to estimate $K_{DR}$ as

$$K_{DR} = 1.08\,\text{MEVR} - 0.08 \tag{9.38}$$

Schneider and Moss (2011) [@SchneiderMoss2011] introduced the notion of a normalized rigidity index,

$$K_G = \frac{G_\text{max}}{q_t} \cdot Q_{tn}^{0.75} \tag{9.39}$$

where $G_\text{max}$ = maximum shear modulus (typically obtained from measured shear wave velocity), $q_t$ is given in Equation (6.53) and has the same units as $G_\text{max}$, and $Q_{tn}$ is as defined in Equation (6.61). Soils that are very stiff at low strain levels relative to their penetration resistance (which is mobilized at high strain levels) tend to have high $K_G$ values. Schneider and Moss (2011) [@SchneiderMoss2011] showed laboratory and field data indicating that older soils exhibited higher $K_G$ values than younger soils (Figure 9.49); Holocene sands tended to have $K_G$ values in the range of 110–330 (with a median of 220) and aged, cemented, and calcareous sands had values of 330–1,100. Based on frozen samples of Holocene and Pleistocene soils [@Roy2008], Schneider and Moss (2011) [@SchneiderMoss2011] postulated that soils with higher $K_G$ values (e.g., Pleistocene sands, which had a median $K_G = 408$) had a higher liquefaction resistance than Holocene sands for $q_{c1N}$ values less than about 150.

Robertson (2016) [@Robertson2016] proposed a modified version of the normalized rigidity index,

$$K_G^* = \frac{G_\text{max}}{q_n} \cdot Q_{tn}^{0.75} \tag{9.40}$$

where $q_n = q_t - \sigma_v$. Robertson used the term microstructure to describe post-depositional particle-scale features such as cementation, secondary compression, thixotropy, cold welding, and particle reorientation that tend to increase with the age of a soil deposit and found that soils with microstructure had $K_G^*$ values greater than 330 and soils without had lower $K_G^*$ values (Figure 9.50).

**Figure 9.49.** Correlations between normalized cone tip resistance and maximum shear modulus measured in seismic cone tests for various soil deposits. (Schneider and Moss, 2008 [@SchneiderMoss2008] with permission of Emerald Publishing Limited.)

**Figure 9.50.** Proposed chart for identifying soils with microstructure. (Robertson, 2016 [@Robertson2016] with permission of P.K. Robertson.)

Since they depend on essentially the same factors, MEVR and $K_G^*$ should be related and Robertson suggested that

$$K_G^* = \text{MEVR} \tag{9.41}$$

While laboratory studies and empirical evidence leave little question that liquefaction resistance increases with age, the data used to quantify that effect are still sufficiently sparse that the age correction is not commonly used in practice. It could be used in a logic tree framework, however, with a weighting factor interpreted as a subjective probability (i.e., a degree-of-belief) that will likely approach 1.0 as further evidence of age effects is brought to light.

#### Saturation Adjustment

Seasonal or tidal fluctuations in groundwater level, or the generation of gases due to decaying organic material, can lead to zones of soil that are not completely saturated below the water table. As discussed in Section 6.2.4, the air bubbles that exist in the voids of partially saturated soils are so much more compressible than the water in the voids that the air/water mixture has a very high composite compressibility. The tendency for contraction of the soil skeleton, therefore, is accommodated by simple compression of the air bubbles, which occurs without producing significant pore pressure.

Cyclic triaxial tests on silty sands from Japan [@TsukamotoEtAl2014] showed that they generated pore pressure during the tests, but that their liquefaction resistances increased quickly when the degree of saturation dropped below 100% (Figure 9.51). Zhang et al. (2016) [@ZhangEtAl2016] used laboratory data from tests on Toyoura sand and Nevada sand, along with a constitutive model, to investigate the effects of saturation on liquefaction resistance and developed a design chart for those soils (Figure 9.52). These laboratory results give an indication of the sensitivity of liquefaction resistance to degree of saturation.

The propagation of p-waves through saturated sands occurs through the porewater rather than the softer soil skeleton (Section 6.5.2). As indicated in Section 6.5.2, the p-wave velocity of water (at 20°C) is 1,460 m/sec, so measured p-wave velocities lower than that value can indicate partial saturation. Laboratory tests on five liquefiable soils with mean grain sizes ranging from 0.04 to 1.25 mm and relative densities from 40% to 100% indicated [@HossainEtAl2013] that partial saturation increased liquefaction resistance by a saturation adjustment factor

$$K_S = \frac{\text{CRR}_\text{unsat}}{\text{CRR}_\text{sat}} = \begin{cases} 0.95 + \left[1.95\,\ln(V_p/100) - 1.3\right]^{-2} - 0.03\Bigl(1.31 + \exp\!\bigl(2.85\,M(D_r,D_r,B)\bigr)\Bigr) & \text{for } V_p < 1400\ \text{m/sec} \\ 1.0 & \text{for } V_p \geq 1400\ \text{m/sec} \end{cases} \tag{9.42}$$

where $B = 3.5(V_p/V_s)^{4/3} - 3.5(V_p/V_s)$ [@Kokusho2000a]. This adjustment, shown in Figure 9.53, is similar to that of Ishihara et al. (2001) [@IshiharaEtAl2001]. Data from clean and silty sands from Christchurch [@BakiEtAl2023] showed generally consistent behavior at p-wave velocities greater than 500 and 750 m/sec, respectively; the resistance of the silty sand increased very quickly at p-wave velocities lower than 750 m/sec.

**Figure 9.51.** Variation of cyclic resistance ratio with degree of saturation for Inage sand and Urayasu sand. (Tsukamoto et al., 2014 [@TsukamotoEtAl2014] with permission of Y. Tsukamoto.)

**Figure 9.52.** Proposed design chart for liquefaction resistance of unsaturated sand. (Zhang et al., 2016 [@ZhangEtAl2016] with permission of ASCE.)

**Figure 9.53.** Variation of saturation adjustment factor, $K_S$, with p-wave velocity for M8 event.

As in the case of the age adjustment, the saturation adjustment is not explicitly used in typical current practice, as measurements of both $V_p$ and $V_s$ are not commonly available, and it is generally conservative to assume that all soils below the water table are saturated. In critical situations, or where the costs associated with the assumption of saturation are excessive, a saturation adjustment supported by field measurements can provide a more accurate indication of liquefaction potential.

#### Example 9.4

A 4-m-thick layer of dense clayey sand fill with a moist unit weight of 21.5 kN/m³ is underlain by a natural layer of silty sand at 4–5 m depth at a level-ground site. The silty sand has an average $q_{c1Ncs}$ value of 120 and a dry unit weight of 17.5 kN/m³. Groundwater was encountered at the bottom of the fill. Historical records indicate that the silty sand layer was deposited during a flood 100 years ago; recent tests indicate that the p-wave velocity of the layer is 1,420 m/sec. Compute the expected cyclic resistance ratio of the silty sand layer when subjected to ground motion with a peak ground surface acceleration of 0.34g from a M6.8 earthquake.

**Solution:**

Calculating the vertical total and effective stress at the center of the silty sand layer, the dry unit weight of 17.5 kN/m³ corresponds to a saturated unit weight of 20.6 kN/m³ and a buoyant unit weight of 10.8 kN/m³ so the vertical stresses are

$$\sigma_v = (4\ \text{m})(21.5\ \text{kN/m}^3) + (0.5\ \text{m})(20.6\ \text{kN/m}^3) = 96.3\ \text{kPa}$$

$$\sigma'_v = (4\ \text{m})(21.5\ \text{kN/m}^3) + (0.5\ \text{m})(10.8\ \text{kN/m}^3) = 91.4\ \text{kPa}$$

From Equation (9.26), the median standardized cyclic resistance ratio is 0.209 (see calculation in Example 9.2). The CRR value for the actual conditions in the silty sand layer is calculated using the standardized values and the applicable adjustment factors. For this case, adjustments are needed for number of loading cycles, overburden stress, initial static shear stress, diagenetic (age-related) factors, and saturation. The number of cycles correction is computed from Equation (9.30). The magnitude correction, using the decoupled version of $\text{MSF}_{BI}$, is expressed in terms of the number of cycles adjustment factor, $K_N$. From Table 9.6, it is calculated as:

$$\text{MSF}_\text{max} = 1.09 + \frac{q_{c1Ncs}}{180} = 1.09 + \frac{120}{180} = 1.386$$

Then

$$K_N = \frac{1 + (\text{MSF}_\text{max} - 1)(8.64\,\exp(-M/4) - 1.325)}{0.5803 + 2.7368\,\exp(-M/4)} = \frac{1 + (1.386 - 1)(8.64\,\exp(-6.8/4) - 1.325)}{0.5803 + 2.7368\,\exp(-6.8/4)} = 1.016$$

The overburden adjustment factor (Table 9.7) can be computed as

$$K_\sigma = 1 - \frac{\ln(\sigma'_{vo}/P_a)}{37.3 - 8.27\,(q_{c1Ncs})^{0.264}} = 1 - \frac{\ln(91.4\ \text{kPa}/101.3\ \text{kPa})}{37.3 - 8.27(120)^{0.264}} = 1.013$$

The site is level, so the static shear stress adjustment factor, $K_\alpha = 1.0$. With no information other than the estimated age of the layer, the age-related adjustment factor (Equation 9.35) can be estimated as $K_{DR} = 0.13\,\log(100) + 0.83 = 1.09$. Finally, the saturation adjustment factor (Equation 9.42), $K_S = 1.0$ since $V_p > 1,400\ \text{m/sec}$. Therefore, the cyclic resistance ratio is

$$\text{CRR} = \text{CRR}_\text{std} \cdot K_N \cdot K_\sigma \cdot K_\alpha \cdot K_{DR} \cdot K_S = (0.209)(1.016)(1.013)(1.0)(1.09)(1.0) = 0.234$$

### 9.5.4.5 Implications of Non-Triggering

As seen in laboratory and physical model tests, shear strains and deformations remain relatively small until pore pressures become very high and liquefaction is initiated. If liquefaction is not initiated, i.e., if $FS_L > 1.0$, some pore pressure may still exist at the end of shaking, and its dissipation may lead to some degree of settlement. The amount of excess pore pressure at level-ground sites can be estimated from laboratory tests as shown in Figure 9.54. Other procedures for estimation of pore pressure generation are based on cyclic stresses [@ParkAhn2013], cyclic strains [@DobryEtAl1982][@MatasovicVucetic1993][@CetinBilge2012], and dissipated energy [@PolitoEtAl2008].

**Figure 9.54.** Relationship between residual excess pore pressure ratio and factor of safety against liquefaction for level-ground sites. (After Marcuson and Hynes, 1990 [@MarcusonHynes1990].)

### 9.5.4.6 Limitations of the Simplified Method

The simplified method for evaluation of liquefaction potential has been widely and successfully used in engineering practice for over 50 years. It has been updated a number of times as large earthquakes have occurred and produced valuable case histories and as new research, tests, and interpretive tools have advanced understanding of its basic mechanics. It remains limited, however, by a number of factors including: (a) the binary representation of triggering by the presence or absence of surface manifestation to represent the complex mechanical and hydraulic phenomena that occur beneath the surface during and after earthquake shaking, (b) the characterization of loading by a PGA value expected to have occurred in the absence of any pore pressure generation, a magnitude value that is loosely correlated to duration or number of loading cycles because path and site effects are not directly considered, and by the generic (i.e., ergodic) representation of the variation of shear stress with depth, (c) the historical characterization of case history sites by a single critical layer when multiple layers may contribute to the development, or prevention, of surface manifestation, and (d) the implicit assumption, in both case history interpretation and forward prediction, that all layers act independently of each other.

Most of these limitations are relics of the available data and measurement, interpretation, and computational capabilities that existed when the simplified method was first developed. Advances in strong motion instrumentation, field reconnaissance tools, ground motion modeling, site characterization, constitutive modeling, (nonlinear, effective stress) ground response analysis, and database management allow improved characterization and interpretation of liquefaction case histories and should pave the way for improved empirical triggering models in the near future.

## 9.5.5 Cyclic Strain Approach

As discussed in Section 9.5.2.2, stress-controlled cyclic tests showed that the CRR used to characterize liquefaction resistance in the cyclic stress approach was sensitive to a variety of in situ factors (age, soil fabric, prior shaking history, etc.) that could not be replicated in reconstituted laboratory test specimens. Subsequent strain-controlled testing showed that the volumetric strain of dry sands [@SilverSeed1971][@Youd1972][@MartinEtAl1975] and pore pressure generation in saturated sand [@DobryLadd1980][@DobryEtAl1982][@CetinBilge2012] were not significantly affected by those factors. These observations led to the now widespread recognition that pore pressures in liquefiable soils are more closely related to shear strain amplitude than shear stress amplitude. In an effort to develop a more robust approach to the liquefaction problem, Dobry and Ladd (1980) [@DobryLadd1980] and Dobry et al. (1982) [@DobryEtAl1982] described an approach that used cyclic strains rather than cyclic stresses to characterize earthquake-induced loading and liquefaction resistance. The cyclic strain approach has both advantages and disadvantages relative to the cyclic stress approach.

### 9.5.5.1 Characterization of Earthquake Loading

In the cyclic strain approach, earthquake-induced loading is expressed in terms of the amplitude of a series of equivalent constant strain loading cycles. As in the cyclic stress approach, a transient history, in this case of shear strain, must be converted to an equivalent series of uniform cycles. This leads to two primary difficulties in characterizing loading in the cyclic strain approach.

First, an equivalent cyclic shear strain amplitude must be estimated. This can be accomplished by performing a ground response analysis, but it should be recognized that ground response analyses predict strains with much higher variability than they predict stresses, particularly for highly nonlinear conditions. The increased uncertainty in the shear strain induced in the soil by earthquake shaking reduces the benefits of decreased uncertainty in pore pressure generation given some level of cyclic shear strain. Dobry et al. (1982) [@DobryEtAl1982] proposed a simplified method for estimating the amplitude of the uniform cyclic strain from the amplitude of the uniform cyclic stress of Equation (9.9):

$$\gamma_\text{cyc} = 0.65 \frac{a_\text{max}}{g} \cdot \frac{\sigma_v r_d}{G(\gamma_\text{cyc})} \tag{9.43}$$

where $G(\gamma_\text{cyc})$ is the secant shear modulus of the soil at $\gamma = \gamma_\text{cyc}$. Since $\gamma_\text{cyc}$ appears on both sides of Equation (9.43), the value of $G(\gamma_\text{cyc})$ must be obtained iteratively from a measured $G_\text{max}$ profile and appropriate modulus reduction curve (Section 6.6.3). At low strain levels, where the soil may exhibit relatively linear behavior, shear strains can be predicted more accurately when stiffnesses are obtained from measured shear wave velocities.

The second difficulty relates to the determination of the number of equivalent loading cycles. The conversion procedure is analogous to that used in the cyclic stress approach. The equivalent number of strain cycles, $N_\text{eq}$, depends on the earthquake magnitude. The implied consistency between number of stress cycles and number of strain cycles, however, may not exist [@CarterSeed1988][@GreenTerri2005].

### 9.5.5.2 Characterization of Liquefaction Resistance

Despite its difficulties in characterizing loading, the cyclic strain approach has two significant advantages in characterizing liquefaction resistance. First, the existence of the volumetric threshold shear strain provides a screening level (Section 9.5.3.2) of response below which no pore pressure generation should be anticipated (if strains are too small to produce volumetric strain under drained conditions, they will be too small to produce excess pore pressure under undrained conditions). Second, laboratory tests have shown excess pore pressure to be closely related to strain amplitude, and to be quite insensitive to many of the factors known to significantly affect the shear stress amplitude required to initiate liquefaction.

Figure 9.55a shows the pore pressure ratio produced by ten cycles of strain-controlled loading on two different sands prepared by three different methods at three different initial effective confining stresses. Figure 9.55b shows pore pressure ratios following stress-controlled loading cycles plotted against the peak shear strain produced by that loading; the different symbols represent different methods of specimen preparation, and the test conditions range from relative densities of 35%–100% and initial effective stresses of 40–400 kPa. The insensitivity of the generated pore pressure to factors other than cyclic strain amplitude illustrated in Figure 9.55 is a hallmark of the cyclic strain approach. The distribution of pore pressure ratio for a given maximum strain amplitude is relatively narrow, again indicating a close relationship between pore pressure and strain amplitude.

Cyclic simple shear tests [@Bhatia1980][@Finn1981][@DobryEtAl1982][@StamatopoulosEtAl1999] and centrifuge tests [@SharpEtAl2000][@AdalierElgamal2005] have shown, however, that the cyclic strain amplitude required to initiate liquefaction in a given number of cycles increases with increasing overconsolidation ratio. Preshaking or prestraining, either under drained conditions or under undrained conditions followed by pore pressure dissipation, can cause effects similar to those of overconsolidation and also increase liquefaction resistance [@FinnEtAl1970][@Seed1979][@Bhatia1980][@Finn1981][@ElSekellyEtAl2016].

In the cyclic strain approach, laboratory-based curves of the types shown in Figure 9.55 are used to characterize the liquefaction resistance of the soil. Note that initial liquefaction ($r_u = 1.0$) is reached at shear strains ranging from about 0.5% to as much as 50% in the tests shown in Figure 9.55.

Using a modulus reduction curve for sand, relationships between $G_\text{max}$ and $V_s$, and the definitions of secant shear modulus and cyclic stress-based CSR, a relationship between CRR, $V_{s1}$, and cyclic shear strain $\gamma_c$, can be established [@DobryAbdoun2011][@DobryAbdoun2015]. By comparing these relationships to the Andrus and Stokoe (2000) [@AndrusStokoe2000] shear wave velocity-based CRR curve, the stress-based CRR curve was interpreted as a curve of approximately constant cyclic shear strain at $\gamma_c \approx 0.03\%$ for $V_{s1}$ values less than about 160 m/sec. While a boundary curve drawn for that strain level was found to separate cases of liquefaction and non-liquefaction for case histories of uncompacted clean and non-plastic silty sand fills (FC up to about 34%) extracted from the Andrus and Stokoe (2000) [@AndrusStokoe2000] database, the inferred triggering strain level is considerably lower than the strains corresponding to triggering in laboratory tests (e.g., in Figure 9.55).

An investigation of natural silty sands with non-plastic fines from the Imperial Valley of California suggested that liquefaction triggered at shear strains of 0.1%–0.2%. On that basis, Dobry et al. (2015) [@DobryEtAl2015] suggested that a strain-based CRR of

$$\text{CRR} = \frac{a \cdot V_{s1}}{\text{MSF}} \tag{9.44}$$

could be used at $V_{s1} < 200\ \text{m/sec}$ with $a = 0.033$ for uncompacted fills and $a = 0.065$ for Imperial Valley silty sands. The differences in resistance were indicated as being at least partially explained by the preshaking of the silty sands in the highly active Imperial Valley area.

The triggering strain corresponding to $\text{CRR} = 0.3$ ($V_s \gtrsim 200\ \text{m/sec}$) for the Andrus and Stokoe (2000) [@AndrusStokoe2000] CRR curve is much higher — on the order of 0.27% to 0.56% — but still much lower than the values observed in laboratory tests [@DobryAbdoun2015]. These materials generally correspond to denser, overconsolidated, preshaken, or compacted sands. The large difference between the triggering strain levels measured in the laboratory and inferred from field case histories was attributed to differences in numbers of loading cycles (greater in the field than in the laboratory tests), two-directional (field) vs. one-directional (laboratory) shaking, and pore pressure redistribution (exists in field but not in laboratory tests). Corrections for the first two of these factors indicated that the triggering strain level for uncompacted fills would increase from 0.03% to 0.06%–0.12%. The upward flow of porewater during shaking, as measured in six centrifuge tests, was postulated to explain the remainder of the difference.

The apparent variability of the triggering strain level with $V_{s1}$, its inconsistency with laboratory data, and its dependence on hydraulic as well as ground motion parameters suggest that further research is required to better clarify its utility for the evaluation of liquefaction potential. It does, however, provide a useful link between penetration test-based and shear wave velocity-based triggering procedures, at least for very loose soils.

**Figure 9.55.** Variation of pore pressure ratio with cyclic strain amplitude for (a) specimens prepared by different methods and subjected to strain-controlled loading (after Dobry and Ladd, 1980 [@DobryLadd1980]), and (b) specimens prepared by different methods at different densities and effective stress levels and subjected to stress-controlled loading (after Cetin and Bilge, 2012 [@CetinBilge2012] with permission of ASCE).

### 9.5.5.3 Evaluation of Liquefaction Potential

Liquefaction potential may be evaluated in the cyclic strain approach in a manner similar to that used in the cyclic stress approach. The cyclic loading imposed by the earthquake, characterized by the amplitude of a series of $N$ uniform strain cycles, is compared with the liquefaction resistance, which is expressed in terms of the cyclic strain amplitude required to initiate liquefaction in the same number of cycles. Liquefaction can be expected at depths where the cyclic loading exceeds the liquefaction resistance. Since loading and resistance are characterized in terms of strains rather than stresses, the cyclic strain approach does not yield a stress-based factor of safety against liquefaction, but the ratio of strain demand to strain at triggering of liquefaction can be viewed as a demand-capacity ratio, or DCR, as often used in structural earthquake engineering.

The primary advantage of the cyclic strain approach derives from the strong relationship between pore pressure generation and cyclic strain amplitude. For a given soil, excess pore pressure can be predicted more accurately from cyclic strains than from cyclic stresses. As previously stated, however, cyclic strains are more difficult to predict accurately than cyclic stresses. The cyclic strain approach, at present, relies heavily on laboratory data and, more recently, high-quality physical (centrifuge) modeling, but has not been validated against field case histories to the extent that the cyclic stress approach has been. As a result, the cyclic strain approach is not used as commonly as the cyclic stress approach in current geotechnical earthquake engineering practice.

## 9.5.6 Energy Dissipation Approach

The use of dissipated energy as a measure of liquefaction resistance offers a number of potential advantages; it is related to both cyclic stresses and cyclic strains, it is a scalar quantity that reflects duration as well as amplitude, it can be related to fundamental earthquake parameters, and it can be related to inherently stochastic earthquake ground motions in a way that methods based on peak ground motion parameters alone cannot.

The densification of dry soil under cyclic loading involves rearrangement of grains under stress and hence the expenditure of energy. As a cyclically loaded dry soil densifies and approaches its minimum void ratio, the amount of energy required to further rearrange individual soil grains increases. If the soil is saturated, however, the tendency for densification causes the pore pressure to increase and the interparticle contact forces to decrease. As these contact forces decrease, the amount of energy needed to rearrange soil grains decreases. By combining these observations, Nemat-Nasser and Shokooh (1979) [@NematNasserShokooh1979] developed a simple, unified theory that related densification under drained conditions and pore pressure generation under undrained conditions to dissipated energy.

Davis and Berrill (1982) [@DavisBerrill1982] and Berrill and Davis (1985) [@BerrillDavis1985] built upon this idea, characterizing the energy density arriving at a particular site by means of the total energy released by the earthquake (Equation 2.4) adjusted for geometric spreading and crustal damping, and the rate of pore pressure generation as a function of SPT resistance. Calibration against field case history data yielded an expression for pore pressure ratio

$$r_u = \frac{A \cdot M^{0.5} \cdot r^{-0.75}}{\left(\sigma'_{v0}\right)^{1.5} N^{0.75}} \tag{9.45}$$

where $A$ is a normalized attenuation function that accounts for material damping, $M$ is earthquake magnitude, $r$ is the distance to the center of energy release, $N$ is average corrected SPT resistance, and $\sigma'_{v0}$ is initial vertical effective stress in kPa. Equation (9.45) combines loading and resistance to provide a direct prediction of pore pressure ratio rather than the factor of safety most commonly used to characterize liquefaction potential. This simple fundamental procedure has been supplanted by more detailed recent procedures.

### 9.5.6.1 Characterization of Earthquake Loading

Kokusho (2013) [@Kokusho2013] developed an energy-based procedure that explicitly characterized earthquake loading and liquefaction resistance. Two alternative procedures for estimating the energy density in a soil deposit were proposed. Both are based on the incoming energy, i.e., that associated with upward-traveling shear waves, in order to eliminate the effects of destructive interference between upward- and downward-traveling waves that can lead to the appearance of weak shaking at certain depths in a soil profile.

The first procedure, which can be used when ground motions at the base (taken as approximately 100 m depth) are not known, estimates the upward-traveling energy density in soil layer $i$ using the Gutenberg-Richter relationship for total energy release (Equation 2.4), a spherical geometric spreading relationship, and the ratio of soil layer to base layer impedance:

$$E_{u,i} = \frac{\rho_i V_{s,i}}{\rho_\text{base} V_{s,\text{base}}} \cdot \frac{10^{1.5 M + 1.8}}{4\pi R^{0.7}} \tag{9.46}$$

where $R$ is the distance to the center of energy release. The second approach, which assumes that base motions are known or estimated and can be used to perform site response analyses, computes the upward-traveling energy density as

$$E_{u,z} = \int_0^\infty (\rho V_s)_z \cdot u_{u,z}(t) \, dt \tag{9.47}$$

where $(\rho V_s)_z$ = specific impedance of soil at depth $z$, and $u_{u,z}$ = particle velocity of upward-traveling wave at depth $z$. The upward-traveling wave can be separated from the downward-traveling wave by means of equivalent linear analyses (as half the outcrop motion at a particular depth).

### 9.5.6.2 Characterization of Liquefaction Resistance

Soil specimens liquefied in cyclic triaxial tests show a consistent relationship between pore pressure ratio and normalized dissipated energy for a wide range of relative densities [@Kokusho2013]. Dissipated energy was computed by integration of stress-strain data up to the point of triggering (and thus includes the softening effects of pore pressure generation). Combining triaxial test data with SPT correlations, Kokusho (2013) [@Kokusho2013] described the normalized energy corresponding to 5% double-acting strain in 20 cycles of loading as

$$\frac{\Delta W}{\sigma'_c} = \frac{\int \sigma_d \, d\varepsilon_a}{\sigma'_c} = -0.032\,R_L^2 + 0.48\,R_L - 2.40 \tag{9.48}$$

where $\sigma'_c$ is the isotropic effective stress during consolidation and $R_{L20}$ is the cyclic resistance ratio at 20 cycles of loading, which is related to SPT resistance by

$$R_L = \begin{cases} 0.0882\,\sqrt{N_1 - 1.7} & \text{for } N < 1.7 \\ 0.0882\,\sqrt{N_1 - 1.7} + 1.6 \times 10^{-6}(N - 1.7)^{4.5} & \text{for } N \geq 1.7 \end{cases} \tag{9.49}$$

subject to a minimum value of $R_{L20} = 0.1$, where $N_1$ is the effective stress-adjusted SPT resistance. Figure 9.56a illustrates the variation of normalized dissipated energy with SPT resistance for three strain levels.

Using the 253 case histories compiled by Boulanger and Idriss (2014) [@BoulangerIdriss2014] and a different procedure from Kokusho (2013) [@Kokusho2013] for defining $\Delta W$ and the triggering of liquefaction, Ulmer et al. (2023) [@UlmerEtAl2023] developed a probabilistic CPT- and energy-based triggering model of the form

$$P_L = -\Phi\!\left(\frac{3.352 - 1.224\,\ln(q_{c1Ncs}) - 7.52\,\ln\!\left(\Delta W \cdot \sigma'_{vo}\right)}{1.590}\right) \tag{9.50}$$

Dissipated energy was computed as the product of a total stress-interpreted, single-cycle work increment based on a representative shear stress amplitude and the number of equivalent cycles of loading (and consequently unaffected by pore pressure generation). The variation of normalized energy required to trigger liquefaction with CPT tip resistance is illustrated in Figure 9.56b.

**Figure 9.56.** (a) Relationship between normalized dissipated energy to reach strain levels of 2%, 5%, and 10% and SPT resistance (after Kokusho, 2013 [@Kokusho2013] with permission of Canadian Science Publishing) and (b) percentiles of normalized energy required to trigger liquefaction by method of Ulmer et al. (2023) [@UlmerEtAl2023]. Note that the normalized energies for the two relationships shown here are defined differently.

**Table 9.8.** Expressions for energy density (J/m³) required to trigger liquefaction in various laboratory studies.

- $\log W_m = 2.002 + 0.00477\,D_r + 0.0116\,\sigma'$ — Based on 27 strain-controlled torsional shear tests on Reid Bedford sand — Figueroa et al. (1994) [@FigueroaEtAl1994]

- $\log W_m = 2.4597 + 0.00448\,D_r + 0.0115\,\sigma'$ — Based on 30 centrifuge tests on Reid Bedford sand — Dief and Figueroa (2001) [@DiefFigueroa2001]

- $\log W_m = 2.1028 + 0.004566\,D_r + 0.005685\,\sigma' + 0.001821\,FC - 0.02868\,C_u + D_r\cdot 2.0214$ — Based on 283 cyclic triaxial, torsional, and simple shear tests on various sands — Baziar and Jafarian (2007) [@BaziarJafarian2007]

- $\log W_m = 2.300 \cdot D_r^2 + (0.5\,D_r + \sigma'_m)(D_r \times 300) + 3\,\sigma'_m\left(D_r + \sigma'_m - D_r\cdot FC\cdot C_u\right)^{0.5} - 1.5$ — Based on 283 cyclic triaxial, torsional, and simple shear tests on various sands plus 18 centrifuge tests — Alavi and Gandomi (2012) [@AlaviGandomi2012]

*Source: After Alavi and Gandomi (2012) [@AlaviGandomi2012]. $C_u$, coefficient of uniformity; $D_{50}$, mean grain size (mm); $D_r$, initial relative density (%); FC, fines content (%); $\sigma'_m$, initial mean effective stress (kPa).*

Several investigators have used laboratory test results to determine the dissipated energy density required to trigger liquefaction in the soils that were tested. Several representative relationships are listed in Table 9.8. These relationships characterize the soil in terms of mean effective stress and relative density, so an empirical correlation between relative density and some form of measured in situ parameter (e.g., $(N_1)_{60}$, $q_{c1}$, $V_{s1}$) would be required for practical application.

### 9.5.6.3 Evaluation of Liquefaction Potential

Liquefaction potential can be characterized in terms of an energy-based factor of safety defined as the ratio of energy capacity to energy demand. While interesting from the standpoint of the theoretical basis established by Nemat-Nasser and Shokooh (1979) [@NematNasserShokooh1979], the dissipated energy approach suffers from the difficulty in predicting the energy demands imposed on a particular element of soil at some depth below the ground surface, and on the lack of a direct empirical correlation between liquefaction resistance (in terms of energy capacity) and commonly measured in situ test parameters.

## 9.5.7 Effective Stress Response Analysis Approach

As discussed in Section 7.5.3.3, nonlinear effective stress site response models have the ability to predict pore pressure generation in potentially liquefiable layers within specific soil profiles subjected to specific input motions. In such analyses, the loading applied to the soil is computed on a site- and motion-specific basis rather than characterizing site response by a parameter ($r_d$) based on the average response of many different profiles, and the motion by relatively crude and simplistic parameters ($a_\text{max}$ and $M$). Thus, for sites with strong impedance contrasts, velocity inversions, or other atypical features, or for motions with atypical features such as directivity pulses or very long (or short) durations, effective stress analyses can provide insight into liquefaction behavior that empirical procedures cannot. The accuracy of an effective stress analysis, however, depends on how accurately pore pressure generation, redistribution, and dissipation can be modeled.

Several approaches to the modeling of pore pressure generation have been proposed and implemented into nonlinear site response analyses. These range from relatively simple models in which pore pressures increase monotonically to sophisticated constitutive models that account for phenomena such as phase transformation (PT) behavior that cause pore pressures and shear moduli to fluctuate even within individual loading cycles.

### 9.5.7.1 Pore Pressure Models

Cyclic nonlinear stress-strain models (Section 6.4.5.2) use an empirical backbone curve and a series of unloading-reloading rules that govern cyclic behavior. Pore pressure prediction is accomplished by pore pressure models [@MartinEtAl1975][@IshiharaTowhata1980][@FinnBhatia1981][@DobryEtAl1985][@VuceticDobry1988] that can predict the generation of pore pressure under irregular cyclic loading conditions. In these models, the computed pore pressure is used to degrade, or soften, the backbone curve as the effective stress (and soil stiffness) decreases. Pore pressure models based on cyclic stresses, cyclic strains, and dissipated energy have been proposed.

#### Cyclic Stress-Based Pore Pressure Models

Based on cyclic simple shear data [@DeAlbaEtAl1976], Seed et al. (1975) [@SeedEtAl1975] developed an expression for the pore pressure ratio produced by uniform amplitude harmonic loading

$$r_u = \frac{1}{\pi}\,\arcsin\!\left(2\left(\frac{N}{N_L}\right)^{1/\alpha} - 1\right) \tag{9.51}$$

where $N$ = number of loading cycles, $N_L$ = number of cycles to liquefaction, and $\alpha$ = parameter related to soil properties and test conditions with an average value of 0.7. Polito et al. (2008) [@PolitoEtAl2008] proposed that $\alpha$ be determined as a function of relative density, fines content, and cyclic stress ratio:

$$\alpha = 0.5058 + 0.01166\,FC + 0.007397\,D_r + 0.01034\,CSR \tag{9.52}$$

where FC and $D_r$ are in percent. This type of model suffers from the need to convert actual, transient loading histories to equivalent uniform loading histories, and the need to define the triggering of liquefaction in terms of a specific number of equivalent cycles. It predicts pore pressures that increase monotonically from the initial hydrostatic values.

Martin et al. (1975) [@MartinEtAl1975] proposed that increments of vertical strain from dry sands could be related to increments of pore pressure in saturated sands when subject to undrained loading. In a drained test, slip at the soil grain contacts produces an increment of contractive vertical strain, $\Delta\varepsilon_{vd}$ (Figure 6.111). Under undrained conditions, however, some of the vertical stress resisted by the soil skeleton is transferred to the more incompressible porewater, effectively unloading the soil skeleton and producing an increment of rebound volumetric strain, $\Delta\varepsilon_{vr}$. If the pore water is taken to be incompressible relative to the soil skeleton, the two volume change increments are equal in magnitude but opposite in sign,

$$\Delta\varepsilon_{vr} = -\Delta\varepsilon_{vd} \tag{9.53}$$

If the tangent constrained modulus in one-dimensional rebound is taken as $M_r$, and $d\sigma'_v = -du$, then $du/d\varepsilon_{vr} = -M_r$. This allows the pore pressure increment under undrained conditions to be related to the vertical strain increment that would occur under drained conditions as:

$$\Delta u = -M_r\,\Delta\varepsilon_{vd} \tag{9.54}$$

This approach was used to develop the first simple models that could predict pore pressure generation under irregular cyclic loading.

#### Cyclic Strain-Based Pore Pressure Models

Dobry et al. (1982) [@DobryEtAl1982] used the results of cyclic torsional triaxial tests to predict the pore pressure ratio after $N$ cycles of strain-controlled loading, $r_{u,N}$. Vucetic and Dobry (1986) [@VuceticDobry1986] modified that work and proposed that

$$r_{u,N} = \frac{(\gamma_c - \gamma_{tv})^b\,f\,p\,N^F}{(\gamma_c - \gamma_{tv})^b\,f\,p\,N^F + 1} \tag{9.55}$$

where $\gamma_c$ = cyclic strain amplitude, $\gamma_{tv}$ = volumetric threshold shear strain (Section 6.4.3.1), $f = 1$ for uni-directional shaking or $2$ for bi-directional shaking, and $p$, $F$, and $b$ are coefficients obtained by fitting to the results of laboratory tests.

Cetin and Bilge (2012) [@CetinBilge2012] used a database of 99 cyclic simple shear and cyclic triaxial tests to relate pore pressure ratio to peak shear strain, relative density, and effective stress:

$$r_{u,N} = 1 - \exp\!\left[-\ln\!\left(\frac{\gamma_{\max,N}^{0.407}}{0.486 + 0.025\ln(\sigma'_v/100) - D_r + \gamma_{\max,N}^{0.620}}\right)\right] \tag{9.56}$$

where $\gamma_{\max,N}$ = maximum shear strain in percent after $N$ cycles, $\sigma'_v$ = initial vertical effective stress in kPa, and $D_r$ = relative density in percent. Cetin and Bilge (2012) [@CetinBilge2012] indicated that Equation (9.56) produced less biased and less uncertain pore pressure ratios than other stress-, strain-, and energy-based pore pressure models.

#### Dissipated Energy-Based Pore Pressure Models

Pore pressure generation can also be correlated to dissipated energy [@GreenEtAl2000]. Laboratory tests have shown that pore pressure ratio increases linearly with the square root of normalized dissipated energy density:

$$r_u = \sqrt{\frac{W_s}{\text{PEC}}} \tag{9.57}$$

where $W_s$ = dissipated energy per unit volume divided by initial effective confining stress and the pseudo energy capacity, PEC, is a calibration parameter obtained from the results of cyclic tests (cyclic triaxial or cyclic simple shear). The value of $W_s$ can be computed as

$$W_s = \frac{1}{\sigma'_m} \int \sigma_d \, d\varepsilon_a = \frac{1}{\sigma'_m} \int \tau \, d\gamma \tag{9.58}$$

for cyclic triaxial tests ($\sigma_d$ = deviator stress and $\varepsilon_a$ = axial strain) and cyclic simple shear tests ($\tau$ = shear stress and $\gamma$ = shear strain), respectively; for both, $\sigma'_m$ = initial mean effective stress. Green et al. (2000) [@GreenEtAl2000] found that laboratory data suggested that the pseudo energy capacity, PEC, could be estimated as

$$\text{PEC} = W_s\big|_{r_u = 0.65} \tag{9.59}$$
