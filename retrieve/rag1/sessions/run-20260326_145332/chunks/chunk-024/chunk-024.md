Combining expressions for the flexible base (Equation 8.6) and fixed-base (Equation 8.3) natural periods, the period ratio can be expressed as

$$\frac{\tilde{T}}{T} = \sqrt{1 + \frac{k}{k_x} + \frac{kh^2}{mk_{yy}}} \quad (8.7)$$

which simplifies into the classical period lengthening expression [@VeletsosMeek1974]:

$$\frac{\tilde{T}}{T} = \sqrt{1 + \frac{k}{k_x} + \frac{kh^2}{k_{yy}}} \quad (8.8)$$

For consistency with SSI literature, the subscript "0" is dropped from the vibration periods in Equations (8.7) and (8.8). Note that $\tilde{T}/T$ goes to 1.0 as $k_x$ and $k_{yy}$ go to infinity (i.e., the fixed-base case), but is otherwise always greater than 1.0, indicating that the fundamental period of the soil-structure system will be greater than that of the fixed-base system. Equation (8.8) can be applied to multi-degree-of-freedom structures by taking the height, $h$, as the height of the center of mass for the first-mode shape (usually about two-thirds of the overall structure height). In such cases, period lengthening applies mainly to the first-mode period because higher modes produce relatively limited base shear and moment in most cases.

The dimensionless parameters controlling period lengthening of a rectangular structure with base dimensions $2B \times 2L$ are: $h/(V_s T_0)$, $h/B$, $B/L$, $m/(\rho_s BLh)$, and $\nu$, where $h$ is the structure height (or height to the center of mass of the first-mode shape), $\rho_s$ is the soil mass density, and $\nu$ is the Poisson's ratio of the soil. Note that it is common in SSI to denote $B$ and $L$ as the half-dimensions of rectangular foundations with $B \leq L$, which is different than the full dimensions commonly used in foundation engineering. To the extent that $h/T_0$ quantifies the stiffness of the superstructure, the term $h/(V_s T_0)$ represents the structure-to-soil stiffness ratio. The term $h/T_0$ has units of velocity, and will be larger for stiff lateral force resisting systems, such as shear walls, and smaller for flexible structural systems, such as moment frames. The shear wave velocity, $V_s$, is closely related to soil shear modulus, $G$, being $V_s = \sqrt{G/\rho}$ (Eq. 6.76). For typical building structures on soil and weathered rock sites, $h/(V_s T_0)$ is less than 0.1 for moment frame structures, and between approximately 0.1 and 0.5 for shear wall and braced frame structures [@StewartEtAl1999b]. Period lengthening increases markedly with increasing structure-to-soil stiffness ratio, which is the most important parameter controlling inertial SSI effects. The structure aspect ratio, $h/B$, and foundation aspect ratio, $B/L$, describe the geometry of the soil-structure system. The mass ratio, $m/(\rho_s 4BLh)$, is the ratio of structure mass to the mass of soil in a volume extending to a depth equal to the structure height, $h$, below the foundation plan area. Equation (8.8) shows that period lengthening has no fundamental dependence on mass. The mass ratio term was introduced so that period lengthening could be related to easily recognizable characteristics such as structural first-mode period, $T_0$, and soil shear wave velocity, $V_s$, rather than structural stiffness, $k$, and soil shear modulus, $G$. The effect of mass ratio is modest, and it is commonly taken as 0.15 [@VeletsosMeek1974]. Using models for the stiffness of rectangular foundations (of half-width, $B$; half-length, $L$) resting on a homogeneous isotropic half-space with shear wave velocity, $V_s$, computed period lengthening ratios are shown for the special case of a square footing ($L = B$) in Figure 8.6a. All other factors being equal, period lengthening increases with the structure aspect ratio (i.e., increasing $h/B$), due to increased rocking caused by increased overturning moments. This implies that inertial SSI effects would be more significant in tall buildings, which is actually not the case. Tall buildings typically have low $h/(V_s T_0)$ ratios, which have a greater influence on inertial SSI effects. Hence, period lengthening in tall buildings is near unity. For a fixed structure aspect ratio, period lengthening decreases modestly with increasing foundation aspect ratio (i.e., increasing $B/L$) due to increased foundation size (and therefore stiffness) normal to the direction of loading.

In addition to period lengthening, system behavior is also affected by damping associated with soil-foundation interaction. The contribution of soil-foundation interaction to system damping is referred to as foundation damping, $\xi_f$. This damping has contributions from soil hysteresis (hysteretic damping) and radiation of energy, in the form of stress waves, away from the foundation (radiation damping). The flexible-base system damping, $\tilde{\xi}_0$, is related to $\xi_f$ and fixed-base structural damping $\xi_i$ as:

$$\tilde{\xi}_0 = \xi_f + \xi_i \left(\frac{T}{\tilde{T}}\right)^n \quad (8.9)$$

The fixed-base structural damping depends on structural system type and configuration [@ATC2010], but is often taken by default as 5%. Observations from case studies have shown that $\xi_f$ ranges from approximately 0% to 25% [@StewartEtAl1999b]. The exponent, $n$, on the period lengthening term in Equation (8.9) is 3 for ideally viscous material damping and is 2 otherwise [@GivensEtAl2016]. Use of $n = 2$ is recommended.

**Figure 8.6.** Plot of period lengthening ratio ($\tilde{T}/T$) and foundation damping $\xi_f$ versus structure-to-soil-stiffness ratio $h/(V_s T)$ for square foundations ($L = B$) and varying structure aspect ratios, $h/B$. In this plot, $\nu = 0.33$, $B/L = 1.0$, hysteretic soil damping $\xi_s = 0$, mass ratio = 0.15, and exponent $n = 2$ (see Equations 8.9 and 8.10). (Figure modified from [@NIST2012].)

### Example 8.1

Consider the simple structure in Figure E8.1 on a square foundation, $L/B = 1.0$. Find the fixed-base period ($T_0$), flexible-base period ($\tilde{T}$), and flexible-base damping ratio ($\tilde{\xi}_0$).

**Figure E8.1.** Soil-structure system considered in Example 8.1.

#### Solution

The fixed-base period is computed from Equation (8.3) as $T_0 = 2\pi\sqrt{m/k} = 0.34\ \text{sec}$.

Period lengthening can be evaluated from Figure 8.6 if the structure-to-soil stiffness ratio and structure aspect ratio are known. The structure-to-soil stiffness ratio is $h/(V_s T_0) = 0.35$. The structure aspect ratio is $h/B = 1.0$. From Figure 8.6, period lengthening $\tilde{T}/T$ is found to be 1.5 (by convention, the "0" subscript is dropped from the periods in $\tilde{T}/T$). The foundation damping $\xi_f = 0.2$.

The flexible-base period can then be computed as $\tilde{T} = 1.5 \times 0.34 = 0.51\ \text{sec}$.

The flexible-base damping is computed using Equation (8.9) as $\tilde{\xi}_0 = \xi_f + \xi_i(\tilde{T}/T)^{-n} = 0.22$.

In this example, the period is appreciably lengthened and the damping increases by more than a factor of four. Most building structures do not have such large effects of inertial interaction.

[@GivensEtAl2016] derived analytical models for foundation damping, while also explaining differences between foundation damping equations presented in prior studies [@VeletsosNair1975; @Bielak1975; @Roesset1980; @Wolf1985; @MaravasEtAl2014]. A suitable solution for the foundation damping ratio, $\xi_f$, for most applications is given by:

$$\xi_f = \left[(\xi_x + \xi_s)\left(\frac{T_x^*}{\tilde{T}}\right)^n + (\xi_{yy} + \xi_s)\left(\frac{T_{yy}^*}{\tilde{T}}\right)^n\right] \quad (8.10)$$

where $\xi_s$ is soil hysteretic damping ratio (Section 6.6.4 and Table 8.1), $\xi_x$ and $\xi_{yy}$ are damping ratios related to radiation damping from translational and rotational modes (described further in Section 8.3.2), and $n$ should generally be taken as 2. The periods $T_x^*$ and $T_{yy}^*$ are complex-valued fictitious vibration periods for foundation vibration (their amplitude, as used in Equation (8.10), would represent actual system period if the superstructure were rigid and the respective foundation vibrations were the only available degrees of freedom of a fictitious SDOF system):

$$T_x^* = 2\pi\sqrt{\frac{m}{|k_x^*|}}, \qquad T_{yy}^* = 2\pi\sqrt{\frac{mh^2}{|k_{yy}^*|}} \quad (8.11)$$

In Equation (8.11), $|k_j^*|$ (where $j$ refers to the $x$ or $yy$ indices) is the amplitude of a complex-valued impedance function, as described further in Section 8.3.2.

Figure 8.6b shows that foundation damping, $\xi_f$, increases with increasing structure-to-soil-stiffness ratio, $h/(V_s T_0)$, and decreases with increasing structure aspect ratio, $h/B$. The decrease of $\xi_f$ with aspect ratio indicates that lateral movements of the foundation (which dominate at low $h/B$) dissipate energy into soil more efficiently than foundation rocking (which dominates at high $h/B$). The radiation damping terms, $\xi_x$ and $\xi_{yy}$, are reduced significantly when a stiff bedrock layer is encountered at moderate or shallow depths, as described further in Section 8.3.2.2.

Analysis procedures for $\tilde{T}/T$ and $\xi_f$ similar to those described above have been validated relative to observations from instrumented buildings shaken by earthquakes [@StewartEtAl1999a; @StewartEtAl1999b]. These case studies confirm the analytical finding that the single most important parameter controlling the significance of inertial interaction is $h/(V_s T_0)$, and that inertial SSI effects are generally negligible for $h/(V_s T_0) < 0.1$, which occurs in flexible structures, such as moment frame buildings, located on competent soil or rock. Conversely, inertial SSI effects tend to be significant for stiff structures, such as shear wall or braced frame buildings, located on softer soils. Many of the early advances in understanding and analysis of SSI, in fact, came from the nuclear power industry where stiff structures must be designed for extremely high performance standards.

**Figure 8.7.** Illustration of effects of period lengthening and change of damping on fundamental mode spectral acceleration from which base shear is evaluated. Solid curve represents spectrum for fixed-base damping ratio. Dashed curve represents spectrum at increased damping ratio associated with a flexible-base case.

The effect of inertial SSI on the peak base shear that develops in a structure is illustrated in Figure 8.7. Because base shear for elastic response is commonly computed based on first-mode spectral acceleration, the figure depicts the variation in spectral acceleration versus normalized period on a log scale. The spectra are drawn for two effective damping ratios corresponding to flexible-base ($\tilde{\xi}_0$) and fixed-base ($\xi_i$) conditions. The spectral acceleration for a flexible-base structure, $\tilde{S}_a$, is obtained by entering the spectrum (dashed curve) drawn for damping ratio $\tilde{\xi}_0$ at the corresponding elongated period, $\tilde{T}$. The fixed-base counterpart is obtained using the spectral acceleration for the fixed-base period (indicated without the tilde symbol) and the fixed-base damping. The effect of SSI on base shear is influenced by the slope of the spectrum. Base shear tends to increase when the slope is positive and decrease when the slope is negative. Case A represents buildings with relatively long periods (e.g., $T_A$ in Figure 8.7) on the descending portion of the spectrum; use of $\tilde{S}_a(A)$ (flexible-base $S_a$ ordinate) in lieu of the fixed-base ordinate typically results in reduced base shear demand. Case B represents a short-period structure ($T_B$ in Figure 8.7) on the ascending branch of the spectrum where, despite the effects of increased damping, period lengthening causes inertial SSI to increase the base shear.

### Example 8.2

The structure described in Example 8.1 is subject to design ground motions with the response spectra shown in Figure E8.2. Note that the spectra are provided for two damping ratios corresponding to fixed- and flexible-base conditions. What is the change in the design spectral acceleration that would be achieved by considering inertial soil–structure interaction (SSI)?

**Figure E8.2.** Effect of period lengthening and foundation damping on the first-mode spectral acceleration.

#### Solution

From Example 8.1, the fixed- and flexible-base natural periods of the system were 0.34 and 0.51 sec, respectively. As shown by the solid dot in the plot, the fixed-based spectral acceleration is 0.49g for the fixed-base case, in which the damping ratio is 5%. For the flexible-base case, the spectrum is drawn at a higher damping ratio of 22% and the spectral acceleration at 0.51 sec (open circle) is 0.29g. Hence, the design ground motions are decreased by about 40%, with most of the reduction resulting from the damping increase.

## 8.3.2 Shallow Foundations

The stiffness and damping associated with foundation interaction with supporting soils is a fundamental consideration in SSI analysis. This section describes the factors controlling this interaction and presents models that are used in applications.

### 8.3.2.1 Stiffness and Damping for Rigid Foundations and Uniform Soils

The notion of a complex stiffness that simultaneously represented the stiffness and damping characteristics of an SDOF oscillator is introduced in Section B.6.3. In analogous fashion, complex impedance functions can be used to represent the frequency-dependent stiffness and damping characteristics of soil-foundation interaction. Classical solutions for the complex-valued impedance function can be written as [@LucoWestmann1971; @VeletsosWei1971]:

$$k_j^* = k_j + i\omega c_j \quad (8.12)$$

where $k_j^*$ denotes the complex-valued impedance function for a particular mode of foundation vibration indicated by index $j$ (e.g., $x$ or $yy$), and $k_j$ and $c_j$ denote the frequency-dependent foundation stiffness and dashpot coefficients, respectively. The dashpot with coefficient $c$ represents the effects of damping associated with soil-foundation interaction. An alternative form for Equation (8.12) is

$$k_j^* = k_j(1 + i\xi_j) \quad (8.13)$$

where:

$$\xi_j = \frac{\omega c_j}{k_j} \quad (8.14)$$

which is defined for $k_j > 0$. An advantage of using $\xi_j$ over $c_j$ is that $\xi_j$ can be interpreted as a fraction of critical damping (damping ratio) in the classical sense when a mass is attached to the complex spring and the system oscillates at resonance [@CloughPenzien1993]. The imaginary part of the complex impedance is related to phase difference between harmonic excitation and response at a given frequency, a feature that is usually associated with damping (Section B.6.3). The phase angle, $\phi_j$, between force and (lagged) displacement is [@CloughPenzien1993; @Wolf1985]:

$$\phi_j = \tan^{-1}(\xi_j) \quad (8.15)$$

The angle $\phi_j$ is also known as a loss angle. For example, if $\xi_j$ is 10%, peak harmonic displacement will lag peak force by 11.3° or 0.197 radians. The corresponding time shift between force and displacement depends on oscillation frequency as $\Delta t = \phi_j / \omega$.

To help conceptualize the physical meaning of the complex-valued and frequency-dependent foundation stiffness, it is useful to consider characteristics of foundation load-deformation responses as measured in field tests. Figure 8.8a shows the configuration of a simple test structure resting on soft soil, which was subjected to cyclic forces over a range of frequencies by a shaker mounted on the top slab. Figure 8.8b shows the relationship between foundation rotation and base moment, which can be evaluated for any point in time as the difference between the moment applied by the shaker force and the moments that develop from inertial forces in top and bottom slabs. The "loops" in this figure show the evolution of foundation rotation with base moment over several cycles of shaking; hence time is advancing as one moves along the loops in a clockwise fashion. Figure 8.8c shows a similar result for the base shear-displacement response. Careful interpretation of the rounded tips of the loops in both figures show that the peak load (on y-axis) occurs before the peak deformation (on x-axis) — this offset in time between load and response is a result of damping, and can be assessed either as a time- or frequency-shift per Equation (8.15). Complex numbers are used in the formulation of the stiffness to capture this damping-induced phase shift. With regard to frequency dependence, the loops in Figure 8.8 demonstrate a decrease of secant stiffness as frequency increases from 6 to 7.5 Hz as well as an increase in the relative "fatness" of the loops (which is related to damping; Section 6.6.4). Models for the $k_j$ and $\xi_j$ terms, described below, are intended to capture these features of foundation response.

**Figure 8.8.** (a) Configuration of test structure used for cyclic forced vibration testing of SSI effects (box on roof slab represents shaker, arrows represent measured displacements and rotations); (b) base moment – foundation rotation response at two frequencies (6 Hz is near the system resonance); (c) base shear – foundation displacement response at same frequencies as in (b). (Adapted from data in [@TileyliogluEtAl2011].)

### Example 8.3

Derive the foundation stiffnesses in translation and rotation in response to 6 Hz harmonic loading from the recorded responses of the test structure foundation in Figure 8.8.

#### Solution

The stiffnesses can be measured from the slopes of lines drawn through the tips of the force-displacement and moment-rotation loops, as shown in Figure E8.3.

For the translation case, this slope is $k_x(\omega) = 3\ \text{kN} / (3.0 \times 10^{-3}\ \text{m}) = 1.0 \times 10^3\ \text{kN/m}$.

For the rotation case, this slope is $k_{yy}(\omega) = 12\ \text{kN-m} / (3.3 \times 10^{-3}\ \text{rad}) = 3.6 \times 10^3\ \text{kN-m/rad}$.

**Figure E8.3.** Secant stiffness measurement for Example 8.3.

Many impedance function solutions are available for rigid circular or rectangular foundations located on the surface of, or embedded within, a uniform, elastic, or visco-elastic half-space. In the case of a rigid rectangular foundation resting on the surface of a half-space with shear wave velocity $V_s$, [@PaisKausel1988], [@Gazetas1991], and [@MylonakisEtAl2006] summarize impedance solutions in the literature and present equations for the stiffness and damping terms in Equation (8.12). Solutions for the 2-D case, in which excitation is in the $y$-direction (parallel to the "short" dimension of the footing) are given by [@GazetasRoesset1976] and [@JakubRoesset1977]. These solutions describe translational stiffness and damping along axes $x$, $y$, and $z$, and rotational stiffness and damping around those axes (denoted $xx$, $yy$, and $zz$) as shown in Figure 8.9a.

**Figure 8.9.** Geometry and axis orientations for rectangular foundations (a) at the ground surface and (b) embedded to depth $H$. (Adapted from [@NIST2012].)

For mode $j$, the stiffness, $k_j$, is represented as the product of the static (zero frequency) stiffness of the footing resting on the surface, $K_j$, a dynamic stiffness modifier, $\alpha_j$, and an embedment modifier, $\eta_j$:

$$k_j = K_j \alpha_j \eta_j \quad (8.16)$$

where $K_j = GB \cdot f(B/L, \nu)$, $\alpha_j = f(B/L, a_0)$, and $\eta_j = f(B/L, H/B, m/(\ldots))$; each of these functions is provided in Tables 8.2 and 8.3a. In these functions, parameters $G$ and $\nu$ are the shear modulus and Poisson's ratio of the soil, $m = 1$ for translation of a rectangular foundation for the general 3D case ($m = 0$ for the 2D case corresponding to excitation in $y$-direction for long footing, i.e., $L \to \infty$), and $m = 3$ for rotation of a rectangular foundation for the general 3D case ($m = 2$ for the 2D case). The shear modulus, $G$, is evaluated using an equivalent-linear approach and as such should reflect the effects of modulus reduction with shear strain amplitude. Approximate adjustment factors for different site classes at different PGA levels are shown in Table 8.1. The maximum (or small-strain) shear modulus, $G_\text{max}$, is calculated from shear wave velocity as $G_\text{max} = \rho_s V_s^2$ (Eq. 6.76). An average value of $V_s$ is generally computed across an effective profile depth, $z_p$, as described in Section 8.3.2.2.

Dynamic stiffness modifiers, $\alpha_j$, are related to dimensionless frequency $a_0$:

$$a_0 = \frac{\omega B}{V_s} \quad (8.17)$$

which can be physically interpreted as the ratio of $B$ to approximately one-sixth (actually $1/2\pi$) of the seismic wavelength for frequency $\omega$. For time domain analysis, a single frequency must be selected to evaluate $a_0$-dependent foundation spring and dashpot coefficients; this can be taken as the frequency anticipated to dominate the structural response. In most cases, this will be the first-mode flexible-base frequency.

**TABLE 8.1.** Values of Shear Modulus Reduction and Hysteretic Soil Damping for Various NEHRP Site Classes (Section 7.3.3.1) and Shaking Amplitudes (Source: modified from [@NIST2012] and [@BSSC2020a]).

$V_s$ Reduction Factor $= \sqrt{G/G_\text{max}}$; Value of $G/G_\text{max}$; Value of $\xi_s$

PGA (g):  ≤0.1 / 0.4 / ≥0.8 for each column group.

Site Class A: 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | na / na / na
Site Class B: 1.00 / 0.97 / 0.95 | 1.00 / 0.95 / 0.90 | na / na / na
Site Class BC: 0.98 / 0.92 / 0.86 | 0.97 / 0.84 / 0.73 | na / na / na
Site Class C: 0.97 / 0.87 / 0.77 | 0.95 / 0.75 / 0.60 | 0.01 / 0.03 / 0.05
Site Class CD: 0.96 / 0.79 / 0.50 | 0.92 / 0.62 / 0.25 | 0.01 / 0.05 / 0.09
Site Class D: 0.95 / 0.71 / 0.32 | 0.90 / 0.50 / 0.10 | 0.02 / 0.07 / 0.15
Site Class DE: 0.86 / 0.40 / 0.18 | 0.73 / 0.16 / 0.03 | 0.03 / 0.12 / 0.20
Site Class E: 0.77 / 0.22 / * | 0.60 / 0.05 / * | 0.05 / 0.20 / *
Site Class F: * / * / * | * / * / * | * / * / *

Note: Use straight-line interpolation for intermediate values of PGA. *, should be evaluated from site-specific analysis; na, values not specified (use of foundation damping not recommended). PGA denotes the peak horizontal acceleration for the free-field, ground surface conditions.

**TABLE 8.2.** Elastic Solutions for Static Stiffness of Rigid Footings at the Ground Surface and Embedded to Depth $H$ [@PaisKausel1988; @NIST2012]. Solutions for the 2D case apply for shaking in $y$-direction and are adapted from [@GazetasRoesset1976] and [@JakubRoesset1977]. Axes should be oriented such that $L \geq B$; $G$ = shear modulus (reduced for large-strain problems, e.g., Table 8.1).

Degrees of freedom and associated equation labels:

- Translation along $y$-axis: (T8.2.1-1); 2D case: (T8.2.1-2)
- Translation along $x$-axis: (T8.2.2-1)
- Translation along $z$-axis: (T8.2.3-1)
- Rocking about $y$-axis: (T8.2.4-1)
- Rocking about $x$-axis: (T8.2.5-1); 2D case: (T8.2.5-2)
- Torsion about $z$-axis: (T8.2.6-1)

Surface stiffness expressions ($K_{j,\text{sur}}$) and embedment modifier expressions ($\eta_j$) are provided in terms of $GB$, $L/B$, $H/B$, and $\nu$ per equations (T8.2.1-1) through (T8.2.8-2) as given in [@PaisKausel1988; @NIST2012].

**TABLE 8.3A.** Dynamic Stiffness Modifiers and Radiation Damping Ratios for Rigid Surface Foundations [@PaisKausel1988; @NIST2012]. Orient axes such that $L \geq B$. Hysteretic damping ($\xi_s$) is additive to radiation damping. $a_0 = \omega B / V_s$.

Degrees of freedom and associated equation labels for surface stiffness modifiers ($\alpha_j$) and radiation damping ratios ($\xi_j$):

- Translation along $x$-axis: $\alpha_x$ (T8.3.1-1); $\xi_x$ (T8.3.1-1)
- Translation along $y$-axis: $\alpha_y$ (T8.3.2-1); $\xi_y$ (T8.3.2-1)
- Translation along $z$-axis: $\alpha_z$ (T8.3.3-1); $\xi_z$ (T8.3.3-1)
- Rocking about $y$-axis: $\alpha_{yy}$ (T8.3.4-1); $\xi_{yy}$ (T8.3.4-1)
- Rocking about $x$-axis: $\alpha_{xx}$ (T8.3.5-1); $\xi_{xx}$ (T8.3.5-1)
- Torsion about $z$-axis: $\alpha_{zz}$ (T8.3.6-1); $\xi_{zz}$ (T8.3.6-1); $\psi \leq 2.5$, $\psi = \nu/(1-2\nu)$

2D case labels: (T8.3.1-2) through (T8.3.6-2).

**TABLE 8.3B.** Radiation Damping Ratios for Embedded Rigid Foundations [@PaisKausel1988; @NIST2012]. Note: $\alpha_{j,\text{emb}} = \alpha_{j,\text{sur}}$ from Table 8.3a. Hysteretic damping ($\xi_s$) is additive to radiation damping. $a_0 = \omega B / V_s$; $\psi \leq 2.5$, $\psi = \nu/(1-2\nu)$.

Radiation damping ratios for embedded foundations ($\xi_{j,\text{emb}}$) are given as functions of the surface damping values plus correction terms dependent on $H/B$, $B/L$, and $a_0$, per equations (T8.3.1-3) through (T8.3.6-3).

Table 8.2 provides expressions for static foundation stiffness, $K_j$, and embedment factors, $\eta_j$, for three translational and three rotational degrees of freedom for rigid rectangular footings [@PaisKausel1988; @NIST2012]. Similar equations were provided by [@Gazetas1991] and [@MylonakisEtAl2006]. Due to the additional normal and shear stresses that develop on the sides of the foundation, embedment increases static foundation stiffness and as a result the embedment factors in Table 8.2 only increase the static stiffness. Solutions for the 2D case are also given in Table 8.2 for one translational degree of freedom (along $y$-axis) and one rotational degree of freedom ($xx$) [@GazetasRoesset1976; @JakubRoesset1977].

Equations for dynamic stiffness modifiers, $\alpha_j$, and radiation damping ratios, $\xi_j$, for rigid footings located at the ground surface are provided in Table 8.3a. The frequency dependence of these quantities is an outcome of representing the soil mass supporting the footing with discrete spring and dashpot elements. Due to its distributed mass, the medium actually has an infinite number of degrees of freedom, each with mass and associated dynamic effects. The condensation of the dynamic response of that medium to discrete elements requires that their properties be frequency-dependent (i.e., to incorporate wave propagation phenomena into spring and dashpot values). This frequency dependence would disappear for massless soil, as $a_0$ would become zero (because $V_s = \sqrt{G_\text{max}/\rho_s} \to \infty$ as $\rho_s \to 0$), causing $\alpha_j = 1$ and $\xi_j = 0$.

Radiation damping ratios for embedded footings are provided in Table 8.3b. Dynamic stiffness modifiers are insensitive to embedment, so values for embedded foundations are the same as values given in Table 8.3a for footings located at the ground surface (i.e., $\alpha_{j,\text{emb}} = \alpha_{j,\text{sur}}$).

Figure 8.10 shows the variation of dynamic stiffness modifiers with dimensionless frequency for rigid footings located at the ground surface. In the case of translational stiffness, dynamic stiffness modifiers ($\alpha_x$, $\alpha_y$) are essentially unity, regardless of frequency or foundation aspect ratio. For rotational stiffness, however, dynamic stiffness modifiers for rocking ($\alpha_{xx}$, $\alpha_{yy}$) degrade markedly with frequency, but are relatively insensitive to aspect ratio. Figure 8.10 also shows the variation of radiation damping vs. frequency for translation ($\xi_x$, $\xi_y$) and rotation ($\xi_{xx}$, $\xi_{yy}$). Translational radiation damping is only modestly affected by the direction of shaking or the aspect ratio of the foundation. The modest increase of translational damping with aspect ratio is a result of the increased foundation size (i.e., the foundation becomes larger as aspect ratio increases). In contrast, rotational radiation damping is strongly sensitive to the direction of shaking and the aspect ratio of the foundation. Rotational damping is largely controlled by 180-degree out-of-phase vertical cyclic displacements at the edges of the foundation (assuming no separation between soil and footing). The levels of radiation damping in rotation can be influenced by destructive interference of waves emanating from the ends of the rotating foundation (in effect, the phase shift can cause the waves to "cancel out" each other, reducing radiation damping). This effect is strong for small aspect ratios, producing low levels of rotational radiation damping. As aspect ratio increases, the ends of the foundation are located further apart, and energy radiating into the soil from each end of the foundation experiences less destructive interference, thus increasing damping. At low frequencies ($a_0 < 1$ to 2), damping from rotation is generally smaller than damping from translation, although the trend reverses as frequency increases and foundations become relatively oblong. The practical significance of this effect is that translational deformation modes in the foundation, while often relatively unimportant from the perspective of overall structural system flexibility, can be the dominant source of foundation damping. When used to calculate the dashpot coefficient, $c_j$ (Equation 8.14), the $\xi_j$ term should be taken as the sum of radiation damping for the appropriate vibration mode (Table 8.3) and hysteretic damping ($\xi_s$) (from ground response analysis or Table 8.1).

**Figure 8.10.** Plot of dynamic stiffness modifiers and damping ratios versus dimensionless frequency, for rectangular footings supported on the surface of a homogeneous half-space, with zero hysteretic damping, and $\nu = 0.33$: (a) $x$-direction (long dimension of footing); and (b) $y$-direction (short dimension). (Figure from [@NIST2012].)

### Example 8.4

The foundation for which the responses were measured in Example 8.3 has plan dimensions of 4.06 × 4.06 m. The site at which these measurements were made has an average velocity of 198 m/s and mass density of 1,800 kg/m³ over the applicable depth range for impedance calculations. Calculate the predicted foundation stiffnesses for the test structure for linear conditions using the relations in Table 8.2.

#### Solution

For foundation stiffness calculations, it is best to start with the static stiffness of the foundations and then to make the dynamic adjustment per Equation (8.16). Static stiffnesses are computed using expressions of the form $K_j = GB \cdot f(B/L, \nu)$, with equations for specific vibration modes $j$ provided in Table 8.2.

For the case of horizontal translation, the loading direction is taken in the $x$-direction (because the foundation is square, it could have equivalently been taken as the $y$-direction). Using $G = \rho_s V_s^2 = (1800\ \text{kg/m}^3)(198\ \text{m/s})^2$ and taking $\nu = 0.3$ (surficial materials are sandy), with $B = L = 2.03\ \text{m}$:

$$K_{x,\text{sur}} = \frac{GB}{2 - \nu}\left[6.8 + 2.4\left(\frac{L}{B}\right)^{0.65}\right] = 7.8 \times 10^3\ \text{kN/m}$$

For the case of rotation caused by excitation in the $x$-direction, the rotation is about the $yy$-axis (Figure 8.9):

$$K_{yy,\text{sur}} = \frac{GB^3}{1 - \nu}\left[3.73 + 0.27\left(\frac{L}{B}\right)^{2.4}\right] = 3.4 \times 10^3\ \text{kN-m/rad}$$

The dynamic modifiers depend on dimensionless frequency. From Equation (8.17):

$$a_0 = \frac{2\pi \times 2.03\ \text{m} \times 6\ \text{Hz}}{198\ \text{m/s}} = 0.39$$

Then, from Table 8.3, the dynamic stiffness modifiers $\alpha_j$ and radiation damping ratios $\xi_j$ can be evaluated at $a_0 = 0.39$.
