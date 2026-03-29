$$u(z,t) = A\cos(kz)\,e^{i\omega t} \tag{10.6}$$

and the shear stress is given by

$$\tau(z,t) = G\frac{\partial u(z,t)}{\partial z} = -GkA\sin(kz)\,e^{i\omega t} \tag{10.7}$$

Dividing the shear stress by the total vertical stress (assuming a constant density, $\rho$), the ratio of shear stress to total vertical stress at depth, $z$, is given by

$$\frac{\tau(z,t)}{\sigma_v} = \frac{GkA\sin(kz)}{\rho gz}\,e^{i\omega t} = \frac{V_s\omega A}{gz}\sin(kz)\,e^{i\omega t} \tag{10.8}$$

Now, the average acceleration of the soil above depth, $z$, can be computed as

$$\bar{a}(z,t) = \frac{1}{z}\int_0^z \ddot{u}(z,t)\,dz = \frac{\omega A\sin(kz)}{kz}\,e^{i\omega t} \tag{10.9}$$

Recognizing that $k = \omega/V_s$, the right side of Equation (10.9) can be divided by the acceleration of gravity to express the average acceleration as a fraction of gravity,

$$\frac{\bar{a}(z,t)}{g} = \frac{V_s\omega A}{gz}\sin(kz)\,e^{i\omega t} \tag{10.10}$$

Comparing Equations (10.10) and (10.8) shows that

$$\frac{\tau(z,t)}{\sigma_v} = \frac{\bar{a}(z,t)}{g} \tag{10.11}$$

i.e., the average acceleration of the soil above a particular depth, expressed as a fraction of gravity, is equal to the shear stress at that depth divided by the total vertical stress. This average acceleration is referred to as the horizontal equivalent acceleration, HEA($t$) and can also be expressed in terms of a horizontal equivalent acceleration coefficient, $k_h(t) = \text{HEA}(t)/g = \bar{a}(t)/g$. Note that the average acceleration above a particular depth differs from the actual acceleration at that depth due to the compliance of the overlying soil. The average acceleration accounts for the fact that the soil at different points above the depth of interest are moving by different amounts and out of phase with each other – some may even be moving to the left when others are moving to the right. For the simple case of harmonic loading, Equations (10.5), (10.7), and (10.10) can be manipulated to show that the ratio of maximum horizontal equivalent acceleration, MHEA, to peak ground surface acceleration, $a_\text{max}$, is given by

$$\frac{\text{MHEA}}{a_\text{max}} = \frac{\sin(2\pi z/\lambda)}{2\pi z/\lambda} \tag{10.12}$$

where $\lambda$ is wavelength, i.e., $\lambda = 2\pi V_s/\omega$. Equation (10.12) indicates that the ratio is 1.0 at the ground surface, decreases with depth at a rate that increases with decreasing wavelength (i.e., increasing frequency and/or decreasing shear wave velocity), and approaches zero at very large depths (corresponding to many wavelengths). Figure 10.20 shows this variation as a function of depth/wavelength for a harmonic motion, with values equal to zero occurring between nodes of standing waves (Section 7.5.1.2). Because seismic waves include many frequencies, each of which has a different wavelength, the reduction in horizontal equivalent acceleration with actual depth will be more complicated than shown in Figure 10.20 for normalized depth but the trend of generally decreasing amplitude with depth illustrated in that figure still applies. Equation (10.11) also shows that the average acceleration within a dynamically responding body can be obtained from the stresses acting on its boundaries. The same basic concepts used in the one-dimensional case here apply to the more realistic cases of two- and three-dimensional slopes. As previously described, waves can travel in many different directions in such cases leading to incoherent vertical and horizontal motions within a potentially unstable zone of soil. Approaches to handling the effects of such incoherence (Clough and Chopra, 1966; Seed and Martin, 1966) involve integrating the horizontal components of shear and normal stresses on a potential failure surface (Figure 10.21) and dividing the resulting horizontal force by the weight of the soil above the failure surface to obtain the horizontal equivalent acceleration coefficient, $k_h(t) = \text{HEA}(t)/g$. The resultant inertial force acting on the unstable soil is the product of its mass and the horizontal equivalent acceleration (or of its weight and the horizontal equivalent acceleration coefficient).

**FIGURE 10.20** Reduction of horizontal equivalent acceleration amplitude with normalized depth for a single harmonic motion. Note that MHEA and $a_\text{max}$ are defined as absolute values.

**FIGURE 10.21** Evaluation of average acceleration for potential failure mass within an embankment. Two-dimensional numerical analysis predicts variations of shear and normal stresses on potential failure surface with time. Integration of horizontal components of stresses over failure surface gives resultant horizontal force acting within the potential failure mass. A time series of average acceleration is obtained by dividing resultant force by mass of potentially unstable soil.

### 10.9.1.3 Selection of Pseudostatic Coefficient

The results of pseudostatic analyses are critically dependent on the specified value of the seismic coefficient, $k_h$. Selection of an appropriate pseudostatic coefficient is the most important, and most difficult, aspect of a pseudostatic stability analysis. The seismic coefficient controls the pseudostatic force acting on the failure mass, so its value should be related to some measure of the amplitude of the inertial force induced in the potentially unstable material. In its original form, pseudostatic analyses were typically performed by applying the peak ground surface acceleration to a rigid failure mass. If the pseudostatic coefficient is based on the peak acceleration, i.e., $k_h = a_\text{max}/g$, a factor of safety of 1.0 would correspond to the point of incipient instability, and a factor of safety greater than 1.0 would imply no movement. A pseudostatic factor of safety less than 1.0 would imply failure with the unstable mass of soil accelerating in the downslope direction. However, the accelerations produced by earthquake shaking are transient rather than constant as assumed in the pseudostatic approach, and so the state of "failure" may not last for very long. As will be discussed in detail in Section 10.9.2, the result of a peak acceleration-based factor of safety temporarily falling below 1.0 will be a temporary acceleration of the unstable mass (relative to the material beneath it) and an increment of downslope movement. As recognition grew that actual slopes are not rigid and that the peak acceleration exists for only an instant in time, the pseudostatic coefficients used in practice generally corresponded to acceleration values well below $a_\text{max}$. Terzaghi (1950) originally suggested the use of $k_h = 0.1$ for "severe" earthquakes (Rossi-Forel IX), $k_h = 0.2$ for "violent, destructive" earthquakes (Rossi-Forel X), and $k_h = 0.5$ for "catastrophic" earthquakes. Seed (1979) listed pseudostatic design criteria for 14 dams in ten seismically active countries; 12 required minimum factors of safety of 1.0–1.5 with pseudostatic coefficients of 0.10–0.12. Hynes-Griffin and Franklin (1984) applied the sliding block analysis method described in the following section to over 350 accelerograms and concluded that earth dams with pseudostatic factors of safety greater than 1.0 using $k_h = 0.5\,a_\text{max}$ would not develop "dangerously large" deformations, which they interpreted as being up to approximately 1 m. As the preceding discussion indicates, there are no hard and fast rules for selection of a pseudostatic coefficient for design. In reality, the serviceability (or performance) of a slope is more closely related to the permanent deformations it undergoes than to the value of the factor of safety itself. A slope with a high pseudostatic factor of safety will generally displace less than a slope with a low pseudostatic factor of safety when subjected to the same earthquake motion. As will be discussed in Section 10.9.2.5, the relationship between pseudostatic factor of safety and permanent displacement can be used to identify a pseudostatic acceleration level that is consistent with a specified allowable level of permanent displacement. Such an approach represents the most appropriate use of the pseudostatic approach at this time.

### 10.9.1.4 Discussion

The pseudostatic approach has a number of attractive features. The analysis is relatively simple and straightforward; indeed, its similarity to the static limit equilibrium analyses routinely conducted by geotechnical engineers makes its computations easy to understand and perform. It produces a scalar index of stability (the factor of safety) that is analogous to that produced by static stability analyses. However, representation of the complex, transient, dynamic effects of earthquake shaking by a single constant unidirectional pseudostatic acceleration is obviously quite crude. Even in its infancy, the limitations of the pseudostatic approach were clearly recognized. Terzaghi (1950) stated that "the concept it conveys of earthquake effects on slopes is very inaccurate, to say the least," and that a slope could be unstable even if the computed pseudostatic factor of safety was greater than 1. Indeed, pseudostatic analyses of a number of dams that failed in earthquakes (Table 10.4) show factors of safety well above 1.0. Detailed analyses of earthquake-induced landslides (e.g., Seed et al., 1969, 1975; Marcuson et al., 1979) have illustrated significant shortcomings of the pseudostatic approach.

**TABLE 10.4** Results of Pseudostatic Analyses of Earth Dams that Failed During Earthquakes

Sheffield (CA): $k_h = 0.10$, FS = 1.2. Effect of earthquake: Complete failure.

Lower San Fernando (CA): $k_h = 0.15$, FS = 1.3. Effect of earthquake: Upstream slope failure (~2–2.5 ft).

Upper San Fernando (CA): $k_h = 0.15$, FS ~1.3. Effect of earthquake: Downstream shell, including crest, slipped about 6 ft downstream.

Tailings dam (Japan): $k_h = 0.20$. Effect of earthquake: Failure of dam with release of tailings.

**FIGURE 10.22** Analogy between (a) potential landslide and (b) block resting on inclined plane.

Experience has clearly shown, for example, that pseudostatic analyses can be unreliable for soils that build up large pore pressures or show more than about 15% degradation of strength due to earthquake shaking. Difficulty in the assignment of appropriate pseudostatic coefficients and in interpretation of pseudostatic factors of safety, coupled with the development of more realistic methods of analysis, have largely reduced the use of the pseudostatic approach for seismic slope stability analyses to screening applications. Methods based on evaluation of permanent slope deformation, such as those described in Section 10.9.2.5, are now commonly used for seismic slope stability analysis. Such deformation analyses can be used to identify pseudostatic coefficients that are consistent with specific levels of computed soil displacement. Using such coefficients in pseudostatic analyses provide factors of safety against exceeding desired allowable displacements. In this way, slopes that pass the screen are unlikely to exceed the allowable displacement.

###### 10.9.2 Sliding Block Analysis

The pseudostatic method of analysis, like all limit equilibrium methods, provides an index of stability (the factor of safety) but no information on deformations associated with slope failure. Since the serviceability of a slope after an earthquake is controlled by deformations, analyses that predict slope displacements provide a more useful indication of seismic slope performance. Earthquake-induced accelerations, and the inertial forces they produce, vary with time, so the factor of safety against slope failure will also vary over the duration of an earthquake. If the inertial forces acting on a potential failure mass become large enough that the total (static plus dynamic) driving forces exceed the available resisting forces, the factor of safety will drop below 1.0. When its factor of safety drops below 1.0, a potential failure mass is no longer in equilibrium; consequently, it will be accelerated by the unbalanced force. In 1963, Whitman laid out the principles by which a potentially unstable slope could be treated as a block resting on an inclined plane (Marcuson, 1994) subjected to horizontal shaking (Figure 10.22). Newmark (1965) further developed the sliding block model for prediction of the permanent displacement of a slope subjected to a specific ground motion.

Sliding block analyses allow calculation of permanent displacements for a very simple analog to a potentially unstable slope. The initial (pre-earthquake) stability of the slope is computed, the level of shaking required to initiate instability is determined, and permanent displacements are computed for specific ground motions. The required calculations are relatively simple, at least for the original, rigid block model. The limiting assumptions of the original, rigid block model have led to the development of more sophisticated sliding block models and procedures. The primary distinction between currently available sliding block models is related to the compliance, or flexibility, of the block that represents the soil above a potential failure surface. It should be noted that sliding block analyses predict deformations associated with shearing; additional deformations associated with volume change (Section 6.6.5.4) can occur and should be computed separately to determine the total deformation associated with earthquake shaking. Both components can be computed simultaneously in a numerical analysis with an appropriate constitutive model.

### 10.9.2.1 Rigid Block Analysis

The original sliding block model employed the same basic assumptions used in static and pseudostatic limit equilibrium analyses – the material above the failure surface was assumed to be rigid and the interface between the block and plane was assumed to exhibit rigid-perfectly plastic behavior.

**Rigid Block Mechanics** Consider the rigid block in stable, static equilibrium on the inclined plane of Figure 10.23. Under static conditions, equilibrium of the block (in the direction parallel to the plane) requires that the static driving force, $D_s$ (Figure 10.23a), be less than the available static resisting force, $R_s$. Assuming that the block's resistance to sliding is purely frictional ($c = 0$),

$$\text{FS} = \frac{R_s}{D_s} = \frac{N\tan\phi}{W\sin\beta} = \frac{W\cos\beta\tan\phi}{W\sin\beta} = \frac{\tan\phi}{\tan\beta} \tag{10.13}$$

where $W$ is the weight of the block, $\phi$ is the angle of friction between the block and the plane, and $\beta$ is the inclination of the plane. Now consider the effect of inertial forces transmitted to the block by horizontal shaking of the inclined plane with acceleration, $a_h(t) = k_h(t)g$ (the effects of vertical accelerations will be neglected for simplicity). Because the block is rigid, the acceleration throughout it is constant. At a particular instant of time, horizontal acceleration of the block will induce a horizontal inertial force, $k_h W$ (Figure 10.23b). When the inertial force acts in the downslope direction, resolving forces parallel to the inclined plane gives

$$\text{FS}_d(t) = \frac{R_d(t)}{D_d(t)} = \frac{\tan\phi[\cos\beta - k_h(t)\sin\beta]}{\sin\beta + k_h(t)\cos\beta} \tag{10.14}$$

where $R_d$ and $D_d$ are the dynamic resisting and driving forces, respectively.

**FIGURE 10.23** Forces acting on a block resting on an inclined plane: (a) static conditions; (b) dynamic conditions.

**FIGURE 10.24** Variation of pseudostatic factor of safety with horizontal pseudostatic coefficient for block on plane inclined at 20°. For $\phi = 20°$, block is at the point of failure (FS = 1) under static conditions ($k_h = 0$), so the yield coefficient is zero. For $\phi = 30°$ and $\phi = 40°$, yield coefficients are 0.17 and 0.36, respectively.

Obviously, the dynamic factor of safety decreases as $k_h$ increases and there will be (for a statically stable block) some positive value of $k_h$ that will produce a factor of safety of 1.0 (Figure 10.24). This coefficient, termed the yield coefficient, $k_y$, corresponds to the yield acceleration, $a_y = k_y g$. The yield acceleration is the minimum pseudostatic acceleration required to produce instability of the block. For the block of Figure 10.23, using Equation (10.14) with $\text{FS}_d = 1.0$ gives the yield coefficient

$$k_y = \tan(\phi - \beta) \tag{10.15}$$

for sliding in the downslope direction. For sliding in the uphill direction (which can occur when $\beta$ and $\phi$ are small),

$$k_y = \frac{\tan\phi + \tan\beta}{1 + \tan\phi\tan\beta} \tag{10.16}$$

### Example 10.3

Compute the yield acceleration for the slope described in Example 10.2.

**Solution:**

The yield acceleration can be computed by trial and error, or computed directly for relatively simple slopes. Reviewing Example 10.2, it is apparent that the total moment is equal to

$$(4{,}488\ \text{k-ft/ft}) + (149.6\ \text{k/ft})(38\ \text{ft})\ k_h + (1{,}438\ \text{k-ft/ft}) + (287.5\ \text{k/ft})(62\ \text{ft})\ k_h$$

$$= 5{,}926\ \text{k-ft/ft} + 23{,}510\ \text{k-ft/ft}\cdot k_h$$

The yield coefficient is the value of $k_h$ that produces a pseudostatic factor of safety of 1.0. Because the resisting moment is equal to the overturning moment when FS = 1.0,

$$5{,}926\ \text{k-ft/ft} + 23{,}510\ \text{k-ft/ft}\cdot k_h = 10{,}624\ \text{k-ft/ft}$$

or

$$k_h = \frac{10{,}624 - 5{,}926}{23{,}510} = \frac{7{,}508}{23{,}510} = 0.067$$

Therefore, the yield acceleration is 0.067g.

When a block on an inclined plane is subjected to a pulse of acceleration that is lower than the yield acceleration, the block and plane move together with no relative displacement. If the acceleration of the plane exceeds the yield acceleration, the block cannot move as quickly as the plane and therefore moves relative to the plane – the plane is, in a sense, pulled out from under the block and the block moves to a lower position on the plane. To illustrate the procedure by which the resulting permanent displacements can be calculated, consider the case in which an inclined plane is subjected to a base acceleration history, $a_b(t)$, consisting of a single rectangular acceleration pulse of amplitude, $A$, and duration, $\Delta t$. If the yield acceleration, $a_y$, is less than $A$ (Figure 10.25a), the acceleration of the block relative to the plane during the period from $t_0$ to $t_0 + \Delta t$ is

$$a_\text{rel}(t) = a_b(t) - a_y = A - a_y, \quad t_0 \leq t \leq t_0 + \Delta t \tag{10.17}$$

The relative movement of the block during this period can be obtained by integrating the relative acceleration twice, i.e.,

$$v_\text{rel}(t) = \int_{t_0}^{t} a_\text{rel}(t)\,dt = (A - a_y)(t - t_0), \quad t_0 \leq t \leq t_0 + \Delta t \tag{10.18}$$

$$d_\text{rel}(t) = \int_{t_0}^{t} v_\text{rel}(t)\,dt = (A - a_y)(t - t_0)^2/2, \quad t_0 \leq t \leq t_0 + \Delta t \tag{10.19}$$

**FIGURE 10.25** Variation of relative velocity and relative displacement between sliding block and plane due to rectangular pulse that exceeds yield acceleration between $t = t_0$ and $t = t_0 + \Delta t$.

At $t = t_0 + \Delta t$, the relative velocity reaches its maximum value. At that time,

$$v_\text{rel}(t_0 + \Delta t) = (A - a_y)\Delta t \tag{10.20}$$

$$d_\text{rel}(t_0 + \Delta t) = (A - a_y)\Delta t \tag{10.21}$$

After the base acceleration, $a_b(t)$, drops below $a_y$ (in this case to zero at $t = t_0 + \Delta t$), the block does not stop sliding but rather the sliding block is decelerated by the friction force acting on its base. The block will continue to slide on the plane, but at a decreasing relative velocity that eventually reaches zero. The acceleration during this time is given by

$$a_\text{rel}(t) = a_b(t) - a_y = 0 - a_y = -a_y, \quad t_0 + \Delta t \leq t \tag{10.22}$$

where $t_1$ is the time at which the relative velocity becomes zero (note that the block undergoes negative acceleration, or deceleration, during this period). Between $t_0 + \Delta t$ and $t_1$, the relative velocity will decrease with time according to

$$v_\text{rel}(t) = v_\text{rel}(t_0 + \Delta t) + \int_{t_0+\Delta t}^{t} a_\text{rel}\,dt = (A - a_y)\Delta t - a_y(t - t_0 - \Delta t), \quad t_0 + \Delta t \leq t \tag{10.23}$$

Setting the relative velocity equal to zero at $t = t_1$ gives

$$t_1 = t_0 + \Delta t + \frac{(A - a_y)\Delta t}{a_y} = t_0 + \frac{A\,\Delta t}{a_y} \tag{10.24}$$

Then, for $t_0 + \Delta t \leq t \leq t_1$,

$$d_\text{rel}(t) = (A - a_y)\Delta t\,(t - t_0 - \Delta t) - \tfrac{1}{2}\,a_y(t - t_0 - \Delta t)^2 \tag{10.25}$$

After time $t_1$, the block and inclined plane move together again. During the total period of time between $t = t_0$ and $t = t_1$, the relative movement of the block is shown in Figure 10.25. Between $t_0$ and $t_0 + \Delta t$, the relative velocity increases linearly and the relative displacement quadratically. At $t_0 + \Delta t$, the relative velocity has reached its maximum value, after which it decreases linearly. The relative displacement continues to increase (but at a decreasing rate) until $t = t_1$. Note that the total relative displacement is given by the sum of Equations (10.19) and (10.25),

$$d_\text{rel}(t_1) = \frac{(A - a_y)^2 \Delta t^2}{2\,a_y} \tag{10.26}$$

This displacement depends strongly on both the amount by which, and the length of time during which, the yield acceleration is exceeded. This suggests that the relative displacement caused by a single pulse of strong ground motion should be related to both the amplitude and frequency content of that pulse. An earthquake motion, however, can exceed the yield acceleration a number of times and produce a number of increments of displacement (Figure 10.26). Thus the total displacement will be influenced by strong-motion duration as well as amplitude and frequency content. Indeed, application of this approach to a variety of simple waveforms (e.g., Sarma, 1975; Yegian et al., 1991) has shown that the permanent displacement of a sliding block subjected to rectangular, sinusoidal, and triangular periodic base motions is proportional to the number of pulses and the square of their period.

**FIGURE 10.26** Development of permanent slope displacements for actual earthquake ground motion. (After Wilson and Keefer, 1985.)

**FIGURE 10.27** Illustration of influence of yield acceleration on sliding block displacements: (a) $a_y = 0.4g$, (b) $a_y = 0.3g$, (c) $a_y = 0.2g$.

**Rigid Block Behavior** Obviously, the sliding block model will predict zero permanent slope displacement if earthquake-induced accelerations never exceed the yield acceleration ($a_\text{max} < a_y$). Since the permanent displacement is obtained by double integration of the excess acceleration, the computed displacements for a slope with a relatively low yield acceleration (small $a_y/a_\text{max}$) will be greater than that of a slope with a higher yield acceleration. Figure 10.27 illustrates how the computed displacements increase quickly with decreasing yield acceleration. The relationship between slope displacement and $a_\text{max}/a_y$ has been investigated by a number of researchers. Sarma (1975) and Yegian et al. (1988) derived closed-form solutions for the permanent displacement, $D$, produced by simple periodic (triangular, sinusoidal, and rectangular) input motions (Figure 10.28). To allow measures of frequency content and duration to be considered explicitly, Yegian et al. (1991) used the database of Franklin and Chang (1977) to develop the following expression for median normalized displacement:

$$\log\!\left(\frac{D}{D_n}\right) = -0.22 - 10.12\frac{a_y}{a_\text{max}} + 16.38\left(\frac{a_y}{a_\text{max}}\right)^2 - 11.48\left(\frac{a_y}{a_\text{max}}\right)^3 \tag{10.27}$$

with $D_n = N_\text{eq}\,T\,(a_\text{max}/g)$ and $\sigma_{\log D_n} = 0.45$ ($\sigma_{\ln D_n} = 1.04$). In Equation (10.27), $N_\text{eq}$ is an equivalent number of cycles and $T$ is the predominant period of the input motion.

### 10.9.2.2 Decoupled Rigid Block Analyses

Of course, the material above the failure plane in a soil slope is never truly rigid. Actual slopes are compliant – they deform during earthquake shaking. Their dynamic response depends on their geometry and stiffness and on the amplitude and frequency content of the motion of the underlying ground. The amplitude of the motion within a particular failure mass can be amplified or deamplified by the materials and geometry of the slope itself. The dynamic response of the soils above a failure surface can be accounted for and used to compute the average acceleration of a potential failure mass using dynamic stress-deformation analyses (Chopra, 1966). Using a dynamic analysis, the time-varying horizontal components of the dynamic stresses acting on a potential failure surface can be integrated over the failure surface to produce the time-varying resultant horizontal force that acts on the potential failure surface. This resultant force can then be divided by the mass of the soil above the potential failure surface to produce the average horizontal acceleration of the potential failure mass. The average acceleration time history, which may be of greater or smaller amplitude than the base acceleration time history (depending on the input motions and the amplification characteristics of the slope), accounts for both vertical and lateral variability of acceleration within the slope and provides a more realistic input motion for a sliding block analysis of the compliant potential failure mass. In a decoupled analysis (Makdisi and Seed, 1978; Bray et al., 1995; Bray et al., 1998; Rathje and Antonakos, 2011), the average acceleration time history computed in a dynamic analysis is used as the input motion in a rigid sliding block analysis.

**FIGURE 10.28** Variation of normalized permanent displacement with ratio of yield acceleration to maximum acceleration for simple waveforms. The normalized permanent displacement is defined in Equation (10.27). (After Yegian et al., 1991.)

The decoupled procedure can be viewed as a two-step process in which the sliding displacement analysis is decoupled from the dynamic response analysis. In the first step, a dynamic analysis of the compliant slope is performed, and its results are used to compute time histories of average acceleration corresponding to one or more potential failure surfaces passing through the slope. The slope is modeled as a continuum – no discrete failure surfaces are provided; in fact the analyses are usually performed using equivalent linear procedures so that no failure (or permanent deformation) is allowed to occur. These analyses typically idealize the slope as a soil column (one-dimensional) or as plane-strain (two-dimensional). It should be recognized that the average acceleration time histories for different potential failure surfaces will be different. In the second step, a conventional rigid sliding block analysis is performed with the average acceleration from the first step used as the input motion. Multiple potential failure surfaces should be examined in order to find the one that maximizes the slope displacement; the critical static surface will not necessarily produce the largest slope displacement under seismic loading conditions.

### 10.9.2.3 Coupled Compliant Block Analysis

The two-step decoupled procedure can account for the dynamic response of the soil above the failure surface but implicitly assumes that that response is unaffected by any slip that occurs on the failure surface. The validity of that assumption was investigated in the context of earth dam stability by Lin and Whitman (1986) and Gazetas and Uddin (1994). Lin and Whitman (1986) concluded that the decoupled procedure was somewhat conservative (i.e., predicted higher displacements) at frequencies above the fundamental frequency of the dam, and most conservative at and near the fundamental frequency. Gazetas and Uddin (1994) found generally good agreement between coupled and decoupled displacements, but found the decoupled procedure to produce conservative results for narrow-band motions that coincide with the natural frequency of the dam. A compliant slope idealized as a one-dimensional lumped mass system (Kramer and Smith, 1997) to provide a first-order approximation of coupled sliding behavior showed that decoupled procedures overpredicted displacements of thin and/or stiff failure masses and underpredicted them for thick and/or soft ones. Normalizing the fundamental period of the failure mass, $T_s$, by the mean period of the input motion, $T_m$ (Section 3.3.2.2), a more refined generalized SDOF model (Rathje and Bray, 1999) showed that the decoupled procedure was conservative (overpredicted displacements) at $a_y/a_\text{max} < 0.6$ and slightly unconservative at higher $a_y/a_\text{max}$ values for $T_s/T_m = 1.0$. At $T_s/T_m = 4.0$ (i.e., for relatively thick and/or soft failure masses), decoupled analyses were unconservative at all $a_y/a_\text{max}$ ratios. Similarly, rigid block analyses were shown to underpredict permanent displacements at $T_s/T_m = 1.0$ and overpredict them at $T_s/T_m = 4.0$. The general behavior of coupled and decoupled models relative to rigid block behavior is illustrated in Figure 10.29. Rathje and Bray (2000) used a one-dimensional nonlinear site response program to consider the effects of material nonlinearity on coupled sliding behavior and found results that were generally similar to those of Kramer and Smith (1997) and Rathje and Bray (1999); decoupled analyses were found to be potentially unconservative for systems with larger $T_s/T_m$ ratios and $a_y/a_\text{max}$ values greater than 0.4. As one-dimensional procedures, these analyses do not account for lateral incoherency of motions within the failure mass.

### 10.9.2.4 Sliding Block-Based Displacement Predictions

Sliding block analyses are not particularly difficult to perform in practice. Jibson et al. (2013) developed a program that can compute sliding block displacements for user-specified ground motions and yield accelerations. A number of researchers have performed and compiled the results of numerous sliding block analyses and used the results to develop predictive equations for sliding block displacements. These equations relieve the user of having to perform the actual sliding block analyses, but produce results that are representative of the suite of ground motions used to develop the equations, which may or may not be representative of the ground motion hazards at a particular site of interest. The different predictive relationships make different assumptions about the nature of the potentially unstable material (e.g., rigid or compliant) and the manner in which the level of shaking is characterized (e.g., by various intensity measures and in terms of peak base or horizontal equivalent acceleration). The following subsections break these predictive relationships into rigid block and compliant block categories and provide examples of relationships based on scalar IMs, mixed scalar IMs, and vector IMs within each category.

**Rigid Block Displacements** A number of investigators have used rigid block analyses to develop predictive relationships for sliding block displacements. For rigid blocks, horizontal equivalent accelerations are equivalent to base motions. These studies have been performed with increasingly broad ground motion databases and interpreted with increasingly sophisticated statistical analyses. The most current procedures are based on thousands of ground motions and allow estimation of probability distributions of predicted displacements. The procedures use different IMs, which differ in the extent to which they reflect amplitude, frequency content, and duration, to characterize the ground motions. Some models characterize ground motions with a single (scalar) IM, but others use multiple (vector) IMs to provide a more complete characterization of the motion. The models, therefore, differ in their complexity and in the dispersion of their predictions.

**Scalar IMs** The earliest scalar methods predicted permanent displacement as a function of peak acceleration, generally through the yield acceleration ratio, $a_y/a_\text{max}$. Ambraseys and Menu (1988) used recorded ground motions to show that plots of displacement vs. $a_y/a_\text{max}$ showed shapes that were similar to those of the sinusoidal and triangular waves at $a_y/a_\text{max}$ values greater than about 0.5. Ambraseys and Menu (1988) proposed that displacements could be predicted by an equation of the form

$$\log D = a + b\log\!\left(1 - \frac{a_y}{a_\text{max}}\right) + c\log\!\left(\frac{a_y}{a_\text{max}}\right) \tag{10.28}$$

for $0.1 \leq a_y/a_\text{max}$, $6.6 \leq M_s \leq 7.3$, with $D$ in cm and $a_y$ computed using residual soil strength. Using 50 motions from 11 earthquakes, Ambraseys and Menu (1988) found that median displacements were best predicted with $a = 0.90$, $b = 2.53$, and $c = -1.09$; the displacements were predicted with a variability of $\sigma_{\log D} = 0.30$ ($\sigma_{\ln D} = 0.69$). Using many more motions (2,270 recorded motions from 30 earthquakes) covering a broader range of earthquake magnitudes, Jibson (2007) found that Equation (10.28) matched the computed sliding block displacements best with $a = 0.215$, $b = 2.341$, and $c = -1.438$, giving $\sigma_{\log D} = 0.510$ ($\sigma_{\ln D} = 1.17$). Although the uncertainty in Jibson's calibration is higher, its median displacements are about one-third of those of Ambraseys and Menu (1988). These $\sigma_{\ln D}$ values, which represent the fit of the predictive equation to the sliding block model displacements (not to actual observed slope displacements) are extremely high. The additional epistemic uncertainty of interest, i.e., the model uncertainty in actual slope displacement given a computed sliding block displacement, is not provided by these relationships.

**Mixed Scalar IMs** More recent investigations have found that improved predictions can be made by including the source parameter, moment magnitude, in addition to peak acceleration, which results in a "mixed" (ground motion IM and source parameter) measure of ground motion intensity. Jibson (2007) found that the dispersion of his scalar model could be reduced by including magnitude as

$$\log D = -2.710 + 2.335\log\!\left(1 - \frac{a_y}{a_\text{max}}\right) - 1.478\log\!\left(\frac{a_y}{a_\text{max}}\right) + 0.424\,M \tag{10.29}$$

where $D$ is in cm. For this relationship, $\sigma_{\log D} = 0.454$ ($\sigma_{\ln D} = 1.045$). The use of magnitude in the relationship introduces information on the frequency content and duration of the ground motion, both of which are relevant to sliding block displacements. As magnitude increases, seismic waves have longer periods and longer durations, both of which increase displacement for a given $a_y/a_\text{max}$. Saygili and Rathje (2008) developed a model based on peak ground acceleration and earthquake magnitude with which permanent displacement could be computed as

$$\ln D = -4.89 - 4.85\frac{a_y}{a_\text{max}} - 19.64\left(\frac{a_y}{a_\text{max}}\right)^2 + 42.49\left(\frac{a_y}{a_\text{max}}\right)^3 - 29.06\left(\frac{a_y}{a_\text{max}}\right)^4 + 0.72\ln M + 0.89\ln(a_\text{max}/g) \tag{10.30}$$

with

$$\sigma_{\ln D} = 0.732 + 0.789\frac{a_y}{a_\text{max}} - 0.530\left(\frac{a_y}{a_\text{max}}\right)^2$$

where $D$ is in cm, and the yield acceleration, $a_y$, and peak acceleration, $a_\text{max}$, are in the same units. Figure 10.30 shows the variation of median displacement with yield acceleration ratio for different earthquake magnitudes. Noting the logarithmic nature of the displacement scale, the displacement can be seen to increase quickly as the peak acceleration exceeds the yield acceleration and to increase with increasing magnitude and, to a lesser degree, peak acceleration.

**FIGURE 10.30** Variation of predicted sliding block displacement with yield acceleration ratio for different earthquake magnitudes and peak ground accelerations using Saygili and Rathje (2008) model.

### Example 10.4

For the slope described in Example 10.3, estimate the 50th and 84th percentile permanent displacement when subjected to the Alhambra-Fremont School E-W record (see Figure 3.14) from the 1994 Northridge earthquake. Use the procedures of Jibson (Equation 10.29) and Saygili and Rathje (Equation 10.30).

**Solution:**

From Figure 3.14, the peak acceleration of the Alhambra-Fremont School motion was 0.10g. Therefore, the normalized yield acceleration, $a_y/a_\text{max} = 0.067\text{g}/0.1\text{g} = 0.67$. Using Equation (10.29), the Jibson (2007) 50th and 84th percentile displacements are

$$\log D = -2.710 + 2.335\log(1 - 0.67) - 1.478\log(0.67) + 0.424(6.7) = -0.7364$$

$$D_{50} = 10^{-0.7364} = 0.18\ \text{cm}$$

$$\log D_{84} = \log D_{50} + \sigma_{\log D} = -0.7364 + 0.454 = -0.2824 \quad \Rightarrow \quad D_{84} = 0.52\ \text{cm}$$

Using Equation (10.30), the Saygili and Rathje (2008) permanent displacements are

$$\ln D = -4.89 - 4.85(0.67) - 19.64(0.67)^2 + 42.49(0.67)^3 - 29.06(0.67)^4 + 0.72\ln(6.7) + 0.89\ln(0.1) = -1.287$$

$$D_{50} = e^{-1.287} = 0.28\ \text{cm}$$

$$\sigma_{\ln D} = 0.732 + 0.789(0.67) - 0.530(0.67)^2 = 1.023$$

$$\ln D_{84} = \ln D_{50} + \sigma_{\ln D} = -1.287 + 1.023 = -0.264 \quad \Rightarrow \quad D_{84} = e^{-0.264} = 0.77\ \text{cm}$$

**Vector IMs** Vector methods are based on the assumption that the use of additional ground motion information will lead to more accurate displacement predictions. Since sliding block displacements have been shown to be influenced by amplitude, frequency content, and duration, IMs that reflect those characteristics or, for example, reflect amplitudes over a range of different frequencies, should provide more accurate estimates of displacement. Rathje and Saygili (2009) added peak ground velocity, PGV, to peak ground acceleration (eliminating $M$) and produced a model of the form

$$\ln D = -1.56 - 4.58\frac{a_y}{a_\text{max}} - 20.84\left(\frac{a_y}{a_\text{max}}\right)^2 + 44.75\left(\frac{a_y}{a_\text{max}}\right)^3 - 30.5\left(\frac{a_y}{a_\text{max}}\right)^4 - 0.64\ln(a_\text{max}/g) + 1.55\ln(\text{PGV}) \tag{10.31}$$

$$\sigma_{\ln D} = 0.41 + 0.52\frac{a_y}{a_\text{max}}$$

where $D$ is in cm, $a_y$ and $a_\text{max}$ are expressed as fractions of gravity, and PGV is in cm/sec. By including PGV, this model indirectly incorporates effects of frequency content, but does not incorporate duration. Median displacements from the PGA-PGV model are shown in Figure 10.31. The dispersion of the PGA-PGV model varies with $a_y/a_\text{max}$ but is much lower than that of the PGA-$M$ model, indicating a significantly greater efficiency in displacement prediction. As will be discussed in Section 10.12, the vector model leads to some complications in the prediction of ground motion hazards, but the improved efficiency can lead to substantial benefits in a performance-based slope displacement analysis.

**Compliant Block Displacements** Compliant block models of both decoupled and coupled forms have also been used with large ground motion databases to compile predictive relationships for slope deformations.

**FIGURE 10.31** Variation of predicted sliding block displacement with yield acceleration ratio for different earthquake magnitudes and peak ground accelerations using Saygili and Rathje (2009) model.

**Scalar IMs** Makdisi and Seed (1978) used a decoupled procedure with average accelerations computed by the procedure of Chopra (1966) and sliding block analyses to compute earthquake-induced permanent deformations of earth dams and embankments. By using average accelerations instead of base accelerations, this approach directly accounts for the dynamic response of the compliant material within the failure mass. By subjecting several real and hypothetical dams to several actual and synthetic ground motions scaled to represent different earthquake magnitudes, Makdisi and Seed computed the variation of permanent displacement with $a_\text{max}/a_y$, $T_s$, and magnitude. The use of magnitude accounts for the effects of duration and, albeit to a lesser degree, frequency content. Prediction of permanent displacements by the Makdisi-Seed procedure is accomplished with the charts shown in Figure 10.32. The bands shown in Figure 10.32b suggest a significant degree of variability in the predicted normalized displacements although the actual level of variability was not formally evaluated. The Makdisi-Seed procedure has been a cornerstone of practice in seismic slope stability evaluation since its introduction some 40 years ago but was based on what would now be considered an extremely small number of ground motions; newer predictive relationships are based on many more motions from many more earthquakes and provide much more robust predictions of slope displacement with quantified characterization of variability. The effects of frequency content and duration can be accounted for more explicitly than by using magnitude as in Figure 10.32. Bray and Rathje (1998) accounted for both amplitude and frequency content through the use of a maximum equivalent horizontal acceleration coefficient, $k_\text{max} = \text{MHEA}/g$, and duration through the significant duration, $D_{5\text{-}95}$ (Section 3.3.3).

$$\log D = 1.87 - 3.477\frac{k_y}{k_\text{max}} - k_\text{max}\cdot D_{5\text{-}95} \tag{10.32}$$

where $D$ = displacement in cm, $k_y$ = yield coefficient, and the approximate (common log) standard deviation of the normalized displacement is 0.35 (Bray, 2007). The Bray and Rathje (1998) procedure (Figure 10.33) requires more effort than that of Makdisi and Seed (1978) but is based on many more ground motions and accounts for ground motions and dynamic response in a more comprehensive manner.

**FIGURE 10.32** Variation of normalized permanent displacement with yield acceleration for earthquakes of different magnitudes: (a) summary for several earthquakes and dams/embankments; (b) average values. (After Makdisi and Seed, 1978 with permission of ASCE.)

**FIGURE 10.33** Variation of normalized displacement with $k_y/k_\text{max}$. (After Bray and Rathje, 1998 with permission of ASCE.)

**Mixed Scalar IMs** Bray and Travasarou (2007) found that compliant sliding block displacements for ground motions from shallow crustal earthquakes along active plate margins were better correlated to spectral accelerations at a lengthened period (that reflected soil stiffness degradation) than to peak acceleration. To account for softening due to soil nonlinearity, Bray and Travasarou (2007) identified a spectral acceleration at a multiple of the initial (low-strain) fundamental period of the slope, as an efficient intensity measure for sliding block displacement, and used it to develop a two-part model that treats the predicted displacement as a mixed (discrete-continuous) random variable with a probability density function

$$f_D(d) = p\cdot\delta(d - d_0) + (1 - p)\cdot f_D(d) \tag{10.33}$$

where $p$ = discrete probability mass that the displacement is less than some value, $d_0$, considered to be negligible, $\delta(d - d_0)$ = Dirac delta function (equal to 1.0 for $d \leq d_0$ and zero elsewhere), and $f_D(d)$ = probability density function for $d > d_0$. Using a larger, updated crustal ground motion database, Bray and Macedo (2019) found that for negligible predicted displacements (i.e., less than 0.5 cm – $d_0 < 0.5$ cm), the discrete probability mass can be computed as

$$p = \begin{cases} -\Phi\!\left(-2.48 - 2.97\ln k_y - 0.12\ln\!\left(\dfrac{k_y}{T_s}\right) - 0.72\ln k_y + 1.70 + 2.78\ln[S_a(1.3T_s)T_s]\right) & T_s \leq 0.7\ \text{sec} \\[6pt] -\Phi\!\left(-3.42 - 4.93\ln k_y - 0.30\ln\!\left(\dfrac{k_y}{T_s}\right) - 0.35\ln k_y + 0.62 + 2.86\ln[S_a(1.3T_s)T_s]\right) & T_s > 0.7\ \text{sec} \end{cases} \tag{10.34}$$

where $S_a(1.3T_s)$ = RotD50 5%-damped spectral acceleration at a period of $1.3T_s$ in units of g of design outcropping ground motion for site conditions below potential sliding mass [i.e., the value of $S_a(1.3T_s)$ for the earthquake ground motion at the elevation of the sliding surface if the potential sliding mass was removed]. The median displacement greater than 1 cm can then be computed (in cm) as

$$\ln D = a_1 + 2.482\ln k_y + 0.244\ln k_y^2 - 0.344\ln(k_y)\ln S_a(1.3T_s) + 2.649\ln S_a(1.3T_s) + 0.090\ln S_a(1.3T_s)^2 + a_2 T_s + a_3 T_s^2 + 0.603\,M \pm 1\varepsilon\,\sigma_{\ln D} \tag{10.35}$$

where $a_1 = -5.981$, $a_2 = 3.223$, and $a_3 = -0.945$ for systems with $T_s \geq 0.10$ sec, and $a_1 = -4.684$, $a_2 = -9.471$, and $a_3 = 0.0$ for $T_s < 0.10$ sec, with $\sigma_{\ln D} = 0.72$. Bray et al. (2018) presented a similar model for subduction zone events and Bray and Macedo (2019) also present models for rigid sliding blocks (i.e., $T_s = 0.0$) and for maximum and median displacements caused by near-fault pulse motions. With the median and uncertainty terms established for these models, the probability that the displacement exceeds some allowable displacement, $d_\text{all}$, can be computed as

$$P[D > d_\text{all}] = (1 - p)\cdot P[D > d_\text{all} \mid D > d_0] = (1 - p)\left[1 - \Phi\!\left(\frac{\ln d_\text{all} - \ln\bar{D}}{\sigma_{\ln D}}\right)\right] \tag{10.36}$$

The Saygili and Rathje (2008) rigid block model (Equation 10.30) was modified to account for failure mass compliance in the form of the natural period of the sliding mass, $T_s$ (Rathje and Antonakos, 2011). Using the average acceleration within the sliding mass, $a_\text{max}$, and magnitude to characterize the level of ground shaking, median displacements are predicted as

$$\ln D = -4.89 - 4.85\frac{a_y}{a_\text{max}} - 19.64\left(\frac{a_y}{a_\text{max}}\right)^2 + 42.49\left(\frac{a_y}{a_\text{max}}\right)^3 - 29.06\left(\frac{a_y}{a_\text{max}}\right)^4 + 0.72\ln M + 0.89\ln(a_\text{max}/g) + f(T_s) \tag{10.37}$$

with $D$ in cm and

$$f(T_s) = \begin{cases} -3.69 - 1.22\ln T_s & T_s \leq 1.5\ \text{sec} \\ 2.78 & T_s > 1.5\ \text{sec} \end{cases}$$

$$\sigma_{\ln D} = 0.694 + 0.322\frac{a_y}{a_\text{max}}$$

The value of $a_\text{max}$ can be estimated from the relationship

$$\ln\!\left(\frac{a_\text{max}}{\text{PGA}}\right) = -0.459 - 0.702\ln\!\left(\frac{T_s}{T_m}\right)\cdot 0.228 - 0.076\ln\!\left(\frac{T_s}{T_m}\right)\cdot\ln\!\left(\frac{\text{PGA}}{0.1}\right) \tag{10.38}$$

where PGA is the peak acceleration and $T_m$ is the mean period (Section 3.3.2.2) of the base motion.

### Example 10.5

A slope in southern California is determined to have a yield acceleration of 0.10g for a failure mass with a fundamental period, $T_s = 0.46$ sec. If the slope was subjected to a repeat of the El Centro ground motion (EW component, Figure 3.9b) from the 1940 Imperial Valley ($M$ 6.9) earthquake, compute the median displacement and the probability that the displacement would exceed 30 cm.

**Solution:**

Using the procedure of Bray and Macedo (2019) for crustal ground motions, the elongated period of interest would be $1.3 \times 0.46 = 0.60$ sec. From Figure 3.9b, the spectral acceleration at the elongated period would be 610 cm/sec² = 0.622g. Then, from Equation (10.34), the probability of negligible ($< 0.5$ cm) displacement would be

$$p = 1 - \Phi(-3.948) \approx 0.00004$$

which indicates that there is essentially zero probability that the displacements will be negligible. Then, since $T_s > 0.1$ sec, the median displacement is obtained from

$$\ln D = -5.981 - 2.482\ln(0.1) - 0.244\ln(0.1)^2 - 0.344\ln(0.1)\ln(0.622) + 2.649\ln(0.622) + 0.090\ln(0.622)^2 + 3.223(0.46) - 0.945(0.46)^2 + 0.603(6.9) = \ln(20.9)$$

The median displacement is thus approximately 20.9 cm.

The probability that the lateral displacement would exceed 30 cm is therefore

$$P[D > 30\ \text{cm}] = 1 - \Phi\!\left(\frac{\ln 30 - \ln 20.9}{0.72}\right) = 1 - \Phi(0.308) \approx 0.38$$

**Vector IMs** The Rathje and Saygili (2009) rigid block vector model was also extended (Rathje and Antonakos, 2011) to account for failure mass compliance.

$$\ln D = -1.56 - 4.58\frac{a_y}{a_\text{max}} - 20.84\left(\frac{a_y}{a_\text{max}}\right)^2 + 44.75\left(\frac{a_y}{a_\text{max}}\right)^3 - 30.5\left(\frac{a_y}{a_\text{max}}\right)^4 - 0.64\ln(a_\text{max}/g) + 1.55\ln(k\text{-vel}_\text{max}) + f(T_s) \tag{10.39}$$

with

$$f(T_s) = \begin{cases} 1.42 & T_s \leq 0.5\ \text{sec} \\ 0.71 & T_s > 0.5\ \text{sec} \end{cases}$$

and

$$\sigma_{\ln D} = 0.40 + 0.284\frac{a_y}{a_\text{max}}$$

where the term $k\text{-vel}_\text{max}$ is the peak value of a velocity-like parameter obtained by integrating the time history of normalized average acceleration, i.e.,

$$k\text{-vel}_\text{max} = \int_{-\infty}^{\infty} \frac{a(t)}{g}\,dt \tag{10.40}$$

or, with knowledge of PGV, estimated from

$$\ln(k\text{-vel}_\text{max}) = \begin{cases} 0.240 + \ln\!\left(\dfrac{\text{PGV}}{\text{PGA}}\right) + 0.091\ln\!\left(\dfrac{T_s}{T_m}\right) - 0.171\ln\!\left(\dfrac{T_s}{T_m}\right) & T_s/T_m \geq 0.2 \\[6pt] \ln(0.2) + \ln\!\left(\dfrac{\text{PGV}}{\text{PGA}}\right) & T_s/T_m < 0.2 \end{cases} \tag{10.41}$$
