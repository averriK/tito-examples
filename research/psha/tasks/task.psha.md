DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)

El objetivo de este análisis es particularizar las ecuaciones de peligrosidad sísmica probabilística (PSHA) para el caso de una región continental estable (Stable Continental Crust), sin fallas finitas conocidas, con una única fuente sísmica areal circular de radio $R$ (del orden de 600 km) con sismicidad uniformemente distribuida, que rodea al sitio de estudio. El aporte de cualquier fuente externa más allá de $R$ se considera despreciable.

La fuente se caracteriza por los parámetros de Gutenberg-Richter $a$ y $b$, una magnitud mínima de ingeniería $M_{\min}$, y un sismo máximo $M_{\max}$.
Este análisis particulariza esas expresiones generales al caso de fuente única circular.

Todas las derivaciones deben usar la misma notación de los documentos en `kb/`. Las expresiones deben ser analíticas en forma cerrada cuando sea posible, indicando explícitamente cuándo se requiere integración numérica. No asumir una GMPE específica: expresar la probabilidad de excedencia en términos genéricos de la mediana $\hat{\eta}_I(m,r)$ y la desviación estándar $\sigma_{\ln I}$. No incluir efectos de sitio — el análisis es en roca de referencia.

Questions to answer:

1. Derive the probability density function of source-to-site distance $f_R(r)$ for a site located at the center of a circular areal source of radius $R$ with uniformly distributed seismicity. Justify geometrically from the differential area $dA = 2\pi r\,dr$, normalize over the domain $[0, R]$, and provide the cumulative distribution function $F_R(r)$.

2. Starting from the general hazard integral (@eq-hazard-integral in `kb/hazard.qmd`), develop the particularized annual exceedance rate $\lambda_I(i^*)$ for a single circular areal source with parameters $a$, $b$, $M_{\max}$, using the $f_R(r)$ derived in question 1. Explicitly state the annual occurrence rate $\nu_0 = 10^{a - b\,M_{\min}}$, the truncated Gutenberg-Richter magnitude PDF $f_M(m)$ (consistent with @eq-branch-pdf in `kb/uncertainty_model.qmd`), the conditional exceedance probability $P[I > i^* \mid m, r]$ through a generic GMPE, and the final double integral expression over $m$ and $r$.

3. Develop the expression that estimates the ground-motion intensity of the maximum credible earthquake (MCE) at the site. Consider an event with magnitude $M_{\max}$ at distance $r$, and derive the intensity $i^*_{\text{MCE}}$ such that its annual exceedance probability equals a target AEP (e.g., $\text{AEP} = 1/T_R$ for a given return period $T_R$). Link to the AEP relation from @eq-aep in `kb/hazard.qmd`.

4. Using the disaggregation framework from `kb/disaggregation.qmd` (@eq-disagg-rate, @eq-disagg-bin, @eq-disagg-prob), develop the joint $M$-$R$ disaggregation for the circular source. Present two formulations: (a) disaggregation by rate contribution — the fraction of $\lambda_I(i^*)$ attributable to each bin $(m_k, r_j)$, expressed as $\theta_{k,j}$; and (b) disaggregation including the $\varepsilon$ dimension of the GMPE residual, with contributions from bins $(m_k, r_j, \varepsilon_\ell)$ and the marginal distributions $P[M \in m_k \mid I > i^*]$ and $P[R \in r_j \mid I > i^*]$. For both formulations, particularize the PDFs and rates to the circular source with $a$, $b$, $M_{\max}$, and $f_R(r) = 2r/R^2$.
