## SLOT 2: Closed-form equations for seismic shear strains derived from the acceleration field

### Kinematic Relation Linking Strain to Displacement and Acceleration

The engineering shear strain at depth $z$ is defined as the horizontal displacement gradient with respect to depth:

$$\gamma(z,t) = \frac{\partial u(z,t)}{\partial z}$$

Because the displacement field satisfies the wave equation, an equivalent integral expression exists that connects shear strain directly to the acceleration field. From the equilibrium equation $\partial \tau / \partial z = \rho\,\partial^2 u / \partial t^2 = \rho\,a(z,t)$, where $\tau = G(z)\,\gamma$ is the shear stress, integration from the free surface (where $\tau = 0$) to depth $z$ yields

$$\tau(z,t) = \rho\!\int_0^z a(\zeta,t)\,d\zeta$$

so that

$$\gamma(z,t) = \frac{\tau(z,t)}{G(z)} = \frac{\rho}{G(z)}\!\int_0^z a(\zeta,t)\,d\zeta$$

[WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: HIGH, Rationale: The integral form $\gamma = \rho/G \cdot \int_0^z a \, d\zeta$ follows directly from integrating the equation of motion from the free surface; it is derived in Dobry et al. (1982) and in the cited paper on seismic shear strains in dams and embankments. The derivation is algebraically straightforward and independent of the specific stiffness profile.]

This expression is particularly useful as a proxy relationship: once the acceleration profile $a(z,t)$ is known from a site response analysis, the shear strain at any depth can be computed without separately solving for displacement.

### Shear Strain for a Uniform Stratum

For the uniform stratum with complex shear modulus $G^* = G_0(1+2iD)$ and wavenumber $k^* = \omega/V_s^*$, the frequency-domain displacement is

$$U(z,\omega) = U_g(\omega)\,\frac{\cos(k^*z)}{\cos(k^*H_s)}$$

Differentiating with respect to $z$:

$$\Gamma(z,\omega) \equiv \frac{\partial U}{\partial z} = -k^*\,U_g(\omega)\,\frac{\sin(k^*z)}{\cos(k^*H_s)}$$

Expressing the base displacement in terms of the base acceleration, $U_g = A_g/(-\omega^2)$:

$$\Gamma(z,\omega) = \frac{k^*}{\omega^2}\,\frac{\sin(k^*z)}{\cos(k^*H_s)}\,A_g(\omega)$$

Since $k^*/\omega^2 = 1/(\omega\,V_s^*)$ and $V_s^{*2} = G^*/\rho$:

$$\Gamma(z,\omega) = \frac{\sin(k^*z)}{\omega\,V_s^*\,\cos(k^*H_s)}\,A_g(\omega) = \frac{\rho\,\sin(k^*z)}{\omega^2\,\rho\,V_s^{*2}/\omega}\,\frac{A_g(\omega)}{\omega}$$

A compact form of the shear strain transfer function $H_\gamma(z,\omega) = \Gamma(z,\omega)/A_g(\omega)$ is therefore

$$H_\gamma(z,\omega) = \frac{\sin(k^*z)}{\omega\,V_s^*\,\cos(k^*H_s)}$$

[WEB:https://www.sciencedirect.com/science/article/pii/S0267726122003773][WEB:https://nheri-simcenter.github.io/TFT-Documentation/theory.html]^[Confidence: HIGH, Rationale: The expression follows by direct differentiation of the displacement transfer function for the uniform layer, which is itself a classical result. The complex wavenumber formulation naturally incorporates damping. The result is algebraically consistent with the stress-integral form derived in the preceding paragraph.]

#### Modal Representation of Shear Strain

In the time domain, using the modal expansion $u(z,t) = \sum_n \phi_n(z)\,q_n(t)$, the shear strain is

$$\gamma(z,t) = \sum_{n=1}^{\infty} \phi_n'(z)\,q_n(t)$$

where $\phi_n'(z) = d\phi_n/dz$. For the uniform layer with $\phi_n(z) = \cos(k_n z)$ and $k_n = (2n-1)\pi/(2H_s)$:

$$\phi_n'(z) = -k_n\,\sin(k_n z)$$

so

$$\gamma(z,t) = -\sum_{n=1}^{\infty} k_n\,\sin(k_n z)\,q_n(t)$$

Each generalized coordinate $q_n(t)$ is the response of an SDOF oscillator at frequency $\omega_n$ driven by $a_g(t)$, as defined in Slot 1. The peak shear strain at depth $z$ under a given ground motion is governed by the modes with largest $|q_n|$ combined with the depth-dependent weight $k_n\,|\sin(k_n z)|$. At the base ($z = H_s$), $\sin(k_n H_s) = \sin((2n-1)\pi/2) = \pm 1$, so all modes contribute with maximum amplitude. At the surface ($z = 0$), all mode shape derivatives vanish, consistent with the zero-stress condition. [WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: HIGH, Rationale: The modal shear strain expression follows by term-by-term differentiation of the modal expansion; the derivative of cosine mode shapes and the boundary behavior at surface and base are straightforward analytical results consistent with the physical boundary conditions.]

### Shear Strain for the Power-Law Stiffness Profile

For the power-law profile $G(\xi) = G_b\,\xi^m$ with $\xi = z/H_s$, the displacement field is

$$U(\xi,\omega) = \frac{U_g(\omega)}{J_q(\lambda)}\,\xi^{(1-m)/2}\,J_q\!\left(\lambda\,\xi^{(2-m)/2}\right)$$

Differentiating with respect to $z = H_s\,\xi$ and using the Bessel function identity $d/dx[x^{-\nu}J_\nu(x)] = -x^{-\nu}J_{\nu+1}(x)$ in reverse, the derivative simplifies to

$$\frac{dU}{dz} = \frac{U_g(\omega)}{H_s\,J_q(\lambda)}\cdot\frac{2-m}{2}\cdot\lambda\cdot\xi^{(1-2m)/2}\,J_{q-1}\!\left(\lambda\,\xi^{(2-m)/2}\right)$$

The closed-form shear strain transfer function for the power-law profile is therefore

$$H_\gamma(\xi,\omega) = \frac{\Gamma(\xi,\omega)}{A_g(\omega)} = \frac{-1}{H_s\,\omega^2}\cdot\frac{(2-m)\,\lambda}{2\,J_q(\lambda)}\cdot\xi^{(1-2m)/2}\,J_{q-1}\!\left(\lambda\,\xi^{(2-m)/2}\right)$$

[WEB:https://www.academia.edu/16861773/1D_harmonic_response_of_layered_inhomogeneous_soil_Analytical_investigation][WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: HIGH, Rationale: The strain expression is obtained by direct differentiation of the Bessel-function displacement solution, using the standard recurrence relation for Bessel functions. The algebra is confirmed by the derivation for shear strain in Gazetas (1985) and the cited paper on seismic shear strains, which present equivalent modal strain expressions for inhomogeneous profiles.]

The depth dependence of the strain amplitude is controlled by the factor $\xi^{(1-2m)/2}\,J_{q-1}(\lambda\,\xi^{(2-m)/2})$. For $m < 1/2$, the exponent $(1-2m)/2 > 0$ so the factor vanishes as $\xi \to 0$ and the surface strain is zero, consistent with the zero-stress condition when $G(0) = 0$ but still finite because the modulus also vanishes. For $m > 1/2$, the exponent $(1-2m)/2 < 0$ and the strain amplitude diverges as $\xi \to 0$ even though surface displacements and accelerations remain finite; this is the analytical signature of an extremely soft surface layer concentrating deformation near the free surface. [WEB:https://www.academia.edu/16861773/1D_harmonic_response_of_layered_inhomogeneous_soil_Analytical_investigation]^[Confidence: HIGH, Rationale: The behavior of the strain factor as $\xi \to 0$ follows from the asymptotics of the Bessel function $J_{q-1}(x) \sim (x/2)^{q-1}/\Gamma(q)$ as $x \to 0$ combined with the power of $\xi$; the paper cited explicitly states that surface strains become infinite for inhomogeneity exponents exceeding 0.5 when the surface stiffness is zero, which is consistent with this analysis.]

#### Modal Strain Expansion for the Power-Law Profile

Using the eigenfunction expansion of the power-law problem, the shear strain can alternatively be written as

$$\gamma(\xi,t) = \sum_{n=1}^{\infty} \phi_n'(\xi)\,q_n(t)$$

where

$$\phi_n'(\xi) = \frac{d\phi_n}{dz}\bigg|_{z=H_s \xi} = \frac{1}{H_s}\,\frac{(2-m)}{2}\,\lambda_n\,\xi^{(1-2m)/2}\,J_{q-1}\!\left(\lambda_n\,\xi^{(2-m)/2}\right)$$

The generalized coordinates satisfy $\ddot{q}_n + 2D\omega_n\dot{q}_n + \omega_n^2 q_n = -\Gamma_n\,a_g(t)$ with the modal participation factor

$$\Gamma_n = \frac{\int_0^{H_s} \rho\,\phi_n\,dz}{\int_0^{H_s} \rho\,\phi_n^2\,dz}$$

evaluated numerically from the Bessel-function mode shapes. The modal shear strain contribution at each depth and each mode is thus controlled by two factors: the mode shape derivative $\phi_n'(\xi)$, which encodes the depth distribution of strain for that mode, and the modal response $q_n(t)$, which captures the frequency content of the input relative to the modal frequency $\omega_n$. [WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: MEDIUM, Rationale: The modal strain expansion follows algebraically from differentiating the eigenfunction expansion, and the participation factor integral is structurally identical to that for the uniform case. However, no closed-form expression for $\Gamma_n$ in terms of Bessel functions was located in the searched sources; the integral must generally be evaluated numerically, which is a minor limitation of this presentation.]

### Influence of Stiffness Profile and Modal Structure on Strain Distribution

The depth distribution of shear strains under seismic excitation is shaped jointly by the stiffness profile $G(z)$ and the modal structure of the acceleration solution. For the uniform layer, strain mode shapes $\phi_n'(z) = -k_n\sin(k_n z)$ increase linearly from zero at the surface to a maximum at $z = H_s$ for the fundamental mode ($n = 1$), with higher modes producing additional zero crossings at intermediate depths. The fundamental mode dominates at low frequencies and produces a strain profile that peaks near the base of the layer.

For the power-law profile, the strain mode shapes involve $J_{q-1}(\lambda_n \xi^{(2-m)/2})$, whose spatial distribution depends sensitively on $m$. As $m$ increases toward 2, the stiffness contrast between surface and base grows, confining higher-frequency energy to progressively shallower depths and amplifying near-surface strains. This is reflected in the factor $\xi^{(1-2m)/2}$: for $m$ close to 2, the exponent $(1-2m)/2$ approaches $-3/2$, producing a strong concentration of strain near the surface. The shear stress $\tau(z,t) = G(z)\,\gamma(z,t)$, by contrast, remains bounded at the surface for all values of $m < 2$, as required by the zero-stress boundary condition. [WEB:https://www.academia.edu/16861773/1D_harmonic_response_of_layered_inhomogeneous_soil_Analytical_investigation][WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: HIGH, Rationale: The discussion of strain depth distribution follows analytically from the mode shape derivatives derived above; the physical interpretation is consistent with the wave propagation principle that energy concentrates in softer zones, as documented in the cited sources on inhomogeneous site response and shear strains in dams and embankments.]

For the proxy model objective of predicting pore pressure increase from a seismic record, the integral form $\gamma(z,t) = (\rho/G(z))\int_0^z a(\zeta,t)\,d\zeta$ is directly actionable: it requires only the acceleration profile $a(\zeta,t)$ and the depth-dependent stiffness $G(z)$, both of which are either measured or prescribed. Under the uniform-layer approximation, this further simplifies to $\gamma(z,t) = (1/V_s^2)\int_0^z a(\zeta,t)\,d\zeta$, expressing the shear strain as a depth-integrated measure of the acceleration field normalized by the elastic wave speed squared. [WEB:https://nheri-simcenter.github.io/TFT-Documentation/theory.html][WEB:https://www.academia.edu/103879197/Seismic_shear_strains_and_seismic_coefficients_in_dams_and_embankments]^[Confidence: HIGH, Rationale: The simplification to $\gamma = (1/V_s^2)\int_0^z a\,d\zeta$ for the uniform layer follows directly from $G_0 = \rho V_s^2$ and the integral equilibrium expression; this form is consistent with the frequency-domain transfer function derived earlier and provides a concise proxy formula for the strain field in terms of the acceleration record.]
