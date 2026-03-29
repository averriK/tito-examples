The steady-state response can be visualized with the aid of rotating vectors, both for the deformation responses and for the forces induced in the system, as shown in Figure B.10. Note that the spring, dashpot, and inertial forces act opposite to the displacement, velocity and acceleration vectors, and that the displacement lags the applied loading vector by the negative phase angle, $\phi$. For harmonic loading the phase angle varies with both damping ratio and tuning ratio, as shown in Figure B.11b. The influence of the tuning ratio can be illustrated by the use of the magnification factor, again defined as the ratio of the amplitude to the static displacement:

$$M = \frac{Q_0/k}{\sqrt{(1-\beta^2)^2 + (2\xi\beta)^2}} \tag{B.46}$$

*Figure B.10 Rotating vector representations of deformation response and forces in vibrating SDOF system.*

*Figure B.11 Variation of (a) magnification factor, and (b) phase angle with damping ratio and tuning ratio.*

The variation of the magnification factor with tuning ratio and damping ratio is shown in Figure B.11a. The damping ratio influences the peak magnification factor and also the variation of magnification factor with frequency. The magnification factor curves broaden with increasing damping ratio. Note that the magnification is unbounded (resonance) only for $\xi = 0$ and $\beta = 1$. For nonzero damping, there is some maximum magnification, $M_{\max}$,

$$M_{\max} = \frac{1}{2\xi\sqrt{1-\xi^2}} \tag{B.47}$$

which occurs when the tuning ratio $\beta = \sqrt{1-2\xi^2}$. The shape of the magnification curve is obviously controlled by the damping ratio. Although a system with low damping may produce large magnification at a tuning ratio near 1, it will exhibit significant magnification over a smaller range of frequencies than a system with higher damping.

### B.5.4 Response of SDOF Systems to Periodic Loading

The solutions for the response of an SDOF system to harmonic loading developed in the preceding section can be used to develop solutions for the more general case of periodic loading. As shown in Appendix A, periodic loading can be approximated by a Fourier series (i.e., as the sum of a series of harmonic loads). The response of an SDOF system to the periodic loading, using the principle of superposition, is simply the sum of the responses to each term in the loading series. The required calculations can be performed using trigonometric or exponential notation.

#### B.5.4.1 Trigonometric Notation

From Equation (A.12) a periodic load, $Q(t)$, can be expressed by the Fourier series

$$Q(t) = a_0 + \sum_{n=1}^{\infty}\!\left(a_n \cos n\omega t + b_n \sin n\omega t\right) \tag{B.48}$$

where the Fourier coefficients are

$$a_0 = \frac{1}{T_f}\int_0^{T_f} Q(t)\,dt$$

$$a_n = \frac{2}{T_f}\int_0^{T_f} Q(t)\cos n\omega_n t\,dt$$

$$b_n = \frac{2}{T_f}\int_0^{T_f} Q(t)\sin n\omega_n t\,dt$$

and $\omega_n = 2\pi n/T_f$. Using the steady-state portion of Equation (B.44), the response to each sine term $n$ in the Fourier series is

$$u_{n,\sin}(t) = \frac{b_n/k}{(1-\beta_n^2)^2+(2\xi\beta_n)^2}\left[(1-\beta_n^2)\sin\omega_n t - 2\xi\beta_n\cos\omega_n t\right] \tag{B.49a}$$

where $\beta_n = \omega_n T_f/2\pi$. In the same way, the steady-state response to each cosine term can be shown to be

$$u_{n,\cos}(t) = \frac{a_n/k}{(1-\beta_n^2)^2+(2\xi\beta_n)^2}\left[(1-\beta_n^2)\cos\omega_n t + 2\xi\beta_n\sin\omega_n t\right] \tag{B.49b}$$

Since the steady-state response to the constant load term is the static displacement, $u_0 = a_0/k$, the total steady-state response is given by

$$u(t) = u_0 + \sum_{n=1}^{\infty}\left[u_{n,\sin}(t) + u_{n,\cos}(t)\right] \tag{B.50}$$

#### B.5.4.2 Exponential Notation

Periodic loading can also be described by the Fourier series in exponential form. Using Equation (A.16), a periodic load with a zero mean can be expressed as

$$Q(t) = \sum_{n=-\infty}^{\infty} q_n^{\,*} e^{i\omega_n t} \tag{B.51}$$

The complex Fourier coefficients, $q_n^*$, can be determined directly from $Q(t)$ as

$$q_n^{\,*} = \frac{1}{T_f}\int_0^{T_f} Q(t)\,e^{-i\omega_n t}\,dt \tag{B.52}$$

The response of an SDOF system loaded by the $n$th harmonic would be governed by the equation of motion

$$m\ddot{u}_n(t) + c\dot{u}_n(t) + ku_n(t) = q_n^{\,*} e^{i\omega_n t} \tag{B.53}$$

The response of the system can be related to the loading by

$$u_n(t) = H(\omega_n)\,q_n^{\,*} e^{i\omega_n t} \tag{B.54}$$

where $H(\omega_n)$ is a transfer function [i.e., a function that relates one parameter (in this case, the displacement of the oscillator) to another (the external load)]. Substituting Equation (B.54) into the equation of motion gives

$$-m\omega_n^2\,H(\omega_n)\,q_n^* e^{i\omega_n t} + ic\omega_n\,H(\omega_n)\,q_n^* e^{i\omega_n t} + k\,H(\omega_n)\,q_n^* e^{i\omega_n t} = q_n^* e^{i\omega_n t} \tag{B.55}$$

which can be rearranged to find the transfer function

$$H(\omega_n) = \frac{1}{k - m\omega_n^2 + ic\omega_n} = \frac{1/k}{(1-\beta_n^2) + 2i\xi\beta_n} \tag{B.56a}$$

Since $A^* = a + ib = Ae^{i\theta}$, where the modulus $A = \sqrt{a^2+b^2}$ and the phase $\phi = \tan^{-1}(b/a)$, the transfer function can also be written as

$$H(\omega_n) = \frac{1/k}{\sqrt{(1-\beta_n^2)^2+(2\xi\beta_n)^2}}\exp\!\left[-i\tan^{-1}\!\left(\frac{2\xi\beta_n}{1-\beta_n^2}\right)\right] \tag{B.56b}$$

Note the close relationship between the modulus of the transfer function and the magnification factor of Equation (B.46). Because the transfer function can be used for any frequency in the series, the principle of superposition gives the total response as

$$u(t) = \sum_{n=-\infty}^{\infty} H(\omega_n)\,q_n^{\,*} e^{i\omega_n t} \tag{B.57}$$

Many different transfer functions can be developed. For example, a transfer function relating the acceleration of the SDOF system to the external load could have been developed just as easily. The advantages of the transfer function approach lie in its simplicity and in the ease with which it allows computation of the response to complicated loading patterns. The transfer function may be viewed as a filter that acts upon some input signal to produce an output signal. In the case just considered, the input signal was the loading history, $Q(t)$, and the output was the displacement, $u(t)$. If the input signal has Fourier amplitude and phase spectra, $F_i(\omega_n)$ and $\phi_i(\omega_n)$, the Fourier amplitude and phase spectra of the output signal will be given by

$$F_0(\omega_n) = A_H(\omega_n) \cdot F_i(\omega_n) \tag{B.58a}$$

$$\phi_0(\omega_n) = \phi_H(\omega_n) + \phi_i(\omega_n) \tag{B.58b}$$

where the amplitude change and phase shift produced by $H(\omega_n)$ are given by $A[H(\omega_n)]$ and $\phi[H(\omega_n)]$, respectively. Thus, the procedure for Fourier analysis of SDOF system response can be summarized in the following steps:

1. Obtain the Fourier series for the applied loading (or base motion). In doing so, the loading (or base motion) is expressed as a function of frequency rather than a function of time.
2. Multiply the Fourier series coefficients by the appropriate value of the transfer function at each frequency. This will produce the Fourier series of the output motion.
3. Express the output motion in the time domain by obtaining the inverse Fourier transform of the output motion.

It is precisely this approach that forms the backbone of several of the most commonly used methods for the analysis of ground response and soil-structure interaction. These methods are presented in Chapters 7 and 8.

### B.5.5 Response of SDOF Systems to General Loading

Not all loading is harmonic or even periodic. To determine the response of SDOF systems to general loading conditions, a more general solution of the equation of motion is required.

#### B.5.5.1 Response to Step Loading

Consider a damped SDOF system subjected to a step load of intensity, $Q_0$, which is applied instantaneously at $t = 0$ and removed instantaneously at $t = t_1$ as shown in Figure B.12. For $t \leq t_1$, the complementary solution to the equation of motion for this system [Equation (B.39)], $u_c(t) = e^{-\xi\omega_0 t}[C_1\sin\omega_d t + C_2\cos\omega_d t]$ describes the transient response of the system. The equation of motion for the steady-state condition is given by

$$m\ddot{u}_p + c\dot{u}_p + ku_p = Q_0 \tag{B.59}$$

*Figure B.12 Time history of step loading.*

Since the applied load does not vary with time, the steady-state response will be a constant displacement,

$$u_p(t) = \frac{Q_0}{k} \tag{B.60}$$

The general solution to the step loading problem for $t \leq t_1$ can then be written as

$$u(t) = e^{-\xi\omega_0 t}\!\left(C_1\sin\omega_d t + C_2\cos\omega_d t\right) + \frac{Q_0}{k} \tag{B.61}$$

with free vibration occurring at $t > t_1$ (when no external load is applied). The constants are determined by the initial conditions, $u_0$ and $\dot{u}_0$. At $t = 0$,

$$u(0) = C_2 + \frac{Q_0}{k}, \qquad \dot{u}(0) = \omega_d C_1 - \xi\omega_0 C_2 \tag{B.62}$$

from which it can be shown that $C_2 = u_0 - Q_0/k$ and $C_1 = \bigl(\dot{u}_0 + \xi\omega_0(u_0 - Q_0/k)\bigr)/\omega_d$, so that

$$u(t) = e^{-\xi\omega_0 t}\!\left[\frac{\dot{u}_0 + \xi\omega_0(u_0 - Q_0/k)}{\omega_d}\sin\omega_d t + \left(u_0 - \frac{Q_0}{k}\right)\cos\omega_d t\right] + \frac{Q_0}{k} \tag{B.63}$$

describes the response of the system up to the beginning of free vibration at $t = t_1$.

#### B.5.5.2 Dirac Pulse

A particular type of step loading can be described using a Dirac delta function. A Dirac delta function is one whose value is zero at all values of $x$ except one at which it goes to infinity in such a way that the area under the function is unity. Mathematically, the Dirac delta function satisfies the conditions

$$\delta(x-a) = \begin{cases} 0 & x \neq a \\ \infty & x = a \end{cases} \tag{B.64a}$$

$$\int_{-\infty}^{\infty}\delta(x)\,dx = 1 \tag{B.64b}$$

*Figure B.13 Dirac pulse loading.*

Consider a Dirac pulse that consists of a constant force $Q_0$ applied over a duration $t_1$ that approaches zero as shown in Figure B.13. From impulse-momentum principles, $m\dot{u}(t) = Q_0 t_1$. As $t_1$ approaches zero, the effect of the Dirac pulse is to cause an initial velocity $\dot{u} = Q_0 t_1/m$, with no initial displacement. Thus, the steady-state response occurs only over an infinitesimal period of time, and the system is immediately set into free vibration. From Equation (B.21), if $t_1 = 0$ the response to a Dirac pulse disturbance at $t > 0$ is given by

$$u(t) = \frac{Q_0 t_1}{m\omega_d}\,e^{-\xi\omega_0 t}\sin\omega_d t \tag{B.65}$$

#### B.5.5.3 Duhamel Integral

A general loading function such as that shown in Figure B.14 can be thought of as a series of load pulses, each of infinitesimal duration. Looking at one of these pulses — the pulse of duration $d\tau$ occurring at $t = \tau$ (Figure B.14) — the response it causes at a later time, $t$, follows from Equation (B.66):

$$du(t\,|\,t{=}\tau) = \frac{Q(\tau)\,d\tau}{m\omega_d}\,e^{-\xi\omega_0(t-\tau)}\sin\omega_d(t-\tau) \tag{B.66}$$

The response induced by the entire train of load pulses can be obtained by summing the responses of all of the individual pulses up to the time $t$, i.e.,

$$u(t) = \sum_{i=1}^{n}\frac{Q_i}{m\omega_d}\,e^{-\xi\omega_0(t-\tau_i)}\sin\omega_d(t-\tau_i)\,d\tau \tag{B.67}$$

*Figure B.14 Pulse of duration $d\tau$ occurring at $t = \tau$.*

where $n$ is the total number of pulses up to $t$. As $d\tau$ approaches zero, the summation becomes an integral with which the total response can be calculated as

$$u(t) = \frac{1}{m\omega_d}\int_0^t Q(\tau)\,e^{-\xi\omega_0(t-\tau)}\sin\omega_d(t-\tau)\,d\tau \tag{B.68}$$

This equation describing the response of a linear system is known as Duhamel's integral. It is usually very difficult to solve analytically, but can be integrated numerically by a variety of procedures. Its use, however, is constrained to linear systems.

### B.6 Damping

Energy is dissipated in soils and structures by several mechanisms, including friction, heat generation, and plastic yielding. For specific soils and structures, however, the operative mechanisms are not understood sufficiently to allow them to be explicitly modeled. As a result, the effects of the various energy loss mechanisms are usually lumped together and represented by some convenient damping mechanism.

#### B.6.1 Viscous Damping

The most commonly used mechanism for representing energy dissipation is viscous damping. When a viscous damped SDOF system such as that shown in Figure B.3 is subjected to a harmonic displacement [Equation B.27]

$$u(t) = u_0\sin\omega t$$

the net force exerted on the mass by the spring and dashpot is

$$F(t) = ku(t) + c\dot{u}(t) = ku_0\sin\omega t + cu_0\omega\cos\omega t \tag{B.69}$$

Evaluating these functions from time $t_0$ to time $t_0 + 2\pi/\omega$ yields the force-displacement values for one cycle of a hysteresis loop. When the viscous damping coefficient, $c$, is zero, the force and displacement are in phase and proportional to each other, implying a linear elastic stress-strain relationship. For nonzero damping, however, the hysteresis loop is elliptical, as shown in Figure B.15. Note that when the displacement is zero, the spring force is zero and the net force comes entirely from the dashpot. Similarly, when the velocity is zero (at $\omega t = \pi/2 + n\pi$), the dashpot force vanishes and the net force consists entirely of the spring force. The aspect ratio of the hysteresis loop decreases with increasing damping; the loop becomes a circle when $c = k/\omega$. Obviously, the shape of the hysteresis loop depends on the viscous damping coefficient and therefore on the damping ratio. Hence we should be able to determine the damping ratio from a known hysteresis loop. The energy dissipated in one cycle of oscillation is given by the area inside the hysteresis loop and can be obtained from

$$W_D = \int F\,du = \int_t^{t+2\pi/\omega} F\,\frac{du}{dt}\,dt = \pi c\omega u_0^2 \tag{B.70}$$

At maximum displacement, the velocity is zero and the strain energy stored in the system is given by

*Figure B.15 Stress-strain behavior implied by viscous damping. Hysteresis loop is elliptical.*

$$W_S = \frac{1}{2}ku_0^2 \tag{B.71}$$

Equations (B.70) and (B.71) show that $W_D = \pi c\omega u_0^2$ and $W_S = \frac{1}{2}ku_0^2$. Substituting these into Equation (B.17) with $\omega = \omega_0$ gives an expression

$$\xi = \frac{W_D}{4\pi W_S} \tag{B.72}$$

that is commonly used for graphical determination of the damping ratio from a measured hysteresis loop. Referring to Figure B.16, the damping ratio is taken as the ratio of the area of the hysteresis loop to the area of the shaded triangle, all divided by $4\pi$. This graphical evaluation of the damping ratio is commonly used in the interpretation of many of the laboratory tests discussed in Chapter 6. The damping characteristics of a linear system can also be evaluated from its frequency response characteristics. Setting the magnification factor expression [Equation (B.46)] equal to $M_{\max}/\sqrt{2}$, the half-power tuning ratios, shown in Figure B.17, can be approximated as

*Figure B.16 Graphical evaluation of damping ratio from measured hysteresis loop. The damping ratio is proportional to the ratio of the area of the hysteresis loop to the area of the shaded triangle.*

*Figure B.17 Half-power tuning ratios for evaluation of damping ratio from magnification curve.*

$$\beta_1 \approx 1 - \xi \tag{B.73a}$$

$$\beta_2 \approx 1 + \xi \tag{B.73b}$$

Therefore, the damping ratio is given by half the difference between the half-power tuning ratios

$$\xi \approx \frac{\beta_2 - \beta_1}{2} \tag{B.74}$$

or, when the response is expressed in terms of frequency, where $\omega_1 = \beta_1\omega_0$ and $\omega_2 = \beta_2\omega_0$,

$$\xi \approx \frac{\omega_2 - \omega_1}{\omega_1 + \omega_2} \tag{B.75}$$

Thus the damping ratio of a system can be measured by exciting the system at different frequencies and determining the amplitude of the magnification factor at each frequency.

#### B.6.2 Other Measures of Energy Dissipation

In addition to the viscous damping ratio, $\xi$, a number of other parameters have been used to describe energy dissipation characteristics. Seismologists, for example, often work with the quality factor

$$Q = \frac{1}{2\xi} \tag{B.76}$$

In vibration analysis, the loss factor

$$\eta = 2\xi \tag{B.77}$$

and specific damping capacity

$$\psi = \pi\xi \tag{B.78}$$

are often used (Goodman, 1988). It is important to remember that the damping ratio, and any of these other parameters, are simply parameters used to describe the effects of phenomena that are often poorly understood. They allow the effects of energy dissipation to be represented in a mathematically convenient manner. For most soils and structures, however, energy is dissipated hysteretically. In cases with large hysteretic damping caused by yielding or plastic straining of the material, the behavior is more accurately characterized by evaluating the nonlinear response of the system.

#### B.6.3 Complex Stiffness

A viscously damped system can be represented conveniently in a different but equivalent way for a class of techniques known as complex response analysis. Consider a damped SDOF system subjected to simple harmonic loading of amplitude, $Q_0$, and loading frequency, $\omega$. The loading can be represented by

$$Q(t) = Q_0\,e^{i\omega t} \tag{B.79}$$

Assuming that $u(t) = U_0 e^{i\omega t}$, the equation of motion is

$$m\ddot{u} + c\dot{u} + ku = Q_0\,e^{i\omega t} \tag{B.80}$$

and its steady-state solution is

$$u(t) = \frac{Q_0\,e^{i\omega t}}{k - m\omega^2 + ic\omega} \tag{B.81}$$

Now consider the SDOF system of Figure B.18, which has no dashpot but which has a spring of complex stiffness $k^* = k_1 + ik_2$. The equation of motion for this system is

$$m\ddot{u} + k^* u = Q_0\,e^{i\omega t} \tag{B.82}$$

Again assuming that $u(t) = U_0 e^{i\omega t}$, the steady-state solution can be expressed as

$$u(t) = \frac{Q_0\,e^{i\omega t}}{k^* - m\omega^2} \tag{B.83}$$
