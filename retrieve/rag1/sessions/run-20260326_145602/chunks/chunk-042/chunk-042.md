$$r_{max} \leq \sum_{n=1}^{N} (r_n)_{max}$$

(B.122)

This upper bound value is usually too conservative and is rarely used for design. Instead, modal combination procedures based on random vibration theory are used. The simplest of these is the root‑sum‑square value

$$r_{max} = \sqrt{\sum_{n=1}^{N} (r_n)_{max}^2}$$

(B.123)

The root‑sum‑square procedure provides a good estimate of maximum total response when the natural periods are well separated (by a factor of about 1.5 or more for 5% damping). Procedures that account for correlation between modes are available (Newmark and Rosenblueth, 1971; [@Chopra2022]) for cases of closely spaced modes.

## B.10.5 Discussion

The mode superposition method and response spectrum analysis procedures both rely on the representation of an MDOF system by a set of SDOF systems. The characteristics of the set of SDOF systems are such that those corresponding to the lower natural frequencies generally contribute more to the total response than those corresponding to the higher natural frequencies. For practical purposes, the response of an MDOF system can be computed with reasonable accuracy by considering only the lower modes that contribute significantly to the total response of the structure. For some structures, only a small number of modes may need to be considered. It is common to exclude higher modes if their participation factors fall below a certain threshold of percent contribution to total response (often shear in the lowest story). All of the analyses described in this section apply to linear structures. Procedures for analysis of nonlinear MDOF structures are available but are beyond the scope of this appendix.

# Appendix C: Wave Propagation

## C.1 Introduction

It is the continuous nature of geologic materials that causes soil dynamics and geotechnical earthquake engineering to diverge from their structural counterparts. While most structures can readily be idealized as assemblages of discrete masses with discrete sources of stiffness, geologic materials cannot. They must be treated as continua, and their response to dynamic disturbances must be described in the context of wave propagation. Some basic concepts of wave propagation will be required to fully understand the material presented in Chapters 2–4; a more fundamental treatment of the basic concepts is presented in this appendix. The presentation follows a repeated pattern of simple‑to‑complex applications. The relatively simple problem of waves in unbounded media is followed by the more complicated problem of waves in bounded and layered media. Within each, the concepts are presented first for the simple case of one‑dimensional wave propagation, and then for the more general three‑dimensional case. The careful reader will note that the basic techniques and principles used to solve the more complicated cases are generally the same as those used for the simple cases; the additional complexity simply results from the need to consider more dimensions.

## C.2 Waves in Unbounded Media

The propagation of stress waves is most easily understood by first considering an unbounded, or "infinite," medium [i.e., one that extends infinitely in the direction(s) of wave propagation]. A simple, one‑dimensional idealization of an unbounded medium is that of an infinitely long rod or bar. Using the basic requirements of equilibrium of forces and compatibility of displacements, and using strain‑displacement and stress‑strain relationships, a one‑dimensional wave equation can be derived and solved. The process can be repeated, using the same requirements and relationships, for the more general case of wave propagation in a medium that extends infinitely in three orthogonal directions.

### C.2.1 One‑Dimensional Wave Propagation

Three different types of vibration can occur in a thin rod: longitudinal vibration during which the axis of the rod extends and contracts without lateral displacement; torsional vibration in which the rod rotates about its axis without lateral displacement of the axis; and flexural vibration during which the axis itself moves laterally. The flexural vibration problem has little application in soil dynamics and will not be considered further. For the first two cases, however, the operative wave equations are easily derived and solved.

#### C.2.1.1 Longitudinal Waves in an Infinitely Long Rod

Consider the free vibration of an infinitely long, linear elastic, constrained rod with cross‑sectional area, $A$, Young's modulus, $E$, Poisson's ratio, $\nu$, and mass density, $\rho$, as shown in Figure C.1. If the rod is constrained against radial straining, then particle displacements caused by a longitudinal wave must be parallel to the axis of the rod. Assume that cross‑sectional planes will remain planar and that stresses will be distributed uniformly over each cross‑section. As a stress wave travels along the rod and passes through the small element shown in Figure C.2, the axial stress at the left end of the element ($x = x_0$) is $\sigma_x$. At the right end ($x = x_0 + dx$), the axial stress is $\sigma_x + (\partial \sigma_x / \partial x)\, dx$. Dynamic equilibrium of the element (Newton's second law) requires that

$$\left(\sigma_x + \frac{\partial \sigma_x}{\partial x}\, dx\right) A - \sigma_x A = \rho A\, dx\, \ddot{u}$$

(C.1)

where $u$ is the displacement in the $x$‑direction. This simply states that the unbalanced external forces acting on the ends of the element [the left side of Equation (C.1)] must equal an inertial force induced by the acceleration of the mass of the element (the right side). Simplifying yields the one‑dimensional equation of motion

$$\frac{\partial \sigma_x}{\partial x} = \rho \ddot{u}$$

(C.2)

In this form, the equation of motion is valid for any stress‑strain behavior but cannot be solved directly because it mixes stresses [on the left side of Equation (C.2)] with displacements (on the right side). To simplify the equation of motion, the left side can be expressed in terms of displacement by using the stress‑strain relationship, $\sigma_x = M \varepsilon_x$, where the constrained modulus $M = (1 - \nu)E / [(1 + \nu)(1 - 2\nu)]$, and $\varepsilon_x$ is obtained from the strain‑displacement relationship, $\varepsilon_x = \partial u / \partial x$. These substitutions allow the one‑dimensional equation of motion to be written in the familiar form of the one‑dimensional longitudinal wave equation for a constrained rod:

$$\frac{\partial^2 u}{\partial t^2} = \frac{M}{\rho} \frac{\partial^2 u}{\partial x^2}$$

(C.3)

The one‑dimensional wave equation can be written in the alternative form

$$\frac{\partial^2 u}{\partial t^2} = v_p^2 \frac{\partial^2 u}{\partial x^2}$$

(C.4)

where $v_p = \sqrt{M/\rho}$ is the wave propagation velocity. Note that the wave propagation velocity depends only on the properties of the rod material (its stiffness and density) and is independent of the amplitude of the stress wave or the nature of the loading. The wave propagation velocity increases with increasing stiffness and with decreasing density.

*Figure C.1 Constrained, infinite rod for one‑dimensional wave propagation. Constraint against radial straining schematically represented by rollers.*

*Figure C.2 Stresses and displacements at ends of element of length $dx$ and cross‑sectional area, $A$.*

The wave propagation velocity is an extremely important material property that is relied upon heavily in soil dynamics and geotechnical earthquake engineering. The wave propagation velocity is the velocity at which a stress wave would travel along the rod. It is not the same as the particle velocity, which is the velocity at which a single point within the rod would move as the wave passes through it. Knowing that $\varepsilon_x = \partial u / \partial x$ (from the strain‑displacement relationship), $\sigma_x = M \varepsilon_x$ (from the stress‑strain relationship), and $\partial u / \partial t = v_p\, \partial u / \partial x$ (from the definition of wave propagation velocity), the particle velocity $\dot{u}$ can be shown to be

$$\dot{u} = \frac{\sigma_x}{\rho v_p}$$

(C.5)

Equation (C.5) shows that the particle velocity is proportional to the axial stress in the rod. The coefficient of proportionality, $\rho v_p$, is called the specific impedance of the material. The specific impedance is another important property that influences the behavior of waves at boundaries (Section C.4).

#### C.2.1.2 Torsional Waves in an Infinitely Long Rod

Torsional waves involve rotation of the rod about its own axis. In the case of the longitudinal wave, the direction of particle motion was parallel to the direction of wave propagation. For torsional waves, particle motion is constrained to planes perpendicular to the direction of wave propagation. The development of a wave equation for torsional vibrations, however, follows exactly the same steps as for longitudinal vibration. Consider the short segment of a cylindrical rod shown in Figure C.3 as a torsional wave of torque amplitude, $T$, travels along the rod. Dynamic torsional equilibrium requires that the unbalanced external torque [left side of Equation (C.6)] is equal to the inertial torque (right side):

$$\left(T + \frac{\partial T}{\partial x}\, dx\right) - T = \rho J\, dx\, \ddot{\theta}$$

(C.6)

where $J$ is the polar moment of inertia of the rod about its axis. This equilibrium equation can be simplified to produce the equation of motion

$$\frac{\partial T}{\partial x} = \rho J \frac{\partial^2 \theta}{\partial t^2}$$

(C.7)

Now, incorporating the torque‑rotation relationship

$$T = GJ \frac{\partial \theta}{\partial x}$$

(C.8)

*Figure C.3 Torque and rotation at ends of element of length $dx$ and cross‑sectional area, $A$.*

where $G$ is the shear modulus of the rod, the torsional wave equation can be written as

$$\frac{\partial^2 \theta}{\partial t^2} = \frac{G}{\rho} \frac{\partial^2 \theta}{\partial x^2} = v_s^2 \frac{\partial^2 \theta}{\partial x^2}$$

(C.9)

where $v_s = \sqrt{G/\rho}$ is the velocity of propagation of the torsional wave. Note that the form of the wave equation for torsional waves [Equation (C.9)] is identical to that for longitudinal waves [Equation (C.4)], but the wave propagation velocities are different. The wave propagation velocity depends both on the stiffness of the rod in the mode of deformation induced by the wave and on the material mass density but is independent of the amplitude of the stress wave.

#### C.2.1.3 Solution of the One‑Dimensional Equation of Motion

The one‑dimensional wave equation is a second‑order partial differential equation of the form

$$\frac{\partial^2 u}{\partial t^2} = v^2 \frac{\partial^2 u}{\partial x^2}$$

(C.10)

where $v$ represents the wave propagation velocity corresponding to the type of stress wave of interest. The solution of such an equation can be written in the form

$$u(x, t) = f(vt - x) + g(vt + x)$$

(C.11)

where $f$ and $g$ can be any arbitrary functions of $(vt - x)$ and $(vt + x)$ that satisfy Equation (C.10). Note that the argument of $f$ remains constant when $x$ increases with time (at velocity, $v$), and the argument of $g$ remains constant when $x$ decreases with time. Therefore, the solution of Equation (C.11) describes a displacement wave $f(vt - x)$ traveling at velocity $v$ in the positive $x$‑direction and another wave $g(vt + x)$ traveling at the same speed in the negative $x$‑direction. It also implies that the shapes of the waves do not change with position or time. If the rod is subjected to some steady‑state harmonic stress $\sigma(t) = \sigma_0 \cos\omega t$ where $\sigma_0$ is the stress wave amplitude and $\omega$ is the circular frequency of the applied loading, the solution can be expressed using the wave number $k = \omega/v$ in the form

$$u(x, t) = A\cos(\omega t - kx) + B\cos(\omega t + kx)$$

(C.12)

Here the first and second terms describe harmonic waves propagating in the positive and negative $x$‑directions, respectively. The wave number is related to the wavelength, $\lambda$, of the motion by

$$\lambda = \frac{2\pi}{k} = \frac{v}{f} = vT$$

(C.13)

where $T$ is the period of the applied loading and $f = 1/T$. Note that at a given frequency, the wavelength increases with increasing wave propagation velocity. Equation (C.12) indicates that the displacement varies harmonically with respect to both time and position as illustrated in Figure C.4. Equation (C.13) and Figure C.4 show that wave number is to wavelength as circular frequency is to period of vibration. For a wave propagating in the positive $x$‑direction only ($B = 0$), differentiating $u(x,t)$ twice with respect to $x$ and twice with respect to $t$ and substituting into the wave equation [Equation (C.10)] gives

$$-Ak^2\cos(\omega t - kx) = -\frac{\omega^2}{v^2} A\cos(\omega t - kx)$$

(C.14)

*Figure C.4 Particle displacement (a) as function of time, and (b) as function of position along the rod.*

which reduces to the identity $\omega = kv$, thereby verifying Equation (C.12) as a solution to the wave equation. Using complex notation (Appendix A), the equivalent form of the solution can be written as

$$u(x, t) = Ce^{i(\omega t - kx)} + De^{i(\omega t + kx)}$$

(C.15)

This form of the solution can be verified in the same way as the trigonometric form.

### C.2.2 Three‑Dimensional Wave Propagation

The preceding discussion of wave propagation in rods illustrates some of the basic principles of wave propagation, but an infinite rod is hardly an adequate model for describing the propagation of seismic waves through the Earth. Since the Earth is three‑dimensional and sources of seismic energy are three‑dimensional, seismic waves must be described in terms of three‑dimensional wave propagation. Derivations of three‑dimensional equations of motion follow the same steps as those used for one‑dimensional propagation; the equations of motion are formulated from equilibrium considerations, stress‑strain relationships, and strain‑displacement relationships. In the three‑dimensional case, however, the various relationships are more complex and the derivation more cumbersome. Brief reviews of three‑dimensional stress and strain notation and three‑dimensional stress‑strain behavior will precede the derivation of the equations of motion.

#### C.2.2.1 Review of Stress Notation

The stress at a point on some plane passing through a solid does not usually act normal to that plane but has both normal and shear components. Considering a small element with one corner at the center of an $x$‑$y$‑$z$ Cartesian coordinate system (Figure C.5), a total of nine components of stress will act on its faces. These stresses are denoted by $\sigma_{xx}$, $\sigma_{yy}$, $\sigma_{zz}$, and so on, where the first and second letters in the subscript describe the direction of the stress itself and the axis perpendicular to the plane in which it acts, respectively. Thus $\sigma_{xx}$, $\sigma_{yy}$, $\sigma_{zz}$ are normal stresses, while the other six components represent shear stresses. Moment equilibrium of the element requires that

$$\sigma_{xy} = \sigma_{yx}, \quad \sigma_{xz} = \sigma_{zx}, \quad \sigma_{yz} = \sigma_{zy}$$

(C.16)

which means that only six independent components of stress are required to define the state of stress of the element completely. In some references, the notation $\sigma_x$, $\sigma_y$, $\sigma_z$, $\tau_{xy}$, $\tau_{yz}$, and $\tau_{xz}$ is used to describe $\sigma_{xx}$, $\sigma_{yy}$, $\sigma_{zz}$, $\sigma_{xy}$, $\sigma_{yz}$, and $\sigma_{xz}$, respectively.

*Figure C.5 Stress notation for element of dimensions $dx$ by $dy$ by $dz$.*

#### C.2.2.2 Review of Strain Notation

Components of strain are easily visualized by considering the two‑dimensional strain in the $x$‑$y$ plane shown in Figure C.6. The point $P$, at coordinates $(x_0, y_0)$, is at one corner of the infinitesimal element $PQRS$ which has a square shape before deformation. After deformation, the infinitesimal element has been displaced, distorted, and rotated into the shape $P'Q'R'S'$. From Figure C.6, $\tan\alpha = \partial v / \partial x$ and $\tan\beta = \partial u / \partial y$, where $u$ and $v$ represent displacements in the $x$‑ and $y$‑directions, respectively. The shear strain in the $x$‑$y$ plane is given by $\varepsilon_{xy} = \alpha + \beta$. For small deformations, the angles may be taken equal to their tangents so that the relationship between the shear strain and the displacements is $\varepsilon_{xy} = \partial v / \partial x + \partial u / \partial y$. The rotation of the element about the $z$‑axis is given by $\Omega_z = (\alpha - \beta)/2$.

*Figure C.6 Square element subjected to plane strain deformation.*

Analogous definitions can be developed for the $x$‑$z$ and $y$‑$z$ planes. For the three‑dimensional case, the strain‑displacement relationships are defined by

$$\varepsilon_{xx} = \frac{du}{dx}, \quad \varepsilon_{yy} = \frac{dv}{dy}, \quad \varepsilon_{zz} = \frac{dw}{dz}$$

$$\varepsilon_{xy} = \frac{du}{dy} + \frac{dv}{dx}, \quad \varepsilon_{yz} = \frac{dv}{dz} + \frac{dw}{dy}, \quad \varepsilon_{zx} = \frac{dw}{dx} + \frac{du}{dz}$$

(C.17)

Rigid body rotation about the $x$‑, $y$‑, and $z$‑axes are given by the rotation‑displacement relationships

$$\Omega_x = \frac{1}{2}\!\left(\frac{dw}{dy} - \frac{dv}{dz}\right), \quad \Omega_y = \frac{1}{2}\!\left(\frac{du}{dz} - \frac{dw}{dx}\right), \quad \Omega_z = \frac{1}{2}\!\left(\frac{dv}{dx} - \frac{du}{dy}\right)$$

(C.18)

The first three quantities, $\varepsilon_{xx}$, $\varepsilon_{yy}$, and $\varepsilon_{zz}$, represent the extensional and compressional strains parallel to the $x$‑, $y$‑, and $z$‑axes, and are called normal strains. The second three quantities, $\varepsilon_{xy}$, $\varepsilon_{yz}$, and $\varepsilon_{zx}$, represent the components of shear strain in the planes corresponding to their suffixes. These six quantities are the components of strain that correspond to the deformation at $P$. In some references, the notation $\varepsilon_x$, $\varepsilon_y$, $\varepsilon_z$, $\gamma_{xy}$, $\gamma_{yz}$, and $\gamma_{zx}$ is used to describe $\varepsilon_{xx}$, $\varepsilon_{yy}$, $\varepsilon_{zz}$, $\varepsilon_{xy}$, $\varepsilon_{yz}$, and $\varepsilon_{zx}$ respectively.

#### C.2.2.3 Review of Stress‑Strain Relationships

Stresses and strains are proportional in a linear elastic body. The stress‑strain relationship can be described by Hooke's law, which can be written in generalized form as

$$\sigma_{xx} = c_{11}\varepsilon_{xx} + c_{12}\varepsilon_{yy} + c_{13}\varepsilon_{zz} + c_{14}\varepsilon_{xy} + c_{15}\varepsilon_{yz} + c_{16}\varepsilon_{zx}$$

$$\sigma_{yy} = c_{21}\varepsilon_{xx} + c_{22}\varepsilon_{yy} + c_{23}\varepsilon_{zz} + c_{24}\varepsilon_{xy} + c_{25}\varepsilon_{yz} + c_{26}\varepsilon_{zx}$$

$$\sigma_{zz} = c_{31}\varepsilon_{xx} + c_{32}\varepsilon_{yy} + c_{33}\varepsilon_{zz} + c_{34}\varepsilon_{xy} + c_{35}\varepsilon_{yz} + c_{36}\varepsilon_{zx}$$

$$\sigma_{xy} = c_{41}\varepsilon_{xx} + c_{42}\varepsilon_{yy} + c_{43}\varepsilon_{zz} + c_{44}\varepsilon_{xy} + c_{45}\varepsilon_{yz} + c_{46}\varepsilon_{zx}$$

$$\sigma_{yz} = c_{51}\varepsilon_{xx} + c_{52}\varepsilon_{yy} + c_{53}\varepsilon_{zz} + c_{54}\varepsilon_{xy} + c_{55}\varepsilon_{yz} + c_{56}\varepsilon_{zx}$$

$$\sigma_{zx} = c_{61}\varepsilon_{xx} + c_{62}\varepsilon_{yy} + c_{63}\varepsilon_{zz} + c_{64}\varepsilon_{xy} + c_{65}\varepsilon_{yz} + c_{66}\varepsilon_{zx}$$

(C.19)

where the 36 coefficients represent the elastic constants of the material. The requirement that the elastic strain energy must be a unique function of the strain (which requires that $c_{ij} = c_{ji}$ for all $i$ and $j$) reduces the number of independent coefficients to 21. If the material is isotropic, the coefficients must be independent of direction, so that

$$c_{12} = c_{21} = c_{13} = c_{31} = c_{23} = c_{32} = \lambda$$

$$c_{44} = c_{55} = c_{66} = \mu$$

$$c_{11} = c_{22} = c_{33} = \lambda + 2\mu$$

(C.20)

and all other constants are zero. Therefore, Hooke's law for an isotropic, linear, elastic material allows all components of stress and strain to be expressed in terms of the two Lamé constants, $\lambda$ and $\mu$:

$$\sigma_{xx} = \lambda\varepsilon + 2\mu\varepsilon_{xx}, \quad \sigma_{xy} = \mu\varepsilon_{xy}$$

$$\sigma_{yy} = \lambda\varepsilon + 2\mu\varepsilon_{yy}, \quad \sigma_{yz} = \mu\varepsilon_{yz}$$

$$\sigma_{zz} = \lambda\varepsilon + 2\mu\varepsilon_{zz}, \quad \sigma_{zx} = \mu\varepsilon_{zx}$$

(C.21)

where the volumetric strain $\varepsilon = \varepsilon_{xx} + \varepsilon_{yy} + \varepsilon_{zz}$. Note that the symbol $\lambda$ is used universally for both Lamé's constant and for wavelength; the context in which it is used should make its meaning obvious. For convenience, several other parameters are often used to describe the stress‑strain behavior of isotropic, linear, and elastic materials, each of which can be expressed in terms of Lamé's constants. Some of the more common of these are

$$E = \frac{\mu(3\lambda + 2\mu)}{\lambda + \mu} \quad \text{Young's modulus}$$

(C.22a)

$$K = \lambda + \frac{2}{3}\mu \quad \text{Bulk modulus}$$

(C.22b)

$$G = \mu \quad \text{Shear modulus}$$

(C.22c)

$$M = \lambda + 2\mu \quad \text{Constrained modulus}$$

(C.22d)

$$\nu = \frac{\lambda}{2(\lambda + \mu)} \quad \text{Poisson's ratio}$$

(C.22e)

Hooke's law for an isotropic, linear, elastic material can be expressed using any combination of two of these parameters.

#### C.2.2.4 Equations of Motion for a Three‑Dimensional Elastic Solid

The three‑dimensional equations of motion for an elastic solid are obtained from equilibrium requirements in much the same way as for the one‑dimensional rod, except that equilibrium must be ensured in three perpendicular directions. Consider the variation in stress across an infinitesimal cube aligned with its sides parallel to the $x$‑$y$‑$z$ axes shown in Figure C.7. Assuming that the average stress on each face of the cube is represented by the stress shown at the center of the face, the resultant forces acting in the $x$‑, $y$‑, and $z$‑directions can be evaluated; in the $x$‑direction, the unbalanced external forces must be balanced by an inertial force in that direction, so that

$$\left(\sigma_{xx} + \frac{\partial \sigma_{xx}}{\partial x}\,dx - \sigma_{xx}\right)dy\,dz + \left(\sigma_{xy} + \frac{\partial \sigma_{xy}}{\partial y}\,dy - \sigma_{xy}\right)dx\,dz + \left(\sigma_{xz} + \frac{\partial \sigma_{xz}}{\partial z}\,dz - \sigma_{xz}\right)dx\,dy = \rho\,dx\,dy\,dz\,\ddot{u}$$

(C.23)

*Figure C.7 Stresses in $x$‑direction on infinitesimal cube.*

which simplifies to

$$\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \sigma_{xy}}{\partial y} + \frac{\partial \sigma_{xz}}{\partial z} = \rho \ddot{u}$$

(C.24a)

Repeating this operation in the $y$‑ and $z$‑directions:

$$\frac{\partial \sigma_{yx}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} + \frac{\partial \sigma_{yz}}{\partial z} = \rho \ddot{v}$$

(C.24b)

$$\frac{\partial \sigma_{zx}}{\partial x} + \frac{\partial \sigma_{zy}}{\partial y} + \frac{\partial \sigma_{zz}}{\partial z} = \rho \ddot{w}$$

(C.24c)

Equations (C.24) represent the three‑dimensional equations of motion of an elastic solid. Note that these equations of motion were derived solely based on equilibrium considerations and thus apply to solids of any stress‑strain behavior. To express these equations of motion in terms of displacements, it is again necessary to use a stress‑strain relationship and a strain‑displacement relationship. Using Hooke's law as developed in Section C.2.2.3, the first of the equations of motion [Equation (C.24a)] can be written in terms of strains. Substituting the strain‑displacement relationships

$$\varepsilon_{xx} = \frac{\partial u}{\partial x}, \quad \varepsilon_{xy} = \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}, \quad \varepsilon_{xz} = \frac{\partial u}{\partial z} + \frac{\partial w}{\partial x}$$

into Equation (C.24a) produces the desired equation of motion in terms of displacements:

$$\rho \ddot{u} = (\lambda + \mu) \frac{\partial \varepsilon}{\partial x} + \mu \nabla^2 u$$

(C.26a)

where the Laplacian operator, $\nabla^2$, represents

$$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

Repeating this process in the $y$‑ and $z$‑directions gives

$$\rho \ddot{v} = (\lambda + \mu) \frac{\partial \varepsilon}{\partial y} + \mu \nabla^2 v$$

(C.26b)

$$\rho \ddot{w} = (\lambda + \mu) \frac{\partial \varepsilon}{\partial z} + \mu \nabla^2 w$$

(C.26c)

#### C.2.2.5 Solutions of the Three‑Dimensional Equations of Motion

Together, Equations (C.26) represent the three‑dimensional equations of motion for an isotropic, linear, elastic solid. It turns out that these equations can be manipulated to produce two wave equations. Consequently, only two types of waves can travel through such an unbounded solid. The characteristics of each type of wave will be revealed by their respective wave equations. The solution for the first type of wave can be obtained by differentiating each of Equations (C.26) with respect to $x$, $y$, and $z$ and adding the results together to give

$$(\lambda + 2\mu)\nabla^2\varepsilon = \rho \frac{\partial^2 \varepsilon}{\partial t^2}$$

(C.27)

Rearranging yields the wave equation

$$\frac{\partial^2 \varepsilon}{\partial t^2} = \frac{\lambda + 2\mu}{\rho} \nabla^2 \varepsilon$$

(C.28)

Recalling that $\varepsilon$ is the volumetric strain (which describes deformations that involve contraction/dilation but no shearing or rotation), this wave equation describes an irrotational, or dilatational, wave. It indicates that a dilatational wave will propagate through the body at a velocity

$$v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}}$$

(C.29)

This type of wave is commonly known as a p‑wave (or primary wave) and $v_p$ is referred to as the p‑wave velocity of the material. The general nature of p‑wave motion is illustrated in Figure 2.1a. Note that particle displacements are parallel to the direction of wave propagation, just as they were in the constrained rod of Section C.2.1.1. The longitudinal wave in the constrained rod is actually a p‑wave. Using Equations (C.22c) and (C.22e), $v_p$ can be written in terms of the shear modulus and Poisson's ratio as

$$v_p = \sqrt{\frac{2G(1 - \nu)}{\rho(1 - 2\nu)}}$$

(C.30)

As $\nu$ approaches 0.5 (at which point the body becomes incompressible, i.e., infinitely stiff with respect to dilatational deformations), $v_p$ approaches infinity. To obtain the solution for the second type of wave, $\varepsilon$ is eliminated by differentiating Equation (C.26b) with respect to $z$ and Equation (C.26c) with respect to $y$, and subtracting one from the other:

$$\rho \frac{\partial^2}{\partial t^2}\!\left(\frac{\partial w}{\partial y} - \frac{\partial v}{\partial z}\right) = \mu \nabla^2\!\left(\frac{\partial w}{\partial y} - \frac{\partial v}{\partial z}\right)$$

(C.31)

Recalling the definition of rotation [Equation (C.18)], Equation (C.31) can be written in the form of the wave equation

$$\frac{\partial^2 \Omega_x}{\partial t^2} = \frac{\mu}{\rho} \nabla^2 \Omega_x$$

(C.32)

which describes an equivoluminal, or distortional wave, of rotation about the $x$‑axis. Similar expressions can be obtained by the same process for rotation about the $y$‑ and $z$‑axes. Equation (C.32) shows that a distortional wave will propagate through the solid at a velocity

$$v_s = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{G}{\rho}}$$

(C.33)

This type of wave is commonly known as an s‑wave (or shear wave) and $v_s$ is referred to as the shear wave velocity of the material. Note that the particle motion is constrained to a plane perpendicular to the direction of wave propagation, just as it was in the case of the torsional wave of Section C.2.1.2. Consequently, the torsional wave represented a form of an s‑wave. The close relationship between s‑wave velocity and shear modulus is used to advantage in many of the field and laboratory tests discussed in Chapter 6. The general nature of s‑wave motion is illustrated in Figure 2.1b. S‑waves are often divided into two types, or resolved into two perpendicular components. SH‑waves are s‑waves in which particle motion occurs only in a horizontal plane. SV‑waves are s‑waves whose particle motion lies in a vertical plane. A given s‑wave with arbitrary particle motion can be represented as the vector sum of its SH and SV components. In summary, only two types of waves, known as body waves, can exist in an unbounded (infinite) elastic solid. P‑waves involve no rotation of the material they pass through and travel at velocity, $v_p$. S‑waves involve no volume change and travel at velocity, $v_s$. The velocities of p‑ and s‑waves depend on the stiffnesses of the solid with respect to the types of deformation induced by each wave. Comparing the velocities [Equations (C.30) and (C.33)]

$$\frac{v_p}{v_s} = \sqrt{\frac{2(1 - \nu)}{1 - 2\nu}}$$
