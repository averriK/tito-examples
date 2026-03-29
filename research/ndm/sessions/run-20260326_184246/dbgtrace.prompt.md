# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## SLOTS

### SLOT 1: Problem Introduction and Objective

Prepare an introductory section that frames the engineering problem addressed by the memo. The central objective is the selection of a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The coefficient is calibrated to two categories of input: (a) a target seismic intensity level, which reflects the degree of consequences associated with slope failure, and (b) physical characteristics of the slope itself, including stiffness, shear strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 7-8, which state the objective of selecting a performance-based seismic coefficient calibrated to a target intensity level related to failure consequences and to slope characteristics including stiffness, strength, and fundamental periods.]

### SLOT 2: Current State of Practice

Prepare a section surveying the current state of practice for performance-based seismic design of slopes. Research and present the normative frameworks, published design guidelines, and professional recommendations that govern seismic slope design through limit-equilibrium models. Identify key standards, code provisions, and guideline documents issued by major geotechnical and earthquake engineering organizations.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests investigation of normatives, guidelines, and recommendations for performance-based seismic design of slopes using limit-equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methodologies

Prepare a section summarizing the Newmark sliding-block displacement analysis methodologies employed in the approach described by this memo. Define the rigid-block and flexible-block idealizations, explain the physical assumptions underlying each, and identify which displacement prediction methods apply to rigid blocks, which apply to flexible blocks, and which accommodate both categories.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which asks for a section summarizing Newmark displacement methodologies, the definition of rigid block and flexible block, and which methods apply to each.]

### SLOT 4: Appendix Detailing Newmark Displacement Equations

Prepare a detailed appendix presenting the displacement prediction equations for each Newmark-type method considered. For every model, include: (a) the regression equation together with its independent variables, (b) the type of failure surface geometry (e.g., planar, circular, or general) for which the regression was calibrated, where that information is available, and (c) the error term or residual standard deviation that characterizes model uncertainty.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix with equations for each method, the failure figure types for which models were calibrated, and the error term of each method.]

### SLOT 5: Ensemble Numerical Model

Prepare a section describing the numerical model adopted in this work. The model is formulated as an ensemble - a weighted sum - of the individual Newmark displacement prediction models detailed in the appendix (SLOT 4). The weighting scheme assigns greater weight to more recent models on the basis that they were calibrated against larger and more comprehensive ground-motion datasets, and this rationale must be stated explicitly.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 17-18, which describe the numerical model as an ensemble or weighted sum of different appendix models, with emphasis on assigning more weight to modern models calibrated with larger datasets.]

## CONSTRAINTS

- The output language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly requires the document to be written in English ("escribir en ingles").]

- The document adopts the format and tone of a professional executive memo.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 specifies "estilo profesional, un memo ejecutivo" (professional style, executive memo).]

- A knowledge-base document located in the kb/ directory contains a preliminary summary of the methodology and serves as a reference source for downstream workflows. The final output must be independently well-organized and clearly written rather than a surface-level revision of that source material.
^[Confidence: HIGH, Rationale: TASK_FILE lines 5-6 note the existence of a KB document summarizing the methodology, described as poorly written and poorly organized, implying the output must substantially improve upon it.]
