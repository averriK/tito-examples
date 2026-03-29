where $P[IM > im | m, r]$ is obtained from the GMM and $f_M(m)$ and $f_R(r)$ are the probability density functions for magnitude and source-site distance, respectively. Note that if $m$ and $r$ are not independent, the integration would take place across the joint probability density function, $f_{M,R}(m, r)$. The individual components of Equation (4.23) are, for virtually all realistic PSHAs, sufficiently complicated that the integrals cannot be evaluated analytically. Numerical integration, which can be performed by a variety of different techniques, is therefore required. One approach, used here for simplicity and clarity rather than efficiency, is to divide the possible ranges of magnitude and distance into $N_M$ and $N_R$ segments, respectively. The probability of exceedance can then be estimated as

$$P[IM > im | E] \approx \sum_{j=1}^{N_M} \sum_{k=1}^{N_R} P[IM > im | m_j, r_k] \, P(M = m_j) \, P(R = r_k) \tag{4.24}$$

where $m_j = M_{min} + (j - 0.5)(M_{max} - M_{min})/N_M$ and $r_k = r_{min} + (k - 0.5)(r_{max} - r_{min})/N_R$. This is equivalent to assuming that each source is capable of generating only $N_M$ different earthquakes of magnitude $m_j$ at only $N_R$ different source-to-site distances $r_k$. The three components on the right side of Equation 4.24 are illustrated graphically for a single $\{M, R\}$ pair in Figure 4.16. The accuracy of this simple numerical integration procedure increases with increasing $N_M$ and $N_R$. More refined methods of numerical integration (e.g., [@BradleyEtAl2009]) will provide greater accuracy for the same values of $N_M$ and $N_R$.

**Figure 4.16** Schematic illustration of main components of PSHA probability calculations. Products of terms in boxes are summed over all combinations of $M$ and $R$ (in Equation 4.24) to obtain $P[IM > im | E]$.

Equation (4.23) provides the conditional probability required to compute a hazard curve. However, a refinement of the conditional probability calculation provides useful insight into the role of ground motion variability. Since IMs are found to be lognormally distributed, the probability of exceeding a specific value, $im$, for a given $m$-$r$ pair can be expressed as

$$P[IM > im | m, r] = 1 - \Phi\!\left(\frac{\ln im - \mu_{\ln IM|m,r}}{\sigma_{\ln IM|m,r}}\right) \tag{4.25}$$

where $\mu_{\ln IM|m,r}$ and $\sigma_{\ln IM|m,r}$ are the median and standard deviation of IM from a GMM in natural log units conditional on magnitude $m$ and distance $r$. Defining term "epsilon" as the number of logarithmic standard deviations by which the natural log of $im$ exceeds the logarithmic mean for that $m$-$r$ pair,

$$\varepsilon = \frac{\ln im - \mu_{\ln IM|m,r}}{\sigma_{\ln IM|m,r}} \tag{4.26a}$$

the conditional probability of exceeding $im$, which appears in Equations (4.23) and (4.24), can be written more compactly as

$$P[IM > im | m, r] = 1 - \Phi(\varepsilon) \tag{4.26b}$$

Epsilon, $\varepsilon$, describes how "unusual" the value of $im$ is — highly positive values represent particularly strong motions, highly negative values represent particularly weak motions, and values near zero represent typical (median-level) motions. Utilizing the parameter $\varepsilon$, the probability of exceeding $im$ conditional on the occurrence of earthquake event $E$ in Equation (4.23) can alternatively be written as

$$P[IM > im | E] = \int\!\int\!\int P[IM > im | m, r, \varepsilon] \, f_{M,R,\varepsilon}(m, r, \varepsilon) \, dm \, dr \, d\varepsilon \tag{4.27}$$

Note that the probability term in the integrand is now binary, taking on values of 1.0 if the inequality is true and 0.0 if it is not for each combination of $m$, $r$, and $\varepsilon$, because of the specification of $\varepsilon$. With an additional integral, this form appears to be more complicated than that of Equation (4.23); however, it allows convenient characterization of the values of $\varepsilon$ that contribute to the exceedance probability at different levels of $im$, which is useful for a subsequent application (disaggregation, Section 4.4.3.5).

Equations (4.23) and (4.27) describe the probability of exceeding a specified IM level ($im$) given that an earthquake has occurred on a particular source. The rate at which $im$ is exceeded, which can be thought of as a rate of a certain subset of events that produce ground motions that exceed $im$, is also of interest. The mean annual rate of ground motion exceedance is given by

$$\lambda_{IM}(im) = \lambda_{M_{min}} \cdot P[IM > im | E] \tag{4.28}$$

where $\lambda_{M_{min}} = \lambda_M(M_{min})$ is the mean annual rate of earthquakes that exceed the minimum magnitude $M_{min}$. The conditional probability $P[IM > im | E]$ can be obtained from either Equation (4.23) or, more commonly in current practice, Equation (4.27). If the site of interest is in a region of $N_S$ potential earthquake sources, each having its own rate of earthquakes $\lambda_i$ with magnitudes $m > M_{min}$, and the occurrences of earthquakes on the various sources are statistically independent, the total average exceedance rate for the site can be obtained by adding the rates from each of the sources:

$$\lambda_{IM}(im) = \sum_{i=1}^{N_S} \lambda_i \int\!\int\!\int P[IM > im | m, r, \varepsilon] \, f_{M,R,\varepsilon}(m, r, \varepsilon) \, dm \, dr \, d\varepsilon \tag{4.29}$$

Integrating numerically, the average exceedance rate can then be estimated as

$$\lambda_{IM}(im) \approx \sum_{i=1}^{N_S} \sum_{j=1}^{N_M} \sum_{k=1}^{N_R} \lambda_i \cdot P[IM > im | m_j, r_k] \cdot f_M(m_j) \cdot f_R(r_k) \cdot \Delta m \cdot \Delta r \tag{4.30}$$

where $m_j$, $r_k$, $\Delta m$, and $\Delta r$ are defined as before. Note that Eq. (4.30) returns to the $im$ exceedance probability represented as a real number and not a 0.0 or 1.0 binary. An equivalent but more compact form of Equation (4.30) utilizing Eq. (4.26b) to replace the probability of exceedance term can be written as

$$\lambda_{IM}(im) \approx \sum_{i=1}^{N_S} \sum_{j=1}^{N_M} \sum_{k=1}^{N_R} \lambda_i \left[1 - \Phi(\varepsilon_j)\right] f_M(m_j) \, f_R(r_k) \, \Delta m \, \Delta r \tag{4.31a}$$

which is also equivalent to

$$\lambda_{IM}(im) \approx \sum_{i=1}^{N_S} \sum_{j=1}^{N_M} \sum_{k=1}^{N_R} \lambda_i \left[1 - \Phi(\varepsilon_j)\right] P(M = m_j) \, P(R = r_k) \tag{4.31b}$$

When rate calculations of the type given by Equation (4.31) are carried out for a range of IM levels (as given by $im$) for a given IM, the resulting plot of $im$ against rate of exceedance is termed a seismic hazard curve. Hazard curves for peak ground acceleration are shown in Figure 4.17 for several regions in the US. For any particular hazard curve, relatively low values of IM (i.e., weak levels of shaking) occur relatively frequently and relatively high values of IM (strong shaking) will occur more rarely. The return period of a particular intensity value $im$ is the reciprocal of its mean annual rate of exceedance:

$$T_R(im) = \frac{1}{\lambda_{IM}(im)} \tag{4.32}$$

Accordingly, areas of high hazard have short return periods for a given ground motion level, whereas areas of lower hazard have longer return periods. As shown in Figure 4.17, areas near plate boundaries (coastal California, Seattle) are high-hazard, meaning high exceedance rates for a given IM. In contrast, stable continental regions (central and eastern North America) have relatively low hazard. Slopes of hazard curves are also regionally variable. As one moves to the right on a hazard curve (increasing IM), both the earthquake rate and conditional ground motion exceedance probability (Equation 4.23) change. In areas with low rates of seismicity and sources that are modeled with Gutenberg-Richter magnitude-frequency distributions, increasing ground motions are associated with rarer, larger magnitude earthquakes (decreasing $\lambda_m$), and higher conditional probability terms ($P$) (because larger earthquakes produce higher IMs). These counter-acting effects can produce relatively flat hazard curves, as in stable continental regions near faults or in seismic zones with a history of large but low-recurrence rate earthquakes (Memphis, Charleston). In contrast, if moving right on the hazard curve does not appreciably change magnitude, which can occur if hazard is dominated by relatively high-rate characteristic events, then $\lambda_m$ remains nearly constant, and the $P$ term controls the hazard curve slope, which is relatively steep. This occurs near plate boundaries where earthquake rates can be relatively high relative to much of the $\lambda_{IM}$ range in the plot.

**Figure 4.17** Hazard curves for $S_a(0.2\text{ sec})$ at rock site conditions ($V_{S30} = 760$ m/s) at various locations across the US (using 2018 seismic hazard model from USGS, [@PetersenEtAl2020]).

### Example 4.4

Consider the site and fault in Figure E4.4a with the indicated location coordinates and, using the fault parameters shown in the figure, compute a seismic hazard curve for PGA.

**Figure E4.4A** Position of site relative to linear fault and fault parameters for Example 4.4.

#### Solution

The PSHA can be performed by applying the four previously described steps:

1. This step involves the identification and characterization of earthquake sources, including the characterization of the probability distribution and recurrence rates of the full range of earthquake magnitudes that each source is capable of producing. To simplify the calculation, four magnitude bins are considered as shown in the table below. Using the mid-magnitude in each bin, the probability density using a truncated exponential model is computed using Equation (4.9). The truncated exponential probability density function is $f_M(m) = \frac{\beta e^{-\beta(m - M_{min})}}{1 - e^{-\beta(M_{max} - M_{min})}}$ where $\beta = \ln(10) \cdot b$. The corresponding probability masses for each rupture size are computed as $P(m) = f_M(m) \cdot dm$ (where the bin width $dm = 0.5$). The magnitude bins, mid-values, $f_M(m)$, and $P(m)$ are: bin 5.0–5.5 mid-value 5.25 ($f_M = 1.254$, $P(m) = 0.627$); bin 5.5–6.0 mid-value 5.75 ($f_M = 0.445$, $P(m) = 0.223$); bin 6.0–6.5 mid-value 6.25 ($f_M = 0.158$, $P(m) = 0.079$); bin 6.5–7.0 mid-value 6.75 ($f_M = 0.056$, $P(m) = 0.028$). These results are summarized in the portion of Table E4.4 marked as Step 1.

2. The second step considers alternative rupture locations within the source, which control the rupture distances that must be considered in hazard calculations. A uniform probability distribution is assigned to hypocenter locations along the fault as parameterized by the normalized position coordinate $h$ as shown in Figure 4.15. Six bins of $h$ are considered along with their probability masses: $h$ = 0.083, 0.167 (omitted from raw — six values 0.083, 0.250, 0.417, 0.583, 0.750, 0.917 each with $P(h) = 0.167$). Distance calculations are affected by rupture size (length in this case) and hypocenter location $h$ as shown in Figure 4.15. As indicated in the text below Equation (4.20), logarithmic mean rupture length is taken as $\log(L_{rup}) = 0.74 \cdot m - 3.55$ ($L_{rup}$ in km; from [@WellsCoppersmith1994]). Table E4.4 shows distances calculated for the six realizations of $h$ for each magnitude, each of which has a unique $L_{rup}$ (to simplify the calculations, uncertainty in rupture dimensions is not considered in this example). The computed rupture lengths are: $L_{rup} = 2.16$ km for $m = 5.25$; 5.07 km for $m = 5.75$; 11.89 km for $m = 6.25$; 27.86 km for $m = 6.75$. The probability mass for each distance is computed using Equation (4.21) adapted to probability masses as $P(R = r_{rup}) = f_R(r) \cdot dr = P(h)$. These results are provided in the portion of Table E4.4 marked as Step 2.

3. For each magnitude and distance combination, median ground motions (denoted $\mu_{\ln PGA|m,r}$) are computed using the simple Campbell (1981) [@Campbell1981] GMM in Equation (3.25). These are shown in the Part 3 portion of Table E4.4. As indicated in Example 4.3, the use of the Campbell model is for illustrative purposes only — it is a simple model that can be relatively easily applied to illustrate the steps in PSHA.

4. The probability calculation begins by computing the epsilon ($\varepsilon$) value corresponding to a particular target ground motion level ($im$) for each magnitude and distance combination using Equation (4.26a). A target ground motion level of 0.1g is used in Table E4.4. This value of $\varepsilon$ is used with the standard normal CDF table (Table D.1) to compute $F_{IM}(\varepsilon)$. The value $1 - F_{IM}(\varepsilon)$ is the probability that $\varepsilon$ is exceeded, which is equivalent to the probability that the target ground motion $im$ is exceeded for the particular $m$ and $r$ combination. The combined probability (integrand in Equation 4.23) is then computed. The summation provides the conditional probability that $IM > im$ given that an earthquake has occurred (Equation 4.23), which is 0.281 for the target $im$ value. The mean annual rate of ground motion exceedance is computed using Equation (4.28) as $\lambda_{IM}(0.1\text{g}) = \lambda_{M_{min}} \cdot P[IM > im | E] = 0.03 \times 0.281 = 0.0084/\text{year}$. This result represents one point on a PGA seismic hazard curve as shown in Figure E4.4b. Repeating this calculation for many values of $im$ provides the entire hazard curve. The probability of exceedance in $\Delta t = 30$ years is $P = 1 - \exp(-\lambda_{IM} \cdot \Delta t) = 0.2234$.

Table E4.4 (Calculations for Mean Annual Rate of Exceeding PGA Value of 0.1g) presents the full numerical computation across 24 rows (4 magnitude bins × 6 hypocenter position bins). The table is organized by Steps 1–4 with columns for $m$, $h$, $P(h)$, $L_{rup}$ (km), $P(L_{rup})$, $r(h, L)$ (km), $P(r)$, $\mu_{\ln PGA|m,r}$, $\sigma_{\ln PGA}$, $\varepsilon$ (for $im = 0.1\text{g}$), $F_{IM}(\varepsilon)$, $1 - F_{IM}(\varepsilon)$, and the product $\lambda_i \cdot P(m) \cdot P(r) \cdot [1 - F_{IM}(\varepsilon)]$. The standard deviation $\sigma_{\ln PGA} = 0.372$ applies uniformly to all 24 rows. Source-to-site distances $r$ range from 10.00 to 35.36 km across the combinations. The individual probability products and their row-by-row values sum to $\lambda_{IM}(0.1\text{g}) = 0.0084$/year (conditional probability $= 0.2809$).

**Figure E4.4B** Hazard curve derived for Example 4.4, with the point computed in Table E4.4 marked.

### 4.4.3.2 Vector PSHA

As discussed in Section 1.6, earthquake engineers use IMs to predict the seismic response of systems of interest and characterize that response in terms of engineering demand parameters, or EDPs. Because no single IM captures all of the ground motion characteristics that influence response, there will always be some uncertainty in EDP for a given IM (i.e., in $EDP|IM$). That uncertainty can often be reduced, however, with the addition of more information about the ground motions. For example, it would seem logical (and will be discussed in Chapter 5) that the permanent displacement of an unstable slope could be predicted more accurately if both the amplitude and duration of an earthquake motion are known rather than just the amplitude. The joint rates of exceedance of multiple IMs can be predicted using vector PSHA. [@BazzurroCornell2002] described a procedure for evaluating the mean annual joint rate of occurrence of the elements of a vector of ground motion IMs. The procedure is more easily understood by considering a scalar PSHA expressed in a different form. As shown in Section 4.4.3.1, the mean annual rate of exceedance of some value of a scalar $IM = im$ for a given source can be expressed (noting that, despite the boldface notation, magnitude is a scalar quantity) as

$$\lambda_{IM}(im) = \lambda_{M_{min}} \int\!\int P[IM > im | m, r] \, f_{M,R}(m, r) \, dm \, dr \tag{4.33}$$

The conditional probability $P[IM > im | m, r]$ is the complementary cumulative distribution function, $G_{IM}(im | m, r) = 1 - F_{IM}(im | m, r)$. Differentiating the expression for the mean rate of exceedance in Equation (4.33) with respect to IM produces the mean rate density

$$MRD_{IM}(im) = \lambda_{M_{min}} \int\!\int f_{IM}(im | m, r) \, f_{M,R}(m, r) \, dm \, dr \tag{4.34}$$

where

$$f_{IM}(im | m, r) = \frac{1}{im \sqrt{2\pi} \, \sigma_{\ln IM|m,r}} \exp\!\left(-\frac{(\ln im - \mu_{\ln IM|m,r})^2}{2\sigma^2_{\ln IM|m,r}}\right) \tag{4.35}$$

for a lognormally distributed IM.

Considering the case where two IMs, $IM_1$ and $IM_2$, are of interest at a particular site, the joint mean rate density can be expressed as

$$MRD_{IM_1,IM_2}(im_1, im_2) = \lambda_{M_{min}} \int\!\int f_{IM_1,IM_2}(im_1, im_2 | m, r) \, f_{M,R}(m, r) \, dm \, dr \tag{4.36}$$

where $f_{IM_1,IM_2}(im_1, im_2 | m, r)$ is the joint PDF of $IM_1$ and $IM_2$ conditional upon $M = m$ and $R = r$.

As indicated in Section D.5.3 of Appendix D, a joint PDF can also be written in conditional form, i.e., as

$$f_{IM_1,IM_2}(im_1, im_2 | m, r) = f_{IM_1}(im_1 | m, r) \cdot f_{IM_2|IM_1}(im_2 | im_1, m, r) \tag{4.37}$$

Note that the first term on the right side of Equation (4.37) is the conditional PDF of a single IM (as appeared on the right side of the scalar PSHA expression in Equation 4.33). Assuming that $IM_1$ and $IM_2$ are jointly lognormal (a reasonable assumption given that they are each marginally lognormal), the conditional distribution comprising the second term on the right side of Equation (4.37) will also be lognormal. The conditional distribution can then be expressed as

$$f_{IM_2|IM_1}(im_2 | im_1, m, r) = \frac{1}{im_2 \sqrt{2\pi} \, \sigma_{\ln IM_2|im_1,m,r}} \exp\!\left(-\frac{(\ln im_2 - \mu_{\ln IM_2|im_1,m,r})^2}{2\sigma^2_{\ln IM_2|im_1,m,r}}\right) \tag{4.38}$$

The logarithmic mean and standard deviation of the conditional distribution are [@BenjaminCornell1970]

$$\mu_{\ln IM_2|im_1,m,r} = \mu_{\ln IM_2|m,r} + \rho_{1,2} \left(\ln im_1 - \mu_{\ln IM_1|m,r}\right) \frac{\sigma_{\ln IM_2|m,r}}{\sigma_{\ln IM_1|m,r}} \tag{4.39a}$$

and

$$\sigma_{\ln IM_2|im_1,m,r} = \sigma_{\ln IM_2|m,r} \sqrt{1 - \rho_{1,2}^2} \tag{4.39b}$$

where $\rho_{1,2}$ is the correlation coefficient for the natural logarithms of $IM_1$ and $IM_2$, and $\sigma_{\ln IM_1|m,r}$ and $\sigma_{\ln IM_2|m,r}$ are obtained from the GMM. Substituting Equations (4.38) and (4.39) into Equation (4.37), the joint mean rate density function can be obtained. Computing this function, therefore, requires the availability of GMMs for each IM and the correlations between both IMs in the vector (e.g., [@BakerJayaram2008]; [@Bradley2011]). By integrating over the IM values, a corresponding joint mean rate of exceedance surface (the multi-dimensional analog to the one-dimensional curve obtained for a scalar IM) is obtained as:

$$MRE_{IM_1,IM_2}(im_1, im_2) = \int_{im_1}^{\infty} \int_{im_2}^{\infty} MRD_{IM_1,IM_2}(im_1', im_2') \, d(im_1') \, d(im_2')$$

where the mean rate density in the integrand is given in Equation (4.36).

### 4.4.3.3 Finite Time Periods

The IM exceedance rates described in Section 4.4.3.1 can be combined with the Poisson model (Section D.7.1.2) to estimate the probability of exceeding a particular IM level ($im$) in a finite time interval. From Equation (D.48), the probability of exceedance of $im$ in a time period $\Delta t$ is

$$P[N \geq 1] = 1 - e^{-\lambda_{IM}(im) \cdot \Delta t} \tag{4.40}$$

Expanding $1 - e^{-\lambda_{IM}(im) \cdot \Delta t}$ in a Taylor series shows that

$$P[N \geq 1] \approx \lambda_{IM}(im) \cdot \Delta t \tag{4.41}$$

for small values of $\lambda_{IM}(im) \cdot \Delta t$ (or, equivalently, small values of $\Delta t / T_R$) that are normally of interest for design. This result is often used to approximate the annual ($\Delta t = 1$ yr) probability of exceedance as being equal to $\lambda_{IM}$. Hazard maps show the spatial variation of a given IM at a particular probability level; the example in Figure 4.18 applies for the IM of $S_a(0.2\text{ sec})$, $V_{S30} = 760$ m/s site condition, and the 2% probability of exceedance in 50-year hazard level. Finally, as shown in Figure 4.19, a uniform hazard spectrum (UHS) can be defined for a given site by computing hazard curves for spectral accelerations at multiple periods and plotting the spectral accelerations vs. period for a given exceedance rate. All ordinates of the UHS, therefore, have the same return period, i.e., the same probability of exceedance in a particular period of time.

**Figure 4.18** Shaded map of $S_a(0.2\text{ sec})$ spectral acceleration (expressed as a percentage of gravity) with 2% probability of exceedance in 50 years for rock sites with $V_{S30} = 760$ m/s ([@PetersenEtAl2020]; used with permission of SAGE Publications, Ltd.).
