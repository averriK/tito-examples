# SLOT 1: Numerical R Algorithm for Instantaneous Shear Strain History

The algorithm estimates the instantaneous shear strain history $\gamma(z, t)$ at user-specified depths within a one-dimensional soil stratum by a two-step procedure: it first reconstructs the depth-varying acceleration field $a(z, t)$ from the base excitation record via analytical frequency-domain transfer functions, then integrates the resulting acceleration field vertically to obtain the shear strain at each instant. The physical domain is a stratum of thickness $H_s$ with power-law shear modulus $G(z) = G_o(\eta/H_s)^m$, where $\eta = H_s - z$ denotes depth below the free surface, $G_o = \rho c_o^2$ is the base shear modulus, and $m \in [0, 2)$ is the profile exponent [@Ref001]. Material damping with hysteretic ratio $\xi$ enters through the complex modulus $G^*(z) = G(z)(1 + 2i\xi)$, which replaces the real base wavenumber $k_o = \omega/c_o$ with its complex analogue $k_o^* = \omega/c_o^*$ where $c_o^* = c_o\sqrt{1 + 2i\xi}$ [@Ref001].

For the uniform stratum ($m = 0$), the governing wave equation reduces to the constant-coefficient form and the zero-stress free-surface condition yields the closed-form acceleration transfer function [@Ref001]:

$$H_a(z,\,\omega) = \frac{\cos(k^*\,\eta)}{\cos(k^*\,H_s)}, \qquad k^* = \frac{\omega}{c_o^*}, \quad \eta = H_s - z$$

For the general power-law profile ($0 < m < 2$), the substitution $\zeta(\eta) = 2k_o H_s/(2-m)\cdot(\eta/H_s)^{(2-m)/2}$ transforms the governing ordinary differential equation into Bessel's equation of order $\nu = (1-m)/(2-m)$; excluding the singular $Y_\nu$ component by the regularity condition at the free surface and enforcing the base boundary condition gives the acceleration transfer function [@Ref001]:

$$H_a(z,\,\omega) = \left(\frac{\eta}{H_s}\right)^{(1-m)/2} \frac{J_\nu\!\left[\zeta(\eta)\right]}{J_\nu\!\left[\zeta(H_s)\right]}, \qquad \nu = \frac{1-m}{2-m}$$

The time-domain acceleration at any depth is recovered by multiplying the base acceleration spectrum $A_g(\omega)$ by $H_a(z, \omega)$ and applying the inverse discrete Fourier transform. Both transfer functions are extended to include damping by evaluating $\zeta$ at the complex wavenumber $k_o^*$, while Bessel function values are computed at the real part of $\zeta$ -- a standard approximation that introduces errors of order $\xi^2$ in spectral amplitudes and is adequate for engineering damping ratios ($\xi \leq 0.2$) [@Ref001].

The shear strain $\gamma(\eta, t)$ is derived from $a(\eta, t)$ by integrating the equation of motion vertically from the free surface, where $\tau(H_s, t) = 0$, downward to depth $\eta$ [@Ref001]:

$$\gamma(\eta,\,t) = \frac{\rho}{G(\eta)} \int_0^{\eta} a(\eta',\,t)\,d\eta'$$

This expression is exact and model-independent: the shear stress $\tau = G\gamma$ at any level equals the total inertial force of the overlying soil column and does not depend on the specific form of $G(z)$ [@Ref001]. At the free surface ($\eta = 0$), the integral vanishes and $\gamma = 0$, consistent with the zero-stress boundary condition. For power-law profiles with $m \geq 1/2$, the factor $G^{-1}(\eta) \propto (\eta/H_s)^{-m}$ causes the linearized strain to amplify toward the free surface, while $\tau$ remains bounded for all $m < 2$ [@Ref001].

The R implementation provides two public functions. `computeAccelField` executes Step 1: it zero-pads the input acceleration to the next power of two, computes the discrete Fourier transform, evaluates $H_a$ at each frequency for every point on a user-supplied depth grid, multiplies point-wise, and returns the real part of the inverse DFT as a numeric matrix with rows indexing time and columns indexing depth. `computeStrainHistory` executes the full pipeline: it builds a uniform grid in $\eta$, calls `computeAccelField` on that grid, accumulates the trapezoidal sum along the depth axis at each time step to form the cumulative integral $\mathcal{I}(\eta_k, t_i) = \int_0^{\eta_k} a(\eta', t_i)\,d\eta'$, linearly interpolates $\mathcal{I}$ to the requested evaluation depths, divides by $G(\eta)/\rho$, and returns a long-format `data.table` keyed by depth and time.

```r
library(data.table)

## -----------------------------------------------------------------
## Private helpers
## -----------------------------------------------------------------

.buildOmega <- function(Nfft, Dt) {
  2 * pi * (0L:(Nfft - 1L)) / (Nfft * Dt)
}

.complexKo <- function(Omega, Co, Xi) {
  CoStar <- Co * sqrt(complex(real = 1, imaginary = 2 * Xi))
  Omega / CoStar
}

.accelTFUniform <- function(Omega, Eta, Hs, Co, Xi) {
  ## Uniform stratum: H_a = cos(k* eta) / cos(k* Hs)
  KStar  <- .complexKo(Omega, Co, Xi)
  Ha     <- cos(KStar * Eta) / cos(KStar * Hs)
  Ha[1L] <- 1 + 0i    # DC: unit static transfer
  Ha
}

.accelTFPowerLaw <- function(Omega, Eta, Hs, Co, M, Xi) {
  ## Power-law profile: H_a = (eta/Hs)^((1-m)/2) * Jnu(zeta(eta)) / Jnu(zeta(Hs))
  Nu     <- (1 - M) / (2 - M)
  KoStar <- .complexKo(Omega, Co, Xi)
  ZetaFn <- function(X) 2 * KoStar * Hs / (2 - M) * (X / Hs)^((2 - M) / 2)
  JnuEta <- besselJ(pmax(Re(ZetaFn(Eta)), 0), Nu)
  JnuHs  <- besselJ(pmax(Re(ZetaFn(Hs)),  0), Nu)
  Ha     <- (Eta / Hs)^((1 - M) / 2) * JnuEta / JnuHs
  Ha[1L] <- 1 + 0i
  Ha
}

## -----------------------------------------------------------------
## Step 1: acceleration field on a uniform depth-from-surface grid
## -----------------------------------------------------------------

#' Compute a(EtaGrid[j], t) for all t using closed-form transfer functions
#'
#' @param Ag       Base acceleration [m/s^2], length N
#' @param Dt       Time step [s]
#' @param Hs       Stratum thickness [m]
#' @param Co       Base shear wave velocity [m/s]
#' @param M        Profile exponent (0 = uniform; 0 < M < 2 = power-law)
#' @param Xi       Hysteretic damping ratio
#' @param EtaGrid  Depth-from-surface grid [m], length K
#' @return Numeric matrix [N x K]
computeAccelField <- function(Ag, Dt, Hs, Co, M, Xi, EtaGrid) {
  N      <- length(Ag)
  Nfft   <- 2L^ceiling(log2(N))
  Omega  <- .buildOmega(Nfft, Dt)
  AgFreq <- fft(c(Ag, rep(0, Nfft - N)))
  K      <- length(EtaGrid)
  Amat   <- matrix(0.0, nrow = N, ncol = K)
  for (J in seq_len(K)) {
    Ha        <- if (M == 0) .accelTFUniform(Omega, EtaGrid[J], Hs, Co, Xi)
                 else        .accelTFPowerLaw(Omega, EtaGrid[J], Hs, Co, M, Xi)
    Az        <- Re(fft(Ha * AgFreq, inverse = TRUE)) / Nfft
    Amat[, J] <- Az[seq_len(N)]
  }
  Amat
}

## -----------------------------------------------------------------
## Step 2: shear strain by cumulative depth integration
## -----------------------------------------------------------------

#' Compute gamma(z, t) at specified depths from the base
#'
#' gamma(eta, t) = (rho / G(eta)) * integral_0^eta a(eta', t) d eta'
#'
#' @param Ag       Base acceleration [m/s^2], length N
#' @param Dt       Time step [s]
#' @param Hs       Stratum thickness [m]
#' @param Co       Base shear wave velocity [m/s]
#' @param Rho      Mass density [kg/m^3]
#' @param M        Profile exponent (0 = uniform; 0 < M < 2 = power-law)
#' @param Xi       Hysteretic damping ratio
#' @param ZVec     Evaluation heights from base [m], values in [0, Hs]
#' @param NIntGrid Depth integration grid size (default 200)
#' @return data.table with columns: Time [s], Depth [m], ShearStrain [-]
computeStrainHistory <- function(Ag, Dt, Hs, Co, Rho, M, Xi, ZVec,
                                  NIntGrid = 200L) {
  ## Integration grid: uniform in eta = Hs - z (depth from surface)
  EtaInt <- seq(0, Hs, length.out = NIntGrid)
  DEta   <- EtaInt[2L] - EtaInt[1L]

  ## Step 1: acceleration field on integration grid
  Afield <- computeAccelField(Ag, Dt, Hs, Co, M, Xi, EtaInt)
  ## Afield[I, K] = a(EtaInt[K], T[I])

  N    <- nrow(Afield)
  TVec <- (seq_len(N) - 1L) * Dt

  ## Shear modulus profile on integration grid
  Go   <- Rho * Co^2
  Gvec <- if (M == 0) rep(Go, NIntGrid) else
            Go * (pmax(EtaInt, Hs * 1e-8) / Hs)^M

  ## Cumulative trapezoidal integral over depth:
  ## CumI[I, K] = integral_0^EtaInt[K] a(eta', T[I]) d eta'
  CumI <- matrix(0.0, nrow = N, ncol = NIntGrid)
  for (K in 2L:NIntGrid) {
    CumI[, K] <- CumI[, K - 1L] +
      0.5 * DEta * (Afield[, K - 1L] + Afield[, K])
  }

  ## Evaluate gamma at each requested output depth
  EtaOut  <- Hs - ZVec    # convert height from base to depth from surface
  NOut    <- length(ZVec)
  StrainM <- matrix(0.0, nrow = N, ncol = NOut)

  for (J in seq_len(NOut)) {
    EtaJ <- EtaOut[J]
    Gj   <- if (M == 0) Go else Go * max(EtaJ, Hs * 1e-8)^M / Hs^M
    Idx  <- min(max(findInterval(EtaJ, EtaInt), 1L), NIntGrid - 1L)
    Wt   <- (EtaJ - EtaInt[Idx]) / DEta
    IntJ <- (1 - Wt) * CumI[, Idx] + Wt * CumI[, Idx + 1L]
    StrainM[, J] <- Rho * IntJ / Gj
  }

  ## Assemble and return long-format data.table
  Result <- data.table(
    Time        = rep(TVec, times = NOut),
    Depth       = rep(ZVec, each  = N),
    ShearStrain = as.vector(StrainM)
  )
  setkey(Result, Depth, Time)
  Result
}
```

The implementation covers the uniform stratum ($m = 0$), the Gibson deposit ($m = 1$, which is a special case of the power-law branch), and the full power-law family ($0 < m < 2$) without changes to the calling interface. Near-surface numerical singularities for profiles with $m > 0$ are regularized by clamping $\eta$ to $10^{-8} H_s$ before evaluating $G^{-1}(\eta)$; this has no effect on strain values at engineering-relevant depths and correctly returns $\gamma = 0$ at the free surface where the integral also vanishes. The `NIntGrid` parameter controls integration resolution: 200 points is adequate for smooth input motions and stratum geometries typical of engineering site response analyses, and convergence may be verified by comparing results at doubled resolution for input records with significant high-frequency content [@Ref001].

The example below demonstrates the function call with a synthetic base acceleration record, a power-law profile with $m = 0.5$, and five evaluation heights spanning the full stratum thickness.

```r
## -----------------------------------------------------------------
## Example: m = 0.5 power-law profile, synthetic base acceleration
## -----------------------------------------------------------------

Hs  <- 20       # stratum thickness, m
Co  <- 200      # base shear wave velocity, m/s
Rho <- 1800     # mass density, kg/m^3
M   <- 0.5      # stiffness profile exponent
Xi  <- 0.05     # hysteretic damping ratio

set.seed(7L)
Dt <- 0.01
Ag <- rnorm(1000L, sd = 0.2)    # synthetic base acceleration, m/s^2

ZVec <- c(0, 5, 10, 15, 20)    # evaluation heights from base, m

StrainDT <- computeStrainHistory(Ag, Dt, Hs, Co, Rho, M, Xi, ZVec)

## Peak absolute shear strain at each depth
SummaryDT <- StrainDT[, .(PeakStrain = max(abs(ShearStrain))), by = Depth]
print(SummaryDT)
```
