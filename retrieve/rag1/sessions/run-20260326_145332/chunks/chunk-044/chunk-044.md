The displacement amplitude of the transmitted wave is:

$$u_T(x,t) = A_T e^{i(\omega t - kx)} \tag{C.67c}$$

Stress-strain and strain-displacement relationships can be used to relate the stress amplitudes to the displacement amplitudes:

$$\sigma_I(x,t) = M \frac{\partial u_I}{\partial x} = -ik_M M A_i e^{i(\omega t - kx)} \tag{C.68a}$$

$$\sigma_R(x,t) = M \frac{\partial u_R}{\partial x} = +ik_M M A_r e^{i(\omega t + kx)} \tag{C.68b}$$

$$\sigma_T(x,t) = M \frac{\partial u_T}{\partial x} = -ik_M M A_t e^{i(\omega t - kx)} \tag{C.68c}$$

From these, the stress amplitudes are related to the displacement amplitudes by

$$\sigma_i = -ik_M M A_i \tag{C.69a}$$

$$\sigma_r = +ik_M M A_r \tag{C.69b}$$

$$\sigma_t = -ik_M M A_t \tag{C.69c}$$

At the interface ($x = 0$), both compatibility of displacements and continuity of stresses must be satisfied. The former requires that

$$u_I(0,t) + u_R(0,t) = u_T(0,t) \tag{C.70}$$

and the latter that

$$\sigma_I(0,t) + \sigma_R(0,t) = \sigma_T(0,t) \tag{C.71}$$

Substituting Equations (C.67) and (C.66) into Equations (C.70) and (C.71), respectively, indicates that

$$A_i + A_r = A_t \tag{C.72}$$

$$\sigma_i + \sigma_r = \sigma_t \tag{C.73}$$

at the interface. Substituting Equations (C.69) into Equation (C.73) and using the relationship $k_M = \omega\rho v$, gives

$$-\rho_1 v_1 A_i + \rho_1 v_1 A_r = -\rho_2 v_2 A_t = -\rho_2 v_2(A_i + A_r) \tag{C.74}$$

Equation (C.74) can be rearranged to relate the displacement amplitude of the reflected wave to that of the incident wave:

$$A_r = \frac{\rho_1 v_1 - \rho_2 v_2}{\rho_1 v_1 + \rho_2 v_2} A_i \tag{C.75}$$

The displacement amplitude of the transmitted wave can be similarly derived as:

$$A_t = \frac{2\rho_1 v_1}{\rho_1 v_1 + \rho_2 v_2} A_i \tag{C.76}$$

Remember that the product of the mass density and the wave propagation velocity is the specific impedance of the material. Equations (C.75) and (C.76) indicate that the partitioning of energy at the interface depends only on the ratio of the specific impedances of the materials on either side of the interface. Defining the impedance ratio as $\alpha_z = \rho_2 v_2 / \rho_1 v_1$, the displacement amplitudes of the reflected and transmitted waves are

$$A_r = \frac{1 - \alpha_z}{1 + \alpha_z} A_i \tag{C.77}$$

$$A_t = \frac{2}{1 + \alpha_z} A_i \tag{C.78}$$

After evaluating the effect of the interface on the displacement amplitudes of the reflected and transmitted waves, its effect on stress amplitudes can be investigated. From Equations (C.69)

$$\sigma_i = -ik_M M A_i \tag{C.79a}$$

$$\sigma_r = +ik_M M A_r \tag{C.79b}$$

$$\sigma_t = -ik_M M A_t \tag{C.79c}$$

Substituting Equations (C.79) into Equations (C.77) and (C.78) and rearranging gives

$$\sigma_r = \frac{1 - \alpha_z}{1 + \alpha_z} \sigma_i \tag{C.80}$$

$$\sigma_t = \frac{2\alpha_z}{1 + \alpha_z} \sigma_i \tag{C.81}$$

The importance of the impedance ratio in determining the nature of reflection and transmission at interfaces can clearly be seen. Equations (C.77), (C.78), (C.80), and (C.81) indicate that fundamentally different types of behavior occur when the impedance ratio is less than or greater than 1. When the impedance ratio is less than 1, an incident wave can be thought of as approaching a "softer" material. For this case, the reflected wave will have a smaller stress amplitude than the incident wave and its sign will be reversed (an incident compression pulse will be reflected as a tensile pulse, and vice versa). If the impedance ratio is greater than 1, the incident wave is approaching a "stiffer" material in which the stress amplitude of the transmitted wave will be greater than that of the incident wave and the stress amplitude of the reflected wave will be less than, but of the same sign, as that of the incident wave. The displacement amplitudes are also affected by the impedance ratio. The displacement amplitude of a wave transmitted from a stiffer material into a softer material will be greater than that of the incident wave. The relative stress and displacement amplitudes of reflected and transmitted waves at boundaries with several different impedance ratios are illustrated in Table 5.1.

**TABLE C.1** Influence of Impedance Ratio on Displacement and Stress Amplitudes of Reflected and Transmitted Waves

Displacement Amplitudes — Stress Amplitudes — Impedance Ratio $\alpha_z$ — Incident — Reflected — Transmitted — Incident — Reflected — Transmitted

$\alpha_z = 0$: $A_i$ — $A_i$ — $2A_i$ — $\sigma_i$ — $-\sigma_i$ — $0$

$\alpha_z = 1/4$: $A_i$ — $3A_i/5$ — $8A_i/5$ — $\sigma_i$ — $-3\sigma_i/5$ — $2\sigma_i/5$

$\alpha_z = 1/2$: $A_i$ — $A_i/3$ — $4A_i/3$ — $\sigma_i$ — $-\sigma_i/3$ — $2\sigma_i/3$

$\alpha_z = 1$: $A_i$ — $0$ — $A_i$ — $\sigma_i$ — $0$ — $\sigma_i$

$\alpha_z = 2$: $A_i$ — $-A_i/3$ — $2A_i/3$ — $\sigma_i$ — $\sigma_i/3$ — $4\sigma_i/3$

$\alpha_z = 4$: $A_i$ — $-3A_i/5$ — $2A_i/5$ — $\sigma_i$ — $3\sigma_i/5$ — $8\sigma_i/5$

$\alpha_z = \infty$: $A_i$ — $-A_i$ — $0$ — $\sigma_i$ — $\sigma_i$ — $2\sigma_i$

The cases of $\alpha_z = 0$ and $\alpha_z = \infty$ are of particular interest. An impedance ratio of zero implies that the incident wave is approaching a "free end" across which no stress can be transmitted ($\sigma_t = 0$). To satisfy this zero stress boundary condition, the displacement of the boundary (the transmitted displacement) must be twice the displacement amplitude of the incident wave ($A_t = 2A_i$). The reflected wave has the same amplitude as the incident wave but is of the opposite polarity ($\sigma_r = -\sigma_i$). In other words, a free end will reflect a compression wave as a tension wave of identical amplitude and shape and a tension wave as an identical compression wave. An infinite impedance ratio implies that the incident wave is approaching a "fixed end" at which no displacement can occur ($u_r = 0$). In that case, the stress at the boundary is twice that of the incident wave ($\sigma_t = 2\sigma_i$) and the reflected wave has the same amplitude and polarity as the incident wave ($A_r = -A_i$). The case of $\alpha_z = 1$, in which the impedances on each side of the boundary are equal, is also of interest. Equations (C.77), (C.78), (C.80), and (C.81) indicate that no reflected wave is produced and that the transmitted wave has, as expected, the same amplitude and polarity as the incident wave. In other words, all of the elastic energy of the wave crosses the boundary unchanged and travels away, never to return. Another way of looking at a boundary with an impedance ratio of unity is as a boundary between two identical, semi-infinite rods. A harmonic wave traveling in the positive $x$-direction (Figure C.15a) would impose an axial force [see Equation (C.5)] on the boundary:

$$F = \sigma A_x = \rho v_m \dot{u} A_x \tag{C.82}$$

This axial force is identical to that which would exist if the semi-infinite rod on the right side of the boundary were replaced by a dashpot (Figure C.15b) of coefficient $c = \rho v_m A_x$. In other words, the dashpot would absorb all the elastic energy of the incident wave, so the response of the rod on the left would be identical for both cases illustrated in Figure C.15. This result has important implications for ground response and soil-structure interaction analyses (Chapters 7 and 8), where the replacement of a semi-infinite domain by discrete elements such as dashpots can provide tremendous computational efficiencies.

**Figure C.15** (a) Harmonic wave traveling along two connected semi-infinite rods; (b) semi-infinite rod attached to dashpot. With proper selection of dashpot coefficient, response in semi-infinite rod on left will be identical for both cases.

### C.4.2 Three-Dimensional Case: Inclined Waves

In general, waves will not approach interfaces at 90° angles as they did in Section C.4.1. The orientation of an inclined body wave can strongly influence the manner in which energy is reflected and transmitted across an interface. Fermat's principle defines the propagation time of a seismic pulse between two arbitrary points A and B as the minimum travel time along any continuous path that connects A and B. The path that produces the minimum travel time is called a ray path, and its direction is often represented by a vector called a ray. A wavefront is defined as a surface of equal travel time; consequently, a ray path must (in an isotropic material) be perpendicular to the wavefront as illustrated in Figure C.16. Snell considered the change of direction of ray paths at interfaces between materials with different wave propagation velocities. Using Fermat's principle, Snell showed that

$$\frac{\sin i}{v} = \text{constant} \tag{C.83}$$

where $i$ is the angle between the ray path and the normal to the interface and $v$ is the velocity of the wave (p-wave or s-wave) of interest. This relationship holds for both reflected and transmitted waves. It indicates that the transmitted wave will be refracted (except when $i = 0$) when the wave propagation velocities are different on each side of the interface. Consider the case of two half-spaces of different elastic materials in contact with each other. As for the previous case, the requirements of equilibrium and compatibility and the theory of elasticity can be used to determine the nature and distribution of energy among the reflected and transmitted waves for the cases of an incident p-wave, an incident SV-wave, and an incident SH-wave. The types of waves produced by incident p-, SV-, and SH-waves are shown in Figure C.17. Since incident p- and SV-waves involve particle motion perpendicular to the plane of the interface, they will each produce both reflected and refracted p- and SV-waves. An incident SH-wave does not involve particle motion perpendicular to the interface; consequently, only SH-waves are reflected and refracted.

**Figure C.16** Ray path, ray, and wavefront for (a) plane wave and (b) curved wavefront.

**Figure C.17** Reflected and refracted rays resulting from incident (a) p-wave, (b) SV-wave, and (c) SH-wave.

The directions and relative amplitudes of the waves produced at the interface depend on both the direction and amplitude of the incident wave. Using Snell's law and the requirements of equilibrium and compatibility, these directions and amplitudes can be determined. Using the notation of Richter (1958) [@Richter1958]:

Wave Type — Velocity — Amplitude — Angle with Normal

- Incident p: velocity $U$, amplitude $A$, angle $a$
- Incident s: velocity $V$, amplitude $B$, angle $b$
- Reflected p: velocity $U$, amplitude $C$, angle $c$
- Reflected s: velocity $V$, amplitude $D$, angle $d$
- Refracted p: velocity $Y$, amplitude $E$, angle $e$
- Refracted s: velocity $Z$, amplitude $F$, angle $f$

The directions of all waves are easily related to the direction of the incident wave using Snell's law:

$$\frac{\sin a}{U} = \frac{\sin b}{V} = \frac{\sin c}{U} = \frac{\sin d}{V} = \frac{\sin e}{Y} = \frac{\sin f}{Z} \tag{C.84}$$

Since incident and reflected waves travel through the same material, $a = c$ and $b = d$, which shows that the angle of incidence is equal to the angle of reflection for both p- and s-waves. The angle of refraction is uniquely related to the angle of incidence by the ratio of the wave velocities of the materials on each side of the interface. Snell's law indicates that waves traveling from higher-velocity materials into lower-velocity materials will be refracted closer to the normal to the interfaces. In other words, waves propagating upward through horizontal layers of successively lower velocity (as is common near the Earth's surface) will be refracted closer and closer to a vertical path (Figure C.18). This phenomenon is relied upon heavily by many of the methods of ground response analysis presented in Chapter 7. The critical angle of incidence, $i_c$, is defined as that which produces a refracted wave that travels parallel to the interface ($e$ or $f = 90°$). Therefore,

$$\sin i_c = \frac{U}{Y} \quad \text{or} \quad \sin i_c = \frac{V}{Z} \tag{C.85}$$

The concept of critical refraction is used in the interpretation of seismic refraction tests (Section 6.5.2.1). Assuming that the incident wave is simple harmonic, satisfaction of the requirements of equilibrium and compatibility at the interface give rise to the following systems of simultaneous equations [@Richter1958], which allow the amplitudes of the reflected and refracted waves ($C$, $D$, $E$, and $F$) to be expressed in terms of the amplitude of the incident p-wave ($A$).

**Figure C.18** Refraction of an SH-wave ray path through a series of successively softer (lower $v_s$) layers. Note that orientation of ray path becomes closer to vertical as the ground surface is approached. Reflected rays are not shown.

$$(-A + C)\sin a + (-D)\sin b + E\sin e + (-F)\sin f = 0$$

$$(A + C)\cos a + D\cos b + E\cos e + (-F)\cos f = 0$$

$$\frac{U}{V}(-A + C)\sin 2a - D\cos 2b + \frac{EKZ}{VY}\sin 2e + \frac{FKZ}{V}\cos 2f = 0$$

$$\frac{U}{V}(-A + C)\cos 2b - D\sin 2b - \frac{EKY}{VU}\cos 2e + \frac{FKZ}{VU}\sin 2f = 0 \tag{C.86}$$

where $K = \rho_1/\rho_2$ (the subscripts 1 and 2 refer to materials 1 and 2, respectively). Note that the amplitudes are functions of the angle of incidence, the velocity ratio, and the density ratio. Figure C.19 shows the variation of amplitude with angle of p-wave incidence for the following conditions: $U = 8.000$, $Y = 2.003$, $K = 0.606$, and $\nu = 0.25$. The sensitivity of the reflected and refracted wave amplitudes to the angle of incidence is apparent. SV-waves are neither reflected nor refracted at angles of incidence of 0° and 90°, but can carry the majority of the wave energy away from the interface at intermediate angles. For an incident SV-wave, both SV- and p-waves are reflected and refracted. The equilibrium/compatibility equations relating the relative amplitudes are

$$(B + D)\sin b + (-C)\sin a + E\sin e + (-F)\sin f = 0$$

$$(-B + D)\cos b + C\cos a + E\cos e + (-F)\cos f = 0$$

$$\frac{V}{U}(B + D)\cos 2b + C\sin 2a + \frac{EKZ}{UY}\sin 2e + \frac{FKZ}{U}\cos 2f = 0$$

$$\frac{V}{U}(-B + D)\sin 2b - C\cos 2a - \frac{EKY}{UV}\cos 2e + \frac{FKZ}{UV}\sin 2f = 0 \tag{C.87}$$

**Figure C.19** Ratio of amplitudes of (a) reflected p-wave, (b) reflected SV-wave, (c) refracted p-wave, and (d) refracted SV-wave to amplitude of incident p-wave versus angle of incidence.

which produce the amplitude behavior shown in Figure C.20. For angles of incidence greater than $\sin^{-1}(V/U)$, about 36° in Figure C.20a, no p-wave can be reflected, so the incident wave energy must be carried away by the remaining waves. A more detailed discussion of this phenomenon can be found in McCamy et al. (1962) [@McCamyEtAl1962]. An incident SH-wave involves no particle motion perpendicular to the interface; consequently, it cannot produce p-waves ($C = E = 0$) or SV-waves. The equilibrium/compatibility equations are considerably simplified and easily solved as

$$D = B\frac{\cos f / KZ - \cos b / V}{\cos f / KZ + \cos b / V} \tag{C.88a}$$

$$F = B\frac{2\cos b / V}{\cos f / KZ + \cos b / V} \tag{C.88b}$$

The preceding results show that the interaction of stress waves with boundaries can be quite complicated. As seismic waves travel away from the source of an earthquake, they invariably encounter heterogeneities and discontinuities in the Earth's crust. The creation of new waves and the reflection and refraction of ray paths by these heterogeneities cause seismic waves to reach a site by many different paths. Since the paths have different lengths, the motion at the site is spread out in time by this wave-scattering effect. Scattering effects are discussed in more detail in Section C.5.3.

**Figure C.20** Ratio of amplitudes of (a) reflected p-wave, (b) reflected SV-wave, (c) refracted p-wave, and (d) refracted SV-wave to amplitude of incident SV-wave versus angle of incidence.

## C.5 ATTENUATION OF STRESS WAVES

The preceding sections have considered only the propagation of waves in linear elastic materials. In a homogeneous linear elastic material, stress waves travel indefinitely without change in amplitude. This type of behavior cannot occur, however, in real materials. The amplitudes of stress waves in real materials, such as those that comprise the Earth, attenuate with distance. This attenuation can be attributed to two sources, one of which involves the materials through which the waves travel and the other the geometry of the wave propagation problem.

### C.5.1 Material Damping

In real materials, part of the elastic energy of a traveling wave is converted to heat. The conversion is accompanied by a decrease in the amplitude of the wave. Viscous damping, by virtue of its mathematical convenience, is often used to represent this dissipation of elastic energy. For the purposes of viscoelastic wave propagation, soils are usually modeled as Kelvin-Voigt solids (i.e., materials whose resistance to shearing deformation is the sum of an elastic part and a viscous part). A thin element of a Kelvin-Voigt solid can be illustrated as in Figure C.21.

**Figure C.21** Thin element of a Kelvin-Voigt solid subjected to horizontal shearing. Total resistance to shearing deformation is given by the sum of an elastic (spring) component and a viscous (dashpot) component.

The stress-strain relationship for a Kelvin-Voigt solid in shear can be expressed as

$$\tau = G\gamma + \eta \frac{\partial\gamma}{\partial t} \tag{C.89}$$

where $\tau = \sigma_{xz}$ is the shear stress, $\gamma = \partial u / \partial x$ is the shear strain, and $\eta$ is the viscosity of the material. Thus the shear stress is the sum of an elastic part (proportional to strain) and a viscous part (proportional to strain rate). For a harmonic shear strain of the form

$$\gamma = \gamma_0 \sin\omega t \tag{C.90}$$

the shear stress will be

$$\tau = G\gamma_0 \sin\omega t + \omega\eta\gamma_0 \cos\omega t \tag{C.91}$$

Together, Equations (C.90) and (C.91) show that the stress-strain loop of a Kelvin-Voigt solid is elliptical. The elastic energy dissipated in a single cycle is given by the area of the ellipse, or

$$\Delta W = \int_t^{t + 2\pi/\omega} \tau \frac{\partial\gamma}{\partial t}\, dt = \pi\omega\eta\gamma_0^2 \tag{C.92}$$

which indicates that the dissipated energy is proportional to the frequency of loading. Real soils, however, dissipate elastic energy hysteretically, by the slippage of grains with respect to each other. As a result, their energy dissipation characteristics are insensitive to frequency. For discrete Kelvin-Voigt systems (Section B.6.1), the damping ratio $\xi$ was shown to be related to the area within the force-displacement (or, equivalently, the stress-strain) loop as shown in Figure C.22. Since the peak energy stored in the cycle is

**Figure C.22** Relationship between hysteresis loop and damping ratio.

$$W = \frac{1}{2}G\gamma_0^2 \tag{C.93}$$

Then

$$\xi = \frac{\pi\omega\eta\gamma_0^2}{\pi G\gamma_0^2} = \frac{\omega\eta}{G} \tag{C.94}$$

To eliminate frequency dependence while maintaining the convenience of the viscoelastic formulation, Equation (C.94) is often rearranged to produce an equivalent viscosity that is inversely proportional to frequency. The use of this equivalent viscosity ensures that the damping ratio is independent of frequency:

$$\eta = \frac{2\xi G}{\omega} \tag{C.95}$$

A Kelvin-Voigt solid for vertically propagating SH-waves may be represented by a stack of infinitesimal elements of the type shown schematically in Figure C.21. The one-dimensional equation of motion for vertically propagating SH-waves can be written as

$$\rho \frac{\partial^2 u}{\partial t^2} = \frac{\partial \sigma_{xz}}{\partial z} \tag{C.96}$$

Substituting Equation (C.89) into (C.96) with $\tau = \sigma_{xz}$ and $\gamma = \partial u / \partial z$, and differentiating the right side allows the wave equation to be expressed as

$$\rho \frac{\partial^2 u}{\partial t^2} = G \frac{\partial^2 u}{\partial z^2} + \eta \frac{\partial^3 u}{\partial z^2 \partial t} \tag{C.97}$$

For harmonic waves, the displacements can be written as

$$u(z,t) = U(z)\, e^{i\omega t} \tag{C.98}$$

where $U(z)$ is the depth-varying amplitude of a standing wave of frequency $\omega$. Substituting this expression into the wave equation (C.97) yields the ordinary differential equation

$$G\frac{d^2 U}{dz^2} + i\omega\eta\frac{d^2 U}{dz^2} = -\rho\omega^2 U \tag{C.99}$$

$$G^* \frac{d^2 U}{dz^2} = -\rho\omega^2 U \tag{C.100}$$

where $G^* = G + i\omega\eta$ is the complex shear modulus. The complex shear modulus is analogous to the complex stiffness described in Section B.6.3. Using Equation (C.95) to eliminate frequency dependence, the complex shear modulus can also be expressed as $G^* = G(1 + 2i\xi)$. This equation of motion has the solution

$$u(z,t) = A e^{i(\omega t - k^* z)} + B e^{i(\omega t + k^* z)} \tag{C.101}$$

where $A$ and $B$ depend on the boundary conditions, $k^* = \omega\sqrt{\rho/G^*}$ is the complex wave number, and time dependence has been added by multiplying the displacement terms by $e^{i\omega t}$. It can be shown (after Kolsky, 1963 [@Kolsky1963]) that $k^*$ is given by

$$k^* = k + i\kappa \tag{C.102}$$

where

$$k = \frac{\omega}{v_s}\sqrt{\frac{1}{2}\left(\sqrt{1+4\xi^2}+1\right)\frac{1}{1+4\xi^2}}$$

$$\kappa = \frac{\omega}{v_s}\sqrt{\frac{1}{2}\left(\sqrt{1+4\xi^2}-1\right)\frac{1}{1+4\xi^2}}$$
