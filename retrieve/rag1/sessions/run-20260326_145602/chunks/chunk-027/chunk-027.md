$$P_A = K_A \gamma H \quad (8.61)$$

**Figure 8.48**: Rankine active earth pressure distributions for backfills with various combinations of frictional and cohesive strength: (a) friction resistance, no cohesion, (b) cohesive soil, no friction, (c) combined friction and cohesion. (After U.S. Navy, 1982.)

### Example 8.7

A free-standing, unrestrained retaining wall at a Class D soil site has height $H = 6$ m and retains soil with a unit weight of 18 kN/m³, Poisson's ratio of 0.3, and active earth pressure coefficient of 0.25. The wall has good drainage, so that the water table will not build up behind the wall. What is the static earth pressure resultant force?

### Solution

Assuming a triangular distribution of static active earth pressure, the resultant force would be calculated using Equation (8.61) as: $P_A = \frac{1}{2} K_A \gamma H^2 = 0.5 \times 0.25 \times 18\,\text{kN/m}^3 \times (6\,\text{m})^2 = 81\,\text{kN/m}$

Coulomb (1776) [@Coulomb1776] was the first to study the problem of lateral earth pressures on retaining structures. He assumed that the force acting on the back of a retaining wall is that required to maintain equilibrium of a wedge of soil above a planar failure surface (Figure 8.49). The active earth pressure resultant can be computed for a given a wall-soil interface friction angle $\delta$, backfill angle $\beta$, vertical angle of back side of wall $\theta$, and base angle of soil wedge $\alpha_A$. The problem is indeterminate in the sense that angle $\alpha_A$ is unknown and different wall reaction forces are derived for each $\alpha_A$. The solution is obtained by using the surface that produces the greatest active thrust force. The thrust force is related to $K_A$ using Equation (8.61) with $K_A$ expressed as

$$K_A = \frac{\cos^2(\phi' - \theta)}{\cos^2\theta\,\cos(\delta+\theta)\!\left[1 + \sqrt{\dfrac{\sin(\phi'+\delta)\sin(\phi'-\beta)}{\cos(\delta+\theta)\cos(\beta-\theta)}}\right]^2} \quad (8.62)$$

The critical failure surface is inclined at an angle $\alpha_A = -\phi' + \arctan(C_1/C_2) + \text{const}$ (8.63) to the horizontal where

$$C_1 = \tan(\phi'-\beta)\,[\tan(\phi'-\beta) + \cot(\phi'-\theta)] + \tan(\delta+\theta)\cot(\phi'-\theta) \quad (8.64\text{a})$$

$$C_2 = \{1 + \tan(\delta+\theta)\,[\tan(\phi'-\beta) + \cot(\phi'-\theta)]\} \quad (8.64\text{b})$$

**Figure 8.49**: (a) Triangular active wedge bounded at base by planar sliding surface; (b) force polygon for active Coulomb wedge. The critical failure surface is that which maximizes $P_A$.

Coulomb theory does not explicitly predict the distribution of active pressure, but it can be shown to be triangular for linear backfill surfaces with no surface loads. In such cases, $P_A$ acts at a point located $H/3$ above the base of a wall of height $H$ and is inclined to a normal at the back of the wall at the interface friction angle $\delta$, which is typically taken as approximately $1/2$–$2/3$ of $\phi'$ for soil-concrete interfaces and $1/3$–$1/2$ of $\phi'$ for soil-steel interfaces. The logarithmic spiral method for active earth pressures is illustrated in Figure 8.50. Log-spiral methods were introduced for limit equilibrium problems by Rendulic (1935), followed by Taylor (1937), and were first tabulated for use in the prediction of active and passive pressures on retaining walls by Caquot and Kerisel (1948) [@CaquotKerisel1948]. While the major principal stress may act nearly perpendicular to the backfill surface at some distance behind a rough ($\delta > 0$) wall, the presence of shear stresses on the wall-soil interface rotates principal stresses near the back of the wall. If the inclination of principal stresses varies within the backfill, the inclination of the failure surface must also vary. In other words, the failure surface must be curved, which can be described by a logarithmic spiral function. The critical failure surface consists of a curved portion near the back of the wall and a linear portion that extends up to the ground surface (Figure 8.50a). The active earth pressure distribution is triangular (Figure 8.50b) for walls retaining cohesionless backfills. Thus the active soil thrust is given by Equation (8.61) using tabulated values of $K_A$ from Table 8.5. The active earth pressure coefficients given by the log-spiral approach are generally considered to be slightly more accurate than those given by Rankine or Coulomb theory, but the difference is so small that the more convenient Coulomb approach is usually used.

**Figure 8.50**: (a) Logarithmic spiral representation of the critical failure surface for active earth pressure conditions; (b) orientation of critical failure surface for nonvertical wall with inclined backfill surface.

#### 8.6.2.3 Passive Earth Pressures

Solutions for passive earth pressure coefficients have been developed according to the same principles applied for active conditions by Rankine (1857), Coulomb (1776) [@Coulomb1776], and Terzaghi (1943)/Caquot and Kerisel (1948) [@CaquotKerisel1948] (log-spiral). Rankine theory predicts wall pressures given by

$$\sigma_p = K_P \sigma'_v + c' K_P \quad (8.65)$$

where $K_P$ is the coefficient of passive earth pressure. For smooth, vertical walls retaining horizontal backfills,

$$K_P = \frac{1 + \sin\phi'}{1 - \sin\phi'} = \tan^2\!\left(45° + \frac{\phi'}{2}\right) \quad (8.66)$$

and

$$K_P = \cos\beta\,\frac{\cos\beta + \sqrt{\cos^2\beta - \cos^2\phi'}}{\cos\beta - \sqrt{\cos^2\beta - \cos^2\phi'}} \quad (8.67)$$

**Table 8.5**: Values of $K_A$ and $K_P$ for Log-Spiral Failure Surfaces

Columns: $\phi$ (20°, 25°, 30°, 35°, 40°, 45°); rows indexed by $\delta$, $\beta$, $\theta$; values of $K_P$ and $K_A$ given for each combination.

$\delta = 0°$, $\beta = -15°$, $\theta = -10°$: $K_A = 0.37$, $K_P = 1.32$; $K_A = 0.30$, $K_P = 1.66$; $K_A = 0.24$, $K_P = 2.05$; $K_A = 0.19$, $K_P = 2.52$; $K_A = 0.14$, $K_P = 3.09$; $K_A = 0.11$, $K_P = 3.95$

$\delta = 0°$, $\beta = -15°$, $\theta = 0°$: $K_A = 0.42$, $K_P = 1.09$; $K_A = 0.35$, $K_P = 1.33$; $K_A = 0.29$, $K_P = 1.56$; $K_A = 0.24$, $K_P = 1.82$; $K_A = 0.19$, $K_P = 2.09$; $K_A = 0.16$, $K_P = 2.48$

$\delta = 0°$, $\beta = -15°$, $\theta = 10°$: $K_A = 0.45$, $K_P = 0.87$; $K_A = 0.39$, $K_P = 1.03$; $K_A = 0.34$, $K_P = 1.17$; $K_A = 0.29$, $K_P = 1.30$; $K_A = 0.24$, $K_P = 1.33$; $K_A = 0.21$, $K_P = 1.54$

$\delta = 0°$, $\beta = 0°$, $\theta = -10°$: $K_A = 0.42$, $K_P = 2.33$; $K_A = 0.34$, $K_P = 2.96$; $K_A = 0.27$, $K_P = 3.82$; $K_A = 0.21$, $K_P = 5.00$; $K_A = 0.16$, $K_P = 6.68$; $K_A = 0.12$, $K_P = 9.20$

$\delta = 0°$, $\beta = 0°$, $\theta = 0°$: $K_A = 0.49$, $K_P = 2.04$; $K_A = 0.41$, $K_P = 2.46$; $K_A = 0.33$, $K_P = 3.00$; $K_A = 0.27$, $K_P = 3.69$; $K_A = 0.22$, $K_P = 4.59$; $K_A = 0.17$, $K_P = 5.83$

$\delta = 0°$, $\beta = 0°$, $\theta = 10°$: $K_A = 0.55$, $K_P = 1.74$; $K_A = 0.47$, $K_P = 1.89$; $K_A = 0.40$, $K_P = 2.33$; $K_A = 0.34$, $K_P = 2.70$; $K_A = 0.28$, $K_P = 3.14$; $K_A = 0.24$, $K_P = 3.69$

$\delta = 0°$, $\beta = 15°$, $\theta = -10°$: $K_A = 0.55$, $K_P = 3.36$; $K_A = 0.41$, $K_P = 4.56$; $K_A = 0.32$, $K_P = 6.30$; $K_A = 0.23$, $K_P = 8.98$; $K_A = 0.17$, $K_P = 12.2$; $K_A = 0.13$, $K_P = 20.0$

$\delta = 0°$, $\beta = 15°$, $\theta = 0°$: $K_A = 0.65$, $K_P = 2.99$; $K_A = 0.51$, $K_P = 3.86$; $K_A = 0.41$, $K_P = 5.04$; $K_A = 0.32$, $K_P = 6.72$; $K_A = 0.25$, $K_P = 10.4$; $K_A = 0.20$, $K_P = 12.8$

$\delta = 0°$, $\beta = 15°$, $\theta = 10°$: $K_A = 0.75$, $K_P = 2.63$; $K_A = 0.60$, $K_P = 3.23$; $K_A = 0.49$, $K_P = 3.97$; $K_A = 0.41$, $K_P = 4.98$; $K_A = 0.34$, $K_P = 6.37$; $K_A = 0.28$, $K_P = 8.20$

$\delta = \phi'$, $\beta = -15°$, $\theta = -10°$: $K_A = 0.31$, $K_P = 1.95$; $K_A = 0.26$, $K_P = 2.90$; $K_A = 0.21$, $K_P = 4.39$; $K_A = 0.17$, $K_P = 6.97$; $K_A = 0.14$, $K_P = 11.8$; $K_A = 0.11$, $K_P = 22.7$

$\delta = \phi'$, $\beta = -15°$, $\theta = 0°$: $K_A = 0.37$, $K_P = 1.62$; $K_A = 0.31$, $K_P = 2.31$; $K_A = 0.26$, $K_P = 3.35$; $K_A = 0.23$, $K_P = 5.04$; $K_A = 0.19$, $K_P = 7.99$; $K_A = 0.17$, $K_P = 14.3$

$\delta = \phi'$, $\beta = -15°$, $\theta = 10°$: $K_A = 0.41$, $K_P = 1.29$; $K_A = 0.36$, $K_P = 1.79$; $K_A = 0.31$, $K_P = 2.50$; $K_A = 0.27$, $K_P = 3.58$; $K_A = 0.25$, $K_P = 5.09$; $K_A = 0.23$, $K_P = 8.86$

$\delta = \phi'$, $\beta = 0°$, $\theta = -10°$: $K_A = 0.37$, $K_P = 3.45$; $K_A = 0.30$, $K_P = 5.17$; $K_A = 0.24$, $K_P = 8.17$; $K_A = 0.19$, $K_P = 13.8$; $K_A = 0.15$, $K_P = 25.5$; $K_A = 0.12$, $K_P = 52.9$

$\delta = \phi'$, $\beta = 0°$, $\theta = 0°$: $K_A = 0.44$, $K_P = 3.01$; $K_A = 0.37$, $K_P = 4.29$; $K_A = 0.30$, $K_P = 6.42$; $K_A = 0.26$, $K_P = 10.2$; $K_A = 0.22$, $K_P = 17.5$; $K_A = 0.19$, $K_P = 33.5$

$\delta = \phi'$, $\beta = 0°$, $\theta = 10°$: $K_A = 0.50$, $K_P = 2.57$; $K_A = 0.43$, $K_P = 3.50$; $K_A = 0.38$, $K_P = 4.98$; $K_A = 0.33$, $K_P = 7.47$; $K_A = 0.30$, $K_P = 12.0$; $K_A = 0.26$, $K_P = 21.2$

$\delta = \phi'$, $\beta = 15°$, $\theta = -10°$: $K_A = 0.50$, $K_P = 4.95$; $K_A = 0.37$, $K_P = 7.95$; $K_A = 0.29$, $K_P = 13.5$; $K_A = 0.22$, $K_P = 24.8$; $K_A = 0.17$, $K_P = 50.4$; $K_A = 0.14$ (value not given in source)

$\delta = \phi'$, $\beta = 15°$, $\theta = 0°$: $K_A = 0.61$, $K_P = 4.42$; $K_A = 0.48$, $K_P = 6.72$; $K_A = 0.37$, $K_P = 10.8$; $K_A = 0.32$, $K_P = 18.6$; $K_A = 0.25$, $K_P = 39.6$; $K_A = 0.21$, $K_P = 73.6$

$\delta = \phi'$, $\beta = 15°$, $\theta = 10°$: $K_A = 0.72$, $K_P = 3.88$; $K_A = 0.58$, $K_P = 5.62$; $K_A = 0.46$, $K_P = 8.51$; $K_A = 0.42$, $K_P = 13.8$; $K_A = 0.35$, $K_P = 24.3$; $K_A = 0.31$, $K_P = 46.9$

**Figure 8.51**: Rankine passive earth pressure distributions for backfills with various combinations of frictional and cohesive strength: (a) friction resistance, no cohesion, (b) cohesive soil, no friction, (c) combined friction and cohesion. (After U.S. Department of the Navy, 1982.)

for backfills inclined at angle $\beta$ to the horizontal. Passive pressure distributions for various backfill strength characteristics are shown in Figure 8.51. For a dry homogeneous backfill, Rankine theory predicts a triangular passive pressure distribution oriented parallel to the backfill surface. The passive earth pressure resultant, or passive thrust, $P_P$, acts at a point located $H/3$ above the base of a wall of height $H$ (Figure 8.51a) with magnitude

$$P_P = \frac{1}{2} K_P \gamma H^2 \quad (8.68)$$

The passive thrust force from Coulomb theory is also described by Equation (8.68), but with $K_P$ computed as

$$K_P = \frac{\cos^2(\phi'+\theta)}{\cos^2\theta\,\cos(\delta-\theta)\!\left[1 - \sqrt{\dfrac{\sin(\phi'+\delta)\sin(\phi'+\beta)}{\cos(\delta-\theta)\cos(\beta-\theta)}}\right]^2} \quad (8.69)$$

The angles used in the solution are defined in Figure 8.52 and mirror those for the active case, the only difference being the direction of the lateral earth pressure with respect to the back of the wall. The critical failure surface is again planar with an angle $\alpha_P = -\phi' + \arctan(C_1/C_2) + \text{const}$ (8.70) to the horizontal where

$$C_1 = \tan(\phi'+\beta)\,[\tan(\phi'+\beta) + \cot(\phi'+\theta+\delta-\theta)] \quad (8.71\text{a})$$

$$C_2 = \{1 + \tan(\delta-\theta)\,[\tan(\phi'+\beta) + \cot(\phi'+\theta)]\} \quad (8.71\text{b})$$

Whereas the positions of base of the sliding surface for the active case are similar for the Coulomb and log-spiral solutions, the differences can be much more significant in the case of passive earth pressures. As shown in Figure 8.53, the curved portion of the failure surface is much more pronounced than for the active condition and typically extends below the elevation of the wall heel – this makes for a larger failure surface but lower (and thus more critical) values of $K_P$. The passive thrust force from the log-spiral solution for granular backfills is given by Equation (8.68), with the $K_P$ values tabulated in Table 8.5. Experimental results show that maximum passive earth pressure coefficients given by the log-spiral method are considerably more accurate than those given by Rankine or Coulomb theory, which tend to underpredict and overpredict, respectively [@MokwaDuncan2001; @LemnitzerEtAl2009]. The maximum passive earth pressure resultants evaluated using log-spiral methods can be extended to load-deflection relationships using hyperbolic functions, details of which are presented by Shamsabadi et al. (2007) and Khalili-Tehrani et al. (2016) [@KhaliliTehraniEtAl2016]. For bridge abutment applications, it is often required to compute passive capacities for cases in which the inertial load applied to the abutment wall by a bridge deck is skewed relative to the alignment of the abutment. Figure 8.54a shows such a case, with skew angle $\Theta$ defined as the angle between the abutment wall alignment and the transverse direction of the bridge deck. As shown in Figure 8.54a, the bridge deck inertial load $P_L$ is resisted within the abutment by a maximum passive earth pressure resultant $P_P$ and a shear force $P_R$. The value of $P_P$ in this case is reduced relative to the values obtained without skew (i.e., Equations 8.68 with $K_P$ taken from Table 8.5) by the factor $R_\text{skew}$, which depends on skew angle as shown in Figure 8.54b. The fit relationship for $R_\text{skew}$ in Figure 8.54b is based on model tests and numerical simulations (Rollins and Jessee, 2013). For cohesionless backfills, shear resistance $P_R$ is related to $P_P$ as:

$$P_R = P_P \tan\delta \quad (8.72)$$

where $\delta$, as before, is the wall-soil interface friction angle.

**Figure 8.52**: (a) Triangular passive wedge bounded at base by planar sliding surface; (b) force polygon for passive Coulomb wedge. The critical failure surface is that which minimizes $P_P$.

**Figure 8.53**: (a) Logarithmic spiral representation of the critical failure surface for passive earth pressure conditions; (b) orientation of critical failure surface for nonvertical wall with inclined backfill surface.

**Figure 8.54**: (a) Configuration of bridge with skewed abutment showing forces at deck-abutment interface; (b) variation of maximum passive earth pressure resultant reduction factor with skew angle. (Adapted from Rollins and Jessee, 2013.)

### 8.6.3 Seismic Lateral Earth Pressures

As described in Section 8.6.1, earthquake loading changes the earth pressures (demands) acting on embedded structures from those that exist under static conditions. Section 8.6.2 highlighted the profound effect of wall displacement on static lateral earth pressures. Seismic earth pressures can be understood in the same context, but with the additional complexity that both the wall and the free-field soil displace as a result of earthquake shaking. At any point during an earthquake, when the wall displaces away from the backfill, earth pressures can drop from the static condition (if not already in a minimum active state). Conversely, and more importantly for engineering application, at any point in time when the wall displaces toward the backfill, earth pressures will rise relative to the static condition. Since earthquake loading is transient, both increases and decreases in earth pressure are to be expected at different times over the duration of shaking; engineering procedures focus on the former for practical application. Mechanisms that can produce relative wall-soil displacements include: (1) different levels of transient wall displacement relative to the free-field independent of the inertia of structures that may be connected to the wall; (2) free-field permanent ground displacements arising from soil strength loss (e.g., liquefaction, cyclic softening, etc.); and (3) forces applied to a wall/foundation system by attached vibrating structures, which in turn produce relative foundation/free-field displacements independent from those in (1). Mechanism (1) is a kinematic SSI problem having some similarity to the analysis of $u_\text{FIM}$ and $\theta_\text{FIM}$ for embedded structures as described in Section 8.4.2. Mechanism (2) is a ground failure problem and is not discussed further here (analysis procedures for predicting the onset of ground failure are described in Chapter 9; the interaction of lateral spreads with foundations, which may include walls, is described in Section 8.5.2.2). Mechanism (3) is an inertial SSI problem that requires analysis of the response of a structure connected to a suitable foundation system using either direct (Figure 8.1) or substructure (Figures 8.2–8.4) methods of analysis.

The following subsections describe classical methods for the analysis of seismic earth pressure that are based on the acceleration of backfill soil, the kinematic wall response problem and available solutions, and considerations in the inertial wall-soil response problem.

#### 8.6.3.1 Methods Based on Pseudo-Static Backfill Force

For many years, seismic earth pressures on retaining walls have been analyzed using a pseudo-static framework in which accelerations are applied to backfill materials, the wall is assumed to displace forming a soil wedge at a state of shear failure in the backfill (i.e., limit state), and resulting wall force demands are analyzed. Figure 8.55 illustrates the concept for the case of an active soil wedge with horizontal acceleration of $k_h g$ and vertical acceleration of $k_v g$ (where $g$ is acceleration of gravity), which produce horizontal and vertical inertial forces in the backfill. The force polygon in Figure 8.55b illustrates how these inertial forces increase the wall soil interaction force by an amount $P_E$, above the static force $P_A$ (assuming active conditions prior to the earthquake). By solving the equilibrium problem in Figure 8.55b for a variety of acceleration levels, the combined thrust $P_A + P_E$ can be computed as

$$P_A + P_E = \frac{1}{2} \gamma H^2 K_{AE}(1 - k_v) \quad (8.73)$$

where $K_{AE}$ is a seismic earth pressure coefficient that combines the effects of gravity and the pseudo-static inertial forces in the wedge, and is given by (e.g., Koseki et al., 1998) [@KosekiEtAl1998]:

$$K_{AE} = \frac{\cos^2(\phi' - \theta - \psi)}{\cos\psi\,\cos^2\theta\,\cos(\delta+\theta+\psi)\!\left[1 + \sqrt{\dfrac{\sin(\phi'+\delta)\sin(\phi'-\beta-\psi)}{\cos(\delta+\theta+\psi)\cos(\beta-\theta)}}\right]^2} \quad (8.74)$$

The angles $\phi'$, $\theta$, $\beta$, and $\delta$ in Equation (8.74) are as defined in Figure 8.49, and $\psi$ is related to the pseudo-static accelerations as:

$$\psi = \tan^{-1}\!\left(\frac{k_h}{1 - k_v}\right) \quad (8.75)$$

**Figure 8.55**: (a) Retaining wall with horizontal and vertical pseudo-accelerations applied to backfill wedge; (b) force polygon showing the effect of inertial forces from pseudo-acceleration on the wall-soil interaction force.

**Figure 8.56**: Active earth pressure coefficient $K_{AE}$ as derived from M-O formulation for vertical frictionless wall with horizontal backfill and variable levels of horizontal acceleration. The seismic increment is the difference between $K_{AE}$ for the case of finite horizontal acceleration and $k_h = 0$. The angles defining the problem geometry are defined in Figure 8.49. (Adapted from results in Koseki et al., 1998 [@KosekiEtAl1998]; used with permission of Springer Nature BV.)

Figure 8.56 shows values of $K_{AE}$ obtained using Equation (8.75) for a vertical ($\theta = 0$) and smooth ($\delta = 0$) wall with horizontal backfill ($\beta = 0$) subjected to horizontal-only inertial loads ($k_v = 0$). As expected, earth pressures increase with pseudo-acceleration $k_h$, but a notable feature of the solution is that earth pressures are undefined for large accelerations (indicated by the curves becoming nearly vertical), which is a result of soil failure in the backfill (Wood, 2023). Seed and Whitman (1970) observed that for levels of $K_h$ up to about 0.4, the seismic increment of earth pressure could be reasonably approximated by $\Delta K_{AE} = 0.75 k_h$, which can then be used to estimate the combined earth pressure as $K_{AE} \approx K_A + \Delta K_{AE}$. Pseudo-static limit state methods of this type for the active case originate in the classical work by Okabe (1926) and Mononobe and Matsuo (1929) [@MononobeMatsuo1929] [widely known as the "Mononobe-Okabe" (M-O) method]. Variants on the classical approach derived by means of kinematic limit analyses considering non-planar failure surfaces (Chen, 1975 [@Chen1975]; Chen and Liu, 1990 [@ChenLiu1990]), stress fields (Mylonakis et al., 2007), backfill soils with cohesion and friction (National Cooperative Highway Research Program, 2008; Xu et al., 2015), and accounting for the phasing of inertial demands within the retained soil (Steedman and Zeng, 1990) are conceptually alike and provide similar results for the active case. Wood (1973, 2023) considered the case of pre-seismic at-rest earth pressures (as a consequence, the initial condition of the backfill is not at a limit state), which produces larger seismic earth pressures than those of the M-O method. Richart and Elms (1979) considered sliding block displacements of gravity walls (similar to procedures in Section 10.9.2). A shortcoming of the conceptual framework behind this large body of work is its implicit assumption that seismic earth pressures are related to backfill acceleration rather than the relative displacement of the wall and soil. While pseudo-accelerations in the active wedge are associated with motion of the backfill, relative wall-soil motion is not considered because the formulation assumes the wall to be stationary during earthquake shaking. If both the backfill and wall move with comparable, in-phase displacement amplitudes, no appreciable seismic earth pressure will develop, despite the fact that the backfill is accelerating. Hence, there is a conceptual flaw in the classical methods.

Not surprisingly, when seismic earth pressures have been computed from direct analyses (Figure 8.1) or measured experimentally, they seldom conform to predictions from M-O-type procedures when PGA is used to estimate $k_h$. In some cases involving high-frequency ground motions, computed pressures exceed M-O predictions (e.g., Ostadan, 2005; Veletsos and Younan, 1994), while measured pressures in experiments (generally involving relatively low-frequency ground motions) typically fall below M-O predictions (e.g., Al Atik and Sitar, 2010 [@AlAtikSitar2010]; Hushmand et al., 2016 [@HushmandEtAl2016]; Wagner and Sitar, 2016; Candia et al., 2016 [@CandiaMikolaSitar2016]). For these reasons, the continued use of pseudo-acceleration-based (e.g., M-O type) methods is problematic because of their inability to account for the problem physics.

#### 8.6.3.2 SSI-Based Seismic Earth Pressures

The estimation of seismic earth pressures can be improved by recognizing that such pressures develop as a result of SSI involving the wall, supporting and retained soil, and any attached superstructures. As with other SSI problems, both kinematic and inertial components can be significant. Treating the problem that way allows consideration of important effects such as wall and soil stiffness and loading frequency to be taken into account, and produces pressures that are consistent with those obtained from direct analyses and model tests.

**Kinematic Seismic Earth Pressures** Kinematic seismic earth pressures are produced by the combined seismic excitation of shallow layers of soil at a site and a relatively stiff wall system embedded within those soils. Figure 8.29 depicts a U-shaped building basement wall system. Figure 8.57 illustrates the problem for the case of a free-standing wall. In the kinematic problem, the wall itself is assumed to have a certain flexural stiffness but no mass and to be connected to the soil but not to any structure. The ground motions producing the excitation occur over a wide frequency range, typically from about 0.2 to 10 Hz. If these waves can be reasonably assumed as vertically propagating near the ground surface (such that the ground response is one-dimensional; Section 7.5), they produce waves of wavelength $\lambda = V_s/f$ with maximum amplitude at the ground surface (Figure 8.57 and Equation 8.41). Accordingly, at each frequency, and at a given point in time, the horizontal ground motion varies with depth. When this variation is small (i.e., for low frequencies with long wavelengths), the motion of the wall system nearly matches that of the free-field soil, relative wall-soil displacements are small, and seismic earth pressures are low [@BrandenbergEtAl2015]. Conversely, as shown in Figure 8.57, short wavelengths can produce motions that decrease significantly with depth over the height of the wall. Under such conditions, the relatively stiff wall must displace differently from the free-field soil, and the differences in displacement produce potentially large seismic earth pressures. For these short wavelength conditions, the flexibility of the wall system, the distribution with depth of soil stiffness, and the ability of the wall to yield also affect seismic earth pressures. The kinematic problem illustrated in Figure 8.57 can be solved using direct analysis in which the ground response and SSI are solved for simultaneously (Figure 8.1), and procedures of this sort are used for critical projects. Simplified methods are useful to help conceptualize the physics of the problem and for applications where more approximate solutions suffice. For the conditions represented in Figure 8.58, which include rigid wall elements and uniform, elastic backfill soils, an approximate solution for the amplitude of seismic earth pressure resultant $P_E$ (normalized to remove dimensions) is given by Durante et al. (2022) [@DuranteEtAl2022]:

$$\frac{P_E}{k^i_y u_{ff0} H} = \frac{\sin(kH)}{\cos(kH)} - \frac{1}{kH\cos(kH)} \quad (8.76)$$

where $k$ is the wavenumber ($\omega/V_S$), $u_{ff0}$ is the free-field ground surface displacement, and $H$ is wall height (Figure 8.58). The normalized height of resultant $h/H$, where $h$ is measured up to the resultant from the base of the foundation, is given for the same conditions as [@DuranteEtAl2022]:

$$\frac{h}{H} = \frac{\cos(kH) - 1 + \cos(kH)}{\cos(kH)\sin(kH) - kH\cos(kH) \cdot kH} \quad (8.77)$$

Equation (8.77) gives $h/H = 5/8$ for $\lambda/H \gtrsim 4$. The normal stress on the wall is described by the product of relative wall-soil displacement and stiffness intensity $k^i_y$ (introduced in Section 8.3.2.3), which is computed for application to walls as [@KloukinasEtAl2012]:

$$k^i_y = \frac{\pi G}{(1-\nu)(2-\nu)H} \quad (8.78)$$

where $G$ and $\nu$ are the shear modulus and Poisson's ratio of the backfill, respectively.

**Figure 8.57**: Schematic illustration of free-standing retaining wall subjected to seismic waves with different wavelengths. Displacement $u_\text{FIM}$ applies at the foundation level of the wall, and $\theta_\text{FIM}$ represents the rotation of a rigid wall-footing system.

**Figure 8.58**: Schematic rigid wall systems with uniform backfill soils subjected to vertically propagating shear wave showing soil-structure stiffness terms for (a) U-shaped wall and (b) cantilever-type single wall.

**Figure 8.59**: Variation of normalized amplitude of $P_E$ with normalized wavelength $\lambda/H$ for wall founded on rigid base (solution given in Equation 8.76). Dotted line at low $\lambda/H$ is an approximation of the exact solution.

Equations (8.76–8.78) apply for the case of a stiff foundation (infinite base slab stiffnesses $K_y$ and $K_{xx}$), rigid wall, and backfill of uniform stiffness. For those conditions, Figure 8.59 shows the variation of the normalized force amplitude $P_E / (k^i_y u_{ff0} H)$, and its normalized point of application $h/H$, with the ratio of wavelength to wall height $\lambda/H$ (note that this ratio increases with decreasing frequency). The portion of this curve for $\lambda/H \gtrsim 2.7$ typically contains the frequency range of engineering interest. Kinematic pressures are high near $\lambda/H = 2.7$ due to large relative displacements of wall and soil. For smaller $\lambda/H$, relative displacements are large and normalized forces oscillate due to tensile and compressive stress changes acting on different portions of the wall height; this complex behavior is simplified to the dashed horizontal lines shown in Figure 8.59. As $\lambda/H$ increases beyond 2.7, $P_E$ decreases rapidly. In the limiting case where $\lambda/H \to \infty$, the deformed shape of the free-field soil profile becomes vertical, conforming to the shape of the rigid wall and producing zero kinematic interaction. For a given value of $\lambda/H$, the normalization of force accounts for the effects of soil stiffness and shaking amplitude on seismic earth pressures. The normalized resultant height has little variation with $\lambda/H$ beyond 4.0. In addition to wavelength, another critical factor that affects the development of seismic earth pressures is relative soil-to-wall flexibility. A rigid wall is less able to conform with free-field ground motions than is a flexible wall; the effect of increasing wall flexibility is to reduce both relative displacements and seismic earth pressures. Relative soil-to-wall flexibility is parameterized as (Novak, 1974):

$$\beta = \frac{k^i_y}{EI} \quad (8.79)$$

where $E$ is Young's modulus of the wall material and $I$ is the moment of inertia for the wall section (the product represents the wall flexural stiffness). $\beta$ has units of 1/length, and is multiplied by $H$ to remove dimensions. A rigid wall has $\beta H = 0$, but walls with $\beta H < 0.5$ respond in an effectively rigid manner. Rigid or nearly rigid walls are seldom encountered in practice; values of $\beta H$ ranging from 2 to 4 are more common for modern building basement walls in seismically active regions.

**Figure 8.60**: Effect of wall flexibility on (a) normalized wall resultant and (b) its point of application above the foundation. These results are for a rigid base and uniform backfill. (Modified from Durante et al., 2022 [@DuranteEtAl2022]; used with permission of SAGE Publications, Ltd.)

Figure 8.60 shows wall flexibility effects on the seismic earth pressure resultant and its height as derived from finite element analyses [@DuranteEtAl2022]. As shown in Figure 8.60, $P_E$ and its resultant height decrease substantially as wall stiffness decreases (i.e., with increasing $\beta H$). Several additional factors affect seismic earth pressures, but to a lesser degree than wavelength and wall flexibility. One of these is non-uniform backfill conditions in which $V_s$ increases with depth. The effects of velocity gradient have been investigated by holding the time-averaged shear wave velocity within the backfill soil as constant (Vrettos et al., 2016; Brandenberg et al., 2017 [@BrandenbergEtAl2017]). For rigid walls, backfill non-uniformity reduces $P_E$ and its resultant height; however, these effects are small for modest levels of wall flexibility. A second factor is nonlinearity in backfill soils, which both reduces stiffness intensity (Equation 8.78) and decreases wavelength due to modulus reduction. These effects largely offset and the net impact on seismic earth pressure resultant is typically small and can be neglected for simplified analyses [@DuranteEtAl2022]. A third factor is non-rigid (i.e., compliant) foundation conditions, which strongly reduce $P_E$ for rigid walls [@BrandenbergEtAl2015]. However, these effects are more modest for flexible walls [@BrandenbergEtAl2020], and may be neglected for simplified analyses [@DuranteEtAl2022]. The solutions presented in Figures 8.59 and 8.60 can be applied with a free-field ground motion by converting the time series to a Fourier series, computing earth pressure resultants ($P_E$) and moments ($hP_E$) for each frequency in the Fourier series, and computing the resultant force and moment time series using an inverse Fourier transformation. Routines for performing such calculations are presented by Brandenberg et al. (2020) [@BrandenbergEtAl2020]. A more approximate procedure that avoids the need for Fourier transforms simplifies the representation of ground motions by using the intensity measures of PGV (for amplitude) and mean period $T_m$ (for frequency content; Section 3.3.2). This procedure is summarized as follows [@BSSC2020b; @DuranteEtAl2022]:

**Figure 8.61**: Ground motion amplitude adjustment factor for use with simplified method for evaluation of amplitude of seismic earth pressure resultant force $P_E$. (Adapted from Durante et al., 2022 [@DuranteEtAl2022].)

1. Perform a seismic hazard analysis (probabilistic or deterministic) to estimate PGV for the site.

2. If the estimation of PGV is based on probabilistic seismic hazard analysis, disaggregate the hazard (Section 4.4.3.5) at the return period of interest to obtain the controlling magnitudes and distances (either a single mean value or, as appropriate, multiple pairs for distinct contributing sources). Estimate the mean period $T_m$ for this condition (Section 3.5.3.2). If PGV is derived using deterministic methods, use the selected magnitude and distance for the estimation of mean period. Compute the corresponding mean angular frequency $\omega_m = 2\pi / T_m$.

3. Develop a shear wave velocity profile for the backfill soil. Compute the average shear wave velocity $V_{s,av}$ as the ratio of wall height $H$ to shear wave travel time through the backfill. Compute $k_m = \omega_m / V_{s,av}$.

4. Estimate the ground surface displacement as $u_{g0} = f_u \cdot \text{PGV} / \omega_m$. The adjustment factor $f_u$ depends on $\lambda/H$ as shown in Figure 8.61. This factor has been calibrated to match the results of single-frequency analyses to more complete Fourier series analyses.

5. Estimate $k^i_y$ using Equation (8.80) as its static counterpart:

$$k^i_y = \frac{\pi \rho_s V^2_{s,av}}{(1-\nu)(2-\nu)H} \quad (8.80)$$

This expression is modified from Equation (8.78) by removing the frequency-dependent term and by taking $G = \rho_s V^2_{s,av}$, where $\rho_s$ is backfill mass density.

6. Estimate $\beta H$ from the relative soil-to-wall stiffness (Equation 8.79) and wall height $H$. In cases where $\beta H$ is unknown because wall section sizes are undetermined, an initial estimate in the range of 1–2 can be applied and will often be conservative.

7. Compute the normalized force amplitude $P_E / (k^i_y u_{g0} H)$ and resultant height $h/H$. These quantities are obtained for rigid walls using Equations (8.76 and 8.77). The effects of wall flexibility can be incorporated using Figure 8.62 or the following expressions (which describe the change of resultant amplitude and its height with $\beta H$):

$$\frac{P_E}{P_{E,\text{rigid wall}}} = \begin{cases} \exp\!\left(-\dfrac{2.9}{\beta H}\right) - 1 & \beta H < \text{threshold} \\[6pt] \sin(0.45\,\beta H) + 1.43\cos(0.34\,\beta H) + 1.22 & \beta H > \text{threshold} \end{cases} \quad (8.81)$$

$$\frac{h}{H} = \begin{cases} -0.6\exp\!\left(-\dfrac{2.8}{\beta H}\right) - 0.12 & \beta H < \text{threshold} \\[6pt] \sin(1.5\,\beta H) + 1.92\cos(1.68\,\beta H) - 2.87 & \beta H > \text{threshold} \end{cases} \quad (8.82)$$

The relations in Equations (8.81 and 8.82) and Figure 8.62 are curve-fits to finite element simulation results.

8. De-normalize to compute $P_E = (P_E / k^i_y u_{g0} H) \cdot k^i_y u_{g0} H$. The moment at the base of the wall is computed as $M = h P_E$.

Simplifications associated with this procedure include the approximation of the ground motions with intensity measures, neglecting the frequency-dependence of wall-soil stiffness intensity, the treatment of the backfill as uniform and elastic, the treatment of the wall bending response as elastic, and neglecting wall inertia. Despite these assumptions, validation against centrifuge test data and the results of direct analyses (e.g., Al Atik and Sitar, 2010 [@AlAtikSitar2010]; Hushmand et al., 2016 [@HushmandEtAl2016]; Wagner and Sitar, 2016; Candia et al., 2016 [@CandiaMikolaSitar2016]; Ostadan, 2005) show good (if slightly conservative) results, and markedly more reliable predictions than the M-O method [@DuranteEtAl2022].

### Example 8.8

Consider again the wall from Example 8.7. Seismic hazard analyses are performed, and the PGV for the design return period is 50 cm/sec, with a controlling magnitude of 7.0 and source-to-site distance of 15 km. The average small-strain shear wave velocity of the sandy backfill materials over the 6.0 m wall height is 200 m/sec. The wall's relative soil/wall flexibility is $\beta = 0.33$/m. What is the resultant force from kinematic soil-structure interaction?

### Solution

To evaluate the seismic increment, the steps described in the text are applied as follows:

1. The seismic hazard analysis described in the problem statement provides the value of PGV = 50 cm/sec.

2. The expected mean period of the ground motion is computed from the relations in Section 3.5.3.2 (Figure 3.44); the median $T_m$ for the given magnitude and distance is 0.6 sec. The corresponding angular frequency is $\omega_m = 2\pi / T_m = 10.5$ rad/sec.

3. The shear wave velocity is 200 m/sec as given in the problem statement.

4. The ground surface displacement is computed as $u_{g0} = f_u \cdot \text{PGV} / \omega_m$, where the adjustment factor $f_u$ depends on $\lambda/H$. Then, with $\lambda = V_s T_m = 120$ m, the value of $\lambda/H = 20$, so Figure 8.61 shows that $f_u = 0.95$ and $u_{g0}$ can be calculated as $u_{g0} = (0.95)(200\,\text{m/sec}) / 10.5\,\text{sec}^{-1} = 0.045$ m.

5. Recalling that $\nu = 0.3$ from Example 8.7, estimate $k^i_y$ using Equation (8.80) as: $k^i_y = \pi \times (18/9.81) \times 200^2 / [(0.3-1)(0.3-2) \times 6] = 3.5 \times 10^3\,\text{kN/m}^3$ (approximately).

6. Given the relative soil/wall flexibility, $\beta H = 0.33 \times 6 = 2$.

7. The normalized force amplitude for a rigid wall can then be read from Figure 8.59 using $\lambda/H = 20$, which gives a value of $P_E / (k^i_y u_{g0} H) = 0.033$. Since the wall is not rigid, the effects of its flexibility are accounted for by the reduction factor shown in Figure 8.62, which has a value of 0.5. The resulting normalized force amplitude is $0.033 \times 0.5 = 0.017$.

8. From de-normalization, the resultant in force units is $P_E = 0.017 \times k^i_y u_{g0} H = 157\,\text{kN/m}$.

From the above, the overall lateral earth pressure coefficient can be calculated using Equation (8.73) as $K_{AE} = 0.7$. Given $K_A = 0.25$ (from Example 8.7), the seismic response can be seen to nearly triple the earth pressure from the static condition. The static and seismic resultants will generally occur at different heights $h$ above the base of the foundation; the static resultant is at $h/H = 1/3$ whereas the height of the seismic resultant is obtained from Figure 8.62. In this case, the seismic resultant is also at $h/H = 0.42$.

**Inertial Seismic Earth Pressures** The kinematic solution presented above does not consider the effects of inertia. Actual retaining walls have mass, which will produce inertial forces when excited by earthquake shaking. That inertia will affect the wall response and therefore change seismic earth pressures relative to the kinematic case. Relative to the case where inertia is ignored, inertial effects can increase or decrease seismic earth pressures. The combined effects of kinematic and inertial interaction for free-standing walls or basement walls can be analyzed using frequency domain procedures [@BrandenbergEtAl2020]. Such analyses may well be justified when inertial effects may be important, such as when gravity walls are used. Inertial seismic earth pressures are typically most significant when structures are connected to a foundation system containing walls and the lateral force resisting system below the ground level includes those walls (e.g., Figure 8.4b). Under these conditions, the base shear and moment generated by the vibrating structure cause the foundation system to displace horizontally and rotate, producing wall reaction stresses. Analysis of this problem does not require specialized procedures – direct or substructure approaches to the SSI problem can be employed as illustrated in Figures 8.1–8.4 and discussed in Section 8.2. Provided wall-soil interaction elements are included in the SSI model, the reaction stresses against the walls are a natural product of the analysis. It is important to consider the degree to which subterranean walls participate in the below-ground lateral force resisting system in the analysis of inertial effects. Figure 8.63 shows a building in which lateral loads are resisted by a central core of shear walls that extend directly to the foundation mat. If the foundation for the core walls is not structurally connected to the foundations for the surrounding podium (i.e., a portion of the structure with a wider footprint, generally near and below ground line) and floor diaphragms within the podium are either not connected to the core walls or are relatively flexible, the podium's basement walls may see little of the inertial loading. In such cases, the loading of basement walls is likely to be controlled by the kinematic mechanisms described in the previous section. Peak kinematic and inertial seismic demands on basement walls are unlikely to coincide in time. When both effects are expected, load combination rules such as SRSS can be applied.

**Figure 8.63**: Structure with lateral loads resisted by a central core of shear walls supported on a mat foundation that is distinct from the foundations for podium basement walls. In such cases, the degree to which podium basement walls are affected by inertial interaction effects depends on the connectivity of floor diaphragms to the core walls and perimeter walls and their flexibility.

### 8.6.4 Underground Structures

Underground structures such as tunnels, culverts, and pipelines can comprise critical lifelines, the design and analysis of which is a SSI problem that often falls within the purview of geotechnical earthquake engineers. The distinction from retaining walls is that underground structures are buried (they do not extend to the ground surface), they are hollow, low-density inclusions, and their lengths can be much greater than their cross-sectional dimensions. As with other earth-retaining structures, underground structures experience a combination of loading from static lateral (and vertical) earth pressures and additional demands imposed by earthquakes. Seismic demands in structural elements result from two principal sources: (1) spatially variable transient ground displacements that produce relative displacements between free-field and structure, which in turn produce force and moment demands in the lining of the underground structure; and (2) permanent displacements associated with ground failure mechanisms such as soil liquefaction, cyclic softening, and slope instability. The former is addressed in this section; the latter are ground failure problems that are the subject of Chapters 9 and 10. Spatial variations of transient ground motions in both the vertical and horizontal directions can affect underground structures. Vertically variable demands are caused by one-dimensional ground response in a manner similar to that considered in kinematic analysis procedures for walls (Section 8.6.3.2). Horizontally variable demands are caused by wave passage and other spatial variability effects (Section 3.8). The manner by which these demands are considered for underground structures is described in the following subsections [more information can be found in Hashash et al. (2001) [@HashashEtAl2001] and Wang (1993)].

#### 8.6.4.1 Demands from Vertically Propagating Shear Waves

As illustrated in Figure 8.64, vertical shear wave propagation can produce ovaling of circular tunnel sections and racking of rectangular sections (Owen and Scholl, 1981). Analysis procedures for the two cases consider the effects of the vertical variation of ground displacement, and the stiffness of the tunnel lining structure (relative to that of the soil), on the force and moment demands that develop in the lining. As with other SSI problems, these effects can be considered using direct SSI analysis procedures that simultaneously consider the site response and SSI (Section 8.2.1); the focus of this section is on simplified methods that illustrate some of the important physics of the problem. Analysis of ovaling for circular sections begins with the estimation of peak soil shear strain ($\gamma_\text{max}$) over the depth range of the tunnel from site-specific ground response analysis. The ratio of soil stiffness to tunnel lining stiffness in shear (Merritt et al., 1985 [@MerrittEtAl1985]) can be expressed in terms of the flexibility ratio

$$F = \frac{E_s(1-\nu_c^2)\,r_t}{E_c I_c(1+\nu)} \quad (8.83)$$

where $r_t$ is the tunnel radius, $E_s$ is the soil Young's modulus (related to shear modulus $G$, per Equation 8.29), $\nu$ is the soil Poisson's ratio, and $E_c$, $I_c$, and $\nu_c$ are the Young's modulus, moment of inertia, and Poisson's ratio of the tunnel lining material (generally concrete), respectively. Similarly, the ratio of soil medium to tunnel axial stiffness (Merritt et al., 1985 [@MerrittEtAl1985]) can be expressed by the compressibility ratio

$$C = \frac{E_s(1-\nu_c)\,r_t}{E_c t_c(1+\nu)(1-2\nu)} \quad (8.84)$$

where $t_c$ is the thickness of the tunnel lining. The tunnel section diametric strain (computed as ratio of diameter change from ovaling $\Delta d_t$, shown in Figure 8.64, to initial diameter) is then computed assuming full slip between soil and liner [@HashashEtAl2001] as

$$\frac{\Delta d_t}{r_t} = K_1 F \gamma_\text{max} \quad (8.85)$$

where $K_1$ is a response coefficient that depends on $F$ and $\nu$ as shown in Figure 8.65a for the case where slip is allowed at the soil-tunnel interface. Demands within the tunnel liner, specifically the axial thrust force ($T_\text{max}$) and moment ($M_\text{max}$) per unit length [@HashashEtAl2001], are then computed as

$$T_\text{max} = K_2 \frac{E_s}{2(1+\nu)}\,r_t\,\gamma_\text{max} \quad (8.86)$$

$$M_\text{max} = K_3 \frac{E_s}{2(1+\nu)}\,r_t^2\,\gamma_\text{max} \quad (8.87)$$

where $K_2$ (and $K_3$) are response coefficients that depend on $F$, $C$, and $\nu$; results for $\nu = 0.35$ are shown in Figure 8.65b.

**Figure 8.64**: Deformation modes of tunnel or culvert cross-section from vertical shear wave propagation. (Adapted from Hashash et al., 2001 [@HashashEtAl2001] and Owen and Scholl, 1981; used with permission of Elsevier Science and Technology Journals.)

**Figure 8.65**: Response coefficients $K_1$ and $K_2$. Poisson's ratios shown in the figure are for soil ($\nu$). (Plotted from equations in Wang, 1993.)

**Figure 8.66**: Free-field racking deformation imposed on a buried rectangular frame. (Adapted from Wang, 1993.)

Analysis of racking for rectangular sections begins with the evaluation of a ground displacement profile as shown in Figure 8.66 and the relative free-field displacement between the top and bottom of the tunnel section $\Delta_\text{diff}$. The racking stiffness of the tunnel section $K_t$ is evaluated as the ratio of force (per unit length)/deflection to produce deformations of the type shown on the right side of Figure 8.66. The flexibility ratio $F_r$ for this case is then computed as:

$$F_r = \frac{G\,w}{K_t\,h} \quad (8.88)$$

where $w$ and $h$ are width and height of the tunnel, as shown in Figure 8.66. The ratio of tunnel/free-field displacement ($\Delta_t / \Delta_\text{diff}$) is then evaluated from $F_r$ as shown in Figure 8.67. Internal member demands are evaluated from displacement $\Delta_t$ using standard structural analyses.

#### 8.6.4.2 Demands from Horizontally Variable Ground Motions

Horizontally variable ground motions have the potential to produce axial and bending deformations of underground structures (Figure 8.68). As described in Section 3.8, these variations in ground shaking arise from horizontal wave passage (most predominantly in the direction from source-to-site) and more complex stochastic processes that produce spatial variations in amplitude and phase. Horizontally variable motions can also occur at boundaries between soils of different impedance, for example as might occur when a tunnel or pipeline passes from stiff soils beneath a hill into softer (and possibly even liquefiable) soils in an adjacent alluvial valley; sharp impedance contrasts at such material boundaries can impose high flexural demands on buried structures.

**Figure 8.67**: Dependence of tunnel-to-free-field displacement ratio with flexibility ratio $F_r$. Full slip results from Wang (1993) and Penzien (2000), no slip results from Penzien (2000). (Figure adapted from Power et al., 2006.)

**Figure 8.68**: Deformation modes of underground structures due to traveling waves producing (a) tension/compression and (b) bending. (Adapted from Owen and Scholl, 1981.)

A first-order approximation of axial and bending strains induced in tunnel sections from horizontal ground motion variability is to assume they are equal to corresponding free-field ground strains (i.e., implicitly assuming that the tunnel is completely flexible). As described in Section 3.8.2, spatially variable ground strains from wave passage can cause a variety of shear and axial strains depending on wave type (p-waves, s-waves, surface waves) and direction of wave travel with respect to the longitudinal axis of the tunnel. The largest strains are most often associated with shear waves. However, as noted in Section 3.8.2, actual peak ground strains from analysis of dense array data are larger than can be attributed to shear wave passage alone, due to the other sources of horizontal ground motion variability. When free-field ground strains are taken as approximations of strains in underground structures, the effects of SSI are neglected, causing the structural strains to be over-estimated. More realistic analyses use springs to model the structural stiffness of the underground structure and the stiffness of surrounding soil. As with other substructure SSI problems (e.g., Figures 8.2–8.4), spatially variable ground motions are applied at the ends of springs to evaluate the response of the structure. Additional details on analyses of this type for underground structures are described by Wang (1993) and Hashash et al. (2001) [@HashashEtAl2001].

## 8.7 Summary

1. Seismic SSI analyses evaluate the response of three linked systems to seismic ground motion – a structure (such as a building or bridge), a foundation (shallow foundations or piles) and the geologic media surrounding the foundation. The purpose of these analyses is to provide a more realistic evaluation of seismic demands in structures and their foundations than is possible from fixed-base analysis in which the foundation support is assumed as rigid.

2. Seismic SSI analyses can follow a direct approach in which site response is modeled together with the response of the foundation and structure. Analyses of this sort require sophisticated treatment of spatially variable ground motions and accurate modeling of soil, foundation, structural, and interface elements. Alternatively, substructure methods separate the analysis of the effective excitation at the foundation level of a structure (termed the foundation input motion or FIM) from the modeling of foundation-soil flexibility and damping (using springs and dashpots). The structural response is computed using the FIM to excite the ends of the spring/dashpot elements, which are attached to a model of the structure.

3. The structure-to-soil stiffness ratio $h/(V_s T_0)$ can be used to estimate when inertial SSI effects are likely to be significant. When $h/(V_s T_0) > 0.1$, inertial SSI can significantly lengthen the building period and change (generally increase) damping in the system. This will modify the design base shear (up or down, depending on spectral shape) and the distribution of force and deformation demands within the structure, relative to a fixed-base analysis.

4. The interaction between foundation and soil is described by complex-valued and frequency-dependent springs for each vibration mode (translations and rotations in three directions). The use of complex numbers is required to capture the phase differences between demand (force or moment) and response (displacement or rotation), which are effects of damping. A vibrating foundation can also act as a wave source radiating body and surface waves into the surrounding soil medium; the frequency-dependence of stiffness and damping accounts for the effects of this wave propagation on the foundation response.

5. Models of complex-valued springs are termed impedance functions. The most basic impedance functions are for rigid shallow foundations resting on the surface of a uniform half-space. These can be extended for embedment effects, the impact of soil non-uniformity, and non-rigid structural foundation elements. Limiting capacities should be used with foundation springs to account for possible effects of soil yielding (e.g., bearing capacity).

6. Impedance models for pile foundations operate similarly to those for shallow foundations, representing the stiffness and damping of the foundation system at the pile head. The most significant pile impedances are for the vertical and lateral modes of vibration. Nonlinearities in pile-soil interaction, including soil-pile gapping effects, can be described with macro-element models distributed along the pile length.

7. Kinematic SSI causes FIMs to deviate from free-field ground motions as a result of spatially variable ground motions applied to stiff foundation systems. Base slab averaging results from spatial variability of ground motion in the horizontal direction within the perimeter of the foundation system. Embedment and pile effects result from spatial variability of ground motions in the vertical direction. Models that have been validated against field recordings (especially for the cases of base slab averaging and embedment) are available for these effects. Each of these kinematic effects is most pronounced at high frequencies, generally reducing the amplitude of foundation motions relative to those in the free-field.

8. Practical applications of SSI vary by structure type. For buildings, consideration of SSI is generally optional in current guidelines documents and building codes for the design of new structures or retrofit of older structures. Consideration of SSI is more common for bridge structures, especially at the abutments. SSI is also relatively frequently considered in the analysis and design of nuclear structures. Seismic response is evaluated using force-based methods, nonlinear static pushover methods, and response history procedures. Both kinematic effects and inertial effects can be considered in each case.

9. Application of SSI principles is important for embedded structures including earth-retaining structures and underground structures such as tunnels. Under static conditions, lateral earth pressures depend strongly on the level of wall displacement, being minimized for the active case where the wall relaxes away from the backfill and maximized for the passive case in which the wall is advanced into the backfill. At-rest earth pressures are an intermediate case involving no horizontal displacement.

10. Transient ground shaking from earthquakes cyclically increases and decreases soil reactions against embedded structures due to relative displacements between the structure and free-field. In the absence of ground failure, these relative displacements can be caused by kinematic interaction and inertia applied to wall elements or underground structures from vibrations of attached superstructures. The primary factors affecting the development of kinematic seismic earth pressures are the amplitude of free-field ground shaking, the ratio of seismic wavelength to wall height, and the ratio of soil-to-wall stiffness. These same factors affect the demands applied to underground structures from vertically propagating shear waves. Additional demands for extended underground structures like tunnels are produced by spatial variations in ground motions and soil conditions in the horizontal direction.
