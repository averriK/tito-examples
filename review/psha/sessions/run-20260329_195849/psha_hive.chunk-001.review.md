## MCER and ELastic Design Spectra (ASCE) {#sec-mcer}

Seismic demand for all Risk Categories I–IV was derived in accordance with **ASCE/SEI 7-22**—as adopted by **IBC 2021**—using the site-specific uniform-hazard spectrum (UHS) established in the preceding chapter. Chapter 11 of ASCE 7 permits replacement of mapped spectral accelerations by values obtained from a probabilistic hazard analysis coupled with site-response modelling, provided the procedures of §11.4.7 are satisfied [@ASCE722 §11.4.7].
^[Confidence: HIGH, Rationale: The reference to ASCE/SEI 7-22 as adopted by IBC 2021 and the claim that Chapter 11 permits replacement of mapped spectral accelerations with site-specific hazard analysis under §11.4.7 are well supported. Published practitioner documentation consistently confirms both the adoption relationship and the §11.4.7 pathway for site-specific procedures [WEB:https://www.iccsafe.org/building-safety-journal/bsj-technical/is-continued-use-of-the-two-period-design-spectrum-in-the-equivalent-lateral-force-procedure-of-seismic-design-permitted-by-asce-7-22/][WEB:https://amplify.asce.org/content/standard/9780784415788/part/provisions/standard-chapter/s11].]

Chapter §11.4.7 indicate that to perform a site response analysis and a ground motion hazard analysis to determine ground motions for any structure procedures of sections §21.1 and §21.2 must be applied.
^[Confidence: MEDIUM, Rationale: The substance of this statement -- that §11.4.7 requires compliance with §21.1 and §21.2 for site-specific hazard analysis -- is consistent with the hierarchical structure of ASCE 7-22 as described in publicly available documentation [WEB:https://amplify.asce.org/content/standard/9780784415788/part/provisions/standard-chapter/s21]. A grammatical error is present: "Chapter §11.4.7 indicate" should read "Chapter §11.4.7 indicates". Confidence is MEDIUM rather than HIGH because exact normative clause wording requires access to the licensed standard document.]

When the procedures of either Section §21.1 or §21.2 are used, the design response spectrum shall be determined in accordance with Section §21.3, the design acceleration parameters shall be determined in accordance with Section §21.4.
^[Confidence: MEDIUM, Rationale: The assignment of §21.3 to the design response spectrum and §21.4 to the design acceleration parameters is consistent with the chapter structure of ASCE 7-22 described in available technical sources [WEB:https://amplify.asce.org/content/standard/9780784415788/part/provisions/standard-chapter/s21][WEB:https://earthquake.usgs.gov/ws/designmaps/asce7-22.html]. Full verification of the exact normative language requires the licensed standard.]

The probabilistic spectral response accelerations shall be taken as the spectral response accelerations in the direction of maximum horizontal response represented by a 5% damped acceleration response spectrum that is expected to achieve a 1% probability of collapse within a 50-year period. If the spectral response accelerations predicted by the ground motion models do not represent the maximum response in the horizontal plane, then the response spectral accelerations computed from the hazard analysis shall be scaled by factors to increase the motions to the maximum response. If the ground motion models predict the geometric mean or similar metric of the two horizontal components, then the scale factors shall be 1.2 for periods less than, or equal to, 0.2 s, 1.25 for a period of 1.0 s, and 1.3 for periods greater than or equal to 10 s.
^[Confidence: MEDIUM, Rationale: The risk-targeted MCER criterion of 1% probability of collapse in 50 years is a foundational element of the risk-targeted ground motion framework introduced in ASCE 7-10 and retained in ASCE 7-22 [WEB:https://www.asce.org/communities/institutes-and-technical-groups/structural-engineering-institute/news/asce-7-22-ground-motions---a-rational-approach-for-structural-engineers]. The 5% critical damping assumption for response spectra is standard across building codes [WEB:https://earthquake.usgs.gov/ws/designmaps/asce7-22.html]. The specific geometric-mean-to-maximum-direction scale factors (1.2, 1.25, 1.3) at period breakpoints (0.2 s, 1.0 s, 10 s) are internal provisions of the licensed ASCE 7-22 text; they could not be independently verified from publicly available excerpts alone, leaving residual uncertainty about the exact numerical values and period thresholds.]

Consistent with §21.3, the **design-level spectral accelerations** are obtained by scaling the MCER ordinates by the factor $2/3$ [@ASCE722 Eq. 21.3-1]:
^[Confidence: HIGH, Rationale: The factor-of-two-thirds relationship $S_a = \frac{2}{3}S_{aM}$ is a foundational result in ASCE 7-22 §21.3, consistently confirmed by multiple authoritative practitioner sources describing the relationship between MCER and design spectra [WEB:https://www.iccsafe.org/building-safety-journal/bsj-technical/is-continued-use-of-the-two-period-design-spectrum-in-the-equivalent-lateral-force-procedure-of-seismic-design-permitted-by-asce-7-22/][WEB:https://earthquake.usgs.gov/ws/designmaps/asce7-22.html]. No contradictions were identified.]

$$
S_{a}=\frac{2}{3}S_{aM}
$$

When a site-specific procedure is used to determine the design ground motion the design acceleration parameters are calculated as [@ASCE722 §21.4]:
$$
  S_{DS} = 0.9 \max_{T\,\in\,[0.2,\,5\,\text{s}]} S_a(T)
  $$ $$
  S_{D1} = \max\!\left(0.9\max_{T\,\in\,[1,\,T^*]\,\text{s}} \left[T \cdot S_a(T)\right],\quad
  S_a(1\,\text{s})\right)
  \quad \text{con} \quad
  T^* = \begin{cases} 2\,\text{s} & \bar{v}_s > 442\,\text{m/s} \\ 5\,\text{s} & \bar{v}_s \leq
  442\,\text{m/s} \end{cases}
  $$
^[Confidence: MEDIUM, Rationale: The formulas for $S_{DS}$ (0.9 times the maximum $S_a$ over 0.2-5 s) and $S_{D1}$ (incorporating a velocity-dependent integration limit $T^*$ with a threshold of 442 m/s, approximately 1450 ft/s) are broadly consistent with the §21.4 provisions described in available documentation [WEB:https://www.iccsafe.org/building-safety-journal/bsj-technical/is-continued-use-of-the-two-period-design-spectrum-in-the-equivalent-lateral-force-procedure-of-seismic-design-permitted-by-asce-7-22/]. A language error is present: the term "con" appearing in the conditional definition of $T^*$ is a Spanish or Portuguese preposition meaning "with" or "where"; it should be replaced by the English equivalent ("where") in an English-language document. The mathematical structure of the formulas is otherwise internally consistent.]

The spectral response acceleration parameter at short periods ($S_{MS}$) and the spectral response acceleration parameter at a period of 1 s ($S_{M1}$) are calculated as:
^[Confidence: LOW, Rationale: The first equation, $S_{MS} = 1.5\,S_{DS}$, is algebraically correct: it follows directly from the standard ASCE 7-22 relationship $S_{DS} = \frac{2}{3}S_{MS}$, confirmed by multiple sources [WEB:https://earthquake.usgs.gov/ws/designmaps/asce7-22.html][WEB:https://www.iccsafe.org/building-safety-journal/bsj-technical/is-continued-use-of-the-two-period-design-spectrum-in-the-equivalent-lateral-force-procedure-of-seismic-design-permitted-by-asce-7-22/]. The second equation, however, is written as $S_{M1} = 1.5\,S_{M1}$, which is a trivially circular identity that conveys no information. The correct expression is $S_{M1} = 1.5\,S_{D1}$, derived from the standard relationship $S_{D1} = \frac{2}{3}S_{M1}$. This is a typographical error with significant technical consequences for any reader or downstream system relying on this equation to recover $S_{M1}$ from $S_{D1}$.]

$$
S_{MS}= 1.5 S_{DS}, \qquad
S_{M1}=1.5 S_{M1}
$$
