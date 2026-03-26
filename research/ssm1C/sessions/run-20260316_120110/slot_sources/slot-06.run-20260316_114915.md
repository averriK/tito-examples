## SLOT 6: Maximum Magnitude Characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the MFD for each source and is a critical parameter controlling the tail of the hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through `maxMagGRRelative` logic-tree branch set 2, which applies simultaneous perturbations of $\Delta = -0.3$, $0.0$, and $+0.3$ Mw to all sources (weights 0.32, 0.36, 0.32). The derivation method for all area sources is the truncated Gutenberg-Richter MFD, with $M_{\max}$ assigned per zone from the source characterisation study by Nath and Thingbaijam [-@Nath2012]. For smoothed point-source models, $M_{\max}$ is inherited from the parent areal zone parametrisation; the same logic-tree perturbations apply to these sources. [KB:source_model.md]^[Confidence: HIGH, Rationale: The Mmax epistemic treatment via maxMagGRRelative branches (perturbations -0.3/0.0/+0.3 Mw, weights 0.32/0.36/0.32) is explicitly documented in source_model.md. The attribution to Nath and Thingbaijam (2012) is stated in the provenance section. The logic-tree structure is confirmed by site_sources_data.md for the Rampura Agucha site.]

Table 2 summarises the base $M_{\max}$ ranges for each tectonic region type, along with the resulting low and high epistemic bounds. The highest $M_{\max}$ values correspond to Subduction Interface settings, where great earthquakes ($M > 8.5$) are considered possible along the Sumatra and Himalaya-Main Frontal Thrust systems. [KB:source_model.md]^[Confidence: HIGH, Rationale: Mmax ranges by TRT are directly tabulated in source_model.md. The statement about the highest Mmax zones (SIF, great earthquakes $M > 8.5$) is explicitly stated in the "Maximum Magnitude" section of source_model.md. The low/high bounds are derived by simple arithmetic ($\pm 0.3$ Mw) applied to the stated base ranges, which is consistent with the logic-tree branch perturbations.]

**Table 2. Maximum magnitude ($M_{\max}$) characterisation by tectonic region type (base and epistemic bounds, area sources).**^[Confidence: HIGH, Rationale: Table caption only; descriptive label for the following table, whose values are drawn from source_model.md.]

| Tectonic Region | Base $M_{\max}$ (Mw) | Low ($\Delta - 0.3$, Mw) | High ($\Delta + 0.3$, Mw) | Derivation method |
|---|---|---|---|---|
| ASC | 7.0-8.8 | 6.7-8.5 | 7.3-9.1 | truncGutenbergRichterMFD |
| SCC | 6.0-8.2 | 5.7-7.9 | 6.3-8.5 | truncGutenbergRichterMFD |
| SIF | 6.5-9.4 | 6.2-9.1 | 6.8-9.7 | truncGutenbergRichterMFD |
| SIS | 6.5-8.6 | 6.2-8.3 | 6.8-8.9 | truncGutenbergRichterMFD |

