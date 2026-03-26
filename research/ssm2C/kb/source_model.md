# Seismic Source Model

## Overview of the Seismic Source Model

The seismic source model (SSM) defines the spatial distribution, geometry, and earthquake
occurrence rates of all seismogenic sources considered capable of contributing to the
ground-motion hazard at the site. The SSM is the principal input to the probabilistic
seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model
logic tree (ssmLT) that captures epistemic uncertainty by assigning weights to alternative
model configurations. This section provides an overview of the SSM structure: the source
types included, the geographic extent of the model domain, and the minimum earthquake
magnitude ($M_{\min}$) adopted for hazard calculations. The parameterisation of individual
sources is described in the following sections.

The XAF seismic source model comprises 255 seismic sources of two types: 115 simple fault sources (`simpleFaultSource`) and 140 multi-point sources (`multiPointSource`). These sources are classified into two tectonic region types: Active Shallow Crust (ASC, 150 sources) and Stable Continental Crust (SCC, 105 sources). The model is defined through two logic-tree files — `ssmLT_XAF.xml` (the full logic tree with 5 branch sets) and `ssmLT_XAF_collapsed.xml` (a collapsed variant with a single branch set) — referencing five source-model XML files. Source types `griddedSeismicitySource` and `pointSource` were excluded from the detailed analysis. The minimum magnitude ($M_{\min}$) across all sources is 4.0 Mw (multi-point sources range from 4.0 to 4.5; fault sources are defined from 6.05 Mw).

The model domain extends from approximately 19.5°W to 52.9°E in longitude and 28.7°S to 38.5°N in latitude, covering North Africa, West Africa, and parts of sub-Saharan Africa.

[FIGURE: Map of the seismic source model domain showing all source zones or fault traces,
and the site location where applicable.]

### Adopted Source Model

The adopted SSM is a composite of independently published component models assembled under the GEM Global Seismic Hazard Map programme. All 255 sources are attributed to the North Africa (NAF) seismic hazard model developed by Poggi et al. [-@Poggi2020]. Fault source geometries and kinematics are derived from the GEM North Africa Active Fault Database (NAAFD) compiled by Styron and Poggi [-@Styron2018]. The model is composed of five source-model XML files:

- **`ssm_XAF/FaultSources.xml`** — 115 simple fault sources representing mapped active faults across the NAF domain.
- **`ssm_XAF/GridMultiSources_C.xml`** — Multi-point sources representing smoothed seismicity for the NAF region (used in the `naf_smooth` branch).
- **`ssm_XAF/GridMultiSources_C_L50_BG.xml`** — Multi-point sources combining smoothed seismicity with background rates (used in the `naf_faults` branch alongside `FaultSources.xml`).
- **`ssm_XAF/WAF_GridMultiSources_Collapsed.xml`** — Collapsed multi-point sources for West Africa.
- **`ssm_XAF/SSA_GridMultiSources_Collapsed.xml`** — Collapsed multi-point sources for sub-Saharan Africa.

## Source Model Methodology

Seismic-source characterisation follows the classical PSHA framework outlined by
Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources
are delineated from geologic, geophysical, and seismological evidence, with their
geometry and parametrisation defined in OpenQuake source-model XML files and encoded
in the logic tree.

Three magnitude-frequency distribution (MFD) types are present in this model:

- **Truncated Gutenberg–Richter** (`multiMFD:truncGutenbergRichterMFD`) — Used by 86 multi-point sources (predominantly the SC_1–SC_54 sources and MPS-1–MPS-6 sources in the NAF smoothed seismicity component). Earthquake rates are parameterised by an $a$-value (range: 3.13–5.45) and $b$-value (range: 0.93–1.16) with explicit $M_{\min}$ and $M_{\max}$ bounds.
- **Incremental MFD** (`incrementalMFD`) — Used by all 115 fault sources. Occurrence rates are specified as discrete values per magnitude bin (bin width 0.1 Mw); $a$- and $b$-values are not defined. This formulation directly encodes the expected rate at each magnitude level.
- **Arbitrary MFD** (`multiMFD:arbitraryMFD`) — Used by 54 multi-point sources (the BG_1–BG_54 background sources). Occurrence rates are specified at arbitrary magnitude points without an underlying parametric model.

Two magnitude-area scaling relationships are applied: `Leonard2014_Interplate` [@Leonard2014] for all 115 fault sources, and `WC1994` [@Wells1994] for all 140 multi-point sources.

Unless the logic tree includes a time-dependent (renewal) branch, temporal occurrence
is modelled as a stationary Poisson process — the canonical assumption in standard PSHA.

## Logic Tree Structure

The source-model logic tree encodes epistemic uncertainty by defining alternative
realisations of the SSM. Each branch set addresses a specific source of uncertainty
(e.g., alternative source-model geometries, maximum-magnitude perturbations, or
b-value perturbations), and the branches within each set are assigned weights reflecting
the relative credibility of each alternative.

### Primary logic tree (`ssmLT_XAF.xml`)

The primary logic tree contains five branch sets producing 2 × 3 × 3 × 3 × 3 = **162 end-branches**:

**Branch set 1 — Source model selection** (`sourceModel`, applies to all sources):

| Branch | Model files | Weight |
|--------|------------|--------|
| `naf_faults` | FaultSources.xml + GridMultiSources_C_L50_BG.xml + WAF + SSA collapsed | 0.50 |
| `naf_smooth` | GridMultiSources_C.xml + WAF + SSA collapsed | 0.50 |

The first branch includes explicit fault sources alongside background smoothed seismicity; the second replaces fault sources with a purely smoothed seismicity representation.

**Branch set 2 — $M_{\max}$ perturbation for WAF sources** (`maxMagGRRelative`, applies to MPS-1 through MPS-6):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `waf_m_m0.2` | +0.2 | 0.25 |
| `waf_m_e0.0` | 0.0 | 0.50 |
| `waf_m_p0.2` | −0.2 | 0.25 |

**Branch set 3 — $b$-value perturbation for WAF sources** (`bGRRelative`, applies to MPS-1 through MPS-6):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `waf_b_m0.05` | +0.05 | 0.25 |
| `waf_b_e0.0` | 0.0 | 0.50 |
| `waf_b_p0.05` | −0.05 | 0.25 |

**Branch set 4 — $b$-value perturbation for NAF sources** (`bGRRelative`, applies to SC_1 through SC_54):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `naf_b_m0.05` | +0.05 | 0.25 |
| `naf_b_e0.0` | 0.0 | 0.50 |
| `naf_b_p0.05` | −0.05 | 0.25 |

**Branch set 5 — $M_{\max}$ perturbation for NAF sources** (`maxMagGRRelative`, applies to SC_1 through SC_54):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `naf_m_m0.2` | +0.2 | 0.25 |
| `naf_m_e0.0` | 0.0 | 0.50 |
| `naf_m_p0.2` | −0.2 | 0.25 |

### Collapsed logic tree (`ssmLT_XAF_collapsed.xml`)

A collapsed variant retains only branch set 1 (source-model selection, 2 branches). This represents a mean-hazard approximation where epistemic uncertainty in $M_{\max}$ and $b$-value has been pre-collapsed into the source parameters.

## Seismic Sources

### Simple Fault Sources

The model includes 115 simple fault sources from `ssm_XAF/FaultSources.xml`, representing mapped active faults across the North Africa domain. These sources span two tectonic region types: Active Shallow Crust (ASC, 69 sources) and Stable Continental Crust (SCC, 46 sources).

**Geometry**: Fault traces are defined as polylines (`geom_kind = line`) with 2 to 53 vertices per trace. The fault sources span the full model domain from approximately 9°W to 36°E in longitude and 29°N to 38°N in latitude, concentrated along the North African plate boundary.

**Depth**: Upper seismogenic depth is 0.0 km for all faults. Lower seismogenic depth ranges from 1.7 km to 25.0 km.

**Focal mechanism**: Rakes are defined for all 115 faults. The dominant faulting styles are reverse (rake = 90°, 52 sources) and normal (rake = −90°, 29 sources), with strike-slip and oblique mechanisms accounting for the remainder (34 sources with rakes of 0°, ±45°, ±135°, 180°, and 157.5°).

**Magnitude scaling**: All fault sources use the `Leonard2014_Interplate` magnitude-area scaling relationship with a rupture aspect ratio of 2.0.

**MFD**: All 115 fault sources use an incremental MFD (`incrementalMFD`) with a bin width of 0.1 Mw, starting at $M_{\min}$ = 6.05. Activity rates are specified as discrete occurrence rates per magnitude bin; $a$- and $b$-values are not defined for these sources. Maximum magnitudes range from 6.05 to 7.75 Mw.

### Multi-Point Sources

The model includes 140 multi-point sources distributed across four source-model XML files, representing smoothed and background seismicity. These sources span Active Shallow Crust (ASC, 81 sources) and Stable Continental Crust (SCC, 59 sources).

The multi-point sources comprise three functional groups:

- **MPS sources** (MPS-1 through MPS-6): 6 sources representing West African smoothed seismicity. These use a truncated Gutenberg–Richter MFD.
- **SC sources** (SC_1 through SC_54): 54 sources from the NAF component plus additional WAF/SSA collapsed sources with truncated GR MFD. Total: 80 sources with `multiMFD:truncGutenbergRichterMFD`.
- **BG sources** (BG_1 through BG_54): 54 background sources using `multiMFD:arbitraryMFD`.

**Geometry**: Defined as grid point sets (`geom_kind = points`) spanning the full model domain (approximately 19.5°W to 52.9°E, 28.7°S to 38.5°N).

**Depth**: Upper seismogenic depth is 0.0 km for all multi-point sources. Lower seismogenic depth ranges from 40.0 to 45.0 km.

**Focal mechanism**: Nodal plane distributions are defined for all 140 multi-point sources, specifying strike, dip, rake, and probability for each nodal plane.

**Magnitude scaling**: All multi-point sources use `WC1994` [@Wells1994] with a rupture aspect ratio of 2.0.

**MFD**: For the 86 sources with truncated GR MFD: $a$-values range from 3.13 to 5.45, $b$-values from 0.93 to 1.16, and $M_{\min}$ from 4.0 to 4.5. For the 54 sources with arbitrary MFD: occurrence rates are specified directly without parametric $a$/$b$ values. Maximum magnitudes for all multi-point sources range from 5.25 to 9.00 Mw (base values).

### Notable Fault Sources

Two fault sources are associated with documented historic earthquakes of $M$ ≥ 6.5:

- **FL_42** — Murdjadjo Thrust (ASC), $M_{\max}$ = 6.95
- **FL_45** — El Asnam Fault (ASC), $M_{\max}$ = 6.35

The ten highest-$M_{\max}$ faults in the model are:

| Fault ID | Name | TRT | $M_{\max}$ |
|----------|------|-----|-----------|
| FL_119 | Arzew Fault | ASC | 7.75 |
| FL_115 | (unnamed) | ASC | 7.65 |
| FL_127 | (unnamed) | ASC | 7.55 |
| FL_130 | (unnamed) | ASC | 7.55 |
| FL_36 | Oran Anticline | ASC | 7.55 |
| FL_123 | Khayr al Din Fault | ASC | 7.45 |
| FL_58 | Orbata Thrust | SCC | 7.45 |
| FL_61 | Chotts Thrust | SCC | 7.45 |
| FL_87 | Western Fault | SCC | 7.45 |
| FL_89 | Eastern Fault Zone | SCC | 7.45 |

## Earthquake Recurrence Parameters

The earthquake recurrence parameters quantify the expected rate and size distribution
of future earthquakes on each seismic source. Recurrence is described by a
magnitude-frequency distribution (MFD) whose type and parameters are specified per
source in the model.

| Source group | MFD type | $a$-value range | $b$-value range | $M_{\max}$ range (Mw) | $n$ |
|-------------|----------|----------------|----------------|----------------------|-----|
| Fault sources | incrementalMFD | — | — | 6.05–7.75 | 115 |
| MPS / SC (truncated GR) | truncGutenbergRichterMFD | 3.13–5.45 | 0.93–1.16 | 5.25–9.00 | 86 |
| BG (arbitrary MFD) | arbitraryMFD | — | — | 5.25–9.00 | 54 |

For fault sources, earthquake rates are encoded as discrete incremental rates per 0.1-Mw bin. No parametric $a$/$b$ values are defined; recurrence is directly specified from the model without an underlying Gutenberg–Richter fit.

For the 86 multi-point sources with truncated GR MFD, epistemic uncertainty in $b$-value is captured through logic-tree branch sets 3 and 4, applying relative perturbations of ±0.05 to the WAF (MPS) and NAF (SC) source groups respectively.

For the 54 background sources with arbitrary MFD, occurrence rates are specified at arbitrary magnitude points, providing a non-parametric representation of seismicity that does not assume a GR relationship.

[FIGURE: Magnitude-frequency distribution plots for the principal source groups,
showing the range of modelled rates across logic-tree branches where applicable.]

## Maximum Magnitude

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency
distribution for each source and is a critical parameter controlling the tail of the
hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree
branches where specified.

**Fault sources**: $M_{\max}$ ranges from 6.05 to 7.75 Mw (base values). For these sources, $M_{\max}$ is implicit from the highest magnitude bin in the incremental MFD; the low and high bounds are equal to the base value, indicating no additional epistemic uncertainty in $M_{\max}$ beyond what is encoded in the logic-tree source-model selection (branch set 1). The derivation method is `incrementalMFD`.

**Multi-point sources**: $M_{\max}$ base values range from 5.25 to 9.00 Mw. Epistemic uncertainty is applied through `maxMagGRRelative` logic-tree branches:

- For WAF sources (MPS-1 through MPS-6): perturbations of +0.2, 0.0, and −0.2 with weights 0.25, 0.50, 0.25, yielding low values of 5.05–8.80 and high values of 5.45–9.20 Mw.
- For NAF sources (SC_1 through SC_54): identical perturbation structure (±0.2, weights 0.25/0.50/0.25).

## Depth Model

Seismogenic depth parameters define the vertical extent within which earthquake
ruptures are generated. Upper and lower seismogenic depths bound the rupture zone;
hypocentral depth distributions, where specified, control the depth placement of
point-source ruptures.

| Source type | $z_{\text{upper}}$ (km) | $z_{\text{lower}}$ (km) |
|------------|------------------------|------------------------|
| Simple fault sources | 0.0 | 1.7–25.0 |
| Multi-point sources | 0.0 | 40.0–45.0 |

Fault sources exhibit a wide range of lower seismogenic depths, from very shallow structures (1.7 km) to crustal-scale faults extending to 25.0 km depth. Multi-point sources are assigned a deeper lower seismogenic depth of 40–45 km, reflecting the broader depth distribution of smoothed background seismicity.

## Source Evidence and Provenance

The provenance of source parameters and model components is documented from metadata
embedded in the source-model files and from external databases referenced during
model construction.

### Model Provenance

All 255 sources are attributed to the North Africa Probabilistic Seismic Hazard Model (NAF), as documented in Poggi et al. [-@Poggi2020]. The model was developed under the GEM Foundation's Global Seismic Hazard Map programme.

### Fault Database

Fault source geometries and parameters are derived from the GEM North Africa Active Fault Database (NAAFD) compiled by Styron and Poggi [-@Styron2018]. The database provides fault traces, kinematics, and where available, slip-rate estimates for active faults across North Africa.

### Fault Kinematics

Kinematics data from the NAAFD are available for 60 of the 115 fault sources. The documented faulting styles include reverse, normal, sinistral, dextral, and oblique combinations (e.g., Reverse-Sinistral, Dextral-Reverse, Normal-Sinistral). Key references include Sebrier et al. (2006), Arboleya et al. (2004), Pastor et al. (2015), and Rigby (2008), as cited in the NAAFD.

### Slip-Rate Evidence

Slip-rate estimates from the evidence database are available for 15 fault sources. These include net slip rates, strike-parallel rates, vertical rates, and shortening rates, with values typically in the range 0.01–2.5 mm/yr. Note that these slip rates are documented in the external evidence database but are not encoded in the OpenQuake source-model XML files (`sources_with_slip_rate = 0` in the model audit).

### Historic Event Associations

Five fault sources have documented associations with historic earthquakes:

- **FL_42** — Murdjadjo Thrust: associated with a documented historic event.
- **FL_45** — El Asnam Fault: associated with a documented historic event.
- **FL_123** — Khayr al Din Fault: associated with the 1716 Algiers earthquake and tsunami [@Babonneau2020].
- **FL_136** — Kalabsha Fault: associated with the 1981 Aswan earthquake ($M_w$ 5.8) [@Ibrahim2021].
- **FL_119** — Arzew Fault: fault parameters documented by Bouhadad and Laouami [-@Bouhadad2002].
