# Seismic Source Model Analysis: IND Indian Subcontinent

## 1. SSM Overview and Source Census

The seismic source model (SSM) defines the spatial distribution, geometry, and earthquake occurrence rates of all seismogenic sources considered capable of contributing to ground-motion hazard at the site. It is the principal input to the probabilistic seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model logic tree (ssmLT) that captures epistemic uncertainty by assigning weights to alternative model configurations.

The IND model is based on the probabilistic seismic hazard model for the Indian subcontinent developed by Nath and Thingbaijam [@Nath2012], subsequently updated and translated into OpenQuake format in collaboration with Natural Resources Canada (version v2012.2.0), as documented in the GEM model report [@GemInd2012]. The model domain extends from approximately $60.0^\circ$E to $100.8^\circ$E in longitude and $2.0^\circ$N to $40.0^\circ$N in latitude, covering India, Bangladesh, Bhutan, Nepal, Pakistan, Myanmar, and surrounding regions of the Indian subcontinent. The minimum earthquake magnitude ($M_{\min}$) adopted for hazard calculations is 4.5 Mw across all area sources; the two smoothed-seismicity grids employ $M_{\min}$ thresholds of 4.5 Mw and 5.5 Mw respectively.

The IND SSM comprises 443,197 seismic sources of two types: 108 area sources (`areaSource`) and 443,089 point sources (`pointSource`). These sources span four tectonic region types (TRTs); the table below provides the complete census by TRT and source type.

| Tectonic region type | Code | Area sources | Point sources | Total |
|---|---|---:|---:|---:|
| Subduction Intraslab | SIS | 35 | 139,942 | 139,977 |
| Subduction Interface | SIF | 27 | 123,748 | 123,775 |
| Stable Continental Crust | SCC | 17 | 94,433 | 94,450 |
| Active Shallow Crust | ASC | 29 | 84,966 | 84,995 |
| **Total** | | **108** | **443,089** | **443,197** |

The SSM is defined through three logic-tree XML files: `ssmLT_IND.xml` (the primary logic tree with three branch sets), `ssmLT_IND_collapsed.xml` (a collapsed variant), and `ssmLT_IND_garage_v1.xml` (a full alternative variant). The primary logic tree references three source-model XML files and produces 27 end-branches from the Cartesian product of three branch sets ($3 \times 3 \times 3 = 27$). The branch set structure is described in detail in Section 2.

Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [@Cornell1968] and formalised under SSHAC guidelines [@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with geometry and parametrisation defined in OpenQuake source-model XML files. The implementation is publicly available at the `nackerley/indian-subcontinent-psha` repository on GitHub [@NackerleyRepo].

## 2. Source-Model Logic Tree Structure

The source-model logic tree (`ssmLT_IND.xml`) encodes epistemic uncertainty through three branch sets, collectively producing $3 \times 3 \times 3 = 27$ end-branches. Each branch set addresses a distinct type of epistemic uncertainty; branches within each set carry weights reflecting the relative credibility of each alternative [@GemInd2012].

### 2.1 Branch Set 1: Source Model Selection (`sourceModel`)

Branch set 1 addresses source-model selection, offering three alternative source-model representations of the regional seismicity. Branch `b1m1` selects the 108-zone areal source model; branches `b1m2` and `b1m3` select spatially smoothed point-source grids with $M_{\min}$ thresholds of 4.5 Mw and 5.5 Mw respectively.

| Branch | Model file | Weight |
|---|---|---:|
| `b1m1` | `nt2012_areal_source_model_v1.xml` | 0.40 |
| `b1m2` | `nt2012_smoothed_source_model_v1_mmin4.5.xml` | 0.27 |
| `b1m3` | `nt2012_smoothed_source_model_v1_mmin5.5.xml` | 0.33 |

### 2.2 Branch Set 2: Maximum Magnitude Perturbation (`maxMagGRRelative`)

Branch set 2 applies simultaneous relative perturbations to the base $M_{\max}$ of all sources. The symmetric flanking branches ($\pm 0.3$ Mw) each carry weight 0.32; the unperturbed central branch carries the higher weight of 0.36, reflecting greater credibility attributed to the nominal parameter estimate.

| Branch | Perturbation ($\Delta M_{\max}$, Mw) | Weight |
|---|---:|---:|
| `b2m1` | $-0.3$ | 0.32 |
| `b2m2` | $0.0$ | 0.36 |
| `b2m3` | $+0.3$ | 0.32 |

### 2.3 Branch Set 3: $b$-Value Perturbation (`bGRRelative`)

Branch set 3 applies simultaneous relative perturbations to the Gutenberg-Richter $b$-value of all sources, with the same symmetric weight structure as branch set 2.

| Branch | Perturbation ($\Delta b$) | Weight |
|---|---:|---:|
| `b3m1` | $-0.1$ | 0.32 |
| `b3m2` | $0.0$ | 0.36 |
| `b3m3` | $+0.1$ | 0.32 |

The combined weights within each branch set sum to unity: source-model branches sum to $0.40 + 0.27 + 0.33 = 1.00$; both perturbation branch sets sum to $0.32 + 0.36 + 0.32 = 1.00$.

## 3. Earthquake Recurrence Parameters

All 108 area sources employ the truncated Gutenberg-Richter MFD (`truncGutenbergRichterMFD`), parameterised by an $a$-value and a $b$-value with explicit $M_{\min}$ and $M_{\max}$ bounds. The minimum magnitude is 4.5 Mw for area sources in Active Shallow Crust, Stable Continental Crust, and Subduction Interface settings; Subduction Intraslab sources encompass a range of $M_{\min}$ values from 4.5 to 7.5 Mw reflecting the variable depth of deep slab zones. Epistemic uncertainty in the $b$-value is captured through logic-tree branch set 3, which applies simultaneous relative perturbations of $-0.1$, $0.0$, and $+0.1$ (weights 0.32, 0.36, 0.32); $M_{\max}$ uncertainty treatment is addressed in Section 6. The two smoothed-seismicity point-source grids inherit the same Gutenberg-Richter parametrisation from the parent areal zones, distributed over a regular spatial grid; individual grid nodes carry spatially redistributed $a$-values derived from parent zone rates rather than independently fitted catalogue statistics [@Nath2012].

Table 1 summarises the recurrence parameters for the 108 area sources grouped by tectonic region type. The $M_{\max}$ values are base (central) estimates prior to application of the $M_{\max}$ logic-tree perturbation.

**Table 1. Earthquake recurrence parameters by tectonic region type (108 area sources, base values).**

| Tectonic region | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) | $n$ |
|---|---|---|---|---|---|---|
| Active Shallow Crust (ASC) | truncGR | 2.73-7.08 | 0.72-1.37 | 4.5 | 7.0-8.8 | 29 |
| Stable Continental Crust (SCC) | truncGR | 1.58-4.84 | 0.63-1.19 | 4.5 | 6.0-8.2 | 17 |
| Subduction Interface (SIF) | truncGR | 3.12-5.40 | 0.72-1.24 | 4.5 | 6.5-9.4 | 27 |
| Subduction Intraslab (SIS) | truncGR | 3.22-7.33 | 0.80-1.57 | 4.5-7.5 | 6.5-8.6 | 35 |

## 4. Magnitude-Frequency Distribution Types

The IND source model employs a single MFD type for all 108 area sources and all smoothed-seismicity point-source grids: the truncated Gutenberg-Richter distribution (`truncGutenbergRichterMFD`). Under this parametrisation, earthquake occurrence rates are expressed as a log-linear function of magnitude, bounded at $M_{\min}$ and $M_{\max}$, and governed by the $a$-value (total activity rate intercept at the reference magnitude) and the $b$-value (slope of the frequency-magnitude relation). The `incrementalMFD`, `arbitraryMFD`, and `multiMFD` distribution types are not present in this model; characteristic or hybrid MFD formulations are likewise absent.

Three magnitude-area scaling relationships are applied across different tectonic environments to relate moment magnitude to rupture dimensions. The Wells and Coppersmith (1994) relationship (`WC1994`) [@Wells1994] is applied to 46 area sources in Active Shallow Crust and Stable Continental Crust settings. The Strasser et al. (2010) intraslab relationship (`StrasserIntraslab`) [@Strasser2010] is applied to 35 area sources in Subduction Intraslab settings. The Strasser et al. (2010) interface relationship (`StrasserInterface`) [@Strasser2010] is applied to 27 area sources in Subduction Interface settings. The sum $46 + 35 + 27 = 108$ accounts for all area sources. All area sources adopt a rupture aspect ratio of 2.0.

## 5. Slip-Rate Data and Moment Balance

Activity rates for fault sources with available slip-rate data are in principle derived from seismic-moment balance, where the seismic moment rate $\dot{M}_0$ is related to the shear modulus $\mu$, fault area $A$, and long-term slip rate $S$:

$$\dot{M}_0 = \mu\, A\, S$$

The IND source model contains no fault sources. The complete source inventory consists exclusively of 108 areal seismogenic zones and 443,089 spatially distributed point sources in two smoothed-seismicity grids; no fault-source XML files are present, and no slip-rate data are specified for any source. Accordingly, the number of sources with slip-rate data is zero, and no slip-rate range is applicable within this model. Recurrence parameters for all area sources are derived from seismological catalogue statistics via Gutenberg-Richter fitting, as documented in the source-model implementation [@Nath2012][@GemInd2012].

## 6. Maximum Magnitude Characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the MFD for each source and is a critical parameter controlling the tail of the hazard curve. For all 108 area sources, base $M_{\max}$ values range from 6.0 to 9.4 Mw across the four tectonic region types, reflecting environments spanning from stable continental crust to subduction megathrust settings. The highest base $M_{\max}$ values correspond to Subduction Interface zones -- such as the Sumatra and Himalaya-Main Frontal Thrust systems -- where great earthquakes exceeding $M$ 8.5 are considered possible. $M_{\max}$ values are assigned per zone from the seismotectonic characterisation study by Nath and Thingbaijam [@Nath2012] and are set as explicit parameters within the `truncGutenbergRichterMFD` specification.

Epistemic uncertainty in $M_{\max}$ is captured through `maxMagGRRelative` logic-tree branch set 2, which applies simultaneous perturbations of $\Delta = -0.3$, $0.0$, and $+0.3$ Mw to all sources (weights 0.32, 0.36, 0.32). For the smoothed-seismicity point-source grids, $M_{\max}$ is inherited from the parent areal zone parametrisation; point-source $M_{\max}$ values are not independently constrained and follow the same global perturbation scheme.

Table 2 summarises the base $M_{\max}$ ranges by tectonic region type together with the derived epistemic bounds.

**Table 2. Maximum magnitude ($M_{\max}$) characterisation by tectonic region type (base and epistemic bounds, area sources).**

| Tectonic region | Base $M_{\max}$ (Mw) | Low ($\Delta - 0.3$, Mw) | High ($\Delta + 0.3$, Mw) | Derivation method |
|---|---|---|---|---|
| ASC | 7.0-8.8 | 6.7-8.5 | 7.3-9.1 | truncGutenbergRichterMFD |
| SCC | 6.0-8.2 | 5.7-7.9 | 6.3-8.5 | truncGutenbergRichterMFD |
| SIF | 6.5-9.4 | 6.2-9.1 | 6.8-9.7 | truncGutenbergRichterMFD |
| SIS | 6.5-8.6 | 6.2-8.3 | 6.8-8.9 | truncGutenbergRichterMFD |

## 7. Seismogenic Depth Parameters

The seismogenic depth model in the IND SSM reflects a multi-layer structure consistent with the tectonic environment assigned to each source zone. Active Shallow Crust (ASC) sources are confined to the upper 25 km, with upper seismogenic depth $z_{\text{upper}}$ = 0 km, lower seismogenic depth $z_{\text{lower}}$ = 25 km, and mean hypocentral depth 15 km. Stable Continental Crust (SCC) sources span $z_{\text{upper}}$ = 0-25 km and $z_{\text{lower}}$ = 25-70 km, with mean hypocentral depths of 15-25 km. Subduction Interface (SIF) sources exhibit $z_{\text{upper}}$ = 0-70 km and $z_{\text{lower}}$ = 25-180 km, with mean hypocentral depths of 15-70 km. Subduction Intraslab (SIS) sources occupy the deepest zone, with $z_{\text{upper}}$ = 25-180 km, $z_{\text{lower}}$ = 70-300 km, and mean hypocentral depths of 25-180 km. Hypocentral depth distributions are specified as single-value distributions with probability 1.0 for all area sources; that is, a single representative hypocentral depth is assigned deterministically to each zone.

**Table 3. Seismogenic depth parameters by tectonic region type (area sources).**

| Tectonic region | $z_{\text{upper}}$ (km) | $z_{\text{lower}}$ (km) | Mean hypocentral depth (km) |
|---|---|---|---|
| Active Shallow Crust (ASC) | 0 | 25 | 15 |
| Stable Continental Crust (SCC) | 0-25 | 25-70 | 15-25 |
| Subduction Interface (SIF) | 0-70 | 25-180 | 15-70 |
| Subduction Intraslab (SIS) | 25-180 | 70-300 | 25-180 |

The depth structure reflects a three-layer architecture: shallow crustal sources (ASC and the upper SCC layer) are confined to the uppermost 25 km; intermediate-depth zones (lower SCC and the upper portions of the subduction envelopes) extend to 70 km; and deep subduction intraslab zones reach 300 km depth. The wide depth ranges for SIF and SIS reflect the global variability of subduction geometries included in the model domain, from shallow interface contact zones to deep slab ruptures.

## 8. Local Sources and Site Interrogation

The Rampura Agucha site ($74.7413^\circ$E, $25.8474^\circ$N) is located in Rajasthan within the Peninsular Indian shield. The site is contained within two overlapping areal seismogenic zones in the IND model: zone z919 (Peninsular India Layer 1, shallow SCC) and zone z932 (Peninsular India Layer 2, intermediate SCC). Both zones are classified under the Stable Continental Crust (SCC) tectonic regime; no Active Shallow Crust, Subduction Interface, or Subduction Intraslab sources include the site. No fault sources are present in the IND model. Zone z919 is designated as the primary zone for the site by the source-selection algorithm.

Zone z919 represents the shallow crustal seismogenic layer: upper seismogenic depth 0.0 km, lower depth 25.0 km, mean hypocentral depth 15.0 km. Its base $M_{\max}$ is 7.20 Mw (epistemic range 6.90-7.50 Mw), with $a$ = 2.73, $b$ = 0.72 (base), and $M_{\min}$ = 4.5 Mw. The focal mechanism is reverse faulting (nodal plane: strike $290^\circ$, dip $61^\circ$, rake $123^\circ$).

Zone z932 represents the intermediate seismogenic layer: upper depth 25.0 km, lower depth 70.0 km, mean hypocentral depth 25.0 km. Its base $M_{\max}$ is 6.50 Mw (epistemic range 6.20-6.80 Mw), with $a$ = 4.15, $b$ = 0.93 (base), and $M_{\min}$ = 4.5 Mw. The focal mechanism is sinistral strike-slip faulting (nodal plane: strike $239^\circ$, dip $67^\circ$, rake $8^\circ$).

The surrounding source environment is characterised exclusively by intraplate SCC seismicity, consistent with the stable shield character of Peninsular India. Based on the parameters of the two enclosing zones, the magnitude range applicable to the immediate site vicinity extends from $M_{\min}$ = 4.5 Mw to a base $M_{\max}$ of 7.20 Mw (zone z919), with mean hypocentral depths of 15-25 km and dominant reverse and sinistral strike-slip faulting mechanisms. The supplementary intermediate-depth zone z932 carries a lower magnitude potential (base $M_{\max}$ 6.50 Mw) at depths of 25-70 km. The two zones described here represent the geometric candidates from source-to-site proximity analysis; definitive identification of the controlling sources requires deaggregation of the PSHA results.

## 9. Smoothed-Seismicity Nearest Point Sources

In addition to the areal source model (branch b1m1, weight 0.40), the logic tree includes two smoothed-seismicity branches with a combined weight of 0.60. For each branch, the nearest point source to the Rampura Agucha site was identified by geometric proximity search across the grid index. Both nearest sources lie within the intermediate SCC layer (depth 25-70 km), consistent with parent areal zone z932.

**Branch b1m2 (`nt2012_smoothed_source_model_v1_mmin4.5.xml`, weight 0.27)**

Nearest source: `25N_75p2E_L2_M4p5`, located at $75.20^\circ$E, $25.00^\circ$N, at a distance of 104.60 km from the site. MFD: truncated Gutenberg-Richter with $M_{\min}$ = 4.5 Mw, $a$ = $-1.4682$, base $b$ = 0.93 (epistemic range 0.83-1.03). Base $M_{\max}$ = 6.5 Mw (low: 6.2 Mw; high: 6.8 Mw). Seismogenic depth range: 25.0-70.0 km; mean hypocentral depth: 25.0 km.

**Branch b1m3 (`nt2012_smoothed_source_model_v1_mmin5.5.xml`, weight 0.33)**

Nearest source: `26p7N_74p1E_L2_M5p5`, located at $74.10^\circ$E, $26.70^\circ$N, at a distance of 114.13 km from the site. MFD: truncated Gutenberg-Richter with $M_{\min}$ = 5.5 Mw, $a$ = $-0.9144$, base $b$ = 0.93 (epistemic range 0.83-1.03). Base $M_{\max}$ = 6.5 Mw (low: 6.2 Mw; high: 6.8 Mw). Seismogenic depth range: 25.0-70.0 km; mean hypocentral depth: 25.0 km.

Both nearest smoothed-seismicity point sources lie more than 100 km from the site. The shared $b$ = 0.93 and $M_{\max}$ = 6.5 Mw (base) at these grid nodes are consistent with the parameters of overlapping areal zone z932, confirming that the smoothed-seismicity grids reproduce the parent zone characterisation at the site location. The higher $a$-value of the mmin5.5 nearest source ($-0.9144$ versus $-1.4682$) reflects the spatial redistribution of activity above $M$ 5.5 rather than above $M$ 4.5 on the grid cells in that region.
