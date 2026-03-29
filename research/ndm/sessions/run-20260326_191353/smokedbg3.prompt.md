# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## SLOTS

### SLOT 1: Introduction to the Problem

Present an introductory section that frames the problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated to a target seismic intensity level, which is related to the degree of consequences of failure, and to the physical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 7-8, which specify the introduction scope, performance-based calibration objectives, target intensity level tied to failure consequences, and slope characteristics (stiffness, strength, fundamental periods).]

### SLOT 2: Current State of Practice

Investigate and present the current state of practice for performance-based seismic slope design using limit equilibrium models. This section covers applicable design standards, professional guidelines, and published recommendations that govern the selection of horizontal seismic coefficients for slope analysis.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 9, which requests research into "normativas, guidelines y recomendaciones para el diseno sismico de taludes basado en performance mediante modelos de equilibrio limite."]

### SLOT 3: Newmark Displacement Analysis Methodologies

Summarize the Newmark displacement analysis methodologies employed in this approach. Define and distinguish rigid-block and flexible-block sliding models, and identify which displacement estimation methods apply to each block type.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 12, which requests a section on Newmark displacement methodologies with explicit definitions of rigid and flexible blocks and their associated methods.]

### SLOT 4: Appendix of Newmark Displacement Equations by Method

Prepare a detailed appendix presenting the Newmark displacement equations for each method. For each regression model, document the types of failure surfaces for which the model was calibrated (where this information is available) and the associated error term.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 14, which requests an appendix detailing equations, failure surface calibration types, and error terms for each Newmark displacement method.]

### SLOT 5: Ensemble Numerical Model

Present the numerical model used in this methodology. The model is formulated as an ensemble, that is, a weighted sum of the individual Newmark displacement models documented in the appendix. The presentation must emphasize that greater weight is assigned to more recent models, which were calibrated with larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 17, which describes the ensemble as a "suma ponderada de diferentes modelos" and requires emphasis on the weighting rationale favoring modern, larger-dataset models.]

## CONSTRAINTS

- The output language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly requires "escribir en ingles."]

- The document follows a professional style suitable for an executive memo.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 specifies "estilo profesional" and "memo ejecutivo."]

- The overarching subject is the current-practice methodology for estimating the horizontal seismic coefficient of a slope.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 defines the topic as "metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud."]

- A reference document in the kb/ folder summarizes the methodology and serves as a primary source; however, its structure and prose quality require substantial improvement in the final output.
^[Confidence: HIGH, Rationale: TASK_FILE lines 5-6 note the kb/ document is "muy mal escrita y muy mal ordenada," establishing it as a source that must be reorganized and rewritten.]
