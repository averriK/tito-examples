<!-- chunk-033 | Kramer and Stewart - 2024 - Geotechnical Earthquake Engineering -->

$$\ln \Delta H_s = 0.84\ln(0.58) + 0.41\ln(0.30) + 2.848$$

The median settlement is then

$$\Delta H_s = \exp(\ln \Delta H_s) = \exp(2.848) \approx 17.3 \text{ mm}$$

The aforementioned procedure was derived to match foundation settlements observed in centrifuge tests and numerical analyses [@BrayMacedo2017] and has been shown to be reasonably consistent with those observed in regular (i.e., uniformly loaded) and short- to moderate-height (up to 24 m) buildings in a limited number of earthquakes. Because the procedure is empirical, it should be used with caution and engineering judgment for conditions that differ from those upon which the procedure has been calibrated. For a given building, then, the total settlement can be estimated as the sum of the reconsoldiation, ejecta, and shear-induced components, i.e.,

$$\Delta H_{tot} = \Delta H_v + \Delta H_e + \Delta H_s \tag{9.96}$$

Bullock et al. (2019) [@BullockEtAl2019] used physical model tests, numerical analyses, and case history observations to develop an alternative CAV-based procedure for estimation of building settlement that accounts for numerous soil profile, foundation, and structural characteristics. Of course, the spatial variability of liquefiable soil deposits should always be taken into account. In some depositional environments, isolated pockets of liquefiable soil (Figure 9.85) may exist and lead to additional differential settlement of structures.

**Figure 9.85.** Pockets of liquefied soil that can lead to differential settlement. Small pockets at shallow depth or larger pockets at greater depth can cause different problems.

## Deep Foundations

Deep foundations (e.g., driven piles or drilled shafts) develop their resistance to downward-acting loads through end-bearing resistance and skin friction that develops along the perimeter surface of the foundation. The development of both components of resistance requires some level of downward movement of the foundation relative to the surrounding soil; mobilization of skin resistance requires much less relative movement (typically < 1 cm) than mobilization of end-bearing resistance (typically 10%–20% of pile or shaft diameter). As pore pressures build up during shaking, skin friction in liquefiable soil layers may decrease and lead to additional downward movement required to mobilize additional end-bearing resistance; this movement may be significant in large-diameter foundations such as drilled shafts in which an appreciable fraction of the capacity is derived from end bearing.

When deep foundations pass through compressible soils that undergo consolidation, the resulting settlement can cause the soil within and above the consolidating layer to move downward relative to the foundation element. When this occurs, the skin friction stresses act downward instead of upward; this negative skin friction imposes additional, downward-acting downdrag loads that must be resisted by the portions of the foundation below the consolidating layer. The pile or shaft itself must also have the structural capacity to resist the additional compressive force caused by negative skin friction.

Two approaches to the estimation of the resulting downdrag loads have been used in practice. In the "explicit" approach (Figure 9.86), the profile of settlement along the length of a pile (or shaft) is computed and the soil that experiences a settlement (relative to the pile or shaft) that exceeds some threshold value (10 mm is typical) is considered to cause negative skin friction [@FelleniusSiegel2008] [@AASHTO2017]. Integration of that negative skin friction over the perimeter surface area on which it acts yields a downdrag force that is added to the load applied at the top of the pile for design.

In the neutral plane approach, two axial load profiles are plotted as functions of depth along the pile (Figure 9.87a). The first (loading) curve shows the axial load in the pile assuming that all soils develop negative skin friction; this curve begins with the applied dead load at the top of the pile and then increases with cumulative downdrag force at increasing depths. The second (resistance) curve begins at the tip of the pile with the mobilized end-bearing resistance, $Q_{tm}$, and assumes positive skin friction is developed in all soils; this curve increases with decreasing depth. The two curves intersect at the depth at which the applied dead load plus the cumulative downdrag force is equal to the mobilized base resistance plus cumulative positive skin resistance. This depth, at which there is no relative movement between the pile and the soil, defines the neutral plane and is the location of the maximum axial force in the pile. Figure 9.87b illustrates the vertical movement of the soil and the pile (accounting for its elastic compression); negative skin friction is developed above the neutral plane and positive skin friction below it.

**Figure 9.86.** Illustration of positive and negative skin friction in explicit approach. All soil above depth of threshold ground settlement (10 mm in this case) is assumed to develop negative skin friction.

**Figure 9.87.** Illustration of positive and negative skin friction in the neutral plane approach: (a) loading and resistance curves showing axial load (bold curve) in pile, and (b) movements of ground and pile indicating position of neutral plane.

Post-earthquake settlement of liquefied soils can also induce significant downdrag loads in pile foundations, and the neutral plane approach can also be applied to that problem [@BoulangerBrandenberg2004] [@RollinsStrand2006] [@FelleniusSiegel2008] [@MuhunthanEtAl2017] [@ZiotopoulouEtAl2024]. The occurrence of liquefaction will affect the skin friction in the liquefied layer and lead to settlement that causes downdrag forces above that level. The effects of liquefaction-induced settlement will depend on the location of the liquefiable zone relative to the pile and the pre-earthquake neutral plane.

If the liquefying layer is above the neutral plane (Figure 9.88), the loading curve will decrease as the skin friction goes to zero (i.e., as $r_u$ goes to 1.0) in the liquefying layer. The reduced loading of the pile from downdrag reduces the mobilized end-bearing resistance, $Q_{tm}$. This unloading of the pile tip will cause the resistance curve to move upward, so the position of the neutral plane (and the maximum axial force in the pile) does not change appreciably. As the excess pore pressure dissipates, the loading and resistance curves move back to essentially their original positions.

If the liquefying layer is located below the original neutral plane (Figure 9.89), post-earthquake settlement caused by pore pressure dissipation in the liquefied layer will increase the length of pile subject to negative skin friction. This increases the downdrag load, which increases the mobilized end-bearing resistance, $Q_{tm}$. The net result is that the neutral plane moves downward, additional pile tip penetration occurs, and the maximum axial force in the pile increases.

Three additional conditions should be considered. If the liquefying layer lies entirely below the tip of the pile, the skin and end-bearing resistances should not change but the pile and soil above the liquefied layer will settle by the amount of settlement of that layer. Also, if the tip of the pile is within the liquefiable layer, the available end-bearing resistance may be significantly reduced; if the pile relies upon that resistance to support vertical loads, bearing capacity failure may occur. It should be noted that such a mechanism can occur in a deep layer of liquefiable soil, even if its thickness is not sufficient to produce surficial evidence of liquefaction. Finally, liquefaction can cause porewater to flow upward along the perimeter of the pile and reduce the available skin friction both in the liquefied layer and in overlying layers [@LedezmaEtAl2012].

**Figure 9.88.** Loading and resistance curves, and settlement curves for downdrag with liquefiable layer above original neutral plane. (After Muhunthan et al., 2017.)

**Figure 9.89.** Loading, resistance, and settlement curves for downdrag with liquefiable layer below original neutral plane. (After Muhunthan et al., 2017.)

## 9.7 Probabilistic Liquefaction Hazard Analysis

As discussed in Section 5.5, uncertainty in the prediction of response of some system to a given level of ground motion will affect the return period, and hence the mean annual probability, of the computed response. To predict the level of response that has a specific, desired return period, a probabilistic response model must be coupled with a probabilistic seismic hazard analysis. When applied to liquefaction, this coupling, which can be described as probabilistic liquefaction hazard analysis (PLHA), can be accomplished in different ways.

### 9.7.1 Triggering of Liquefaction

The first procedure for combining PSHA and liquefaction analysis, termed PLHA by Atkinson et al. (1984) [@AtkinsonEtAl1984], used an early simplified triggering model [@SeedEtAl1983] to compute a critical peak acceleration that would be required to initiate liquefaction for a given earthquake magnitude and SPT resistance. In this approach, the probability of liquefaction was taken as being equal to the probability that the peak acceleration at the site exceeded the critical peak acceleration. The probability calculations were added to a PSHA analysis so that the probability of liquefaction was computed for all combinations of magnitude and distance. However, the uncertainty in the critical peak acceleration (i.e., in the liquefaction resistance) was not explicitly accounted for so the procedure falls short of what would currently be considered to represent a full PLHA.

As GMMs and earthquake recurrence models have become more sophisticated, PSHA software has become more specialized and complex. However, the general approach described in Section 5.5.2 can be used to combine the results of a PSHA with a probabilistic liquefaction potential model to achieve a full PLHA. Kramer and Mayfield (2007) [@KramerMayfield2007] modified that approach to account for the fact that the loading used for the evaluation of liquefaction potential depends on the joint distribution of earthquake magnitude and peak ground acceleration. Recognizing that the condition of interest in an evaluation of liquefaction potential is that in which the factor of safety, $FS_L$, is less than some value, $fs_L$, the mean annual rate of non-exceedance can be written as

$$\Lambda(FS_L < fs_L) = \iint P[FS_L < fs_L \mid PGA, M]\, f_{PGA,M}(PGA, m)\, dPGA\, dm \tag{9.97}$$

$$\lambda(FS_L < fs_L) \approx \sum_i \sum_j P[FS_L < fs_L \mid PGA_i, M_j]\, \Delta\lambda_{PGA_i, M_j}$$

where $f_{PGA,M}(PGA, m)$ is the joint probability density function of peak ground acceleration and magnitude. Disaggregation data can be used to decompose the PGA hazard curve into a series of curves corresponding to the different earthquake magnitudes that contributed to the PGA hazard, which can then be integrated over all combinations of PGA and $M$ to compute the mean annual rate of non-exceedance [@KramerMayfield2007]. The reciprocal of that rate is the return period for non-exceedance of $FS_L = fs_L$. The return period for $FS_L \leq 1.0$, therefore, is the return period of liquefaction itself, as computed with consideration of all peak acceleration levels, all magnitudes, and the uncertainty in liquefaction potential given peak acceleration and magnitude. Factor of safety hazard curves, as illustrated in Figure 9.90, slope in the opposite direction to hazard curves for ground motion parameters since weak motions (which occur relatively frequently) produce high factors of safety and strong motions that occur more rarely produce low factors of safety.

Considering a standard reference element in a reference soil profile, Kramer and Mayfield (2007) [@KramerMayfield2007] showed that conditions indicated as having identical liquefaction potential (i.e., the same $FS_L$ values based on 475-year PGA and mean magnitudes in deterministic analyses) had actual return periods of liquefaction that varied by factors of up to 2 when applied at different locations across the continental United States. With the conventional approach, therefore, designs thought to provide the same level of liquefaction hazard can lead to very different levels of performance in different tectonic environments. These results show that actual liquefaction hazards, which can be characterized using a full PLHA (e.g., Equation 9.97), are influenced by the shape (particularly the slope) of the peak acceleration hazard curve and by the nature of the underlying magnitude distribution.

**Figure 9.90.** Results of PLHA-based hazard curves for triggering of liquefaction of reference element of soil (2 m depth, $q_{c1Ncs} = 80$, $V_{s30} = 200$ m/s) at 10 U.S. locations (SF = San Francisco). (Calculations based on Idriss and Boulanger, 2015 liquefaction potential model, courtesy of A. Makdisi.)

Comparisons of the results of PLHA analyses using the probabilistic liquefaction triggering models of Cetin et al. (2004) [@CetinEtAl2004] and Boulanger and Idriss (2012) [@BoulangerIdriss2012] have shown that differences between the two exist but are smaller when used in PLHA analyses than when used in a conventional, deterministic manner [@FrankeEtAl2014]. Mayfield et al. (2010) [@MayfieldEtAl2010] showed that the voluminous calculations required to integrate liquefaction potential over the entire ranges of peak acceleration and magnitude could be encapsulated in a single parameter corresponding to a reference element in a reference soil profile. Site-specific values of that parameter (i.e., for different depths in different soil profiles) could then be accurately approximated by two simple adjustment factors. Mayfield et al. (2010) [@MayfieldEtAl2010] used $FS_L$ and the SPT resistance required to resist liquefaction as liquefaction parameters and showed how values of those parameters corresponding to different return periods of liquefaction could be mapped across geographic regions. Ulmer and Franke (2015) [@UlmerFranke2015] performed the same type of analysis for CSR based on the Boulanger and Idriss (2014) liquefaction triggering model and showed that the full PLHA results could be approximated with good accuracy using a mapped CSR value with five adjustment factors. The development of liquefaction parameter maps of the types proposed by Mayfield et al. (2010) [@MayfieldEtAl2010], Ulmer and Franke (2015) [@UlmerFranke2015], and Makdisi and Kramer (2024) [@MakdisiKramer2024] could allow geotechnical engineers to design for a specified return period of liquefaction itself, and to ensure equal liquefaction potential hazards at sites in different seismo-tectonic environments, using conventional liquefaction potential procedures.

### 9.7.2 Consequences of Liquefaction

With probabilistic response models, hazard curves can also be developed for effects of liquefaction such as manifestation severity, lateral spreading, and post-liquefaction settlement. Such curves show the mean annual rate of exceedance of various response parameters such as liquefaction potential index (Section 9.6.2), lateral spreading displacement (Section 9.6.5.2), and post-liquefaction settlement (Section 9.6.6). These types of analyses allow design based on an allowable level of response corresponding to a specified return period rather than a deterministic response corresponding to a ground motion with a specified return period.

**Figure 9.91.** Liquefaction Potential Index (LPI) hazard curves for Vancouver, Canada. (After Goda et al., 2011 with permission of the Seismological Society of America.)

Goda et al. (2011) [@GodaEtAl2011] extended the PLHA procedure of Atkinson et al. (1984) [@AtkinsonEtAl1984] to include consideration of the uncertainty in liquefaction resistance and to compute values of liquefaction potential index (LPI). Using a shear wave velocity-based procedure [@AndrusStokoe2000] with a probabilistic mapping procedure [@JuangEtAl2005], a PSHA code was modified to compute probabilities of liquefaction within the hazard integral. Figure 9.91 shows LPI hazard curves for a representative soil profile located in Vancouver, British Columbia.

Geyin and Maurer (2019) [@GeyinMaurer2019] used over 15,000 case histories from 24 earthquakes to develop fragility curves (Section 5.5.2.1) for different combinations of CPT-based triggering models, manifestation severity indices, and manifestation severities. Using a logic tree approach, weighted combinations of the triggering models and severity indices allowed direct calculation of hazard curves for minor, moderate, and severe manifestation. Such curves, or hazard maps based upon them, offer an objective and practical means of estimating potential infrastructure damage for planning and policy purposes.

Hazard curves for lateral spreading displacement can be computed in different ways depending on the nature of the displacement prediction model. Displacement prediction models of the general form of Youd et al. (2002) [@YoudEtAl2002] can be handled in a particularly efficient manner [@KramerEtAl2007]. Franke and Kramer (2014) [@FrankeKramer2014] used such an approach to compute lateral spreading hazard curves (Figure 9.92) based on a probabilistic version of the Youd et al. (2002) [@YoudEtAl2002] lateral spreading model. After adjusting the penetration resistances of the soil profile shown in Figure 9.92 such that deterministic analyses based on 475-year PGAs and mean magnitudes produced 30 cm of displacement at ten sites across the United States, the actual return periods for 30 cm displacement at the sites were shown to vary by a factor of nearly 3. This result showed that complete and consistent predictions of lateral spreading displacement hazard using a predictive model of the form of Youd et al. (2002) [@YoudEtAl2002] required consideration of all combinations of magnitude and distance.

Settlement hazard curves for a hypothetical six-story reinforced concrete building are shown in Figure 9.93. The volumetric component of settlement (Section 9.6.6.1) was computed by the procedure of Juang et al. (2013) [@JuangEtAl2013] and the shear-induced component (Section 9.6.6.4) by that of Bray and Macedo (2017) [@BrayMacedo2017]. The settlement can be seen to be dominated by volumetric strains at short return periods with shear strain-induced settlement becoming more important at return periods greater than about 3,000 years.

**Figure 9.92.** Lateral spread displacement hazard curves for gently sloping soil profile at ten locations across the United States. (After Franke and Kramer, 2014 with permission of ASCE.)

**Figure 9.93.** Post-liquefaction settlement hazard curves [@LiuEtAl2021] for six-story building supported on 10 m by 20 m mat foundation embedded at a depth of 2 m below the ground surface.

### 9.7.3 Discussion

Though in their early stages of development, PLHA procedures that consider all levels of shaking and the uncertainty in response for each produce the most complete and accurate assessments of liquefaction hazards. The type of approaches developed by Mayfield et al. (2010) [@MayfieldEtAl2010] and Makdisi and Kramer (2024) [@MakdisiKramer2024] offer engineers the ability to closely approximate the results of a full, site-specific PLHA for triggering with essentially the same level of effort required by conventional procedures. Extension beyond triggering to develop liquefaction consequence hazard curves such as those in Figures 9.91–9.93 represent response-level implementations of the performance-based concepts described in Section 5.6.3.

## 9.8 Cyclic Softening

As described in Sections 6.4.4.3, 6.4.4.5, and 9.3, saturated, plastic, fine-grained soils tend to generate less pore pressure than non-plastic fine- or coarse-grained soils when subjected to the same cyclic loading. However, they do generate excess pore pressure and they can develop significant cyclic and permanent strains. The effects of these phenomena on the shear strength of the soil, i.e., the large-strain shearing resistance required for slope stability, foundation capacity, and site response problems, were described in Sections 6.6.6.3 and 6.6.6.4. The effects on their stiffness and cyclic response characteristics, in particular the potential to develop large strains that can lead to strength loss, are described here.

Fine-grained soils can soften and accumulate significant permanent deformations when cyclic stresses are superimposed on existing static shear stresses, even if the combined static and cyclic stresses do not exceed the shear strength of the soil. This type of behavior is referred to as cyclic softening behavior. Because the types of soils that exhibit cyclic softening are so much easier to sample than typical liquefiable soils, laboratory tests that provide useful information on cyclic softening behavior can be used for design applications. Boulanger and Idriss (2007) [@BoulangerIdriss2007] developed a useful framework for cyclic softening of soils they define as "clay-like" that parallels the simplified method used for evaluation of liquefaction potential. The cyclic softening framework makes use of cyclic stress and cyclic resistance ratios, although they are defined differently for plastic "clay-like" soils than the non-plastic "sand-like" soils that can liquefy, as discussed earlier in this chapter.

### 9.8.1 Characterization of Loading

The cyclic stress ratio used to evaluate cyclic softening is defined in a manner similar to that used for liquefiable soils (Equation 9.10), i.e., as

$$CSR = \frac{\tau_\text{max}}{r_e \cdot \sigma'_v} \tag{9.98}$$

where $r_e$ is usually taken as 0.65. Interpreting the MSF as a measure of the number of equivalent loading cycles for an earthquake of a given magnitude, i.e., as a loading parameter, the reference cyclic stress ratio can be expressed as

$$CSR_{M=7.5} = \frac{0.65 \cdot \tau_\text{max}}{MSF \cdot \sigma'_v} \tag{9.99}$$

where MSF is taken as

$$MSF = 1.12\exp\!\left(-\frac{M_w}{4}\right) + 0.828 \leq 1.13 \tag{9.100}$$

Laboratory data show that clays generate pore pressure more slowly than sands, so the use of $r_e = 0.65$ implies that 30 (rather than the 15 used for sand) equivalent loading cycles are consistent with a $M = 7.5$ earthquake.

### 9.8.2 Characterization of Resistance

The cyclic resistance of a plastic, fine-grained soil is closely related to its undrained shear strength [@BoulangerIdriss2007]. Figure 9.94 shows the number of cycles of loading required to produce 3% peak shear strain for rate-corrected cyclic stresses at different fractions of the soil's undrained strength. Despite having plasticity indices ranging from 13 to 73 and OCRs ranging from 1 to 4, the data fall within a relatively narrow band. The cyclic resistance ratio corresponding to a $M = 7.5$ earthquake can then be expressed as

$$CRR_{M=7.5} = C_{2D} \cdot \left(\frac{\tau_{cyc}}{s_u}\right)_{M=7.5} \cdot K_\alpha \tag{9.101}$$

**Figure 9.94.** Cyclic strength ratios versus number of cycles required to cause 3% peak shear strain in six natural soils. (Boulanger and Idriss, 2007 with permission of ASCE.)

**Figure 9.95.** Variation of $K_\alpha$ with static shear stress ratio and overconsolidation ratio. (Boulanger and Idriss, 2007 with permission of ASCE.)

where $C_{2D}$ is a correction for two-dimensional shaking estimated as 0.96 by Boulanger and Idriss (2004) [@BoulangerIdriss2004], $(\tau_{cyc}/s_u)_{M=7.5}$ is the ratio of cyclic shear stress to undrained strength for the number of cycles (30) representative of a $M = 7.5$ earthquake, and $K_\alpha$ is a static shear stress adjustment factor. Experimental results for several clays [@GouloisEtAl1985] [@AndersenEtAl1988] [@LefebvrePfendler1996] can be used to express $K_\alpha$ as a function of the measured undrained strength ratio, $s_u/\sigma'_{v0}$, and the static stress ratio, $\alpha$ (Equation 9.32):

$$K_\alpha = 1.344 - 0.638 \cdot \left(\frac{\alpha \cdot \sigma'_{vo}}{s_u}\right)^{0.344} \tag{9.102}$$

If the value of $s_u$ for the on-site soils cannot be measured, it can be estimated using a common relationship for typical clays [@Ladd1991]:

$$s_u = 0.8 \cdot \sigma'_v \cdot OCR^{0.22} \tag{9.103}$$

Figure 9.95 shows how initial static shear stress ratios decrease $K_\alpha$ (and thus the cyclic resistance ratio) more strongly for normally consolidated soils than overconsolidated soils.

### 9.8.3 Cyclic Softening Potential

With the value of cyclic stress ratio and cyclic resistance ratio determined, the potential for cyclic softening (defined here as a peak cyclic shear strain exceeding 3%) can be expressed in terms of the factor of safety

$$FS = \frac{CRR_{M=7.5}}{CSR_{M=7.5}} \tag{9.104}$$

It should be noted that a factor of safety less than 1.0 does not necessarily imply catastrophic failure, but rather that cyclic shear strains are expected to exceed 3%; in sensitive soils, that level of disturbance could lead to fabric degradation that contributes to significant strength loss (Section 6.6.6.3).

#### Example 9.10

A slope in southern California is found to be underlain by a lightly overconsolidated ($OCR = 1.8$) saturated clay. Laboratory tests have shown that the undrained strength of the clay is approximately 35% of the vertical effective stress, and site response analyses using ground motions appropriate for a $M7.2$ earthquake show cyclic shear stresses of approximately 40% of the monotonic undrained strength of the soil. An element of the clay near the toe of the slope has a static stress ratio, $\alpha = 0.2$. Compute the factor of safety against cyclic softening of that element of clay.

**Solution:**

For the $M7.2$ event of interest, Equation (9.100) indicates that

$$MSF = 1.12\exp\!\left(-\frac{7.2}{4}\right) + 0.828 = 1.013$$

The cyclic stress ratio induced in the soil can then be computed as

$$CSR_{M=7.5} = \frac{0.65 \cdot \tau_\text{max}}{MSF \cdot \sigma'_v} = \frac{0.65 \times 0.40}{1.013} = 0.257$$

The static shear stress adjustment factor is computed as

$$K_\alpha = 1.344 - 0.638 \cdot \left(\frac{0.2}{0.35}\right)^{0.344} = 1.344 - 0.638 \times (\cdots) = 0.753$$

which allows the cyclic resistance ratio to be computed as

$$CRR_{M=7.5} = C_{2D} \cdot \left(\frac{\tau_{cyc}}{s_u}\right)_{M=7.5} \cdot K_\alpha = (0.96)(0.40)(0.35)(0.753) / (0.35) = 0.210$$

The resulting factor of safety against cyclic softening is

$$FS = \frac{CRR_{M=7.5}}{CSR_{M=7.5}} = \frac{0.210}{0.257} = 0.82$$

which indicates that shear strains greater than 3% are to be expected. The actual level of shear strain, and consequently the deformation of the slope, will depend on the sensitivity of the clay, the nature of the ground motion, and specific site conditions.

### 9.8.4 Discussion

The best approach to evaluating cyclic softening is to evaluate CRR in the laboratory by performing cyclic tests on high-quality samples from the site of interest. This approach, which combines cyclic testing (to obtain $\tau_{cyc}/s_u$) with monotonic testing (to obtain $s_u/\sigma'_{v0}$), will provide the highest level of confidence in the CRR value and the lowest uncertainty in the cyclic softening prediction. The next best approach is to derive CRR using measured monotonic shear strengths derived from laboratory or field tests on soil from the site of interest and to take cyclic strength ratios ($\tau_{cyc}/s_u$) from the results of prior studies (Figure 9.94). If no strength information is available, or if only a rough, preliminary estimate is desired, the cyclic resistance ratio can be estimated from Equation (9.106). Using simplifications described in Boulanger and Idriss (2007) [@BoulangerIdriss2007], the second and third approaches described above can produce cyclic resistance ratios of

$$CRR_{M=7.5} = \left(\frac{s_u}{\sigma'_v}\right)_{NC}^{0.8} \cdot m \cdot K_\alpha \tag{9.105}$$

$$CRR_{M=7.5} = 0.18 \cdot OCR^{0.8} \cdot K_\alpha \tag{9.106}$$

CRR values estimated from Equation (9.105) should be recognized as being more uncertain than values obtained from laboratory testing, and values obtained from Equation (9.106) should be recognized as being more uncertain than values obtained from Equation (9.105).

## 9.9 Summary

1. The term liquefaction refers to the loss of stiffness and strength of a loose, saturated, non-plastic soil. Liquefaction is most often triggered by transient loading such as that induced by earthquakes but can also be initiated by monotonic loading. The generation of high porewater pressure under undrained loading conditions is a hallmark of soil liquefaction.

2. Cyclic softening refers to the reduction of stiffness and strength of saturated, plastic, fine-grained soils that are not susceptible to liquefaction. These reductions can be significant but are generally not as severe as those associated with liquefaction.

3. Liquefaction and cyclic softening can occur over broad ranges of soil conditions. Both are capable of causing significant damage, and both should be evaluated as part of a complete seismic hazard assessment.

4. Flow liquefaction can occur when the shear strength of a liquefied soil, i.e., its residual strength, drops below the shear stresses required to maintain static equilibrium. Flow failures, or flowslides, can involve very large and rapid deformations, and may be triggered by transient or monotonic loading; although they can be tremendously damaging, flow slides are relatively rare.

5. Cyclic liquefaction results from the incremental generation of excess porewater pressure by transient loading while applied static shear stresses are lower than the shear strength of the soil. Cyclic liquefaction can produce small to large deformations of soil slopes and of soil–structure systems. Cyclic liquefaction of level-ground sites, where static shear stresses are zero, is generally manifested by ground oscillation, post-earthquake settlement, and the development of sand boils. Permanent lateral displacements due to level-ground liquefaction are usually small.

6. Evaluation of liquefaction hazards requires that liquefaction susceptibility, triggering, and effects be predicted. For a site to be considered free from significant liquefaction hazards, the soils must be non-susceptible to liquefaction, the anticipated loading must be insufficient to trigger liquefaction, or the effects of liquefaction must be tolerable.

7. Liquefaction susceptibility is a function of the composition of the soil itself, and is independent of the state (density and effective stress) or level of saturation that the soil exists in; state and saturation influence the resistance of triggering of liquefaction. Clean coarse-grained soils and non-plastic fine-grained soils are typically susceptible to liquefaction and highly plastic fine-grained soils are not susceptible. Liquefaction susceptibility is most commonly assessed in terms of the plasticity index of the soil. Historical and geologic indicators can be helpful in identifying locations of soils that are susceptible to liquefaction. Soils that are not susceptible to liquefaction are not exempt from potential problems, however, as they may undergo cyclic softening.

8. Under given loading conditions, any susceptible soil will reach a unique combination of effective stress, void ratio, and shear strength at large strains. The combination can be described graphically by a three-dimensional curve known as the steady state line. The position of the SSL is most strongly influenced by grain size and grain shape characteristics.

9. The resistance of a susceptible soil to triggering of liquefaction depends on its volume change characteristics, specifically its degree of contractiveness. The more contractive an element of soil is, the lower its liquefaction resistance will be. Volume change characteristics can be related to the state parameter, which is the difference between the void ratio and the void ratio at the steady state for the same effective stress. A soil with a high state parameter (generally greater than −0.05) will exhibit contractive behavior at large strain levels, and a soil with a lower state parameter will exhibit dilative behavior.

10. Steady state lines are generally somewhat steeper (in $e$–$\sigma'$ space) than consolidation curves, which means that the state parameter (hence, degree of contractiveness) increases with increasing effective confining stress.

11. Flow liquefaction can occur when the static shear stress acting on the soil is greater than its steady state shear strength (or, in the field, its residual strength). It is triggered when the principal effective stress ratio reaches a critical value under undrained, stress-controlled conditions. The stress state at the triggering of flow liquefaction can be described graphically in stress path space by the FLS. Once the effective stress path reaches the FLS, whether by static or cyclic loading, additional straining will induce additional excess pore pressure and the available shearing resistance will drop to the steady state strength. After triggering, deformations of the soil are driven by the difference between the static shear stress and the steady state shear strength. Under seismic conditions, the function of the earthquake is to bring the soil from its initial equilibrium state to the FLS; at that point, the soil skeleton collapses and deformations are driven by the static stresses.

12. Soils of intermediate density may experience a reduction in shearing resistance associated with a quasi-steady state beyond which dilation leads to increasing shearing resistance as the soil reaches the actual steady state at much larger strain amplitudes.

13. Cyclic liquefaction can be triggered in loose or dense susceptible soil since even dense soils tend to initially contract at low strain levels. The level of loading required to trigger liquefaction depends on their level of contractiveness (i.e., on their state parameter); because they are more contractive, looser soils at a particular effective stress will tend to liquefy at lower levels of cyclic shear stress (for a given number of loading cycles) than denser soils (and at a lower number of cycles for a given cyclic shear stress amplitude). The tendency of denser soils to dilate upon uni-directional (monotonic) straining can limit the severity of the effects of liquefaction even if it happens to be triggered. Although liquefaction can be triggered in very dense laboratory specimens, the level of loading required to do so may exceed that which can reasonably be expected from earthquake shaking; in such cases, screening criteria can be used to eliminate the need for a formal liquefaction potential evaluation.

14. The cyclic stress approach, which remains the most common procedure for the evaluation of liquefaction potential, characterizes both earthquake loading and soil liquefaction resistance in terms of cyclic stresses. A transient earthquake motion is converted to an equivalent series of uniform cycles of shear stress. The number of equivalent cycles, a function of the duration of the motion, is correlated with the magnitude of the earthquake. Liquefaction resistance was originally obtained from laboratory (cyclic triaxial and cyclic simple shear) tests. The cyclic stress-based liquefaction resistance, however, is influenced by factors such as soil fabric, stress and strain history, and age that may be destroyed by sampling and are difficult to replicate in the laboratory.

15. In situ test-based procedures characterize liquefaction resistance in terms of in situ test parameters associated with soils at sites at which surficial manifestation of liquefaction has and has not been observed in past earthquakes; due to its repeatability and resolution, the CPT resistance is most commonly used but other in situ parameters, including SPT resistance (which has the benefit of providing soil samples) and shear wave velocity (which can often be measured economically from the ground surface), are also used. The cyclic stress approach allows the estimation of a factor of safety against liquefaction or a probability of liquefaction. Because of its basis on the presence or absence of surficial manifestation, common in situ test-based procedures can be interpreted as producing factors of safety against or probabilities of surficial manifestation.

16. Surficial manifestation of liquefaction usually takes the form of sand boils (ejecta) and/or ground cracking. Sand boil formation, however, can depend on the mechanical and hydraulic response of the entire soil profile; factors such as the depth, thickness, and void volume of the liquefied layer, the depth of the groundwater table, and the characteristics of overlying and underlying layers affect the hydraulic response and therefore surficial manifestation. Since liquefaction of a thin and/or silty layer at depth may not be expressed at the ground surface, the absence of sand boils does not necessarily indicate that level ground liquefaction has not occurred. Similarly, the large volume of water that can be expelled from a thick, shallow layer of loose soil in which liquefaction is not quite triggered can produce sand boils. Therefore, surficial manifestation as a criterion for liquefaction at depth can give rise to both false positive and false negative indications of liquefaction; this condition gives rise to some of the uncertainty in prediction of liquefaction potential.

17. Other approaches based on characteristics such as cyclic strain and dissipated energy have been proposed for the evaluation of liquefaction potential. Cyclic strain approaches are attractive in that pore pressure generation is inherently more closely related to cyclic strain amplitudes than cyclic stress amplitudes, but cyclic strain amplitudes are more difficult to predict than cyclic stress amplitudes. Dissipated energy demand is related to both stress and strain amplitudes and has been shown to correlate well to pore pressure generation in the laboratory but is also difficult to predict in the field and energy capacity is difficult to correlate to in situ parameters.

18. The generation of excess pore pressure and potential for liquefaction can also be investigated using nonlinear, effective stress ground response analyses. The development of improved numerical tools and constitutive models can allow evaluation and visualization of the coupled mechanical-hydraulic system response of an entire soil profile. The ability to "see inside" a profile as it responds to earthquake shaking can be very useful in understanding how and where pore pressures and deformations develop below as well as at the ground surface.

19. Rapid estimates of manifestation severity can be made using geospatial procedures that utilize regional ground motion, topographic, geologic, geomorphic, and groundwater data instead of site-specific geotechnical properties. Such estimates can be useful for planning and rapid response purposes.

20. The consequences of liquefaction are different for different liquefaction phenomena. Although flow liquefaction is capable of producing the most spectacular effects, cyclic liquefaction can also produce extensive damage.

21. Liquefaction can dramatically alter the amplitude and frequency content of ground surface motions. As the buildup of excess pore pressure causes a layer of liquefiable soil to soften, ground surface displacements may increase even when ground surface accelerations decrease. Dilation-induced stiffening can produce strong, high-frequency spikes in ground surface acceleration. Ground oscillation at level-ground sites may produce chaotic permanent movements of fractured blocks of surficial soil and significant amounts of sand can be ejected at the ground surface.

22. Ground surface settlement can develop during and/or after earthquakes due to the densification of dry or saturated sands. Settlement of dry sand occurs almost immediately, but settlement of saturated sands may not develop until well after earthquake shaking has ended. The magnitude of post-earthquake settlement depends on the density, thickness, and depth of the liquefiable soil, and on the amplitude and duration of shaking. Settlement can be caused by dissipation of excess pore pressure in the free-field or in the vicinity of structures, shear stresses associated with the response of structures supported on shallow foundations, and by loss of soil volume associated with ejecta.

23. The shear strength of a liquefied soil is sensitive to the void ratio, or density, of the soil. In the laboratory, where volume change can be eliminated, the shear strength mobilized at very large strain levels is often referred to as the steady state (or critical state) strength. In the field, where the requirements of the steady state of deformation are generally violated, the large-strain mobilized strength is referred to as the residual strength. Residual strengths are generally estimated as functions of penetration resistance and initial effective stress based on back-calculated strengths from flow slide case histories.

24. Excess pore pressures generated during earthquake shaking produce hydraulic gradients that cause porewater to flow during and after earthquake shaking. The resulting redistribution of pore pressure, and accompanying changes in soil void ratio, can have a strong effect on the consequences of liquefaction. This effect can be particularly important when flow is impeded by low-permeability soils (even thin lenses of such soils) that can cause void ratios to increase and steady state (or residual) strengths to decrease during or after shaking in the materials immediately below the lens. It is not uncommon for flow slides to occur minutes to hours after earthquake shaking has ended.

25. Deformation failures, such as lateral spreading, develop incrementally during, and in some cases partially after, the period of earthquake shaking. Dilation-induced stiffening can play an important role in limiting permanent deformations, and void redistribution can lead to increased deformations. For strong levels and/or long durations of shaking, deformation failures can produce large displacements and cause significant damage. Both empirical and numerical procedures are available to estimate displacements caused by deformation failures.

26. The triggering and consequences of liquefaction are influenced by ground motion characteristics and a complete evaluation of the performance of a soil profile containing liquefiable soils should consider all earthquake scenarios and the range of ground motions they can produce. Basing a liquefaction hazard analysis on one level of ground motion, i.e., that associated with a specific return period, ignores the fact that liquefaction can be triggered by weaker motions that occur more frequently and stronger motions that occur more rarely than those of the selected return period, and can result in highly inconsistent estimates of liquefaction hazard in different seismo-tectonic environments. Probabilistic liquefaction hazard analyses, or PLHAs, allow consideration of all earthquake scenarios and all associated levels of shaking to produce consistent and objective estimates of liquefaction hazards.

27. Saturated, plastic, fine-grained soils may not be susceptible to liquefaction but can generate excess pore pressure and soften under cyclic loading. The degree of softening is influenced by the undrained strength, static shear stress level, and cyclic shear stress level induced in the soil.

28. Plastic fine-grained soils can accumulate significant permanent deformations when cyclic stresses are superimposed on existing static shear stresses, even if the combined static and cyclic stresses do not exceed the shear strength of the soil.

29. Cyclic stress-based procedures that account for rate effects and estimate the potential for cyclic softening (characterized by shear strains in excess of 3%) are available. These soils characterize loading and resistance by means of cyclic stress and cyclic resistance ratios although both are defined differently than for sand-like soils. The cyclic resistance ratio is closely related to the static undrained shear strength ratio of the soil. The rate-dependence of clay-like soils should be considered in estimating the undrained strength that would be mobilized in the field (under rapid earthquake loading) from laboratory measurements (much slower loading).

---

# 10 Ground Failure in Shear: Movement and Seismic Slope Stability

## 10.1 Introduction

Geotechnical ground failure can produce earthquake damage by a number of mechanisms, several of which were discussed in Chapter 9. Liquefaction and cyclic softening can cause both vertical and horizontal ground movements due to both compression and shearing mechanisms. These movements result from the softening and weakening these soils undergo as high porewater pressures are generated during shaking; these movements develop incrementally and cause significant damage even when the strength of the soil is not exceeded.

Ground failure can also occur, however, in materials that do not generate significant porewater pressure during shaking. These failures occur when shear stresses on a potential failure surface exceed the available shear strength on that surface. This chapter describes ground movements that result from shearing on failure surfaces through two mechanisms – fault movement and slope instability – and presents procedures for predicting their likelihoods of occurrence and estimating the deformations they produce.

## 10.2 Fault Displacement

Perhaps the most direct form of seismic ground failure is that associated with fault rupture (Section 1.3.1) itself. As discussed in Section 2.4.2, fault rupture may or may not extend all the way to the ground surface. Ruptures that do extend to the ground surface can produce significant permanent displacements with vertical and/or horizontal offsets over short distances which can cause devastating damage to structures that lie above (e.g., buildings) or cross (e.g., dams, bridges or pipelines) the displaced zones. Ruptures that do not reach the ground surface can still produce significant warping, angular distortion, and extensional/compressive strain at and near the surface of sediments that overlie faulted rock.

Fault rupture damage in the 1971 San Fernando earthquake led the California state legislature in 1972 to enact the Alquist-Priolo Earthquake Fault Zoning Act, which placed restrictions on the development of structures intended for human occupancy on properties near mapped active fault traces. This section describes fault rupture and ground surface displacement patterns and presents the basic components required for assessment of fault rupture hazards. More detailed treatments of such assessments can be found in Youngs et al. (2003), Petersen et al. (2011), Moss and Ross (2011), and Wells and Kulkarni (2014). Databases with information on field observations of surface rupture are presented by Sarmiento et al. (2021) and Nurminen et al. (2022), and models derived from these databases will be forthcoming.

### 10.2.1 Ground Surface Expression of Fault Rupture

Fault rupture damage is influenced by the distribution and nature of ground surface displacement, both of which are in turn influenced by local site conditions. At rock sites, fault rupture displacements are often sharp and readily visible. While the largest displacements may take place at depth on a specific primary fault surface, referred to as the principal fault, displacements near the surface may occur as rupture of the principal fault and as distributed ruptures across secondary faults.
