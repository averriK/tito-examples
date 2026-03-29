## SLOT 2: Closed-form equations for seismic shear strains derived from the acceleration field

### 2.1 Kinematic Relationship and Integral Representation

The engineering shear strain at any depth $z$ in the 1D model is defined by the horizontal displacement gradient with respect to the vertical coordinate:^[Confidence: HIGH, Rationale: The kinematic definition of shear strain as the vertical gradient of horizontal displacement is a fundamental result of continuum mechanics and is universally applicable to the 1D SH wave problem.]

$$\gamma(z,t) = \frac{\partial u(z,t)}{\partial z}$$

An exact, model-independent relationship between $\gamma(z,t)$ and the acceleration field is obtained by integrating the equation of motion vertically from depth $z$ to the free surface $H_s$. Applying the zero-stress free surface condition $\tau(H_s,t) = 0$ yields [DOI:10.1016/j.soildyn.2011.01.007]:^[Confidence: HIGH, Rationale: The integral representation is derived analytically by direct integration of the equation of motion, without approximation, beyond the 1D assumption. It holds for any differentiable $G(z)$ and is implicit in Rovithis et al. (2011).]

$$\gamma(z,t) = -\frac{\rho}{G(z)}\int_z^{H_s} a(z',t)\,dz'$$

This result holds for any stiffness profile $G(z)$. Multiplying both sides by $G(z)$ gives the shear stress profile:^[Confidence: HIGH, Rationale: The shear stress result follows by multiplying both sides of the strain formula by $G(z)$, giving $\tau(z,t) = -\rho\int_z^{H_s}a(z',t)dz'$, which is independent of $G(z)$. This is an exact consequence of the equation of motion.]

$$\tau(z,t) = G(z)\,\gamma(z,t) = -\rho\int_z^{H_s} a(z',t)\,dz'$$

The shear stress at any level $z$ is therefore governed exclusively by the inertia of the overlying soil mass and is independent of the specific form of $G(z)$.^[Confidence: HIGH, Rationale: The G-independence of the shear stress profile is a direct corollary of the exact integral formula above, representing the total inertial force per unit area acting on the soil column between $z$ and $H_s$. This is a well-known result in structural dynamics applied to continuous shear beams.]

### 2.2 Shear Strain for Uniform Stiffness

For $G(z) = G_o$ (constant), the integral representation reduces immediately to a depth-weighted acceleration integral:^[Confidence: HIGH, Rationale: The simplification for uniform $G$ is algebraically direct: $\rho/G_o = 1/c_s^2$. The result is consistent with the frequency-domain formula obtained by differentiating $U(z,\omega)$ with respect to $z$ [DOI:10.1785/BSSA0660041293].]

$$\gamma(z,t) = -\frac{1}{c_s^2}\int_z^{H_s} a(z',t)\,dz'$$

The equivalent frequency-domain expression is obtained by differentiating $U(z,\omega) = U_g\cos[k(H_s-z)]/\cos(kH_s)$ with respect to $z$:^[Confidence: HIGH, Rationale: The differentiation is algebraically trivial. The result is equivalent to the integral representation and is derivable from first principles consistent with Dobry et al. (1976) [DOI:10.1785/BSSA0660041293].]

$$\Gamma(z,\omega) = \frac{dU}{dz} = U_g\,\frac{k\,\sin[k(H_s-z)]}{\cos(kH_s)}$$

Substituting $U_g = -A_g/\omega^2$ and $k/\omega^2 = 1/(c_s\,\omega)$, the strain transfer function becomes:^[Confidence: HIGH, Rationale: The substitution is algebraically straightforward. The resulting formula gives $\Gamma(H_s,\omega) = 0$ (zero strain at the free surface, consistent with zero shear stress BC) and $\Gamma(0,\omega) \propto \sin(kH_s)$ (maximum strain near the base at mid-frequency), which is physically correct.]

$$\Gamma(z,\omega) = -\frac{A_g}{c_s\,\omega}\,\frac{\sin[k(H_s-z)]}{\cos(kH_s)}$$

The strain spatial distribution is governed by $\sin[k(H_s-z)]$, which is zero at the free surface ($z = H_s$) and attains its largest value at the base ($z = 0$) near each resonant frequency. This is 90 degrees out of phase with the acceleration mode shapes $\cos[k_n(H_s-z)]$: the $n$-th mode contributes maximum acceleration at the free surface but maximum strain nearer the base [DOI:10.1785/BSSA0660041293].^[Confidence: HIGH, Rationale: The modal phase relationship between acceleration (cosine modes) and strain (sine modes) follows directly from differentiation of the displacement modes. The observation that strain peaks nearer the base while acceleration peaks at the surface is a well-supported result of the uniform shear beam model.]

### 2.3 Shear Strain for the Linear Profile

For the linear profile $G(z) = G_o(H_s-z)/H_s$ and using $\eta = H_s - z$, the displacement is $U(\eta) = U_g J_0(2k_o\sqrt{H_s\,\eta})/J_0(2k_o H_s)$. Differentiating with respect to $z$ (equivalently $-d/d\eta$) and applying the standard Bessel identity $J_0'(x) = -J_1(x)$ together with the chain rule gives [DOI:10.1002/nag.1610060103]:^[Confidence: HIGH, Rationale: The differentiation uses the Bessel identity $dJ_0(x)/dx = -J_1(x)$ and the chain rule. The result is algebraically exact. The sign is obtained from $d/dz = -d/d\eta$, which introduces an overall positive sign.]

$$\Gamma(z,\omega) = U_g\,k_o\sqrt{\frac{H_s}{H_s-z}}\,\frac{J_1\!\left(2k_o\sqrt{H_s\,(H_s-z)}\right)}{J_0(2k_o H_s)}$$

Substituting $U_g = -A_g/\omega^2$ and $k_o/\omega^2 = 1/(c_o\,\omega)$:^[Confidence: HIGH, Rationale: The substitution is algebraically direct. The resulting formula is consistent with the general power-law formula at $m = 1$ and reduces to zero at $z = H_s$ because $J_1(0) = 0$, confirming that the shear stress vanishes at the free surface.]

$$\Gamma(z,\omega) = -\frac{A_g}{c_o\,\omega}\,\sqrt{\frac{H_s}{H_s-z}}\,\frac{J_1\!\left(2k_o\sqrt{H_s\,(H_s-z)}\right)}{J_0(2k_o H_s)}$$

The factor $\sqrt{H_s/(H_s-z)}$ reflects a geometric amplification of strain toward the free surface. As $z \to H_s$, the shear modulus $G \to 0$ while the shear stress $\tau = G\gamma$ remains bounded; therefore the strain grows without limit in the linearized model [DOI:10.1002/nag.1610060103]. In practice, this near-surface singularity is controlled by material nonlinearity or by the presence of a thin finite-stiffness weathered crust.^[Confidence: MEDIUM, Rationale: The algebraic derivation of the near-surface singularity is exact for the linear G profile. The statement that nonlinearity controls the singularity in practice is physically reasonable and consistent with the geotechnical literature, but no specific cited source in this document supports it quantitatively, hence MEDIUM.]

### 2.4 General Power-Law Profile

For the power-law profile $G(z) = G_o[(H_s-z)/H_s]^m$ with $0 < m < 2$, the displacement is given by the Bessel formula of Section 1.4.3. Differentiating with respect to $z$, applying the Bessel recurrence $J_\nu'(\zeta) = J_{\nu-1}(\zeta) - (\nu/\zeta)J_\nu(\zeta)$, and using the relation $\nu = (1-m)/(2-m)$, the coefficient of the $J_\nu$ term vanishes identically -- a consequence of the algebraic equality $\alpha - \nu\gamma = 0$ that holds precisely when $\alpha = (1-m)/2$ and $\gamma = (2-m)/2$ -- leaving a single Bessel term of order $\nu-1$ [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007]:^[Confidence: HIGH, Rationale: The cancellation of the $J_\nu$ terms is an algebraic consequence of the particular relationship between the power prefactor exponent $\alpha = (1-m)/2$ and the Bessel order $\nu = (1-m)/(2-m)$ in the Bessel-form ODE solution. The derivation is verifiable by direct computation and confirmed at $m=1$ by consistency with the linear-profile formula.]

$$\Gamma(z,\omega) = \frac{A_g}{c_o\,\omega}\left(\frac{H_s-z}{H_s}\right)^{(1-2m)/2}\frac{J_{\nu-1}\!\left[\zeta(H_s-z)\right]}{J_\nu\!\left[\zeta(H_s)\right]}$$

where $\zeta(\eta) = \frac{2k_o H_s}{2-m}\left(\frac{\eta}{H_s}\right)^{(2-m)/2}$ with $\eta = H_s - z$, $\nu = (1-m)/(2-m)$, $k_o = \omega/c_o$, and $J_\nu$ is the Bessel function of the first kind.^[Confidence: HIGH, Rationale: The formula is dimensionally consistent ($A_g/(c_o\omega)$ is dimensionless; the power-law prefactor and ratio of Bessel functions are dimensionless). At $m = 1$: $(H_s-z)^{-1/2}/H_s^{-1/2} = \sqrt{H_s/(H_s-z)}$, $\nu-1 = -1$, $J_{-1} = -J_1$, recovering the linear-profile result with correct sign.]

At $m = 1$: $\nu = 0$, $J_{\nu-1} = J_{-1} = -J_1$, and the prefactor becomes $\sqrt{H_s/(H_s-z)}$. Substituting into the general formula reproduces the linear-profile result of Section 2.3 with correct sign, confirming internal consistency.^[Confidence: HIGH, Rationale: The verification at $m = 1$ is algebraically exact and demonstrates that the general power-law formula nests the linear-profile formula as a special case without contradiction.]

### 2.5 Depth Distribution and Influence of the Stiffness Profile

The depth distribution of shear strain is controlled by two competing factors: the spatial structure of the acceleration modal functions and the depth dependence of the shear modulus through the prefactor $(H_s-z)^{(1-2m)/2}/H_s^{(1-2m)/2}$ in the general formula. For the uniform layer the strain modes are $\sin[k_n(H_s-z)]$, whose spatial form is 90 degrees out of phase with the acceleration modes $\cos[k_n(H_s-z)]$; consequently the $n$-th mode contributes maximum strain at mid-depth (where $\sin$ is maximized) rather than at the free surface [DOI:10.1785/BSSA0660041293].^[Confidence: HIGH, Rationale: The modal phase relationship is a direct algebraic consequence of differentiating the cosine acceleration mode shapes, giving sine strain mode shapes. The observation about the depth of maximum strain is fully supported by the closed-form expressions derived above.]

For non-uniform profiles with $G(z) \to 0$ as $z \to H_s$ (i.e., $m > 0$), the algebraic prefactor $(H_s-z)^{(1-2m)/2}$ in the strain formula modulates the Bessel function contribution with depth. When $m > 1/2$ the exponent $(1-2m)/2 < 0$, so the prefactor amplifies toward the free surface and reinforces the near-surface strain concentration. When $m < 1/2$ the exponent is positive, so the algebraic factor decays toward the surface; whether the net strain increases or decreases near the surface then depends on the relative magnitude of the Bessel function, which is frequency-dependent and must be evaluated numerically for each $\omega$ [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007].^[Confidence: MEDIUM, Rationale: The analysis of the algebraic prefactor is exact. The threshold at $m = 1/2$ is algebraically verifiable. The conclusion about the net depth distribution for $m < 1/2$ is qualitative because it depends on the Bessel term, which varies with frequency; the statement is physically grounded but requires numerical confirmation for specific $m$ and $\omega$ values, hence MEDIUM confidence.]

Higher-mode contributions to the shear strain field are generally more significant relative to the fundamental mode than they are for the surface acceleration, because the strain spatial functions have shorter characteristic wavelengths per mode. As a result, a single-mode approximation is less reliable for depth-strain prediction than for surface acceleration, and full frequency-domain evaluation of $\Gamma(z,\omega)$ using the closed-form expressions above is recommended for accurate assessment of the shear strain profile [DOI:10.1002/nag.1610060103][DOI:10.1016/j.soildyn.2011.01.007].^[Confidence: MEDIUM, Rationale: The qualitative argument about higher-mode contributions to strain versus acceleration is physically well-motivated by the fact that differentiating the modal series with respect to depth increases the relative amplitude of higher modes. This is consistent with the literature [DOI:10.1002/nag.1610060103], but a quantitative comparison of modal truncation errors for strain versus acceleration is not derived here, hence MEDIUM confidence.]

---

