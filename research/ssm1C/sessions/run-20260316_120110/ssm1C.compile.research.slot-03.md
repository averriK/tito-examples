## SLOT 3: Earthquake Recurrence Parameters

All 108 area sources employ the truncated Gutenberg-Richter MFD (`truncGutenbergRichterMFD`), parameterised by an $a$-value and a $b$-value with explicit $M_{\min}$ and $M_{\max}$ bounds. The minimum magnitude is 4.5 Mw for area sources in Active Shallow Crust, Stable Continental Crust, and Subduction Interface settings; Subduction Intraslab sources encompass a range of $M_{\min}$ values from 4.5 to 7.5 Mw reflecting the variable depth of deep slab zones. Epistemic uncertainty in the $b$-value is captured through logic-tree branch set 3, which applies simultaneous relative perturbations of $-0.1$, $0.0$, and $+0.1$ (weights 0.32, 0.36, 0.32); $M_{\max}$ uncertainty treatment is addressed in SLOT 6. The two smoothed-seismicity point-source grids inherit the same Gutenberg-Richter parametrisation from the parent areal zones, distributed over a regular spatial grid; individual grid nodes carry spatially redistributed $a$-values derived from parent zone rates rather than independently fitted catalogue statistics [@Nath2012].

Table 1 summarises the recurrence parameters for the 108 area sources grouped by tectonic region type. The $M_{\max}$ values are base (central) estimates prior to application of the $M_{\max}$ logic-tree perturbation.

**Table 1. Earthquake recurrence parameters by tectonic region type (108 area sources, base values).**

| Tectonic region | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) | $n$ |
|---|---|---|---|---|---|---|
| Active Shallow Crust (ASC) | truncGR | 2.73-7.08 | 0.72-1.37 | 4.5 | 7.0-8.8 | 29 |
| Stable Continental Crust (SCC) | truncGR | 1.58-4.84 | 0.63-1.19 | 4.5 | 6.0-8.2 | 17 |
| Subduction Interface (SIF) | truncGR | 3.12-5.40 | 0.72-1.24 | 4.5 | 6.5-9.4 | 27 |
| Subduction Intraslab (SIS) | truncGR | 3.22-7.33 | 0.80-1.57 | 4.5-7.5 | 6.5-8.6 | 35 |
