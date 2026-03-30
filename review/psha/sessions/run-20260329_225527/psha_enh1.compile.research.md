## MCER and ELastic Design Spectra (ASCE) {#sec-mcer}

Seismic demand for all Risk Categories I-IV was derived in accordance with **ASCE/SEI 7-22**---as adopted by **IBC 2021**---using the site-specific uniform-hazard spectrum (UHS) established in the preceding chapter. Chapter 11 of ASCE 7 permits replacement of mapped spectral accelerations by values obtained from a probabilistic hazard analysis coupled with site-response modelling, provided the procedures of §11.4.7 are satisfied [@ASCE722 §11.4.7].


Chapter §11.4.7 indicates that to perform a site response analysis and a ground motion hazard analysis to determine ground motions for any structure, procedures of sections §21.1 and §21.2 must be applied.


When the procedures of either Section §21.1 or §21.2 are used, the design response spectrum shall be determined in accordance with Section §21.3, and the design acceleration parameters shall be determined in accordance with Section §21.4.


The probabilistic spectral response accelerations shall be taken as the spectral response accelerations in the direction of maximum horizontal response represented by a 5% damped acceleration response spectrum that is expected to achieve a 1% probability of collapse within a 50-year period. If the spectral response accelerations predicted by the ground motion models do not represent the maximum response in the horizontal plane, then the response spectral accelerations computed from the hazard analysis shall be scaled by factors to increase the motions to the maximum response. If the ground motion models predict the geometric mean or similar metric of the two horizontal components, then the scale factors shall be 1.2 for periods less than, or equal to, 0.2 s, 1.25 for a period of 1.0 s, and 1.3 for periods greater than or equal to 10 s; linear interpolation between these period-anchored values is specified in §21.1, and is applied in log-period space consistent with standard spectral analysis convention [@Ref001].


Consistent with §21.3, the **design-level spectral accelerations** are obtained by scaling the MCER ordinates by the factor $2/3$ [@ASCE722 Eq. 21.3-1]:


$$
S_{a}=\frac{2}{3}S_{aM}
$$

When a site-specific procedure is used to determine the design ground motion, the design acceleration parameters are calculated as [@ASCE722 §21.4]:


$$
S_{DS} = 0.9 \max_{T\,\in\,[0.2,\,5\,\text{s}]} S_a(T)
$$ $$
S_{D1} = \max\!\left(0.9\max_{T\,\in\,[1,\,T^*]\,\text{s}} \left[T \cdot S_a(T)\right],\quad
S_a(1\,\text{s})\right)
\quad \text{where} \quad
T^* = \begin{cases} 2\,\text{s} & \bar{v}_s > 442\,\text{m/s} \\ 5\,\text{s} & \bar{v}_s \leq
442\,\text{m/s} \end{cases}
$$

The spectral response acceleration parameter at short periods ($S_{MS}$) and the spectral response acceleration parameter at a period of 1 s ($S_{M1}$) correspond to the MCER-level demands and are recovered from the design-level parameters by inverting the two-thirds scaling relationship:


$$
S_{MS}= 1.5\,S_{DS}, \qquad
S_{M1}=1.5\,S_{D1}
$$

Three international frameworks govern the seismic design of tailings storage facilities (TSFs): the Global Industry Standard on Tailings Management [@gistm2020], the Canadian Dam Association guidelines [@cda2021], and the Australian National Committee on Large Dams [@ancold2019]. Each framework defines performance objectives and design earthquake criteria on the basis of two factors: the consequence classification of the facility and its lifecycle phase. Consequence classification reflects the potential severity of a dam failure, assessed through population at risk (PAR), anticipated loss of life, and the magnitude of environmental and socio-economic impacts. All three standards define consequence classes ranging from Low to Extreme, with progressively more stringent seismic criteria as the consequence class increases. The classification criteria and corresponding design earthquake annual exceedance probabilities (AEPs) for each standard are tabulated in Appendix [-@sec-criteria_appendix] (Tables [-@tbl-gistm], [-@tbl-cda], and [-@tbl-ancold]).


For a given consequence class, the applicable design earthquake also varies by lifecycle phase. Each phase of a TSF's life -- construction, operation, closure, and post-closure -- presents distinct engineering conditions and risk profiles. The design ground motions presented in this chapter are organized into three stages corresponding to the principal design earthquake levels: operational (OBE), closure (SEE), and post-closure (PCE). The assignment of AEPs to each stage differs between standards and is most differentiated by consequence class during operations, where AEPs range from 1/100 to 1/10,000 depending on standard and consequence class (Tables [-@tbl-gistm], [-@tbl-cda], [-@tbl-ancold]). During post-closure, this differentiation collapses: all three frameworks require convergence to the most stringent criterion -- the Maximum Credible Earthquake (MCE) or the 1/10,000-year event -- irrespective of the original consequence class.


The approaches differ in structure. Under GISTM [-@gistm2020], a single earthquake design ground motion (EDGM) is specified for each consequence class and phase; the MCE must also be evaluated and governs if it produces higher demand than the probabilistic criterion. Importantly, GISTM applies the same AEPs during operations and active closure, with a step increase to a uniform 1/10,000 AEP for all consequence classes only at passive closure (Table [-@tbl-gistm]). CDA [-@cda2021] employs the Safety Evaluation Earthquake (SEE) as the design basis, with the MCE applied as an upper bound for high-consequence facilities; AEPs are progressively tightened from operations through closure, and risk-based approaches may be permitted for lower consequence classes during transitional closure phases, provided that post-closure requirements are ultimately satisfied (Table [-@tbl-cda]). ANCOLD [-@ancold2019] applies a dual-level methodology, assigning a uniform Operating Basis Earthquake (OBE) of approximately 1/500 AEP across all consequence categories during operations, with a Safety Evaluation Earthquake (SEE) that varies from 1/1,000 to 1/10,000 depending on consequence class; the most severe criteria (MCE or 1/10,000-year event, 85th percentile) are mandated for Extreme-class facilities and required for all dams prior to abandonment (Table [-@tbl-ancold]).


### Construction

Tailing deposits are frequently constructed in stages, with embankments raised incrementally. Seismic stability during construction is a critical consideration, as the dam may be at partial height or incomplete strength. Even with a low probability of major earthquake occurrence during the relatively brief construction phase, the potential consequences of a moderate event on an incomplete dam can be severe. Accordingly, design requirements stipulate that temporary factors of safety under seismic loading must be satisfied at all construction stages. Initial and intermediate dam stages are analyzed for at least OBE-level events; for facilities with high consequence classifications or in high-seismicity regions, SEE criteria may also be applied. Temporary material properties and geometries are used in analyses, with design iterations as the dam evolves. The CDA Technical Bulletin: Application of Dam Safety Guidelines to Mining Dams [@cda2014] recommends explicit consideration of seismic hazards at every project phase, supported by independent review at critical milestones [@Ref002]. Construction methods and schedules are adjusted as needed to maintain seismic safety, including limiting impounded water volumes or avoiding vulnerable states during periods of heightened seismic risk.


### Operation (Active Life)

During operations, when the facility contains large volumes of tailings and water, the risk profile is at its highest and the design earthquake criteria are most differentiated by consequence class. Under GISTM, operational AEPs range from 1/200 for Low-consequence facilities to 1/10,000 for Extreme (Table [-@tbl-gistm]); CDA spans 1/100 to 1/10,000 (Table [-@tbl-cda]); and ANCOLD assigns a uniform OBE at 1/500 AEP with an SEE that varies from 1/1,000 to MCE or 1/10,000 by consequence category (Table [-@tbl-ancold]). The dam must safely withstand the OBE without operational interruption and must not release tailings under the SEE. Water management is integral -- adequate freeboard must be maintained to accommodate seismic settlement, wave run-up, or ground deformations. For high or extreme consequence dams, design includes provision for concurrent storm and seismic loading, in line with ANCOLD and international practice. Operational seismic readiness is maintained through regular surveillance (crack/deformation monitoring) and emergency response planning. Engineering features -- such as buttresses, drainage to control pore pressures, and control of loose, saturated zones -- can enhance seismic performance. If an OBE is exceeded, post-event inspection and prompt repairs are required to restore the safety margin.


### Closure and Post-Closure

After the cessation of operations, TSFs are expected to remain physically stable for the indefinite future, in the absence of active management. Design for closure and post-closure is based on the principle that the probability of a rare seismic event approaches certainty over an infinite time horizon. The three frameworks handle the transition differently. Under GISTM, the same consequence-dependent AEPs that govern operations continue through active closure; only at passive closure does a uniform 1/10,000 AEP apply to all consequence classes (Table [-@tbl-gistm]). CDA progressively tightens criteria: facilities classified as High or above must already meet 1/10,000 AEP at the closure stage, while lower classes transition from their operational levels toward more conservative values; all facilities must converge to 1/10,000 AEP or MCE before abandonment (Table [-@tbl-cda]). ANCOLD mandates reassessment of all facilities under Extreme-class criteria (MCE or 1/10,000 AEP, 85th percentile) prior to abandonment (Table [-@tbl-ancold]).


Closure design is typically more stringent than operational design for lower consequence facilities. Rehabilitation measures (flattened slopes, reinforcements, erosion protection) may be implemented to achieve maintenance-free performance. Permanent spillways are designed for probable maximum floods, eliminating reliance on operational water management. Post-closure stability analyses must explicitly account for the degradation of temporary features. Components not expected to persist (e.g., geomembranes) are excluded from the long-term stability evaluation; the residual embankment must independently resist seismic loading. Long-term factors of safety are typically higher, and materials (cemented tailings, stabilizing berms) may be specified to enhance seismic resilience.


---
reference-location: section
link-citations: true                   # make in-text cites clickable
---


Probabilistic seismic hazard analysis (PSHA) aggregates the contributions of all plausible earthquake scenarios, obscuring the specific combinations of magnitude ($M$), source-to-site distance ($R$), and ground-motion residual ($\varepsilon$) that control site hazard. **Hazard disaggregation** quantifies the relative contribution of each scenario class---binned by magnitude $m_k$, distance $r_j$, and residual $\varepsilon_\ell$---to the annual frequency of exceedance at a specified ground-motion threshold $i^*$ [@Bazzurro1999].


Disaggregation is performed at a target hazard level, defined by an annual exceedance probability or return period. This produces conditional probability distributions over scenario bins and identifies controlling scenario parameters responsible for site hazard [@Kramer1996]. The ground-motion exceedance probability and total annual exceedance rate are defined in the hazard analysis (see [@eq-hazard-integral], [@eq-epsilon-star]). The joint exceedance rate for scenario $(m_k, r_j, \varepsilon_\ell)$ from source $s$ is given in [@eq-disagg-rate], where $\phi$ is the standard normal probability density function and $\mathbf 1_{{\cdot}}$ is the indicator function. Integration over $\varepsilon$ yields the two-dimensional ($M$-$R$) formulation. Partitioning parameter space into magnitude bins $m_k$, distance bins $r_j$, and residual bins $\varepsilon_\ell$, the contribution from bin $(k,j,\ell)$ is in [@eq-disagg-bin].


$$
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)} =
\mathbf 1_{\{\varepsilon\ge\varepsilon^{*}(m_k,r_j)\}}
\,
\phi(\varepsilon)\,
f_{M,s}(m_k)\,
f_{R|M,s}(r_j|m_k)\,
\nu_{s},
$${#eq-disagg-rate}

$$
\lambda_{k,j,\ell}(i^{*})=
\sum_{s=1}^{N_{S}}
\int_{m_k}
\int_{r_j}
\int_{\varepsilon_\ell}
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)}
d\varepsilon\,dr\,dm
$${#eq-disagg-bin}

The conditional probability that exceedance of $i^*$ is produced by bin $(k,j,\ell)$ is given by [@eq-disagg-prob]. The **modal scenario** is the $(k,j,\ell)$ bin for which $\theta_{k,j,\ell}(i^{*})$ attains its maximum. Hazard disaggregation applies Bayes' theorem to the joint distribution of scenario parameters and ground-motion exceedance as in [@eq-disagg-prob]. The marginal distribution for $\varepsilon$ quantifies the proportion of exceedance attributable to median or above-median ground-motion residuals. Marginal probabilities are obtained by double summation over the other indices as in [@eq-disagg-marginal-M], [@eq-disagg-marginal-R], [@eq-disagg-marginal-eps]:


$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}] = \theta_{k,j,\ell}=
\frac{\lambda_{k,j,\ell}(i^{*})}{\lambda_{I}(i^{*})},
\qquad
\sum_{k}\sum_{j}\sum_{\ell}\theta_{k,j,\ell} = 1
$${#eq-disagg-prob}

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-M}
$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-R}
$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{k,j,\ell}
$${#eq-disagg-marginal-eps}

Disaggregation provides a data-driven basis required for rigorous scenario selection in engineering analysis. The *modal scenario* and the highest-probability bins identified through disaggregation correspond to the earthquake characteristics most responsible for exceedance at the design ground-motion level.


Probabilistic Seismic Hazard Analysis (PSHA) is a methodology that quantifies earthquake ground-motion hazard at a site in terms of probabilities, by integrating over all possible earthquakes that could affect the site [@Cornell1968; @McGuire2004]. Unlike deterministic approaches that focus on a single scenario, PSHA considers the full range of magnitudes, locations, and associated ground motions, providing a comprehensive description of the rate at which various levels of shaking may be exceeded. In probabilistic seismic hazard analysis (PSHA), the annual frequency (rate) of exceeding a ground-motion level at a site is obtained by integrating over all possible earthquake scenarios. For a single seismic source $(s)$ with an annual occurrence rate of earthquakes (above a minimum magnitude $M_{\min}$) denoted $\nu_{0}^{(s)}$ (where $\nu_{0}^{(s)} = N(M_{\min})^{(s)}$), the rate of exceedance of a ground-motion level $i^*$ (e.g., a peak ground acceleration or spectral acceleration) is defined in [@eq-hazard-integral], where $m$ is earthquake magnitude, $\mathbf r$ is the source-to-site distance, $f_{M,s}(m)$ and $f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)$ are the probability density functions describing the distribution of magnitudes and distances for source $(s)$, and $P\left[I > i^* \mid M=m,\,\mathbf r\right]$ is the conditional probability that the ground-motion parameter $I$ exceeds level $i^*$ given an event of magnitude $m$ at distance $\mathbf r$. $M_{\max}^{(s)}$ is the maximum considered magnitude for source $(s)$, which is related to the maximum credible earthquake (MCE) of that source.


$$
\lambda_I(i^*)^{(s)} \;=\;
\nu_{0}^{(s)}
\int_{M_{\min}}^{M_{\max}^{(s)}} \int_{D}
P\left[ I > i^* \,\big|\, m, \mathbf{r} \right]\;
f_{M,s}(m)\;
f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)\;
\mathrm d\mathbf{r}\,\mathrm dm
$${#eq-hazard-integral}

The probability density functions (PDF) $f_{M,s}(m)$ and $f_{\mathbf{R}\mid M,s}(\mathbf{r}\mid m)$ describe the normalized distributions of earthquake magnitudes and locations within source $(s)$. This formulation is a direct application of the total-probability theorem in continuous form, integrating over all magnitudes and locations of earthquakes from source $(s)$ that could contribute to exceedance of level $i^*$. All *aleatory variability* in earthquake occurrence, earthquake size, earthquake location, and ground motion is thus accounted for through the integration [@McGuire2004; @Baker2021]. If multiple seismic sources contribute to the hazard at the site, the total annual exceedance rate $\lambda_I(i^*)$ is obtained by summing the contributions from all sources as in [@eq-hazard-sum]. Assuming $N_S$ independent sources, each with its own occurrence rate and distributions as above, the overall exceedance frequency for level $i^*$ is given by [@eq-hazard-sum], where $\lambda_I(i^*)^{(s)}$ is evaluated for each source via the hazard integral. This linear superposition is valid under the assumption that earthquake occurrences in different sources are independent (typically modeled as independent Poisson processes). The result is a seismic-hazard curve that quantifies the rate at which various ground-motion levels are exceeded at the site.


$$
\lambda_I(i^*) \;=\; \sum_{s=1}^{N_S} \lambda_I(i^*)^{(s)}
$${#eq-hazard-sum}

The GMPE thus enters PSHA through both its median prediction $\hat{\eta}_I$ and its total standard deviation $\sigma_{\ln I}$: small differences among competing GMPEs in either quantity can produce substantial differences in computed exceedance rates, particularly at long return periods where the hazard integral weights the upper tail of the log-normal distribution at several standard deviations above the median [@OpenQuakeEngine].


The annual exceedance frequency $\lambda_I(i^*)$ obtained from the hazard integral [@eq-hazard-integral] can be interpreted as the mean number of times per year that intensity $i^*$ is exceeded. If exceedance events follow a Poisson process in time (a standard assumption in PSHA, owing to the Poissonian occurrence of earthquakes), then the probability of at least one exceedance in a single year is defined in [@eq-aep]^[For small $\lambda_{I}$ (hazard levels of practical interest are usually low probability), $P_{1\text{yr}} \approx \lambda_{I}$ (since $e^{-\lambda} \approx 1-\lambda$)].


$$
P_{1\text{yr}}[I > i^*] = 1 - \exp[-\lambda_I(i^*)] = \text{AEP}
$${#eq-aep}

By extension, the probability of exceedance in $T$ years is $P_{T}(I > i^*) = 1 - \exp[-\lambda_I(i^*) T]$ assuming stationarity and independence year-to-year. This relation allows conversion between a mean annual rate and a probability over $T$ years^[A common case is $T=50$ years (an approximate lifespan of structures); for example, if $\lambda_I(i^*) = 0.0021$ per year, then $P_{50}(I>i^*) = 1 - \exp(-0.0021 \times 50) \approx 0.10$, i.e. a 10% probability in 50 years.]. The **return period** $T_R$ (or **mean return interval**) is a statistical average defined as the reciprocal of the annual frequency of exceedance, usually expressed in years $T_R = \frac{1}{\lambda_I(i^*)}$^[For low probabilities, return period is approximately the inverse of AEP as well, since $\text{AEP} \approx \lambda_{I}$ for small $\lambda_{I}$.]


---
reference-location: section
link-citations: true
---


Near-surface geology modifies seismic waves as they propagate from bedrock to the ground surface. Soft soils amplify ground motion at intermediate-to-long periods while potentially deamplifying short-period motion through nonlinear strain effects; stiff rock sites transmit near-bedrock intensity levels with minimal modification [@Baker2021]. In probabilistic seismic hazard analysis, site effects can be incorporated through two mechanisms: (1) the site term embedded within ground-motion prediction equations (GMPEs), in which the median prediction and aleatory variability are functions of $V_{S30}$, or (2) an external amplification model applied to a reference-rock hazard curve [@Stewart2020]. The first mechanism is ergodic by construction---the empirical site term averages over many recording sites globally and may not capture conditions at a specific site or region. The second mechanism allows regionally calibrated amplification that accounts for nonlinear soil behavior as a function of shaking intensity. This assessment employs both approaches and selects the controlling (maximum) spectral ordinate for each period and hazard level to ensure that the design spectrum is not governed by whichever model happens to be less conservative at a given period.


Site effects were introduced in the probabilistic seismic hazard analysis through two complementary models. The first used an ergodic ground-motion framework in which a logic tree of $V_{S30}$-dependent GMPEs was evaluated for shear-wave velocities ranging from 200 m/s to 1100 m/s. For every branch, OpenQuake computed spectral accelerations $S_a(T_n, V_{S30})$ at the required service levels. Epistemic uncertainty was represented by the branch weights prescribed in the logic tree, and aleatory variability followed the total standard deviation of each GMPE. Because the site term is embedded empirically within the GMPEs, the resulting uniform-hazard spectra remain ergodic.


The second model is an amplification model based on a reference-rock hazard curve at $V_{\mathrm{ref}} = 760\,\text{m/s}$ and transforms it to the target condition $V_{S30}$ by applying period-dependent, nonlinear amplification factors $F(T_n, V_{S30})$, according to [@eq-site-af]. The amplification model follows the formulation of Stewart and co-authors, which expresses $F$ as a log-normal random variable whose mean $\eta_{F\mid\mathrm{PGA}}\!\left(T_n, V_{S30}\right)$ and dispersion $\sigma_{\ln F}$ depend on oscillator period, shear-wave velocity, and input PGA [@Stewart2020; @Hashash2020]. For $V_{S30} < V_{\mathrm{ref}}$, the model captures nonlinear deamplification at short periods and amplification at intermediate-to-long periods; for stiffer sites, the amplification asymptotically approaches unity. Formally, the amplification factor is modeled as a lognormal random variable [@eq-site-lnf]:


$$
\ln F \sim \mathcal{N}\!\left(\mu_{\ln F},\; \sigma_{\ln F}^2\right)
$${#eq-site-lnf}

where $\mu_{\ln F}$ is the conditional mean of the log-amplification factor and $\sigma_{\ln F}$ is the total aleatory standard deviation, both for a given ($V_{S30}$, $T_n$, $pga^*$). The mean $\mu_{\ln F}$ decomposes additively into three period-dependent terms [@Stewart2020]: a reference-condition adjustment $F_{760}$ that bridges the difference between the 760 m/s and 3000 m/s reference horizons, a linear site term $F_V$ that scales with $V_{S30}$ relative to the reference velocity, and a nonlinear factor $F_{nl}$ that captures PGA-dependent soil deamplification at high strain levels. Similarly, the total dispersion decomposes in quadrature [@eq-site-sigma-decomp]:


$$
\sigma_{\ln F}^2 = \sigma_{L}^2 + \sigma_{I}^2 + \sigma_{NL}^2
$${#eq-site-sigma-decomp}

where $\sigma_L$ is the linear site-term dispersion (dependent on $V_{S30}$ and period), $\sigma_I$ is the inter-reference dispersion (nonzero only when $V_{\mathrm{ref}} = 3000\,\text{m/s}$), and $\sigma_{NL}$ is the nonlinear dispersion (dependent on $V_{S30}$ and $pga^*$). All components are period-dependent and tabulated in the published model [@Stewart2020]. The detailed functional forms and calibration of each component are documented in [@sec-site_model].


$$
S_a\!\left(T_n, V_{S30}\right) = F\!\left(T_n, V_{S30}\right)\,S_a\!\left(T_n, V_{\mathrm{ref}}\right).
$${#eq-site-af}

For each return period $T_R$, oscillator period $T_n$, fractile $p$, and site class $V_{S30}$, the design spectral ordinate is defined as the maximum across the GMPE-based and amplification-based estimates [@eq-site-envelope]:


$$
S_a^{\mathrm{max}}(T_n, V_{S30}) = \max\!\left\{S_a^{\mathrm{GMPE}}(T_n, V_{S30}),\; S_a^{F}(T_n, V_{S30})\right\}
$${#eq-site-envelope}

where $S_a^{\mathrm{GMPE}}$ is the spectral ordinate obtained from the GMPE logic tree evaluated directly at the target $V_{S30}$, and $S_a^{F}$ is the spectral ordinate obtained by applying the amplification factor $F$ to the reference-rock hazard curve per [@eq-site-af]. This envelope ensures that the controlling (most hazardous) estimate governs the design spectrum at every period. GMPEs may underpredict at certain periods or $V_{S30}$ ranges where their empirical site terms are poorly constrained by the underlying strong-motion database, while the amplification model may underpredict where the reference-rock hazard curve does not fully represent near-field or source-specific effects. The envelope eliminates the risk of unconservative design by selecting the larger ordinate at each spectral period.


## Site Classification {#sec-vs30_appendix}

The **Vs30** parameter is widely measured in the field using methods such as borehole logging, seismic cone penetration tests, and surface wave techniques. Introduced into engineering practice in the early 1990s, it provides a simple, robust metric to characterize site conditions for earthquake ground motions. **Vs30** is defined as the time-averaged shear-wave velocity in the upper 30 meters of a site profile. In practical terms, it represents the overall stiffness of the near-surface soils and rock. Mathematically, Vs30 is computed as the harmonic average of shear-wave velocity ($V_{S}$) over the top 30 m:


$$
V_{S30} = \frac{30\,\text{m}}{\sum_{i=1}^{N}\frac{H_i}{V_{S,i}}}
$$

where $H_i$ and $V_{S,i}$ are the thickness and shear-wave velocity of the $i$-th layer in the upper 30 m. This formula gives the equivalent uniform velocity that yields the same travel time through 30 m of material as the actual layered profile.


Vs30 has become the primary quantitative predictor of site effects in modern ground-motion models. Virtually all recent ground motion prediction equations (GMPEs) incorporate Vs30 as a key input parameter to adjust predicted shaking for site conditions. Empirical GMPEs (e.g., NGA-West2 and NGA-East) often use a functional form in which the median ground motion is scaled according to $\ln(V_{S30})$ or a similar proxy, with separate terms for linear scaling and nonlinear saturation at low velocities. Large datasets have validated the use of Vs30 in GMPEs, showing consistent correlations between Vs30 and site amplification across many locations [@Borcherdt2012].


In parallel, site-specific analyses (such as 1D site response simulations) rely on Vs30 as an initial classification of the site profile, although they incorporate the full shear-wave velocity profile with depth. While Vs30 does not capture all facets of site response -- such as basin depth or resonance effects -- it serves as a practical first-order proxy.


### NEHRP Site Classes

The NEHRP provisions [-@BSSC2015] established the foundational site classification system used in building codes, defining Site Classes A through F based on Vs30 ranges. The 2020 edition of the NEHRP provisions (FEMA P-2082) introduced a substantially expanded nine-class system -- A, B, BC, C, CD, D, DE, E, and F -- replacing the six-class A-F framework [@Ref003]. Three intermediate classes (BC, CD, DE) were added to provide finer-grained differentiation. Additionally, the 2020 edition requires that site classification be based solely on shear-wave velocity ($V_{S30}$); the 2015 edition allowed SPT blow count and undrained shear strength as alternative classification bases, but this option was removed in FEMA P-2082 [@Ref003]. The 2020 provisions also introduced multi-period response spectra (MPRS), replacing the two-period ($S_S$, $S_1$) spectral shape. ASCE 7-22 and IBC 2021 implement the nine-class system in Table 20.2-1, superseding the six-class A-F boundaries from prior editions [@Ref001]. The approximate Vs30 boundaries for the nine classes are:


* **Site Class A:** Hard rock, $V_{S30} > 1500$ m/s.
* **Site Class B:** Rock, $V_{S30} \approx$ 760-1500 m/s (760 m/s is the B/BC boundary).
* **Site Class BC:** Soft rock, $V_{S30} \approx$ 530-760 m/s (new intermediate class).
* **Site Class C:** Very dense soil or soft rock, $V_{S30} \approx$ 365-530 m/s.
* **Site Class CD:** Dense sand or very stiff clay, $V_{S30} \approx$ 270-365 m/s (new intermediate class).
* **Site Class D:** Stiff soil, $V_{S30} \approx$ 185-270 m/s.
* **Site Class DE:** Loose sand or medium stiff clay, $V_{S30} \approx$ 150-185 m/s (new intermediate class).
* **Site Class E:** Soft clay, $V_{S30} < 150$ m/s (boundary adjusted from 180 m/s in prior editions).
* **Site Class F:** Soils requiring site-specific evaluation (e.g., very soft clays, peats, liquefiable soils, or thick high-plasticity clays).


Class F is defined by qualitative subsoil conditions rather than a $V_{S30}$ threshold; if those conditions are met, a detailed site response analysis is mandated in lieu of using generic amplification factors. In structural design, each non-F class is assigned amplification factors (tabulated in ASCE 7-22 as functions of $V_{S30}$ and ground-motion intensity) that modify the multi-period response spectrum to account for local site effects [@Ref001].


### AS1726 Guidelines

The Australian Standard AS 1726-2017 [-@AS1726-2017] provides guidelines for conducting geotechnical investigations and includes a site classification system that categorises sites into classes based on their soil properties, including the shear wave velocity parameter $\bar{v}_S$, depth to bedrock, and soil type [@Ref004]. AS 1726-2017 works in conjunction with AS 1170.4 "Earthquake Actions on Structures," which prescribes the design ground motions for each site class; the current edition of AS 1170.4 is the 2024 revision, superseding the 2007 edition [@Ref005]. Both standards use site classes A through E plus a special class S for sites requiring site-specific investigation, analogous to NEHRP Class F. In AS 1170.4:2007, $V_{S,30}$ is used explicitly to define the two rock classes: Class A (Strong Rock) requires $V_{S,30} > 1500$ m/s, and Class B (Rock) requires $V_{S,30} > 360$ m/s [@Ref006]. The B/C boundary at 360 m/s is markedly lower than the 760 m/s threshold used in NEHRP/ASCE 7-22. For soil classes, AS 1170.4:2007 uses the estimated site period $T_S$ and soil strength parameters rather than $V_{S,30}$ directly: Class C (Shallow Soil) applies where $T_S \leq 0.6$ s; Class D (Deep or Soft Soil) applies where $T_S > 0.6$ s; and Class E (Very Soft Soil) is defined by more than 10 m of soil with $V_S < 150$ m/s or undrained shear strength $s_u < 12.5$ kPa [@Ref007].


{{< include /psha/_tbl/AS1726.qmd >}}

### ASCE/SEI 7-22 Guidelines

The ASCE/SEI 7-22 Standard [-@ASCE722] provides guidelines for conducting geotechnical investigations and includes a site classification system that categorises sites into classes based on their soil properties, such as shear wave velocity, depth to bedrock, and soil type. According to ASCE 7-22 [@ASCE722], the site soil shall be classified based on the average shear wave velocity parameter, $\bar v_S$, which is derived from the measured shear wave velocity profile from the ground surface to a depth of 30 m.


{{< include /psha/_tbl/ASCE722.qmd >}}

### NBC-2020 Guidelines

The National Building Code of Canada [-@NBC2020] provides guidelines for site characterization and seismic site response. NBC 2020 classifies sites into categories A through F using average shear wave velocity $v_{S30}$, standard penetration test (SPT) blow count $N_{60}$, and undrained shear strength $s_{u}$ as complementary classification bases [@Ref008][@Ref009]. The $v_{S30}$ thresholds are: Class A (Hard Rock, $v_{S30} > 1500$ m/s), Class B (Rock, 760-1500 m/s), Class C (Very Dense Soil or Soft Rock, 360-760 m/s), Class D (Stiff Soil, 180-360 m/s), and Class E (Soft Soil, approximately $v_{S30} < 180$ m/s), closely mirroring the NEHRP framework. Class F covers soils requiring site-specific investigation (liquefiable soils, sensitive or quick clays, deep soft clays, and highly plastic clays). A key innovation in NBC 2020 is the shift from tabulated class-based amplification factors ($F_a$, $F_v$) to a direct $v_{S30}$-based hazard lookup using Canada's 6th-generation seismic hazard model, which delivers hazard curves as a continuous function of $v_{S30}$ over the range 140-3000 m/s; a site designation $X_V$ allows specifying a measured in-situ $v_{S30}$ directly, while $X_S$ uses a class letter [@Ref010][@Ref011].


{{< include /psha/_tbl/NBC2020.qmd >}}
