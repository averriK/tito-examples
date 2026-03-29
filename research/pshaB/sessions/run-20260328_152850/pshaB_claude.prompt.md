# PSHA Equations for a Single Circular Areal Source

This prompt defines the scope and requirements for particularizing the probabilistic seismic hazard analysis (PSHA) equations to the case of a single circular areal source in a stable continental crust (SCC) region. The source region has radius $R$ (on the order of 600 km), uniformly distributed seismicity, and no known finite faults. Contributions from sources beyond $R$ are considered negligible. The source is characterized by Gutenberg-Richter parameters $a$ and $b$, a minimum engineering magnitude $M_{\min}$, and a maximum magnitude $M_{\max}$.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE lines 3-6, which describe the analysis objective, the stable continental crust setting, the single circular source geometry with radius R of order 600 km, uniform seismicity, negligible external contributions, and the Gutenberg-Richter parametrization with a, b, M_min, and M_max.]

## SLOTS

### SLOT 1: Derivation of the particularized annual exceedance rate in epsilon form

Starting from the general PSHA hazard integral, derive the particularized annual exceedance rate $\lambda_I(i^*)$ for a single circular areal source with Gutenberg-Richter parameters $a$, $b$, and maximum magnitude $M_{\max}$. The derivation must incorporate the distance probability density function $f_R(r)$ for a uniform circular source (assumed available from a prior derivation) and the magnitude probability density function $f_M(m)$.
^[Confidence: HIGH, Rationale: Directly paraphrases the first sentence of TASK_FILE line 11, which requests development of the "particularized annual exceedance rate lambda_I(i*) for a single circular areal source with parameters a, b, M_max, using the f_R(r) derived in question 1 and using the f_M(m)." The note that f_R(r) is assumed available reflects the reference to "derived in question 1," indicating a prior step outside this task file.]

Because the ground motion prediction model may represent an arbitrary ensemble, the hazard integral must be reformulated in terms of the normalized residual $\varepsilon$. The complementary CDF term $1 - \Phi(\cdot)$ in the standard hazard integral is to be recognized as corresponding to a normal probability density function with unit mean and standard deviation $\sigma$. All constant factors must be extracted from the integral, so that the integrand reduces to the convolution of a standard normal density with the magnitude distribution function. The final expression must be left as an integral in $\varepsilon$ with explicit limits $R_{\min}$, $R_{\max}$, $M_{\min}$, and $M_{\max}$.
^[Confidence: HIGH, Rationale: Paraphrases the remainder of TASK_FILE line 11, which instructs: express the hazard integral in terms of epsilon; the 1-Phi() term is a PDF with mean 1 and standard deviation sigma; factor out all constant terms; show the convolution of a standard normal function with the magnitude distribution; leave as an integral in terms of epsilon, R_min, R_max, M_min, M_max.]

### SLOT 2: Canonical hazard equations for MCE and disaggregation

Present the hazard equations for the single circular areal source in canonical form, expressed in terms of the normalized residual $\varepsilon$ and a normalized normal probability density function of the GMPE, for two distinct formulations: (a) the Maximum Considered Earthquake (MCE) hazard equation, and (b) the seismic hazard disaggregation equation.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 12, which requests presentation of "las ecuaciones de hazard para single source circular, en terminos de epsilon para el MCE y para la desagregacion, de manera canonica, expresadas en terminos de una PDF de los GMPE normal normalizada." Both the MCE and disaggregation cases, the canonical form requirement, and the normalized GMPE PDF specification are explicit in the source.]

## CONSTRAINTS

- The output document must be written in English, following a professional engineering methodology style.
^[Confidence: HIGH, Rationale: TASK_FILE line 1 states "DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)."]

- All notation must remain consistent with the notation used in the documents available in `kb/`.
^[Confidence: HIGH, Rationale: TASK_FILE line 8 requires "la misma notacion de los documentos en kb/."]

- Expressions must be in closed-form analytical form wherever possible. Any step or result that requires numerical integration must be explicitly identified as such.
^[Confidence: HIGH, Rationale: TASK_FILE line 8 states "Las expresiones deben ser analiticas en forma cerrada cuando sea posible, indicando explicitamente cuando se requiere integracion numerica."]

- The GMPE must remain generic throughout: exceedance probability is expressed in terms of the median ground-motion parameter $\hat{\eta}_I(m,r)$ and the logarithmic standard deviation $\sigma_{\ln I}$, without assuming any specific attenuation model.
^[Confidence: HIGH, Rationale: TASK_FILE line 8 states "No asumir una GMPE especifica: expresar la probabilidad de excedencia en terminos genericos de la mediana hat{eta}_I(m,r) y la desviacion estandar sigma_{ln I}."]

- No site effects are to be included; the analysis applies to reference rock conditions.
^[Confidence: HIGH, Rationale: TASK_FILE line 8 states "No incluir efectos de sitio -- el analisis es en roca de referencia."]

- The seismic source model consists of a single circular areal source of radius $R$ (on the order of 600 km) with uniformly distributed seismicity surrounding the study site, appropriate for a stable continental crust region with no known finite faults. Contributions from any external source beyond $R$ are considered negligible.
^[Confidence: HIGH, Rationale: Paraphrases TASK_FILE lines 3-5, which describe the SCC region, absence of finite faults, circular areal source of radius R of order 600 km, uniform seismicity, and negligible contribution from sources beyond R.]
