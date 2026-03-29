# Structured Prompt: PSHA Equations for a Single Circular Areal Source

## Context

The analysis particularizes the equations of probabilistic seismic hazard analysis (PSHA) for a stable continental crust (SCC) region with no known finite faults. A single circular areal seismic source of radius $R$ (on the order of 600 km) surrounds the study site, with uniformly distributed seismicity. Contributions from any source beyond $R$ are considered negligible. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, an engineering minimum magnitude $M_{\min}$, and a maximum earthquake magnitude $M_{\max}$.

## SLOTS

### SLOT 1: Particularized annual exceedance rate in epsilon form

The particularized annual exceedance rate $\lambda_I(i^*)$ for the single circular areal source is derived starting from the general hazard integral, with source parameters $a$, $b$, and $M_{\max}$. The derivation incorporates the distance PDF $f_R(r)$ for a circular source with uniformly distributed seismicity (assumed available from a prior derivation) and the truncated-exponential magnitude PDF $f_M(m)$.

The hazard integral is reformulated in terms of the normalized residual $\epsilon$, such that the GMPE exceedance probability term $1 - \Phi(\cdot)$ is expressed through the standard normal PDF. All constant terms are factored outside the integral. The resulting expression displays the convolution of the standard normal function with the magnitude distribution function. The final integral remains stated in terms of $\epsilon$, with integration limits $R_{\min}$, $R_{\max}$, $M_{\min}$, and $M_{\max}$.

*Coverage: TASK_FILE lines 10-11. The reference to "$f_R(r)$ derived in question 1" indicates a dependency on a prior derivation; downstream workflows retrieve or re-derive this PDF as a preliminary step.*

### SLOT 2: Canonical MCE and disaggregation hazard equations

The hazard equations for the single circular areal source are stated in canonical form, expressed in terms of $\epsilon$ and a normalized standard normal PDF of the GMPEs, for two distinct applications:

- **MCE (Maximum Considered Earthquake):** the hazard equation governing the determination of the MCE ground motion level.
- **Disaggregation:** the disaggregation equation identifying the relative contributions of magnitude, distance, and $\epsilon$ to the hazard at a given exceedance level.

Both formulations build on the epsilon-based framework established in SLOT 1.

*Coverage: TASK_FILE line 12. The two targets (MCE and disaggregation) and the requirement for canonical form with a normalized normal GMPE PDF are explicitly stated.*

## CONSTRAINTS

- Output language is English, in professional engineering methodology style.
- All notation is consistent with the documents in `kb/`.
- Expressions are in closed-form analytical form where possible; any step requiring numerical integration is identified explicitly.
- The GMPE is treated generically: exceedance probability is expressed in terms of the median $\hat{\eta}_I(m,r)$ and the logarithmic standard deviation $\sigma_{\ln I}$, with no specific GMPE model assumed. Because the ground motion prediction model may represent an arbitrary ensemble, the formulation accommodates this generality.
- No site effects are included; the analysis applies to reference rock conditions.
