## SLOT 1: Definitions, notation, and equations for the GMM framework

A ground-motion prediction equation (GMPE), also referred to as a ground-motion model (GMM), characterizes the conditional probability distribution of a ground-motion intensity measure (IM) at a site given a set of seismic source, propagation path, and local site parameters. The fundamental representation expresses the natural logarithm of the IM as the sum of a deterministic median prediction term and a stochastic residual, reflecting the observed log-normality of ground-motion amplitudes.^[Confidence: HIGH, Rationale: The log-normal parameterization of ground-motion intensity measures is a foundational assumption of the GMPE literature, consistent with all models documented in the KB files and with the NGA-West2 and NGA-Subduction model suites. No unsupported claims are introduced.]

The formal prediction equation is:

$$\ln IM = \mu_{\ln IM}(\mathbf{X}) + \varepsilon$$

where $\mu_{\ln IM}(\mathbf{X})$ is the median prediction expressed on the natural-log scale as a function of the predictor vector $\mathbf{X}$, and $\varepsilon$ is the total residual capturing aleatory variability. The intensity measure IM is therefore log-normally distributed with median $\exp[\mu_{\ln IM}]$ and total dispersion characterized by the total standard deviation $\sigma_{total}$.^[Confidence: HIGH, Rationale: The notation and interpretation are standard across the GMPE literature. No quantitative claims are made beyond those derivable from the log-normal assumption itself.]

The predictor vector $\mathbf{X}$ comprises parameters from three classes. Source parameters include moment magnitude $M_w$, depth to the top of rupture $Z_{TOR}$, fault dip $\delta$, fault width $W$, hypocentral depth $Z_{hyp}$, and rake angle $\lambda$. Path parameters consist of one or more source-to-site distance metrics (defined below). Site parameters include the time-averaged shear-wave velocity in the top 30 m, $V_{S30}$, the depth to the 1.0 km/s shear-wave velocity horizon $Z_{1.0}$, and the depth to the 2.5 km/s horizon $Z_{2.5}$. The specific subset of parameters required by each model varies with tectonic setting and is documented per model in subsequent sections [KB:gmmLT_ASC.md][KB:gmmLT_SCC.md][KB:gmmLT_SIF.md][KB:gmmLT_SIS.md].^[Confidence: HIGH, Rationale: The parameter definitions are standard and consistent with the OpenQuake hazardlib requires_sites_parameters and requires_rupture_parameters fields listed in all four KB documents.]

The total aleatory variability is partitioned into between-event and within-event components according to:

$$\sigma_{total}^2 = \tau^2 + \phi^2$$

where $\tau$ is the standard deviation of the between-event (inter-event) residual $\eta$, and $\phi$ is the standard deviation of the within-event (intra-event) residual $\delta W$. A single ground-motion realization is expressed as:

$$\ln IM = \mu_{\ln IM}(M_w, R, \boldsymbol{\theta}) + \eta + \delta W, \qquad \eta \sim \mathcal{N}(0,\,\tau^2), \qquad \delta W \sim \mathcal{N}(0,\,\phi^2)$$

The between-event term $\eta$ captures earthquake-to-earthquake variability in source properties not explained by the magnitude scaling function; the within-event term $\delta W$ captures residual site-to-site and record-to-record variability not explained by the site characterization parameters.^[Confidence: HIGH, Rationale: The partitioning of total sigma into tau (between-event) and phi (within-event) is a standard result applied uniformly across the NGA-West2, NGA-East, and NGA-Subduction model families. The notation is internally consistent and does not require external citation beyond standard domain knowledge.]

Several distance metrics appear across the models documented in this chapter. The Joyner-Boore distance $R_{JB}$ is the shortest horizontal distance from the site to the surface projection of the fault rupture plane. The closest distance to the fault rupture surface is $R_{rup}$. The horizontal distance from the site to the surface projection of the top edge of the rupture, measured perpendicular to fault strike, is $R_x$. Hypocentral distance is denoted $R_{hypo}$ and epicentral distance $R_{epi}$. The choice of distance metric is model-dependent and reflects both the tectonic regime and the data available for calibration; the metric required by each model in the OpenQuake hazardlib is listed under the per-tectonic-region descriptions [KB:gmmLT_ASC.md][KB:gmmLT_SCC.md][KB:gmmLT_SIF.md][KB:gmmLT_SIS.md].^[Confidence: HIGH, Rationale: Distance metric definitions (RJB, Rrup, Rx, Rhypo) are standard and consistent with OpenQuake hazardlib parameter names used in the KB files. The cross-reference to subsequent sections is accurate.]

