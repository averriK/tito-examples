
Contexto: Tengo un array de N perforaciones con una carga única q, de explosivo. Además, tengo una secuencia de detonación que determina qué barreno se detona en determinado instante de tiempo. Las detonaciones que ocurren en cierto intervalo de tiempo determinan lo que se denomina "carga máxima por delay". Entiendo que la carga máxima por delay de todos los intervalos en que se solapan estas detonaciones se denomina MIC, máxima carga instantánea.
Pregunta: ¿Cómo se define la distancia de "Burden"?
Pregunta: ¿Por qué se usa 8 ms en las guías para definir la ventana de tiempo?
Pregunta: ¿Qué influencia tiene la distancia de Burden en el tiempo de detonación (delay) entre una detonación y la siguiente?
Pregunta: ¿Cómo se calcula el MIC en un array de N pozos con carga constante q? Entiendo que es agrupando todas las detonaciones que ocurren dentro de la ventana, pero pregunto, ¿este valor no depende de la velocidad de propagación de la onda? ¿Es ese el motivo? ¿Por qué 8 ms?
Pregunta: Define un algoritmo en R, robusto, usando data.table(), que permita calcular el MIC en un dataset dado, asumiendo datos cuando el usuario no los proporcione.
Pregunta: define librerías en R y Python que me permitan validar el cálculo mío del MIC contra librerías o algoritmos robustos.


Constraints: Las respuestas deben estar en inglés. El estilo debe seguir una forma de metodolgía para implementar

