# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Objective

This section introduces the problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated to (a) a target seismic intensity level, related to the degree of consequences of slope failure, and (b) the physical characteristics of the slope itself, including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 7, which explicitly requests an introductory section and specifies the calibration targets - intensity level tied to failure consequences and slope characteristics including stiffness, strength, and fundamental periods. No content introduced beyond what TASK_FILE states.]

### SLOT 2: Current State of Practice

This section surveys the current state of practice for performance-based seismic design of slopes. The scope includes applicable standards, guidelines, and recommendations from regulatory and professional bodies, with a focus on approaches that employ limit equilibrium models for seismic slope stability assessment.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 9, which requests a state-of-practice section and specifically calls for research into normative standards, guidelines, and recommendations for performance-based seismic slope design using limit equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed within the overall framework. The definitions of rigid-block and flexible-block models are presented, and the displacement estimation methods applicable to each category are identified.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 12, which requests a section summarizing Newmark displacement methodologies, an explanation of the rigid-block and flexible-block definitions, and identification of which methods apply to each type.]

### SLOT 4: Appendix - Newmark Displacement Equations by Method

This appendix details the Newmark displacement estimation equations for each method included in the framework. Where available, the types of failure surfaces for which each regression model was calibrated are specified. The error term associated with each method is also reported.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 14, which requests an appendix with equations for Newmark displacements, details on the failure-surface types used for calibration (qualified with "if possible"), and the error terms of each method.]

### SLOT 5: Ensemble Numerical Model Description

This section presents the numerical model employed in the methodology. The model consists of an ensemble - a weighted sum of the individual displacement models detailed in the appendix. The weighting scheme assigns greater weight to more recent models that were calibrated using larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly paraphrases TASK_FILE line 17, which requests a section on the numerical model described as an ensemble or weighted sum of different models, with emphasis on the greater weight assigned to more modern models calibrated with larger datasets.]

## CONSTRAINTS

- The output language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly states "escribir en ingles" (write in English).]

- The document adopts a professional, executive memo style.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly requests "estilo profesional, un memo ejecutivo" (professional style, executive memo).]

- The overarching subject is the state-of-practice methodology for estimating the horizontal seismic coefficient for slope stability assessment.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 frames the entire document as presenting "la metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud".]

- A reference document in the kb/ directory contains a summary of the methodology and serves as a starting point, though it requires significant revision for organization and clarity.
^[Confidence: HIGH, Rationale: TASK_FILE line 5 states that the kb/ folder holds a document summarizing the methodology, described as poorly written and poorly organized.]
