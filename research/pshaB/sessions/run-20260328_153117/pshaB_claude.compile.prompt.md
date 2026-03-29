# PSHA Equations for a Single Circular Areal Source

This prompt defines the scope and requirements for particularizing the probabilistic seismic hazard analysis (PSHA) equations to the case of a single circular areal source in a stable continental crust (SCC) region. The source region has radius $R$ (on the order of 600 km), uniformly distributed seismicity, and no known finite faults. Contributions from sources beyond $R$ are considered negligible. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, a minimum engineering magnitude $M_{\min}$, and a maximum magnitude $M_{\max}$.


## SLOTS

### SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

Starting from the general PSHA hazard integral, derive the particularized annual exceedance rate $\lambda_I(i^*)$ for a single circular areal source with Gutenberg-Richter parameters $a$, $b$, and maximum magnitude $M_{\max}$. The derivation must incorporate the distance probability density function $f_R(r)$ for a uniform circular source (assumed available from a prior derivation) and the magnitude probability density function $f_M(m)$.


Because the ground motion prediction model may represent an arbitrary ensemble, the hazard integral must be reformulated in terms of the normalized residual $\varepsilon$. The complementary CDF term $1 - \Phi(\cdot)$ in the standard hazard integral is to be recognized as corresponding to a normal probability density function with unit mean and standard deviation $\sigma$. All constant factors must be extracted from the integral, so that the integrand reduces to the convolution of a standard normal density with the magnitude distribution function. The final expression must be left as an integral in $\varepsilon$ with explicit limits $R_{\min}$, $R_{\max}$, $M_{\min}$, and $M_{\max}$.


### SLOT 2: Canonical hazard equations for MCE and disaggregation

Present the hazard equations for the single circular areal source in canonical form, expressed in terms of the normalized residual $\varepsilon$ and a normalized normal probability density function of the GMPE, for two distinct formulations: (a) the Maximum Considered Earthquake (MCE) hazard equation, and (b) the seismic hazard disaggregation equation.


## CONSTRAINTS

- The output document must be written in English, following a professional engineering methodology style.


- All notation must remain consistent with the notation used in the documents available in `kb/`.


- Expressions must be in closed-form analytical form wherever possible. Any step or result that requires numerical integration must be explicitly identified as such.


- The GMPE must remain generic throughout: exceedance probability is expressed in terms of the median ground-motion parameter $\hat{\eta}_I(m,r)$ and the logarithmic standard deviation $\sigma_{\ln I}$, without assuming any specific attenuation model.


- No site effects are to be included; the analysis applies to reference rock conditions.


- The seismic source model consists of a single circular areal source of radius $R$ (on the order of 600 km) with uniformly distributed seismicity surrounding the study site, appropriate for a stable continental crust region with no known finite faults. Contributions from any external source beyond $R$ are considered negligible.

