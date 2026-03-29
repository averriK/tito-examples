# Closed-form site response: acceleration field and shear strains for a one-dimensional inhomogeneous stratum

## SLOT 1: Closed-form analytical solutions for the seismic site acceleration response

### Physical Model and Coordinate Convention

A horizontally infinite, fine-grained soil stratum of thickness $H_s$ overlies a rigid or compliant rock half-space and is subjected to a prescribed horizontal acceleration time history $a_g(t)$ applied at the rock-soil interface. The coordinate $z$ is measured upward from the rock-soil interface, so $z = 0$ coincides with the base and $z = H_s$ with the free surface. The depth from the free surface is denoted $\eta = H_s - z$. The soil is treated as a linear viscoelastic material with uniform mass density $\rho$ and a depth-dependent small-strain shear modulus $G(z)$ whose maximum value $G_o \equiv G(0)$ is attained at the base. The base shear wave velocity is $c_o = \sqrt{G_o/\rho}$; the base wavenumber at circular frequency $\omega$ is $k_o = \omega/c_o$.

### Governing Wave Equation and Boundary Conditions

One-dimensional, vertically propagating horizontally polarized shear (SH) waves in the stratum satisfy the equilibrium equation for a horizontal soil slice [@Gazetas1982][@SchnabelEtAl1972]:

$$\rho\,\frac{\partial^2 u}{\partial t^2} = \frac{\partial}{\partial z}\!\left[G(z)\,\frac{\partial u}{\partial z}\right]$$

where $u(z,t)$ is the horizontal displacement. For time-harmonic excitation with $u(z,t) = U(z,\omega)\,e^{i\omega t}$, the equation reduces to the second-order ODE [@Gazetas1982]:

$$\frac{d}{dz}\!\left[G(z)\,\frac{dU}{dz}\right] + \rho\,\omega^2\,U = 0$$

Two boundary conditions close the problem. At the free surface ($z = H_s$, $\eta = 0$), the shear stress vanishes:

$$\left.\frac{dU}{dz}\right|_{z=H_s} = 0$$

At the rock-soil interface ($z = 0$), the displacement matches the prescribed base excitation:

$$U(0,\,\omega) = U_g(\omega)$$

When the underlying rock is treated as a compliant elastic half-space, the base condition is replaced by a radiation condition incorporating the impedance ratio $\alpha_I = \rho c_o/(\rho_r c_r)$ between the stratum and the rock [@Gazetas1982][@DobrEtAl1976]. For profiles where $G(H_s) = 0$ (i.e., $m > 0$ in the power-law family), the modulus vanishes at the free surface and the zero-stress condition is satisfied automatically; the operative surface constraint becomes regularity of the solution, which excludes the singular Bessel-$Y$ component [@Gazetas1982][@RovithisEtAl2011].

### Frequency-Domain Transfer Functions

The acceleration transfer function is defined as $H_a(z,\omega) = A(z,\omega)/A_g(\omega)$, where $A(z,\omega) = -\omega^2 U(z,\omega)$ is the harmonic acceleration amplitude at elevation $z$ and $A_g(\omega) = -\omega^2 U_g(\omega)$ is the base input amplitude. Because the $-\omega^2$ factors cancel identically, the acceleration and displacement transfer functions share the same spatial form: $H_a(z,\omega) = U(z,\omega)/U_g(\omega)$ [@Gazetas1982].

#### Uniform Shear Stiffness

For $G(z) = G_o$ (constant throughout), the governing ODE reduces to $d^2U/dz^2 + k^2 U = 0$ with $k = \omega/c_s$ and $c_s = \sqrt{G_o/\rho}$. Applying zero stress at $z = H_s$ and prescribed displacement at $z = 0$ yields the closed-form transfer function [@DobrEtAl1976][@SchnabelEtAl1972]:

$$H_a(z,\omega) = \frac{\cos(k\,\eta)}{\cos(k\,H_s)}, \qquad \eta = H_s - z$$

At the free surface ($\eta = 0$), this simplifies to the classical surface amplification function $H_a = 1/\cos(kH_s)$. The denominator vanishes at the resonant wavenumbers $k_n H_s = (2n-1)\pi/2$, corresponding to the natural frequencies and mode shapes [@DobrEtAl1976]:

$$f_n = \frac{(2n-1)\,c_s}{4\,H_s}, \qquad \phi_n(\eta) = \cos\!\left[\frac{(2n-1)\pi\,\eta}{2\,H_s}\right], \qquad n = 1, 2, 3, \ldots$$

The fundamental frequency $f_1 = c_s/(4H_s)$ corresponds to the quarter-wavelength resonance condition $H_s = \lambda_1/4$.

The time-domain acceleration field is recovered by modal superposition. Expanding the response as $u(z,t) = \sum_n \phi_n(\eta)\,q_n(t)$, each generalized coordinate satisfies an SDOF equation of motion driven by the base acceleration [@SDEE2022]:

$$\ddot{q}_n + 2\xi\,\omega_n\,\dot{q}_n + \omega_n^2\,q_n = -\Gamma_n\,a_g(t)$$

The modal participation factor for a deposit with uniform density is:

$$\Gamma_n = \frac{\int_0^{H_s} \rho\,\phi_n\,dz}{\int_0^{H_s} \rho\,\phi_n^2\,dz} = \frac{4\,(-1)^{n+1}}{(2n-1)\,\pi}$$

and the total acceleration at any elevation is $a(z,t) = \sum_n \phi_n(\eta)\,\ddot{q}_n(t)$.

#### Linear Shear Modulus Profile (Gibson Deposit)

The Gibson deposit assigns a shear modulus that increases linearly from zero at the free surface to $G_o$ at the base:

$$G(z) = G_o\,\frac{\eta}{H_s}, \qquad \eta = H_s - z$$

Substituting into the governing ODE and using $\eta$ as the independent variable yields $\eta\,U'' + U' + k_o^2 H_s\,U = 0$. The substitution $s = 2k_o\sqrt{H_s\,\eta}$ transforms this into Bessel's equation of order zero. Regularity at the free surface ($\eta \to 0$, $G \to 0$) excludes the $Y_0$ component, and the base boundary condition fixes the amplitude. The resulting transfer function is [@Gazetas1982][@DobrEtAl1976]:

$$H_a(z,\omega) = \frac{J_0\!\left(2k_o\sqrt{H_s\,\eta}\right)}{J_0\!\left(2k_o\,H_s\right)}, \qquad \eta = H_s - z$$

The natural frequencies are governed by the zeros $j_{0,n}$ of $J_0$ ($j_{0,1} \approx 2.405$, $j_{0,2} \approx 5.520$, $j_{0,3} \approx 8.654$):

$$\omega_n = \frac{j_{0,n}\,c_o}{2\,H_s}, \qquad \phi_n(\eta) = J_0\!\left(j_{0,n}\sqrt{\eta/H_s}\right)$$

This case corresponds to $m = 1$ in the general power-law family below.

#### General Power-Law Profile

A power-law shear modulus profile

$$G(z) = G_o\!\left(\frac{\eta}{H_s}\right)^m = G_o\!\left(\frac{H_s - z}{H_s}\right)^m, \qquad 0 < m < 2$$

admits a closed-form Bessel-function solution for any real exponent $m$ in the open interval $(0,2)$. The substitution [@Gazetas1982][@RovithisEtAl2011]:

$$\zeta(\eta) = \frac{2\,k_o\,H_s}{2-m}\left(\frac{\eta}{H_s}\right)^{(2-m)/2}$$

transforms the governing ODE into Bessel's equation of order $\nu = (1-m)/(2-m)$. Excluding the singular $Y_\nu$ component by the regularity condition at $\eta \to 0$ and enforcing the base boundary condition gives the acceleration transfer function [@Gazetas1982][@RovithisEtAl2011]:

$$H_a(z,\omega) = \left(\frac{\eta}{H_s}\right)^{(1-m)/2}\frac{J_\nu\!\left[\zeta(\eta)\right]}{J_\nu\!\left[\zeta(H_s)\right]}, \qquad \eta = H_s - z, \quad \nu = \frac{1-m}{2-m}$$

where $J_\nu$ denotes the Bessel function of the first kind of order $\nu$. The natural frequencies are determined by the zeros $j_{\nu,n}$ of $J_\nu$:

$$\omega_n = \frac{j_{\nu,n}\,(2-m)\,c_o}{2\,H_s}$$

with corresponding mode shapes $\phi_n(\eta) = (\eta/H_s)^{(1-m)/2}\,J_\nu[\zeta_n(\eta)]$, where $\zeta_n$ uses $j_{\nu,n}$ in place of $\zeta(H_s)$. The formula is not applicable at $m = 0$, for which the zero-stress boundary condition must be applied explicitly at the non-singular free surface, yielding the trigonometric transfer function of the uniform stratum [@Gazetas1982]. At $m = 1$ ($\nu = 0$), the general formula reduces identically to the Gibson transfer function.

### Layered Stratum: Thomson-Haskell Transfer Matrix

For a stratum composed of $N$ horizontal sublayers, each homogeneous, the displacement and stress state at the bottom of any layer is related to the state at its top by the layer propagator matrix. For layer $j$ of thickness $h_j$, complex shear wave velocity $V_{sj}^*$, and wavenumber $k_j^* = \omega/V_{sj}^*$, the propagator matrix is [@SDEE2022]:

$$\mathbf{P}_j = \begin{pmatrix} \cos(k_j^* h_j) & \sin(k_j^* h_j)/(G_j^* k_j^*) \\ -G_j^* k_j^*\,\sin(k_j^* h_j) & \cos(k_j^* h_j) \end{pmatrix}$$

The global transfer is obtained by multiplying layer matrices: $\mathbf{P} = \mathbf{P}_1\,\mathbf{P}_2\,\cdots\,\mathbf{P}_N$. The surface-to-base acceleration transfer function follows from the $(1,1)$ element of $\mathbf{P}$ combined with the free-surface and base boundary conditions. This approach constitutes the standard discretized implementation of the closed-form layer solutions and converges to the continuous analytical formulas as sublayer thickness approaches zero.

### Material Damping and Equivalent-Linear Extension

Material damping is incorporated by replacing the real shear modulus $G(z)$ with the complex modulus $G^*(z) = G(z)(1 + 2i\xi)$, where $\xi$ is the hysteretic damping ratio, assumed depth-uniform for simplicity. The wavenumber becomes complex, $k^* \approx k(1-i\xi)$ for $\xi \ll 1$, and all transfer functions remain valid under the substitution $k_o \to k_o^*$. The resonant poles acquire finite imaginary parts, bounding amplification at resonance to values proportional to $1/(2\xi)$ for small $\xi$ [@SchnabelEtAl1972][@RovithisEtAl2011].

The equivalent-linear method extends this viscoelastic framework to approximate nonlinear soil behavior by iterating between the frequency-domain solution and strain-compatible values of $G$ and $\xi$ obtained from modulus reduction and damping curves at each depth [@SchnabelEtAl1972]. The closed-form transfer functions apply without modification within each iteration, because the soil is treated as linear viscoelastic during that pass.

### Key Controlling Parameters

The acceleration response $a(z,t)$ is governed by five primary parameter groups: (1) stratum thickness $H_s$, which sets the resonant frequency scale through $f_n \propto c_o/H_s$; (2) base shear wave velocity $c_o = \sqrt{G_o/\rho}$ and mass density $\rho$; (3) stiffness profile exponent $m$, which controls the Bessel order $\nu = (1-m)/(2-m)$, the mode shapes, and the distribution of modal energy with depth; (4) hysteretic damping ratio $\xi$, which governs peak amplification at resonance; and (5) base impedance ratio $\alpha_I = \rho c_o/(\rho_r c_r)$, which determines the fraction of seismic energy reflected back into the stratum and modifies resonant amplitudes when the base is compliant [@Gazetas1982][@DobrEtAl1976].

---

## SLOT 2: Closed-form equations for seismic shear strains derived from the acceleration field

The shear strain field $\gamma(z,t)$ is derived from the acceleration transfer functions established above by differentiation of the displacement field with respect to $z$, or equivalently by vertical integration of the equation of motion from the free surface. All notation -- $z$, $\eta = H_s - z$, $G_o$, $c_o$, $k_o$, $\nu$, $\zeta(\eta)$ -- carries over from Slot 1 without redefinition.

### Kinematic Definition and Exact Integral Representation

The engineering shear strain at any elevation $z$ is defined by the horizontal displacement gradient with respect to the vertical coordinate:

$$\gamma(z,t) = \frac{\partial u(z,t)}{\partial z}$$

An exact, model-independent relationship between $\gamma(z,t)$ and the acceleration field is obtained by integrating the equation of motion vertically from elevation $z$ to the free surface $H_s$. Applying the zero-stress free-surface condition $\tau(H_s,t) = 0$ yields [@RovithisEtAl2011]:

$$\gamma(z,t) = -\frac{\rho}{G(z)}\int_z^{H_s} a(z',t)\,dz'$$

Equivalently, in terms of depth from the free surface $\eta = H_s - z$:

$$\gamma(\eta,t) = \frac{\rho}{G(\eta)}\int_0^{\eta} a(\eta',t)\,d\eta'$$

Multiplying both sides by $G(z)$ gives the shear stress profile [@RovithisEtAl2011]:

$$\tau(z,t) = G(z)\,\gamma(z,t) = -\rho\int_z^{H_s} a(z',t)\,dz'$$

The shear stress at any level is governed exclusively by the inertia of the overlying soil mass and is independent of the specific form of $G(z)$. This property is an exact consequence of the equation of motion and holds for any differentiable stiffness profile.

### Shear Strain for the Uniform Stratum

For $G(z) = G_o$ (constant), the integral representation reduces immediately to:

$$\gamma(\eta,t) = \frac{1}{c_s^2}\int_0^{\eta} a(\eta',t)\,d\eta', \qquad c_s = \sqrt{G_o/\rho}$$

The equivalent frequency-domain expression is obtained by differentiating $U(z,\omega) = U_g\cos(k\eta)/\cos(kH_s)$ with respect to $z$ (noting $dU/dz = -dU/d\eta$) [@DobrEtAl1976][@SchnabelEtAl1972]:

$$\Gamma(z,\omega) = \frac{dU}{dz} = \frac{k\,U_g\,\sin(k\eta)}{\cos(kH_s)}$$

Substituting $U_g = -A_g/\omega^2$ and using $k/\omega^2 = 1/(c_s\omega)$, the shear strain transfer function becomes:

$$H_\gamma(z,\omega) = \frac{\Gamma(z,\omega)}{A_g(\omega)} = -\frac{\sin(k\,\eta)}{c_s\,\omega\,\cos(k\,H_s)}, \qquad \eta = H_s - z$$

The spatial distribution is governed by $\sin(k\eta)$, which is zero at the free surface ($\eta = 0$) -- consistent with the zero-stress boundary condition -- and attains its maximum amplitude near the base at each resonant frequency. This distribution is 90 degrees out of phase with the acceleration mode shapes $\cos(k_n\eta)$: the $n$-th mode contributes maximum acceleration at the free surface but maximum strain nearer the base [@DobrEtAl1976].

In the time domain, differentiating the modal expansion $u(z,t) = \sum_n \phi_n(\eta)\,q_n(t)$ with $\phi_n(\eta) = \cos(k_n\eta)$ with respect to $z$:

$$\gamma(z,t) = \sum_{n=1}^{\infty} k_n\,\sin(k_n\,\eta)\,q_n(t), \qquad \eta = H_s - z$$

where $k_n = (2n-1)\pi/(2H_s)$ and $q_n(t)$ is the SDOF modal response defined in Slot 1. At the base ($\eta = H_s$), $\sin(k_n H_s) = \pm 1$ and all modes contribute with maximum amplitude; at the free surface ($\eta = 0$), all modal strain contributions vanish [@GazetasDakoulas1985].

### Shear Strain for the Linear (Gibson) Profile

For the linear profile $G(z) = G_o\,\eta/H_s$ with $\eta = H_s - z$, differentiating $U(\eta,\omega) = U_g\,J_0(2k_o\sqrt{H_s\,\eta})/J_0(2k_oH_s)$ with respect to $z$ and applying the Bessel identity $dJ_0(x)/dx = -J_1(x)$ together with the chain rule gives [@Gazetas1982]:

$$\Gamma(z,\omega) = \frac{dU}{dz} = U_g\,k_o\sqrt{\frac{H_s}{\eta}}\,\frac{J_1\!\left(2k_o\sqrt{H_s\,\eta}\right)}{J_0(2k_o H_s)}, \qquad \eta = H_s - z$$

Substituting $U_g = -A_g/\omega^2$ and $k_o/\omega^2 = 1/(c_o\omega)$:

$$H_\gamma(z,\omega) = -\frac{1}{c_o\,\omega}\sqrt{\frac{H_s}{\eta}}\,\frac{J_1\!\left(2k_o\sqrt{H_s\,\eta}\right)}{J_0(2k_o H_s)}, \qquad \eta = H_s - z$$

The factor $\sqrt{H_s/\eta}$ reflects a geometric amplification of strain as the free surface is approached ($\eta \to 0$). As $\eta \to 0$, the shear modulus $G \to 0$ while the shear stress $\tau = G\gamma$ remains bounded (because $J_1(x) \to x/2$ as $x \to 0$, so the product $\sqrt{H_s/\eta}\cdot J_1(2k_o\sqrt{H_s\eta}) \to k_o H_s$ -- finite); nevertheless, the strain itself diverges in the linearized model at the free surface for this profile.

### Shear Strain for the General Power-Law Profile

For the power-law profile $G(z) = G_o(\eta/H_s)^m$ with $0 < m < 2$ and $\eta = H_s - z$, the displacement transfer function is given by the Bessel formula of Slot 1. Differentiating with respect to $z$ (equivalently $-d/d\eta$) and applying the Bessel recurrence relation $J_\nu'(\zeta) = J_{\nu-1}(\zeta) - (\nu/\zeta)J_\nu(\zeta)$, the $J_\nu$ term in the resulting expression cancels identically -- a consequence of the algebraic identity between the power prefactor exponent $\alpha = (1-m)/2$ and the Bessel order $\nu = (1-m)/(2-m)$ -- leaving a single Bessel term of order $\nu - 1$ [@Gazetas1982][@RovithisEtAl2011]:

$$H_\gamma(z,\omega) = \frac{\Gamma(z,\omega)}{A_g(\omega)} = \frac{1}{c_o\,\omega}\left(\frac{\eta}{H_s}\right)^{(1-2m)/2}\frac{J_{\nu-1}\!\left[\zeta(\eta)\right]}{J_\nu\!\left[\zeta(H_s)\right]}, \qquad \eta = H_s - z$$

where

$$\zeta(\eta) = \frac{2\,k_o\,H_s}{2-m}\left(\frac{\eta}{H_s}\right)^{(2-m)/2}, \qquad \nu = \frac{1-m}{2-m}, \qquad k_o = \frac{\omega}{c_o}$$

Internal consistency is confirmed at $m = 1$: the Bessel order reduces to $\nu - 1 = -1$, $J_{-1} = -J_1$, $\zeta(\eta) = 2k_o\sqrt{H_s\,\eta}$, and the prefactor becomes $\sqrt{H_s/\eta}$, reproducing the linear-profile formula with correct sign [@Gazetas1982][@RovithisEtAl2011].

The depth dependence of the strain amplitude is controlled by the power-law factor $(\eta/H_s)^{(1-2m)/2}$. For $m > 1/2$, the exponent $(1-2m)/2 < 0$ and this factor amplifies toward the free surface ($\eta \to 0$), producing a near-surface strain concentration. For $m < 1/2$, the exponent is positive and the algebraic factor decays toward the surface; whether the net strain increases or decreases near the surface depends additionally on the frequency-dependent Bessel term.

### Depth Distribution and Influence of the Stiffness Profile

The depth distribution of shear strains is shaped jointly by the stiffness profile $G(z)$ and the modal structure of the acceleration solution. For the uniform layer, the strain modes $\sin(k_n\eta)$ are 90 degrees out of phase with the acceleration modes $\cos(k_n\eta)$; the fundamental mode therefore contributes maximum strain nearer the base, while higher modes introduce additional zero-crossings at intermediate depths [@DobrEtAl1976].

For non-uniform profiles with $m > 0$, the algebraic prefactor $(\eta/H_s)^{(1-2m)/2}$ modulates the Bessel contribution with depth. As $m$ increases toward 2, the stiffness contrast between base and surface grows and near-surface strain concentration intensifies. The shear stress $\tau(z,t) = G(z)\,\gamma(z,t)$ remains bounded at the free surface for all $m < 2$, as required by the zero-stress boundary condition, even when the strain itself diverges algebraically for $m \geq 1/2$ [@Gazetas1982][@RovithisEtAl2011].

For applications that require the strain field from a known acceleration profile, the integral form provides a direct computational path. For the uniform layer, this yields:

$$\gamma(\eta,t) = \frac{1}{c_s^2}\int_0^\eta a(\eta',t)\,d\eta'$$

which expresses the shear strain as a depth-integrated measure of the acceleration field normalized by the square of the elastic wave velocity, directly applicable when the acceleration record is available from site response analysis or measurement [@SimCenterTFT2023][@GazetasDakoulas1985].
