DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)

El propósito de esta investigación, es formular un modelo simple proxy, para predecir el incremento de presión de poros de un material con finos saturados,sometidos a un registro sísmico de aceleraciones. 
Contexto:
Para un estrato de espesor $H_s_$ de un material homogéneo, con rigidez variable con la profundidad $Go(z)$ con un valor máximo en su base $G_o=G(z=0)$, fino, saturado, apoyado sobre roca, y sometido a aceleraciones en su base $a_g(t)$, la carpeta KB/ presenta las diferentes formulaciones analíticas (closed-form solutions) de la respuesta de sitio en términos de aceleraciones instantáneas $a(t,z)$ en diferentes puntos del estrato. 

Pregunta:
¿Cuáles son las estrategias numéricas para estimar la distorsión máxima a lo largo del evento sísmico? RMS? max max? presenta pros y contras 

Pregunta:
Presenta un resumen de los métodos empíricos que estiman el incremento de presión de poros de manera empírica a partir de un PGA y una magnitud, solo a modo de referencia resumido


Pregunta:
¿Cuáles son las estrategias para la implementación numérica (closed form or numerical solutions) que, basado en una historia de aceleraciones en la base $a_g_(z,t)$, que permiten estimar la presión de poros o el exceso de presión de poros en un punto del estrato de finos a partir de una distorsión instantánea $\gamma(z,t)$ y las propiedades geotenicas? 

Pregunta: ¿Qué librerías en R o Python están disponibles para analizar el incremento de presión de poros mediante modelos constitutivos avanzados como el PMForSand? ¿Cómo es posible implementar esos algoritmos en el workflow de un análisis 1D de respuesta de sitio mediante distorsiones instantáneas o mediante los valores RMS?


Pregunta:
En un problema de licuaion en 1D, analizado mediante distorsiones instantanesas, ¿cuales son los criterios para definir una "Extension" de zonas donde se exceden las presiones de poro y el factor de segurodad es menor que 1? ¿Es lo mismo que "falle" un punto que la falla de un 30% del espesor del estrato? ¿Es lo mismo que fallen zonas en profundad, que la falla de zonas superficiales? Cuales son los criterios de diseño y analisis del potencial de licuacion que permiten definir la falla global de un estrato?





