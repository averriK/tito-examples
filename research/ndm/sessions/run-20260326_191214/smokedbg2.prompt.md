# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

This section introduces the problem of selecting a performance-based horizontal seismic coefficient ($k_h$) for pseudo-static slope stability analysis. The seismic coefficient is calibrated to a target intensity level, which relates to the degree of consequences associated with slope failure, and to the physical characteristics of the slope, including stiffness, strength, and fundamental period. The scope encompasses the rationale for adopting a performance-based framework rather than a single deterministic seismic coefficient.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 7, which requests an introduction section and specifies the objective of selecting a performance-based seismic coefficient calibrated for a target intensity level (related to failure consequences) and slope characteristics (stiffness, strength, fundamental periods). All elements of this slot trace to explicit task language.]

### SLOT 2: State of Current Practice for Performance-Based Seismic Slope Design

This section surveys the current state of practice for seismic slope design, including applicable standards, guidelines, and published recommendations that govern performance-based design of slopes through limit-equilibrium models. The survey covers normative frameworks and consensus documents from relevant professional and regulatory bodies.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests a state-of-practice section and explicitly asks for research into standards, guidelines, and recommendations for performance-based seismic slope design using limit-equilibrium models. All elements trace to explicit task language.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark sliding-block displacement analysis methodologies employed in the overall approach. It defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each category.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a section summarizing the Newmark displacement analysis methodologies, including definitions of rigid block and flexible block and which methods apply to each. All elements trace to explicit task language.]

### SLOT 4: Appendix Detailing Newmark Displacement Equations by Method

This appendix presents, for each Newmark displacement prediction method, the governing regression equations with full notation. Where available, it specifies the types of failure surfaces (e.g., shallow translational, deep rotational) for which each regression model was calibrated. It also reports the associated error term (standard deviation or similar uncertainty measure) for each model.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix detailing the Newmark displacement equations for each method, the failure surface types for which regression models were calibrated ("si es posible"), and the error term for each method. The qualifier "where available" faithfully preserves the task's "si es posible" hedge.]

### SLOT 5: Ensemble Numerical Model

This section presents the numerical model used in this work. The model is an ensemble, or weighted sum, of the individual Newmark displacement prediction models detailed in the appendix (SLOT 4). More recent models, which were calibrated with larger ground-motion datasets, receive greater weight in the ensemble.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which requests a section presenting the numerical model as a weighted sum of different models from the appendix, with emphasis on assigning more weight to modern models calibrated with larger datasets. All elements trace to explicit task language.]

## CONSTRAINTS

- The output language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly states "escribir en ingles."]

- The document adopts a professional executive-memo style.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly requests "estilo profesional, un memo ejecutivo."]

- A reference document in the kb/ directory contains a summary of the methodology; it serves as an input source but is noted as poorly written and poorly organized, requiring substantial restructuring and rewriting.
^[Confidence: HIGH, Rationale: TASK_FILE line 5 explicitly states "En la carpeta kb/ existe un documento que presenta un resumen de la metodologia, pero muy mal escrita y muy mal ordenada."]
