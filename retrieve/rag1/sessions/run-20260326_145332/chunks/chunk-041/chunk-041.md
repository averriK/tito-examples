Comparing Equations (B.81) and (B.83), it is apparent that **(B.84)**

$$k^* = k + i\omega c$$

By the appropriate choice of $k^*$, the displacement amplitude of Equation (B.83) can be made equal to that of Equation (B.81), although a small phase difference between the two solutions will remain. To accomplish this, the complex stiffness is represented as **(B.85)**

$$k^* = k\bigl[(-\xi^2 + i\xi)\bigr]$$

**Figure B.18** SDOF system with spring of complex stiffness.

For the usual small damping ratios considered in earthquake engineering problems, where the $\xi^2$ terms can be neglected so that $k^* \approx k(1 + i\xi)$. Using this expression for $k^*$, the error in phase angle between the responses given by Equations (B.81) and (B.83) is $\Delta\theta = 2\xi/(1+\beta)$. As a result, a viscously damped system can be represented as an undamped system with complex stiffness. The use of this approach, however, is restricted to cases of harmonic motion. For problems in which loading is characterized as periodic (and therefore as the sum of a series of harmonic loads), the use of complex stiffness greatly simplifies the calculation of the response of damped systems. For small damping ratios, the complex stiffness then consists of real and imaginary parts **(B.86)**

$$\text{Re}(k^*) = k, \qquad \text{Im}(k^*) = \xi k$$

Consequently, the damping ratio can be expressed as **(B.87)**

$$\xi = \frac{\text{Im}(k^*)}{2\,\text{Re}(k^*)}$$

which is useful to remember in the interpretation of quantities such as complex impedance functions (Section 8.3), which are usually expressed in terms of their real and imaginary parts.

## B.7 Response Spectra

For earthquake-resistant design, the entire time series of response may not be required. For many applications, earthquake-resistant design may be based on the maximum (absolute) value of the response of a structure to a particular base motion. Obviously, the response will depend on the mass, stiffness, and damping characteristics of the structure and on the characteristics of the base motion. The response spectrum describes the maximum response of a SDOF system to a particular input motion as a function of the natural frequency (or natural period) and damping ratio of the SDOF system (Figure B.19). The response may be expressed in terms of acceleration, velocity, or displacement. For a given ground motion, the maximum values of each of these parameters depend only on the natural frequency and damping ratio of the SDOF system. The maximum values of acceleration, velocity, and displacement are referred to as the spectral acceleration ($S_a$), spectral velocity ($S_v$), and spectral displacement ($S_d$), respectively. Note that an SDOF system of zero natural period (infinite natural frequency) would be rigid, and its spectral acceleration would be equal to the peak ground acceleration. Application of the Duhamel integral to a linear elastic SDOF system produces expressions for the acceleration, velocity, and displacement time series that are proportional (by a factor of $\omega$), except for a phase shift. Because the phase shift does not significantly influence the maximum response values, the spectral acceleration, velocity, and displacement can be approximately related to each other by the following simple expressions:

$$S_d = |u|_{\max} \tag{B.88a}$$

$$PSV \approx S_v = \omega\,S_d \tag{B.88b}$$

$$PSA \approx S_a = \omega\,PSV = \omega^2\,S_d \tag{B.88c}$$

**Figure B.19** Response spectrum. Spectral accelerations are the maximum absolute acceleration amplitudes of SDOF systems in response to the same input motion. The response spectrum is obtained by plotting the spectral accelerations against the periods of vibration of the SDOF systems.

where $u$ and $\omega_0$ are the displacement and natural frequency of the SDOF system, PSV is the pseudospectral velocity, and PSA is the pseudospectral acceleration. The PSV and PSA are not the true maximum values of velocity and acceleration, although in the case of PSA it is very close. In practice, the pseudospectral acceleration is generally assumed to be equal to the spectral acceleration and is generally referred to as $S_a$ in this text. Note that there is no pseudospectral displacement, only spectral displacement. In most of the text, pseudospectral acceleration is written more concisely as "spectral acceleration."

## B.8 Ductility of Structural Materials and Components

The ideal way to prevent damage due to a structure during earthquake shaking would be to ensure that it responds in a linear, elastic manner throughout an earthquake — if no yielding occurs, the structure (and all of its components) will return to its original position following shaking and there will be no structural damage. This objective may be easily achieved for low levels of shaking, but could require massive, expensive structural components for strong shaking.

**Figure B.20** Schematic illustration of different types of force-displacement behavior: (a) brittle, (b) ductile, and (c) ductile with removal of applied loading.

Consider an SDOF system with the force-displacement behavior shown in Figure B.20a. The system exhibits linear elastic behavior up to the yield force, $F_y$ (and also the yield displacement, $u_y$), but the yield force is equal to the ultimate capacity, $F_{ult}$, so complete failure (with loss of subsequent load-resisting capability) occurs at that point. Such a system, in which load-carrying capacity is lost at, or very shortly after, yielding is described as being brittle. If a load smaller than the yield force is applied to this structure and then removed, the displacement will go back to zero and no damage will have occurred. A brittle system can perform well during earthquake shaking, as long as its strength exceeds all loads applied to it. If a brittle system fails, however, damage will usually be rapid and catastrophic. Another SDOF system may have the force-displacement behavior shown in Figure B.20b. The ultimate capacity of this system is the same as that of the previous system, but it yields at a lower force, $F_y$ (and yield displacement, $u_y$). After yielding, this system continues to pick up resistance (albeit with lower stiffness) with increasing displacement. At a larger displacement, $u_p$, the full plastic capacity of the system, $F_{ult}$, is reached and the system continues to deform, while maintaining its load-resisting capacity, until complete failure occurs at a larger failure displacement, $u_f$. This system, which can continue to resist load while deforming well past its yield point, is described as being ductile. Structural engineers generally quantify ductility as the ratio of some measure of deformation (such as displacement, curvature, etc.) to its value at yield, e.g., in the form of ductility demand, $\mu = u_{\max}/u_y$. The ductility at failure, or ductility capacity, is defined as $\mu = u_f/u_y$. If the load applied to a ductile structure is released prior to failure (Figure B.20c), the displacement of the structure will decrease (usually nearly linearly) so that a residual displacement, $u_r$, occurs. The area under the force-displacement curve represents the energy dissipated by the plastic deformation of the structure. The structure would then be considered to have suffered some damage from the applied loading; the significance of this damage would depend on the amount of residual displacement and its effect on the utility of the specific structure. A ductile system can perform well during earthquake shaking even if the induced forces exceed its yield strength because it maintains load-carrying capacity and dissipates energy after yielding. There are, therefore, two basic approaches that can be taken in the seismic design of a structure. One is to allow brittle behavior but make the structure very strong so that yielding (which would be followed shortly by failure) never occurs. The other is to make the structure very ductile (and allow controlled yielding) so that failure doesn't occur. The "strength vs. ductility" decision has a number of implications, both for design of new structures and retrofitting of existing structures. Designing a new structure to be stronger generally involves using more material — thicker columns, beams, girders, walls, etc. and/or more reinforcement — these increase the cost and mass of the structure and reduce the usable space within its boundaries. Designing a new structure to be ductile can generally be achieved using less material, and thereby provide a less expensive structure. However, it also means that some level of damage will be accepted and requires more detailed analysis of the structure (and its components and connections) to ensure that failure does not occur. The design of retrofitting measures for existing structures can be particularly challenging because many older structures, due to materials and/or form, are both brittle and weak. Designing for ductility requires the ability to predict the seismic response of nonlinear systems. Nonlinear analyses are generally more complex and time-consuming, both from the standpoint of material characterization and computational demand, than linear analyses, as described in the following section.

## B.9 Response of Nonlinear SDOF Systems to General Loading

Numerical integration of the Duhamel integral is very useful for the calculation of the response of linear systems to general loading. Many systems for which the seismic response is to be calculated, however, exhibit nonlinear behavior. In such systems, the mass is usually constant, but the damping coefficient and/or the stiffness may vary with time, deflection, or velocity. It will be useful to develop methods for analysis of the response of nonlinear systems, recognizing that they will be appropriate for linear systems as well when damping and stiffness values are held constant. The most common approach to nonlinear analysis is the direct integration of incremental equations of motion that govern the response of the system over small time increments. The response is calculated for each time increment after adjusting the stiffness and damping at the beginning of the increment. By using the conditions at the end of one time increment as the initial conditions for the next time increment, the nonlinear system is approximated as an incrementally changing linear system.

**Figure B.21** SDOF system with nonlinear damping and spring forces.

### B.9.1 Incremental Equation of Motion

Consider the SDOF system shown in Figure B.21, which has a nonlinear spring and dashpot (i.e., the spring force is not proportional to displacement and the dashpot force is not proportional to velocity). Dynamic equilibrium at time $\tau$ requires that **(B.89)**

$$f_I(\tau) + f_D(\tau) + f_S(\tau) = Q(\tau)$$

and that at time $\tau + \Delta\tau$ **(B.90)**

$$f_I(\tau+\Delta\tau) + f_D(\tau+\Delta\tau) + f_S(\tau+\Delta\tau) = Q(\tau+\Delta\tau)$$

Defining the incremental forces **(B.91a–d)**

$$\Delta f_I(\tau) = f_I(\tau+\Delta\tau) - f_I(\tau)$$

$$\Delta f_D(\tau) = f_D(\tau+\Delta\tau) - f_D(\tau)$$

$$\Delta f_S(\tau) = f_S(\tau+\Delta\tau) - f_S(\tau)$$

$$\Delta Q(\tau) = Q(\tau+\Delta\tau) - Q(\tau)$$

and subtracting Equation (B.89) from Equation (B.90), the incremental equation of motion for the time interval from $\tau$ to $\tau + \Delta\tau$ is **(B.92)**

$$\Delta f_I(\tau) + \Delta f_D(\tau) + \Delta f_S(\tau) = \Delta Q(\tau)$$

or expressing the incremental forces in terms of incremental displacements, velocities, and accelerations **(B.93)**

$$m\,\Delta\ddot{u}(\tau) + c(\tau)\,\Delta\dot{u}(\tau) + k(\tau)\,\Delta u(\tau) = \Delta Q(\tau)$$

**Figure B.22** Stress-strain behavior of (a) linear elastic, (b) nonlinear elastic, and (c) nonlinear, inelastic materials under cyclic loading conditions.

By integrating this incremental equation of motion in a series of small time steps, the response of the nonlinear system can be obtained. It should be noted that this approach can be used to calculate the response of linear elastic, nonlinear elastic, or nonlinear inelastic materials with stress-strain behaviors shown in Figure B.22. The third of these is particularly important because it allows representation of the hysteretic damping displayed by cyclically loaded soils.

### B.9.2 Numerical Integration

There are many ways to numerically integrate the incremental equation of motion. One of the simplest and most easily coded of these is the linear acceleration method. It is based on the assumption that the acceleration varies linearly within each time increment. If the acceleration in the time increment varies linearly, the velocity and displacement will vary quadratically and cubically, respectively. **(B.94)**

$$\Delta\dot{u}(\tau) = \dot{u}(\tau)\,\Delta t + \frac{\Delta t}{2}\,\Delta\ddot{u}$$

$$\Delta u(\tau) = \dot{u}(\tau)\,\Delta t + \frac{\Delta t^2}{2}\,\ddot{u}(\tau) + \frac{\Delta t^2}{6}\,\Delta\ddot{u} \tag{B.95}$$

Rearranging, the incremental acceleration and velocity can be expressed in terms of the incremental displacement **(B.96a–b)**

$$\Delta\ddot{u}(\tau) = \frac{6}{\Delta t^2}\,\Delta u - \frac{6}{\Delta t}\,\dot{u}(\tau) - 3\,\ddot{u}(\tau)$$

$$\Delta\dot{u}(\tau) = \frac{3}{\Delta t}\,\Delta u - 3\,\dot{u}(\tau) - \frac{\Delta t}{2}\,\ddot{u}(\tau)$$

Substituting Equations (B.96) into the incremental equation of motion [Equation (B.93)] and rearranging to solve for incremental displacement **(B.97–B.98)**

$$\Delta u(\tau) = \frac{\Delta Q(\tau) + m\!\left[\frac{6}{\Delta t}\,\dot{u}(\tau) + 3\,\ddot{u}(\tau)\right] + c(\tau)\!\left[3\,\dot{u}(\tau) + \frac{\Delta t}{2}\,\ddot{u}(\tau)\right]}{\frac{6}{\Delta t^2}\,m + \frac{3}{\Delta t}\,c(\tau) + k(\tau)}$$

**Figure B.23** Variation of acceleration, velocity, and displacement over time increment when the time-variation of acceleration is linear.

Equation (B.98) shows that if the displacement, velocity, and acceleration at time $\tau$ are known, the incremental displacement during the succeeding time increment $\Delta\tau$ can be calculated based on the loading and the stiffness and damping during that time increment. From this incremental displacement, the incremental velocity and acceleration, and from these the displacement, velocity, and acceleration at the end of the time increment, can be determined. The conditions at the end of the time increment are then taken as the initial conditions for the next time increment and are used to calculate the appropriate stiffness and damping values for the next time increment. To prevent the accumulation of errors resulting from the assumptions of the linear acceleration method, the acceleration at the beginning of each time step should be calculated by subtracting the damping and spring forces from the total external load and dividing the result by the mass. This will ensure that total equilibrium is satisfied at each step of the analysis. For numerical stability, it is necessary that the time steps be relatively small, typically less than about 55% of the shortest undamped natural period of the system. These small time steps can lead to considerable computational effort when the linear acceleration method is applied to multiple-degree-of-freedom systems. A number of other numerical integration techniques, including some that are unconditionally stable, are available; Berg (1989) describes the application of several to structural dynamics problems.

## B.10 Multiple-Degree-of-Freedom Systems

In most physical systems, the motion of the significant masses cannot be described by a single variable; such systems must be treated as multiple-degree-of-freedom (MDOF) systems. With the exception of only the simplest cases, the types of buildings, bridges, and other structures that are of interest in earthquake engineering have multiple DOF. Some structures can be idealized with only a few DOF; others may require hundreds or even thousands. In many respects, the response of MDOF systems is similar to the response of SDOF systems, and procedures for analysis are analogous to those described previously for SDOF systems. Although the additional DOF complicate the algebra, the procedures are conceptually quite similar. In fact, a very useful approach to the response of linear MDOF systems allows their response to be computed as the sum of the responses of a series of SDOF systems.

### B.10.1 Equations of Motion

In evaluating the response of an MDOF system, the dynamic equilibrium of all masses must be ensured simultaneously. Consider the idealized two-story structure shown in Figure B.24. The structure has two DOF: horizontal translation of the upper mass and horizontal translation of the lower mass. For each mass the externally applied load must be balanced by the inertial, damping, and elastic forces that resist motion:

$$f_{I,1} + f_{D,1} + f_{S,1} = q_1(t) \tag{B.99a}$$

$$f_{I,2} + f_{D,2} + f_{S,2} = q_2(t) \tag{B.99b}$$

or, in matrix form **(B.100)**

$$\mathbf{f}_I + \mathbf{f}_D + \mathbf{f}_S = \mathbf{q}(t)$$

Each of the terms on the left side of Equation (B.100) are vectors that depend on the structural properties given in Figure B.24. If the structure exhibits linear behavior, the principle of superposition is valid. Then the forces that resist motion at each level can be expressed in terms of coefficients by which the motion parameter at all levels are multiplied. For example, the elastic force resisting motion at level 1 can be expressed as **(B.101)**

$$f_{S,1} = k_{11}\,u_1 + k_{12}\,u_2$$

where the stiffness coefficients $k_{ij}$ represent the force induced at level $i$ due to a unit displacement at level $j$ (with the displacements at all levels except $j$ held equal to zero). In matrix form **(B.102)**

$$\mathbf{f}_S = \begin{bmatrix} k_{11} & k_{12} \\ k_{21} & k_{22} \end{bmatrix} \mathbf{u}$$

or **(B.103)**

$$\mathbf{f}_S = \mathbf{k}\,\mathbf{u}$$

**Figure B.24** Two-degree-of-freedom system. Displacements of masses 1 and 2 from equilibrium positions are $u_1$ and $u_2$, respectively.

in which $\mathbf{k}$ is the stiffness matrix of the structure and $\mathbf{u}$ is a displacement vector. Similarly, a damping matrix and a mass matrix can be developed in which the elements $c_{ij}$ (or $m_{ij}$) represent the damping (or inertial) forces resisting motion at level $i$ due to a unit velocity (or acceleration) of level $j$. Dynamic equilibrium of the MDOF system can then be described by a set of simultaneous equations of motion, which can be expressed in matrix form as **(B.104)**

$$\mathbf{m}\,\ddot{\mathbf{u}} + \mathbf{c}\,\dot{\mathbf{u}} + \mathbf{k}\,\mathbf{u} = \mathbf{q}(t)$$

MDOF systems also respond to base motions. The equation of motion for the case of base shaking is easily developed following the same procedure applied to the SDOF case in Section B.4.2. The resulting equation of motion is **(B.105)**

$$\mathbf{m}\,\ddot{\mathbf{u}} + \mathbf{c}\,\dot{\mathbf{u}} + \mathbf{k}\,\mathbf{u} = -\mathbf{m}\,\mathbf{1}\,\ddot{u}_b(t)$$

where $\mathbf{1}$ is a column vector of ones. Equation (B.105) indicates that the response of an $N$-story structure to base motion is equal to the response to equivalent external loads, where $q_i = -m_i\,\ddot{u}_b(t)$ is the load applied to the $i$th floor.

### B.10.2 Undamped Free Vibrations

For undamped free vibrations, all terms of the damping matrix are zero, so the equations of motion reduce to **(B.106)**

$$\mathbf{m}\,\ddot{\mathbf{u}} + \mathbf{k}\,\mathbf{u} = \mathbf{0}$$

where $\mathbf{0}$ is a column vector of zeros. Assuming that the response of each mass (degree of freedom) is harmonic **(B.107)**

$$\mathbf{u}(t) = \mathbf{U}\sin(\omega t + \theta)$$

where $\mathbf{U}$ is a vector containing the displacement amplitudes, $\omega$ is an angular frequency of vibration, and $\theta$ is a phase angle (similar to Equation B.14). Differentiating Equation (B.107) twice gives **(B.108)**

$$\ddot{\mathbf{u}}(t) = -\omega^2\,\mathbf{U}\sin(\omega t + \theta) = -\omega^2\,\mathbf{u}(t)$$

Substituting the expressions for displacement [Equation (B.107)] and acceleration [Equation (B.108)] into the equation of motion [Equation (B.106)] yields

$$-\mathbf{m}\,\omega^2\,\mathbf{U}\sin(\omega t + \theta) + \mathbf{k}\,\mathbf{U}\sin(\omega t + \theta) = \mathbf{0} \tag{B.109a}$$

or **(B.109b)**

$$\bigl(\mathbf{k} - \omega^2\,\mathbf{m}\bigr)\,\mathbf{U} = \mathbf{0}$$

which is a set of linear algebraic equations with unknown $\mathbf{U}$. Applying methods from linear algebra, a nontrivial solution (one that gives values other than $\mathbf{U} = \mathbf{0}$) can be obtained only if **(B.110)**

$$\det\!\bigl(\mathbf{k} - \omega^2\,\mathbf{m}\bigr) = 0$$

Equation (B.110) is the frequency equation (or characteristic equation) of the system, which for a system of $N$ DOF, will give a polynomial of $N$th degree in $\omega^2$. The $N$ roots of the frequency equation $\{\omega_1, \omega_2, \ldots, \omega_N\}$ represent the frequencies at which the undamped system can oscillate in free vibration. These frequencies are called the natural circular frequencies of the system. Each natural frequency is associated with a mode of vibration of the system. At the natural frequencies, the amplitude of the displacement vector, $\mathbf{U}$, is indeterminate [scaling the displacements up or down by a constant factor will still satisfy Equation (B.110)]. The vector $\mathbf{U}$ does describe the shape of the vibrating system, which is different at each natural frequency. This shape is often made dimensionless by dividing the elements of $\mathbf{U}$ by the displacement of one (often the first, sometimes the largest) element. The resulting vector describes the mode shape; the mode shape for the $n$th mode of vibration would be **(B.111)**

$$\boldsymbol{\phi}_n = \mathbf{U}_n / U_{1n} = \begin{bmatrix} \phi_{1n} & \phi_{2n} & \cdots & \phi_{Nn} \end{bmatrix}^T$$

All mode shapes (regardless of normalization) satisfy the relationship $(\mathbf{k} - \omega_n^2\,\mathbf{m})\,\boldsymbol{\phi}_n = \mathbf{0}$ for $n = 1, \ldots, N$. Example mode shapes for the structure in Figure B.24 are shown in Figure B.25. Note that in the first mode, both masses move in the same direction, whereas in the second mode, they move in opposite directions. Thus, a system of $N$ degrees of freedom will have $N$ natural frequencies corresponding to $N$ modes of vibration. Each mode of vibration occurs at a particular natural frequency and causes the structure to deform with a particular mode shape. The mode corresponding to the lowest natural frequency is called the first mode or fundamental mode, the second lowest natural frequency is called the second mode, and so on. The mode shapes can be shown to be orthogonal, i.e., for $m \neq n$ **(B.112a–b)**

$$\boldsymbol{\phi}_m^T\,\mathbf{m}\,\boldsymbol{\phi}_n = 0$$

$$\boldsymbol{\phi}_m^T\,\mathbf{k}\,\boldsymbol{\phi}_n = 0$$

### B.10.3 Mode Superposition Method

For linear structures with certain types of damping, the response in each mode of vibration can be determined independently of the response in the other modes. The independent modal responses can then be combined to determine the total response. This is the basis of the mode superposition method.

**Figure B.25** Two-degree-of-freedom structure illustrating: (a) initial geometry and properties, (b) first mode shape with displacements normalized by top floor displacement, and (c) normalized second mode shape.

Recalling that the mode shape vector, $\boldsymbol{\phi}_n$, describes only the shape of the $n$th mode, the displacements can be expressed as the product of the mode shape and the modal amplitude, $y_n$ **(B.113)**

$$\mathbf{U}_n(t) = \boldsymbol{\phi}_n\,y_n(t)$$

Then, by substituting Equation (B.113) into Equation (B.104) and pre-multiplying each term by $\boldsymbol{\phi}_n^T$, the equation of motion can be written for the $n$th mode of vibration as **(B.114)**

$$M_n\,\ddot{y}_n + C_n\,\dot{y}_n + K_n\,y_n = Q_n(t)$$

where the generalized (or modal) mass, $M_n = \boldsymbol{\phi}_n^T\,\mathbf{m}\,\boldsymbol{\phi}_n$; generalized damping coefficient, $C_n = \boldsymbol{\phi}_n^T\,\mathbf{c}\,\boldsymbol{\phi}_n$; generalized stiffness, $K_n = \boldsymbol{\phi}_n^T\,\mathbf{k}\,\boldsymbol{\phi}_n$; and generalized load, $Q_n(t) = \boldsymbol{\phi}_n^T\,\mathbf{q}(t)$. This modal equation of motion is based on the assumption that the damping matrix is orthogonal (i.e., that for $m \neq n$, $\boldsymbol{\phi}_m^T\,\mathbf{c}\,\boldsymbol{\phi}_n = 0$). Rayleigh damping, in which the damping matrix can be broken into a component proportional to the mass matrix and a component proportional to the stiffness matrix, satisfies the orthogonality requirement. Other procedures are described in structural dynamics texts. Alternatively, the equation of motion can be written as **(B.115)**

$$\ddot{y}_n + 2\xi_n\omega_n\,\dot{y}_n + \omega_n^2\,y_n = \frac{Q_n(t)}{M_n}$$

where $\xi_n = C_n/(2M_n\omega_n)$. For the case of base shaking, the equation of motion can be expressed as **(B.116)**

$$\ddot{y}_n + 2\xi_n\omega_n\,\dot{y}_n + \omega_n^2\,y_n = -\frac{L_n}{M_n}\,\ddot{u}_b(t)$$

where $L_n = \sum_{j=1}^{N} m_j\,\phi_{jn}$. The quantity $L_n/M_n$, often referred to as the modal participation factor, reflects the extent to which each mode contributes to the overall response. By this process, the system of $N$ simultaneous equations (the original equations of motion) is transformed into a system of $N$ independent equations. Each of these independent equations can be solved for $y_n(t)$ using the SDOF procedures described earlier in this appendix. Then the total displacement is obtained by superposition of the modal contributions **(B.117)**

$$\mathbf{u}(t) = \boldsymbol{\phi}_1\,y_1(t) + \boldsymbol{\phi}_2\,y_2(t) + \cdots + \boldsymbol{\phi}_N\,y_N(t)$$

Once the displacements are known, they can be used to compute forces, stresses, and other parameters of interest. The displacements can also be used to compute a set of equivalent lateral forces, $\mathbf{f}(t)$, which would produce the displacements $\mathbf{u}(t)$ if they were applied as static loads **(B.118)**

$$\mathbf{f}(t) = \mathbf{k}\boldsymbol{\phi}_1\,y_1(t) + \mathbf{k}\boldsymbol{\phi}_2\,y_2(t) + \cdots + \mathbf{k}\boldsymbol{\phi}_N\,y_N(t)$$

Internal forces and moments can be computed by static analysis of the structure subjected to the equivalent lateral forces. These internal forces can be used for design of the various elements of the structure.

### B.10.4 Response Spectrum Analysis

The mode superposition method produces the entire time series of structural response. For design purposes, however, the entire time series may not be needed; the maximum response values may be sufficient. Because each mode of vibration can be treated as an independent SDOF system, maximum values of modal responses can be obtained from the response spectrum. The modal maxima can then be combined to estimate the maximum total response.

#### B.10.4.1 Calculation of Modal Response Maxima

Let $S_{dn}$, $S_{vn}$, and $S_{an}$ denote the spectral displacement, velocity, and acceleration associated with the $n$th mode of vibration, respectively (these values would be obtained from the response spectrum at a period, $T_n = 2\pi/\omega_n$). Then the maximum modal displacement is given by **(B.119)**

$$y_{n,\max} = \frac{L_n}{M_n}\,S_{dn} = \frac{L_n}{M_n}\cdot\frac{T_n^2}{4\pi^2}\,S_{an}$$

Using Equation (B.113), the maximum displacement of the $j$th floor from vibration in the $n$th mode would be **(B.120)**

$$U_{jn,\max} = \phi_{jn}\,\frac{L_n}{M_n}\,S_{dn} = \phi_{jn}\,\frac{L_n}{M_n}\cdot\frac{T_n^2}{4\pi^2}\,S_{an}$$

The maximum value of the equivalent lateral force at the $j$th floor from vibration in the $n$th mode is **(B.121)**

$$f_{jn,\max} = m_j\,\phi_{jn}\,\frac{L_n}{M_n}\,S_{an}$$

Maximum values of the internal forces and moments can then be computed by static analysis of the structure subjected to the maximum equivalent lateral forces.

#### B.10.4.2 Combination of Modal Response Maxima

Section B.10.4.1 showed how the response spectrum can be used to predict maximum values of various modal response parameters. The mode superposition method showed that time series of modal response can be combined by simple superposition to obtain the total time series of response. However, the combination of modal response maxima to obtain the maximum total response is not as straightforward. The exact value of the maximum total response cannot be obtained directly from the modal maxima because the modal maxima occur at different times. Direct superposition of the modal maxima, which implies that the maxima do occur simultaneously, produces an upper bound to the maximum total response; for any response parameter $r(t)$,
