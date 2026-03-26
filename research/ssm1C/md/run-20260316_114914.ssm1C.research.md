# Seismic Source Model: Structure, Parameterisation, and Site Interrogation

## SLOT 1: SSM Overview and Source Census

The seismic source model (SSM) defines the spatial distribution, geometry, and earthquake occurrence rates of all seismogenic sources considered capable of contributing to ground-motion hazard at the site. It is the principal input to the probabilistic seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model logic tree (ssmLT) that captures epistemic uncertainty by assigning weights to alternative model configurations. [KB:source_model.md]^[Confidence: HIGH, Rationale: This introductory description is reproduced directly from source_model.md and accurately characterises the SSM role. No contradictions detected across KB documents.]

The IND model is based on the seismic hazard study for the Indian subcontinent by Nath and Thingbaijam [-@Nath2012], updated and translated into OpenQuake in collaboration with Natural Resources Canada and documented in the GEM model report [-@GEM_IND] (version v2012.2.0). Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with geometry and parametrisation defined in OpenQuake source-model XML files and encoded in the logic tree. [KB:source_model.md][KB:ind-report.pdf.md]^[Confidence: HIGH, Rationale: Provenance and methodological attribution are consistently stated in source_model.md and confirmed by ind-report.pdf.md. The citekeys [-@Nath2012], [-@GEM_IND], [-@Cornell1968], and [-@SSHAC1997] are preserved as they appear in the KB.]

Two source types are represented in the model: area sources (`areaSource`) defining 108 seismogenic zone polygons across the regional tectonic structure, and point sources (`pointSource`) constituting 443,089 gridded nodes from two smoothed-seismicity grids. The combined total is 443,197 seismic sources. [KB:source_model.md]^[Confidence: HIGH, Rationale: Source type counts are explicitly stated in source_model.md (108 area + 443,089 point = 443,197 total). Arithmetic is internally consistent.]

These sources span four tectonic region types (TRTs). The table below provides the complete census by TRT and source type, derived from the totals reported per TRT and the area-source counts tabulated by tectonic environment. [KB:source_model.md]^[Confidence: HIGH, Rationale: TRT totals (SIS 139,977; SIF 123,775; SCC 94,450; ASC 84,995) and area-source counts by TRT (SIS 35; ASC 29; SIF 27; SCC 17) are explicitly stated in source_model.md. Point-source counts per TRT are computed by difference and the sum recovers the stated totals.]

| Tectonic region type | Code | Area sources | Point sources | Total |
|---|---|---:|---:|---:|
| Subduction Intraslab | SIS | 35 | 139,942 | 139,977 |
| Subduction Interface | SIF | 27 | 123,748 | 123,775 |
| Stable Continental Crust | SCC | 17 | 94,433 | 94,450 |
| Active Shallow Crust | ASC | 29 | 84,966 | 84,995 |
| **Total** | | **108** | **443,089** | **443,197** |

The model domain extends from approximately 60.0$^\circ$E to 100.8$^\circ$E in longitude and 2.0$^\circ$N to 40.0$^\circ$N in latitude, covering India, Bangladesh, Bhutan, Nepal, Pakistan, Myanmar, and surrounding regions. [KB:source_model.md]^[Confidence: HIGH, Rationale: Geographic extent is explicitly stated in source_model.md and is consistent with the described tectonic coverage of the Indian subcontinent.]

The minimum magnitude ($M_{\min}$) adopted for hazard calculations is 4.5 Mw across all area sources and across the primary smoothed-seismicity branch. An alternative smoothed-seismicity branch uses $M_{\min}$ = 5.5 Mw as an epistemic alternative. [KB:source_model.md]^[Confidence: HIGH, Rationale: The 4.5 Mw Mmin for area sources is stated in source_model.md. The two Mmin thresholds (4.5 and 5.5 Mw) for the respective smoothed-seismicity branches are confirmed by the file names and source descriptions in source_model.md.]

The SSM is defined through three logic-tree files: `ssmLT_IND.xml` (the primary logic tree containing three branch sets), `ssmLT_IND_collapsed.xml` (a collapsed variant), and `ssmLT_IND_garage_v1.xml` (a full variant). The primary logic tree references three source-model XML files and produces 27 end-branches from the combination of three branch sets, each containing three branches ($3 \times 3 \times 3 = 27$). [KB:source_model.md]^[Confidence: HIGH, Rationale: Logic-tree file names and branch-set structure are explicitly listed in source_model.md. The end-branch count of 27 follows directly from the stated 3 x 3 x 3 configuration.]

## SLOT 2: Source-Model Logic Tree Structure

The source-model logic tree encodes epistemic uncertainty by defining alternative realisations of the SSM. Each branch set addresses a specific source of uncertainty, and branches within each set carry weights reflecting the relative credibility of each alternative. The primary logic tree (`ssmLT_IND.xml`) contains three branch sets that together produce 27 end-branches; the two additional files (`ssmLT_IND_collapsed.xml` and `ssmLT_IND_garage_v1.xml`) are variant representations of the same structure. [KB:source_model.md]^[Confidence: HIGH, Rationale: All logic-tree details are directly stated in source_model.md. Weights within each branch set sum to 1.00, confirming internal consistency.]

Branch set 1 addresses source-model selection (uncertainty type: `sourceModel`, applies to all sources). Three alternative source-model realisations are offered: the 108-zone areal model and two smoothed-seismicity grids differing in their minimum magnitude threshold. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 1 composition is explicitly described in source_model.md with branch IDs, file names, and weights. Weights sum to 0.40 + 0.27 + 0.33 = 1.00.]

| Branch | Source-model file | Weight |
|---|---|---:|
| `b1m1` | `nt2012_areal_source_model_v1.xml` | 0.40 |
| `b1m2` | `nt2012_smoothed_source_model_v1_mmin4.5.xml` | 0.27 |
| `b1m3` | `nt2012_smoothed_source_model_v1_mmin5.5.xml` | 0.33 |

Branch set 2 addresses maximum-magnitude perturbation (uncertainty type: `maxMagGRRelative`, applies to all sources). A relative adjustment is applied to the base $M_{\max}$ of every source simultaneously, spanning a symmetric range of $\pm 0.3$ magnitude units. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 2 parameters are explicitly stated in source_model.md. Weights sum to 0.32 + 0.36 + 0.32 = 1.00, internally consistent.]

| Branch | Perturbation ($\Delta M_{\max}$) | Weight |
|---|---:|---:|
| `b2m1` | $-0.3$ | 0.32 |
| `b2m2` | $0.0$ | 0.36 |
| `b2m3` | $+0.3$ | 0.32 |

Branch set 3 addresses $b$-value perturbation (uncertainty type: `bGRRelative`, applies to all sources). A relative adjustment is applied to the base $b$-value of every source simultaneously, spanning a symmetric range of $\pm 0.1$. [KB:source_model.md]^[Confidence: HIGH, Rationale: Branch set 3 parameters are explicitly stated in source_model.md. Weights sum to 0.32 + 0.36 + 0.32 = 1.00, internally consistent.]

| Branch | Perturbation ($\Delta b$) | Weight |
|---|---:|---:|
| `b3m1` | $-0.1$ | 0.32 |
| `b3m2` | $0.0$ | 0.36 |
| `b3m3` | $+0.1$ | 0.32 |

## SLOT 3: Earthquake Recurrence Parameters

Earthquake recurrence parameters quantify the expected rate and size distribution of future earthquakes on each seismic source. Recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source. All 108 area sources use the truncated Gutenberg-Richter MFD (`truncGutenbergRichterMFD`), parameterised by an $a$-value (the logarithm of the rate of earthquakes above $M = 0$), a $b$-value (the slope of the log-linear frequency-magnitude relationship), and explicit bounds $M_{\min}$ and $M_{\max}$. The two smoothed-seismicity grid models inherit the same Gutenberg-Richter parametrisation from the parent areal zones, distributed over a regular spatial grid; per-node $a$-values are derived from the zonal rates and therefore represent distributed rates over fine grid cells rather than whole-zone rates. [KB:source_model.md]^[Confidence: HIGH, Rationale: MFD type and parameterisation are explicitly stated in source_model.md for all 108 area sources and for the smoothed-seismicity grids. The derivation of grid-node parameters from areal zone rates is stated in source_model.md.]

The table below summarises recurrence parameters by tectonic region type for the 108 area sources. The $M_{\min}$ is 4.5 Mw for all four groups. Epistemic uncertainty in $b$-value is captured through logic-tree branch set 3 ($\Delta b = \pm 0.1$; weights 0.32, 0.36, 0.32). [KB:source_model.md]^[Confidence: HIGH, Rationale: All tabulated values are directly extracted from source_model.md. The $M_{\min}$ of 4.5 Mw for all area sources is stated explicitly. The b-value epistemic treatment via branch set 3 is documented in source_model.md.]

| Tectonic region | $n$ | MFD type | $a$-value range | $b$-value range | $M_{\min}$ (Mw) | $M_{\max}$ range (Mw) |
|---|---:|---|---|---|---:|---|
| ASC | 29 | truncGR | 2.73 - 7.08 | 0.72 - 1.37 | 4.5 | 7.0 - 8.8 |
| SCC | 17 | truncGR | 1.58 - 4.84 | 0.63 - 1.19 | 4.5 | 6.0 - 8.2 |
| SIF | 27 | truncGR | 3.12 - 5.40 | 0.72 - 1.24 | 4.5 | 6.5 - 9.4 |
| SIS | 35 | truncGR | 3.22 - 7.33 | 0.80 - 1.57 | 4.5 | 6.5 - 8.6 |

## SLOT 4: Magnitude-Frequency Distribution Types

The IND source model employs a single MFD type across all parameterised sources: the truncated Gutenberg-Richter distribution (`truncGutenbergRichterMFD`). This distribution characterises earthquake occurrence rates through an $a$-value, a $b$-value, and explicit lower and upper magnitude bounds $M_{\min}$ and $M_{\max}$. No `incrementalMFD`, `arbitraryMFD`, or `multiMFD` types are present in the model; neither are characteristic or hybrid MFD formulations. [KB:source_model.md]^[Confidence: HIGH, Rationale: source_model.md explicitly states that all 108 area sources use truncGutenbergRichterMFD, and the smoothed-seismicity grids inherit this parametrisation. No other MFD types are referenced in any KB document.]

Three magnitude-area scaling relationships are applied across the model, differentiated by tectonic environment. The Wells and Coppersmith (1994) relationship (`WC1994`) [@Wells1994] governs 46 area sources in Active Shallow Crust and Stable Continental Crust settings. The Strasser et al. (2010) intraslab relationship (`StrasserIntraslab`) [@Strasser2010] is applied to 35 area sources in subduction intraslab settings. The Strasser et al. (2010) interface relationship (`StrasserInterface`) [@Strasser2010] is applied to 27 area sources in subduction interface settings. All area sources use a rupture aspect ratio of 2.0. [KB:source_model.md]^[Confidence: HIGH, Rationale: Scaling relationship assignments and source counts per relationship are explicitly tabulated in source_model.md. The sum 46 + 35 + 27 = 108 is internally consistent with the total area source count. Citekeys [@Wells1994] and [@Strasser2010] are preserved from the KB.]

## SLOT 5: Slip-Rate Data and Moment Balance

Activity rates for fault sources with available slip-rate data are derived through seismic-moment balance, relating the seismic moment rate $\dot{M}_0$ to fault geometry and long-term kinematics.^[Confidence: HIGH, Rationale: The moment-balance approach is standard in PSHA practice and is provided as framing context in the task. The equation below is a transcription of the standard formula.]

$$\dot{M}_0 = \mu\, A\, S$$

In this expression, $\mu$ is the shear modulus of the crust, $A$ is the fault area, and $S$ is the long-term fault slip rate. The moment rate $\dot{M}_0$ is then converted to earthquake occurrence rates via the moment-magnitude scaling and integrated over the MFD.^[Confidence: HIGH, Rationale: The variable definitions follow standard usage in seismic hazard analysis consistent with the PSHA framework cited throughout the source model. No KB-specific citation is required for this definitional statement.]

The IND source model contains no fault sources. The model comprises 108 area sources and 443,089 point sources (smoothed-seismicity grids); no characterised fault traces are included in any of the three source-model XML files. As a consequence, no sources carry slip-rate data, and the seismic-moment balance approach described above is not applied. Activity rates for all area sources are derived from Gutenberg-Richter fitting to the instrumental and historical seismicity catalogue compiled by Nath, Thingbaijam and Ghosh (2010). [KB:source_model.md][KB:site_sources.md]^[Confidence: HIGH, Rationale: The absence of fault sources is explicitly confirmed in site_sources.md ("No fault sources are included in the IND source model") and is consistent with source_model.md, which lists only areaSource and pointSource types. The GR-based derivation of activity rates follows from the use of truncGutenbergRichterMFD for all area sources, as documented in source_model.md.]

## SLOT 6: Maximum Magnitude Characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency distribution for each source and is a critical parameter controlling the tail of the hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree branch set 2, which applies relative perturbations (`maxMagGRRelative`) to the base $M_{\max}$ of all sources simultaneously. [KB:source_model.md]^[Confidence: HIGH, Rationale: The role of Mmax and its logic-tree treatment are explicitly described in source_model.md. No contradictions detected.]

For area sources, base $M_{\max}$ values range from 6.0 to 9.4 Mw across all 108 zones, reflecting the wide range of tectonic environments spanning from stable continental crust to subduction megathrust settings. Applying the logic-tree perturbations of $-0.3$, $0.0$, and $+0.3$ (weights 0.32, 0.36, 0.32) yields a low $M_{\max}$ range of 5.7-9.1 Mw, a central range of 6.0-9.4 Mw, and a high range of 6.3-9.7 Mw. The highest $M_{\max}$ values correspond to subduction interface settings (e.g., Sumatra, Himalayas Main Frontal Thrust) where great earthquakes ($M > 8.5$) are considered possible. The $M_{\max}$ values for all area sources are set as explicit parameters within the `truncGutenbergRichterMFD` specification, derived by expert judgement from regional seismotectonic analysis as documented by Nath and Thingbaijam [-@Nath2012]. [KB:source_model.md]^[Confidence: HIGH, Rationale: Base Mmax range (6.0-9.4 Mw), epistemic bounds (5.7-9.1 low; 6.3-9.7 high), and the derivation attribution to Nath and Thingbaijam (2012) are all directly stated in source_model.md. The citekey [-@Nath2012] is preserved from the KB.]

For the smoothed-seismicity point-source grids, $M_{\max}$ values are inherited from the parent areal zone model and distributed over the regular spatial grid. Epistemic uncertainty is applied by the same `maxMagGRRelative` branch set with the same perturbations and weights, so $M_{\max}$ is not specified independently for each grid node but follows the global relative perturbation scheme. The $M_{\max}$ values for each point source are therefore implicit in the inherited grid parameters rather than independently estimated. [KB:source_model.md][KB:site_sources_data.md]^[Confidence: HIGH, Rationale: The point-source Mmax inheritance mechanism is stated in source_model.md. site_sources_data.md confirms that the nearest smoothed-seismicity point sources carry the same Mmax base/low/high structure (6.5/6.2/6.8 Mw) as the parent areal zone parameters, consistent with the inheritance claim.]

## SLOT 7: Seismogenic Depth Parameters

Seismogenic depth parameters define the vertical extent within which earthquake ruptures are generated. Upper and lower seismogenic depths bound the rupture zone; hypocentral depth distributions, where specified, control the depth placement of point-source ruptures. In the IND model, hypocentral depths are specified as single-value distributions with probability 1.0 for all area sources -- that is, a single representative hypocentral depth is assigned deterministically to each zone. [KB:source_model.md]^[Confidence: HIGH, Rationale: The single-value hypocentral depth distribution specification is explicitly stated in source_model.md. The depth bounding structure is also clearly documented.]

The table below summarises the seismogenic depth parameters by tectonic region type. [KB:source_model.md]^[Confidence: HIGH, Rationale: All depth values are directly tabulated in source_model.md. The multi-layer structure is internally consistent across area source types.]

| Tectonic region | $z_{\text{upper}}$ (km) | $z_{\text{lower}}$ (km) | Mean hypocentral depth (km) |
|---|---|---|---|
| ASC | 0 | 25 | 15 |
| SCC | 0-25 | 25-70 | 15-25 |
| SIF | 0-70 | 25-180 | 15-70 |
| SIS | 25-180 | 70-300 | 25-180 |

The depth structure reflects a multi-layer architecture: shallow crustal sources (ASC and the upper SCC layer) are confined to the uppermost 25 km of the crust; intermediate-depth zones (lower SCC and the upper portions of the subduction envelopes) extend to 70 km; and deep subduction intraslab zones reach 300 km depth. The wide depth ranges for SIF and SIS reflect the global variability of subduction geometries included in the model domain, from shallow interface contact zones to deep slab ruptures. [KB:source_model.md]^[Confidence: HIGH, Rationale: The multi-layer characterisation and the stated depth ranges are consistent with the tabulated values in source_model.md. The interpretation of depth range variability for SIF and SIS is directly supported by the tectonic context described in the KB.]

## SLOT 8: Local Sources and Site Interrogation

The Rampura Agucha site (74.7413$^\circ$E, 25.8474$^\circ$N) is contained within two overlapping areal seismogenic zones -- z919 and z932 -- both classified under the Stable Continental Crust (SCC) tectonic regime of Peninsular India. No Active Shallow Crust, subduction interface, or subduction intraslab sources include the site; the seismic source environment in the immediate vicinity is therefore characterised entirely by intraplate continental seismicity, reflecting the stable shield character of Peninsular India. [KB:site_sources.md][KB:site_sources_data.md]^[Confidence: HIGH, Rationale: Zone containment and TRT classification are explicitly stated in site_sources.md and confirmed by site_sources_data.md. The SCC classification for both containing zones is unambiguous and consistent across KB documents.]

Zone z919 (Peninsular India Layer 1, shallow SCC) spans seismogenic depths of 0.0 to 25.0 km with a mean hypocentral depth of 15.0 km. Its base $M_{\max}$ is 7.20 Mw (epistemic range 6.90-7.50 Mw; $a$ = 2.73, $b$ = 0.72, $M_{\min}$ = 4.5 Mw), and its faulting style is reverse (nodal plane: strike 290$^\circ$, dip 61$^\circ$, rake 123$^\circ$). Zone z932 (Peninsular India Layer 2, intermediate SCC) spans depths of 25.0 to 70.0 km with a mean hypocentral depth of 25.0 km. Its base $M_{\max}$ is 6.50 Mw (epistemic range 6.20-6.80 Mw; $a$ = 4.15, $b$ = 0.93, $M_{\min}$ = 4.5 Mw), and its faulting style is sinistral strike-slip (nodal plane: strike 239$^\circ$, dip 67$^\circ$, rake 8$^\circ$). The source-selection algorithm designates z919 as the primary zone for the site. [KB:site_sources.md][KB:site_sources_data.md]^[Confidence: HIGH, Rationale: All zone parameters (depths, MFD values, faulting style, nodal planes, primary zone designation) are explicitly tabulated in site_sources.md and confirmed by site_sources_data.md. No contradictions between the two KB documents were detected.]

In the immediate vicinity of the site, the most seismically relevant events are characterised as intraplate SCC earthquakes reaching up to approximately 7.2 Mw (base $M_{\max}$) at shallow crustal depths (mean hypocentral depth approximately 15 km, within the 0-25 km seismogenic layer), with reverse faulting kinematics dominant in the shallow layer. The intermediate-depth layer (z932, 25-70 km) contributes a supplementary source at lower magnitude potential (base $M_{\max}$ 6.5 Mw) with strike-slip kinematics. These two zones represent the geometric candidates for site-controlling sources; definitive identification of the dominant contributors to hazard requires deaggregation of the PSHA results. [KB:site_sources.md][KB:site_sources_data.md]^[Confidence: MEDIUM, Rationale: The magnitude and depth interpretation is directly supported by the zone parameters in site_sources.md and site_sources_data.md. MEDIUM confidence is assigned because site_sources.md explicitly cautions that "definitive identification of controlling sources requires deaggregation of the PSHA results" -- the sources listed are geometric candidates, and the actual hazard contribution depends on recurrence rate and ground-motion attenuation, which are not evaluated in this geometric report.]

## SLOT 9: Smoothed-Seismicity Nearest Point Sources

The IND source model includes two smoothed-seismicity branches providing gridded point-source representations of distributed seismicity across the model domain. For each branch, the nearest point source to the Rampura Agucha site provides a reference for the distributed seismicity contribution at the site location. Both nearest sources lie within the SCC intermediate-depth layer (layer L2), consistent with the parent areal zone z932 that occupies the same depth interval. [KB:site_sources_data.md][KB:site_sources.md]^[Confidence: HIGH, Rationale: The two-branch structure and the nearest-point-source identifications are explicitly documented in site_sources_data.md. The L2 layer designation is embedded in the source IDs and confirmed by the depth parameters.]

The first branch (`nt2012_smoothed_source_model_v1_mmin4.5.xml`, branch weight 0.27) has its nearest point source identified as `25N_75p2E_L2_M4p5`, located at 75.2$^\circ$E, 25.0$^\circ$N, at a source-to-site distance of 104.6 km. This source carries a truncated Gutenberg-Richter MFD with $a = -1.4682$, $b = 0.93$ (epistemic range 0.83-1.03), and base $M_{\max}$ = 6.5 Mw (epistemic range 6.2-6.8 Mw). The seismogenic depth interval is 25.0-70.0 km with a mean hypocentral depth of 25.0 km. [KB:site_sources_data.md]^[Confidence: HIGH, Rationale: All parameters for the mmin4.5 nearest point source are explicitly listed in site_sources_data.md. The negative a-value is physically expected for a per-node rate on a fine spatial grid, representing a fraction of the parent zonal rate. No contradictions detected.]

The second branch (`nt2012_smoothed_source_model_v1_mmin5.5.xml`, branch weight 0.33) has its nearest point source identified as `26p7N_74p1E_L2_M5p5`, located at 74.1$^\circ$E, 26.7$^\circ$N, at a source-to-site distance of 114.1 km. This source carries a truncated Gutenberg-Richter MFD with $a = -0.9144$, $b = 0.93$ (epistemic range 0.83-1.03), and base $M_{\max}$ = 6.5 Mw (epistemic range 6.2-6.8 Mw). The seismogenic depth interval is 25.0-70.0 km with a mean hypocentral depth of 25.0 km. [KB:site_sources_data.md]^[Confidence: HIGH, Rationale: All parameters for the mmin5.5 nearest point source are explicitly listed in site_sources_data.md. The higher a-value compared to the mmin4.5 branch nearest source (-0.9144 vs -1.4682) is consistent with the exclusion of smaller-magnitude events concentrating activity into fewer bins. No contradictions detected.]

Both nearest smoothed-seismicity point sources lie more than 100 km from the site, indicating that the areal zones containing the site (z919 and z932) represent the geometrically closest source contributions within the areal model branch. The shared $b = 0.93$ value and $M_{\max}$ = 6.5 Mw (base) at these grid nodes are consistent with the parameters of the overlapping areal zone z932, confirming that the smoothed-seismicity grids reproduce the parent zone characterisation at the site location. [KB:site_sources.md][KB:site_sources_data.md]^[Confidence: HIGH, Rationale: The distances of 104.6 km and 114.1 km are explicitly stated in site_sources_data.md. The b-value and Mmax consistency with z932 is confirmed by comparison of parameters across site_sources.md and site_sources_data.md: z932 has b=0.93 and Mmax=6.5 Mw (base), matching both nearest point sources exactly.]
