## SLOT 3: Maximum credible earthquake ground-motion intensity

The maximum credible earthquake (MCE) represents the largest magnitude earthquake that the source can generate, parameterized by the source's maximum magnitude $M_{\max}$. The ground-motion intensity produced by this MCE at the site depends on the distance at which it occurs. For a site located at the center of a circular areal source, the MCE could theoretically occur anywhere within the disk; however, in practice, the intensity corresponding to a given annual exceedance probability is determined by relating the annual exceedance probability to the hazard integral through the Poisson model of earthquake occurrence. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This description of the MCE concept and its relationship to seismic hazard is consistent with the PSHA framework in KB:hazard.qmd, which uses the Poisson assumption to relate occurrence rates to probabilities.]

The relationship between the annual exceedance probability (AEP) and the annual exceedance rate (hazard) is given by the Poisson assumption. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: The Poisson model is the standard assumption in PSHA and is explicitly documented in KB:hazard.qmd.]

$$
\text{AEP} = P_{1\text{yr}}[I > i^*] = 1 - \exp[-\lambda_I(i^*)],
$$

where $\lambda_I(i^*)$ is the annual exceedance rate of intensity $i^*$ and AEP is the annual exceedance probability. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: This is the standard relation (eq-aep in KB:hazard.qmd) between annual exceedance rate and probability under a Poisson process assumption. For small annual exceedance rates (typical of engineering design), the approximation $\text{AEP} \approx \lambda_I(i^*)$ is valid.]

By extension, the probability of exceedance over a return period $T_R$ years is given by: [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: The extension to multi-year return periods is a standard application of the Poisson model, consistent with the PSHA framework in KB:hazard.qmd.]

$$
P_{T_R}[I > i^*] = 1 - \exp[-\lambda_I(i^*)\, T_R],
$$

which defines the intensity $i^*$ that is exceeded with probability $P_{T_R}$ over $T_R$ years, where $T_R$ is defined as the inverse of the annual exceedance rate: $T_R = 1/\lambda_I(i^*)$. [KB:hazard.qmd]

^[Confidence: HIGH, Rationale: The relationship between return period and annual exceedance rate is standard in PSHA and is documented in KB:hazard.qmd. The derivation follows directly from the Poisson distribution.]

For the MCE scenario, the ground-motion intensity at the site is determined by the GMPE evaluated at magnitude $M_{\max}$ and the distance at which the event occurs. If the MCE is specified to occur at the most critical distance for producing a given intensity level, or if a representative distance (such as the distance corresponding to the modal disaggregation scenario) is chosen, the MCE ground-motion intensity $i^*_{\text{MCE}}$ is obtained from the GMPE as: [KB:hazard.qmd][KB:disaggregation.qmd]

^[Confidence: MEDIUM, Rationale: The MCE intensity depends on both $M_{\max}$ (well-defined by the source) and the distance $r_{\text{MCE}}$ at which the event is assumed to occur. The choice of representative distance introduces a degree of subjectivity, though the framework for relating hazard to intensity through the GMPE is well-established. The reference to modal disaggregation is justified by KB:disaggregation.qmd.]

$$
\hat{\eta}_I(M_{\max}, r_{\text{MCE}}) = i^*_{\text{MCE}},
$$

where $r_{\text{MCE}}$ is the representative distance at which the MCE occurs, typically selected from the disaggregation analysis to correspond to the controlling magnitude-distance pair. [KB:disaggregation.qmd]

^[Confidence: MEDIUM, Rationale: The selection of a representative MCE distance is a practical engineering decision that can be guided by disaggregation analysis, as documented in KB:disaggregation.qmd. However, the specific choice method is not uniquely determined by the physical frameworks.]

Alternatively, if the MCE intensity is required to correspond to a specific annual exceedance probability (e.g., matching a design return period), the inverse problem is solved: given a target AEP or return period, the intensity level $i^*_{\text{MCE}}$ is determined such that: [KB:hazard.qmd]

^[Confidence: MEDIUM, Rationale: This formulation uses the Poisson relation (eq-aep in KB:hazard.qmd) to find the intensity level corresponding to a target AEP. The specific choice of target AEP for the MCE (whether tied to a design return period, code-specified level, or other criterion) is a decision external to the mathematical framework.]

$$
\text{AEP}_{\text{MCE}} = 1 - \exp[-\lambda_I(i^*_{\text{MCE}})],
$$

where $\lambda_I(i^*_{\text{MCE}})$ is computed from the particularized hazard integral for the circular source. [KB:hazard.qmd]

^[Confidence: MEDIUM, Rationale: This inverse formulation correctly applies the Poisson relation to find an intensity corresponding to a target probability. The approach is consistent with PSHA methodology, though the specific choice of target AEP requires external specification.]

