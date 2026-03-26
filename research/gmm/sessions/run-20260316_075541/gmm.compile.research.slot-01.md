## SLOT 1: Definitions, Notation, and Equations for the GMM Framework

A ground-motion prediction equation (GMPE), also referred to as a ground-motion model (GMM) or attenuation relationship, provides a mathematical description of the conditional probability distribution of a ground-motion intensity measure (IM) at a site given a specified earthquake scenario. Intensity measures considered in this chapter include the spectral acceleration $\mathrm{SA}(T)$ at oscillator period $T$, peak ground acceleration ($\mathrm{PGA}$), and peak ground velocity ($\mathrm{PGV}$). The conventional ergodic formulation expresses the natural logarithm of a scalar IM as the sum of a deterministic median prediction and a zero-mean random residual [@OpenQuakeEngine]:

$$\ln Y = \mu_{\ln Y}(M_w,\, \mathbf{R},\, \boldsymbol{\theta}) + \varepsilon$$

In this expression, $Y$ is the ground-motion intensity measure; $M_w$ is moment magnitude; $\mathbf{R}$ denotes the vector of relevant source-to-site distance metrics; $\boldsymbol{\theta}$ collects additional predictor variables including rupture geometry descriptors and site parameters; $\mu_{\ln Y}$ is the median prediction expressed in natural-log units; and $\varepsilon$ is the total residual, assumed to follow a zero-mean normal distribution with standard deviation $\sigma$, so that $Y$ is log-normally distributed with median $\exp[\mu_{\ln Y}]$ [@BEE2022a].

The total aleatory standard deviation $\sigma$ satisfies the quadrature relation:

$$\sigma^2 = \tau^2 + \phi^2$$

where $\tau$ is the between-event (inter-event) standard deviation and $\phi$ is the within-event (intra-event) standard deviation. Under the mixed-effects decomposition adopted by most modern empirical GMPEs, the total residual for record $j$ belonging to event $i$ is partitioned as:

$$\varepsilon_{ij} = \eta_i + \delta_{ij}$$

where $\eta_i \sim \mathcal{N}(0, \tau^2)$ is the between-event residual for event $i$, representing systematic source-to-source variation not captured by the median functional form, and $\delta_{ij} \sim \mathcal{N}(0, \phi^2)$ is the within-event residual for record $j$, representing path and site variability not resolved by the median prediction. The two residual components are assumed mutually independent [@BEE2017]. All three quantities $\sigma$, $\tau$, and $\phi$ are period-dependent in most modern GMPEs and are tabulated or parameterized as part of the published model. Non-ergodic formulations further partition $\tau$ and $\phi$ into site-specific and path-specific components; the models documented in this chapter are predominantly ergodic.

The predictor variables entering a GMPE vary by model and tectonic region type, but the following notation applies consistently across all models documented in this chapter [@GmmLTASC][@GmmLTSCC][@GmmLTSIF][@GmmLTSIS]. Moment magnitude $M_w$ is the primary source-size parameter. For source-to-site geometry, the principal distance metrics are as follows:

- $R_{JB}$: the Joyner-Boore distance, defined as the shortest horizontal distance from the site to the surface projection of the fault rupture plane
- $R_{rup}$: the closest three-dimensional distance from the site to the rupture plane
- $R_x$: the horizontal distance from the site to the surface projection of the top edge of the rupture, measured perpendicular to the fault strike
- $R_{hypo}$: hypocentral distance
- $R_{epi}$: epicentral distance

The specific distance metric required by each model in the OpenQuake hazardlib is declared as part of the GSIM implementation and is listed in the per-tectonic-region sections that follow. Site amplification is parameterized primarily by $V_{S30}$, the time-averaged shear-wave velocity in the uppermost 30 m. Basin depth is captured by $z_{1.0}$, the depth to the horizon where shear-wave velocity first reaches 1.0 km/s, and by $z_{2.5}$, the depth to the 2.5 km/s horizon. Rupture geometry descriptors include $z_{tor}$, the depth to the top of the rupture plane; the fault dip angle; the rake angle characterizing faulting style; the along-dip rupture width $W$; and hypocentral depth $h$. For subduction models, a binary backarc flag distinguishing forearc and backarc site positions is additionally required by certain implementations [@GmmLTSIF][@GmmLTSIS].
