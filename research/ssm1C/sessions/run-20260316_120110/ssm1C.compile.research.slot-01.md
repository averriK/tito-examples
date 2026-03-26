## SLOT 1: SSM Overview and Source Census

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

The SSM is defined through three logic-tree XML files: `ssmLT_IND.xml` (the primary logic tree with three branch sets), `ssmLT_IND_collapsed.xml` (a collapsed variant), and `ssmLT_IND_garage_v1.xml` (a full alternative variant). The primary logic tree references three source-model XML files and produces 27 end-branches from the Cartesian product of three branch sets ($3 \times 3 \times 3 = 27$). The logic tree branch sets are described in detail in SLOT 2.

Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [@Cornell1968] and formalised under SSHAC guidelines [@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with geometry and parametrisation defined in OpenQuake source-model XML files. The implementation is publicly available at the `nackerley/indian-subcontinent-psha` repository on GitHub [@NackerleyRepo].
