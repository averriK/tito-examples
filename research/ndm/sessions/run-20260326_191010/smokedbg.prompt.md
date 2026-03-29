# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## Context

This prompt structures the requirements for an executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of slopes. A reference document in the `kb/` directory contains a preliminary summary of the methodology; that material requires substantial reorganization and rewriting before incorporation into the final deliverable. ^[Confidence: HIGH, Rationale: The overall scope derives directly from TASK_FILE line 3 ("un memo ejecutivo que presente la metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud"), and the kb/ reference note from lines 5-6 ("un documento que presenta un resumen de la metodologia, pero muy mal escrita y muy mal ordenada"). Both statements are explicit in the source.]

## SLOTS

### SLOT 1: Problem Introduction - Performance-Based Seismic Coefficient Selection

This section frames the central problem. The objective is the selection of a performance-based seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated for two factors: (a) a target seismic intensity level, which corresponds to the degree of consequences associated with slope failure, and (b) the physical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period. ^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 7, which requests "una seccion que introduzca el problema" and specifies both calibration factors - target intensity level related to failure consequences, and slope characteristics including "rigidez, resistencia, periodos fundamentales." All elements are present in the slot description without additions.]

### SLOT 2: Current State of Practice - Standards, Guidelines, and Recommendations

This section surveys the current state of practice for performance-based seismic design of slopes using limit equilibrium models. The scope encompasses identification and discussion of relevant codes and standards, engineering guidelines, and published recommendations that govern or inform this design approach. ^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests "una seccion de estado actual de la practica" and specifies investigation of "normativas, guidelines y recomendaciones para el diseno sismico de taludes basado en performance mediante modelos de equilibrio limite." The slot preserves all three categories (standards, guidelines, recommendations) and the limit-equilibrium scope qualifier.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed within the seismic coefficient estimation framework. It defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each block type. ^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a section summarizing "las metodologias de analisis de desplazamientos de Newmark," the definition of "bloque rigido y bloque flexible," and identification of "cuales metodos aplican a cada uno." All three elements are reflected in the slot description.]

### SLOT 4: Appendix - Newmark Displacement Equations and Model Calibration Details

This appendix provides detailed technical content for each Newmark displacement method referenced in SLOT 3. For each method, it includes: (a) the complete governing regression equations, (b) the types of failure surfaces for which the regression models were calibrated, where such information is available, and (c) the associated error term or residual standard deviation. ^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix "detallando las ecuaciones (desplazamientos de Newmark) de cada metodo," the failure surface types ("figuras de falla") used for calibration ("si es posible" - reflected here by the availability qualifier), and "el termino del error de cada metodo." All three sub-requirements are present.]

### SLOT 5: Ensemble Numerical Model

This section presents the specific numerical model used in this methodology. The model is an ensemble constructed as a weighted sum of the individual Newmark displacement models detailed in the appendix (SLOT 4). The weighting scheme assigns greater weight to more recent models that were calibrated using larger ground-motion datasets, reflecting the assumption that newer models benefit from improved data coverage and quality. ^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which describes the model as "un ensamble o suma ponderada de diferentes modelos presentados en el apendice" and requests emphasis on the fact that "se le asigna mas peso a los modelos mas modernos, que fueron calibrados con datasets mas grandes." All elements are covered. The final clause ("improved data coverage and quality") is a minimal clarification of the stated rationale for the weighting, not an invented requirement.]

## CONSTRAINTS

- Output language: English.
- Document style: professional, academic tone appropriate for an executive memo.
- Document format: executive memo presenting a methodology overview for horizontal seismic coefficient estimation.
- The `kb/` directory contains a reference document with a preliminary methodology summary; downstream workflows should consult it as source material but must substantially reorganize and improve that content.

^[Confidence: HIGH, Rationale: The language and style constraints derive from TASK_FILE line 3 ("escribir en ingles, en estilo profesional, un memo ejecutivo"). The document-format constraint paraphrases the same line. The kb/ guidance derives from TASK_FILE lines 5-6, which describe the reference as poorly written and poorly organized. No constraints were invented beyond what TASK_FILE states.]
