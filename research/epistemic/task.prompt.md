# STRUCTURED PROMPT

## CONSTRAINTS

- Output MUST be in English (US)
- Structure: one section (##) per question
- There are six questions total

## SLOTS

### SLOT 1: Fault activity classification

De acuerdo a tus análisis en KB, ¿qué tipo de actividad puede asociarse a la falla Reitfontein Fault? ¿Es una falla paleosísmica o neotéctonica?

### SLOT 2: Recent activity evidence (35,000 years)

Con base en los hallazgos del KB, ¿hay alguna evidencia que permita afirmar que Reitfontein Fault tuvo actividad en los últimos 35.000 años?

### SLOT 3: Logic tree weight for Mmax=7.2

En un árbol lógico para Mmax, ¿Qué peso asignarías a $M_{max}=7.2$, el valor asumido en el reporte de PSHA?

### SLOT 4: Compatible slip-rates and logic tree

Con base en los hallazgos del KB y en el entorno sismotectónico regional (Corteza Continental Estable), ¿cuál sería el rango de slip-rates compatible con una falla de este tipo? ¿Propones un árbol lógico para las slip-rates?

### SLOT 5: Seismic movement probability in return periods

El rango de slip-rates que sugieres en la pregunta anterior, ¿Permite suponer que esta falla podría tener movimientos sísmicos en períodos de retorno menores a 1/10,000 años?

### SLOT 6: Gutenberg-Richter parameters and b-value logic tree

¿Cuáles serían los parámetros de Gutenberg-Richter y, en particular, cuál sería el rango de valores "b" que asignarías a una falla de este tipo? En un árbol lógico, ¿qué propones?

## CONTEXT

Objetivo: El reporte PSHA de South Deep considera la falla "Reitfontein Fault" capaz de producir un evento de Mmax=7.2, pero tiene una alta incertidumbre epistémica. El objetivo de esta investigación es recomendar valores basados en árboles lógicos para diferentes parámetros asociados a la existencia de un evento de 7.2, con una ruptura de 64 km en un período de retorno menor a 1/10,000 años.
