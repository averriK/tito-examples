and only the positive root of $k_1$ and the negative root of $k_2$ have physical significance. Note that for the inviscid case ($\eta = 0$), $k_2 = 0$ and $k_1 = k$. For a wave propagating in the positive $z$-direction, the solution can be written as

$$u(z,t) = Ae^{-k_2 z}\,e^{i(\omega t - k_1 z)} \tag{C.103}$$

which shows (since $k_2$ is negative) that material damping produces exponential attenuation of wave amplitude with distance. Although the Kelvin-Voigt model is by far the most commonly used model for soils, it represents only one of an infinite number of rheological models. By rearranging and adding more springs and dashpots, many different types of behavior can be modeled, although the complexity of the wave equation solution increases dramatically as the number of springs and dashpots increases.

### C.5.2 Radiation Damping

Since material damping absorbs some of the elastic energy of a stress wave, the specific energy (elastic energy per unit volume) decreases as the wave travels through a material. The reduction of specific energy causes the amplitude of the stress wave to decrease with distance. The specific energy can also be decreased by another common mechanism, which can be illustrated by the propagation of stress waves along an undamped conical rod. Consider the unconstrained conical rod of small apex angle shown in Figure C.23 and assume that it is subjected to stress waves of wavelength considerably larger than the diameter of the rod in the area of interest. If the apex angle is sufficiently small, the normal stress will be uniform across each of two spherical surfaces that bound an element of width, $dr$, and will act in a direction virtually parallel to the axis of the rod. Letting $u$ represent the displacement parallel to the axis of the rod, the equation of motion in that direction can be written, using exactly the same approach used in Section C.2.1.1, as

$$\frac{\partial^2 u}{\partial t^2}\rho + \frac{\partial \sigma}{\partial r}\,\alpha = \sigma + \alpha - \sigma \tag{C.104}$$

$$r\,dr \quad r\,dr \quad r\,dr \quad r \quad \frac{\partial}{\partial t}$$

FIGURE C.23 Conical rod of apex angle, $\alpha$.

which simplifies to

$$\rho\,\frac{\partial^2 u}{\partial t^2} = \frac{\partial \sigma}{\partial r} + \frac{\sigma}{r} \tag{C.105}$$

Substituting the stress-strain and strain-displacement relationships (assuming now that the ends of the element are planar) gives

$$\rho\,\frac{\partial^2 u}{\partial t^2} = E\,\frac{\partial^2 u}{\partial r^2} + \frac{E}{r}\,\frac{\partial u}{\partial r} \tag{C.106}$$

$$\rho\,\frac{\partial^2(ur)}{\partial t^2} = E\,\frac{\partial^2(ur)}{\partial r^2} \tag{C.107}$$

$$u(r,t) = \frac{1}{r}\bigl[f(vt - r) + g(vt + r)\bigr] \tag{C.108}$$

where $v = \sqrt{E/\rho}$. Equation (C.108) indicates that the amplitude of the wave will decrease with distance (even though the total elastic energy remains the same). The reduction is of purely geometric origin, resulting from the decrease in specific energy that occurs as the area of the rod increases. Even though elastic energy is conserved (no conversion to other forms of energy takes place), this reduction in amplitude due to spreading of the energy over a greater volume of material is often referred to as radiation damping (also as geometric damping and geometric attenuation). It should be distinguished from material damping in which elastic energy is actually dissipated by viscous, hysteretic, or other mechanisms. When earthquake energy is released from a fault below the ground surface, body waves travel away from the source in all directions. If the rupture zone can be represented as a point source, the wavefronts will be spherical and the preceding analysis can easily be extended to show that geometric attenuation causes the amplitude to decrease at a rate of $1/r$. It can also be shown [@Bullen1953] that geometric attenuation of surface waves causes their amplitudes to decrease at a rate of essentially $1/\sqrt{r}$; in other words, surface waves attenuate (geometrically) much more slowly than body waves. This explains the greater proportion of surface wave motion (relative to body wave motion) that is commonly observed at large epicentral distances. This partly explains the advantages of the surface wave magnitude, relative to body wave magnitude, for the characterization of distant earthquakes (although moment magnitude remains the preferred scale, when available). For problems in which energy is released from a finite source, ranging from the large-scale case of rupture along an earthquake fault to the smaller-scale case of a vibrating foundation, radiation damping can be extremely important. In such cases, the effects of radiation damping are often larger than those of material damping.

### C.5.3 Scattering

Another mechanism, wave scattering, can lead to a reduction in the amplitude of a traveling wave without dissipation of elastic wave energy. Seismic wave scattering results from heterogeneities of density and/or stiffness in the geologic materials that waves travel through. Scattering in the Earth's crust contributes to path effects and scattering in near-surface materials contributes to site effects. While not affecting the total amount of energy it carries, scattering tends to disorganize a wave field by reflection and refraction at the boundaries of heterogeneities. The waves are spread out over a greater duration with their amplitudes, particularly at higher frequencies, being reduced. The factors that lead to this behavior are illustrated below using the concepts of Section C.4 to consider simple, individual inclusions in otherwise homogeneous materials; in reality, the three-dimensional spatial variability of soil and rock can be interpreted as multiple, geometrically-complex inclusions of stiffer and softer materials, which have much more complicated effects on wave propagation. Consider a wave traveling along a constrained infinite elastic rod (Material 1) that contains an inclusion of length, $L$, whose properties (Material 2) are different than those of the rest of the rod. If an incident wave of displacement amplitude, $A$, travels from left to right (Figure C.24) along the rod, part of its energy will be reflected back to the left with amplitude, $A_r$, and part will be transmitted into the inclusion with amplitude, $B$, when it reaches the left side of the inclusion ($x = 0$). However, when the transmitted wave reaches the right side of the inclusion ($x = L$), part of its energy will be reflected back with amplitude, $B_r$, and part will be transmitted with amplitude, $C$, into Material 1 on the right side of the inclusion. The effect of the inclusion can be seen by comparing the amplitude of the transmitted wave, $C$, with that of the incident wave, $A$. To make this comparison, the boundary conditions on the left and right sides of the inclusion must be considered. The various displacements of interest are described by

$$u_i(x,t) = Ae^{i(\omega t - k_1 x)}, \quad u_i(x,t) = Be^{i(\omega t - k_2 x)}, \quad u_i(x,t) = Ce^{i(\omega t - k_1 x)} \tag{C.109}$$

$$u_r(x,t) = A_r e^{i(\omega t + k_1 x)}, \quad u_r(x,t) = B_r e^{i(\omega t + k_2 x)}$$

where $k_1$ and $k_2$ are the wave numbers in Materials 1 and 2, respectively. Using Equation (C.68), the corresponding stresses are given by

$$\sigma_i(x,t) = -ik_1 M_1 Ae^{i(\omega t - k_1 x)}, \quad \sigma_i(x,t) = -ik_2 M_2 Be^{i(\omega t - k_2 x)}, \quad \sigma_i(x,t) = -k_1 M_1 Ce^{i(\omega t - k_1 x)} \tag{C.110}$$

$$\sigma_r(x,t) = ik_1 M_1 A_r e^{i(\omega t + k_1 x)}, \quad \sigma_r(x,t) = k_2 M_2 B_r e^{i(\omega t + k_2 x)}$$

where $M_1$ and $M_2$ are the respective constrained moduli of Materials 1 and 2. Continuity of displacements at the left side of the inclusion requires that $u_i(x,t) + u_r(x,t) = u_i(x,t) + u_r(x,t)$, which, since $x = 0$ at that boundary, gives

$$A + A_r = B + B_r \tag{C.111}$$

At the right side of the inclusion, $u_i(x,t) + u_r(x,t) = u_i(x,t)$, so, since $x = L$ at that boundary,

$$Be^{-ik_2 L} + B_r e^{ik_2 L} = Ce^{-ik_1 L} \tag{C.112}$$

For equilibrium at the left side of the inclusion, $\sigma_i(x,t) + \sigma_r(x,t) = \sigma_i(x,t) + \sigma_r(x,t)$. Since $x = 0$,

$$-k_1 M_1 A + k_1 M_1 A_r = -k_2 M_2 B + k_2 M_2 B_r \tag{C.113}$$

FIGURE C.24 Illustration of inclusion of length, $L$, in infinitely long rod indicating displacement amplitudes of left- and right-traveling waves.

Finally, equilibrium at the right side of the inclusion requires that $\sigma_i(x,t) + \sigma_r(x,t) = \sigma_i(x,t)$, or

$$-k_2 M_2 Be^{-ik_2 L} + k_2 M_2 B_r e^{ik_2 L} = -k_1 M_1 Ce^{-ik_1 L} \tag{C.114}$$

Equations (C.111)–(C.114) are required to satisfy the boundary conditions at both ends of the inclusion. Dividing all four equations by the incident wave amplitude, $A$, and the last two by $k_1 M_1$, and using the impedance ratio $\alpha_z = k_2 M_2 / k_1 M_1 = \rho_2 v_2 / \rho_1 v_1$, gives a set of four simultaneous equations

$$\frac{A_r}{A} - \frac{B}{A} - \frac{B_r}{A} = -1 \tag{C.115a}$$

$$\frac{B}{A}e^{-ik_2 L} - \frac{B_r}{A}e^{ik_2 L} + \frac{C}{A}e^{-ik_1 L} = 0 \tag{C.115b}$$

$$\frac{A_r}{A} + \alpha_z\frac{B}{A} - \alpha_z\frac{B_r}{A} = 1 \tag{C.115c}$$

$$-\alpha_z\frac{B}{A}e^{-ik_2 L} + \alpha_z\frac{B_r}{A}e^{ik_2 L} + \frac{C}{A}e^{-ik_1 L} = 0 \tag{C.115d}$$

These equations involve four unknowns — $A_r/A$, $B/A$, $B_r/A$, and $C/A$. The amplitude of the wave that continues past the inclusion is of greatest interest and that amplitude, relative to that of the original incident wave, can be obtained from the solution of the equations [@SemblatPecker2009] as

$$\frac{C}{A} = \frac{1}{\cos(2\pi L/\lambda) + \frac{i}{2}\!\left(\alpha_z + \frac{1}{\alpha_z}\right)\sin(2\pi L/\lambda)} \tag{C.116}$$

The displacement amplitude ratio can be seen to depend on the impedance ratio of the inclusion and the length of the inclusion relative to the wavelength of the motion. If the impedance ratio is 1.0, the amplitude ratio will be 1.0 (regardless of inclusion length or frequency) since waves would not be reflected at either end of the inclusion. Similarly, as the inclusion length and/or frequency go to zero, the impedance ratio goes to 1.0. If the impedance ratio is not equal to 1.0 (either smaller or larger), the amplitude ratio will be less than 1.0 (Figure C.25a). As the frequency increases, the wavelength shortens and the amplitude ratio decreases. Thus, the effect of the inclusion is to reduce the amplitude of the transmitted wave. The effect, however, is locally symmetric about $L/\lambda = 0.25 + 0.50n$ (where $n$ is a non-negative integer) and periodic at $L/\lambda = 0.5$ (Figure C.25b). For a given impedance ratio, the transmitted wave amplitude decreases with increasing $L/\lambda$ ratio, i.e. increasing frequency for a given inclusion size or increasing inclusion size for a given frequency. Thus, earthquake motions will see their higher frequency (shorter wavelength) components more strongly affected by inclusions than their lower frequency (longer wavelength) components. If the wavelength of a wave is much longer than the dimension of an inclusion it encounters, the inclusion will simply translate almost as a rigid body as the wave passes through it. When waves encounter inclusions with dimensions similar to their wavelengths, the inclusions will respond dynamically, and the waves transmitted through them will be altered. The situation becomes even more complicated when waves strike inclusions at angles other than 90°. Figure C.26 illustrates the refraction, reflection, and transmission of SH- and p-waves that strike an inclusion obliquely. In the case of an incident SH-wave, which has no component of particle motion perpendicular to the boundaries, the transmitted wave is offset by refraction within the inclusion and propagates beyond the inclusion at a different orientation than the original incident wave. In the case of an incident p-wave, both p- and SV-waves are created at the inclusion boundaries, and all components travel in somewhat different directions. In the Earth's crust, naturally occurring heterogeneities act as inclusions, but without the simple, parallel-surface geometries shown in Figures C.25 and C.26. They therefore tend to scatter waves in very different directions so that the energy that reaches a particular site has traveled over a distribution of path lengths, thereby decreasing the amplitude and increasing the significant duration of the motion. Scattering can cause even a simple, planar wave field to become quite complex, and can lead to substantial changes in the motions beyond the inclusion (Figure C.27). As in the one-dimensional case illustrated previously, the effects of the inclusion will depend on the ratio of its dimensions to the wavelengths of the incoming waves, with the result that high frequency (short wavelength) components will be scattered to a greater extent than low frequency (long wavelength) components. The reduction in wave amplitudes due to scattering, therefore, is greater at high frequency than low frequency. The high-frequency reduction in the Fourier amplitude spectra of recorded ground motions (Sections 3.4.2.2 and 3.6.1) is partially caused by this type of scattering phenomenon; the effects are similar to the effects that frequency-dependent damping would have.

FIGURE C.25 Illustration of effects of inclusion on wave transmission: (a) as function of impedance ratio for $L/\lambda < 0.25$, and (b) as function of wavelength ratio for impedance ratios of 1.0–5.0.

FIGURE C.26 Influence of inclusion on obliquely-incident waves: (a) incident SH-wave, and (b) incident p-wave.

FIGURE C.27 Scattering of wavefield due to heterogeneity: (a) incident plane wave with no heterogeneity, (b) location of heterogeneity, (c) wavefield produced by oscillation of heterogeneity, and (d) total response [sum of (a) and (c)] showing alteration of plane wave by presence of heterogeneity [@PageotEtAl2013].

### C.6 IMPLICATIONS FOR SITE RESPONSE

As discussed in Chapters 3 and 7, an important problem in geotechnical earthquake engineering is the evaluation of site response, i.e., the effect of local soil conditions on the nature of earthquake ground motions. The basic principles of wave propagation described in the earlier sections of this appendix can be used to gain insight into many aspects of the response of soil sites to the motions of the bedrock that underlies them. The following sections provide an introduction to the most important of these — they will help the reader understand the basis for site response models in ground motion models (GMMs) discussed in Section 3.5.2.3, and serve as an introduction to the more detailed concepts of site response analysis covered in Sections 7.4–7.7.

### C.6.1 Ground Motion Amplification

The shallow geology at a particular site can have a strong effect on earthquake ground motions. Soil deposits overlying bedrock can amplify or de-amplify ground motion amplitudes and can do both at different frequencies. Upward-traveling seismic waves generally encounter progressively softer materials as they approach the ground surface, so they are refracted toward more and more vertical travel paths (Figure C.18). At shallow depths, seismic ground motions are often idealized as vertically propagating SH-waves, in which case all particle motion is horizontal. The primary mechanisms of ground motion amplification in such cases are associated with impedance gradients and resonance.

### C.6.1.1 Amplification due to Decreasing Impedance

The general trend of increasing density and stiffness with depth means that specific impedance will also generally increase with depth. Based on the continuity of stresses and displacements at a layer boundary, Equation (C.78) showed that the displacement amplitude at a particular frequency will increase as a wave passes from a material of higher impedance to a material of lower impedance. If the displacement amplitude increases, the velocity and acceleration amplitudes will also increase. Thus, the fact that upward-traveling waves typically pass through successively softer materials as they approach the ground surface leads to a form of ground motion amplification manifested as a general increase in ground motion amplitude at shallower depths. The same result can be obtained from energy considerations. Energy flux is defined as the amount of energy per unit time that flows through a given cross-section of material and can be defined as

$$E_f = \rho\,v\left(\frac{\partial u}{\partial t}\right)^2 \tag{C.117}$$

where $\rho$ is the density, $\partial u/\partial t$ is the particle velocity, and $v$ is the wave propagation velocity of the medium. Note that $\rho v$ is the specific impedance of the material. Since energy must be conserved at a boundary between two linear, elastic materials, the energy flux on both sides of a boundary between layers must be equal. Thus, when waves travel from a higher impedance (generally, stiffer) material into a lower impedance (softer) material, deformation (displacement, velocity, and acceleration) amplitudes must increase in order for the energy flux to be equal on both sides of the boundary.

### C.6.1.2 Amplification due to Resonance

The type of amplification discussed in the preceding section can occur in profiles with discrete layers or in profiles with continuously varying stiffness. Profiles with discrete layers of substantial thickness can also display a tendency to strongly amplify motions at certain frequencies that are associated with the thicknesses and stiffnesses of the layers. The simplest case of this type would be a uniform soil layer overlying bedrock. Consider a layer of uniform elastic material (a simplistic idealization of "soil") underlain by a rigid base (a simplistic idealization of "rock"). If the rigid base moves horizontally, vertically propagating shear waves (SH-waves) will travel up through the soil, be reflected back downward at the ground surface (a free-end), and then be reflected back upward again by the rigid base (a fixed-end). The upward- and downward-traveling waves will interfere with each other, sometimes constructively and sometimes destructively, to produce the site response. The one-dimensional wave equation, along with the free- and fixed-end boundary conditions developed earlier in this appendix, allows the response of the soil layer to be computed for both undamped and damped soil conditions.

**Undamped Soil** Consider a uniform layer of isotropic, linear elastic soil overlying rigid bedrock as shown in Figure C.28. Harmonic horizontal motion of the bedrock will produce vertically propagating shear waves in the overlying soil. The resulting horizontal displacement can be expressed, using the results of Section C.2.1.3 (Equation C.15), as

$$u(z,t) = Ae^{i(\omega t + kz)} + Be^{i(\omega t - kz)} \tag{C.118}$$

FIGURE C.28 Linear elastic soil deposit of thickness, $H$, underlain by rigid bedrock.

where $\omega$ is the circular frequency of bedrock shaking, $k$ the wave number ($= \omega/v_s$) and $A$ and $B$ the displacement amplitudes of waves traveling in the $-z$ (upward) and $+z$ (downward) directions, respectively. At the free surface ($z = 0$), the shear stress, and consequently the shear strain, must vanish; i.e.,

$$\tau(0,t) = G\,\frac{\partial u}{\partial z}(0,t) = 0 \tag{C.119}$$

Substituting (C.118) into (C.119) and differentiating yields

$$Gik\bigl(Ae^{i\omega t} - Be^{i\omega t}\bigr) = Gik(A - B)e^{i\omega t} = 0 \tag{C.120}$$

which is satisfied (nontrivially) when $A = B$. The displacement can then be expressed as

$$u(z,t) = A\bigl(e^{-ikz} + e^{ikz}\bigr)e^{i\omega t} = 2A\cos(kz)\,e^{i\omega t} \tag{C.121}$$

which describes a standing wave of amplitude $2A\cos(kz)$. Note that the amplitude of the wave is twice the amplitude of the upward-traveling wave, a characteristic known as the free surface effect. The standing wave is produced by the constructive interference of the upward and downward-traveling waves and has a fixed shape with respect to depth. Equation (C.121) can be used to define a transfer function that describes the ratio of displacement amplitudes at any two points in the soil layer. Choosing these two points to be the top and bottom of the soil layer gives the transfer function

$$F_1(\omega) = \frac{u(0,t)}{u(H,t)} = \frac{Ae^{i\omega t}}{A\cos(kH)\,e^{i\omega t}} = \frac{1}{\cos(kH)} = \frac{1}{\cos(\omega H/v_s)} \tag{C.122}$$

The modulus of the transfer function is the amplification function

$$|F_1(\omega)| = \sqrt{[\operatorname{Re}(F_1(\omega))]^2 + [\operatorname{Im}(F_1(\omega))]^2} = \frac{1}{\cos(\omega H/v_s)} \tag{C.123}$$

which indicates that the surface displacement is always at least as large as the bedrock displacement (since the denominator can never be greater than 1.0 and, at certain frequencies, is much larger). Thus $F_1(\omega)$ is the ratio of the free surface motion amplitude to the bedrock motion amplitude (or, since the bedrock is rigid in this case, the bedrock outcropping motion). As $\omega H/v_s$ approaches $\pi/2 + n\pi$, the denominator of Equation (C.122) approaches zero, which implies that infinite amplification, or resonance, will occur (Figure C.29). Even this very simple model illustrates that the response of a soil deposit is highly dependent upon the frequency of the base motion, and that the frequencies at which strong amplification occurs depend on the geometry (thickness) and material properties (s-wave velocity) of the soil layer.

**Damped Soil** Obviously, the type of unbounded amplification predicted by the previous analysis cannot physically occur. The previous analysis assumed no dissipation of energy, or damping, in the soil. Since damping is present in all materials, more realistic results can be obtained by repeating the analysis with damping. Assuming the soil to have the shearing characteristics of a Kelvin-Voigt solid, the wave equation can be written [Equation (C.97)] as

FIGURE C.29 Influence of frequency on the steady-state response of undamped linear elastic layer.

$$\rho\,\frac{\partial^2 u}{\partial t^2} = G\,\frac{\partial^2 u}{\partial z^2} + \eta\,\frac{\partial^3 u}{\partial z^2\,\partial t} \tag{C.124}$$

The solution to this equation can also be expressed in terms of a transfer function whose modulus can be expressed (see derivation in Section 7.5.1.2) as

$$|F_1(\omega)| = \frac{1}{\sqrt{\cos^2(\omega H/v_s) + (\xi\,\omega H/v_s)^2}} \tag{C.125}$$

for small values of the damping ratio, $\xi$. This expression also indicates that amplification is frequency-dependent (Figure C.30) with local maxima (but not infinite in the case of an undamped material) at the natural frequencies of the layer. The $n$th natural frequency of the soil deposit is given by

$$\omega_n = \frac{(2n+1)\pi v_s}{2H}, \quad n = 0, 1, 2, \ldots \tag{C.126}$$

Since the peak amplification factor decreases with increasing natural frequency, the greatest amplification factor will occur approximately at the lowest natural frequency, i.e., the fundamental frequency, which can be expressed in radians/sec as

FIGURE C.30 Influence of frequency on the steady-state response of damped, linear elastic layer.

$$\omega_0 = \frac{\pi v_s}{2H} \tag{C.127}$$

or in Hz as

$$f_0 = \frac{v_s}{4H} \tag{C.128}$$

The fundamental period, or characteristic site period, then is

$$T_0 = \frac{4H}{v_s} \tag{C.129}$$

These concepts are used to help explain site effects terms in GMMs in Section 3.5.2.3 and are expanded upon in the development of more rigorous site response analysis procedures in Section 7.5.1.2.

### C.6.2 Basin Effects

The refraction of seismic waves also plays an important role in the response of sites located in basins. Basins are localized zones of alluvium and sedimentary rock that are underlain by stiffer basement rock and can have dimensions ranging from kilometers to tens of kilometers. Figure C.31 schematically depicts two sedimentary basins — the narrow Basin 1 overlies the fault and Basin 2 is at some horizontal distance from it. The waves entering from beneath Basin 1 are propagating nearly vertically as they reach the bottom of the basin but are focused toward the center of the narrow basin by refraction at its sloping base. If Basin 1 had been broad with a relatively flat base, waves would have propagated vertically through the basin sediments and site response within the basin would be largely associated with the ground response effects described previously. Wave propagation in that case may be reasonably well represented by a one-dimensional wave propagation analysis (Section 7.5). On the other hand, because the seismic source is located outside the perimeter of Basin 2, waves can enter that basin from beneath (as with Basin 1) but also from the edge. Waves that enter the basin from the edge can be refracted in such a way that downward-traveling reflections strike the bottom of the basin at an incidence angle greater than the critical angle and are completely reflected back into the basin (total internal reflection). The waves then become trapped within the basin and generate Love waves that propagate across the basin. Because basins are generally large (dimensions ranging from km to tens of km), they most strongly affect ground motions with long wavelengths, i.e., low-frequency ground motions.

FIGURE C.31 Schematic showing seismic body waves entering basins from beneath and from the edge. The waves entering through the edge of Basin 2 undergo critical body wave reflections, which generate surface waves that travel across the basin. (Modified from [@ChoiEtAl2005].)

For this reason, basin effects are typically only significant for periods greater than 1.0 sec. Because their specific effects are influenced by their three-dimensional geometries, simple engineering models that properly represent the physics of the problem do not presently exist. Instead, current models for basin-related amplification are a simple function of sediment depth, as discussed in Section 3.5.2.3. A more detailed description of basin effects is presented in Section 7.6.2.

### C.7 SUMMARY

1. Only body waves can travel through an unbounded, homogeneous, solid. There are two types of body waves: p- and s-waves. P-waves are irrotational, or dilatational, waves — they induce volumetric but not shearing deformations in the materials they travel through. The direction of particle movement caused by p-waves is parallel to the direction in which the wave is traveling. S-waves, also known as shear waves, involve shearing but not volumetric deformations. The passage of an s-wave causes particle movement perpendicular to the direction of wave travel.

2. Body waves travel at velocities that depend on the stiffness and density of the material they travel through. Because geologic materials are stiffer in volumetric compression than in shear, p-waves travel faster through them than do s-waves.

3. The interaction of inclined body waves with the stress-free surface of the Earth produces surface waves. The motions produced by surface waves are concentrated in a shallow zone near the surface.

4. Rayleigh waves are the most important type of surface wave for earthquake engineering applications. In a homogeneous elastic half-space, Rayleigh waves would travel slightly more slowly than s-waves and would produce both vertical and horizontal particle motions that follow a retrograde elliptical pattern.

5. The depth to which Rayleigh waves induce significant motion is inversely proportional to the frequency of the wave. Low-frequency Rayleigh waves can produce particle motion at large depths, but the motions produced by high-frequency Rayleigh waves are confined to shallow depths.

6. When body wave velocities increase with depth, as they generally do in the Earth's crust, Rayleigh wave velocities are frequency-dependent. Low-frequency Rayleigh waves, which induce motion in deeper, stiffer materials, travel faster than high-frequency Rayleigh waves. Waves with frequency-dependent velocities are said to be dispersive.

7. Love waves are surface waves that can develop in the presence of a soft surficial layer. Love waves are dispersive — their velocities vary with frequency between the shear wave velocity of the surficial layer (at high frequencies) and the shear wave velocity of the underlying material (at low frequencies).

8. When a body wave strikes a rigid boundary oriented perpendicular to its direction of travel, the wave is perfectly reflected as an identical wave traveling back in the opposite direction. The zero-displacement boundary condition requires that the stress at the boundary be twice that of the wave away from the boundary. When a body wave strikes a stress-free boundary oriented perpendicular to its direction of travel, the wave is reflected as an identical wave of opposite polarity traveling back in the same direction. The zero-stress boundary condition requires that the particle motion at the boundary be twice as large as the particle motion away from the boundary.

9. When a body wave strikes a normal boundary between two different materials, part of the wave energy is reflected and part is transmitted across the boundary. The behavior of the wave at the boundary is governed by the ratio of the specific impedances of the materials on either side of the boundary. This impedance ratio determines the amplitudes and polarities of the reflected and transmitted waves.

10. When body waves strike boundaries between different materials at angles other than 90°, part of the wave energy is reflected and part is refracted as it crosses the boundary. If the direction of particle motion is parallel to the boundary, the reflected and refracted waves will be of the same form as the incident wave. If not, new types of waves can be created; for example, an inclined p-wave that strikes a horizontal boundary will produce reflected p- and SV-waves and also refracted p- and SV-waves.

11. When an inclined wave travels upward through horizontal layers that become successively softer, the portion of the wave that crosses each layer boundary will be refracted closer and closer to a vertical direction.

12. The amplitude of a stress wave decreases as the wave travels through the Earth's crust. There are two primary mechanisms that cause this attenuation of wave amplitude. The first, material damping, is due to the absorption of energy by the materials the wave is traveling through. The second, radiation damping, results from the spreading of wave energy over a greater volume of material as it travels away from its source.

---

# Appendix D

# Probability Concepts

### D.1 INTRODUCTION

Earthquake engineering problems are fraught with uncertainty, and performance-based earthquake engineering seeks to characterize and account for that uncertainty. As a result, the practice of performance-based earthquake engineering requires some level of familiarity with basic concepts of uncertainty and basic procedures of probabilistic analysis. Geotechnical earthquake engineering is particularly affected by uncertainty. At a particular site, bedrock motions depend on the size, location, and rupture behavior of the earthquake — none of which can be predicted with certainty. Because of the inherent variability of soils and the inevitable limits on exploration of subsurface conditions, the resistance of the soil to that loading is not known with certainty. When both loading and resistance are uncertain, the resulting effects are also uncertain. A number of geotechnical earthquake engineering analyses attempt to quantify the uncertainty in the various input parameters for a particular problem and compute the resulting uncertainty in the output. This appendix provides a brief introduction to some of the basic concepts of probability and describes probability terms, distributions, and calculations that are used in the body of the book. It also discusses the propagation of uncertainty, i.e., how uncertainty in input parameters translates to uncertainty in output. More detailed information on these topics can be found in texts such as Benjamin and Cornell (2014), Baecher and Christian (2003), Ang and Tang (2007), and Fenton and Griffiths (2008).

### D.2 SAMPLE SPACES AND EVENTS

Probability theory deals with the results, or outcomes, of processes that are usually described in a general sense as experiments. The set of all possible outcomes of an experiment is called the sample space, and each outcome of an experiment is called a sample point. The sample space therefore consists of all possible sample points. The sample space may be continuous, in which case the number of sample points is infinite, or it may be discrete as when the number of sample points is finite and countable. An event is a subset of a sample space and therefore represents a set of sample points. A single event consists of a single sample point and a compound event consists of more than one sample point. If $\Omega$ represents a sample space and $A$ an event, the complementary event $\bar{A}$ is the set of all sample points in $\Omega$ that are not in $A$. The interrelationships among sets can be conveniently illustrated by means of a Venn diagram of the type illustrated in Figure D.1. In Figure D.1, the sample space is represented by the rectangle $\Omega$ and event $A$ by the circle. The complementary event $\bar{A}$ corresponds to the part of the rectangle that lies outside the circle. Two operations on events are of interest — the union of two events, $A$ and $B$, consists of all sample points that are in either $A$ or $B$ (or both), and the intersection is the set of sample points that are in both $A$ and $B$. Since no sample points are in both $A$ and $\bar{A}$, the intersection of $A$ and $\bar{A}$ is the null set $\emptyset$, i.e., $A \cap \bar{A} = \emptyset$. Similarly, the union of $A$ and $\bar{A}$ is $\Omega$, i.e., $A \cup \bar{A} = \Omega$. Two events, $A$ and $B$, are said to be mutually exclusive if they share no common sample points, i.e. $A \cap B = \emptyset$. A set of events, $B_1, B_2, \ldots, B_n$ are collectively exhaustive if their union makes up the entire sample space, i.e., $B_1 \cup B_2 \cup \cdots \cup B_n = \Omega$.

FIGURE D.1 Venn diagram illustrating event $A$ in sample space $\Omega$.

#### Example D.1

Consider the Venn diagram for the three events, $A$, $B$, and $C$, shown in Figure ED.1.

FIGURE ED.1 Venn diagram with three events considered in Example D.1.

- $A \cap B$ = regions 1 and 4
- $A \cap B$ = regions 3 and 7
- $B \cap (A \cup C)$ = regions 1, 2, 3, 4, 5, and 6
- $A \cup C$ = regions 1, 2, and 3
- $A \cap B \cap C$ = region 1
- $\bar{A} \cap \bar{B} \cap \bar{C}$ = region 8

### D.3 AXIOMS OF PROBABILITY

A probability measure, $P$, can be assigned to each sample point or set of sample points in a sample space. The probability of an event $A$ is then denoted by the symbol $P[A]$. The entire theory of probability is based on the following three fundamental axioms:

**Axiom 1.** The probability of an event is represented by a number greater than or equal to zero but less than or equal to one.

$$0 \leq P[A] \leq 1 \tag{D.1a}$$

**Axiom 2.** The probability of an event equal to the entire sample space $\Omega$ is one.

$$P[\Omega] = 1 \tag{D.1b}$$

**Axiom 3.** The probability of an event representing the union of two mutually exclusive events is equal to the sum of the probabilities of the events.

$$P[A \cup B] = P[A] + P[B] \tag{D.1c}$$

These axioms can be used to develop the rules and theorems that comprise the mathematical theory of probability.

### D.4 PROBABILITY OF EVENTS

Probabilities are often thought of in terms of relative frequencies of occurrence. If the existence of a water content greater than the optimum water content in a compacted fill is considered to be an event, the probability of that event can be estimated by determining the relative frequency of water content measurements that exceed the optimum water content. If the total number of water content measurements is small, the relative frequency may only approximate the actual probability, but as the number of measurements becomes large, the relative frequency will approach the actual probability. This frequentist point of view is not very helpful, however, for situations in which an experiment cannot be repeated. In such cases, probabilities can be viewed as relative likelihoods, as in the probability that the material at a certain depth in a boring is clay rather than sand or rock. The latter interpretation lends itself to the subjective evaluation of probability.

### D.4.1 Probabilities of Unions and Intersections

Regardless of how probabilities are interpreted, the axioms of probability allow statements to be made about the probabilities of occurrence of single or multiple events. These can be visualized with the use of Venn diagrams drawn such that the area of the rectangle representing the sample space $\Omega$ is 1 and the areas of all events within the sample space are equal to their probabilities. Consider the non-exclusive events $A$ and $B$ in Figure D.2. The event $A \cap B$ is represented by the shaded region and $P[A \cap B]$ is given by the area of the shaded region in Figure D.2a. The event $A \cup B$ is represented by the shaded region in Figure D.2b; $P[A \cup B]$ is given by the area of that shaded region, or

$$P[A \cup B] = P[A] + P[B] - P[A \cap B] \tag{D.2}$$

If events $A$ and $B$ were mutually exclusive, their sets in a Venn diagram would not overlap, so $P[A \cap B] = 0$ and $P[A \cup B] = P[A] + P[B]$.

FIGURE D.2 (a) Intersecting events $A$ and $B$ in sample space $\Omega$. If the area of the rectangle $\Omega$ is 1, the probability of $A \cap B$ is given by the shaded area. (b) Union of events $A$ and $B$ in sample space $\Omega$. The probability of $A \cup B$ is given by the shaded area.

#### Example D.2

Consider the rolling of a single fair die as an experiment. Then the resulting sample space, $W = \{1, 2, 3, 4, 5, 6\}$, is the set of all possible outcomes of the experiment. Let the following three events be defined as

- $A = \{1\}$ (a single roll produces a 1)
- $B = \{1, 3, 5\}$ (a single roll produces an odd number)
- $C = \{4, 5, 6\}$ (a single roll produces a number greater than 3)

Define the sets $A \cap B$, $A \cup B$, and $B \cup C$, and compute their probabilities.

**Solution:** The set $A \cap B$ includes all outcomes that are in both $A$ and $B$, so $A \cap B = \{1\}$. The set $A \cup B$ includes all outcomes that are in either $A$ or $B$, so $A \cup B = \{1, 3, 5\}$. The set $B \cup C$ includes all outcomes that are in either $B$ or $C$, so $B \cup C = \{1, 3, 4, 5, 6\}$. The probabilities of each set can be computed as

$$P[A \cap B] = P[A\,|\,B]\,P[B]$$

$$P[A \cup B] = P[A] + P[B] - P[A \cap B]$$
