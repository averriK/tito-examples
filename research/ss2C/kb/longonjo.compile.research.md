# Seismic Source Model (SSM)

## SSM overview and source inventory

The seismic source model (SSM) defines the spatial distribution, geometry, and earthquake occurrence rates of all seismogenic sources considered capable of contributing to ground-motion hazard at the Longonjo site (15.2485 E, 12.9080 S). The SSM is the principal input to the probabilistic seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model logic tree (ssmLT) that captures epistemic uncertainty by assigning weights to alternative model configurations. [@Ref001]

The XAF seismic source model comprises 255 seismic sources of two types: 115 simple fault sources (`simpleFaultSource`) and 140 multi-point sources (`multiPointSource`). These sources are classified into two tectonic region types: Active Shallow Crust (ASC, 150 sources) and Stable Continental Crust (SCC, 105 sources). The model is defined through two logic-tree files -- `ssmLT_XAF.xml` (the full logic tree with 5 branch sets) and `ssmLT_XAF_collapsed.xml` (a collapsed variant with a single branch set) -- referencing five source-model XML files. The minimum magnitude ($M_{\min}$) across all sources is 4.0 Mw; multi-point sources range from 4.0 to 4.5 Mw, while fault sources are defined from 6.05 Mw. [@Ref001][@Ref002]

The model domain extends from approximately 19.5 W to 52.9 E in longitude and 28.7 S to 38.5 N in latitude, covering North Africa, West Africa, and parts of sub-Saharan Africa. [@Ref001]

Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with their geometry and parametrisation defined in OpenQuake source-model XML files and encoded in the logic tree. [@Ref001]

All 255 sources are attributed to the North Africa Probabilistic Seismic Hazard Model (NAF), as documented in Poggi et al. [-@Poggi2020]. The model was developed under the GEM Foundation's Global Seismic Hazard Map programme. Fault source geometries and kinematics are derived from the GEM North Africa Active Fault Database (NAAFD) compiled by Styron and Poggi [-@Styron2018]. The model is composed of five source-model XML files: `ssm_XAF/FaultSources.xml` (115 simple fault sources), `ssm_XAF/GridMultiSources_C.xml` (NAF smoothed seismicity for the `naf_smooth` branch), `ssm_XAF/GridMultiSources_C_L50_BG.xml` (NAF smoothed seismicity with background rates for the `naf_faults` branch), `ssm_XAF/WAF_GridMultiSources_Collapsed.xml` (collapsed multi-point sources for West Africa), and `ssm_XAF/SSA_GridMultiSources_Collapsed.xml` (collapsed multi-point sources for sub-Saharan Africa). [@Ref001]

[FIGURE: Map of the seismic source model domain showing all source zones or fault traces, and the site location where applicable.]

## Source-model logic tree structure

The source-model logic tree encodes epistemic uncertainty by defining alternative realisations of the SSM. Each branch set addresses a specific source of uncertainty, and the branches within each set are assigned weights reflecting the relative credibility of each alternative. The primary logic tree (`ssmLT_XAF.xml`) contains five branch sets producing $2 \times 3 \times 3 \times 3 \times 3 = 162$ end-branches. [@Ref001]

Branch set 1 (source-model selection, `sourceModel`, applies to all sources) offers two alternatives: `naf_faults` (weight 0.50), which includes FaultSources.xml alongside GridMultiSources_C_L50_BG.xml plus the WAF and SSA collapsed grids; and `naf_smooth` (weight 0.50), which replaces fault sources with a purely smoothed seismicity representation from GridMultiSources_C.xml plus the WAF and SSA collapsed grids. The first branch includes explicit fault sources alongside background smoothed seismicity; the second replaces fault sources with a purely smoothed seismicity representation. [@Ref001]

Branch set 2 ($M_{\max}$ perturbation for WAF sources, `maxMagGRRelative`, applies to MPS-1 through MPS-6) contains three branches: `waf_m_m0.2` (perturbation +0.2, weight 0.25), `waf_m_e0.0` (perturbation 0.0, weight 0.50), and `waf_m_p0.2` (perturbation -0.2, weight 0.25). Branch set 3 ($b$-value perturbation for WAF sources, `bGRRelative`, applies to MPS-1 through MPS-6) contains three branches: `waf_b_m0.05` (perturbation +0.05, weight 0.25), `waf_b_e0.0` (perturbation 0.0, weight 0.50), and `waf_b_p0.05` (perturbation -0.05, weight 0.25). [@Ref001]

Branch set 4 ($b$-value perturbation for NAF sources, `bGRRelative`, applies to SC_1 through SC_54) contains three branches: `naf_b_m0.05` (perturbation +0.05, weight 0.25), `naf_b_e0.0` (perturbation 0.0, weight 0.50), and `naf_b_p0.05` (perturbation -0.05, weight 0.25). Branch set 5 ($M_{\max}$ perturbation for NAF sources, `maxMagGRRelative`, applies to SC_1 through SC_54) contains three branches: `naf_m_m0.2` (perturbation +0.2, weight 0.25), `naf_m_e0.0` (perturbation 0.0, weight 0.50), and `naf_m_p0.2` (perturbation -0.2, weight 0.25). [@Ref001]

A collapsed logic-tree variant (`ssmLT_XAF_collapsed.xml`) retains only branch set 1 (source-model selection, 2 branches). This represents a mean-hazard approximation where epistemic uncertainty in $M_{\max}$ and $b$-value has been pre-collapsed into the source parameters, reducing the computational cost of the PSHA while preserving the mean hazard estimate. [@Ref001]

## Earthquake recurrence parameters

The earthquake recurrence parameters quantify the expected rate and size distribution of future earthquakes on each seismic source. Recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source in the model. The following table summarises the recurrence parameters by source group. [@Ref001]

| Source group | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) | $n$ |
|---|---|---|---|---|---|---|
| Fault sources | incrementalMFD | -- | -- | 6.05 | 6.05-7.75 | 115 |
| MPS / SC (truncated GR) | truncGutenbergRichterMFD | 3.13-5.45 | 0.93-1.16 | 4.0-4.5 | 5.25-9.00 | 86 |
| BG (arbitrary MFD) | arbitraryMFD | -- | -- | -- | 5.25-9.00 | 54 |

For the 115 fault sources, earthquake rates are encoded as discrete incremental rates per 0.1-Mw bin starting at $M_{\min}$ = 6.05 Mw. No parametric $a$/$b$ values are defined; recurrence is directly specified from the model without an underlying Gutenberg-Richter fit. Maximum magnitudes for fault sources range from 6.05 to 7.75 Mw. [@Ref001]

For the 86 multi-point sources with truncated Gutenberg-Richter MFD (comprising 80 SC-type sources and 6 MPS-type sources), $a$-values range from 3.13 to 5.45, $b$-values from 0.93 to 1.16, and $M_{\min}$ from 4.0 to 4.5 Mw. Epistemic uncertainty in $b$-value is captured through logic-tree branch sets 3 and 4, applying relative perturbations of $\pm$0.05 to the WAF (MPS-1 through MPS-6) and NAF (SC_1 through SC_54) source groups respectively. [@Ref001]

For the 54 background sources (BG_1 through BG_54) with arbitrary MFD, occurrence rates are specified at arbitrary magnitude points, providing a non-parametric representation of seismicity that does not assume a Gutenberg-Richter relationship. These sources have $M_{\max}$ base values ranging from 5.25 to 9.00 Mw. [@Ref001]

## MFD types and scaling relationships

Three magnitude-frequency distribution (MFD) types are present in the model. [@Ref001]

The truncated Gutenberg-Richter MFD (`multiMFD:truncGutenbergRichterMFD`) is used by 86 multi-point sources, predominantly the SC_1 through SC_54 sources and MPS-1 through MPS-6 sources in the NAF and WAF smoothed seismicity components. Earthquake rates are parameterised by an $a$-value and $b$-value with explicit $M_{\min}$ and $M_{\max}$ bounds. The $a$-value defines the overall rate of seismicity (log of the annual number of earthquakes at or above $M_{\min}$), while the $b$-value describes the relative proportion of small to large earthquakes. [@Ref001]

The incremental MFD (`incrementalMFD`) is used by all 115 fault sources. Occurrence rates are specified as discrete values per magnitude bin with a bin width of 0.1 Mw; $a$- and $b$-values are not defined. This formulation directly encodes the expected rate at each magnitude level without imposing a parametric Gutenberg-Richter relationship. [@Ref001]

The arbitrary MFD (`multiMFD:arbitraryMFD`) is used by 54 multi-point sources (the BG_1 through BG_54 background sources). Occurrence rates are specified at arbitrary magnitude points without an underlying parametric model, providing a flexible non-parametric representation of seismicity. [@Ref001]

Two magnitude-area scaling relationships are applied in the model. The `Leonard2014_Interplate` relationship [@Leonard2014] is used for all 115 fault sources with a rupture aspect ratio of 2.0. This scaling relation, developed by Leonard (2014), provides self-consistent relationships between seismic moment, rupture area, length, width, and average displacement for interplate fault environments. The `WC1994` relationship [@Wells1994] is used for all 140 multi-point sources with a rupture aspect ratio of 2.0. This relationship, developed by Wells and Coppersmith (1994), provides empirical regressions between moment magnitude and rupture dimensions based on a global database of source parameters. [@Ref001][@Ref003][@Ref004]

## Slip-rate activity rates and moment balance

Activity rates for fault sources with available slip-rate data are derived from seismic-moment balance. The relationship between moment rate and fault parameters is given by:

$$\dot{M}_0 = \mu\, A\, S$$

where $\mu$ is the shear modulus, $A$ the fault area, and $S$ the long-term slip rate.

Slip-rate estimates from the evidence database are available for 15 of the 115 fault sources in the model. These include net slip rates, strike-parallel rates, vertical rates, and shortening rates, with values typically in the range 0.01-2.5 mm/yr. The slip-rate evidence is documented in the external evidence database (the GEM North Africa Active Fault Database compiled by Styron and Poggi [-@Styron2018]) but is not encoded in the OpenQuake source-model XML files; the model audit reports zero sources with slip rate encoded in the XML parametrisation (`sources_with_slip_rate = 0`). [@Ref001]

Kinematics data from the NAAFD are available for 60 of the 115 fault sources. The documented faulting styles include reverse, normal, sinistral, dextral, and oblique combinations. The dominant faulting styles among all 115 faults are reverse (rake = 90, 52 sources) and normal (rake = -90, 29 sources), with strike-slip and oblique mechanisms accounting for the remaining 34 sources. [@Ref001]

Because the slip-rate data are not parameterised in the source-model XML files, the moment-balance approach described above is not explicitly implemented in the current OpenQuake model. Activity rates for the fault sources are instead specified directly through the incremental MFD, which encodes discrete occurrence rates per magnitude bin without requiring an explicit slip-rate-to-rate conversion. [@Ref001]

[FIGURE: Magnitude-frequency distribution plots for the principal source groups, showing the range of modelled rates across logic-tree branches where applicable.]

## Maximum magnitude characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency distribution for each source and controls the tail of the hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree branches where specified. [@Ref001]

For the 115 fault sources, $M_{\max}$ ranges from 6.05 to 7.75 Mw (base values). For these sources, $M_{\max}$ is implicit from the highest magnitude bin in the incremental MFD; the low and high bounds are equal to the base value, indicating no additional epistemic uncertainty in $M_{\max}$ beyond what is encoded in the logic-tree source-model selection (branch set 1). The derivation method is the `incrementalMFD` itself. The ten highest-$M_{\max}$ faults in the model are FL_119 (Arzew Fault, ASC, $M_{\max}$ = 7.75), FL_115 (unnamed, ASC, 7.65), FL_127 and FL_130 (unnamed, ASC, 7.55 each), FL_36 (Oran Anticline, ASC, 7.55), FL_123 (Khayr al Din Fault, ASC, 7.45), FL_58 (Orbata Thrust, SCC, 7.45), FL_61 (Chotts Thrust, SCC, 7.45), FL_87 (Western Fault, SCC, 7.45), and FL_89 (Eastern Fault Zone, SCC, 7.45). [@Ref001]

For the multi-point sources, $M_{\max}$ base values range from 5.25 to 9.00 Mw. Epistemic uncertainty is applied through `maxMagGRRelative` logic-tree branches. For the WAF sources (MPS-1 through MPS-6), branch set 2 applies perturbations of +0.2, 0.0, and -0.2 Mw with weights 0.25, 0.50, and 0.25, yielding low values of 5.05-8.80 Mw and high values of 5.45-9.20 Mw across the WAF group. For the NAF sources (SC_1 through SC_54), branch set 5 applies an identical perturbation structure ($\pm$0.2, weights 0.25/0.50/0.25). [@Ref001]

For the 54 background sources (BG_1 through BG_54) with arbitrary MFD, $M_{\max}$ is implicit from the highest magnitude point in the rate specification and is not subject to separate logic-tree perturbation. The BG source $M_{\max}$ values range from 5.25 to 9.00 Mw. [@Ref001]

## SLOT 7: Seismogenic depth parameters

Seismogenic depth parameters define the vertical extent within which earthquake ruptures are generated. Upper and lower seismogenic depths bound the rupture zone; hypocentral depth distributions, where specified, control the depth placement of point-source ruptures. [@Ref001]

For the 115 simple fault sources, the upper seismogenic depth is 0.0 km for all faults. The lower seismogenic depth ranges from 1.7 km to 25.0 km, reflecting a wide range of fault geometries from very shallow structures to crustal-scale faults. No hypocentral depth distribution is defined for fault sources, as ruptures are distributed over the fault plane geometry. [@Ref001]

For the 140 multi-point sources, the upper seismogenic depth is 0.0 km for all sources. The lower seismogenic depth ranges from 40.0 to 45.0 km, reflecting the broader depth distribution of smoothed background seismicity. The WAF collapsed sources (MPS-1 through MPS-6) have a lower seismogenic depth of 45.0 km and a mean hypocentral depth of 18.3 km, with a hypocentral depth distribution defined at four depth levels: 5 km (probability 0.267), 15 km (probability 0.267), 25 km (probability 0.333), and 35 km (probability 0.133). The SSA collapsed sources have a lower seismogenic depth of 40.0 km and mean hypocentral depths ranging from approximately 18.0 to 19.5 km. [@Ref001][@Ref005][@Ref002]

## Local sources near the site

The Longonjo site (15.2485 E, 12.9080 S) is located in central-western Angola within the Stable Continental Crust (SCC) tectonic regime. A total of 255 seismic sources were evaluated for the site. The nearest source (MPS-2) lies 2.5 km from the site; only 2 sources are within 500 km and 6 within 1,000 km. The remaining sources are at distances exceeding 1,000 km and include the East African Rift system (ASC) and the North Africa seismicity zones. [@Ref005][@Ref002]

The two sources within 300 km -- MPS-2 (2.5 km) and MPS-1 (271.5 km) -- both belong to the Central Africa (WAF) smoothed-seismicity group and are classified under the Stable Continental Crust (SCC) tectonic region type. MPS-2 is the geometrically dominant source and is expected to control the hazard across all return periods within the SCC tectonic regime. It has a base $M_{\max}$ of 6.76 Mw (range 6.56-6.96 Mw under logic-tree perturbation), a truncated Gutenberg-Richter MFD with $a$ = 3.850 and $b$ = 1.048 (range 0.998-1.098), and a seismogenic depth range of 0.0-45.0 km with a mean hypocentral depth of 18.3 km. [@Ref005][@Ref002]

The next-nearest sources beyond 300 km are associated with the sub-Saharan Africa (SSA) collapsed grids: MPS-1200 (Mweru-Katanga-Upemba, SCC, $M_{\max}$ = 6.90, 593 km), MPS-1100 (Luama Rift, SCC, $M_{\max}$ = 6.90, 875 km), MPS-1201 (Mweru-Katanga-Upemba 2L, SCC, $M_{\max}$ = 6.90, 920 km), and MPS-1300 (Kariba-Okavango, SCC, $M_{\max}$ = 6.90, 922 km). All of these are SCC multi-point sources with truncated Gutenberg-Richter MFDs and lower seismogenic depths of 40.0 km. The first ASC-regime source is MPS-800 (Western Rift-Tanganyika, $M_{\max}$ = 7.90) at 1,673 km. [@Ref005][@Ref002]

The tectonic regime surrounding the Longonjo site is entirely Stable Continental Crust, with all sources within approximately 1,400 km classified as SCC. Based on the nearest local sources, the most relevant earthquake scenarios in the immediate vicinity of the site correspond to moderate-magnitude events ($M_{\max}$ up to approximately 6.96 Mw for MPS-2) at hypocentral depths of 5-35 km, occurring within a stable continental intraplate setting. The nearest Active Shallow Crust sources associated with the East African Rift system lie beyond 1,670 km and, despite their higher magnitude potential ($M_{\max}$ up to 7.90 Mw), are unlikely to contribute significantly to the ground-motion hazard at the site due to the large source-to-site distances. [@Ref005][@Ref002]

## Smoothed-seismicity nearest point sources

The source model includes spatially smoothed seismicity grids as components of both source-model branches. The WAF and SSA collapsed multi-point source grids are present in both the `naf_faults` and `naf_smooth` branches (each with weight 0.50), while the NAF-specific smoothed seismicity grids differ between branches: GridMultiSources_C.xml (SC sources) in the `naf_smooth` branch and GridMultiSources_C_L50_BG.xml (BG background sources) in the `naf_faults` branch. For the Longonjo site, the NAF-specific sources are all located beyond 4,400 km and do not contribute to the local hazard. [@Ref001][@Ref005]

The nearest smoothed-seismicity point source to the Longonjo site is MPS-2, from the WAF collapsed grid (`ssm_XAF/WAF_GridMultiSources_Collapsed.xml`). MPS-2 is present in both source-model branches with a combined weight of 1.0 (`naf_faults` weight 0.50, `naf_smooth` weight 0.50). Its nearest grid node to the site is located at 15.226 E, 12.912 S, at a distance of 2.5 km. The MFD is truncated Gutenberg-Richter with $a$ = 3.850, $b$ = 1.048 (range 0.998-1.098 under `bGRRelative` perturbation), and $M_{\max}$ = 6.76 Mw (range 6.56-6.96 Mw under `maxMagGRRelative` perturbation of $\pm$0.20 Mw). The seismogenic depth range is 0.0-45.0 km with a hypocentral depth distribution at 5 km (0.267), 15 km (0.267), 25 km (0.333), and 35 km (0.133), yielding a mean hypocentral depth of 18.3 km. [@Ref005][@Ref002]

The second-nearest smoothed-seismicity point source is MPS-1, also from the WAF collapsed grid, at a distance of 271.5 km. MPS-1 is likewise present in both source-model branches (combined weight 1.0). Its MFD parameters are $a$ = 4.047, $b$ = 1.048 (range 0.998-1.098), and $M_{\max}$ = 5.76 Mw (range 5.56-5.96 Mw). The depth parameters are identical to MPS-2 (0.0-45.0 km, mean hypocentral depth 18.3 km). Given the substantially lower $M_{\max}$ compared to MPS-2 and the 272 km separation from the site, MPS-1 is unlikely to contribute significantly to the hazard. [@Ref005][@Ref002]

The third-nearest smoothed-seismicity source is MPS-1200 (Mweru-Katanga-Upemba), from the SSA collapsed grid (`ssm_XAF/SSA_GridMultiSources_Collapsed.xml`), at a distance of 592.9 km. This SCC source has a truncated Gutenberg-Richter MFD with $a$ = 4.045, $b$ = 0.991, and $M_{\max}$ = 6.90 Mw (no additional epistemic perturbation, as SSA sources are pre-collapsed). The seismogenic depth range is 0.0-40.0 km with a mean hypocentral depth of approximately 18.0 km. MPS-1200 is present in both source-model branches with combined weight 1.0. [@Ref002]
