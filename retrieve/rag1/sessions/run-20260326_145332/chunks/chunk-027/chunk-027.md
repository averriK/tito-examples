$$P_A = \frac{1}{2} K_A \gamma H^2 \tag{8.61}$$

FIGURE 8.48 Rankine active earth pressure distributions for backfills with various combinations of frictional and cohesive strength: (a) friction resistance, no cohesion, (b) cohesive soil, no friction, (c) combined friction and cohesion. (After U.S. Navy, 1982.)

### Example 8.7

A free‑standing, unrestrained retaining wall at a Class D soil site has height H = 6 m and retains soil with a unit weight of 18 kN/m³, Poisson's ratio of 0.3, and active earth pressure coefficient of 0.25. The wall has good drainage, so that the water table will not build up behind the wall. What is the static earth pressure resultant force?

### Solution

Assuming a triangular distribution of static active earth pressure, the resultant force would be calculated using Equation (8.61) as:

$$P_A = \frac{1}{2} K_A \gamma H^2 = 0.5 \times 0.25 \times 18\,\text{kN/m}^3 \times (6\,\text{m})^2 = 81\,\text{kN/m}$$

Coulomb (1776) [@Coulomb1776] was the first to study the problem of lateral earth pressures on retaining structures. He assumed that the force acting on the back of a retaining wall is that required to maintain equilibrium of a wedge of soil above a planar failure surface (Figure 8.49). The active earth pressure resultant can be computed for a given wall‑soil interface friction angle δ, backfill angle β, vertical angle of back side of wall θ, and base angle of soil wedge αA. The problem is indeterminate in the sense that angle αA is unknown and different wall reaction forces are derived for each αA. The solution is obtained by using the surface that produces the greatest active thrust force. The thrust force is related to KA using Equation (8.61) with KA expressed as

( ) ′ − φ θ cos ( ) = (8.62) K A ( ) ( ) δ + ′ φ φ ′ − β sin sin ( ) θ δ + cos cos ( ) ( ) δ + θ β − θ cos cos

The critical failure surface is inclined at an angle

( ) φ ′ − β + tan C − α A = ′ + ° tan (8.63) C

to the horizontal where

( ) ( ) ( ) ( ) ( ) = φ ′ − β φ ′ − β + φ ′ − θ + δ + θ φ ′ − θ tan tan cot tan cot (8.64a) C

{ } ( ) ( ) ( ) = + δ + θ φ ′ − β + φ ′ − θ tan tan cot (8.64b) C

Coulomb theory does not explicitly predict the distribution of active pressure, but it can be shown to be triangular for linear backfill surfaces with no surface loads. In such cases, PA acts at a point located H/3 above the base of a wall of height H and is inclined to a normal at the back of the wall at the interface friction angle δ, which is typically taken as approximately 1/2–2/3 of ϕ′ for soil‑concrete interfaces and 1/3–1/2 of ϕ′ for soil‑steel interfaces. The logarithmic spiral method for active earth pressures is illustrated in Figure 8.50. Log‑spiral methods were introduced for limit equilibrium problems by Rendulic (1935), followed by Taylor (1937), and were first tabulated for use in the prediction of active and passive pressures on retaining walls by Caquot and Kerisel (1948) [@CaquotKerisel1948]. While the major principal stress may act nearly perpendicular to the backfill surface at some distance behind a rough (δ > 0) wall, the presence of shear stresses on the wall‑soil interface rotates principal stresses near the back of the wall. If the inclination of principal stresses varies within the backfill, the inclination of the failure surface must also vary. In other words, the failure surface must be curved, which can be described by a logarithmic spiral function. The critical failure surface consists of a curved portion near the back of the wall and a linear

FIGURE 8.50 (a) Logarithmic spiral representation of the critical failure surface for active earth pressure conditions; (b) orientation of critical failure surface for nonvertical wall with inclined backfill surface.

portion that extends up to the ground surface (Figure 8.50a). The active earth pressure distribution is triangular (Figure 8.50b) for walls retaining cohesionless backfills. Thus the active soil thrust is given by Equation (8.61) using tabulated values of KA from Table 8.5. The active earth pressure coefficients given by the log‑spiral approach are generally considered to be slightly more accurate than those given by Rankine or Coulomb theory, but the difference is so small that the more convenient Coulomb approach is usually used.

### 8.6.2.3 Passive Earth Pressures

Solutions for passive earth pressure coefficients have been developed according to the same principles applied for active conditions by Rankine (1857), Coulomb (1776) [@Coulomb1776], and Terzaghi (1943)/Caquot and Kerisel (1948) [@CaquotKerisel1948] (log‑spiral). Rankine theory predicts wall pressures given by

σ ′ p = K P σ ′ v + c ′ K P (8.65)

where KP is the coefficient of passive earth pressure. For smooth, vertical walls retaining horizontal backfills,

$$K_P = \frac{1 + \sin\phi'}{1 - \sin\phi'} = \tan^2\!\left(45° + \frac{\phi'}{2}\right) \tag{8.66}$$

and

β + β − ° ′ cos cos cos = β cos (8.67) K P β − β − ° ′ cos cos cos

for backfills inclined at angle β to the horizontal. Passive pressure distributions for various backfill strength characteristics are shown in Figure 8.51. For a dry homogeneous backfill, Rankine theory predicts a triangular passive pressure distribution oriented parallel to the backfill surface. The passive earth pressure resultant, or passive thrust PP, acts at a point located H/3 above the base of a wall of height H (Figure 8.51a) with magnitude

$$P_P = \frac{1}{2} K_P \gamma H^2 \tag{8.68}$$

The passive thrust force from Coulomb theory is also described by Equation (8.68), but with KP computed as

( ) ′ + φ θ cos = (8.69) K P ( ) ( ) δ + ′ φ φ ′ + β sin sin ( ) θ δ − cos cos ( ) ( ) δ − θ β − θ cos cos

The angles used in the solution are defined in Figure 8.52 and mirror those for the active case, the only difference being the direction of the lateral earth pressure with respect to the back of the wall. The critical failure surface is again planar with an angle

( ) φ ′ + β + tan C − α P = −′ + ° tan (8.70) C

to the horizontal where

( ) ( ) ( ) ( ) ( ) = φ ′ + β φ ′ + β + φ ′ + θ + δ − θ φ ′ + θ tan tan cot tan cot (8.71a) C

{ } ( ) ( ) ( ) = + δ − θ φ ′ + β + φ ′ + θ tan tan cot (8.71b) C

Whereas the positions of base of the sliding surface for the active case are similar for the Coulomb and log‑spiral solutions, the differences can be much more significant in the case of passive earth pressures. As shown in Figure 8.53, the curved portion of the failure surface is much

FIGURE 8.52 (a) Triangular passive wedge bounded at base by planar sliding surface; (b) force polygon for passive Coulomb wedge. The critical failure surface is that which minimizes PP.

FIGURE 8.53 (a) Logarithmic spiral representation of the critical failure surface for passive earth pressure conditions; (b) orientation of critical failure surface for nonvertical wall with inclined backfill surface.

more pronounced than for the active condition and typically extends below the elevation of the wall heel – this makes for a larger failure surface but lower (and thus more critical) values of KP. The passive thrust force from the log‑spiral solution for granular backfills is given by Equation (8.68), with the KP values tabulated in Table 8.5. Experimental results show that maximum passive earth pressure coefficients given by the log‑spiral method are considerably more accurate than those given by Rankine or Coulomb theory, which tend to underpredict and overpredict, respectively (Mokwa and Duncan, 2001 [@MokwaDuncan2001]; Rollins and Cole, 2006; Rollins and Sparks, 2002; Lemnitzer et al., 2009 [@LemnitzerEtAl2009]). The maximum passive earth pressure resultants evaluated using log‑spiral methods can be extended to load‑deflection relationships using hyperbolic functions, details of which are presented by Shamsabadi et al. (2007) and Khalili‑Tehrani et al. (2016) [@KhaliliTehraniEtAl2016]. For bridge abutment applications, it is often required to compute passive capacities for cases in which the inertial load applied to the abutment wall by a bridge deck is skewed relative to the alignment of the abutment. Figure 8.54a shows such a case, with skew angle Θ defined as the angle between the abutment wall alignment and the transverse direction of the bridge deck. As shown in Figure 8.54a, the bridge deck inertial load PL is resisted within the abutment by a maximum passive earth pressure resultant PP and a shear force PR. The value of PP in this case is reduced relative to the values obtained without skew (i.e., Equations 8.68 with KP taken from Table 8.5) by the factor Rskew, which depends on skew angle as shown in Figure 8.54b. The fit relationship for Rskew in Figure 8.54b is based on model tests and numerical simulations (Rollins and Jessee, 2013). For cohesionless backfills, shear resistance PR is related to PP as:

$$P_R = P_P \tan\delta \tag{8.72}$$

where δ, as before, is the wall‑soil interface friction angle.

FIGURE 8.54 (a) Configuration of bridge with skewed abutment showing forces at deck‑abutment interface; (b) variation of maximum passive earth pressure resultant reduction factor with skew angle. (Adapted from Rollins and Jessee, 2013.)

### TABLE 8.5

### Values of KA and KP for Log‑Spiral Failure Surfaces

ϕ: 20°, 25°, 30°, 35°, 40°, 45°

δ β θ — KP — KA — KP — KA — KP — KA — KP — KA — KP — KA — KP — KA

0° −15° −10° 0.37 1.32 0.30 1.66 0.24 2.05 0.19 2.52 0.14 3.09 0.11 3.95
0° 0.42 1.09 0.35 1.33 0.29 1.56 0.24 1.82 0.19 2.09 0.16 2.48
10° 0.45 0.87 0.39 1.03 0.34 1.17 0.29 1.30 0.24 1.33 0.21 1.54
0° 0° −10° 0.42 2.33 0.34 2.96 0.27 3.82 0.21 5.00 0.16 6.68 0.12 9.20
0° 0.49 2.04 0.41 2.46 0.33 3.00 0.27 3.69 0.22 4.59 0.17 5.83
10° 0.55 1.74 0.47 1.89 0.40 2.33 0.34 2.70 0.28 3.14 0.24 3.69
0° 15° −10° 0.55 3.36 0.41 4.56 0.32 6.30 0.23 8.98 0.17 12.2 0.13 20.0
0° 0.65 2.99 0.51 3.86 0.41 5.04 0.32 6.72 0.25 10.4 0.20 12.8
10° 0.75 2.63 0.60 3.23 0.49 3.97 0.41 4.98 0.34 6.37 0.28 8.20
ϕ −15° −10° 0.31 1.95 0.26 2.90 0.21 4.39 0.17 6.97 0.14 11.8 0.11 22.7
0° 0.37 1.62 0.31 2.31 0.26 3.35 0.23 5.04 0.19 7.99 0.17 14.3
10° 0.41 1.29 0.36 1.79 0.31 2.50 0.27 3.58 0.25 5.09 0.23 8.86
ϕ 0° −10° 0.37 3.45 0.30 5.17 0.24 8.17 0.19 13.8 0.15 25.5 0.12 52.9
0° 0.44 3.01 0.37 4.29 0.30 6.42 0.26 10.2 0.22 17.5 0.19 33.5
10° 0.50 2.57 0.43 3.50 0.38 4.98 0.33 7.47 0.30 12.0 0.26 21.2
ϕ 15° −10° 0.50 4.95 0.37 7.95 0.29 13.5 0.22 24.8 0.17 50.4 0.14
0° 0.61 4.42 0.48 6.72 0.37 10.8 0.32 18.6 0.25 39.6 0.21 73.6
10° 0.72 3.88 0.58 5.62 0.46 8.51 0.42 13.8 0.35 24.3 0.31 46.9

FIGURE 8.51 Rankine passive earth pressure distributions for backfills with various combinations of frictional and cohesive strength: (a) friction resistance, no cohesion, (b) cohesive soil, no friction, (c) combined friction and cohesion. (After U.S. Department of the Navy, 1982.)

###### 8.6.3 Seismic Lateral Earth Pressures

As described in Section 8.6.1, earthquake loading changes the earth pressures (demands) acting on embedded structures from those that exist under static conditions. Section 8.6.2 highlighted the profound effect of wall displacement on static lateral earth pressures. Seismic earth pressures can be understood in the same context, but with the additional complexity that both the wall and the free‑field soil displace as a result of earthquake shaking. At any point during an earthquake, when the wall displaces away from the backfill, earth pressures can drop from the static condition (if not already in a minimum active state). Conversely, and more importantly for engineering application, at any point in time when the wall displaces toward the backfill, earth pressures will rise relative to the static condition. Since earthquake loading is transient, both increases and decreases in earth pressure are to be expected at different times over the duration of shaking; engineering procedures focus on the former for practical application. Mechanisms that can produce relative wall‑soil displacements include: (1) different levels of transient wall displacement relative to the free‑field independent of the inertia of structures that may be connected to the wall; (2) free‑field permanent ground displacements arising from soil strength loss (e.g., liquefaction, cyclic softening, etc.); and (3) forces applied to a wall/foundation system by attached vibrating structures, which in turn produce relative foundation/free‑field displacements independent from those in (1). Mechanism (1) is a kinematic SSI problem having some similarity to the analysis of uFIM and θFIM for embedded structures as described in Section 8.4.2. Mechanism (2) is a ground failure problem and is not discussed further here (analysis procedures for predicting the onset of ground failure are described in Chapter 9; the interaction of lateral spreads with foundations, which may include walls, is described in Section 8.5.2.2). Mechanism (3) is an inertial SSI problem that requires analysis of the response of a structure connected to a suitable foundation system using either direct (Figure 8.1) or substructure (Figures 8.2–8.4) methods of analysis.

The following subsections describe classical methods for the analysis of seismic earth pressure that are based on the acceleration of backfill soil, the kinematic wall response problem and available solutions, and considerations in the inertial wall‑soil response problem.

### 8.6.3.1 Methods Based on Pseudo‑Static Backfill Force

For many years, seismic earth pressures on retaining walls have been analyzed using a pseudo‑static framework in which accelerations are applied to backfill materials, the wall is assumed to displace forming a soil wedge at a state of shear failure in the backfill (i.e., limit state), and resulting wall force demands are analyzed. Figure 8.55 illustrates the concept for the case of an active soil wedge with horizontal acceleration of $k_h g$ and vertical acceleration of $k_v g$ (where g is acceleration of gravity), which produce horizontal and vertical inertial forces in the backfill. The force polygon in Figure 8.55b illustrates how these inertial forces increase the wall soil interaction force by an amount PE above the static force PA (assuming active conditions prior to the earthquake). By solving the equilibrium problem in Figure 8.55b for a variety of acceleration levels, the combined thrust PA + PE can be computed as

$$P_A + P_E = \frac{1}{2} \gamma H^2 (1 - k_v) K_{AE} \tag{8.73}$$

where KAE is a seismic earth pressure coefficient that combines the effects of gravity and the pseudo‑static inertial forces in the wedge, and is given by (e.g., Koseki et al., 1998 [@KosekiEtAl1998]):

( ) ′ − − φ θ ψ cos = (8.74) K AE ( ) ( ) ′ + ′ − − φ δ φ β ψ sin sin ( ) − − + ψ θ δ θ ψ cos cos cos ( ) ( ) + + − δ θ ψ θ β cos cos

The angles ϕ′, θ, β, and δ in Equation (8.74) are as defined in Figure 8.49, and ψ is related to the pseudo‑static accelerations as:

$$\psi = \tan^{-1}\!\left(\frac{k_h}{1 - k_v}\right) \tag{8.75}$$

FIGURE 8.55 (a) Retaining wall with horizontal and vertical pseudo‑accelerations applied to backfill wedge; (b) force polygon showing the effect of inertial forces from pseudo‑acceleration on the wall‑soil interaction force.

FIGURE 8.56 Active earth pressure coefficient KAE as derived from M‑O formulation for vertical frictionless wall with horizontal backfill and variable levels of horizontal acceleration. The seismic increment is the difference between KAE for the case of finite horizontal acceleration and kh = 0. The angles defining the problem geometry are defined in Figure 8.49. (Adapted from results in Koseki et al., 1998 [@KosekiEtAl1998]; used with permission of Springer Nature BV.)

Figure 8.56 shows values of KAE obtained using Equation (8.75) for a vertical (θ = 0) and smooth (δ = 0) wall with horizontal backfill (β = 0) subjected to horizontal‑only inertial loads (kv = 0). As expected, earth pressures increase with pseudo‑acceleration kh, but a notable feature of the solution is that earth pressures are undefined for large accelerations (indicated by the curves becoming nearly vertical), which is a result of soil failure in the backfill (Wood, 2023). Seed and Whitman (1970) observed that for levels of Kh up to about 0.4, the seismic increment of earth pressure could be reasonably approximated by ΔKAE = 0.75kh, which can then be used to estimate the combined earth pressure as KAE ≈ KA + ΔKAE. Pseudo‑static limit state methods of this type for the active case originate in the classical work by Okabe (1926) and Mononobe and Matsuo (1929) [@MononobeMatsuo1929] [widely known as the "Mononobe‑Okabe" (M‑O) method]. Variants on the classical approach derived by means of kinematic limit analyses considering non‑planar failure surfaces (Chen, 1975 [@Chen1975]; Chen and Liu, 1990 [@ChenLiu1990]), stress fields (Mylonakis et al., 2007), backfill soils with cohesion and friction (National Cooperative Highway Research Program, 2008; Xu et al., 2015), and accounting for the phasing of inertial demands within the retained soil (Steedman and Zeng, 1990) are conceptually alike and provide similar results for the active case. Wood (1973, 2023) considered the case of pre‑seismic at‑rest earth pressures (as a consequence, the initial condition of the backfill is not at a limit state), which produces larger seismic earth pressures than those of the M‑O method. Richart and Elms (1979) considered sliding block displacements of gravity walls (similar to procedures in Section 10.9.2). A shortcoming of the conceptual framework behind this large body of work is its implicit assumption that seismic earth pressures are related to backfill acceleration rather than the relative displacement of the wall and soil. While pseudo‑accelerations in the active wedge are associated with motion of the backfill, relative wall‑soil motion is not considered because the formulation assumes the wall to be stationary during earthquake shaking. If both the backfill and wall move with comparable, in‑phase displacement amplitudes, no appreciable seismic earth pressure will develop, despite the fact that the backfill is accelerating. Hence, there is a conceptual flaw in the classical methods.

Not surprisingly, when seismic earth pressures have been computed from direct analyses (Figure 8.1) or measured experimentally, they seldom conform to predictions from M‑O‑type procedures when PGA is used to estimate kh. In some cases involving high‑frequency ground motions, computed pressures exceed M‑O predictions (e.g., Ostadan, 2005; Veletsos and Younan, 1994), while measured pressures in experiments (generally involving relatively low‑frequency ground motions) typically fall below M‑O predictions (e.g., Al Atik and Sitar, 2010 [@AlAtikSitar2010]; Hushmand et al., 2016 [@HushmandEtAl2016]; Wagner and Sitar, 2016; Candia et al., 2016 [@CandiaEtAl2016]). For these reasons, the continued use of pseudo‑acceleration‑based (e.g., M‑O type) methods is problematic because of their inability to account for the problem physics.

### 8.6.3.2 SSI‑Based Seismic Earth Pressures

The estimation of seismic earth pressures can be improved by recognizing that such pressures develop as a result of SSI involving the wall, supporting and retained soil, and any attached superstructures. As with other SSI problems, both kinematic and inertial components can be significant. Treating the problem that way allows consideration of important effects such as wall and soil stiffness and loading frequency to be taken into account, and produces pressures that are consistent with those obtained from direct analyses and model tests.

**Kinematic Seismic Earth Pressures** Kinematic seismic earth pressures are produced by the combined seismic excitation of shallow layers of soil at a site and a relatively stiff wall system embedded within those soils. Figure 8.29 depicts a U‑shaped building basement wall system. Figure 8.57 illustrates the problem for the case of a free‑standing wall. In the kinematic problem, the wall itself is assumed to have a certain flexural stiffness but no mass and to be connected to the soil but not to any structure. The ground motions producing the excitation occur over a wide frequency range, typically from about 0.2 to 10 Hz. If these waves can be reasonably assumed as vertically propagating near the ground surface (such that the ground response is one-dimensional; Section 7.5), they produce waves of wavelength λ = Vs/f with maximum amplitude at the ground surface (Figure 8.57 and Equation 8.41). Accordingly, at each frequency, and at a given point in time, the horizontal ground motion varies with depth. When this variation is small (i.e., for low frequencies with long wavelengths), the motion of the wall system nearly matches that of the free‑field soil, relative wall‑soil displacements are small, and seismic earth pressures are low (Brandenberg et al., 2015 [@BrandenbergEtAl2015]). Conversely, as shown in Figure 8.57, short wavelengths can produce

FIGURE 8.57 Schematic illustration of free‑standing retaining wall subjected to seismic waves with different wavelengths. Displacement uFIM applies at the foundation level of the wall, and θFIM represents the rotation of a rigid wall‑footing system.

motions that decrease significantly with depth over the height of the wall. Under such conditions, the relatively stiff wall must displace differently from the free‑field soil, and the differences in displacement produce potentially large seismic earth pressures. For these short wavelength conditions, the flexibility of the wall system, the distribution with depth of soil stiffness, and the ability of the wall to yield also affect seismic earth pressures. The kinematic problem illustrated in Figure 8.57 can be solved using direct analysis in which the ground response and SSI are solved for simultaneously (Figure 8.1), and procedures of this sort are used for critical projects. Simplified methods are useful to help conceptualize the physics of the problem and for applications where more approximate solutions suffice. For the conditions represented in Figure 8.58, which include rigid wall elements and uniform, elastic backfill soils, an approximate solution for the amplitude of seismic earth pressure resultant PE (normalized to remove dimensions) is given by Durante et al. (2022) [@DuranteEtAl2022]:

( ) sin kH P ( ) E = − (8.76) cos kH i k y u ff0 H kH

where k is the wavenumber (ω/VS), uff0 is the free‑field ground surface displacement, and H is wall height (Figure 8.58). The normalized height of resultant h/H, where h is measured up to the resultant from the base of the foundation, is given for the same conditions as (Durante et al., 2022 [@DuranteEtAl2022]):

( ) cos kH ( ) ( ) − + cos kH kH h = (8.77) ( ) ( ) ( ) ( ) − H cos sin kH kH kH kH

Equation (8.77) gives h/H = 5/8 for λ/H ≳ 4. The normal stress on the wall is described by the product of relative wall‑soil displacement and stiffness intensity $k_y^i$ (introduced in Section 8.3.2.3), which is computed for application to walls as (Kloukinas et al., 2012 [@KloukinasEtAl2012]):

π G / H = i (8.78) k y (1 − ν)(2 − ν)

where G and ν are the shear modulus and Poisson's ratio of the backfill, respectively.

FIGURE 8.58 Schematic rigid wall systems with uniform backfill soils subjected to vertically propagating shear wave showing soil‑structure stiffness terms for (a) U‑shaped wall and (b) cantilever‑type single wall.

FIGURE 8.59 Variation of normalized amplitude of PE with normalized wavelength λ/H for wall founded on rigid base (solution given in Equation 8.76). Dotted line at low λ/H is an approximation of the exact solution.

Equations (8.76–8.78) apply for the case of a stiff foundation (infinite base slab stiffnesses Ky and Kxx), rigid wall, and backfill of uniform stiffness. For those conditions, Figure 8.59 shows the variation of the normalized force amplitude $P_E / (k_y^i u_{ff0} H)$, and its normalized point of application h/H, with the ratio of wavelength to wall height λ/H (note that this ratio increases with decreasing frequency). The portion of this curve for λ/H ≳ 2.7 typically contains the frequency range of engineering interest. Kinematic pressures are high near λ/H = 2.7 due to large relative displacements of wall and soil. For smaller λ/H, relative displacements are large and normalized forces oscillate due to tensile and compressive stress changes acting on different portions of the wall height; this complex behavior is simplified to the dashed horizontal lines shown in Figure 8.59. As λ/H increases beyond 2.7, PE decreases rapidly. In the limiting case where λ/H → ∞, the deformed shape of the free‑field soil profile becomes vertical, conforming to the shape of the rigid wall and producing zero kinematic interaction. For a given value of λ/H, the normalization of force accounts for the effects of soil stiffness and shaking amplitude on seismic earth pressures. The normalized resultant height has little variation with λ/H beyond 4.0. In addition to wavelength, another critical factor that affects the development of seismic earth pressures is relative soil‑to‑wall flexibility. A rigid wall is less able to conform with free‑field ground motions than is a flexible wall; the effect of increasing wall flexibility is to reduce both relative displacements and seismic earth pressures. Relative soil‑to‑wall flexibility is parameterized as (Novak, 1974):

$$\beta = \frac{k_y^i}{EI} \tag{8.79}$$

where E is Young's modulus of the wall material and I is the moment of inertia for the wall section (the product represents the wall flexural stiffness). β has units of 1/length, and is multiplied by H to remove dimensions. A rigid wall has βH = 0, but walls with βH < 0.5 respond in an effectively

FIGURE 8.60 Effect of wall flexibility on (a) normalized wall resultant and (b) its point of application above the foundation. These results are for a rigid base and uniform backfill. (Modified from Durante et al., 2022 [@DuranteEtAl2022]; used with permission of SAGE Publications, Ltd.)

rigid manner. Rigid or nearly rigid walls are seldom encountered in practice; values of βH ranging from 2 to 4 are more common for modern building basement walls in seismically active regions. Figure 8.60 shows wall flexibility effects on the seismic earth pressure resultant and its height as derived from finite element analyses (Durante et al., 2022 [@DuranteEtAl2022]). As shown in Figure 8.60, PE and its resultant height decrease substantially as wall stiffness decreases (i.e., with increasing βH). Several additional factors affect seismic earth pressures, but to a lesser degree than wavelength and wall flexibility. One of these is non‑uniform backfill conditions in which Vs increases with depth. The effects of velocity gradient have been investigated by holding the time‑averaged shear wave velocity within the backfill soil as constant (Vrettos et al., 2016; Brandenberg et al., 2017 [@BrandenbergEtAl2017]). For rigid walls, backfill non‑uniformity reduces PE and its resultant height; however, these effects are small for modest levels of wall flexibility. A second factor is nonlinearity in backfill soils, which both reduces stiffness intensity (Equation 8.78) and decreases wavelength due to modulus reduction. These effects largely offset and the net impact on seismic earth pressure resultant is typically small and can be neglected for simplified analyses (Durante et al., 2022 [@DuranteEtAl2022]). A third factor is non‑rigid (i.e., compliant) foundation conditions, which strongly reduce PE for rigid walls (Brandenberg et al., 2015 [@BrandenbergEtAl2015]). However, these effects are more modest for flexible walls (Brandenberg et al., 2020 [@BrandenbergEtAl2020]), and may be neglected for simplified analyses (Durante et al., 2022 [@DuranteEtAl2022]). The solutions presented in Figures 8.59 and 8.60 can be applied with a free‑field ground motion by converting the time series to a Fourier series, computing earth pressure resultants (PE) and moments (hPE) for each frequency in the Fourier series, and computing the resultant force and moment time series using an inverse Fourier transformation. Routines for performing such calculations are presented by Brandenberg et al. (2020) [@BrandenbergEtAl2020]. A more approximate procedure that avoids the need for Fourier transforms simplifies the representation of ground motions by using the intensity measures of PGV (for amplitude) and mean period Tm (for frequency content; Section 3.3.2). This procedure is summarized as follows (Building Seismic Safety Council, 2020b [@BSSC2020b]; Durante et al., 2022 [@DuranteEtAl2022]):

FIGURE 8.61 Ground motion amplitude adjustment factor for use with simplified method for evaluation of amplitude of seismic earth pressure resultant force, PE. (Adapted from Durante et al., 2022 [@DuranteEtAl2022].)

1. Perform a seismic hazard analysis (probabilistic or deterministic) to estimate PGV for the site.

1. If the estimation of PGV is based on probabilistic seismic hazard analysis, disaggregate the hazard (Section 4.4.3.5) at the return period of interest to obtain the controlling magnitudes and distances (either a single mean value or, as appropriate, multiple pairs for distinct contributing sources). Estimate the mean period Tm for this condition (Section 3.5.3.2). If PGV is derived using deterministic methods, use the selected magnitude and distance for the estimation of mean period. Compute the corresponding mean angular frequency $\omega_m = 2\pi / T_m$.

1. Develop a shear wave velocity profile for the backfill soil. Compute the average shear wave velocity Vs,av as the ratio of wall height H to shear wave travel time through the backfill. Compute $k_m = \omega_m / V_{s,av}$.

1. Estimate the ground surface displacement as $u_{g0} = f_u \cdot PGV / \omega_m$. The adjustment factor fu depends on λ/H as shown in Figure 8.61. This factor has been calibrated to match the results of single‑frequency analyses to more complete Fourier series analyses.

1. Estimate $k_y^i$ as its static counterpart:

π ρ s V 2 s,av / H = i (8.80) k y (1 − ν)(2 − ν)

This expression is modified from Equation (8.78) by removing the frequency‑dependent term and by taking $G = \rho_s V_{s,av}^2$, where ρs is backfill mass density.

1. Estimate βH from the relative soil‑to‑wall stiffness (Equation 8.79) and wall height H. In cases where βH is unknown because wall section sizes are undetermined, an initial estimate in the range of 1–2 can be applied and will often be conservative.

1. Compute the normalized force amplitude $P_E / (k_y^i u_{g0} H)$ and resultant height h/H. These quantities are obtained for rigid walls using Equations (8.76 and 8.77). The effects of wall flexibility can be incorporated using Figure 8.62 or the following expressions (which describe the change of resultant amplitude and its height with βH):

$$\frac{P_E}{P_{E,\text{rigid wall}}} = \begin{cases} \exp\!\left(-\dfrac{2.9}{\beta H}\right) - \exp\!\left(-\beta H\right) & \beta H < 1.43 \\[6pt] 0.34\,\sin(\beta H) + 0.45\,\cos(\beta H) + 1.22 & \beta H > 1.43 \end{cases} \tag{8.81}$$

FIGURE 8.62 Effect of relative soil‑to‑wall stiffness (βH) on normalized resultant force and normalized resultant height. (Adapted from Durante et al., 2022 [@DuranteEtAl2022].)

$$\frac{h}{H} = \begin{cases} -0.6\,\exp\!\left(-\dfrac{2.8}{\beta H}\right) - 0.12\,\exp\!\left(-\beta H\right) & \beta H < 1.5 \\[6pt] 1.92\,\sin(\beta H) + 1.68\,\cos(\beta H) + 2.87 & \beta H > 1.5 \end{cases} \tag{8.82}$$

The relations in Equations (8.81 and 8.82) and Figure 8.62 are curve‑fits to finite element simulation results.

1. De‑normalize to compute $P_E = (P_E / (k_y^i u_{g0} H)) \cdot k_y^i u_{g0} H$. The moment at the base of the wall is computed as $M = h P_E$.

Simplifications associated with this procedure include the approximation of the ground motions with intensity measures, neglecting the frequency‑dependence of wall‑soil stiffness intensity, the treatment of the backfill as uniform and elastic, the treatment of the wall bending response as elastic, and neglecting wall inertia. Despite these assumptions, validation against centrifuge test data and the results of direct analyses (e.g., Al Atik and Sitar, 2010 [@AlAtikSitar2010]; Hushmand et al., 2016 [@HushmandEtAl2016]; Wagner and Sitar, 2016; Candia et al., 2016 [@CandiaEtAl2016]; Ostadan, 2005) show good (if slightly conservative) results, and markedly more reliable predictions than the M‑O method (Durante et al., 2022 [@DuranteEtAl2022]).

### Example 8.8

Consider again the wall from Example 8.7. Seismic hazard analyses are performed, and the PGV for the design return period is 50 cm/sec, with a controlling magnitude of 7.0 and source‑to‑site distance of 15 km. The average small‑strain shear wave velocity of the sandy backfill materials over the 6.0 m wall height is 200 m/sec. The wall's relative soil/wall flexibility is β = 0.33/m. What is the resultant force from kinematic soil–structure interaction?

### Solution

To evaluate the seismic increment, the steps described in the text are applied as follows:

1. The seismic hazard analysis described in the problem statement provides the value of PGV = 50 cm/sec.

1. The expected mean period of the ground motion is computed from the relations in Section 3.5.3.2 (Figure 3.44); the median Tm for the given magnitude and distance is 0.6 sec. The corresponding angular frequency is $\omega_m = 2\pi / T_m = 10.5\,\text{rad/sec}$.

1. The shear wave velocity is 200 m/sec as given in the problem statement.

1. The ground surface displacement is computed as $u_{g0} = f_u \cdot PGV / \omega_m$, where the adjustment factor fu depends on λ/H. With $\lambda = V_s T_m = 120\,\text{m}$, the value of λ/H = 20, so Figure 8.61 shows that fu = 0.95 and ug0 can be calculated as:

$$u_{g0} = (0.95)(200\,\text{m/sec}) / 10.5\,\text{sec}^{-1} = 0.045\,\text{m}$$

1. Recalling that ν = 0.3 from Example 8.7, estimate $k_y^i$ using Equation (8.80) as:

$$k_y^i = \frac{\pi \times (18/9.81) \times 200^2 / 6}{(1-0.3)(2-0.3)} = 3.5 \times 10^3\,\text{kN/m}^3$$

1. Given the relative soil/wall flexibility, βH = 0.33 × 6 = 2.

1. The normalized force amplitude for a rigid wall can then be read from Figure 8.59 using λ/H = 20, which gives a value of $P_E / (k_y^i u_{g0} H) = 0.033$. Since the wall is not rigid, the effects of its flexibility are accounted for by the reduction factor shown in Figure 8.62, which has a value of 0.5. The resulting normalized force amplitude is 0.033 × 0.5 = 0.017.

1. From de‑normalization, the resultant in force units is $P_E = 0.017 \times k_y^i u_{g0} H = 157\,\text{kN/m}$.

From the above, the overall lateral earth pressure coefficient can be calculated using Equation (8.73) as $K_{AE} = P_A + P_E / (0.5\,\gamma H^2) = 0.7$. Given KA = 0.25 (from Example 8.7), the seismic response can be seen to nearly triple the earth pressure from the static condition. The static and seismic resultants will generally occur at different heights h above the base of the foundation; the static resultant is at h/H = 1/3 whereas the height of the seismic resultant is obtained from Figure 8.62. In this case, the seismic resultant is also at h/H = 0.42.

**Inertial Seismic Earth Pressures** The kinematic solution presented above does not consider the effects of inertia. Actual retaining walls have mass, which will produce inertial forces when excited by earthquake shaking. That inertia will affect the wall response and therefore change seismic earth pressures relative to the kinematic case. Relative to the case where inertia is ignored, inertial effects can increase or decrease seismic earth pressures. The combined effects of kinematic and inertial interaction for free‑standing walls or basement walls can be analyzed using frequency domain procedures (Brandenberg et al., 2020 [@BrandenbergEtAl2020]). Such analyses may well be justified when inertial effects may be important, such as when gravity walls are used. Inertial seismic earth pressures are typically most significant when structures are connected to a foundation system containing walls and the lateral force resisting system below the ground level includes those walls (e.g., Figure 8.4b). Under these conditions, the base shear and moment generated by the vibrating structure cause the foundation system to displace horizontally and rotate, producing wall reaction stresses. Analysis of this problem does not require specialized procedures – direct or substructure approaches to the SSI problem can be employed as illustrated in Figures 8.1–8.4 and discussed in Section 8.2. Provided wall‑soil interaction elements are included in the SSI model, the reaction stresses against the walls are a natural product of the analysis. It is important to consider the degree to which subterranean walls participate in the below‑ground lateral force resisting system in the analysis of inertial effects. Figure 8.63 shows a building in which lateral loads are resisted by a central core of shear walls that extend directly to the foundation mat. If the foundation for the core walls is not structurally connected to the foundations for the surrounding podium (i.e., a portion of the structure with a wider footprint, generally near and below ground line) and floor diaphragms within the podium are either not connected to the core walls or are relatively flexible, the podium's basement walls may see little of the inertial loading. In such cases, the loading of basement walls is likely to be controlled by the kinematic mechanisms described in the previous section. Peak kinematic and inertial seismic demands on basement walls are unlikely to coincide in time. When both effects are expected, load combination rules such as SRSS can be applied.

FIGURE 8.63 Structure with lateral loads resisted by a central core of shear walls supported on a mat foundation that is distinct from the foundations for podium basement walls. In such cases, the degree to which podium basement walls are affected by inertial interaction effects depends on the connectivity of floor diaphragms to the core walls and perimeter walls and their flexibility.

###### 8.6.4 Underground Structures

Underground structures such as tunnels, culverts, and pipelines can comprise critical lifelines, the design and analysis of which is a SSI problem that often falls within the purview of geotechnical earthquake engineers. The distinction from retaining walls is that underground structures are buried (they do not extend to the ground surface), they are hollow, low‑density inclusions, and their lengths can be much greater than their cross‑sectional dimensions. As with other earth‑retaining structures, underground structures experience a combination of loading from static lateral (and vertical) earth pressures and additional demands imposed by earthquakes. Seismic demands in structural elements result from two principal sources: (1) spatially variable transient ground displacements that produce relative displacements between free‑field and structure, which in turn produce force and moment demands in the lining of the underground structure; and (2) permanent displacements associated with ground failure mechanisms such as soil liquefaction, cyclic softening, and slope instability. The former is addressed in this section; the latter are ground failure problems that are the subject of Chapters 9 and 10. Spatial variations of transient ground motions in both the vertical and horizontal directions can affect underground structures. Vertically variable demands are caused by one-dimensional ground response in a manner similar to that considered in kinematic analysis procedures for walls (Section 8.6.3.2). Horizontally variable demands are caused by wave passage and other spatial variability effects (Section 3.8). The manner by which these demands are considered for underground structures is described in the following subsections [more information can be found in Hashash et al. (2001) [@HashashEtAl2001] and Wang (1993)].

### 8.6.4.1 Demands from Vertically Propagating Shear Waves

As illustrated in Figure 8.64, vertical shear wave propagation can produce ovaling of circular tunnel sections and racking of rectangular sections (Owen and Scholl, 1981). Analysis procedures for the two cases consider the effects of the vertical variation of ground displacement, and the stiffness of the tunnel lining structure (relative to that of the soil), on the force and moment demands that develop in the lining. As with other SSI problems, these effects can be considered using direct SSI analysis procedures that simultaneously consider the site response and SSI (Section 8.2.1); the focus of this section is on simplified methods that illustrate some of the important physics of the problem. Analysis of ovaling for circular sections begins with the estimation of peak soil shear strain (γmax) over the depth range of the tunnel from site‑specific ground response analysis. The ratio of

FIGURE 8.64 Deformation modes of tunnel or culvert cross‑section from vertical shear wave propagation. (Adapted from Hashash et al., 2001 [@HashashEtAl2001] and Owen and Scholl, 1981; used with permission of Elsevier Science and Technology Journals.)

soil stiffness to tunnel lining stiffness in shear (Merritt et al., 1985 [@MerrittEtAl1985]) can be expressed in terms of the flexibility ratio

( ) E s (1 − ν c ) r t = (8.83) F ( ) E c I c + ν c

where rt is the tunnel radius, Es is the soil Young's modulus (related to shear modulus G per Equation 8.29), ν is the soil Poisson's ratio, and Ec, Ic, and νc are the Young's modulus, moment of inertia, and Poisson's ratio of the tunnel lining material (generally concrete), respectively. Similarly, the ratio of soil medium to tunnel axial stiffness (Merritt et al., 1985 [@MerrittEtAl1985]) can be expressed by the compressibility ratio

( ) E s (1 − ν c ) r t = (8.84) C ( )( ) E c t c 1 + ν c 1 − 2ν c

where tc is the thickness of the tunnel lining. The tunnel section diametric strain (computed as ratio of diameter change from ovaling, Δdt, shown in Figure 8.64, to initial diameter) is then computed assuming full slip between soil and liner (Hashash et al., 2001 [@HashashEtAl2001]) as

Δd t / r t = K 1 F γ max (8.85)

where K1 is a response coefficient that depends on F and ν as shown in Figure 8.65a for the case where slip is allowed at the soil‑tunnel interface. Demands within the tunnel liner, specifically the axial thrust force (Tmax) and moment (Mmax) per unit length (Hashash et al., 2001 [@HashashEtAl2001]) are then computed as

E s K 2 r t = (8.86) T max 2(1 + ν)

E s K 2 r t = (8.87) M max 6(1 + ν)

where K2 is a response coefficient that depends on F, C, and ν; results for ν = 0.35 are shown in Figure 8.65b.

FIGURE 8.65 Response coefficients K1 and K2. Poisson's ratios shown in the figure are for soil (ν). (Plotted from equations in Wang, 1993.)

FIGURE 8.66 Free‑field racking deformation imposed on a buried rectangular frame. (Adapted from Wang, 1993.)

Analysis of racking for rectangular sections begins with the evaluation of a ground displacement profile as shown in Figure 8.66 and the relative free‑field displacement between the top and bottom of the tunnel section, Δdiff. The racking stiffness of the tunnel section, Kt, is evaluated as the ratio of force (per unit length)/deflection to produce deformations of the type shown on the right side of Figure 8.66. The flexibility ratio Fr for this case is then computed as:

$$F_r = \frac{G w}{K_t h} \tag{8.88}$$

where w and h are width and height of the tunnel, as shown in Figure 8.66. The ratio of tunnel/free‑field displacement (Δt/Δdiff) is then evaluated from Fr as shown in Figure 8.67. Internal member demands are evaluated from displacement Δt using standard structural analyses.

### 8.6.4.2 Demands from Horizontally Variable Ground Motions

Horizontally variable ground motions have the potential to produce axial and bending deformations of underground structures (Figure 8.68). As described in Section 3.8, these variations in ground shaking arise from horizontal wave passage (most predominantly in the direction from source‑to‑site) and more complex stochastic processes that produce spatial variations in amplitude and phase. Horizontally variable motions can also occur at boundaries between soils of different impedance, for example as might occur when a tunnel or pipeline passes from stiff soils beneath a hill into softer (and possibly even liquefiable) soils in an adjacent alluvial valley; sharp impedance contrasts at such material boundaries can impose high flexural demands on buried structures.

FIGURE 8.67 Dependence of tunnel‑to‑free‑field displacement ratio with flexibility ratio Fr. Full slip results from Wang (1993) and Penzien (2000), no slip results from Penzien (2000). (Figure adapted from Power et al., 2006.)

FIGURE 8.68 Deformation modes of underground structures due to traveling waves producing (a) tension/compression and (b) bending. (Adapted from Owen and Scholl, 1981.)

A first‑order approximation of axial and bending strains induced in tunnel sections from horizontal ground motion variability is to assume they are equal to corresponding free‑field ground strains (i.e., implicitly assuming that the tunnel is completely flexible). As described in Section 3.8.2, spatially variable ground strains from wave passage can cause a variety of shear and axial strains depending on wave type (p‑waves, s‑waves, surface waves) and direction of wave travel with respect to the longitudinal axis of the tunnel. The largest strains are most often associated with shear waves. However, as noted in Section 3.8.2, actual peak ground strains from analysis of dense array data are larger than can be attributed to shear wave passage alone, due to the other sources of horizontal ground motion variability. When free‑field ground strains are taken as approximations of strains in underground structures, the effects of SSI are neglected, causing the structural strains to be over‑estimated. More realistic analyses use springs to model the structural stiffness of the underground structure and the stiffness of surrounding soil. As with other substructure SSI problems (e.g., Figures 8.2–8.4), spatially variable ground motions are applied at the ends of springs to evaluate the response of the structure. Additional details on analyses of this type for underground structures are described by Wang (1993) and Hashash et al. (2001) [@HashashEtAl2001].

##### 8.7 SUMMARY

1. Seismic SSI analyses evaluate the response of three linked systems to seismic ground motion – a structure (such as a building or bridge), a foundation (shallow foundations or piles) and the geologic media surrounding the foundation. The purpose of these analyses is to provide a more realistic evaluation of seismic demands in structures and their foundations than is possible from fixed‑base analysis in which the foundation support is assumed as rigid.

1. Seismic SSI analyses can follow a direct approach in which site response is modeled together with the response of the foundation and structure. Analyses of this sort require sophisticated treatment of spatially variable ground motions and accurate modeling of soil, foundation, structural, and interface elements. Alternatively, substructure methods separate the analysis of the effective excitation at the foundation level of a structure (termed the foundation input motion or FIM) from the modeling of foundation‑soil flexibility and damping (using springs and dashpots). The structural response is computed using the FIM to excite the ends of the spring/dashpot elements, which are attached to a model of the structure.

1. The structure‑to‑soil stiffness ratio h/(VsT0) can be used to estimate when inertial SSI effects are likely to be significant. When h/(VsT0) > 0.1, inertial SSI can significantly lengthen the building period and change (generally increase) damping in the system. This will modify the design base shear (up or down, depending on spectral shape) and the distribution of force and deformation demands within the structure, relative to a fixed‑base analysis.

1. The interaction between foundation and soil is described by complex‑valued and frequency‑dependent springs for each vibration mode (translations and rotations in three directions). The use of complex numbers is required to capture the phase differences between demand (force or moment) and response (displacement or rotation), which are effects of damping. A vibrating foundation can also act as a wave source radiating body and surface waves into the surrounding soil medium; the frequency‑dependence of stiffness and damping accounts for the effects of this wave propagation on the foundation response.

1. Models of complex‑valued springs are termed impedance functions. The most basic impedance functions are for rigid shallow foundations resting on the surface of a uniform half‑space. These can be extended for embedment effects, the impact of soil non‑uniformity, and non‑rigid structural foundation elements. Limiting capacities should be used with foundation springs to account for possible effects of soil yielding (e.g., bearing capacity).

1. Impedance models for pile foundations operate similarly to those for shallow foundations, representing the stiffness and damping of the foundation system at the pile head. The most significant pile impedances are for the vertical and lateral modes of vibration. Nonlinearities in pile‑soil interaction, including soil‑pile gapping effects, can be described with macro‑element models distributed along the pile length.

1. Kinematic SSI causes FIMs to deviate from free‑field ground motions as a result of spatially variable ground motions applied to stiff foundation systems. Base slab averaging results from spatial variability of ground motion in the horizontal direction within the perimeter of the foundation system. Embedment and pile effects result from spatial variability of ground motions in the vertical direction. Models that have been validated against field recordings (especially for the cases of base slab averaging and embedment) are available for these effects. Each of these kinematic effects is most pronounced at high frequencies, generally reducing the amplitude of foundation motions relative to those in the free‑field.

1. Practical applications of SSI vary by structure type. For buildings, consideration of SSI is generally optional in current guidelines documents and building codes for the design of new structures or retrofit of older structures. Consideration of SSI is more common for bridge structures, especially at the abutments. SSI is also relatively frequently considered in the analysis and design of nuclear structures. Seismic response is evaluated using force‑based methods, nonlinear static pushover methods, and response history procedures. Both kinematic effects and inertial effects can be considered in each case.

1. Application of SSI principles is important for embedded structures including earth‑retaining structures and underground structures such as tunnels. Under static conditions, lateral earth pressures depend strongly on the level of wall displacement, being minimized for the active case where the wall relaxes away from the backfill and maximized for the passive case in which the wall is advanced into the backfill. At‑rest earth pressures are an intermediate case involving no horizontal displacement.

1. Transient ground shaking from earthquakes cyclically increases and decreases soil reactions against embedded structures due to relative displacements between the structure and free‑field. In the absence of ground failure, these relative displacements can be caused by kinematic interaction and inertia applied to wall elements or underground structures from vibrations of attached superstructures. The primary factors affecting the development of kinematic seismic earth pressures are the amplitude of free‑field ground shaking, the ratio of seismic wavelength to wall height, and the ratio of soil‑to‑wall stiffness. These same factors affect the demands applied to underground structures from vertically propagating shear waves. Additional demands for extended underground structures like tunnels are produced by spatial variations in ground motions and soil conditions in the horizontal direction.
