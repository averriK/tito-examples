**(B.4)**

mu cu ku t

= + or substituting and rearranging, ( ) ( ) ( ) u t u t u t t b

+ + = −  mub

**(B.5)**

mu cu ku

FIGURE B.6 Damped SDOF system subjected to base shaking.

In other words, the response of the system to base shaking is equivalent to the response that the system would have if its base was fixed and the mass was subjected to an external load $Q(t) = -m\ddot{u}_b(t)$. Thus any solutions for the response of an SDOF system subjected to external load can be used to evaluate the response of the system to base shaking.

## B.5 Response of Linear SDOF Systems

To evaluate the dynamic response of a linear SDOF system, the differential equation of motion must be solved. There are several types of conditions under which the dynamic response of SDOF systems are commonly calculated. Forced vibration occurs when the mass is subjected to some external loading, Q(t). The loading may be periodic or nonperiodic and it may correspond to an actual physical force applied to the mass or to some known level of base shaking. Free vibration occurs in the absence of external loading or base shaking. It may result from the release of the mass from some initial displacement or may occur after some transient forced vibration has ended. The following sections will develop solutions to the equation of motion for cases in which damping is and is not present, and for cases in which external loading is and is not present. The resulting four permutations of these conditions are:

1. Undamped free vibrations: c = 0, Q(t) = 0
2. Damped free vibrations: c > 0, Q(t) = 0
3. Undamped forced vibrations: c = 0, Q(t) ≠ 0
4. Damped forced vibrations: c > 0, Q(t) ≠ 0

The solution of the equation of motion for each of these conditions will be presented in turn.

### B.5.1 Undamped Free Vibrations

An SDOF system undergoes free vibration when it oscillates without being acted upon by any external loads. When damping is not present (c = 0) the equation of motion (for undamped free vibration) reduces to

+ =

**(B.6)**

mu ku

or after dividing both sides by the mass,

k + =

**(B.7)**

u m u

The solution to this simple differential equation can be found in any elementary text on differential equations as

k k = + sin cos mt

**(B.8)**

u C mt C

where the values of the constants C1 and C2 depend on the initial conditions of the system. The quantity $\sqrt{k/m}$ is very important — it represents the undamped natural circular frequency of the system:

$$\omega = \sqrt{\frac{k}{m}}$$

**(B.9)**

The undamped natural frequency, $f_0$, and undamped natural period of vibration, $T_0$, can be written as

$$f = \frac{\omega}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

**(B.10)**

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$$

**(B.11)**

$\omega$ is usually expressed in radians/sec and $f_0$ is expressed in cycles/sec, or Hz (Hertz). Substituting Equation (B.9) into the solution for the equation of motion [Equation (B.8)] yields

= ω + ω sin cos t

**(B.12)**

u C t C

which indicates that an undamped system in free vibration will oscillate harmonically at its undamped natural frequency. C1 and C2 can be evaluated by assuming the initial (t = 0) conditions to be represented by an initial displacement, u0, and initial velocity, $\dot{u}_0$. Then

= + = sin(0) cos(0) C u C C

= ω − ω = ω  C cos(0) sin(0) u C C

Therefore $C_2 = u_0$ and $C_1 = \dot{u}_0/\omega$, so the complete solution to the undamped free vibration response of an SDOF system is given by

sin u = + ω ω cos t

**(B.13)**

u t u ω

The response of such a system is shown in Figure B.7. Referring back to Equation (A.1), the free vibration response can also be expressed as

$u(t) = A\sin(\omega t + \phi)$

**(B.14)**

FIGURE B.7 Time history of undamped free vibration with initial displacement, u0, and initial velocity, $\dot{u}_0$.

where the amplitude, A, and phase angle, ϕ, are given by

+    u = A u   ω

° −u φ = tan 1  u

The solution to the equation of motion of an undamped system indicates that the response of the system depends on its initial displacement and velocity. Note that the amplitude remains constant with time. Because no energy is lost in an undamped system, it will continue to oscillate forever. Obviously, truly undamped systems do not exist in the real world; however, some systems can have such low damping that their response over short periods of time may approximate that of an undamped system.

### B.5.2 Damped Free Vibrations

In real systems, energy may be lost as a result of friction, heat generation, air resistance, or other physical mechanisms. Hence the free vibration response of a damped SDOF system will diminish with time. For damped free vibrations, the equation of motion is written as

+ + =

**(B.15)**

mu cu ku

or, dividing by m and substituting $\omega^2 = k/m$ [from Equation (B.9)], we have

c + ω + ω =

2 2

**(B.16)**

u u u km

The quantity $2\sqrt{km}$, called the critical damping coefficient, $c_c$, allows the damping ratio, ξ, to be defined as the ratio of the damping coefficient to the critical damping coefficient, i.e.,

° c c c c ξ = = = =

**(B.17)**

° c m k km c

With this notation, the equation of motion can be expressed as

+ ξω + ° =

**(B.18)**

u u u

The solution of this differential equation of motion depends on the value of the damping ratio. When ξ < 100% (c < cc), the system is said to be underdamped. When ξ = 100% (c = cc), the system is critically damped, and when ξ > 100% (c > cc) the system is overdamped. Separate solutions must be obtained for each of the three cases, but structures of interest in earthquake engineering are virtually always underdamped. For the case in which damping is less than critical, the solution to the equation of motion is of the form

$$u(t) = e^{-\xi\omega t}\bigl(C_1\sin(\omega_d t) + C_2\cos(\omega_d t)\bigr)$$

**(B.19)**

Note the exponential term by which the term in brackets is multiplied. This exponential term gets smaller with time and eventually approaches zero, indicating that the response of an underdamped system in free vibration decays exponentially with time. The rate of decay depends on the damping ratio — for small ξ the response decays slowly and for larger ξ the response decays more quickly. Defining the damped natural circular frequency of the system as $\omega_d = \omega\sqrt{1-\xi^2}$, the solution can be expressed as

$$u(t) = e^{-\xi\omega t}(C_1\sin\omega_d t + C_2\cos\omega_d t)$$

**(B.20)**

The natural frequency of a damped system is always lower than that of an undamped system, and it decreases with increasing damping ratio. The coefficients C1 and C2 can be determined from the initial conditions in the same manner as for the undamped case. The initial displacement and velocity are

[ ] − ξω = + = (0) C sin(0) cos(0) u e C C

[ ] [ ] − ξω − ξω = ω ω − ω ω − ξω ω + ω (0) (0)  cos (0) sin (0) sin (0) cos (0) u e C C e C C d d d d d d = ω − ξω C C d

Therefore $C_2 = u_0$ and $C_1 = (\dot{u}_0 + \xi\omega u_0)/\omega_d$, so the solution for damped free vibrations can be expressed as

  + ξω  u u − ξω = ° + ° t sin cos

**(B.21)**

u e t u t   d d ° d

The free vibration response of an underdamped system is shown in Figure B.8. Note the exponential decay of displacement amplitude with time. The ratio of the amplitudes of any two successive peaks will be

  πξ ω u n = exp 2

**(B.22)**

  ω u + n d

Defining the logarithmic decrement as $\delta = \ln(u_n/u_{n+1})$; then

° ω π ° δ = π =

**(B.23)**

ω − ° d

Rearranging allows the damping ratio to be determined from the logarithmic decrement:

FIGURE B.8 Time history of damped free vibration with initial displacement, u0, and initial velocity, $\dot{u}_0$.

° ξ =

**(B.24)**

π + °

For small values of δ, ξ ≈ δ/(2π). Therefore, a simple way to estimate the damping ratio of an SDOF system is to perform a free vibration test, in which the logarithmic decrement is measured when a system is displaced by some initial displacement, u0, and released with initial velocity $\dot{u}_0 = 0$.

### B.5.3 Response of SDOF Systems to Harmonic Loading

An SDOF system is said to undergo forced vibration when acted upon by some external dynamic force, Q(t). Dynamic loading may come from many different sources and may be periodic or nonperiodic. For problems of soil and structural dynamics, the response to harmonic loading is very important. One form of simple harmonic loading can be expressed as $Q(t) = Q_0\sin\omega t$, where Q0 is the amplitude of the harmonic load and ω is the circular frequency at which the load is applied.

#### B.5.3.1 Undamped Forced Vibrations

The equation of motion for an undamped system subjected to such simple harmonic loading is

+ = ω  t

**(B.25)**

sin mu ku Q

The general solution to this equation of motion is given by the sum of the complementary solution (for the homogeneous case in which the right side of the equation is zero) and the particular solution [which must satisfy the right side of Equation (B.25)]. The homogeneous equation is

+ =  mu ku

so the complementary solution is simply the solution to the undamped free vibration problem

= ω + ω ( ) sin cos

**(B.26)**

u t C t C t c

The portion of the response described by the complementary solution is that which results from the initial conditions of the system. It consists of a simple harmonic oscillation at the undamped natural frequency of the system. The particular solution describes the portion of the response caused by the external loading. This portion of the response can be assumed to be of the same form and to be in phase with the harmonic loading (because of the condition of zero damping); thus

= ω ( ) sin

**(B.27)**

u t U t p

where U0 is the amplitude of the harmonic response. Substituting Equation (B.27) into Equation (B.25) yields

− ω ω + ω = ω sin sin sin t

**(B.28)**

m U t kU t Q

Substituting $k/m = \omega^2$ and rearranging gives

/ / Q k Q k = =

**(B.29)**

U − ω ω − ° /

where β = ω/ω0 is referred to as the tuning ratio. Now the general solution of the equation of motion can be obtained by combining the complementary and particular solutions:

/ Q k = + = ω + ω + ω ( ) ( ) ( ) sin cos

**(B.30)**

sin u t u t C t C t t u t c p − °

The general solution must satisfy the initial conditions. From Equation (B.30), the velocity can be written as

/ Q k du = = ω ω − ω ω + ω ω ( ) cos t

**(B.31)**

cos sin C t C t u t − ° dt

For a given initial displacement, u0, and initial velocity, $\dot{u}_0$,

/ Q k = ω + ω + ω = sin (0) cos (0) sin (0) C

**(B.32)**

u C C − °

and

/ Q k / Q k = ω ω − ω ω + ω ω = ω + ω  cos (0)

**(B.33)**

cos (0) sin (0) C C u C − ° − °

from which

( ) ( )  = − − ω β  / / 1 u Q k °  u Q = −

**(B.34)**

C ( ) ω ω ° − k

Now the general response can finally be written as

  °  / u Q Q k   ω ω ω + + = − t

**(B.35)**

sin cos sin t u t u ( ) ° − ω ° −   k

It is interesting to consider the case in which the system is initially at rest in its equilibrium position (i.e., $u_0 = \dot{u}_0 = 0$). For this case, the response is given by

Q ( ) = ω − β ° sin sin t

**(B.36)**

u t − β k

which indicates that the response has two components. One component occurs in response to the applied loading and occurs at the frequency of the applied loading. The other is a free vibration effect induced by the initial conditions; it occurs at the natural frequency of the system. It is useful to realize that the term Q0/k in Equation (B.36) represents the displacement of the mass that would occur if the load Q0 was applied statically. The term 1/(1 − β2) can then be thought of as a magnification factor that describes the amount by which the static displacement amplitude is modified by the harmonic load. The magnification factor varies with the tuning ratio, β, as shown in Figure B.9. Note that the displacement amplitude is greater than the static displacement for loading frequencies lower than $2\omega_0$. At higher loading frequencies, the displacement amplitude is less than the static displacement and can become very small at high frequencies. However, the response of an undamped SDOF system becomes very large as ω approaches ω0. When harmonic loading is applied at the natural frequency of an undamped SDOF system, the response goes to infinity indicating resonance of the system. However, since truly undamped systems do not exist, true resonance is never really achieved. The concept of the tuning ratio that relates the frequency of loading to the natural frequency of the system is an important one, as evidenced by its strong influence on the response.

FIGURE B.9 Variation of magnification factor with tuning ratio for undamped SDOF system.

#### B.5.3.2 Damped Forced Vibrations

The most general case is that of a damped system subjected to forced harmonic loading. Each of the three prior cases can be considered as a subset of this one since their equations of motion can be obtained by setting various terms of the equation of motion for damped forced vibrations shown below to zero. The equation of motion for a damped SDOF system subjected to simple harmonic loading of the form $Q(t) = Q_0\sin\omega t$ is

+ + = ω   t

**(B.37)**

sin mu cu ku Q

After dividing by m and using the relationships $\xi = c/(2m\omega)$ and $\omega^2 = k/m$, Equation (B.37) can be rewritten as

Q + ξω + ° = °   sin t

**(B.38)**

u u u m

The complementary solution represents the damped free vibration response, which was expressed for an underdamped system by Equation (B.20).

$$u_c(t) = e^{-\xi\omega t}(C_1\sin\omega_d t + C_2\cos\omega_d t)$$

**(B.39)**

Since the response of a damped SDOF system is generally out of phase with the external loading, a harmonic particular solution of the form

= ω + ω ( ) sin cos **(B.40a)** u t C t C t p

can be assumed. The corresponding velocity and acceleration are

= ω ω − ω ω ( ) **(B.40b)** cos sin u t C t C t p

= − ω ω − ω ω ( ) **(B.40c)** sin cos u t C t C t p

Substituting Equations (B.40) into the equation of motion [Equation (B.38)] and grouping the sinωt and cosωt terms gives

( ) ( ) Q ω − ω − ξω ω ω + ω − ω + ω ξω ω = ω sin cos sin t **(B.41)** C C C t C C C t m

Now, at the instances where t = nπ/ω (where n is any positive integer), sinωt = 0 and cosωt = ±1. Thus the relationship

ω − ω + ω ξω = **(B.42a)** C C C

must be satisfied. Further, at t = π/2 + nπ/ω, sinωt = ±1 and cosωt = 0, which means that

Q ω − ω − ξω ω = m **(B.42b)** C C C

Equations (B.42) represent two simultaneous equations with the two unknowns C3 and C4. Solving for the unknowns yields

− β Q = **(B.43a)** C ( )

2 2

k − + ξβ β (2 )

− ξβ Q = **(B.43b)** C ( )

2 2

k − + ξ° β (2 )

The general solution to the equation of motion for damped forced vibration can now be obtained by combining the complementary and particular solutions:

( ) Q ( )  − t e−ξω t C = ω + ω + β ω t − ξβ ω ( ) sin cos sin cos u t d t C d t ( )

2 2

k − β + ξ° (2 )

**(B.44)**

where the constants C1 and C2 depend on the initial conditions. There are several important characteristics of this solution. Note that the complementary solution (which represents the effects of the initial conditions) decays with time. The complementary solution therefore describes a transient response caused by the requirement of satisfying the initial conditions. After the transient response dies out, only the steady-state response described by the particular solution remains. The steady-state response occurs at the frequency of the applied harmonic loading but is out of phase with the loading. The steady-state response could also be described by

$u(t) = A\sin(\omega t + \phi)$

**(B.45)**

where

Q = A ( ) k

2 2

− β + ξβ (2 )

  ξβ − φ = − tan   − β
