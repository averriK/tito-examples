$(C.34)$

$-v_p \, v_s$

The p‑wave velocity can be seen to exceed the s‑wave velocity by an amount that depends on the compressibility (as reflected in Poisson's ratio) of the body. For a typical Poisson's ratio of 0.3 for geologic materials, the ratio $v_p/v_s = 1.87$. Thus, an observer at some distance from a disturbance that produces both would expect to feel p‑waves arriving prior to s‑waves.

## C.3 Waves in a Semi‑Infinite Body

The Earth is obviously not an infinite body – it is a very large sphere with an outer surface on which stresses cannot exist. For near‑surface earthquake engineering problems, the Earth is often idealized as a semi‑infinite body with a planar free surface (the effects of the Earth's curvature are neglected). The boundary conditions associated with the free surface allow additional solutions to the equations of motion to be obtained. These solutions describe waves whose motion is concentrated in a shallow zone near the free surface (i.e., surface waves). Since earthquake engineering is concerned with the effects of earthquakes on humans and their environment, which are located on or very near the Earth's surface, and since they attenuate with distance more slowly than body waves, surface waves are very important. Two types of surface waves are of primary importance in earthquake engineering. One, the Rayleigh wave, can be shown to exist in a homogeneous, elastic half‑space. The other surface wave, the Love wave, requires a surficial layer of lower s‑wave velocity than the underlying half‑space. Other types of surface waves exist but are much less significant from an earthquake engineering standpoint.

### C.3.1 Rayleigh Waves

Waves that exist near the surface of a homogeneous elastic half‑space were first investigated by Rayleigh (1885) [@Rayleigh1885] and are known to this date as Rayleigh waves. To describe Rayleigh waves, consider a plane wave (Figure C.8) that travels in the x‑direction with zero particle displacement in the y‑direction ($v = 0$). The z‑direction is taken as positive downward, so all particle motion occurs in the x‑z plane. Two potential functions, $\Phi$ and $\Psi$, can be defined to describe the displacements in the x‑ and z‑directions:

$$u = \frac{\partial\Phi}{\partial x} + \frac{\partial\Psi}{\partial z} \tag{C.35a}$$

$$w = \frac{\partial\Phi}{\partial z} - \frac{\partial\Psi}{\partial x} \tag{C.35b}$$

The volumetric strain, or dilatation, $\varepsilon$, of the wave is given by $\varepsilon = \varepsilon_{xx} + \varepsilon_{zz}$, or

$$\varepsilon = \frac{\partial u}{\partial x} + \frac{\partial w}{\partial z} = \nabla^2\Phi \tag{C.36}$$

The rotation in the x‑z plane [Equation (5.18)] is given by

$$\Omega_y = \frac{\partial w}{\partial x} - \frac{\partial u}{\partial z} = \nabla^2\Psi \tag{C.37}$$

**Figure C.8.** Motion induced by a typical plane wave that propagates in the x‑direction. Wave motion does not vary in the y‑direction.

Use of the potential functions allows separation of the effects of dilatation and rotation [i.e., Equations (C.36) and (C.37) indicate that $\Phi$ and $\Psi$ are associated with dilatation and rotation, respectively]. Therefore, Rayleigh waves can be thought of as combinations of p‑ and s‑waves (SV waves for this case, since the x‑z plane is vertical) that satisfy certain boundary conditions. Substitution of the expressions for $u$ and $w$ into the equations of motion as written in Equations (C.26a) and (C.26c) gives

$\partial\Phi/\partial x$, $\partial\Psi/\partial z$, $(\rho)$, $(\lambda+2\mu)\nabla^2\Phi + \mu\,\partial\Psi/\partial z\cdot\partial/\partial t = \rho\,\partial^2/\partial t^2$, $\partial/\partial x$, $\partial/\partial z$ $(C.38a)$

$\partial\Phi/\partial z$, $\partial\Psi/\partial x$, $(\rho)$, $(\lambda+2\mu)\nabla^2\Phi - \mu\,\partial\Psi/\partial x\cdot\partial/\partial t = \rho\,\partial^2/\partial t^2$, $\partial/\partial z$, $\partial/\partial x$ $(C.38b)$

Solving Equations (C.38) simultaneously for $\partial\Phi/\partial t$ and $\partial\Psi/\partial t$ gives

$$\frac{\partial^2\Phi}{\partial t^2} = \frac{\lambda + 2\mu}{\rho}\,\nabla^2\Phi = v_p^2\,\nabla^2\Phi \tag{C.39a}$$

$$\frac{\partial^2\Psi}{\partial t^2} = \frac{\mu}{\rho}\,\nabla^2\Psi = v_s^2\,\nabla^2\Psi \tag{C.39b}$$

If the wave is harmonic with frequency $\omega$ and wave number $k_R$ so that it propagates with Rayleigh wave velocity $v_R = \omega/k_R$, the potential functions can be expressed as

$$\Phi = F(z)\,e^{i(\omega t - k_R x)} \tag{C.40a}$$

$$\Psi = G(z)\,e^{i(\omega t - k_R x)} \tag{C.40b}$$

where $F$ and $G$ are functions that describe the manner in which the amplitude of the dilatational and rotational components of the Rayleigh wave vary with depth. Substituting these expressions for $\Phi$ and $\Psi$ into Equations (C.39) gives

$$\frac{d^2F(z)}{dz^2} = \left(k_R^2 - \frac{\omega^2}{v_p^2}\right)F(z) \tag{C.41a}$$

$$\frac{d^2G(z)}{dz^2} = \left(k_R^2 - \frac{\omega^2}{v_s^2}\right)G(z) \tag{C.41b}$$

which can be rearranged to give the second‑order differential equations

$$\frac{d^2F}{dz^2} - \left(k_R^2 - \frac{\omega^2}{v_p^2}\right)F = 0 \tag{C.42a}$$

$$\frac{d^2G}{dz^2} - \left(k_R^2 - \frac{\omega^2}{v_s^2}\right)G = 0 \tag{C.42b}$$

The general solution to these equations can be written as

$$F(z) = A_1 e^{-qz} + B_1 e^{qz} \tag{C.43a}$$

$$G(z) = A_2 e^{-sz} + B_2 e^{sz} \tag{C.43b}$$

where

$$q = \sqrt{k_R^2 - \frac{\omega^2}{v_p^2}}, \qquad s = \sqrt{k_R^2 - \frac{\omega^2}{v_s^2}}$$

The second terms in Equations (C.43a and C.43b) correspond to a disturbance whose displacement amplitude approaches infinity with increasing depth. Since this type of behavior is not realistic, $B_1$ and $B_2$ must be zero, and the potential functions can finally be written as

$$\Phi = A_1\,e^{-qz + i(\omega t - k_R x)} \tag{C.44a}$$

$$\Psi = A_2\,e^{-sz + i(\omega t - k_R x)} \tag{C.44b}$$

Since neither shear nor normal stresses can exist at the free surface of the half‑space, $\sigma_{zz} = 0$ and $\sigma_{xz} = 0$ when $z = 0$. Therefore,

$$\sigma_{zz} = \lambda\varepsilon + 2\mu\frac{\partial w}{\partial z} = 0 \tag{C.45a}$$

$$\sigma_{xz} = \mu\!\left(\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}\right) = 0 \tag{C.45b}$$

Using the potential function definitions of $u$ and $w$ [Equations (C.35)] and the solution for the potential functions [Equation (C.44)], the free surface boundary conditions can be rewritten as

$\sigma_{zz}(z=0) = (\lambda+2\mu)A_1(q^2 - k_R^2) + 2\mu\,ik_R s\,A_2 = 0$ $(C.46a)$

$\sigma_{xz}(z=0) = 2iqk_R A_1 + A_2(s^2 + k_R^2) = 0$ $(C.46b)$

which can be rearranged to yield

$\dfrac{(\lambda+2\mu)q^2 - \lambda k_R^2}{\mu}\dfrac{A_1}{A_2} = -2ik_R s$ $(C.47a)$

$iqk_R A_1 + (s + k_R)A_2 = 0$ $(C.47b)$

With these results, the velocities and displacement patterns of Rayleigh waves can be determined.

#### C.3.1.1 Rayleigh Wave Velocity

The velocity at which Rayleigh waves travel is of interest in geotechnical earthquake engineering. As discussed in Chapter 6, Rayleigh waves are often mechanically generated and their velocities are measured in the field to investigate the stiffness of surficial soils. Adding Equations (C.47) and cross‑multiplying gives

$\mu(q + s)k_R^2 + (\lambda+2\mu)q^2 s\,k_R - (\lambda+2\mu)q\,k_R^2 = 0$ $(C.48)$

which, upon introducing the definitions of $q$ and $s$ and factoring out a $G\,k_R$ term, yields

$16\!\left(1 - \dfrac{\omega^2}{v_p^2 k_R^2}\right)\!\left(1 - \dfrac{\omega^2}{v_s^2 k_R^2}\right) = \left(2 - \dfrac{\omega^2}{v_s^2 k_R^2}\right)^2 \tag{C.49}$

Defining $K_{Rs}$ as the ratio of the Rayleigh wave velocity to the s‑wave velocity

$$K_{Rs} = \frac{v_R}{v_s} = \frac{\omega}{v_s k_R} \tag{C.50a}$$

then

$$K_{Rs,\alpha} = \frac{v_R}{v_p} = \frac{\omega}{v_p k_R} = \alpha K_{Rs} \tag{C.50b}$$

where $\alpha = \sqrt{\mu/(\lambda+2\mu)} = \sqrt{(1-2\nu)/(2-2\nu)}$. Then Equation (C.49) can be rewritten as

$(K_{Rs}^2 - 2)^2(K_{Rs}^2 - 2) - 16(1 - K_{Rs}^2)(1 - \alpha^2 K_{Rs}^2) = 0$ $(C.51a)$

which can be expanded and rearranged into the equation

$K_{Rs}^6 - 8K_{Rs}^4 + (24 - 16\alpha^2)K_{Rs}^2 - 16(1-\alpha^2) = 0$ $(C.51b)$

This equation is cubic in $K_{Rs}$, and real solutions for $K_{Rs}$ can be found for various values of Poisson's ratio. These allow evaluation of the ratios of the Rayleigh wave velocity to both s‑ and p‑wave velocities as functions of $\nu$. The solution shown in Figure C.9 shows that Rayleigh waves travel slightly slower than s‑waves for all values of Poisson's ratio except 0.5.

#### C.3.1.2 Rayleigh Wave Displacement Amplitude

Section C.3.1.1 showed how the velocity of a Rayleigh wave compares with that of p‑ and s‑waves. Some of the intermediate results of that section can be used to illustrate the nature of particle motion during the passage of Rayleigh waves. Substituting the solutions for the potential functions $\Phi$ and $\Psi$ [Equations (C.44)] into the expressions for $u$ and $w$ [Equation (C.35)] and carrying out the necessary partial differentiations yields

$$u = -A_1 i k_R e^{-qz+i(\omega t-k_Rx)} - A_2 s\,e^{-sz+i(\omega t-k_Rx)} \tag{C.52a}$$

$$w = -A_1 q\,e^{-qz+i(\omega t-k_Rx)} + A_2 i k_R e^{-sz+i(\omega t-k_Rx)} \tag{C.52b}$$

**Figure C.9.** Variation of Rayleigh wave and body wave propagation velocities with Poisson's ratio.

Rearranging Equation (C.47b) as $A_2/A_1 = -iqk_R/(s + k_R)$ and substituting into Equations (C.52) gives

$$u = A_1 i k_R\!\left[-e^{-qz} + \frac{qs}{k_R + s}\,e^{-sz}\right]e^{i(\omega t - k_R x)} \tag{C.53a}$$

$$w = A_1 k_R\!\left[-qe^{-qz} + \frac{qk_R}{k_R + s}\,e^{-sz}\right]e^{i(\omega t - k_R x)} \tag{C.53b}$$

where the terms in parentheses describe the variation of the amplitudes of $u$ and $w$ with depth. These horizontal and vertical displacement amplitudes are illustrated for several values of Poisson's ratio in Figure C.10. Examination of Equations (C.53) indicates that the horizontal and vertical displacements are out of phase by 90°. Hence the horizontal displacement will be zero when the vertical displacement reaches its maximum (or minimum), and vice versa. The motion of a particle near the surface of the half‑space is in the form of a retrograde ellipse (as opposed to the prograde ellipse particle motion observed at the surface of water waves). The general nature of Rayleigh wave motion is illustrated in Figure 2.2a. The Rayleigh waves produced by earthquakes were once thought to appear only at very large site‑to‑source distances (several hundred km). It is now recognized, however, that they can be significant at much shorter distances (a few tens of kilometers). The ratio of minimum epicentral distance, $R$, to focal depth, $h$, at which Rayleigh waves first appear in a homogeneous medium is given by

$$\frac{R}{h} = \frac{1}{\sqrt{(v_P/v_R)^2 - 1}} \tag{C.54}$$

where $v_p$ and $v_R$ are the wave propagation velocities of p‑waves and Rayleigh waves, respectively [@EwingEtAl1957].

**Figure C.10.** Horizontal and vertical motion of Rayleigh waves. A negative amplitude ratio indicates that the displacement is in the opposite direction of the surface displacement. (After Richart et al., 1970 [@RichartEtAl1970].)

### C.3.2 Love Waves

In a homogeneous elastic half‑space, only p‑waves, s‑waves, and Rayleigh waves can exist. If the half‑space is overlain by a layer of material with lower body wave velocity, however, Love waves can also develop (Love, 1927) [@Love1927]. Love waves essentially consist of SH‑waves that are trapped by multiple reflections within the surficial layer. Consider the case of a homogeneous surficial layer of thickness $H$ overlying a homogeneous half‑space as shown in Figure C.11. A Love wave traveling in the $+x$‑direction would involve particle displacements only in the y‑direction (SH‑wave motion), and could be described by the equation

$$v(x,z,t) = V(z)\,e^{i(k_L x - \omega t)} \tag{C.55}$$

**Figure C.11.** Schematic illustration of softer surficial layer ($G_1/\rho_1 < G_2/\rho_2$) overlying elastic half‑space, the simplest conditions for which Love waves can exist.

where $v$ is the particle displacement in the y‑direction, $V(z)$ describes the variation of $v$ with depth, and $k_L$ is the wave number of the Love wave. The Love wave must satisfy the wave equations for s‑waves in both the surficial layer and the half‑space

$G_1(\partial^2 v/\partial x^2 + \partial^2 v/\partial z^2) = \rho_1\,\partial^2 v/\partial t^2$, for $0 \le z \le H$ $(C.56a)$

$G_2(\partial^2 v/\partial x^2 + \partial^2 v/\partial z^2) = \rho_2\,\partial^2 v/\partial t^2$, for $z \ge H$ $(C.56b)$

The amplitude can be shown [@AkiRichards1980] to vary with depth according to

$$V(z) = \begin{cases} A_1 e^{-\nu_1 z} + B_1 e^{\nu_1 z}, & 0 \le z < H \\[4pt] A_2 e^{-\nu_2 z} + B_2 e^{\nu_2 z}, & z \ge H \end{cases} \tag{C.57a}$$

where the $A$ and $B$ coefficients describe the amplitudes of downgoing and upgoing waves, respectively, and

$$\nu_{1,2} = \sqrt{k_L^2 - \omega^2/(G_{1,2}/\rho_{1,2})} \tag{C.57b}$$

Since the half‑space extends to infinite depth, $B_2$ must be zero (no energy can be supplied or reflected at infinite depth to produce an upgoing wave). The requirement that all stresses vanish at the ground surface is satisfied if

$$\frac{\partial v}{\partial z}\bigg|_{z=0} = \frac{\partial V(z)}{\partial z}\bigg|_{z=0}\,e^{i(k_L x - \omega t)} = (-\nu_1 A_1 + \nu_1 B_1)\,e^{i(k_L x-\omega t)} = 0 \tag{C.58}$$

in other words, if $A_1 = B_1$. The amplitudes can now be rewritten in terms of the two remaining unknown amplitudes as

$$V(z) = \begin{cases} A_1(e^{-\nu_1 z} + e^{\nu_1 z}), & 0 \le z < H \\[4pt] A_2\,e^{-\nu_2 z}, & z \ge H \end{cases} \tag{C.59}$$

At the $z = H$ interface, continuity of stresses requires that

$$G_1 \nu_1 A_1 \sin(\nu_1 H) = iG_2 \nu_2 A_2 \tag{C.60}$$

and compatibility of displacements requires that

$$A_1 \cos(\nu_1 H) = A_2\,e^{-\nu_2 H} \tag{C.61}$$

Using Equations (C.60) and (C.61), $A_2$ can be expressed in terms of $A_1$ by

$$A_2 = \frac{2\cos(\nu_1 H)}{e^{-\nu_2 H}} A_1 \tag{C.62}$$

Substituting Equations (C.59) and (C.60) into (C.55) gives

$$v(x,z,t) = \begin{cases} A\cos\!\left(\dfrac{\omega z}{\sqrt{v_{s1}^{-2}-v_L^{-2}}}\right)e^{i(k_L x-\omega t)}, & 0 \le z < H \\[6pt] A\cos\!\left(\dfrac{\omega H}{\sqrt{v_{s1}^{-2}-v_L^{-2}}}\right)\exp\!\left(-\omega(z-H)\sqrt{v_L^{-2}-v_{s2}^{-2}}\right)e^{i(k_L x-\omega t)}, & z \ge H \end{cases} \tag{C.63}$$

where $v_{s1}$ and $v_{s2}$ are the shear wave velocities of materials 1 and 2, respectively, and $v_L$ is the velocity of the Love wave. Equation (C.63) shows, as illustrated in Figure C.12, that the Love wave displacement amplitude varies with depth as a cosine function in the surficial layer and decays exponentially with depth in the underlying half‑space. Because of this, Love waves are often described as SH‑waves that are trapped in the surficial layer. The general nature of Love wave displacement is shown in Figure 2.2b.

**Figure C.12.** Variation of particle displacement amplitude with depth for Love waves.

The Love wave velocity is given by the solution of

$$\tan\!\left(\omega H\sqrt{\frac{1}{v_{s1}^2} - \frac{1}{v_L^2}}\right) = \frac{G_2\sqrt{v_L^{-2} - v_{s2}^{-2}}}{G_1\sqrt{v_{s1}^{-2} - v_L^{-2}}} \tag{C.64}$$

which indicates, as illustrated in Figure C.13, that Love wave velocities range from the s‑wave velocity of the half‑space (at very low frequencies) to the s‑wave velocity of the surficial layer (at very high frequencies). This frequency dependence indicates that Love waves are dispersive (Section C.3.4).

**Figure C.13.** Variation of Love wave velocity with frequency.

### C.3.3 Higher‑Mode Surface Waves

Any surface wave must (1) satisfy the equation of motion, (2) produce zero stress at the ground surface, and (3) produce zero displacement at infinite depth. Nontrivial solutions do not exist for arbitrary combinations of frequency and wave number; rather, a set of discrete and unique wave numbers exist for a given frequency. Each wave number describes a different displacement pattern, or mode, of the surface wave. The preceding derivations have been limited to the fundamental modes of Rayleigh and Love waves, which are the most important for earthquake engineering applications. Detailed treatment of higher‑mode surface waves can be found in most advanced seismology texts.

### C.3.4 Dispersion of Surface Waves

For a homogeneous half‑space, the Rayleigh wave velocity was shown to be related to the body wave velocities by Poisson's ratio. Since the body wave velocities are constant with depth, the Rayleigh wave velocity in a homogeneous half‑space is independent of frequency. The velocity of the Love wave, on the other hand, varies with frequency between an upper and a lower limit. Dispersion is a phenomenon in which waves of different frequencies (and different wavelengths) propagate at different velocities. Hence Love waves are clearly dispersive, and Rayleigh waves in a homogeneous half‑space are nondispersive. Near the Earth's surface, however, soil and rock stiffnesses usually increase with depth. Since the depth to which a Rayleigh wave causes significant displacement increases with increasing wavelength (Figure C.10), Rayleigh waves of long wavelength (low frequency) can propagate faster than Rayleigh waves of short wavelength (high frequency). Therefore, in the real world of heterogeneous materials, Rayleigh waves are also dispersive. The dispersion of Rayleigh waves can be used to evaluate subsurface stiffness profiles by field testing techniques described in Chapter 6. Since the velocities of both Rayleigh waves and Love waves decrease with increasing frequency, the low‑frequency components of surface waves produced by earthquakes can be expected to arrive at a particular site before their high‑frequency counterparts. This tendency to spread the seismic energy over time is an important effect of dispersion.

### C.3.5 Phase and Group Velocities

The solutions for Rayleigh wave velocity, $v_R$, and Love wave velocity, $v_L$, were based on the assumption of harmonic loading which produces an infinite wave train. These velocities describe the rate at which points of constant phase (e.g., peaks, troughs, or zero points) travel through the medium and are called phase velocities. A transient disturbance may produce a packet of waves with similar frequencies. This packet of waves travels at the group velocity, $c_g$, given by

$$c_g = c + k\frac{dc}{dk} \tag{C.65}$$

where $c$ is the phase velocity (equal to $v_R$ or $v_L$ depending on which type of wave is being considered) and $k$ is the wave number (equal to $\omega/v_R$ or $\omega/v_L$). In a nondispersive material, $dc/dk = 0$, so the group velocity is equal to the phase velocity. Since both $v_R$ and $v_L$ generally decrease with increasing frequency in geologic materials, $dc/dk$ is less than zero and the group velocity is lower than the phase velocity. Consequently, a wave packet would appear to consist of a series of individual peaks that appear at the back end of the packet, move through the packet to the front, and then disappear. The opposite behavior can be observed by dropping a rock into a calm pond of water (for which $c < c_g$) and watching the resulting ripples carefully.

## C.4 Waves in a Layered Body

The model of a homogeneous elastic half‑space is useful for explaining the existence of body waves and Rayleigh waves, and the addition of a softer surficial layer allows Love waves to be described. In the Earth, however, conditions are much more complicated with many different materials of variable thickness occurring in many areas. To analyze wave propagation under such conditions, and to understand the justification for idealizations of actual conditions when all features cannot be explicitly analyzed, the general problem of wave behavior at interfaces must be investigated.

### C.4.1 One‑Dimensional Case: Material Boundary in an Infinite Rod

Consider a harmonic stress wave traveling along a constrained rod in the $+x$ direction and approaching an interface between two different materials, as shown in Figure C.14. Since the wave is traveling toward the interface, it will be referred to as the incident wave. Since it is traveling in material 1, its wavelength will be $\lambda_i = 2\pi/k_i$, and based on Eq. (C.12) it can be described by

$$\sigma_i(x,t) = \sigma_I\,e^{i(\omega t - k_i x)} \tag{C.66a}$$

When the incident wave reaches the interface, part of its energy will be transmitted through the interface to continue traveling in the positive x‑direction through material 2. This transmitted wave will have a wavelength $\lambda_t = 2\pi/k_t$. The remainder will be reflected at the interface and will travel back through material 1 in the negative x‑direction as a reflected wave. The transmitted and reflected waves can be described by

$$\sigma_t(x,t) = \sigma_T\,e^{i(\omega t - k_t x)} \tag{C.66b}$$

$$\sigma_r(x,t) = \sigma_R\,e^{i(\omega t + k_r x)} \tag{C.66c}$$

Assuming that the displacements associated with each of these waves are of the same harmonic form as the stresses that cause them:

$$u_i(x,t) = A_i\,e^{i(\omega t - k_i x)} \tag{C.67a}$$

$$u_R(x,t) = A_r\,e^{i(\omega t + k_r x)} \tag{C.67b}$$

**Figure C.14.** One‑dimensional wave propagation at material interface. Incident and reflected waves travel in opposite directions in material 1. The transmitted wave travels through material 2 in the same direction as the incident wave.
