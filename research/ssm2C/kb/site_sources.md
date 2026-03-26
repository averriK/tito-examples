# Site-Specific Seismic Sources

## Site Identification

This section identifies the seismic sources most relevant to the project site
based on source-to-site distance analysis. The regional seismic source model —
including its methodology, logic-tree structure, recurrence parameters, depth model,
and provenance — is described in the companion Chapter 2 (Regional Seismic Source
Model). This supplement reports only the site-specific source characterisation.

**Site**: Longonjo
**Coordinates**: 15.2485°E, 12.9080°S
**Region**: XAF

A total of 255 seismic sources were evaluated for the site. The nearest source
(MPS-2) lies 2.5 km from the site. Only 2 sources are within 500 km and 6 within
1,000 km; the remaining sources are at distances exceeding 1,000 km and include
the East African Rift system (ASC) and the North Africa seismicity zones.

## Source-to-Site Distance Ranking

The following table ranks the seismic sources by distance to the site. Sources
closer to the site have greater potential to contribute to ground-motion hazard,
subject to their magnitude potential and recurrence rate. This ranking is based
on geometric distance; definitive hazard contributions require deaggregation of
the PSHA results.

| Rank | Source ID | Name | Type | TRT | Distance (km) | Mmax base | MFD type | Model |
|---|---|---|---|---|---|---|---|---|
| 1 | MPS-2 | — | multiPointSource | SCC | 2.5 | 6.76 | truncGR | Central Africa |
| 2 | MPS-1 | — | multiPointSource | SCC | 271.5 | 5.76 | truncGR | Central Africa |
| 3 | MPS-1200 | Mweru–Katanga–Upemba | multiPointSource | SCC | 592.9 | 6.90 | truncGR | SSHARA |
| 4 | MPS-1100 | Luama Rift | multiPointSource | SCC | 874.8 | 6.90 | truncGR | SSHARA |
| 5 | MPS-1201 | Mweru–Katanga–Upemba (2L) | multiPointSource | SCC | 920.3 | 6.90 | truncGR | SSHARA |
| 6 | MPS-1300 | Kariba–Okavango | multiPointSource | SCC | 921.6 | 6.90 | truncGR | SSHARA |
| 7 | MPS-1101 | Luama Rift (2L) | multiPointSource | SCC | 1051.6 | 6.90 | truncGR | SSHARA |
| 8 | MPS-3 | — | multiPointSource | SCC | 1201.8 | 6.50 | truncGR | Central Africa |
| 9 | MPS-1301 | Kariba–Okavango (2L) | multiPointSource | SCC | 1263.8 | 6.90 | truncGR | SSHARA |
| 10 | MPS-1000 | Walikale and Masisi | multiPointSource | SCC | 1340.3 | 6.90 | truncGR | SSHARA |
| 11 | MPS-1001 | Walikale and Masisi (2L) | multiPointSource | SCC | 1670.5 | 6.90 | truncGR | SSHARA |
| 12 | MPS-800 | Western Rift–Tanganyika | multiPointSource | ASC | 1673.4 | 7.90 | truncGR | SSHARA |
| 13 | MPS-600 | Western Rift–Lake Edward, Albert and Kivu | multiPointSource | ASC | 1794.4 | 7.90 | truncGR | SSHARA |
| 14 | MPS-4 | — | multiPointSource | SCC | 1795.8 | 5.43 | truncGR | Central Africa |
| 15 | MPS-900 | Malawi–Nyasa Rift | multiPointSource | ASC | 1826.6 | 7.90 | truncGR | SSHARA |
| 16 | MPS-1800 | South Mozambique | multiPointSource | ASC | 1913.7 | 7.90 | truncGR | SSHARA |
| 17 | MPS-700 | Lake Victoria | multiPointSource | SCC | 1923.9 | 6.90 | truncGR | SSHARA |
| 18 | MPS-2000 | Rowuma Basin | multiPointSource | SCC | 2100.3 | 6.90 | truncGR | SSHARA |
| 19 | MPS-701 | Lake Victoria (2L) | multiPointSource | SCC | 2147.7 | 6.90 | truncGR | SSHARA |
| 20 | MPS-1500 | Eastern Rift | multiPointSource | SCC | 2226.3 | 7.40 | truncGR | SSHARA |

235 additional sources at distances up to 5,967 km are listed in `data/report.json`.
These include 115 simpleFaultSource objects (North Africa fault domain, all beyond
4,000 km) and 108 North Africa smoothed-seismicity zones (beyond 4,400 km). No
fault source or North Africa source is expected to contribute to site hazard at
any practical distance threshold.

[FIGURE: Map centred on the Longonjo site (15.25°E, 12.91°S) showing the 20 nearest
seismic sources with source IDs, distances, and Mmax indicated. Include distance
rings at 300 km, 1,000 km, and 2,000 km.]

## Site-Controlling Sources

The site-controlling sources are those expected to dominate the seismic hazard
at the site based on proximity, magnitude potential, and recurrence rate.
Definitive identification of controlling sources requires deaggregation of
the PSHA results; the sources listed here are geometric candidates identified
from source-to-site distance analysis.

Two sources lie within 300 km of the site: MPS-2 (2.5 km) and MPS-1 (271.5 km),
both in the Central Africa (WAF) smoothed-seismicity group. MPS-2 is the
geometrically dominant source and is expected to control the hazard across all
return periods within the SCC tectonic regime. The next higher-Mmax source
is MPS-1200 (Mweru–Katanga–Upemba, Mmax 6.90) at 593 km; the first ASC-regime
source is MPS-800 (Western Rift–Tanganyika, Mmax 7.90) at 1,673 km.

### MPS-2 — Central Africa (WAF), primary site source

| Parameter | Value |
|---|---|
| Source ID | MPS-2 |
| Source name | — |
| Distance to site (km) | 2.5 |
| Source type | multiPointSource |
| Tectonic region | SCC (Stable Continental Crust) |
| Model | WAF_GridMultiSources_Collapsed (Central Africa — Smoothed Seismicity) |
| XML path | `ssm_XAF/WAF_GridMultiSources_Collapsed.xml` |
| MFD type | truncated Gutenberg–Richter (multiMFD) |
| a-value | 3.850 |
| b-value (base / low / high) | 1.048 / 0.998 / 1.098 |
| Mmax (base / low / high, Mw) | 6.76 / 6.56 / 6.96 |
| Mmax uncertainty | maxMagGRRelative ±0.20 Mw |
| Seismogenic depth (upper / lower, km) | 0.0 / 45.0 |
| Mean hypocentral depth (km) | 18.3 |
| Hypocentral depth distribution | 5 km (0.267), 15 km (0.267), 25 km (0.333), 35 km (0.133) |
| N₀ (annual rate ≥ Mmin) | 7,083 (method: sum of 10^a per grid node) |
| Nearest grid node to site (lon, lat) | 15.226°E, 12.912°S |

**Logic-tree presence:**
MPS-2 is present in both sourceModel branches with combined weight 1.0:

- `naf_faults` (weight 0.50) — includes FaultSources + WAF + SSA
- `naf_smooth` (weight 0.50) — includes NAF smoothed + WAF + SSA

**Epistemic adjustments affecting MPS-2:**

| Branch set | Type | Branches | Weights |
|---|---|---|---|
| `mmax_waf` | maxMagGRRelative | Δ+0.20, Δ0.00, Δ−0.20 Mw | 0.25, 0.50, 0.25 |
| `bval_waf` | bGRRelative | Δ+0.05, Δ0.00, Δ−0.05 | 0.25, 0.50, 0.25 |

These branch sets apply to sources MPS-1 through MPS-6 (all WAF group sources).
The resulting Mmax range for MPS-2 is 6.56–6.96 Mw; the b-value range is
0.998–1.098.

### MPS-1 — Central Africa (WAF), secondary site source

| Parameter | Value |
|---|---|
| Source ID | MPS-1 |
| Source name | — |
| Distance to site (km) | 271.5 |
| Source type | multiPointSource |
| Tectonic region | SCC (Stable Continental Crust) |
| Model | WAF_GridMultiSources_Collapsed (Central Africa — Smoothed Seismicity) |
| XML path | `ssm_XAF/WAF_GridMultiSources_Collapsed.xml` |
| MFD type | truncated Gutenberg–Richter (multiMFD) |
| a-value | 4.047 |
| b-value (base / low / high) | 1.048 / 0.998 / 1.098 |
| Mmax (base / low / high, Mw) | 5.76 / 5.56 / 5.96 |
| Mmax uncertainty | maxMagGRRelative ±0.20 Mw |
| Seismogenic depth (upper / lower, km) | 0.0 / 45.0 |
| Mean hypocentral depth (km) | 18.3 |
| Hypocentral depth distribution | 5 km (0.267), 15 km (0.267), 25 km (0.333), 35 km (0.133) |
| N₀ (annual rate ≥ Mmin) | 11,146 (method: sum of 10^a per grid node) |
| Nearest grid node to site (lon, lat) | 15.837°E, 15.294°S |

**Logic-tree presence:**
Same as MPS-2 — present in both sourceModel branches (combined weight 1.0).

**Epistemic adjustments:**
Same branch sets as MPS-2 (`mmax_waf` and `bval_waf`). The resulting Mmax range
for MPS-1 is 5.56–5.96 Mw. Given the substantially lower Mmax compared to MPS-2
and the 272 km separation from the site, MPS-1 is unlikely to contribute
significantly to the hazard.
