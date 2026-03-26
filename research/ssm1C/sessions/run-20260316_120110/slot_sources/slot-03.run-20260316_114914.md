## SLOT 3: Earthquake Recurrence Parameters

Earthquake recurrence parameters quantify the expected rate and size distribution of future earthquakes on each seismic source. Recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source. All 108 area sources use the truncated Gutenberg-Richter MFD (`truncGutenbergRichterMFD`), parameterised by an $a$-value (the logarithm of the rate of earthquakes above $M = 0$), a $b$-value (the slope of the log-linear frequency-magnitude relationship), and explicit bounds $M_{\min}$ and $M_{\max}$. The two smoothed-seismicity grid models inherit the same Gutenberg-Richter parametrisation from the parent areal zones, distributed over a regular spatial grid; per-node $a$-values are derived from the zonal rates and therefore represent distributed rates over fine grid cells rather than whole-zone rates. [KB:source_model.md]^[Confidence: HIGH, Rationale: MFD type and parameterisation are explicitly stated in source_model.md for all 108 area sources and for the smoothed-seismicity grids. The derivation of grid-node parameters from areal zone rates is stated in source_model.md.]

The table below summarises recurrence parameters by tectonic region type for the 108 area sources. The $M_{\min}$ is 4.5 Mw for all four groups. Epistemic uncertainty in $b$-value is captured through logic-tree branch set 3 ($\Delta b = \pm 0.1$; weights 0.32, 0.36, 0.32). [KB:source_model.md]^[Confidence: HIGH, Rationale: All tabulated values are directly extracted from source_model.md. The $M_{\min}$ of 4.5 Mw for all area sources is stated explicitly. The b-value epistemic treatment via branch set 3 is documented in source_model.md.]

| Tectonic region | $n$ | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) |
|---|---:|---|---|---|---:|---|
| ASC | 29 | truncGR | 2.73 - 7.08 | 0.72 - 1.37 | 4.5 | 7.0 - 8.8 |
| SCC | 17 | truncGR | 1.58 - 4.84 | 0.63 - 1.19 | 4.5 | 6.0 - 8.2 |
| SIF | 27 | truncGR | 3.12 - 5.40 | 0.72 - 1.24 | 4.5 | 6.5 - 9.4 |
| SIS | 35 | truncGR | 3.22 - 7.33 | 0.80 - 1.57 | 4.5 | 6.5 - 8.6 |

