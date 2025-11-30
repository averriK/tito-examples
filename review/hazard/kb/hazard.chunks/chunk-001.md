## Methodology

### Hazard Model

Probabilistic Seismic Hazard Analysis (PSHA) is a methodology that quantifies earthquake ground-motion hazard at a site in terms of probabilities, by integrating over all possible earthquakes that could affect the site [@Cornell1968; @McGuire2004]. Unlike deterministic approaches that focus on a single scenario, PSHA considers the full range of magnitudes, locations, and associated ground motions, providing a comprehensive description of the rate at which various levels of shaking may be exceeded. In probabilistic seismic hazard analysis (PSHA), the annual frequency (rate) of exceeding a ground-motion level at a site is obtained by integrating over all possible earthquake scenarios. For a single seismic source $(s)$ with an annual occurrence rate of earthquakes (above a minimum magnitude $M_{\min}$) denoted $\nu_{0}^{(s)}$ (where $\nu_{0}^{(s)} = N(M_{\min})^{(s)}$), the rate of exceedance of a ground-motion level $i^*$ (e.g., a peak ground acceleration or spectral acceleration) is defined in [@eq-A1], where $m$ is earthquake magnitude, $\mathbf r$ is the source-to-site distance, $f_{M,s}(m)$ and $f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)$ are the probability density functions describing the distribution of magnitudes and distances for source $(s)$, and $P\left[I > i^* \mid M=m,\,\mathbf r\right]$ is the conditional probability that the ground-motion parameter $I$ exceeds level $i^*$ given an event of magnitude $m$ at distance $\mathbf r$. $M_{\max}^{(s)}$ is the maximum considered magnitude for source $(s)$, which is related to the maximum credible earthquake (MCE) of that source (see [@sec-MCE]).

$$
\lambda_I(i^*)^{(s)} \;=\;
\nu_{0}^{(s)}
\int_{M_{\min}}^{M_{\max}^{(s)}} \int_{D}
P\left[ I > i^* \,\big|\, m, \mathbf{r} \right]\;
f_{M,s}(m)\;
f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)\;
\mathrm d\mathbf{r}\,\mathrm dm
$${#eq-A1}



The probability density functions (PDF) $f_{M,s}(m)$ and $f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)$ describe the normalized distributions of earthquake magnitudes and locations within source $(s)$. This formulation is a direct application of the total-probability theorem in continuous form, integrating over all magnitudes and locations of earthquakes from source $(s)$ that could contribute to exceedance of level $i^*$. All *aleatory variability* in earthquake occurrence, earthquake size, earthquake location, and ground motion is thus accounted for through the integration [@McGuire2004; @Baker2021]. If multiple seismic sources contribute to the hazard at the site, the total annual exceedance rate $\lambda_I(i^*)$ is obtained by summing the contributions from all sources as in [@eq-A1-sum]. Assuming $N_S$ independent sources, each with its own occurrence rate and distributions as above, the overall exceedance frequency for level $i^*$ is given by [@eq-A1-sum], where $\lambda_I(i^*)^{(s)}$ is evaluated for each source via the hazard integral. This linear superposition is valid under the assumption that earthquake occurrences in different sources are independent (typically modeled as independent Poisson processes). The result is a seismic-hazard curve that quantifies the rate at which various ground-motion levels are exceeded at the site.

$$
\lambda_I(i^*) \;=\; \sum_{s=1}^{N_S} \lambda_I(i^*)^{(s)}
$${#eq-A1-sum}


The annual exceedance frequency $\lambda_I(i^*)$ obtained from the hazard integral [@eq-A1] can be interpreted as the mean number of times per year that intensity $i^*$ is exceeded. If we assume that exceedance events follow a Poisson process in time (a standard assumption in PSHA, owing to the Poissonian occurrence of earthquakes), then the probability of at least one exceedance in a single year is defined in [@eq-AEP]^[For small $\lambda_{I}$ (hazard levels of practical interest are usually low probability), $P_{1\text{yr}} \approx \lambda_{I}$ (since $e^{-\lambda} \approx 1-\lambda$)].

$$
P_{1\text{yr}}[I > i^*] = 1 - \exp[-\lambda_I(i^*)] = \text{AEP}
$${#eq-AEP}

By extension, the probability of exceedance in $T$ years is $P_{T}(I > i^*) = 1 - \exp[-\lambda_I(i^*) T]$ assuming stationarity and independence year-to-year. This relation allows conversion between a mean annual rate and a probability over $T$ years^[A common case is $T=50$ years (an approximate lifespan of structures); for example, if $\lambda_I(i^*) = 0.0021$ per year, then $P_{50}(I>i^*) = 1 - \exp(-0.0021 \times 50) \approx 0.10$, i.e. a 10% probability in 50 years.]. The **return period** $T_R$ (or **mean return interval**) is a statistical average defined as the reciprocal of the annual frequency of exceedance, usually expressed in years $T_R = \frac{1}{\lambda_I(i^*)}$^[For low probabilities, return period is approximately the inverse of AEP as well, since $\text{AEP} \approx \lambda_{I}$ for small $\lambda_{I}$.]

### Ground-Motion Prediction Equations (GMPE) {#sec-GMPE}

The term $P[I > i^* \mid m,\mathbf{r}]$ in the hazard integral represents the ground-motion model’s probabilistic prediction of exceedance and can be obtained from ground-motion prediction equations (GMPEs). GMPEs—also called attenuation relationships—are empirical or semi-empirical models that predict the statistical distribution of ground-motion intensity measures (e.g., PGA, spectral acceleration) given an earthquake’s characteristics. A GMPE typically provides a median predicted ground motion (often in $\log_{10}$ or natural-log units) as a function of parameters such as magnitude $M$, source-to-site distance $R$, and site condition, along with an estimate of **aleatory variability** (the standard deviation $\sigma$ of the logarithmic residuals) [@Boore2008]. A generic form of a GMPE for an arbitrary intensity measure $I$ is given in [@eq-GMPE],
where $F$ and $S$ are indicator variables for fault type (e.g., reverse/normal) and site class (e.g., rock or soil), and $\varepsilon$ is a standard-normal (zero-mean) random variable representing the random scatter (with $\sigma_{\ln I}$ being the log-standard deviation) [@Boore2008]^[$\varepsilon$ is a random variable representing the residual (in log units) for an individual event].

$$
\ln I \approx \hat{\eta}_I(m,\mathbf{r},F,S)\;+\;\varepsilon\,\sigma_{\ln I},
$${#eq-GMPE}


 If $\hat\eta_I(m,r,F,S)$ denotes the median intensity $I$ (in linear units) for magnitude $m$ at distance $r$ and $\sigma_{\ln I}$ is the standard deviation of $\ln I$, then the conditional exceedance probability can be expressed as in [@eq-GMPE-exc], where $\Phi$ is the standard-normal cumulative-distribution function. The quantity $\varepsilon^*$, defined in [@eq-A2],represents the number of standard deviations by which $i^*$ exceeds the median prediction for scenario $(m,r,F,S)$.
$$
P[I > i^* \mid m,\mathbf{r}] \;=\; 1 \;-\; \Phi\left(\varepsilon^*\right),
$${#eq-GMPE-exc}

$$
\varepsilon^* \;=\; \frac{\ln i^* - \ln \hat{\eta}_I(m,\mathbf{r},F,S)}{\sigma_{\ln I}}
$${#eq-A2}


### Hazard Disaggregation

Probabilistic seismic hazard analysis (PSHA) aggregates the contributions of all plausible earthquake scenarios, obscuring the specific combinations of magnitude ($M$), source-to-site distance ($R$), and ground-motion residual ($\varepsilon$) that control site hazard. **Hazard disaggregation** quantifies the relative contribution of each scenario class—binned by magnitude $m_k$, distance $r_j$, and residual $\varepsilon_\ell$—to the annual frequency of exceedance at a specified ground-motion threshold $i^*$ [@Bazzurro1999].

Disaggregation is performed at a target hazard level, defined by an annual exceedance probability or return period. This produces conditional probability distributions over scenario bins and identifies controlling scenario parameters responsible for site hazard [@Kramer1997]. The ground-motion exceedance probability and total annual exceedance rate are defined in the hazard analysis (see [@eq-A1], [@eq-A2]). The joint exceedance rate for scenario $(m_k, r_j, \varepsilon_\ell)$ from source $s$ is given in [@eq-D1], where $\phi$ is the standard normal probability density function and $\mathbf 1_{{\cdot}}$ is the indicator function. Integration over $\varepsilon$ yields the two-dimensional ($M$–$R$) formulation. Partitioning parameter space into magnitude bins $m_k$, distance bins $r_j$, and residual bins $\varepsilon_\ell$, the contribution from bin $(k,j,\ell)$ is in [@eq-D2].

$$
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)} =
\mathbf 1_{\{\varepsilon\ge\varepsilon^{*}(m_k,r_j)\}}
\,
\phi(\varepsilon)\,
f_{M,s}(m_k)\,
f_{R|M,s}(r_j|m_k)\,
\nu_{s},
$${#eq-D1}

$$
\lambda_{k,j,\ell}(i^{*})=
\sum_{s=1}^{N_{S}}
\int_{m_k}
\int_{r_j}
\int_{\varepsilon_\ell}
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)}
d\varepsilon\,dr\,dm
$${#eq-D2}

The conditional probability that exceedance of $i^*$ is produced by this bin is given by [@eq-D3]. The **modal scenario** is the $(k,j,\ell)$ bin for which $P_{kj\ell}(i^{*})$ attains its maximum. Hazard disaggregation applies Bayes’ theorem to the joint distribution of scenario parameters and ground-motion exceedance as in [@eq-D3].
The marginal distribution for $\varepsilon$ quantifies the proportion of exceedance attributable to median or above-median ground-motion residuals. Marginal probabilities are obtained by double summation over the other indices as in [@eq-DH1], [@eq-DH2], [@eq-DH3]:


$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}] = \theta_{j,k,l}=
\frac{\lambda_{k,j\ell}(i^{*})}{\lambda_{I}(i^{*})}
\qquad
\sum_{k}\sum_{j}\sum_{\ell}P_{k,j,\ell}([I>i^{*}]=1
$${#eq-D3}

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{j,k,l}
$${#eq-DH1}
$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{j,k,l}
$${#eq-DH2}
$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{j,k,l}
$${#eq-DH3}

Disaggregation provides a data-driven basis required for rigorous scenario selection in engineering analysis. The *modal scenario* and the highest-probability bins identified through disaggregation correspond to the earthquake characteristics most responsible for exceedance at the design ground-motion level.

### Uncertainty model {#sec-uncertainty_hazard}

Epistemic uncertainty in seismic source characterization is represented by assigning alternative parameter sets—specifically, distinct Gutenberg–Richter triplets $(a^{(k)}, b^{(k)}, M_{\max}^{(k)})$—to each epistemic branch $(k)$ of the logic tree. Each branch defines its own magnitude-frequency distribution $f_{M,s}^{(k)}(m)$ and maximum magnitude $M_{\max}^{(k)}$ for the hazard integral as formulated in [@eq-A1]. The Gutenberg–Richter recurrence law $\log_{10} N(M)^{(s,k)} = a^{(k)} - b^{(k)}\,M$ specifies, for each source $s$ and branch $(k)$, the mean annual number of earthquakes with magnitude $\geq M$, where $a^{(k)}$ and $b^{(k)}$ are activity and slope parameters, respectively. The mean occurrence rate above $M_{\min}$ is $\nu_{0}^{(s,k)} = N(M_{\min})^{(s,k)} = 10^{\,a^{(k)} - b^{(k)}\,M_{\min}}$ [@eq-HA2], and the normalized magnitude density is $f_{M,s}^{(k)}(m)$ as defined in [@eq-HA3], with $M_{\max}^{(s,k)}$ acting as the truncation threshold for each epistemic branch.

$$
\nu_{0}^{(s,k)} = N(M_{\min})^{(s,k)} = 10^{\,a^{(k)} - b^{(k)}\,M_{\min}}.
$${#eq-HA2}

$$
f_{M,s}^{(k)}(m) =
\frac{b^{(k)}\ln 10 \,\, 10^{\,a^{(k)} - b^{(k)} m}}
     {\displaystyle\int_{M_{\min}}^{M_{\max}^{(s,k)}} 10^{\,a^{(k)} - b^{(k)} u}\,du},
\qquad
M_{\min} \le m \le M_{\max}^{(s,k)}.
$${#eq-HA3}

The branch-specific mean annual exceedance rate for a given intensity $i^*$ is $\lambda_I^{(k)}(i^*)$ [@eq-HA4], which is computed by integrating over magnitude, distance, and conditional ground motion exceedance, using the branch-dependent conditional distance distribution $f_{\mathbf{R}\mid M,s}^{(k)}(\mathbf{r}\mid m)$. The probability of exceedance $P[I > i^* \mid m,\mathbf{r},k]$ is evaluated via the ground-motion prediction equation (GMPE) assigned to each branch, which provides a branch-specific median $\hat\eta_I(m,\mathbf{r},F,S)$ and logarithmic standard deviation $\sigma_{\ln I}^{(k)}$ [@eq-HA5], where $\Phi(\cdot)$ is the standard normal cumulative distribution function. Substitution of these components yields the branch-explicit exceedance rate for each source $s$ and branch $k$ as $\lambda_I^{(s,k)}(i^*)$ [@eq-HA6], with total exceedance rate for branch $(k)$ given by the sum $\lambda_I^{(k)}(i^*) = \sum_{s=1}^{N_S} \lambda_I^{(s,k)}(i^*)$ [@eq-HA7].

$$
\lambda_I^{(k)}(i^*) =
\sum_{s=1}^{N_S} \nu_{0}^{(s,k)}
\int_{M_{\min}}^{M_{\max}^{(s,k)}} \int_D
P[I > i^* \mid m,\mathbf{r},k]\;
f_{M,s}^{(k)}(m)\;
f_{\mathbf{R}\mid M,s}^{(k)}(\mathbf{r}\mid m)\;
d\mathbf{r}\,dm,
$${#eq-HA4}

$$
P[I > i^* \mid m,\mathbf{r},k] =
1 - \Phi\!\left(
\frac{\ln i^* - \ln \hat\eta_I(m,\mathbf{r},F,S)}
     {\sigma_{\ln I}^{(k)}}
\right),
$${#eq-HA5}

$$
\lambda_I^{(s,k)}(i^*) =
\nu_{0}^{(s,k)}
\int_{M_{\min}}^{M_{\max}^{(s,k)}} \int_{D}
\left( 1 - \Phi\!\left(
\frac{\ln i^* - \ln \hat\eta_I(m,\mathbf{r},F,S)}
     {\sigma_{\ln I}^{(k)}}
\right) \right)
f_{M,s}^{(k)}(m)\,
f_{\mathbf{R}\mid M,s}^{(k)}(\mathbf{r}\mid m)\,
d\mathbf{r}\,dm.
$${#eq-HA6}

$$
\lambda_I^{(k)}(i^*) = \sum_{s=1}^{N_S} \lambda_I^{(s,k)}(i^*).
$${#eq-HA7}


Within each epistemic branch, aleatory uncertainty is fully integrated through the hazard and GMPE formulations described in [@eq-A1] and [@eq-A2], as well as through the disaggregation approach [@eq-D1], [@eq-D2], [@eq-D3]. Scenario sampling and numerical integrations are performed over the domains and bins defined in the XML logic-tree configuration. Each branch $(k)$ consistently applies its own $(a^{(k)}, b^{(k)}, M_{\max}^{(k)})$, median ground-motion model, and dispersion $\sigma_{\ln I}^{(k)}$, without mixing parameters across branches. All aggregation and quantile extraction procedures strictly follow the OpenQuake implementation [-@OpenQuakeManual2024].

