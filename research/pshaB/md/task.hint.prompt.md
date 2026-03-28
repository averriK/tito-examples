# Structured Prompt: PSHA Equations for a Single Circular Areal Source

## Context

This analysis particularizes the general probabilistic seismic hazard analysis (PSHA) equations for a stable continental crust region with no known finite faults. The seismic source model consists of a single circular areal source of radius $R$ (on the order of 600 km) with uniformly distributed seismicity, centered on the study site. Contributions from any source beyond radius $R$ are considered negligible. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, a minimum engineering magnitude $M_{\min}$, and a maximum earthquake magnitude $M_{\max}$. The general PSHA expressions are particularized to this single circular source case.

## SLOTS

### SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

This slot covers the derivation of the particularized annual exceedance rate $\lambda_I(i^*)$ for the single circular areal source, starting from the general hazard integral. The derivation uses the distance probability density function $f_R(r)$ appropriate for the circular source geometry (as derived in a prior step) together with the magnitude probability density function $f_M(m)$, and the source parameters $a$, $b$, and $M_{\max}$. Because the ground motion prediction model may constitute an arbitrary ensemble, the hazard integral is reformulated in terms of the variable $\varepsilon$, recognizing that the complementary standard normal cumulative distribution term $1 - \Phi(\cdot)$ corresponds to a probability density function with unit mean and standard deviation $\sigma$. All constant terms are factored outside the integral to expose the core expression as a convolution of the standard normal probability density function with the magnitude distribution function. The final result is a well-posed integral expressed in terms of $\varepsilon$, with explicit integration limits $R_{\min}$, $R_{\max}$, $M_{\min}$, and $M_{\max}$.

### SLOT 2: Canonical hazard equations for MCE and disaggregation

This slot covers the presentation of the hazard equations for the single circular areal source in canonical form, expressed in terms of $\varepsilon$, for two distinct applications: (a) the Maximum Considered Earthquake (MCE) determination and (b) seismic hazard disaggregation. Both formulations are expressed in terms of a normalized normal probability density function associated with the ground motion prediction equations.

## CONSTRAINTS

- The output document is in English, following a professional engineering methodology style.
- All derivations employ notation consistent with the documents in `kb/`.
- Expressions take closed-form analytical form wherever possible; any step requiring numerical integration is identified explicitly.
- No specific ground motion prediction equation (GMPE) is assumed; exceedance probabilities are expressed generically in terms of the median ground motion $\hat{\eta}_I(m,r)$ and the logarithmic standard deviation $\sigma_{\ln I}$.
- No site effects are included; the analysis applies to reference rock conditions.

