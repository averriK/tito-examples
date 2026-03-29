# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## Context

This prompt structures the requirements for an executive memo presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A reference document summarizing the methodology exists in the `kb/` directory; it is noted as poorly written and poorly organized, and may serve as a starting point for downstream research and synthesis workflows.
^[Confidence: HIGH, Rationale: The memo topic is stated explicitly in TASK_FILE line 3 ("un memo ejecutivo que presente la metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud"). The KB reference and its quality assessment are stated in TASK_FILE line 5.]

## SLOTS

### SLOT 1: Problem Introduction

Prepare an introductory section framing the central problem: selection of a performance-based horizontal seismic coefficient ($k_h$) for pseudo-static slope stability analysis. The coefficient is calibrated to (a) a target seismic intensity level, which relates to the degree of consequences associated with slope failure, and (b) the physical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 7, which requests "una seccion que introduzca el problema" and specifies calibration targets: a target intensity level related to failure consequences, and slope characteristics including stiffness ("rigidez"), strength ("resistencia"), and fundamental periods ("periodos fundamentales").]

### SLOT 2: State of Current Practice

Prepare a state-of-practice section surveying the standards, guidelines, and professional recommendations that govern performance-based seismic design of slopes through limit-equilibrium models. The survey identifies relevant normative frameworks and practice documents currently in use.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests "una seccion de estado actual de la practica" and specifies investigating "normativas, guidelines y recomendaciones para el diseno sismico de taludes basado en performance mediante modelos de equilibrio limite."]

### SLOT 3: Newmark Displacement Analysis Methods

Prepare a section summarizing the Newmark displacement analysis methodologies employed in the overall approach. The section defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each category.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a summary of "las metodologias de analisis de desplazamientos de newmark" together with definitions of the rigid-block and flexible-block models ("bloque rigido y bloque flexible") and an identification of which methods apply to each.]

### SLOT 4: Appendix - Newmark Displacement Equations by Method

Prepare a detailed appendix presenting, for each Newmark displacement method: (a) the regression equations for predicted displacement, (b) the types of failure surfaces for which the regression models were calibrated (where such information is available), and (c) the error term or residual standard deviation of each model.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix with "las ecuaciones (desplazamientos de Newmark) de cada metodo," failure-surface types ("tipos de figuras de falla"), and "el termino del error de cada metodo."]

### SLOT 5: Ensemble Numerical Model

Prepare a section presenting the numerical model used in the methodology. The model is a weighted ensemble - a weighted sum - of the individual Newmark displacement models detailed in the appendix (SLOT 4). The section emphasizes that more recent models, which were calibrated with larger ground-motion datasets, receive higher weights in the ensemble.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which requests a section on "el modelo numerico" described as "un ensamble o suma ponderada de diferentes modelos presentados en el apendice" and explicitly requires emphasis on the assignment of higher weights to modern models calibrated with larger datasets.]

## CONSTRAINTS

- Output language: English.
- Document format and register: professional executive memo.
^[Confidence: HIGH, Rationale: Both constraints are explicitly stated in TASK_FILE line 3: "escribir en ingles, en estilo profesional, un memo ejecutivo." No additional global constraints are present in TASK_FILE; slot-specific instructions remain within their respective slot descriptions.]
