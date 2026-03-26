# Seismic Source Model (SSM) {#sec-SSM}

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

The IND seismic source model comprises 443,197 seismic sources of two types: 108 area sources (`areaSource`) and 443,089 point sources (`pointSource`). These sources are classified into four tectonic region types: Subduction Intraslab (SIS, 139,977 sources), Subduction Interface (SIF, 123,775 sources), Stable Continental Crust (SCC, 94,450 sources), and Active Shallow Crust (ASC, 84,995 sources). The model is defined through three logic-tree files — `ssmLT_IND.xml` (the full logic tree with 3 branch sets), `ssmLT_IND_collapsed.xml` (collapsed variant), and `ssmLT_IND_garage_v1.xml` (full variant) — referencing three source-model XML files. Source types `griddedSeismicitySource` and `pointSource` were excluded from the detailed source-by-source analysis; point sources are represented by two smoothed-seismicity models described at the model level below. The minimum magnitude ($M_{\min}$) across all area sources is 4.5 Mw.

The model domain extends from approximately 60.0°E to 100.8°E in longitude and 2.0°N to 40.0°N in latitude, covering India, Bangladesh, Bhutan, Nepal, Pakistan, Myanmar, and surrounding regions.

[FIGURE: Map of the seismic source model domain showing all source zones or fault traces,
and the site location where applicable.]

### Adopted Source Model

The adopted SSM is based on the seismic hazard model for the Indian subcontinent developed by Nath and Thingbaijam [-@Nath2012], updated and translated into OpenQuake in collaboration with Natural Resources Canada, as documented in the GEM model report [-@GEM_IND]. The model version described is v2012.2.0.

The SSM comprises three source-model components:

- **`ssm_IND/nt2012_areal_source_model_v1.xml`** — 108 areal seismogenic source zones defining the regional source zonation. This is the primary characterised component of the model. An author overlay CSV file (`nt2012_areal_source_model_v1.csv`) provides complementary parameters including focal mechanism analysis, tectonic subregion classification, and faulting style for each zone.
- **`ssm_IND/nt2012_smoothed_source_model_v1_mmin4.5.xml`** — Smoothed-gridded point-source model with $M_{\min}$ = 4.5 (443,089 point sources). NRML XML generated from smaller CSV/TSV inputs using scripts dependent on the OpenQuake Hazard Model Toolkit (HMTK) [-@nackerley_repo].
- **`ssm_IND/nt2012_smoothed_source_model_v1_mmin5.5.xml`** — Smoothed-gridded point-source model with $M_{\min}$ = 5.5 (identical grid, higher minimum magnitude threshold).

The implementation repository is publicly available at `nackerley/indian-subcontinent-psha` on GitHub [-@nackerley_repo].

## Source Model Methodology

Seismic-source characterisation follows the classical PSHA framework outlined by
Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources
are delineated from geologic, geophysical, and seismological evidence, with their
geometry and parametrisation defined in OpenQuake source-model XML files and encoded
in the logic tree.

All 108 area sources in the detailed model use a single MFD type:

- **Truncated Gutenberg–Richter** (`truncGutenbergRichterMFD`) — Earthquake rates are parameterised by an $a$-value (range: 1.58–7.33) and $b$-value (range: 0.63–1.57) with $M_{\min}$ = 4.5 Mw (for most shallow sources) to 7.5 Mw (for deep subduction intraslab zones) and explicit $M_{\max}$ bounds.

The smoothed point-source models inherit the same GR parametrisation from the parent areal zones, distributed over a regular grid.

Three magnitude-area scaling relationships are applied across different tectonic environments:

- `WC1994` [@Wells1994] — Used by 46 area sources, predominantly in Active Shallow Crust and Stable Continental Crust settings.
- `StrasserIntraslab` [@Strasser2010] — Used by 35 area sources in subduction intraslab settings.
- `StrasserInterface` [@Strasser2010] — Used by 27 area sources in subduction interface settings.

Unless the logic tree includes a time-dependent (renewal) branch, temporal occurrence
is modelled as a stationary Poisson process — the canonical assumption in standard PSHA.

## Logic Tree Structure

The source-model logic tree encodes epistemic uncertainty by defining alternative
realisations of the SSM. Each branch set addresses a specific source of uncertainty
(e.g., alternative source-model geometries, maximum-magnitude perturbations, or
b-value perturbations), and the branches within each set are assigned weights reflecting
the relative credibility of each alternative.

### Primary logic tree (`ssmLT_IND.xml`)

The primary logic tree contains three branch sets producing 3 × 3 × 3 = **27 end-branches**:

**Branch set 1 — Source model selection** (`sourceModel`, applies to all sources):

| Branch | Model file | Weight |
|--------|-----------|--------|
| `b1m1` | nt2012_areal_source_model_v1.xml | 0.40 |
| `b1m2` | nt2012_smoothed_source_model_v1_mmin4.5.xml | 0.27 |
| `b1m3` | nt2012_smoothed_source_model_v1_mmin5.5.xml | 0.33 |

The first branch uses the 108 areal seismogenic source zones; the second and third branches use smoothed-gridded point-source models with different minimum magnitude thresholds (4.5 and 5.5 Mw respectively).

**Branch set 2 — $M_{\max}$ perturbation** (`maxMagGRRelative`, applies to all sources):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `b2m1` | −0.3 | 0.32 |
| `b2m2` | 0.0 | 0.36 |
| `b2m3` | +0.3 | 0.32 |

**Branch set 3 — $b$-value perturbation** (`bGRRelative`, applies to all sources):

| Branch | Perturbation | Weight |
|--------|-------------|--------|
| `b3m1` | −0.1 | 0.32 |
| `b3m2` | 0.0 | 0.36 |
| `b3m3` | +0.1 | 0.32 |


## Seismic Sources

### Area Sources

The model includes 108 area sources from `ssm_IND/nt2012_areal_source_model_v1.xml`, representing seismogenic source zones across the Indian subcontinent and surrounding regions. These sources span four tectonic region types:

| Tectonic region | Code | Sources | Depth range |
|----------------|------|---------|-------------|
| Subduction Intraslab | SIS | 35 | 25–300 km |
| Active Shallow Crust | ASC | 29 | 0–25 km |
| Subduction Interface | SIF | 27 | 0–180 km |
| Stable Continental Crust | SCC | 17 | 0–70 km |

**Geometry**: All area sources are defined as polygons (`geom_kind = polygon`) with 4 to 18 vertices per zone. The source zones cover the full model domain from approximately 60°E to 101°E in longitude and 2°N to 40°N in latitude.

**Depth**: Upper seismogenic depths range from 0.0 km (shallow crustal sources) to 180.0 km (deep subduction intraslab zones). Lower seismogenic depths range from 25.0 km (shallow zones) to 300.0 km (deep subduction intraslab). Three depth layers are represented: shallow (0–25 km), intermediate (25–70 km), and deep (70–300 km).

**Focal mechanism**: Nodal plane distributions are defined for all 108 area sources (one nodal plane per zone with probability 1.0), based on the author overlay analysis. The author overlay classifies zones by faulting style: reverse, normal, strike-slip, and oblique combinations. A complementary focal plane is also documented in the overlay for each zone.

**Magnitude scaling**: Three relationships are used by tectonic environment:
- `WC1994` [@Wells1994]: 46 sources (ASC, SCC)
- `StrasserIntraslab` [@Strasser2010]: 35 sources (SIS)
- `StrasserInterface` [@Strasser2010]: 27 sources (SIF)

All sources use a rupture aspect ratio of 2.0.

**MFD**: All 108 area sources use truncated Gutenberg–Richter MFD with $a$-values from 1.58 to 7.33 and $b$-values from 0.63 to 1.57. Maximum magnitudes range from 6.0 to 9.4 Mw (base values).

### Point Sources (Smoothed Seismicity)

The model includes 443,089 point sources distributed across two smoothed-gridded source-model files. These sources inherit their parametrisation from the areal zone model and are distributed over a regular spatial grid covering the same domain. The two variants differ only in their minimum magnitude threshold:

- `nt2012_smoothed_source_model_v1_mmin4.5.xml` — $M_{\min}$ = 4.5 Mw (branch weight 0.27)
- `nt2012_smoothed_source_model_v1_mmin5.5.xml` — $M_{\min}$ = 5.5 Mw (branch weight 0.33)

These models were generated from smaller CSV/TSV inputs using scripts dependent on the OpenQuake Hazard Model Toolkit (HMTK). The smoothed-gridded source model files are too large for version control and can be regenerated from the input data using the provided scripts [-@nackerley_repo].

## Earthquake Recurrence Parameters

The earthquake recurrence parameters quantify the expected rate and size distribution
of future earthquakes on each seismic source. Recurrence is described by a
magnitude-frequency distribution (MFD) whose type and parameters are specified per
source in the model.

All 108 area sources use truncated Gutenberg–Richter MFD:

| Tectonic region | $a$-value range | $b$-value range | $M_{\max}$ range (Mw) | $n$ |
|----------------|----------------|----------------|----------------------|-----|
| ASC | 2.73–7.08 | 0.72–1.37 | 7.0–8.8 | 29 |
| SCC | 1.58–4.84 | 0.63–1.19 | 6.0–8.2 | 17 |
| SIF | 3.12–5.40 | 0.72–1.24 | 6.5–9.4 | 27 |
| SIS | 3.22–7.33 | 0.80–1.57 | 6.5–8.6 | 35 |

Epistemic uncertainty in $b$-value is captured through logic-tree branch set 3, applying relative perturbations of ±0.1 to all sources simultaneously (weights 0.32/0.36/0.32).

[FIGURE: Magnitude-frequency distribution plots for the principal source groups,
showing the range of modelled rates across logic-tree branches where applicable.]

## Maximum Magnitude

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency
distribution for each source and is a critical parameter controlling the tail of the
hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree
branches where specified.

**Area sources**: $M_{\max}$ base values range from 6.0 to 9.4 Mw across all 108 zones. Epistemic uncertainty is applied through `maxMagGRRelative` logic-tree branch set 2, with perturbations of −0.3, 0.0, and +0.3 (weights 0.32, 0.36, 0.32) applied to all sources simultaneously. This yields:

- Low $M_{\max}$: 5.7–9.1 Mw
- Central $M_{\max}$: 6.0–9.4 Mw
- High $M_{\max}$: 6.3–9.7 Mw

The highest $M_{\max}$ zones correspond to subduction interface settings (e.g., Sumatra, Himalayas – Main Frontal Thrust) where great earthquakes ($M$ > 8.5) are considered possible. The derivation method for all sources is `truncGutenbergRichterMFD`.

## Depth Model

Seismogenic depth parameters define the vertical extent within which earthquake
ruptures are generated. Upper and lower seismogenic depths bound the rupture zone;
hypocentral depth distributions, where specified, control the depth placement of
point-source ruptures.

| Tectonic region | $z_{\text{upper}}$ (km) | $z_{\text{lower}}$ (km) | Mean hypocentral depth (km) |
|----------------|------------------------|------------------------|---------------------------|
| ASC | 0 | 25 | 15 |
| SCC | 0–25 | 25–70 | 15–25 |
| SIF | 0–70 | 25–180 | 15–70 |
| SIS | 25–180 | 70–300 | 25–180 |

The depth model reflects a multi-layer structure: shallow crustal sources (ASC and upper SCC) are confined to the top 25 km; intermediate-depth zones (lower SCC, upper SIF/SIS) extend to 70 km; and deep subduction intraslab zones reach 300 km depth. Hypocentral depths are specified as single-value distributions with probability 1.0 for all area sources.

## Source Evidence and Provenance

The provenance of source parameters and model components is documented from metadata
embedded in the source-model files and from external databases referenced during
model construction.

### Model Provenance

The source model is based on the study by Nath and Thingbaijam [-@Nath2012], which proposed one areal zones model plus two smoothed-gridded point-source models for the Indian subcontinent. The model was updated and translated into OpenQuake format in collaboration with Natural Resources Canada, as documented in the GEM model report (version v2012.2.0) [-@GEM_IND]. The implementation is available at the `nackerley/indian-subcontinent-psha` GitHub repository [-@nackerley_repo].

### Tectonic Context

The Indian subcontinent moves northward relative to Eurasia at a rate of 35–45 mm/yr [-@GEM_IND], colliding with the southern Asian margin. This plate convergence drives uplift of the Himalaya, Tien Shan, Pamir, and Tibetan plateau, and generates the dominant seismic hazard sources in the region.


### Historic Event Associations

Notable historic earthquakes within the model domain include [-@GEM_IND]:

- 1950 Assam–Tibet earthquake ($M$ 8.6)
- 2004 Sumatra–Andaman earthquake ($M$ 9.1)
- 2015 Gorkha, Nepal earthquake ($M_w$ 7.8)
- 2001 Bhuj, India earthquake ($M$ 7.7)

### Validation

The implementation repository includes a South Asian earthquake catalogue (Nath, Thingbaijam & Ghosh, 2010) used for model validation [-@nackerley_repo].
