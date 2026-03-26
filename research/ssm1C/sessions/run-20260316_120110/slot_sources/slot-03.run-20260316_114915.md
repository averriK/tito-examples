## SLOT 3: Earthquake Recurrence Parameters

Earthquake recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source. All 108 area sources use the truncated Gutenberg-Richter distribution (`truncGutenbergRichterMFD`), parameterised by an $a$-value and a $b$-value with fixed $M_{\min}$ = 4.5 Mw and explicit $M_{\max}$ bounds. The smoothed point-source models inherit the same Gutenberg-Richter parametrisation from the parent areal zones, distributed over a regular spatial grid; no distinct $a$- or $b$-values are independently specified for individual point sources. [KB:source_model.md]^[Confidence: HIGH, Rationale: The MFD type, Mmin = 4.5 Mw, and the inheritance of GR parameters by point sources are all explicitly stated in source_model.md. The site-specific data for z919 and z932 in site_sources.md confirms Mmin = 4.5 Mw for the SCC zones at the project site.]

Table 1 summarises the earthquake recurrence parameters across the four tectonic region types for the area source model. The $a$-value and $b$-value ranges reflect the spread across all sources within each TRT. The $M_{\max}$ values are base (central) values prior to application of the $M_{\max}$ perturbation logic-tree branches; epistemic uncertainty in $M_{\max}$ is addressed separately in SLOT 6. [KB:source_model.md]^[Confidence: HIGH, Rationale: Recurrence parameter ranges by TRT are directly tabulated in source_model.md ("Earthquake Recurrence Parameters" section). The total source counts per TRT (29 + 17 + 27 + 35 = 108) are internally consistent with the stated total of 108 area sources.]

**Table 1. Earthquake recurrence parameters by tectonic region type (area sources, base values).**^[Confidence: HIGH, Rationale: Table caption only; descriptive label for the following table, whose values are drawn from source_model.md.]

| Tectonic Region | MFD Type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) | $n$ |
|---|---|---|---|---|---|---|
| Active Shallow Crust (ASC) | truncGR | 2.73-7.08 | 0.72-1.37 | 4.5 | 7.0-8.8 | 29 |
| Stable Continental Crust (SCC) | truncGR | 1.58-4.84 | 0.63-1.19 | 4.5 | 6.0-8.2 | 17 |
| Subduction Interface (SIF) | truncGR | 3.12-5.40 | 0.72-1.24 | 4.5 | 6.5-9.4 | 27 |
| Subduction Intraslab (SIS) | truncGR | 3.22-7.33 | 0.80-1.57 | 4.5 | 6.5-8.6 | 35 |

