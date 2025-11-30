## Numerical Implementation in OpenQuake {#sec-hazard_appendix}

The probabilistic seismic hazard analysis is performed with the OpenQuake engine. The input model follows the NRML structure: a source-model logic tree and a ground-motion logic tree describe epistemic alternatives and weights; realizations are built from their Cartesian product, with realization weights given by the product of branch weights [@OpenQuakeManual section 2.2.1; @Pagani2014].

Calculation settings are defined in the job configuration, including mesh spacing for source discretization, magnitude-frequency bin width, maximum integration distance, truncation level for the Gaussian distribution of $\ln IM$, investigation time, intensity-measure types, and the grid of intensity-measure levels [@OpenQuakeConfig].

For each realization, OpenQuake constructs ruptures by sampling source geometry and magnitude bins. Rupture dimensions follow the configured magnitude–area or magnitude–length scaling relationship and aspect-ratio assumptions; a common option is the Wells–Coppersmith family of relations [@Wells1994].

Ground-motion exceedance probabilities for each magnitude–distance scenario are computed from the selected GSIM branch using its median and dispersion and the required distance metrics (for example, $R_{\mathrm{rup}}$ and $R_{\mathrm{JB}}$) evaluated from the rupture surfaces, consistent with the hazard library interface [@Pagani2014; @OpenQuakeGSIM].

Hazard curves are produced on the user-specified grid of intensity-measure levels for each oscillator period. When epistemic uncertainties are present, OpenQuake stores per-realization curves and statistical aggregates. In OpenQuake, the mean at a given intensity level is the weighted arithmetic mean of branchwise probabilities of exceedance, and quantiles are weighted quantiles of those probabilities; statistics are thus taken in PoE space at fixed IMLs [@Weatherill2024; @OpenQuakeManual section 2.3.3.1].

Uniform-hazard spectra are obtained by interpolating hazard curves at a fixed exceedance probability across periods, yielding spectral ordinates consistent with the chosen statistic (mean or quantile) [@OpenQuakeHazardCalcs].

Outputs and metadata are available through the standard export mechanisms. The documentation details per-site CSV outputs with `poe-<IML>` columns, the list of realizations and weights, and datastore/HDF5 contents for reproducibility [@OpenQuakeOutputs].


