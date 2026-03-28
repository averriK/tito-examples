DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)

El objetivo de este análisis es particularizar las ecuaciones de peligrosidad sísmica probabilística (PSHA) para el caso de una región continental estable (Stable Continental Crust), sin fallas finitas conocidas, con una única fuente sísmica areal circular de radio $R$ (del orden de 600 km) con sismicidad uniformemente distribuida, que rodea al sitio de estudio. El aporte de cualquier fuente externa más allá de $R$ se considera despreciable.

La fuente se caracteriza por los parámetros de Gutenberg-Richter $a$ y $b$, una magnitud mínima de ingeniería $M_{\min}$, y un sismo máximo $M_{\max}$.
Este análisis particulariza esas expresiones generales al caso de fuente única circular.

Todas las derivaciones deben usar la misma notación de los documentos en `kb/`. Las expresiones deben ser analíticas en forma cerrada cuando sea posible, indicando explícitamente cuándo se requiere integración numérica. No asumir una GMPE específica: expresar la probabilidad de excedencia en términos genéricos de la mediana $\hat{\eta}_I(m,r)$ y la desviación estándar $\sigma_{\ln I}$. No incluir efectos de sitio — el análisis es en roca de referencia.

Questions to answer:
Starting from the general hazard integral develop the particularized annual exceedance rate $\lambda_I(i^*)$ for a single circular areal source with parameters $a$, $b$, $M_{\max}$, using the $f_R(r)$ derived in question 1 and using the $f_M(m)$.  Debido aque el modelo de prediccion del movimiento sismico puede ser un ensemble arbitrario, expresa la integral del hazard en terinos de epsilon, donde el termino 1-$\Phi()$ es en realiddad una PDF con media 1 y desvio sigma. Saca todos los terminos constantes fuera de la integral y deja en evidencia la expresion de la integral de una funcion normal estandar convolucionada con la funcion de distribucion de la magnitid. DEja planteada una integral en terminos de epsilon, Rmin Rmax Mmin Mmax
Presenta las ecuaciones de hazard para single source circular, en terminos de epsilon para el MCE y para la desagregacion, de manera canonica, expresadas en terminos de una PDF de los GMPE normal normalizada.