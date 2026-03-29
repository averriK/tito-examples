# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slope Stability

The overarching deliverable is a professional executive memo presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A reference summary of the methodology exists in the kb/ folder; this source is characterized as poorly written and poorly organized and should be consulted for technical content but not emulated in structure or style.
^[Confidence: HIGH, Rationale: The deliverable description paraphrases TASK_FILE line 3, which specifies a professional executive memo on seismic coefficient estimation methodology. The KB folder characterization paraphrases TASK_FILE line 5, which notes the document is poorly written and poorly organized.]

## SLOTS

### SLOT 1: Problem Introduction

Prepare an introductory section framing the problem. The central objective is the selection of a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The coefficient is calibrated for two categories of input: (a) a target seismic intensity level, linked to the degree of consequences associated with slope failure, and (b) the mechanical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 7, which requests an introduction section and specifies the performance-based objective, target intensity calibration related to failure consequences, and slope characteristics including stiffness, strength, and fundamental periods.]

### SLOT 2: State of Current Practice

Prepare a section reviewing the current state of practice for performance-based seismic slope design. This slot requires investigation of existing codes, standards, guidelines, and professional recommendations that govern the seismic design of slopes using limit-equilibrium models. The review identifies the principal normative frameworks and their respective approaches.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests a state-of-practice section and explicitly calls for research into codes ("normativas"), guidelines, and recommendations for performance-based seismic slope design via limit-equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methodologies

Prepare a section summarizing the Newmark sliding-block displacement analysis methodologies used in this approach. The section defines the rigid-block and flexible-block idealizations and identifies which displacement estimation methods are applicable to each block type.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a summary of Newmark displacement methodologies, definitions of rigid and flexible blocks, and identification of applicable methods for each type.]

### SLOT 4: Appendix - Newmark Displacement Equations by Method

Prepare an appendix presenting the Newmark displacement regression equations for each method in full mathematical detail. For each regression model, specify (where available) the types of failure surfaces for which the model was calibrated. Report the error term or residual standard deviation associated with each method.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix with Newmark displacement equations per method, failure surface calibration types, and error terms for each method.]

### SLOT 5: Ensemble Numerical Model

Prepare a section presenting the numerical model adopted in this work. The model is a weighted ensemble - a weighted sum of the individual Newmark displacement regression models detailed in the appendix (SLOT 4). The section emphasizes that greater weight is assigned to more recent models, which were calibrated using larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which requests a section on the ensemble model described as a weighted sum of appendix models, with emphasis on weighting newer models calibrated with larger datasets.]

## CONSTRAINTS

- Output language: English.
- Prose style: professional executive memo with academic register.
^[Confidence: HIGH, Rationale: Both constraints are explicitly stated in TASK_FILE line 3, which specifies "escribir en ingles, en estilo profesional, un memo ejecutivo."]
