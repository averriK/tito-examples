## SLOT 3: Earthquake Recurrence Parameters

All 108 area sources in the IND model employ the truncated Gutenberg-Richter MFD (`truncGutenbergRichterMFD`), in which earthquake occurrence rates are parameterised by an $a$-value, a $b$-value, and explicit $M_{\min}$ and $M_{\max}$ bounds. The minimum magnitude $M_{\min}$ is 4.5 Mw for area sources in the shallow and intermediate tectonic regions; deep Subduction Intraslab (SIS) sources may adopt $M_{\min}$ up to 7.5 Mw. Epistemic uncertainty in the $b$-value is captured through logic-tree branch set 3, applying simultaneous relative perturbations of -0.1, 0.0, and +0.1 with weights 0.32, 0.36, and 0.32 [KB:source_model.md].^[Confidence: HIGH, Rationale: MFD type, Mmin range, and b-value epistemic branch details are stated explicitly in KB:source_model.md; the b-value branch set is confirmed in KB:site_sources_data.md.]

The two smoothed-seismicity point-source models do not carry independently specified $a$- or $b$-values at the individual point-source level; instead, they inherit their truncated GR parametrisation from the parent areal zone model, distributed spatially over a regular grid. The rate specification method for point sources is therefore one of spatial redistribution of the parent zone activity rather than independent catalogue fitting. Table 1 presents the recurrence parameters for the 108 area sources grouped by tectonic region type [KB:source_model.md].^[Confidence: HIGH, Rationale: Point-source inheritance from areal zones is explicitly stated in KB:source_model.md. Parameter ranges in Table 1 are reproduced from the recurrence table in KB:source_model.md. TRT counts sum to 29 + 17 + 27 + 35 = 108, consistent with the total area source count.]

**Table 1. Earthquake recurrence parameters by tectonic region type (108 area sources).**

| Tectonic region | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) | $n$ |
|---|---|---|---|---|---|---|
| Active Shallow Crust (ASC) | truncGR | 2.73-7.08 | 0.72-1.37 | 4.50 | 7.0-8.8 | 29 |
| Stable Continental Crust (SCC) | truncGR | 1.58-4.84 | 0.63-1.19 | 4.50 | 6.0-8.2 | 17 |
| Subduction Interface (SIF) | truncGR | 3.12-5.40 | 0.72-1.24 | 4.50 | 6.5-9.4 | 27 |
| Subduction Intraslab (SIS) | truncGR | 3.22-7.33 | 0.80-1.57 | 4.50-7.50 | 6.5-8.6 | 35 |

