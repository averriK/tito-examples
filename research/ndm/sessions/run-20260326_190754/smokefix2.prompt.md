# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## SLOTS

### SLOT 1: Problem Introduction and Objective

This section introduces the problem context. The objective is the selection of a performance-based seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated to (a) a target intensity level, which relates to the degree of consequences associated with slope failure, and (b) the characteristics of the slope itself, including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE lines 7-8, which explicitly request an introduction section and specify calibration parameters: target intensity level tied to failure consequences, and slope characteristics including stiffness, strength, and fundamental periods. No content invented beyond what TASK_FILE states.]

### SLOT 2: Current State of Practice

This section covers the current state of practice. It requires research into the existing codes, standards, guidelines, and technical recommendations governing performance-based seismic design of slopes through limit equilibrium models. The scope includes both normative frameworks and published professional guidance.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 9, which requests a state-of-practice section and specifies the scope as normativas, guidelines, and recommendations for performance-based seismic slope design using limit equilibrium models. The phrase "published professional guidance" is a reasonable gloss of "recomendaciones" in context.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed in the overall framework. It must define the rigid-block and flexible-block idealizations and identify which displacement prediction methods apply to each type.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 12, which requests a summary section on Newmark displacement methodologies and explicitly requires definitions of rigid block ("bloque rigido") and flexible block ("bloque flexible") along with the methods applicable to each.]

### SLOT 4: Appendix - Newmark Displacement Equations by Method

This appendix presents, for each Newmark displacement method, the following details: (a) the regression equations and their parameters, (b) the types of failure surfaces for which each regression model was calibrated, where such information is available, and (c) the error term or residual standard deviation associated with each model.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 14, which requests an appendix detailing equations for each method, the failure-surface types ("figuras de falla") used in calibration, and the error term ("termino del error") of each method. All three sub-items are explicitly stated in TASK_FILE.]

### SLOT 5: Ensemble Numerical Model

This section presents the numerical model adopted in this work. The model is an ensemble - a weighted sum of different Newmark displacement prediction models detailed in the appendix (SLOT 4). The section must highlight that greater weight is assigned to more recent models, which were calibrated against larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 17, which requests a section on the numerical model, defines it as an ensemble or weighted sum ("ensamble o suma ponderada"), and specifies the emphasis on modern models ("modelos mas modernos") calibrated with larger datasets ("datasets mas grandes").]

## CONSTRAINTS

- Output language: English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly states "escribir en ingles."]

- Document format: professional executive memo.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly states "estilo profesional, un memo ejecutivo."]

- Topic scope: methodology for estimating the horizontal seismic coefficient for slopes, following current state-of-practice approaches.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 defines the scope as "la metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud."]

- A reference document exists in the $\texttt{kb/}$ folder containing a methodology summary; it may serve as background material but is noted as poorly written and poorly organized.
^[Confidence: HIGH, Rationale: TASK_FILE line 5 states "En la carpeta kb/ existe un documento que presenta un resumen de la metodologia, pero muy mal escrita y muy mal ordenada." This constraint preserves the provenance note so downstream workflows can use the KB document with appropriate caution.]
