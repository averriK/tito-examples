# Structured Prompt: PSHA Report Analysis

## SLOTS

### SLOT 1: Seismotectonic Setting Analysis

Analyze the seismotectonic setting from chapters 3.0 and 4.0 of the PSHA report to answer:
- ¿Cuáles son los regímenes tectónicos que controlan la sismicidad de la zona en un radio de 1000 km a la redonda?
- ¿Todas las fuentes empleadas en el modelo son del tipo SCC?

### SLOT 2: Frequent Events Characterization (1/475 to 1/1000 years AEP)

For the considered region, determine:
- ¿Cuáles son las magnitudes "Características" y las distancias epicentrales de los eventos que controlan la amenaza para los eventos "frecuentes" de 1/475 a 1/1000 años de AEP?

### SLOT 3: Rare Events Characterization (1/5000 to 1/10,000 years AEP)

For the considered region, determine:
- ¿Cuáles son las magnitudes "Características" y las distancias epicentrales de los eventos que controlan la amenaza para los eventos "raros" de 1/5000 a 1/10,000 años de AEP?

### SLOT 4: Active Neotectonic Faults Identification

Investigate and answer:
- ¿Existen fallas activas neotectónicas identificadas en la región, a menos de 100 km del sitio?

### SLOT 5: Maximum Credible Earthquake (MCE) Consideration

Determine:
- ¿Se ha considerado el cálculo de un sismo máximo creíble MCE en el análisis para alguna fuente en particular?

### SLOT 6: Seismic Record Selection Executive Summary

From chapter 8.0 "EARTHQUAKE ACCELERATION TIME HISTORY DEVELOPMENT":
- Proporcióneme un resumen ejecutivo de cómo se seleccionaron los registros sísmicos para que sean compatibles con el sitio del proyecto.

### SLOT 7: Selection Criteria Adequacy for Continental Stable Region

Analyze the selection criteria provided in chapter 8.0 (Magnitude 7.3, Rupture distance 170 km, etc.):
- ¿Son adecuados estos criterios para el tipo tectónico (Continental Stable) de la región?

### SLOT 8: Rupture Distance Criteria Origin and Validity

Investigate:
- ¿De dónde salen los 170 km que se seleccionaron de Rupture Distance? ¿De la desagregación? ¿Para qué periodos de retorno es válido esto?

### SLOT 9: Rupture Parameters Verification in Tables 10 and 11

Examine the criteria "Depth-to-Top Rupture" and "Rupture plane dip 90":
- Los criterios de "Depth-to-Top Rupture" o "Rupture plane dip 90" sugieren que estos parámetros están disponibles en los catálogos públicos. ¿Puedes confirmar si estos criterios efectivamente fueron aplicados en la confección de las tablas 10 y 11?

### SLOT 10: Candidate Ground Motion Catalog Selection Process

Address point 3 from chapter 8.0 which mentions "A catalogue of candidate ground motion records":
- ¿Quién seleccionó a estos candidatos? ¿Con qué criterios?

### SLOT 11: Amplitude Scaling Factors Analysis

Point 4 mentions "Candidate ground motions were amplitude-scaled to be in general agreement with the target spectrum":
- ¿Cuáles son los factores de amplificación mínimos y máximos obtenidos en ese escalamiento?

### SLOT 12: State-of-the-Art on Amplitude Scaling

Review the literature and state-of-the-art:
- ¿Qué indica la bibliografía y el estado del arte para la amplificación de amplitudes en registros reales?
- ¿Es razonable aceptar factores de amplificación mucho mayores a 2 o mucho menores que 0.5? Cite bibliografía moderna que discuta límites sobre los factores de escala.

### SLOT 13: Tables 10 and 11 Selection Criteria Verification

Analyze the seismic record suite shown in tables 10 and 11:
- ¿Con qué criterio fueron seleccionados? ¿Cumplen con los criterios establecidos en el inicio del capítulo 8.0?

### SLOT 14: SCR Record Classification Confirmation

From tables 10 and 11:
- ¿Podrías confirmar de estas tablas, cuáles registros son efectivamente pertenecientes a regiones continentales estables SCR?

## CONSTRAINTS

- All responses and analysis generated from this task must be written in English.
- The structured prompt derived from this task, and all downstream research outputs, must be written in English.
- In the final research report, use one top-level `##` section per question/slot so that each question is answered in its own section.
