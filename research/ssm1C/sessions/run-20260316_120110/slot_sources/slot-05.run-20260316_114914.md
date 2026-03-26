## SLOT 5: Slip-Rate Data and Moment Balance

Activity rates for fault sources with available slip-rate data are derived through seismic-moment balance, relating the seismic moment rate $\dot{M}_0$ to fault geometry and long-term kinematics.^[Confidence: HIGH, Rationale: The moment-balance approach is standard in PSHA practice and is provided as framing context in the task. The equation below is a transcription of the standard formula.]

$$\dot{M}_0 = \mu\, A\, S$$

In this expression, $\mu$ is the shear modulus of the crust, $A$ is the fault area, and $S$ is the long-term fault slip rate. The moment rate $\dot{M}_0$ is then converted to earthquake occurrence rates via the moment-magnitude scaling and integrated over the MFD.^[Confidence: HIGH, Rationale: The variable definitions follow standard usage in seismic hazard analysis consistent with the PSHA framework cited throughout the source model. No KB-specific citation is required for this definitional statement.]

The IND source model contains no fault sources. The model comprises 108 area sources and 443,089 point sources (smoothed-seismicity grids); no characterised fault traces are included in any of the three source-model XML files. As a consequence, no sources carry slip-rate data, and the seismic-moment balance approach described above is not applied. Activity rates for all area sources are derived from Gutenberg-Richter fitting to the instrumental and historical seismicity catalogue compiled by Nath, Thingbaijam and Ghosh (2010). [KB:source_model.md][KB:site_sources.md]^[Confidence: HIGH, Rationale: The absence of fault sources is explicitly confirmed in site_sources.md ("No fault sources are included in the IND source model") and is consistent with source_model.md, which lists only areaSource and pointSource types. The GR-based derivation of activity rates follows from the use of truncGutenbergRichterMFD for all area sources, as documented in source_model.md.]

