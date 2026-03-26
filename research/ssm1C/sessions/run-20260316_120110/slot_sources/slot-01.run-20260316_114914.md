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

