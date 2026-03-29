## SLOT 3: Maximum credible earthquake ground-motion intensity

The maximum credible earthquake (MCE) at the site is defined by the largest earthquake magnitude the source can produce, $M_{\max}$, occurring at source-to-site distance $r$. The objective is to determine the ground-motion intensity $i^*_{\text{MCE}}$ such that its annual exceedance probability equals a prescribed target AEP -- for example, $\text{AEP} = 1/T_R$ for a given return period $T_R$. The AEP relation from @eq-aep in `kb/hazard.qmd` links the annual exceedance rate to the annual exceedance probability under the Poisson occurrence assumption:^[Confidence: HIGH, Rationale: The MCE definition and the reference to @eq-aep in KB:hazard.qmd are taken directly from the task and from the KB source. The Poisson assumption underlying @eq-aep is stated explicitly in KB:hazard.qmd. The claim is fully supported.]

$$\text{AEP} = P_{1\text{yr}}[I > i^*] = 1 - \exp\!\left[-\lambda_I(i^*)\right]$$

Solving for the rate corresponding to the target AEP yields:^[Confidence: HIGH, Rationale: The display of @eq-aep is taken verbatim from KB:hazard.qmd. The lead-in correctly notes the Poisson assumption. The result is fully supported.]

$$\lambda_I(i^*_{\text{MCE}}) = -\ln\!\left(1 - \text{AEP}\right) = -\ln\!\left(1 - \frac{1}{T_R}\right) \approx \frac{1}{T_R}, \qquad T_R \gg 1$$

The approximation $-\ln(1 - 1/T_R) \approx 1/T_R$ holds for large return periods and is noted in the footnote to @eq-aep in `kb/hazard.qmd`. This relation defines $i^*_{\text{MCE}}$ implicitly as the intensity level on the hazard curve at which the annual exceedance rate equals the target value. Because the full hazard integral (Slot 2) requires numerical evaluation, the inversion of the hazard curve to recover $i^*_{\text{MCE}}$ likewise requires numerical methods. [KB:hazard.qmd]^[Confidence: HIGH, Rationale: The algebraic inversion of @eq-aep is exact. The large-$T_R$ approximation is explicitly noted in KB:hazard.qmd. The statement that numerical inversion is required follows from the non-closed-form nature of the particularized hazard integral established in Slot 2. All claims are supported by KB:hazard.qmd.]

For the MCE scenario specifically, the ground motion is conditioned on an event of magnitude $M_{\max}$ at distance $r$. The intensity $I$ is lognormal with median $\hat{\eta}_I(M_{\max}, r)$ and logarithmic standard deviation $\sigma_{\ln I}$, and the conditional exceedance probability is:^[Confidence: HIGH, Rationale: The conditional exceedance probability follows directly from @eq-branch-exc in KB:uncertainty_model.qmd restricted to the scenario $m = M_{\max}$. The lognormal model applies here without modification. The claim is fully supported.]

$$P\!\left[I > i^* \mid M_{\max}, r\right] = 1 - \Phi\!\left(\frac{\ln i^* - \ln\hat{\eta}_I(M_{\max}, r)}{\sigma_{\ln I}}\right)$$

Setting this probability equal to the target AEP and inverting:^[Confidence: HIGH, Rationale: The step preceding the displayed equations is a standard algebraic setup for inverting the lognormal conditional exceedance probability. It is fully consistent with the GMPE model in KB:uncertainty_model.qmd.]

$$\Phi\!\left(\frac{\ln i^*_{\text{MCE}} - \ln\hat{\eta}_I(M_{\max}, r)}{\sigma_{\ln I}}\right) = 1 - \text{AEP}$$

$$i^*_{\text{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\Phi^{-1}\!\left(1 - \text{AEP}\right)\right]$$

For $\text{AEP} = 1/T_R$, the expression becomes:^[Confidence: HIGH, Rationale: The algebraic inversion of the normal CDF relationship to isolate $i^*_{\text{MCE}}$ is exact. The result follows by exponentiation after applying $\Phi^{-1}$ to both sides. The derivation is consistent with KB:uncertainty_model.qmd.]

$$i^*_{\text{MCE}} = \hat{\eta}_I(M_{\max}, r)\cdot\exp\!\left[\sigma_{\ln I}\cdot\Phi^{-1}\!\!\left(1 - \frac{1}{T_R}\right)\right]$$

The factor $\varepsilon^*_{\text{MCE}} = \Phi^{-1}(1 - 1/T_R)$ is the number of logarithmic standard deviations above the median at which $i^*_{\text{MCE}}$ lies; for large $T_R$ this factor is positive and increases with $T_R$, reflecting the expectation that rarer ground-motion levels require above-median GMPE residuals. The representative distance $r$ for the MCE scenario may be taken as the mean distance of the circular source, $\bar{r} = \int_0^R r\, f_R(r)\, dr = 2R/3$, or as the distance $r \to 0^+$ for a conservative bound; the choice must be stated explicitly for any specific application. [KB:hazard.qmd] [KB:uncertainty_model.qmd]^[Confidence: MEDIUM, Rationale: The interpretation of $\varepsilon^*_{\text{MCE}}$ and its monotone growth with $T_R$ are analytically correct consequences of the properties of $\Phi^{-1}$. The computation of the mean distance $\bar{r} = 2R/3$ follows from integrating $r \cdot f_R(r) = 2r^2/R^2$ over $[0,R]$, which is exact. The recommendation to use $\bar{r}$ or $r \to 0^+$ is physically motivated but represents a modeling choice not uniquely specified by KB:hazard.qmd or KB:uncertainty_model.qmd; it is presented as a suggestion, not a KB-derived result, which justifies the MEDIUM confidence.]

The two perspectives on $i^*_{\text{MCE}}$ are complementary. The full probabilistic approach (inversion of the complete hazard curve from Slot 2) is consistent with the Poisson-PSHA framework of @eq-aep and integrates over the continuous distributions of all magnitude-distance pairs; the scenario-conditioned expression provides an analytical closed form for rapid estimation at a representative distance. Both expressions are anchored to the AEP definition of @eq-aep in `kb/hazard.qmd`. [KB:hazard.qmd] [ZOTERO:B9QX9ZYI]^[Confidence: MEDIUM, Rationale: The methodological comparison between the full probabilistic and scenario-conditioned MCE approaches is consistent with the PSHA framework in KB:hazard.qmd. The statement that both are anchored to @eq-aep is correct. However, the explicit comparison of these two perspectives is an interpretive synthesis not stated in the KB text itself. External support is provided by McGuire (1995) [ZOTERO:B9QX9ZYI], which discusses the connection between probabilistic hazard levels and design earthquakes, warranting MEDIUM confidence for this inferential claim.]

---

