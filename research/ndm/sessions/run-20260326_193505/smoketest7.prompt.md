# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slope Stability

## SLOTS

### SLOT 1: Problem Introduction

The introductory section frames the problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The section covers two key aspects: (a) calibration of the seismic coefficient to a target intensity level, where the target intensity relates to the degree of consequences associated with slope failure, and (b) dependence of the coefficient on slope characteristics, including stiffness, strength, and fundamental period of the slope.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 7-8, which explicitly request an introductory section covering the objective of selecting a performance-based seismic coefficient calibrated for a target intensity level and for slope characteristics including stiffness, strength, and fundamental periods.]

### SLOT 2: Current State of Practice

The state-of-practice section identifies and summarizes the standards, guidelines, and published recommendations that govern performance-based seismic design of slopes using limit-equilibrium models. The scope encompasses research into applicable normative frameworks and current design guidance documents.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which explicitly requests a state-of-practice section and research into the normative standards, guidelines, and recommendations for performance-based seismic slope design via limit-equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methodologies

The methodologies section summarizes the Newmark displacement analysis approaches employed within the overall framework. The section defines and distinguishes between the rigid-block and flexible-block idealizations and identifies which analytical methods apply to each idealization.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which explicitly requests a section summarizing Newmark displacement methodologies, definitions of rigid block and flexible block, and identification of which methods apply to each.]

### SLOT 4: Appendix - Newmark Displacement Equations

The appendix presents, for each Newmark displacement method, the following details: (a) the complete regression equations for estimating seismic displacements, (b) the types of failure surfaces for which the regression models were calibrated, where such information is available, and (c) the error term or standard deviation of the model residuals.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which explicitly requests a detailed appendix with equations for each method, information on calibration failure-surface types where possible, and the error term of each method.]

### SLOT 5: Numerical Model - Weighted Ensemble

The numerical model section describes the model used in the present work, which consists of a weighted ensemble - a weighted sum - of the individual Newmark displacement models detailed in the appendix (SLOT 4). The section emphasizes that greater weight is assigned to more recent models on the basis that they were calibrated using larger and more comprehensive ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which explicitly requests a section presenting the numerical model as a weighted sum of different models from the appendix, with emphasis on assigning more weight to modern models calibrated with larger datasets.]

## CONSTRAINTS

- The output document language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 states "escribir en ingles" (write in English).]

- The document adopts a professional executive-memo style.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 requests "en estilo profesional, un memo ejecutivo" (in professional style, an executive memo).]

- A reference document in the kb/ folder contains a summary of the methodology and serves as background material for downstream workflows. The source is noted as poorly written and poorly organized, requiring substantial restructuring.
^[Confidence: HIGH, Rationale: TASK_FILE lines 5-6 state that the kb/ folder contains a poorly written and poorly organized summary document.]
