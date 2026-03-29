where $a$ and $b$ are empirical coefficients (Table 7.2) obtained by regression. Different models have been obtained for portions of Japan [@BooreEtAl2011] and Greece [@StewartEtAl2014], which is expected due to regional variations in geological conditions. Relationships between $V_{S30}$ and $V_{Sz}$ are also useful when $z > 30$ m, principally for the prediction of average velocities beyond the limits of geotechnical exploration. This can be significant for deep sites since the response to low-frequency waves (with longer wavelengths) will be affected by profile stiffness at depths greater than 30 m. Since many shear wave velocity measurements are made in borings or CPT soundings advanced for foundation design purposes, some sites may lack velocity data for depths greater than 30 m. In this case, the prediction is of $V_{Sz}$ from $V_{S30}$, which can be evaluated from:

$$\log(V_{Sz}) = c + d \log(V_{S30}) \tag{7.5}$$

Using data from California, the coefficients $c$ and $d$ and the standard deviation of the fit have been derived, as given in Table 7.3. These correlations have been found to be surprisingly robust in California (e.g., as shown by the low standard deviations in Table 7.3), which indicates that the $V_{S30}$ parameter has strong predictive power for (i.e., is well correlated to) velocity structure at greater depth. This helps explain why $V_{S30}$ correlates strongly to site amplification even at low frequencies, where wavelengths are often much greater than 30 m. Regional variations in geological conditions may cause correlations like Equation (7.5) to break down in some areas, weakening the predictive power of $V_{S30}$ as a site parameter. This appears to be the case, for example, in central and eastern North America [@ParkerEtAl2019] where geologic conditions often cause large impedance contrasts to be present in site profiles and the dependence of site response on $V_{S30}$ is weaker than in the western United States. In some cases, where site-specific measurements are not available, $V_{S30}$ can be roughly estimated using proxies such as ground slope, ground slope plus surficial geology, or more complicated terrain indicators (Section 6.6.2.2).

### TABLE 7.3

Coefficients for Estimation of $V_{Sz}$ Based on $V_{S30}$ for $z > 30$ m as Described by Boore et al. (2011) [@BooreEtAl2011]

Column headers: Depth, $z$ (m) | $c$ | $d$ | $\sigma_{\log V_{Sz}}$ | $\sigma_{\ln V_{Sz}}$

Data rows (c, d, $\sigma_{\log}$, $\sigma_{\ln}$):
0.151, 0.980, 0.042, 0.097
0.327, 0.942, 0.071, 0.163
0.466, 0.909, 0.087, 0.200
0.713, 0.831, 0.112, 0.258
0.887, 0.783, 0.124, 0.286
1.188, 0.661, 0.114, 0.262
1.534, 0.532, 0.123, 0.283

Coefficients from D.M. Boore (personal communication).

**Uncertainty in $V_{S30}$**

The uncertainty in $V_{S30}$ from measured velocity profiles has been evaluated from sites with clusters of profiles, typically spaced on the order of 10 to about 100 m. This uncertainty, denoted $\sigma_{\ln V_{S30}}$, is useful for uncertainty propagation in ground motion predictions that utilize $V_{S30}$-based site response models (Section 3.5.2). This uncertainty can in general be influenced by variations among $V_S$ measurement types (generally small when reliable data providers are used) and natural heterogeneity in the site conditions. Based on data compiled by Moss (2008) [@Moss2008] and Seyhan et al. (2014) [@SeyhanEtAl2014], the range of $\sigma_{\ln V_{S30}}$ was approximately 0.02–0.12, with an average of about 0.06 for sites without strongly variable geological conditions. Values of 0.1 are often applied in current practice.

### 7.3.3.2 Geology-Based Classification

Geology-based site classification is attractive because geologic maps are readily available, at various levels of resolution, for many parts of the world. Surface geology can provide a general indication of profile stiffness, at least between the relatively broad categories shown in typical geologic maps. To better capture variations in stiffness within these broad categories, additional information can be added to supplement the basic mapped categories. Such information can include sediment thickness, texture, regional location, geologic history, and geomorphological data such as ground slope [@KottkeEtAl2012]. Stewart et al. (2003) [@StewartEtAl2003] used age, depositional environment, and sediment texture (Table 7.4) to classify surface geology for ground motion amplification purposes. As part of the development of a shear wave velocity map for California, Wills et al. (2015) [@WillsEtAl2015] collected downhole, crosshole, and suspension log shear wave velocity data from multiple profiles in different geologic environments and compiled $V_{S30}$ values for 15 geological site categories (Table 7.5). Geographic criteria were used to help define the dominant characteristics of Quaternary materials within the upper 30 m of the profile, noting that the soil maps upon which many maps of Quaternary geology are based often reflect the material only in the upper few meters. The $V_{S30}$ values can clearly be seen to vary systematically with sediment texture (e.g., fine-grained vs. coarse-grained) and age.

### 7.3.3.3 Geotechnical-Based Classification

Geotechnical classification schemes are based on characteristics such as sediment type, thickness, and stiffness. Such schemes began with the four site categories of Seed et al. (1976a) [@SeedEtAl1976a] shown in Figure 7.7, but were later refined by a number of researchers. Rodriguez-Marek et al. (2001) [@RodriguezMarekEtAl2001]

### TABLE 7.4

Geology-Based Site Classification Criteria (Stewart et al., 2003) [@StewartEtAl2003]

Column headers: Age | Depositional Environment | Sediment Texture

Data rows:
Holocene | Fan alluvium | Coarse
Pleistocene | Valley alluvium | Fine
(Pleistocene) | Lacustrine/marine | Mixed
(Pleistocene) | Aeolian | —
(Pleistocene) | Artificial Fill | —
Tertiary | — | —
Mesozoic + Igneous | — | —

### TABLE 7.5

$V_{S30}$ Values (in m/s) for Different Site Geology Units in California from Site-Condition Map of California and from Borehole Profiles with Indicated Unit at Ground Surface

Column headers: Unit | Geologic Description | $V_{S30}$ for Map Units (Mean, St. Dev., No. prof.) | $V_{S30}$ from Boreholes (Mean, St. Dev., No. prof.)

Data rows (Unit, Description, Map Mean, Map St. Dev., Map No. prof., Borehole Mean, Borehole St. Dev.):
Qi — Intertidal Mud, including mud around the San Francisco Bay and similar mud in the Sacramento/San Joaquin delta and in Humboldt Bay: 176.1, 47.6; borehole: 176.0, 57.0
af/qi — Artificial fill over intertidal mud around San Francisco Bay: 225.6, 113.3; borehole: 199.4, 41.4
Qal1 — Quaternary Holocene alluvium (flat): 228.2, 48.0; borehole: 298.5, 93.9
Qal2 — Quaternary Holocene alluvium (moderate): 293.5, 73.5
Qal3 — Quaternary Holocene alluvium (steep): 351.9, 112.2
Qoa — Quaternary (Pleistocene) alluvium: 386.6, 145.1; borehole: 372.8, 132.1
Qs — Quaternary (Pleistocene) sand deposits: 307.6, 33.7; borehole: 331.3, 52.3
QT — Quaternary to Tertiary (Pleistocene-Pliocene) alluvial deposits such as the Saugus Formation of southern California, Paso Robles Formation of central coast ranges, and the Santa Clara Formation of the San Francisco Bay Area: 444.0, 159.7; borehole: 456.6, 193.7
Tsh — Tertiary (mostly Miocene and Eocene) shale and siltstone units such as the Repetto, Fernando, Puente, and Modelo Formations of the Los Angeles area: 385.1, 129.4; borehole: 404.5, 98.0
Tss — Tertiary (mostly Miocene, Oligocene, and Eocene) sandstone units such as the Topanga Formation in the Los Angeles area and the Butano sandstone in the San Francisco Bay Area: 468.4, 212.6; borehole: 433.0, 119.9
Tv — Tertiary volcanic units including the Conejo Volcanics in the Santa Monica Mountains and the Leona Rhyolite in the East Bay Hills: 518.9, 172.0; borehole: 536.7, 155.6
Serp. — Serpentine, generally considered part of the Franciscan complex: 571.6, 87.0; borehole: 545.8, 42.6
Kss — Cretaceous sandstone of the Great Valley Sequence in the central Coast Ranges: 502.5, 227.9; borehole: 796.7, 294.6
KJf — Franciscan complex rock, including mélange, sandstone, shale, chert, and greenstone: 733.4, 340.1; borehole: 800.3, 365.6
Xtal. — Crystalline rocks, including Cretaceous granitic rocks, Jurassic metamorphic rocks, schist, and Precambrian gneiss: 710.1, 393.8; borehole: 614.9, 228.5

Source: After Wills et al. (2015) [@WillsEtAl2015].

### TABLE 7.6

Geomatrix Site Classification Based on Geotechnical Characteristics

Column headers: Site Category | Description | $\sigma_{\ln V_{S30}}$ | Median $V_{S30}$ (m/s) | Mean $V_{S30}$ (m/s)

Data rows:
A — Rock: Instrument on rock or $<$5 m soil over rock; $\sigma_{\ln V_{S30}}$ = 0.41
B — Shallow (stiff) soil: Instrument on/in soil profile up to 20 m thick overlying rock; $\sigma_{\ln V_{S30}}$ = 0.43
C — Deep, narrow soil: Instrument on/in soil profile at least 20 m thick overlying rock, in a narrow canyon or valley no more than several km wide; $\sigma_{\ln V_{S30}}$ = 0.20
D — Deep, broad soil: Instrument on/in soil profile at least 20 m thick overlying rock, in a broad valley; $\sigma_{\ln V_{S30}}$ = 0.34
E — Soft, deep soil: Instrument on/in deep soil profile with average $V_{S30} < 150$ m/s; $\sigma_{\ln V_{S30}}$ = 0.25

Source: After Seyhan et al. (2014) [@SeyhanEtAl2014], Adapted from Chiou et al. (2008) [@ChiouEtAl2008].

developed a system of six basic site categories based primarily on material type and stiffness with several subcategories based on sediment thickness. Geomatrix [@SadighEtAl1993] developed a site classification system (Table 7.6) that includes five relatively broad categories – rock, shallow (stiff) soil, deep narrow soil, deep broad soil, and soft, deep soil. The distinction between narrow and broad soil deposits allows the differentiation of cases where multi-dimensional effects and basin effects may have more or less influence on ground motions.

##### 7.4 SITE-SPECIFIC PREDICTION OF SITE EFFECTS

Generic ground motion predictions based on data from many different sites within a particular site class will necessarily represent the average response of profiles within that site class and will correspond most closely to the response of the smooth, "average profile" within it. The response of a particular site of interest, however, will be influenced in a systematic and repeatable manner by the individual characteristics of that site. Some sites may respond more strongly than the average response implied by a GMM and others may respond less strongly. Also, the dispersion of response in multiple events at a specific site will be lower than the dispersion obtained from a GMM based on data from many different sites. More accurate and less uncertain estimates of site effects, therefore, can often be obtained by site-specific procedures. Site-specific characterization of site response can be accomplished in one of two main ways – empirically using ground motion recordings at an instrumented site, and analytically using dynamic analyses. In some situations, a third approach to characterization may be advisable – a hybrid approach in which dynamic analyses are used to define part of the amplification behavior and empirical data is used to define other parts.

###### 7.4.1 Empirical Site-Specific Approach

A purely empirical approach to site-specific response prediction would be ideal. In that case, a site of interest would already have been instrumented with a vertical array extending to bedrock that has recorded many ground motions from a wide range of earthquakes (small to large) on all sources (nearby to distant) capable of producing strong ground motion at the site. Since source and path effects would affect both the downhole and surface instruments, ratios of surface-to-downhole spectral amplitudes (either Fourier or response spectra) could be used to characterize site-specific amplification behavior of the site (at periods less than the site period, above which the profile tends to respond as a rigid body) in each earthquake. With sufficient data, both the median amplification behavior and the dispersion in amplification could be characterized across a broad range of frequencies and input motion amplitudes. This approach would give the actual small- and large-strain amplification behavior of the site soil column, accounting for all details associated with its specific geometric and material characteristics. The approach would account for linear response under very weak shaking and nonlinear response under strong shaking and for both shallow and deep soils at the site. The effects of spatial variability, basin structure, and surface topography at that particular site would all be included. Unfortunately, instrumented sites with this amount of data do not exist. While vertical arrays allow for a direct evaluation of site response, ground motion instruments installed only at the surface of a site can also be used to evaluate site response if the instruments have recorded a sufficient number of earthquakes [@StewartEtAl2017]. In this case, the site response is evaluated using a non-reference site approach and is evaluated relative to the reference condition in the GMM (often corresponding to $V_{S30} = 760$ m/s). Because the recordings available for a given site are likely to be low in amplitude, and thus associated with small levels of strain, they can often only be used to characterize the linear site response. The effects of nonlinearity under stronger shaking can then be assessed by numerical ground response analyses. Incorporation of this type of information into a ground motion hazard evaluation is described in Section 7.7.

###### 7.4.2 Analytical Site-Specific Approach

When detailed information on the characteristics of a specific site is available, site-specific amplification behavior can be predicted by numerical analysis. Numerical ground response analyses provide the additional benefits of predicting not only ground surface motions but also ground motions, stresses, strains, and other important measures of response below the ground surface, which can be important for ground failure, liquefaction, and soil-structure interaction problems. Numerical analyses can account for the individual characteristics of a specific profile and the effects of those characteristics on the response of that profile to specific ground motions. For a profile with characteristics close to the average characteristics of a particular site class, a good numerical analysis will generally produce ground surface motions that are about as accurate as those produced by empirical amplification factors [@BaturayStewart2003]. For profiles with characteristics that deviate in some significant way from the average of a particular site class, site-specific numerical analyses can produce more accurate estimates of site response. The details of the modeling are important, though, and oversimplification of site conditions can lead to inaccurate results (e.g., Thompson et al., 2009) [@ThompsonEtAl2009]. Ground response analyses can be performed in a number of different ways. Some sites, with level ground surfaces and horizontal layer boundaries that extent laterally to distances significantly greater than the thickness of the profile, can be modeled as one-dimensional. Other sites may have significant two- or three-dimensional characteristics and must be modeled as such. Anticipated material behavior also plays a role in determining the type of site response analysis that should be performed. For stiff soils and/or weak motions, the stresses and strains in soil layers will be low, and linear or equivalent linear analyses can be used. For soft or loose, saturated soils and/or for strong motions, nonlinear analyses may be required. Profiles with soils capable of generating significant porewater pressure during shaking may require nonlinear effective stress analysis. All of these types of analyses are described in the remainder of this section.

##### 7.5 ONE-DIMENSIONAL GROUND RESPONSE ANALYSIS

When a fault ruptures below the Earth's surface, body waves travel away from the source in all directions and are reflected and refracted as they reach boundaries between different geologic materials. Since the wave propagation velocities of shallower materials are generally lower than the materials beneath them, inclined rays that strike horizontal layer boundaries are usually refracted to a more vertical direction (Section C.4.2). By the time the rays reach the ground surface, multiple refractions have often bent them to a nearly vertical direction (Figure 7.9). One-dimensional ground response analyses are based on the assumption that all boundaries are horizontal and that the response of a soil deposit is predominantly caused by SH waves propagating vertically (hence with horizontal particle motion) from the underlying bedrock. For one-dimensional analyses, the soil layers and bedrock surface are assumed to extend infinitely with exactly the same properties in the horizontal direction. As a result of these assumptions, one-dimensional analyses cannot account for surface waves or for the effects of lateral inhomogeneity; the former can lead to the underprediction of low-frequency response and the latter to the overprediction of high-frequency response. These limitations in the ability of one-dimensional analyses to represent all of the physical processes that can affect the response of a particular site can lead to systematic errors, or bias, in the predicted response. The amount of bias can range from negligible to significant on a case-by-case basis, and will generally be different at different frequencies. One-dimensional amplification arises primarily from two phenomena – conservation of energy as upward-traveling waves encounter softer materials on their way to the ground surface and resonance. The increase in wave amplitude (of acceleration, velocity, and displacement) that occurs when waves travel from a stiffer material into a softer material was described in Section C.4.1.

FIGURE 7.9 Refraction process that produces nearly vertical wave propagation near the ground surface.

FIGURE 7.10 Ground response nomenclature: (a) soil overlying bedrock; (b) no soil overlying bedrock. Vertical scale is exaggerated.

Resonance phenomena develop in layered profiles where upward- and downward-traveling waves interfere with each other, both constructively and destructively, at different frequencies. Resonance can cause strong amplification at certain frequencies. One-dimensional ground response analyses can account for the simultaneous occurrence of both of these phenomena, along with damping effects that attenuate site amplification. Before describing any of the ground response models, it is necessary to define several terms that are commonly used to describe ground motions. With reference to Figure 7.10a, the motion at the surface of a soil deposit is the free surface motion. The motion at the base of the soil deposit (also the top of bedrock) is called a bedrock within motion. The motion at a location where bedrock is exposed at the ground surface is called a rock outcropping motion. If the soil deposit was not present (Figure 7.10b), the motion at the top of the bedrock would be the bedrock outcropping motion. Consistent use of this terminology is important for understanding important principles of site response and the proper application of input motions (Section 7.5.5.1) in ground response analyses.

###### 7.5.1 Linear Analyses

Profiles with very stiff soils subjected to relatively weak shaking may develop strains so small that the stiffness and damping of the soil material are essentially constant. Under such conditions, site response can be analyzed using linear analyses. Linear analyses of site response are most easily accomplished in the frequency domain using transfer functions. The manner in which transfer functions can be used to compute the response of single-degree-of-freedom systems is illustrated in Appendix B (Section B.5.4.2). An important class of techniques for ground response analysis is also based on the use of transfer functions. For the ground response problem, transfer functions can be used to relate various response parameters, such as displacement, velocity, acceleration, shear stress, and shear strain, to the input motion. Because it relies on the principle of superposition, this approach is limited to the analysis of linear (elastic or viscoelastic) systems. The primary effects of mild to moderate nonlinearity can be approximated using linear analyses in an equivalent linear framework (Section 7.5.2). The basic mathematical aspects of the transfer function approach are described in Section B.5.4.2 of Appendix B. Although the calculations involve the manipulation of complex numbers in order to account for damping, the approach itself is quite simple. A known time history of bedrock (input) motion is represented as a Fourier series, usually using the FFT (Section A.3). Each term in the Fourier series of the bedrock (input) motion is then multiplied by the transfer function to produce the Fourier series of the ground surface (output) motion. The ground surface (output) motion can then be expressed in the time domain using the inverse FFT. Thus the transfer function determines how each frequency in the bedrock (input) motion is amplified, or deamplified, by the soil deposit; the imaginary part of a complex transfer function introduces the phase shift of each frequency.

The key to the linear approach is the evaluation of transfer functions. In the following sections, transfer functions are derived for a series of successively more complicated geotechnical conditions. Although the simplest of these may only rarely be applicable to actual problems, they illustrate some of the important effects of soil deposits on ground motion characteristics without undue mathematical complexity. The more complex solutions are capable of describing the most important aspects of ground response and are very commonly used in geotechnical earthquake engineering practice.

### 7.5.1.1 Undamped Soil on Rigid Bedrock

Section C.6.1.2 showed how a linear undamped material fixed at one end (e.g., bedrock) and free at the other (the ground surface) would respond to a harmonic motion of the fixed end. The response was expressed in terms of a transfer function whose modulus varied with frequency in the form of an amplification factor. That amplification factor was

$$F(\omega) = \frac{1}{\cos(kH)} = \frac{1}{\cos(\omega H / V_s)} \tag{7.6}$$

which is strongly frequency-dependent (Figure C.29) and implies infinite amplification at circular frequencies $\omega = \pi V_s / 2H,\; 3\pi V_s / 2H,\; 5\pi V_s / 2H$, etc.

### 7.5.1.2 Damped Soil on Rigid Bedrock

Obviously, the type of unbounded amplification predicted by the previous analysis cannot physically occur. The previous analysis assumed no dissipation of energy, or damping, in the soil. Since damping is present in all materials, more realistic results can be obtained by repeating the analysis with damping. Assuming the soil to have the shearing characteristics of a Kelvin-Voigt solid, the wave equation can be written (Equation C.124) as

$$\rho \frac{\partial^2 u}{\partial t^2} = G \frac{\partial^2 u}{\partial z^2} + \eta \frac{\partial^3 u}{\partial z^2 \partial t} \tag{7.7}$$

where $\eta$ is the viscosity of the soil. The solution to this wave equation is of the form

$$u(z,t) = A e^{i(\omega t + k^* z)} + B e^{i(\omega t - k^* z)} \tag{7.8}$$

where $k^*$ is a complex wave number with real part $k_1$ and imaginary part $k_2$. Repeating the previous algebraic manipulations with the complex wave number, the transfer function for the case of damped soil over rigid rock can be expressed as

$$F(\omega) = \frac{1}{\cos(k^* H)} = \frac{1}{\cos(\omega H / V_s^*)} \tag{7.9}$$

Unlike the undamped case described in the previous section and Section C.6.1.2, the transfer function for the damped case is complex. The imaginary part of the transfer function accounts for damping. Since the frequency-independent complex shear modulus is given by $G^* = G(1 + i2\xi)$, the complex shear wave velocity can be expressed as

$$V_s^* = \sqrt{\frac{G^*}{\rho}} = \sqrt{\frac{G(1+i2\xi)}{\rho}} \approx V_s(1+i\xi) \tag{7.10}$$

for small $\xi$. Then the complex wave number can be written, again for small $\xi$, as

$$k^* = \frac{\omega}{V_s^*} = \frac{\omega}{V_s(1+i\xi)} \approx \frac{\omega}{V_s}(1-i\xi) = k(1-i\xi) \tag{7.11}$$

and finally, the transfer function, as

$$F(\omega) = \frac{1}{\cos\!\left[(1-i\xi)kH\right]} = \frac{1}{\cos\!\left[\frac{\omega H}{V_s}(1-i\xi)\right]} \tag{7.12}$$

Using the identity $\cos(x + iy) = \cos x \cosh y + i \sin x \sinh y$, wait — using $|\cos(x+iy)|^2 = \cos^2 x + \sinh^2 y$, the amplification function (i.e., modulus of the transfer function) can be expressed as

$$|F(\omega)| = \frac{1}{\sqrt{\cos^2(kH) + \sinh^2(\xi kH)}} \tag{7.13}$$

Since $\sinh^2 y \approx y^2$ for small $y$, the amplification function can be simplified to

$$|F(\omega)| \approx \frac{1}{\sqrt{\cos^2(\omega H / V_s) + (\xi \omega H / V_s)^2}} \tag{7.14}$$

for small damping ratios. Equation (7.14) indicates that amplification by a damped soil layer also varies with frequency. The amplification will reach a local maximum whenever $kH = \omega H / V_s = n\pi/2 + n\pi$ but will never reach a value of infinity since (for $\xi > 0$) the denominator will always be greater than zero. The frequencies that correspond to the local maxima are the natural frequencies of the soil deposit. As discussed in Section C.6.1.2, the lowest natural frequency is the fundamental frequency ($f_0 = V_s/4H$) and its corresponding period is the characteristic site period ($T_s = 4H/V_s$). The variation of amplification factor with frequency is shown for different levels of damping in Figure 7.11. This amplification factor is also equal to the ratio of the free surface motion amplitude to the bedrock (or bedrock outcropping) motion amplitude. Comparing Figures C.28 and 7.11 shows that damping clearly reduces amplification and does so more strongly at high frequencies than at lower frequencies. High-frequency motions have shorter wavelengths than low-frequency motions, so a high-frequency component undergoes more "cycles" of stress and strain over the thickness of the soil layer than does a low-frequency component of the motion. As a result, it dissipates more energy and hence exhibits a greater reduction in amplitude, than the low-frequency component that travels the same distance. As the frequency approaches zero, the value of $|F_1(\omega)|$ approaches 1.0, which indicates that little to no amplification of the base motion should be expected at frequencies well below the fundamental frequency (or periods well above the characteristic site period). For very low frequencies, wavelengths will be long relative to the thickness of the soil and the entire soil profile will tend to move in a nearly rigid-body fashion – the ground surface motion will be very similar to the bedrock motion. In reality, however, mechanisms not accounted for in one-dimensional analyses, subsequently discussed in Section 7.6, can cause some amplification of long-period motions.

FIGURE 7.11 Influence of frequency on the steady-state response of damped, linear elastic layer.

FIGURE 7.12 Displacement patterns for standing waves at fundamental ($n = 0$), second ($n = 1$), and third ($n = 2$) natural frequencies for a soil layer with $\xi = 5\%$. Displacements are normalized by maximum displacement at the fundamental frequency.

When subjected to harmonic input motion at each natural frequency, a standing wave, i.e., a wave in which the amplitude at each depth is constant, will develop in the soil. Normalized deformed shapes, or mode shapes, for the first three natural frequencies of a simple, uniform layer are shown in Figure 7.12. Note that the soil displacements are in phase at all depths in the fundamental mode, but not in the higher modes. At frequencies above the fundamental frequency, part of the soil deposit may be moving in one direction while another part is moving in the opposite direction. This phenomenon must be considered in the evaluation of inertial forces in soil masses required for seismic stability analyses (Chapter 10). The mode shapes reflect the contributions of both upward- and downward-traveling waves. At some depths, the waves interfere constructively and produce local peaks in displacement amplitude; at other depths, the waves can interfere in a destructive manner with the downward-traveling waves canceling out the upward-traveling waves. At these nodes, the response amplitude reaches a local minimum (zero amplitude if undamped). The amplitude of the transfer function between the depth of a node and the ground surface is infinite if damping is zero, but finite in the presence of damping due to phase lags between motions at different depths. The fact that the amplitude of motion at a node is zero, however, should not be taken to imply that waves (and energy) are not passing through those points; the nodes are specific to particular modal excitation frequencies and will not be present for other excitation frequencies. Transfer functions computed as ratios of surface-to-downhole motions recorded at vertical arrays can have strong peaks and troughs caused by constructive and destructive interference of upward- and downward-traveling waves. Note that the displacement amplitude of the fundamental mode is considerably greater than that of any of the higher modes. The displaced shape of the fundamental mode is described by the first quarter-cycle of a cosine function, i.e., bedrock is at a depth equal to one-quarter of the wavelength of the fundamental mode. The degree of peak amplification, therefore, depends on the characteristics of the material within the upper quarter-wavelength of the motion. That depth, however, is different for different frequencies – shallower for high frequencies and deeper for low frequencies. That fact is helpful in developing an intuitive understanding of how sites are likely to respond during earthquake shaking – higher frequencies are affected by shallower material and lower frequencies are affected by deeper materials. For the purposes of the simple transfer functions described in this section, the shear modulus of the soil was assumed constant. For most actual profiles, however, stiffness tends to increase with depth. As evidence of the importance of the characteristic site period, consider the response measured in Mexico City (Figure 7.4) in the 1985 Michoacán earthquake. As discussed in Section 7.2.2, the SCT site was underlain by 35–40 m (115–131 ft) of soft clay with an average shear wave velocity of about 75 m/s (250 ft/s). As a result, its characteristic site period was $T_s = 4H/V_s = 4(37.5\,\text{m})/(75\,\text{m/s}) = 2$ sec, a value consistent with a strong local peak in the rock motion illustrated by the UNAM response spectrum.

FIGURE 7.13 Illustration of effects of soft clay thickness on response spectrum amplitude and shape from Mexico City ground motion recordings. (After Dobry and Iai, 2000 [@DobryIai2000]; used with permission of CRC Press.)

Figure 7.13 shows the response spectra from the UNAM and SCT sites, along with spectra from two other sites underlain by greater thicknesses of soft clay. As the thickness of the clay increased, the characteristic site periods of the various soil profiles lengthened, and the strongest levels of amplification were pushed to longer periods – 2.6 sec for the CAF site and 3.7 sec for the CAO site. The CAF and CAO motions are strongest at their respective characteristic site periods, but did not rise to the level of the SCT site because the intensity of the rock motion (see UNAM spectrum) decreased at periods beyond about 2 sec. Figure 7.14 shows computed transfer functions and ground surface response spectra for three sites consisting of 30 m of soil with different shear wave velocities, each constant with depth and underlain by a rigid base. The velocities correspond to the centers of ASCE-7 (2022) [@ASCE2022] Site Classes C, D, and E and the soils are assumed to exhibit linear behavior with 5% damping. The three profiles were subjected to the same base motion – a recorded earthquake motion from Taft Lincoln School in the 1952 Kern County earthquake ($M_w$ 7.4). With velocities of 560, 270, and 150 m/s, the characteristic site periods can be computed ($T_s = 4H/V_s$) as 0.214, 0.444, and 0.800 sec. The three transfer functions, plotted here as functions of period rather than frequency, confirm those characteristic site periods and show that the stiffest profile amplified the lower period (higher frequency) components of the motion most strongly, and that the softest profile amplified the longer period (lower frequency) components most strongly. The nature of the amplification can be seen in the ground surface response spectra, each of which has a peak near the fundamental period of the profile. Since spectral acceleration is influenced by multiple frequencies, the amplitude and period of a particular peak in a response spectrum are not uniquely related to specific peaks in the transfer function. The acceleration histories show significant differences in amplitude and frequency content. Note that while amplification of the $V_s = 270$ m/s profile is approximately equivalent to that of the stiffer or softer profiles, the $V_s = 270$ m/s profile produces the largest response spectra. This occurs because the rock spectrum has its largest amplitudes at periods in the vicinity of the characteristic site period of the $V_s = 270$ m/s profile. The case of a perfectly uniform layer of viscoelastic material on a rigid base is not realistic, even within the constraints of one-dimensional analyses. Rock is never perfectly rigid and soil properties, particularly soil stiffness, usually vary with depth. The basic principles of wave propagation described in Appendix C, however, can be used to account for these factors in one-dimensional ground response analyses.

FIGURE 7.14 Effects of profile stiffness on ground surface response: (a) ground surface response spectra, (b) transfer functions, (c) ground surface acceleration for $V_s = 560$ m/s profile, (d) ground surface acceleration for $V_s = 270$ m/s profile, (e) ground surface acceleration for $V_s = 150$ m/s profile.

### Example 7.2

The site at which the Gilroy No. 2 motion from the Loma Prieta earthquake was recorded is near the location of the Gilroy No. 1 motion recording and underlain by some 540 ft of soil underlain in turn by shale and serpentinite bedrock. The shear wave velocity of the soil varies from about 300 to 600 m/s with an average velocity of 450 m/s and an average unit weight of 19 kN/m³. Assuming a damping ratio of 5% and rigid bedrock, compute the ground motion that would occur if the bedrock was subjected to the Gilroy No. 1 input motion (Figure E7.2a).

FIGURE E7.2A

**Solution:**

Computation of the ground surface motion from the bedrock motion can be accomplished in the same five steps described in Example 7.2. The only difference is in the transfer function, which is now complex-valued due to the existence of damping.

1. Obtain a digital accelerogram of the input motion; the motion is shown in Figure E7.2b.
2. Compute the Fourier series of the input motion. The one-sided Fourier spectrum is shown in Figure E7.2c.
3. Compute the transfer function that relates the ground surface (output) motion to the bedrock (input) motion. The modulus (amplitude) of the complex-valued transfer function is shown in Figure E7.2d. The shape of the transfer function indicates that significant amplification will occur at several natural frequencies, and that higher frequencies (greater than about 10 Hz) will be deamplified.
4. Compute the Fourier series of the ground surface (output) motion as the product of the transfer function and the Fourier series of the bedrock (input) motion. The Fourier spectrum of the ground surface motion (Figure E7.2e) shows amplification at the natural frequencies of the soil deposit and little high-frequency motion.
5. Obtain the time series of the ground surface motion (Figure E7.2f) of the ground surface motion by inverting the Fourier series. The peak accelerations at the ground surface and bedrock levels are similar, but the frequency contents are different. Because the ground surface motion is weighted toward lower frequencies, the peak velocity and displacement at the ground surface are likely to be considerably greater than at bedrock.

The rigid base analysis predicts a peak ground surface acceleration of 0.452g, which is considerably greater than the peak acceleration of 0.322g actually recorded at the Gilroy No. 2 station.

FIGURE E7.2B-F

### 7.5.1.3 Damped Soil on Elastic Bedrock

Section 7.5.1.2 described the response of a viscoelastic layer on rigid bedrock. If the bedrock is rigid, its motion will be unaffected by motions in (or even the presence of) the overlying soil – it acts as a fixed end (Section C.4.1) boundary. Any downward-traveling waves in the soil will be completely reflected back toward the ground surface by the rigid layer, thereby trapping all of the elastic wave energy within the soil layer. If the rock is elastic, however, downward-traveling stress waves that reach the soil/rock boundary will be only partially reflected; part of their energy will be transmitted through the boundary to continue traveling downward through the rock. If the rock extends to great depth (large enough that waves reflected from any deeper material boundaries do not return to the soil-rock boundary soon enough, or with sufficient amplitude, to influence the response of the soil deposit), the elastic energy of these waves will effectively be removed from the soil layer. This is a form of radiation damping, and it causes the free surface motion amplitudes to be smaller than those for the case of rigid bedrock. Consider the case of a viscoelastic soil layer overlying a halfspace of viscoelastic rock (Figure 7.15). If the subscripts $s$ and $r$ refer to soil and rock, respectively, the displacements due to vertically propagating S-waves in each material can be written as

$$u_s(z_s, t) = A_s e^{i(\omega t + k_s^* z_s)} + B_s e^{i(\omega t - k_s^* z_s)} \tag{7.15a}$$

$$u_r(z_r, t) = A_r e^{i(\omega t + k_r^* z_r)} + B_r e^{i(\omega t - k_r^* z_r)} \tag{7.15b}$$

The free surface effect (Section C.6.1.2) requires that $A_s = B_s$ and compatibility of displacements and continuity of stresses at the soil-rock boundary require that

$$u_s(z_s = H) = u_r(z_r = 0) \tag{7.16}$$

$$\tau_s(z_s = H) = \tau_r(z_r = 0) \tag{7.17}$$

Substituting Equations (7.15) into Equation (7.16) yields

$$A_s\!\left(e^{-ik_s^*H} + e^{ik_s^*H}\right) = A_r + B_r \tag{7.18}$$

From Equation (7.17) and the definition of shear stress ($\tau = G \,\partial u/\partial z$)

$$A_s G_s^* k_s^*\!\left(e^{-ik_s^*H} - e^{ik_s^*H}\right) = G_r^* k_r^*(A_r - B_r) \tag{7.19}$$

or

$$\frac{G_s^* k_s^*}{G_r^* k_r^*} A_s\!\left(e^{-ik_s^*H} - e^{ik_s^*H}\right) = A_r - B_r \tag{7.20}$$

FIGURE 7.15 Nomenclature for the case of a soil layer overlying a halfspace of elastic rock.

The ratio of the products of shear modulus and wavenumber can be written as

$$\alpha_z = \frac{G_s^* k_s^*}{G_r^* k_r^*} = \frac{\rho_s V_{ss}^*}{\rho_r V_{sr}^*} \tag{7.21}$$

where $V_{ss}^*$ and $V_{sr}^*$ are the complex shear wave velocities of the soil and rock, respectively, and $\alpha_z$ is the complex impedance ratio (see Section C.4.1). Solving Equations (7.18) and (7.20) simultaneously gives

$$A_r = \frac{1}{2} A_s\!\left[(1+\alpha_z)e^{ik_s^*H} + (1-\alpha_z)e^{-ik_s^*H}\right] \tag{7.22a}$$

$$B_r = \frac{1}{2} A_s\!\left[(1-\alpha_z)e^{ik_s^*H} + (1+\alpha_z)e^{-ik_s^*H}\right] \tag{7.22b}$$

Suppose that a vertically propagating shear wave of amplitude, $A$, traveled upward through the rock. If the soil was not present, the free surface effect at the rock outcrop would produce a bedrock outcropping motion of amplitude $2A$. With the soil present, however, the free surface motion amplitude would be

$$A_s = \frac{2A}{(1+\alpha_z)e^{ik_s^*H} + (1-\alpha_z)e^{-ik_s^*H}} \tag{7.23}$$

Defining the transfer function, $F_3$, as the ratio of the soil surface amplitude to the rock outcrop amplitude,

$$F_3(\omega) = \frac{A_s}{A} = \frac{2}{(1+\alpha_z)e^{ik_s^*H} + (1-\alpha_z)e^{-ik_s^*H}} \tag{7.24}$$

which, using Euler's law, can be rewritten as

$$F_3(\omega) = \frac{1}{\cos(k_s^* H) + i\alpha_z \sin(k_s^* H)} \tag{7.25}$$

The modulus of $F_3(\omega)$ cannot be expressed in a very compact form when soil damping exists. To illustrate the important effect of bedrock elasticity, however, the amplification factor for undamped soil can be expressed as

$$|F_3(\omega)| = \frac{1}{\sqrt{\cos^2(kH) + \alpha_z^2 \sin^2(kH)}} \tag{7.26}$$

Note that unbounded resonance cannot occur – the denominator is always greater than zero, even when the soil is undamped. The effect of the bedrock stiffness, as characterized by the impedance ratio, on amplification behavior is illustrated in Figure 7.16. Note the similarity between the effects of soil damping and bedrock stiffness by comparing the shapes of the amplification factor curves in Figure 7.16 and those in Figure 7.11. The elasticity of the rock affects amplification similarly to the damping ratio of the soil – both prevent the denominator from reaching zero – although the bedrock stiffness effect does not diminish with increasing frequency. This radiation damping effect has significant practical importance. In the western United States, where bedrock is often not particularly stiff in many cases, the impedance ratio is large, allowing transmission of a larger proportion of downward-traveling waves into the bedrock and leading to substantial radiation damping which reduces site response. On the other hand, in the eastern United States, harder bedrock leads to lower impedance ratios, greater reflection of downward-traveling waves, and reduced radiation damping. This produces transfer functions with strong local peaks (as in Figure 7.16) that produce greater amplification at certain frequencies. As a result of these differences, design criteria established on the basis of empirical evidence from western earthquakes may be biased in the east.

FIGURE 7.16 Effect of impedance ratio on amplification factor for case of undamped soil.

FIGURE 7.17 Effects of bedrock stiffness on ground surface response to Taft rock outcrop motion: (a) ground surface response spectra, (b) transfer functions, (c) ground surface acceleration for $V_s = 1{,}600$ m/s bedrock, (d) ground surface acceleration for $V_s = 760$ m/s bedrock, (e) ground surface acceleration for $V_s = 500$ m/s bedrock.

When performing site response analyses using recorded outcrop motions, the halfspace stiffness should be consistent with the stiffness of the material at the base of the modeled soil column. Figure 7.17 shows the results of analyses in which the same rock outcrop motion was applied to the same soil profile (constant $V_s = 270$ m/s) underlain by bedrock with three different stiffnesses – $V_{sr} = 1{,}600$, $V_{sr} = 760$, and $V_{sr} = 500$ m/s. Because the bedrock stiffnesses are different, the within-profile bedrock motions are different, as indicated by the different rock spectra (bold lines in Figure 7.17a). The behavior of the soil profile was the same for each case, as evidenced by the identical transfer functions, but the resulting ground surface motions are also significantly different; as should be expected, the amplitude of the surface motion increases with increasing rock stiffness. The sensitivity to bedrock stiffness decreases, however, as the difference between the rock and soil stiffness increases. It is also useful to consider the nature of the waves in the halfspace below the soil profile. Consider a variation of the condition in Figure 7.15 in which the soil above the halfspace is removed; for this case, the upward- and downward-traveling wave amplitudes are denoted $A_r^*$ and $B_r^*$, respectively. Because the upward-traveling wave would be perfectly reflected at the free surface of the halfspace (as a downward-traveling wave of amplitude $B_r^* = A_r^*$), the total displacement at the free surface would be $2A_r^*$. With the soil layer present (for which the $*$ notation is dropped, as in Figure 7.15), some of the upward-traveling waves will be transmitted into the overlying soil, which affects the wave reflected off the soil-rock interface so that $B_r \neq A_r$. Because the upward-traveling wave in the halfspace is the same for both cases, $A_r = A_r^*$ (assuming the halfspace has the same properties in both cases), but the motions at the top of the halfspace will be different for the two cases because of the differences in the reflected motions. The motions can be related by the transfer function

$$F_{rr} = \frac{u_r}{u_r^*} = \frac{A_r + B_r}{A_r^*} \tag{7.27}$$

This transfer function is most commonly applied to determine the characteristics of the within-profile motion that is consistent with a recorded outcrop motion. If the recorded motion is from a rock outcrop with stiffness and density equal to that below a profile of interest, the response of the profile can be analyzed by applying the within-profile motion at the base of the soil column. The within-profile motion will be weaker than the recorded outcrop motion, principally at the natural frequencies of the soil profile and by amounts that increase with increasing damping and decreasing (soil/rock) impedance ratio. Most ground response analysis programs have provisions for computing the within-profile motion from an outcrop motion and therefore allow the outcrop motion to be specified as the input motion. If this is done, it is critical to specify that the input motion is an outcrop motion; otherwise, the full motion, including the free surface effect, will be imposed at the bedrock level.

### Example 7.3

Repeat Example 7.2 assuming that the bedrock is not rigid. Assume a shear wave velocity of 760 m/s, a unit weight of 25 kN/m³, and 2% damping for bedrock at the site shown in Figure E7.3a.

FIGURE E7.3A

**Solution:**

Computation of the ground surface motion from the bedrock motion can be accomplished in the same five steps described in Example 7.3. The only difference is that the transfer function in this example will include the effects of bedrock compliance. Figure E7.3b–f shows the input motion, transfer function, and output motion in the same format as the preceding two examples. The transfer function for the compliant base case in this example is weaker than that of Example 7.2 and the resulting ground surface motion is also significantly weaker (note differences in ordinate scales used in plots). The compliant bedrock analysis predicts a peak ground surface acceleration of 0.339g, which agrees well with the peak acceleration of 0.322g recorded at the Gilroy No. 2 station. The good agreement between peak accelerations, however, does not mean that this simple analysis has predicted all aspects of the Gilroy No. 2 motion well.

FIGURE E7.3B-F

The compliant bedrock analysis predicts a peak ground surface acceleration of 0.339g, which agrees well with the peak acceleration of 0.322g recorded at the Gilroy No. 2 station. The good agreement between peak accelerations, however, does not mean that this simple analysis has predicted all aspects of the Gilroy No. 2 motion. Comparison of the Fourier amplitude spectrum of the predicted motion (Figure E7.3e) with that of the recorded motion shows significant differences in frequency content.

### 7.5.1.4 Layered Soil on Elastic Rock

Real ground response problems usually involve soil deposits with stiffness and damping characteristics that vary with depth, either due to the layering of different materials or depth-dependence within individual layers. Elastic wave energy will be reflected and/or transmitted at the boundaries between these layers. Such conditions require the development of transfer functions for layered soil deposits.

FIGURE 7.18 Nomenclature for layered soil deposit on elastic bedrock.

Consider a soil deposit consisting of $N$ horizontal layers where the $N$th layer is bedrock (Figure 7.18). Assuming that each layer of soil behaves as a Kelvin-Voigt solid, the wave equation is of the form given in Equation (C.124). The solution to the wave equation can be expressed in the form

$$u(z,t) = A e^{i(\omega t + k^* z)} + B e^{i(\omega t - k^* z)} \tag{7.28}$$

where $A$ and $B$ represent the amplitudes of waves traveling in the $-z$ (upward) and $+z$ (downward) directions, respectively. The shear stress is then given by the product of the complex shear modulus, $G^*$, and the shear strain, so

$$\tau(z,t) = G^* \frac{\partial u}{\partial z} = (G + i\omega\eta) \frac{\partial u}{\partial z} \tag{7.29}$$

where $\eta$ is the viscosity of the material (Section C.5.1). Introducing a local coordinate system, $Z$, for each layer, the displacement at the top and bottom of layer $m$ will be

$$u_m(Z=0, t) = (A_m + B_m)e^{i\omega t} \tag{7.30a}$$

$$u_m(Z=h_m, t) = \left(A_m e^{-ik_m^* h_m} + B_m e^{ik_m^* h_m}\right)e^{i\omega t} \tag{7.30b}$$

Displacements at layer boundaries must be compatible (i.e., the displacement at the top of a particular layer must be equal to the displacement at the bottom of the overlying layer). Applying the compatibility requirement to the boundary between layer $m$ and layer $m + 1$, i.e.,

$$u_m(Z=h_m, t) = u_{m+1}(Z=0, t) \tag{7.31}$$

yields

$$A_m e^{-ik_m^* h_m} + B_m e^{ik_m^* h_m} = A_{m+1} + B_{m+1} \tag{7.32}$$

The shear stresses at the top and bottom of layer $m$ are

$$\tau_m(Z=0, t) = -ik_m^* G_m^* (A_m - B_m)e^{i\omega t} \tag{7.33a}$$

$$\tau_m(Z=h_m, t) = -ik_m^* G_m^* \left(A_m e^{-ik_m^* h_m} - B_m e^{ik_m^* h_m}\right)e^{i\omega t} \tag{7.33b}$$

Since stresses must be continuous at layer boundaries,

$$\tau_m(Z=h_m, t) = \tau_{m+1}(Z=0, t) \tag{7.34}$$

so

$$\frac{k_m^* G_m^*}{k_{m+1}^* G_{m+1}^*}\left(A_m e^{-ik_m^* h_m} - B_m e^{ik_m^* h_m}\right) = A_{m+1} - B_{m+1} \tag{7.35}$$

Adding (7.32) and (7.35) and subtracting (7.35) from (7.32) gives the recursion formulas

$$A_{m+1} = \frac{1}{2} A_m (1+\alpha_m) e^{-ik_m^* h_m} + \frac{1}{2} B_m (1-\alpha_m) e^{ik_m^* h_m} \tag{7.36a}$$

$$B_{m+1} = \frac{1}{2} A_m (1-\alpha_m) e^{-ik_m^* h_m} + \frac{1}{2} B_m (1+\alpha_m) e^{ik_m^* h_m} \tag{7.36b}$$

where $\alpha_m$ is the complex impedance ratio at the boundary between layers $m$ and $m + 1$

$$\alpha_m = \frac{k_m^* G_m^*}{k_{m+1}^* G_{m+1}^*} = \frac{\rho_m v_{sm}^*}{\rho_{m+1} v_{s,m+1}^*} \tag{7.37}$$

This means that, if the motion in layer $m$ is known and the material properties of layers $m$ and $m + 1$ are known, the motion in layer $m + 1$ can be determined. The process can obviously be repeated to obtain the motions in layers $m + 2$, $m + 3$, etc. At the ground surface, the shear stress must be equal to zero, which requires [from Equation 7.33a, setting $m = 1$] that $A_1 = B_1$. If the recursion formulas of Equation (7.36) are applied repeatedly for all layers from 1 to $m$, functions relating the amplitudes in layer $m$ to those in layer 1 can be expressed by

$$A_m = a_m(\omega) A_1 \tag{7.38a}$$

$$B_m = b_m(\omega) B_1 \tag{7.38b}$$

The transfer function relating the displacement amplitude at layer $i$ to that at layer $j$ is given by

$$F_{ij}(\omega) = \frac{u_i}{u_j} = \frac{a_i(\omega) + b_i(\omega)}{a_j(\omega) + b_j(\omega)} \tag{7.39}$$

Because $\ddot{u} = -\omega^2 u$ for harmonic motion, Equation (7.39) also describes the amplification of accelerations and velocities from layer $i$ to layer $j$. Equation (7.39) indicates that the motion in any layer can be determined from the motion in any other layer. Hence if the motion at any one point in the soil profile is known, the motion at any other point can be computed.

### Example 7.4

As part of a comprehensive investigation of ground motion estimation techniques, the Electric Power Research Institute performed a detailed subsurface investigation at the site of the Gilroy No. 2 recording station [@EPRI1993]. A rough approximation to the measured shear wave velocity profile is listed below.

Depth Range (ft) | Average Shear Wave Velocity (ft/s)
0–20: —
20–45: —
45–70: 1,500
70–130: 1,000
130–540: 2,000
> 540: 5,000

Assuming, as in Examples 7.2 and 7.3, an average soil unit weight of 125 lb/ft³ and 5% soil damping, compute the expected ground surface response when the bedrock is subjected to the Gilroy No. 1 motion.

**Solution:**

As in the previous two examples in this chapter, this problem requires evaluation of the transfer function that relates the ground surface motion to the bedrock motion. Because of multiple reflections within the layered system, the transfer function (Equation 7.39) for this example is considerably more complicated than for the single-layered cases of the previous examples. While the transfer function can be evaluated by hand, it has also been coded in computer programs. The program ProShake 2.0 (www.proshake.com) was used, with constant soil stiffness and damping ratio, to obtain the transfer function shown in Figure E7.4c. As in the previous examples, the Fourier series of the ground surface motion (Figure E7.4d) was computed as the product of the transfer function and the Fourier series of the input motion. Inversion of this Fourier series produces the time series of ground surface acceleration (Figure E7.4e). Examination of Figure E7.4c shows that the transfer function for the layered system is indeed more complicated than the transfer functions for the single-layered cases of Examples 7.2 and 7.3. Resonances producing narrow, high spikes in the transfer function at frequencies of about 1.3, 3.5, and 5.5 Hz help produce a peak acceleration of 0.499g, which is considerably larger than the peak acceleration of 0.322g that was recorded at the Gilroy No. 2 station.

FIGURE E7.4A-E
