# Site-Specific Seismic Sources

## Site Identification

This section identifies the seismic sources most relevant to the project site
based on source-to-site distance analysis. The regional seismic source model —
including its methodology, logic-tree structure, recurrence parameters, depth model,
and provenance — is described in the companion Chapter 2 (Regional Seismic Source
Model). This supplement reports only the site-specific source characterisation.

**Site**: Rampura Agucha
**Coordinates**: 74.7413°E, 25.8474°N
**Region**: IND

The site lies within two overlapping areal seismogenic zones — z919 (0–25 km
depth) and z932 (25–70 km depth) — both in the Stable Continental Crust (SCC)
tectonic regime of Peninsular India. These zones are present in the areal source
model branch (weight 0.40). Two alternative smoothed-seismicity grids provide
the remaining source representation (combined weight 0.60); their nearest point
sources are at 104.6 km and 114.1 km from the site.

No fault sources are included in the IND source model. The full areal zonation
(108 zones spanning four TRTs) and the smoothed-seismicity grids (443,089 point
sources) are described in section [@sec-SSM]

[FIGURE: Map showing areal zones z919 and z932 polygon outlines on a tectonic
background, the Rampura Agucha site location, and the nearest smoothed-grid point
source locations. Label zone IDs, Mmax, and branch weights.]

## Site-Controlling Sources

The site-controlling sources are those expected to dominate the seismic hazard
at the site based on proximity, magnitude potential, and recurrence rate.
Definitive identification of controlling sources requires deaggregation of
the PSHA results; the sources listed here are geometric candidates identified
from source-to-site distance analysis.

The Rampura Agucha site is contained within two overlapping SCC areal zones,
both present exclusively in the areal source model branch (weight 0.40). Zone
z919 represents the shallow crustal seismogenic layer and carries the higher
Mmax (7.20 Mw nominal); zone z932 represents the intermediate layer with a
lower Mmax (6.50 Mw) but higher activity rate. The primary areal zone selected
by the site-association algorithm is z919.

###  Zone 919, Peninsular India Layer 1 (shallow SCC)

| Parameter | Value |
|---|---|
| Zone ID | z919 |
| Zone name | zone 919 |
| Source type | areaSource |
| Tectonic region | SCC (Stable Continental Crust) |
| Tectonic sub-region | Stable shallow crust |
| Source model file | `nt2012_areal_source_model_v1.xml` (branch weight 0.40) |
| MFD type | truncated Gutenberg–Richter |
| a-value | 2.73 |
| b-value (base / low / high) | 0.72 / 0.62 / 0.82 |
| Mmin (Mw) | 4.50 |
| Mmax (base / low / high, Mw) | 7.20 / 6.90 / 7.50 |
| Mmax uncertainty | maxMagGRRelative ±0.30 Mw |
| Seismogenic depth (upper / lower, km) | 0.0 / 25.0 |
| Mean hypocentral depth (km) | 15.0 |
| Hypocentral depth distribution | 15.0 km (1.0) |
| Magnitude scaling | WC1994 |
| Rupture aspect ratio | 2.0 |
| Nodal plane (strike / dip / rake) | 290° / 61° / 123° |
| Faulting style | Reverse |
| Zone bounding box (lon/lat) | 67.88–91.65°E, 20.69–31.19°N |
| Zone polygon area (deg²) | 102.5 |

**Epistemic adjustments affecting z919:**

| Branch set | Type | Branches | Weights |
|---|---|---|---|
| per-zone mmax | maxMagGRRelative | Mmax = 6.90, 7.20, 7.50 Mw (Δ−0.30, Δ0.00, Δ+0.30) | 0.32, 0.36, 0.32 |
| per-zone b | bGRRelative | b = 0.62, 0.72, 0.82 (Δ−0.10, Δ0.00, Δ+0.10) | 0.32, 0.36, 0.32 |

###  Zone 932, Peninsular India Layer 2 (intermediate SCC)

| Parameter | Value |
|---|---|
| Zone ID | z932 |
| Zone name | zone 932 |
| Source type | areaSource |
| Tectonic region | SCC (Stable Continental Crust) |
| Tectonic sub-region | Stable shallow crust |
| Source model file | `nt2012_areal_source_model_v1.xml` (branch weight 0.40) |
| MFD type | truncated Gutenberg–Richter |
| a-value | 4.15 |
| b-value (base / low / high) | 0.93 / 0.83 / 1.03 |
| Mmin (Mw) | 4.50 |
| Mmax (base / low / high, Mw) | 6.50 / 6.20 / 6.80 |
| Mmax uncertainty | maxMagGRRelative ±0.30 Mw |
| Seismogenic depth (upper / lower, km) | 25.0 / 70.0 |
| Mean hypocentral depth (km) | 25.0 |
| Hypocentral depth distribution | 25.0 km (1.0) |
| Magnitude scaling | WC1994 |
| Rupture aspect ratio | 2.0 |
| Nodal plane (strike / dip / rake) | 239° / 67° / 8° |
| Faulting style | Sinistral strike-slip |
| Zone bounding box (lon/lat) | 68.09–91.68°E, 20.80–31.00°N |
| Zone polygon area (deg²) | 105.2 |

**Epistemic adjustments affecting z932:**

| Branch set | Type | Branches | Weights |
|---|---|---|---|
| per-zone mmax | maxMagGRRelative | Mmax = 6.20, 6.50, 6.80 Mw (Δ−0.30, Δ0.00, Δ+0.30) | 0.32, 0.36, 0.32 |
| per-zone b | bGRRelative | b = 0.83, 0.93, 1.03 (Δ−0.10, Δ0.00, Δ+0.10) | 0.32, 0.36, 0.32 |


