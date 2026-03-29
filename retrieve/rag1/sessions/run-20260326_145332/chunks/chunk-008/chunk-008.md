$$f_M(m \mid M_{\min} \leq m \leq M_{\max}) = \frac{\beta\,e^{-\beta(m - M_{\min})}}{1 - e^{-\beta(M_{\max} - M_{\min})}} \tag{4.9}$$

A plot of $f_M(m)$ for a fault with $M_{\min} = 5$ and $M_{\max} = 7.5$ is shown with a dashed line in Figure 4.10a.

**Maximum Magnitude Model:** Some faults appear to generate earthquakes only within a relatively narrow magnitude range involving full‑segment ruptures [@Allen1968][@WesnouskyEtAl1983]. Such faults include certain segments of the San Andreas fault (e.g., the North Coast segment, which last ruptured in 1906 [@HillEtAl1990]; and the Cholame, Carrizo, and Mojave segments, which last ruptured in 1857 [@HaukssonEtAl2012]) and portions of the Wasatch fault in Utah [@ArabaszEtAl1980]. Such atypical behavior on major faults may result from the last major event on the fault having ruptured to unusually large depth, into the ductile zone in the upper mantle [@JiangLapusta2016]. This behavior can be described using the maximum magnitude model [@WesnouskyEtAl1983], which consists of a truncated normal distribution for $f_M(m)$, with cutoff magnitudes of $M_{\min}$ and $M_{\max}$, mean magnitude of $M_{\max}$, and a standard deviation of $\sigma_m$. The CDF and PDF for this model are given by:

*FIGURE 4.10 PDFs for magnitude, $f_M(m)$; (a) truncated exponential and characteristic, (b) maximum magnitude.*

$$F_M(m \mid M_{\min} \leq m \leq M_{\max}) = \frac{F_Z(Z) - F_Z(Z_{\min})}{F_Z(Z_{\max}) - F_Z(Z_{\min})}$$

$$f_M(m \mid M_{\min} \leq m \leq M_{\max}) = \frac{\exp\!\left[-\dfrac{(m - M_{\max})^2}{2\sigma_m^2}\right]}{\sigma_m\sqrt{2\pi}\,[F_Z(Z_{\max}) - F_Z(Z_{\min})]} \tag{4.10a}$$

where $F_Z(Z)$ represents the CDF of the standard normal distribution (Table D.1), with the standard normal variate as used in Equation (4.10a) defined as

$$Z = \frac{m - M_{\max}}{\sigma_m}, \quad Z_{\min} = \frac{M_{\min} - M_{\max}}{\sigma_m}, \quad Z_{\max} = \frac{M_{\max} - M_{\max}}{\sigma_m} \tag{4.10b}$$

The model is depicted in Figure 4.10(b) for $M_{\max} = 7.0$, $\sigma_m = 0.2$, and truncation limits set at $\pm 2\sigma_m$ from the mean, i.e., $M_{\min} = 6.6$ and $M_{\max} = 7.4$.

**Hybrid Models:** The Gutenberg‑Richter law implies that individual faults should produce an exponential distribution of magnitudes and, hence, an exponential distribution of fault offsets. However, paleoseismic investigations using fault trenching have shown that points on individual faults and fault segments tend to displace by similar amounts in successive earthquakes. These observations suggest that individual large active faults repeatedly generate earthquakes of similar (within about one‑half magnitude unit) size, known as characteristic earthquakes [@SchwartzCoppersmith1984][@Schwartz1988]. By dating these characteristic earthquakes, their historical rate of recurrence can be estimated. Geologic evidence indicates that characteristic earthquakes occur more frequently than would be implied by extrapolation of the Gutenberg‑Richter law from high exceedance rates (low magnitudes) to low exceedance rates (high magnitudes). The result is a more complex recurrence law that is governed by seismicity data at low magnitudes and geologic data at large magnitudes, as shown in Figure 4.11. These are referred to as hybrid recurrence relations because they combine different functional forms for the magnitude PDF at low and high magnitudes.

*FIGURE 4.11 Inconsistency of mean annual rate of exceedance ($N_m$) as determined from seismicity data and geologic data. (After Youngs and Coppersmith, 1985.)*

Youngs and Coppersmith (1985) [@YoungsCoppersmith1985] developed a hybrid PDF for $f_M(m)$ that combines a truncated exponential magnitude distribution at low magnitudes with a uniform distribution in the vicinity of the characteristic earthquake. This distribution is shown in Figure 4.10a, where $\Delta M_c$ is the increment of uniform probability density associated with the characteristic earthquake (generally taken as 0.5), and $\Delta M_1$ is the magnitude offset between the lower bound of the characteristic earthquake and the portion of the truncated exponential model having the same probability density. The CDF of this distribution can be expressed as [@ConvertitoEtAl2006]:

$$F_M(m \mid M_{\min} \leq m < M_{\max} - \Delta M_c) = \frac{1 - e^{-\beta(m - M_{\min})}}{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)} + C\,\Delta M_c} \tag{4.11a}$$

$$F_M(m \mid M_{\max} - \Delta M_c \leq m \leq M_{\max}) = \frac{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)} + C\,(m - (M_{\max} - \Delta M_c))}{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)} + C\,\Delta M_c}$$

where $C$ is a constant defined by

$$C = \frac{\Delta M_c\,\beta\,e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)}}{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)}}$$

Differentiating $F_M(m)$ yields the PDF

$$f_M(m \mid M_{\min} \leq m < M_{\max} - \Delta M_c) = \frac{\beta\,e^{-\beta(m - M_{\min})}}{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)} + C\,\Delta M_c} \tag{4.11b}$$

$$f_M(m \mid M_{\max} - \Delta M_c \leq m \leq M_{\max}) = \frac{C}{1 - e^{-\beta(M_{\max} - M_{\min} - \Delta M_c)} + C\,\Delta M_c}$$

Other approaches for hybrid modeling of major active faults use a maximum magnitude model (truncated normal distribution) for the characteristic earthquake coupled with a truncated exponential model for smaller magnitudes (e.g., [@FieldEtAl2009][@FieldEtAl2014]).

### 4.2.2.5 Rate of Earthquake Recurrence

Two philosophies are available for modeling the rate of earthquake recurrence. The time‑independent approach assumes that earthquakes occur as a Poisson process, which in turn assumes that the occurrence of an event (excluding foreshocks and aftershocks) has no influence on the timing of future events. Alternatively, the time‑dependent approach holds that the occurrence of an event releases stress on the fault and thus temporarily reduces the rate of future earthquakes (excluding aftershocks). The processes by which rates of earthquake occurrence are derived using these approaches are described below.

**Time‑Independent Models:** Earthquake recurrence has most commonly been expressed using the time‑independent Poisson model. As described in Section D.7.1.2, the Poisson model provides a simple framework for evaluating probabilities of events that can be represented by a Poisson process in which the occurrence of events in any given time interval is independent of events in other time intervals. The key parameter in the Poisson model is the mean annual rate of occurrence of events. As described in Section 4.2.2.3, the mean annual rate of exceedance, $\lambda_m$, is defined as the rate of occurrence of events with magnitude $> m$. This rate can be defined using a fully empirical approach or a moment balance approach.

As described in Section 4.2.2.3, the empirical approach involves collecting available earthquake magnitude data and computing earthquake rates as a function of magnitude. Such data are typically observed to follow the Gutenberg‑Richter law. However, it should be recognized that the observation period may be inadequate to accurately determine the rates of infrequent large magnitude events, which are often critical for engineering design. Nonetheless, this approach is widely used in seismically active areas where fault source information may be unavailable within regions having long historical records such as southern Europe [@BasiliEtAl2008] and Japan [@PaganiEtAl2016].

In the moment balance approach, the Poisson rate of earthquake occurrence on a given fault can be computed based on the seismic moment (Section 2.8.1) if the slip rate, $\dot{s}$, is known and a magnitude distribution model, $f_M(m)$, is selected. Differentiating Equation (2.2) with respect to time, the rate of moment build‑up on the fault during periods without earthquakes is

$$\dot{M}_0 = \mu A_s \dot{s} \tag{4.12}$$

For non‑hybrid fault models, the rate of moment release is calculated as

$$\dot{M}_0 = \lambda_{M_{\min}} \int_{M_{\min}}^{M_{\max}} M_0(m)\,f_M(m)\,dm \tag{4.13}$$

where $\lambda_{M_{\min}}$ is the Poisson rate of occurrence of earthquakes with $m > M_{\min}$ and $M_0$ indicates seismic moment. The integral in Equation (4.13) represents the mean moment release for future earthquakes in the magnitude range of $M_{\min}$ to $M_{\max}$. The seismic moment, $M_0$, can be related to $m$ by rearranging Equation (2.3) as

$$M_0 = 10^{1.5m + 16.05} \tag{4.14}$$

Assuming that the seismic moment that builds up over time is eventually released in the form of earthquakes, the long‑term rate of moment build‑up must be equal to the rate of moment release. Setting Equations (4.12) and (4.13) equal, $\lambda_{M_{\min}}$ can be readily calculated.

When a hybrid model for the magnitude PDF is used, the rate of the characteristic earthquake, $\lambda_c$, is typically evaluated from a paleoseismic investigation. A separate rate for the smaller magnitude events, $\lambda_{M_{\min}}$, is computed to cover the magnitude range for the low‑magnitude PDF (e.g., $M_{\min} \leq m < (M_{\max} - \Delta M_c)$ for the Characteristic Earthquake model). In this case, moment build‑up is still evaluated using Equation (4.12), with moment release now evaluated as

$$\dot{M}_0 = \lambda_{M_{\min}} \int_{M_{\min}}^{M_{\max} - \Delta M_c} M_0(m)\,f_M(m)\,dm + \lambda_c \int_{M_{\max} - \Delta M_c}^{M_{\max}} M_0(m)\,f_M(m)\,dm \tag{4.15}$$

The Poisson rate term $\lambda_{M_{\min}}$ is evaluated by equating Equations (4.12) and (4.15).

**Time‑Dependent Models:** The assumption of independence of events inherent in the Poisson model is inconsistent with elastic rebound theory, which holds that some period of time is required for strain energy to build back up on a fault that has just produced an earthquake. A logical extension of this principle is that if a fault section has not produced a large earthquake over a long time horizon, it is more likely to produce a future earthquake. Such seismic gaps, introduced in Section 2.5.1, have produced some notable earthquakes, but whether they necessarily have a higher likelihood of future earthquakes has been a topic of debate [@KaganJackson1991].

To model the time‑variable rate of earthquakes implied by elastic rebound theory, time‑dependent models can be applied that adjust earthquake probabilities during a future time window based on the time elapsed since the previous major earthquake on the fault. These models assign a probability distribution to the time from present until the next occurrence of a major earthquake, $f_T(t)$, where $t$ is the time to the next event. These models are used to update the rate of occurrence of large events such as characteristic earthquakes. Figure 4.12 illustrates the use of $f_T(t)$ to evaluate the rate of a characteristic event, $\lambda_c$, using a time‑dependent model. In the figure, $f_T(t)$ is taken as normal with a mean of $1/\lambda_c$. If $t_e$ years have passed since the last event, a conditional density function $f_T(t \mid t > t_e)$ can be constructed as:

$$f_T(t \mid t > t_e) = \frac{f_T(t)}{1 - F_T(t_e)} \tag{4.16}$$

*FIGURE 4.12 Illustration of PDF for time between earthquakes and its use to evaluate conditional event probability given that time $t_e$ has elapsed since the last event with no activity. Annual rate of characteristic event, $\lambda_c = 1/300$ years.*

where $F_T(t_e)$ is the CDF of time between earthquakes evaluated at time $t_e$. As shown in Figure 4.12, the probability of an event between time $t_e$ and $t_e + \Delta t$, denoted $P_{E,\Delta t}$, is simply the area beneath $f_T(t \mid t > t_e)$ over the time interval $t_e$ to $t_e + \Delta t$. This probability can be computed as

$$P_{E,\Delta t} = \frac{F_T(t_e + \Delta t) - F_T(t_e)}{1 - F_T(t_e)} \tag{4.17}$$

The probability from Equation (4.17) can then be converted to an updated Poisson rate of the characteristic event, $\lambda_{c|t>t_e}$, by manipulation of Equation (D.48) as:

$$\lambda_{c|t>t_e} = \frac{-\ln(1 - P_{E,\Delta t})}{\Delta t} \tag{4.18}$$

This updated rate of characteristic earthquakes can then be used in the same manner as $\lambda_c$ for probabilistic seismic hazard analysis. Field and Jordan (2015) [@FieldJordan2015] derived earthquake probabilities using time‑dependent models for the case where $t_e$ is unknown; interestingly, they found higher probabilities than when time‑independent models were used. This suggests that consideration of $t_e$ is an important aspect of source characterization, even when specific knowledge of $t_e$ is unavailable for a particular source. It should be noted that moment build‑up and release rates must not only balance for individual faults, but cumulative slip rates for all faults in a region should be consistent with regional geodetic and geologic data where such data exists and is reliable. This may require adjustments of slip rates for individual faults [@FieldEtAl2009][@FieldEtAl2014]. This topic is discussed further in Section 4.4.2.

##### 4.3 DETERMINISTIC SEISMIC HAZARD ANALYSIS

In the early years of geotechnical earthquake engineering, the use of deterministic seismic hazard analysis (DSHA) was prevalent. A DSHA involves the development of a particular earthquake scenario upon which a ground motion hazard evaluation is based. The scenario consists of a postulated earthquake of a specified size occurring at a specified location. A typical DSHA can be described as a four‑step process consisting of (modified from [@Reiter1990]):

1. Identification and characterization of all earthquake sources capable of producing significant ground motions at the site. The characteristics of a potential earthquake, which take into consideration source geometry, activity, and magnitude, are developed for each source. For a particular fault, this requires selecting a single magnitude from the appropriate distribution, which will have some associated recurrence rate. Traditionally, the maximum magnitude of each source is selected (e.g., $M_{\max}$ in Figure 4.10), but this may be considered impractical in cases where the maximum magnitude is especially unlikely.

2. Selection of a source‑to‑site distance parameter for each source. The distance parameter(s) must be consistent with that in the GMM used to estimate ground motion characteristics in Step (4) of this procedure. In most DSHAs, the shortest distance between each source and the site of interest is selected.

3. Calculation of ground motions at the site of interest produced by the earthquakes identified in Step (1), which are assumed to occur at the distances identified in Step (2). Ground motions are generally expressed in terms of some IM such as peak acceleration, peak velocity, or spectral acceleration, the values of which are usually computed using GMMs (Section 3.5) for a selected percentile.

4. Identification of the controlling earthquake for the site, typically by comparing ground motions across all considered sources and selecting the one that produces the strongest shaking. The controlling earthquake is described in terms of its size (usually expressed as magnitude) and distance from the site. The ground motion IMs produced by the controlling earthquake define the hazard from a DSHA.

*FIGURE 4.13 Four steps of a deterministic seismic hazard analysis (DSHA).*

The DSHA procedure is shown schematically in Figure 4.13. Expressed in these four compact steps, DSHA appears to be a very simple procedure, and in many respects, it is. When applied to structures for which failure could have catastrophic consequences, such as nuclear power plants and large dams, DSHA is often considered to provide a straightforward framework for the evaluation of "worst‑case" ground motions for the identified scenario. However, a number of subjective decisions that can strongly affect the computed IMs must be made in the DSHA procedure, causing the "worst‑case" condition to be poorly (and often inconsistently) defined. For example, in Step (1), what combination of fault segments should be considered to rupture together for a given source? Referring to the Hayward and Rogers Creek faults shown in Figure 4.6, the worst‑case would require a through‑going rupture involving the SH, NH, and RC segments, even if that combination is extremely unlikely. What magnitude will then be assigned to a particular rupture scenario? As described in Section 4.2.2.2, relationships between fault area and magnitude have uncertainty. If a 95th percentile earthquake (two standard deviations above the mean) was considered, the magnitude would be approximately 0.5 (magnitude units) beyond the mean estimates.

Similarly, in Step (3), GMMs produce a distribution of ground motion IMs for a particular scenario earthquake. As described in Section 3.5.4, IMs are generally considered to be lognormally distributed, which implies that the true "worst‑case" ground motion would be much larger than the median, i.e., that computed from the logarithmic mean. To account for uncertainty in ground motion predictions, DSHAs must select some percentile IM level (often 84th or 95th percentile, which corresponds to one or two logarithmic standard deviations above the logarithmic mean) to characterize the ground shaking from the identified scenario event. If true "worst‑case" conditions are considered, involving multi‑segment through‑going ruptures, the magnitude will correspond to a point on the $f_M(m)$ distribution with a low likelihood and high percentile IMs from the GMM would be used. This can cause the resulting ground motions to be so large that structures cannot be reasonably, let alone economically, designed to resist them. They can also be so strong that the likelihood of their occurrence during the useful lifetime of the structure being designed is miniscule. These factors create pressure to "back off" from the worst‑case scenario, but where and how far to back off is also subjective and inherently arbitrary.

Dealing with the subjectivity inherent to DSHA requires the combined expertise and opinions of seismologists, seismic geologists, engineers, risk analysts, economists, social scientists, and government officials. The broad range of backgrounds and often divergent goals of such professionals can cause difficulty in reaching a consensus on earthquake potential. Over the years there have been many terms used to describe earthquake potential [@Krinitzsky2002]; among them the maximum credible earthquake (MCE), design basis earthquake (DBE), safe shutdown earthquake (SSE), maximum probable earthquake (MPE), operating basis earthquake (OBE), and seismic safety evaluation earthquake. The MCE, for example, is usually defined as the largest earthquake that appears capable of occurring under the known tectonic framework. The DBE and SSE are usually defined in essentially the same way as the MCE. The MPE has been defined as the maximum historical earthquake and also as the maximum earthquake likely to occur in a 100‑year interval. Many DSHAs have used the two‑pronged approach of evaluating hazards for both the MCE and MPE (or SSE and OBE). The Committee on Seismic Risk of the Earthquake Engineering Research Institute (EERI) has stated that terms such as MCE and MPE "are misleading ... and their use is discouraged" [@CommitteeSeismicRisk1984].

One common use of deterministic analysis is to provide a "cap" to ground motions predicted through probabilistic seismic hazard analysis for use in the USGS national seismic hazard model [@LeyendeckerEtAl2000]. Mapped ground motions are based on probabilistic results with a risk adjustment, except in areas where DSHA provides lower values. The outcome of this process is referred to as a risk‑targeted, maximum considered earthquake ground motion, $MCE_R$ [@LucoEtAl2015], with the objective being a 1% probability of structure collapse in 50 years. That objective is not achieved in areas where the $MCE_R$ ground motions are set by deterministic caps, which causes confusion and controversy [@StewartEtAl2020]. The DSHA magnitude for these calculations is based on disaggregations of probabilistic analysis (Section 4.4.3.5). Uncertainty in the ground motion is considered by using an 84th percentile value.

#### Example 4.3

The site shown in Figure E4.3 is located in the vicinity of the three independent, shallow seismic sources shown as Sources 1, 2, and 3. Using a DSHA, compute the peak acceleration considering the 50th percentile (median) ground motions.

**Solution:**

Source zones 1, 2, and 3 are shallow linear, areal, and point sources with the coordinates and maximum magnitudes indicated in the figure. The four‑step procedure for DSHA is applied as follows:

1. The problem statement provides the location and maximum magnitude of each source. In a real DSHA, this is a difficult task.

2. Since the sources are shallow, the source‑to‑site distances are given below. Source 1: 23.7 km; Source 2: 25.0 km; Source 3: 60.0 km.

*FIGURE E4.3 Positions of sources around site for Problem E4.3.*

3. For this example, the peak acceleration is computed using the Campbell (1981) [@Campbell1981] GMM (Equation 3.25). This leads to the ground motions below: Source 1: $M = 6.3$, distance $= 23.7$ km, $\text{PGA} = 0.09\,g$; Source 2: $M = 6.7$, distance $= 25.0$ km, $\text{PGA} = 0.12\,g$; Source 3: $M = 5.0$, distance $= 60.0$ km, $\text{PGA} = 0.01\,g$. On this basis, Source 2 produces the controlling event. Note: Though currently out of date, the Campbell (1981) relationship is used here because of its simplicity.

4. The hazard would be taken as that which results from a magnitude 6.7 earthquake occurring at a distance of 25 km, which produces $\text{PGA} = 0.12\,g$. Other IMs could be obtained from the GMMs described in Chapter 3.

##### 4.4 PROBABILISTIC SEISMIC HAZARD ANALYSIS

Probabilistic seismic hazard analysis (PSHA) provides a framework in which seismic hazards can be computed with consideration of uncertainty in the size and location of earthquakes, their rates of recurrence, and variations of ground motion characteristics for various magnitude and distance combinations. Whereas a DSHA estimates ground motions for a controlling earthquake scenario corresponding to a single magnitude‑distance pair, PSHA‑based ground motions include contributions from all possible combinations of magnitude and distance, and the full range of ground motions that can be produced by each combination, all weighted by their relative likelihoods of occurrence. As such, PSHA avoids the arbitrary choices required in DSHA and provides a more complete and objective representation of seismic hazards.

Understanding the concepts and mechanics of PSHA requires familiarity with some terminology and basic concepts of probability theory. Such background information can be found in Appendix D. The PSHA methodology described in this section is similar in many respects to the well‑established methods developed by Cornell (1968) [@Cornell1968], Esteva (1969) [@Esteva1969], Algermissen et al. (1982) [@AlgermissenEtAl1982], and McGuire (2004) [@McGuire2004]. PSHA can be described as a four‑step procedure (modified from [@Reiter1990]), each of which bears some similarity to the DSHA steps, as illustrated in Figure 4.14.

1. The identification and characterization of earthquake sources is identical to the first step of DSHA, except that the probability distribution and recurrence rates of the full range of earthquake magnitudes that each source is capable of producing must also be characterized. In contrast, a DSHA implicitly assumes a probability of 1.0 for the selected magnitude and 0.0 for all other magnitudes.

*FIGURE 4.14 Four steps of a probabilistic seismic hazard analysis (PSHA).*

2. The probability distribution of potential rupture locations within each source, which controls the distribution of site‑to‑source distances, is considered. In most cases, uniform probability distributions are assigned to hypocenter locations, implying that earthquakes are equally likely to initiate at any point within the source. These distributions are then combined with the source geometry to obtain the corresponding probability distribution of source‑to‑site distances, using the distance measure(s) appropriate for the GMM(s) considered in the next step. DSHA, on the other hand, typically assumes a probability of 1.0 that the portion of the source closest to the site will rupture.

3. The ground motions produced at the site by earthquakes of any size within the applicable range from Step (1), occurring at any possible hypocenter location in each source, are computed, typically with GMMs. The entire distribution of IM estimates from GMMs is considered in a PSHA, whereas a DSHA would typically compute an IM at a single, fixed percentile level.

4. Finally, the uncertainties in earthquake size, earthquake location, and ground motion IMs are combined to obtain the time rate that a specified level of the IM will be exceeded during a particular time period.

The proper performance of a PSHA requires careful attention to the problems of source characterization (Section 4.2.2), IM prediction (Sections 3.5–3.6), and the mechanics of the probability computations. The sections that follow emphasize the implementation of concepts described previously and describe the PSHA computations.

###### 4.4.1 Distributions of Independent Variables Used in GMMs

A fundamental aspect of PSHA is the characterization of the range of input variables used to predict future ground motions for a particular site. In general, the three types of parameters used in ground motion prediction are related to source, path, and site conditions. The principal source parameter is magnitude. In PSHA, an appropriate magnitude distribution, generally selected from among the options in Section 4.2.2.4, is assigned to each source. Site parameters are not variable for a given location (i.e., sites have a certain condition, which does not vary from event‑to‑event in the same manner as source and path effects). The remainder of this section describes variability in the principal path parameter, source‑to‑site distance, as considered in PSHA.

Earthquakes can occur anywhere on a particular fault, so their hypocenters, or nucleation points, are usually assumed to be uniformly distributed across a source (i.e., fault rupture is considered equally likely to initiate at any location). The assumption of uniformity is by no means required; nonuniform distributions may be used (e.g., [@MaiEtAl2005]). A uniform distribution within the source does not, however, often translate into a uniform distribution of source‑to‑site distance. Since GMMs use particular measures of source‑to‑site distance, the spatial uncertainty of earthquake locations must be used to compute the distribution of distance measures. The relative likelihood of realizing different values over the range of possible source‑to‑site distances is represented by a probability density function for distance, $f_R(r)$.

For the point source of Figure 4.15a, the epicentral distance, $R$, is known to be $r_s$; consequently, the probability that $R = r_s$ is assumed to be 1.0 and the probability that $R \neq r_s$ is 0.0. Other cases are not as simple. Consider the case of a linear source that produces earthquakes of zero rupture length (Figure 4.15b). The probability that an earthquake occurs on the small segment of the fault between $L = \ell$ and $\ell + d\ell$ is the same as the probability that it occurs between epicentral distances $R = r$ and $R = r + dr$; i.e.,

$$f_L(\ell)\,d\ell = f_R(r)\,dr \tag{4.19}$$

where $f_L(\ell)$ and $f_R(r)$ are the probability density functions for the variables $L$ and $R$, respectively. Consequently, the distribution of epicentral distance is

$$f_R(r) = f_L(\ell)\,\frac{d\ell}{dr} \tag{4.20}$$

which produces a distribution of the type shown in Figure 4.15b.

Epicentral distance, however, is not a good predictor of IMs because it does not indicate how close the actual rupture is to a particular site of interest. Energy is not released from a single location in an actual earthquake – it is released over some finite fault rupture area and the level of shaking at a particular site depends on how close the site is to the zone of energy release. In the case of the linear source example in Figure 4.15, the applicable fault dimension is rupture length, which is commonly assumed to have a logarithmic mean that is a linear function of magnitude and to have a lognormally distributed error term. One empirical relationship for length distribution for active tectonic regions has a mean of $\log_{10} L_{\text{rup}} = 0.74\,m - 3.55$ (in km) and a standard deviation of $\sigma_{\log_{10}} = 0.23$ [@WellsCoppersmith1994].

*FIGURE 4.15 (a–c) Examples of variations of source‑to‑site distance for different source geometries.*

When the finite size of fault ruptures is considered (e.g., Figure 4.15c), or for more complex source geometries, $f_R(r)$ is replaced with PDFs for the parameters controlling source distance. Consider, for example, the case shown in Figure 4.15c in which the distance measure of interest is the closest distance to the rupture surface, $R_{\text{rup}}$. That distance depends on the position of the midpoint of the ruptured portion of the fault (described by the normalized location, $h$) and the length of the fault rupture, $L_{\text{rup}}$. Taking $r$ as the closest distance from the ruptured portion of the fault to the site, the probability of having a particular value of $r$ is equivalent to the probability of the corresponding values of $h$ and $L_{\text{rup}}$, both of which are defined by PDFs (typically uniform for $h$; log‑normal for $L_{\text{rup}}$).

Since the probability of $r$ is $f_R(r)\,dr$, this can be expressed as:

$$P(R = r) = f_R(r)\,dr = f_{L_{\text{rup}}}(\ell_{\text{rup}})\,d\ell_{\text{rup}} = f_H(h)\,dh \tag{4.21}$$

When using relations like Equation (4.21) in probability calculations, it is important to check that ruptures do not extend beyond the fault dimensions; for the case in Figure 4.15c in which the rupture location is specified at the midpoint, this can be achieved by taking $f_H(h)$ as zero from the ends of the fault to $L_{\text{rup}}/2$ inward from the ends. Randomization of the rupture length relationship turns out to not affect hazard results significantly [@Bender1984], hence some hazard analyses are performed by taking fault geometric parameters as mean values. This would remove the first two terms from the analysis of $f_R(r)\,dr$ in Equation (4.21).

###### 4.4.2 Earthquake Rates

To calculate the probabilities of various hazards occurring in a given time period, the distribution of earthquake occurrence with respect to time must be considered. The probability of earthquake occurrence in a specified time interval is typically modeled with a Poisson process, which assumes that earthquakes occur randomly in time. As described in Sections 4.2.2.3–4.2.2.5, the classical Gutenberg‑Richter recurrence model is equivalent to an exponential magnitude PDF and a Poisson model to express time‑dependence. The Poisson rate in this case represents the rate of earthquakes larger than the minimum magnitude, $\lambda_{M_{\min}}$. Strategies for computation of the Poisson rate in the classical, time‑independent manner, or in a time‑dependent manner that considers time since the last large (characteristic) event are described in Section 4.2.2.5. The time‑dependent approach allows the Poisson model to be used without violating the implications of elastic rebound theory (Section 2.5.1).

Fault models for California, as assembled by Field et al. (2009, 2014, 2015) [@FieldEtAl2009][@FieldEtAl2014][@FieldEtAl2015], provide instructive examples of how alternative approaches for developing Poisson rate parameters can be used in combination with the magnitude distributions described in Section 4.2.2.4. Earthquake rate parameters for piecewise rectangular faults and off‑fault zones are evaluated as:

- Time‑dependent models are considered for all piecewise rectangular faults, including those for which the date of the last rupture is unknown [@FieldJordan2015]. Large ruptures on faults are also modeled as time‑independent (Poisson), which is considered to be less accurate.

- For off‑fault areal sources (i.e., sources that are not associated with any specific known fault), location‑specific values of the Gutenberg‑Richter $a$ parameter (Equation 4.4) are used based on areal source zones with observed rates of seismicity (Section 4.2.1.4). The $b$ value is taken as 1.0 (Section 4.2.2.3).

Earthquake rates on all source types are evaluated to achieve regional moment balance, in consideration of a variety of available geologic, geodetic, and seismological data.

###### 4.4.3 Probability Computations

The results of a PSHA can be expressed in different ways. All involve some level of probabilistic computations to combine the distributions of earthquake magnitudes and site‑source distances, the distributions of ground motion IMs for each magnitude and distance combination, and the rate of earthquake occurrence to estimate seismic hazards. A common approach involves the development of seismic hazard curves, which indicate the mean annual rate of exceedance of different values of a selected IM. The seismic hazard curves can then be used to compute the probability of exceeding the selected IM in a specified period of time. PSHA calculations can be performed in a number of ways, but have historically been performed for individual (scalar) IMs. The response of a structure or system to earthquake shaking, however, may be more accurately predicted if more than one IM is known. It is possible to predict the joint occurrence of multiple IMs using a vector PSHA.

### 4.4.3.1 Scalar PSHA

Seismic hazard curves can be obtained for individual sources and combined to express the aggregate hazard at a particular site. The basic concept of the computations required for the development of seismic hazard curves is fairly simple. The probability of exceeding a particular value, $im$, of a single, or scalar, ground motion IM is calculated for one possible earthquake at one possible source location and then multiplied by the probability that that particular magnitude earthquake would occur at that particular location. The process is then repeated for all possible magnitudes and locations with the probabilities of each summed. The required calculations are described in the following paragraphs.

For a given earthquake occurring on a given source, the probability that a single ground motion parameter, IM, will exceed a particular value, $im$, given that an earthquake (event $E$) has occurred, can be computed using the total probability theorem, i.e.,

$$P[IM > im \mid E] = \int_{\text{all}\,x} P[IM > im \mid X = x]\,f_X(x)\,dx \tag{4.22}$$

where $X$ is a vector of random variables that influence IM and $f_X(x)$ is the joint pdf (Section D.5.3) of $X$. Equation (4.22) and variants thereof are often referred to as hazard integrals. In most cases the quantities in $X$ that are varied within the integral are limited to the magnitude, $M$, and distance, $R$, so $f_X(x)$ can be written as $f_{M,R}(m,r)$. Assuming that $m$ and $r$ are independent, then $f_{M,R}(m,r) = f_M(m)\,f_R(r)$, and the probability of exceedance can be written as

$$P[IM > im \mid E] = \int_{M} \int_{R} P[IM > im \mid M = m,\,R = r]\,f_M(m)\,f_R(r)\,dr\,dm \tag{4.23}$$
