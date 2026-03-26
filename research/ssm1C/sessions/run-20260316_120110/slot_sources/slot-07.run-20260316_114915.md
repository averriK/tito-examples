## SLOT 7: Seismogenic Depth Parameters

Seismogenic depth parameters define the vertical extent within which earthquake ruptures are generated. Upper and lower seismogenic depths bound the rupture zone; hypocentral depth distributions, where specified, control the depth placement of point-source ruptures. The depth model reflects a multi-layer structure: shallow crustal sources (ASC and upper SCC) are confined to the top 25 km; intermediate-depth zones (lower SCC, upper SIF and SIS) extend to 70 km; and deep subduction intraslab zones reach 300 km depth. [KB:source_model.md]^[Confidence: HIGH, Rationale: The depth model and its three-layer structure are explicitly described and tabulated in source_model.md. The depth ranges for each TRT are directly stated with no internal contradictions.]

Table 3 summarises the seismogenic depth parameters for each tectonic region type. Hypocentral depths are specified as single-value distributions with probability 1.0 for all area sources. [KB:source_model.md]^[Confidence: HIGH, Rationale: The depth parameter values are directly taken from the depth model table in source_model.md. The specification of single-value hypocentral distributions (probability 1.0) is explicitly stated in the same document. Site-specific data for z919 (15.0 km, prob 1.0) and z932 (25.0 km, prob 1.0) in site_sources.md confirm this pattern for SCC sources.]

**Table 3. Seismogenic depth parameters by tectonic region type (area sources).**^[Confidence: HIGH, Rationale: Table caption only; descriptive label for the following table, whose values are drawn from source_model.md.]

| Tectonic Region | $z_{\text{upper}}$ (km) | $z_{\text{lower}}$ (km) | Mean hypocentral depth (km) |
|---|---|---|---|
| ASC | 0 | 25 | 15 |
| SCC | 0-25 | 25-70 | 15-25 |
| SIF | 0-70 | 25-180 | 15-70 |
| SIS | 25-180 | 70-300 | 25-180 |

