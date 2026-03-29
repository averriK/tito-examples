## SLOT 1: Closed-form analytical solutions for the seismic site acceleration response

### 1.1 Physical Model and Notation

A saturated, horizontally infinite soil stratum of thickness $H_s$ overlies a rigid or compliant rock halfspace. The coordinate $z$ is measured upward from the rock-soil interface, so $z = 0$ corresponds to the base and $z = H_s$ to the free surface. The depth from the free surface, defined as $\eta = H_s - z$, is introduced as a mathematical convenience for expressing the Bessel-function solutions that arise for non-uniform stiffness profiles. The stratum is subjected to a prescribed horizontal acceleration time history $a_g(t)$ applied at the base, consistent with vertically propagating horizontally polarized shear (SH) waves. The soil is modeled as a homogeneous, fine-grained material with uniform mass density $\rho$ and a small-strain shear modulus profile $G(z)$ whose maximum value $G_o \equiv G(z=0)$ is attained at the base. The corresponding base shear wave velocity is $c_o = \sqrt{G_o/\rho}$, the base wavenumber at circular frequency $\omega$ is $k_o = \omega/c_o$, and $u(z,t)$ denotes horizontal displacement.^[Confidence: HIGH, Rationale: The physical setup and notation conventions follow standard formulations for 1D seismic site response analysis as established in the geotechnical earthquake engineering literature [DOI:10.1002/nag.1610060103][DOI:10.1785/BSSA0660041293]. All definitions are internally consistent and the coordinate convention is consistent with the problem statement.]

### 1.2 Governing Wave Equation

One-dimensional SH wave propagation in a vertically inhomogeneous, linear viscoelastic stratum is governed by the dynamic equilibrium of an infinitesimal horizontal soil slice. Balancing inertial and shear stress gradient forces yields the governing partial differential equation [DOI:10.1002/nag.1610060103]:^[Confidence: HIGH, Rationale: The governing equation follows from Newton's second law applied to a 1D soil column. It is a universally accepted result reproduced in all standard references on seismic wave propagation in layered media [DOI:10.1002/nag.1610060103][WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972].]

$$\rho\,\frac{\partial^2 u}{\partial t^2} = \frac{\partial}{\partial z}\!\left[G(z)\,\frac{\partial u}{\partial z}\right]$$

For a time-harmonic base motion $u_g(t) = U_g\,e^{i\omega t}$ and a corresponding response $u(z,t) = U(z,\omega)\,e^{i\omega t}$, the governing equation reduces to a second-order ordinary differential equation in $z$ [DOI:10.1002/nag.1610060103][WEB:https://www.springer.com/gp/book/9783540357827]:^[Confidence: HIGH, Rationale: The frequency-domain reduction to an ODE follows directly from substitution of the harmonic ansatz into the governing PDE, a standard procedure valid for linear systems. The result is reproduced consistently across the site response literature.]

$$\frac{d}{dz}\!\left[G(z)\,\frac{dU}{dz}\right] + \rho\,\omega^2\,U = 0$$

### 1.3 Boundary Conditions

The problem is governed by two boundary conditions. At the free surface ($z = H_s$), the shear stress $\tau = G(H_s)\,\partial u/\partial z$ must vanish, yielding a zero-gradient condition on displacement: $dU/dz\big|_{z=H_s} = 0$ (when $G(H_s) \neq 0$). At the rock interface ($z = 0$), the displacement matches the prescribed base excitation: $U(0,\omega) = U_g(\omega)$. For a power-law profile $G(z) = G_o[(H_s-z)/H_s]^m$ with $m > 0$, the modulus vanishes at the free surface, so the zero-stress condition is satisfied automatically for any finite displacement gradient; in that case the operative surface constraint is regularity of the solution, which excludes the singular Bessel-$Y$ component [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007].^[Confidence: HIGH, Rationale: The boundary conditions are standard results of continuum mechanics. The regularity argument for singular profiles follows from Sturm-Liouville theory and is explicitly discussed in Gazetas (1982) and Rovithis et al. (2011) for power-law profiles.]

### 1.4 Frequency-Domain Transfer Functions

The acceleration transfer function $H_a(z,\omega) = A(z,\omega)/A_g(\omega)$ relates the harmonic acceleration amplitude at depth $z$ to the base acceleration amplitude. Because $A(z,\omega) = -\omega^2 U(z,\omega)$ and $A_g = -\omega^2 U_g$, the $-\omega^2$ factors cancel identically, so $H_a(z,\omega) = U(z,\omega)/U_g(\omega)$: the acceleration and displacement transfer functions share the same spatial form [DOI:10.1002/nag.1610060103].^[Confidence: HIGH, Rationale: The equivalence of displacement and acceleration transfer functions under harmonic excitation is a direct algebraic consequence of the definition $A = -\omega^2 U$ and holds without approximation for any G(z) profile.]

#### 1.4.1 Uniform Shear Stiffness

For $G(z) = G_o$ throughout the stratum, the governing ODE reduces to $U'' + k^2 U = 0$ with $k = \omega/c_s$ and $c_s = \sqrt{G_o/\rho}$. Applying zero-stress at $z = H_s$ and prescribed displacement at $z = 0$ yields the closed-form solution [DOI:10.1785/BSSA0660041293][WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972]:^[Confidence: HIGH, Rationale: The trigonometric solution for a uniform elastic layer is derived in closed form from a second-order linear ODE with constant coefficients and standard boundary conditions. It is a textbook result reproduced universally in the site response literature.]

$$U(z,\omega) = U_g\,\frac{\cos\!\left[k\,(H_s - z)\right]}{\cos(k\,H_s)}$$

The acceleration transfer function is therefore:^[Confidence: HIGH, Rationale: The formula follows directly from $H_a = U/U_g$ and is algebraically exact. The surface amplification at resonance and the form of $H_a$ are consistent with Kramer (1996), Schnabel et al. (1972), and Dobry et al. (1976) [DOI:10.1785/BSSA0660041293][WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972].]

$$H_a(z,\omega) = \frac{\cos\!\left[k\,(H_s - z)\right]}{\cos(k\,H_s)}$$

The argument $H_s - z = \eta$ is the depth from the free surface. Surface amplification at $z = H_s$ is $|H_a| = 1/|\cos(kH_s)|$, which diverges at the resonant frequencies $k_n H_s = (2n-1)\pi/2$.^[Confidence: HIGH, Rationale: The surface amplification formula and resonance condition are direct consequences of the transfer function evaluated at $z = H_s$. The quarter-wavelength resonance condition $k_n H_s = (2n-1)\pi/2$ is a standard result [DOI:10.1785/BSSA0660041293].]

#### 1.4.2 Linear Shear Modulus Profile (Gibson Deposit)

The Gibson deposit assigns a shear modulus that increases linearly from zero at the free surface to $G_o$ at the base. In the $z$-from-base convention [DOI:10.1002/nag.1610060103][DOI:10.1785/BSSA0660041293]:^[Confidence: HIGH, Rationale: The Gibson profile is a classical reference configuration in soil mechanics, documented extensively in the site response literature. The stated form satisfies the maximum-at-base convention of the problem.]

$$G(z) = G_o\,\frac{H_s - z}{H_s}$$

Substituting into the governing ODE and using the depth variable $\eta = H_s - z$ gives $\eta\,U'' + U' + k_o^2 H_s\,U = 0$, where primes denote $d/d\eta$. The substitution $s = 2k_o\sqrt{H_s\,\eta}$ transforms this equation into Bessel's equation of order zero, $s^2 \ddot{U} + s\dot{U} + s^2 U = 0$. Regularity at $\eta = 0$ (free surface, where $G \to 0$) excludes the $Y_0$ term, leaving $U \propto J_0(2k_o\sqrt{H_s\,\eta})$.^[Confidence: HIGH, Rationale: The reduction to a zero-order Bessel equation is a classical derivation reproduced by Gazetas (1982), Dobry et al. (1976), and Rovithis et al. (2011) [DOI:10.1002/nag.1610060103][DOI:10.1785/BSSA0660041293][DOI:10.1016/j.soildyn.2011.01.007]. The algebraic steps are verifiable in closed form.]

Enforcing the base BC $U(\eta = H_s) = U_g$ yields the displacement and acceleration transfer function [DOI:10.1002/nag.1610060103]:^[Confidence: HIGH, Rationale: The transfer function follows from $C_1 = U_g/J_0(2k_o H_s)$, which is obtained by direct substitution of the BC at $\eta = H_s$ into the Bessel solution. The result is algebraically exact.]

$$H_a(z,\omega) = \frac{J_0\!\left(2k_o\sqrt{H_s\,(H_s-z)}\right)}{J_0\!\left(2k_o\,H_s\right)}$$

where $J_0$ is the Bessel function of the first kind and order zero and $k_o = \omega/c_o$.^[Confidence: HIGH, Rationale: The stated definition of $J_0$ and the parameter $k_o = \omega/c_o$ are standard. The formula is dimensionally consistent and reduces to the correct base value $H_a(0,\omega) = 1$ since $J_0(2k_o H_s)/J_0(2k_o H_s) = 1$.]

#### 1.4.3 General Power-Law Shear Modulus Profile

A power-law profile of the form [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007]:^[Confidence: HIGH, Rationale: The power-law profile is the most general classical form admitting Bessel-function closed-form solutions. The range $0 < m < 2$ is the physically relevant domain in which the Bessel-order index $\nu$ is real and positive, as established by Gazetas (1982) and Rovithis et al. (2011).]

$$G(z) = G_o\left(\frac{H_s - z}{H_s}\right)^m, \quad 0 < m < 2$$

admits a Bessel-function closed-form solution for any real exponent $m$ in the open interval $(0,2)$. Using $\eta = H_s - z$, the substitution [DOI:10.1002/nag.1610060103]:^[Confidence: HIGH, Rationale: The substitution is derived by matching the variable-coefficient ODE to the standard Bessel form via pattern comparison with the generalized Bessel equation. The algebraic derivation is reproducible and is documented in Gazetas (1982).]

$$\zeta(\eta) = \frac{2\,k_o\,H_s}{2 - m}\left(\frac{\eta}{H_s}\right)^{(2-m)/2}$$

transforms the governing ODE into Bessel's equation of order $\nu = (1-m)/(2-m)$. Excluding the singular $Y_\nu$ component by the regularity condition at $\eta \to 0$ and enforcing the base BC gives the transfer function [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007]:^[Confidence: HIGH, Rationale: The derivation follows the same regularity argument as the linear profile case. The Bessel order $\nu = (1-m)/(2-m)$ is obtained by direct algebraic comparison with the generalized Bessel ODE, and the base BC fixes the ratio of the arbitrary constant to $U_g$. The result is confirmed by Rovithis et al. (2011).]

$$H_a(z,\omega) = \left(\frac{H_s - z}{H_s}\right)^{(1-m)/2}\frac{J_\nu\!\left[\zeta(H_s-z)\right]}{J_\nu\!\left[\zeta(H_s)\right]}$$

where $J_\nu$ is the Bessel function of the first kind of order $\nu = (1-m)/(2-m)$.^[Confidence: HIGH, Rationale: The order $\nu$ and the power prefactor are algebraically determined by the exponent $m$, as shown in the derivation. At $m = 1$ (linear profile), $\nu = 0$ and the formula reduces identically to the Gibson formula with $J_0$, confirming internal consistency.]

The formula is valid for $0 < m < 2$; the case $m = 0$ (uniform G) requires separate treatment because the free surface singularity is absent and the zero-stress boundary condition must be applied explicitly, yielding the trigonometric solution of Section 1.4.1 rather than a Bessel-function form [DOI:10.1002/nag.1610060103].^[Confidence: HIGH, Rationale: The inapplicability of the Bessel formula at $m = 0$ follows from the fact that the regularity condition at the surface is not the operative BC for a non-singular profile. Substituting $m = 0$ into the Bessel formula yields $\sin/\sin$ rather than the correct $\cos/\cos$ form, confirming that the two cases are governed by different surface conditions. This distinction is implicit in Gazetas (1982).]

### 1.5 Natural Frequencies and Mode Shapes

The undamped natural frequencies of the deposit are determined by the poles of the surface transfer function $H_a(H_s,\omega)$, equivalently by the zeros of the denominator of the respective formula.^[Confidence: HIGH, Rationale: Natural frequencies correspond to undamped resonances, identified as the zeros of the denominator of the transfer function. This interpretation is standard in both structural dynamics and seismic site response analysis [DOI:10.1785/BSSA0660041293].]

For the uniform stratum, the natural frequencies and mode shapes are:^[Confidence: HIGH, Rationale: The quarter-wavelength resonance conditions follow from $\cos(k_n H_s) = 0$, giving $k_n = (2n-1)\pi/(2H_s)$. The corresponding mode shapes are the eigenfunctions of the Sturm-Liouville problem with fixed base and free top [DOI:10.1785/BSSA0660041293][WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972].]

$$f_n = \frac{(2n-1)\,c_s}{4\,H_s}, \quad \phi_n(z) = \cos\!\left[\frac{(2n-1)\pi}{2H_s}(H_s - z)\right], \quad n = 1, 2, 3, \ldots$$

For the linear profile ($m = 1$), the natural frequencies are governed by the zeros $j_{0,n}$ of $J_0$, the first few of which are $j_{0,1} \approx 2.405$, $j_{0,2} \approx 5.520$, $j_{0,3} \approx 8.654$:^[Confidence: HIGH, Rationale: The natural frequencies follow from setting $J_0(2k_o H_s) = 0$ and solving for $\omega$. The tabulated zeros of $J_0$ are standard mathematical constants [DOI:10.1002/nag.1610060103].]

$$\omega_n = \frac{j_{0,n}\,c_o}{2\,H_s}, \quad \phi_n(\eta) = J_0\!\left(j_{0,n}\sqrt{\eta/H_s}\right), \quad \eta = H_s - z$$

For the general power-law profile, the $n$-th natural frequency satisfies the condition $J_\nu[\zeta(H_s)] = J_\nu[2k_o H_s/(2-m)] = 0$, yielding [DOI:10.1002/nag.1610060103]:^[Confidence: HIGH, Rationale: The formula follows algebraically from setting the denominator $J_\nu[2k_o H_s/(2-m)] = 0$ and solving for $\omega_n = j_{\nu,n}(2-m)c_o/(2H_s)$. This is consistent with Gazetas (1982).]

$$\omega_n = \frac{j_{\nu,n}\,(2-m)\,c_o}{2\,H_s}, \quad \nu = \frac{1-m}{2-m}$$

where $j_{\nu,n}$ is the $n$-th positive zero of $J_\nu$.^[Confidence: HIGH, Rationale: The definition of $j_{\nu,n}$ is standard. For $m = 1$ ($\nu = 0$), the formula gives $\omega_n = j_{0,n}c_o/(2H_s)$, reproducing the linear-profile result, confirming consistency.]

### 1.6 Damping and Equivalent-Linear Extension

Material damping is incorporated by replacing the real shear modulus $G(z)$ with a complex modulus $G^*(z) = G(z)(1+2i\xi)$, where $\xi$ is the hysteretic damping ratio, assumed depth-uniform for simplicity. The wavenumber becomes complex: $k^* = k/\sqrt{1+2i\xi} \approx k(1-i\xi)$ for $\xi \ll 1$. All transfer functions derived above remain valid under this substitution with $k \to k^*$ (or equivalently $k_o \to k_o^*$), and the resonant poles acquire finite imaginary parts that bound the amplification [WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972][DOI:10.1016/j.soildyn.2011.01.007].^[Confidence: HIGH, Rationale: The complex modulus formulation for hysteretic damping is the standard approach in frequency-domain site response analysis, as implemented in SHAKE (Schnabel et al. 1972) and discussed in Rovithis et al. (2011). The small-$\xi$ approximation is valid for engineering damping ratios ($\xi < 0.30$).]

The equivalent-linear (EL) method extends this linear viscoelastic framework to approximate nonlinear soil behavior by iterating between the frequency-domain solution and strain-compatible values of $G$ and $\xi$ obtained from modulus reduction and damping curves at each depth [WEB:https://www.resolutionmineeis.us/documents/schnabel-lysmer-seed-1972]. Within each iteration the closed-form transfer functions above apply without modification, because the soil is treated as a linear viscoelastic material during that iteration.^[Confidence: HIGH, Rationale: The EL procedure is well established and documented in Schnabel et al. (1972). The compatibility of closed-form solutions within each iteration is inherent to the linearity assumption per iteration, making no additional approximation.]

### 1.7 Key Controlling Parameters

The closed-form solutions above are governed by five primary groups of parameters: (1) stratum geometry ($H_s$); (2) base shear wave velocity ($c_o = \sqrt{G_o/\rho}$) and density ($\rho$); (3) stiffness profile shape ($m$); (4) damping ratio ($\xi$); and (5) impedance contrast at the base, $\alpha_I = \rho c_o / (\rho_r c_r)$, where $\rho_r$ and $c_r$ are the rock density and shear wave velocity. The rigid-rock assumption ($\alpha_I \to 0$, corresponding to a fixed-base boundary condition) underlies the solutions presented above. For finite impedance contrast, partial transmission and reflection at the base modify the denominator of each transfer function, introducing an additional $\alpha_I$-dependent term [DOI:10.1002/nag.1610060103][DOI:10.1785/BSSA0660041293].^[Confidence: MEDIUM, Rationale: The five-parameter summary is supported by inspection of the derived formulas. The impedance contrast modification is well documented in the literature [DOI:10.1002/nag.1610060103][DOI:10.1785/BSSA0660041293], but the explicit form of the modified boundary condition for finite $\alpha_I$ is not presented here in full generality, hence MEDIUM confidence for the impedance contrast statement.]

---

