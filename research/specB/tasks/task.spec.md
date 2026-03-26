DOCUMENT IN ENGLISH (PROFESSIONAL ENGINEERING METHODOLOGY STYLE)

El propósito de esta investigación es formular un marco robusto de "spectral matching" de espectros de respuesta de pseudo aceleraciones horizontales Sa(Tn).


Las metodologías tradicionales de ajuste espectral (spectral matching) modifican los acelerogramas registrados para alcanzar conformidad con espectros de respuesta objetivo derivados del análisis de amenaza sísmica probabilista (PSHA, por sus siglas en inglés), pero al hacerlo alteran fundamentalmente el contenido de frecuencias, las características de duración y el número de reversiones de signo presentes en los registros de movimiento del suelo originales.  Además, el ajuste espectral tradicional  reduce el coeficiente de variación entre registros seleccionados, suprimiendo artificialmente la variabilidad registro-a-registro que refleja incertidumbre epistémica en características del movimiento del suelo 



La respuesta sísmica de sistemas que acumulan daño bajo carga cíclica depende no sólo de la amplitud máxima sino también de la duración y del número efectivo de ciclos, parámetros reconocidos explícitamente en métodos de evaluación del potencial de licuefacción [@Green2005]. El ajuste espectral en el dominio del tiempo o de la frecuencia distorsiona con frecuencia las características no estacionarias del movimiento del suelo y puede alterar parámetros escalares la intensidad de Arias [@Akkar2010]. Numerosos fenómenos físicos, incluidos la degradación de rigidez y la licuefacción, dependen del número de reversiones de carga. 

Pregunta: Resume brevemente las metodologias de seleccion de registros sismcos que modifan el contenido espectral para que la combinacion lineal de espectros sea "parecida" al espectro objetivo. 
PRegunta: segun esta metodologia, cuantos espectros se necesitan como minimo para lograr el match? De donde vienen los 7 u 11 registros minimos recomendados por algunas normativas como el ASCE-7, en la seleccion de registros sismicos para analisis no lineal de estructuraS? 




Imagina que tenemos K espectros sísmicos k=1..K, cada espectro está definido por  Sa_k(Tn) ordenadas, con n=1..N ordenadas espéctrales y valores de Sa(Tn). 
Imagina que tenemos un espectro "objetivo" derivado del PSHA Sa*(Tn) evaluado en los mismos periodos.  

Dado un conjunto candidato de $m$ espectros Sa(Tn) y una malla de períodos de $n$ puntos $\{T_1,\dots,T_n\}$,
Sea el espectro objetivo derivado del PSHA se codifica como el vector $\mathbf{y}\in\mathbb{R}^n$ con componentes $y_i=\ln S_a^{\mathrm{obj}}(T_i)$

 Quiero construir una combinación lineal de espectros  Sa(Tn) que minimice el error respecto del espectro objetvo. Es decir, quiero encontrar el conjunto de pesos w_k tal que la diferencia combinación lineal de los espectros Sa(Tn) menos Sa_*(Tn) sea minima
Pregunta: Formula el problema como un problema clasico de regresion lineal, donde se buscan los pesos w que minimizan el error global RMSE. Emplea la notacion anterior


Contexto
En el espacio Log(Sa) - Log(Tn), las funciones son más suaves. 
Pregunta: formula el mismo problema anterior en el espacio log-log en esta notación.

Contexto:  Desde el punto de vista matemático, el conjunto de K espectros minimiza el error respecto del espectro objetivo. Imagina ahora que algunos pesos son negativos. 
Pregunta: Extiende el problema de regresión lineal en donde se busquen únicamente los pesos positivos. ¿Implementa la solución? ¿Es posible resolverlo directamente con Ridge pidiendo la restricción de pesos positivos? Proponga un ejemplo de código en R. 


Contexto: Imagina ahora que ademas de pedir que los pesos sean positivos, también ponemos restriccions al tamaño de los pesos Supongamoque que no quier ofactores w mayores a w_max ni factores menores a w_min. 
Pregunta: extiende la formulacion del problerma para limitar los tamanos de los pesos. ¿Es posible aplicar Ridge/Lasso para esto? propon un ejemplo

Pregunta: Esp osible plantear generalizar este problema matematico a un problema de optimizacion convexa,? Propon la funcion de perdida que debo plantea.r Dame ejemplos mediante librerias estandar de R.
