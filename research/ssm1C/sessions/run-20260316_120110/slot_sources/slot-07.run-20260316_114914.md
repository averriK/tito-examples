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

