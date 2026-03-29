# Structured Prompt: Horizontal Seismic Coefficient for Slope Stability - Executive Memo

This prompt defines the work items and constraints for producing a professional executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A knowledge-base folder (`kb/`) contains a preliminary summary of the methodology; downstream workflows should treat it as source material requiring substantial revision in both content organization and prose quality.
^[Confidence: HIGH, Rationale: TASK_FILE lines 3-5 explicitly request an English-language professional executive memo on the seismic-coefficient methodology and note the existence of a poorly written KB document.]

## SLOTS

### SLOT 1: Introduction to the Problem

Present the problem context for selecting a performance-based seismic coefficient for pseudo-static slope stability analysis. The introduction must establish that the horizontal seismic coefficient is calibrated along two axes: (a) a target intensity level, which is tied to the degree of consequences associated with slope failure, and (b) the mechanical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period. The section should frame why a performance-based approach is necessary and what parameters govern the selection of the coefficient.
^[Confidence: HIGH, Rationale: TASK_FILE line 7 explicitly requests an introductory section and specifies the calibration axes (target intensity level related to failure consequences; slope characteristics including stiffness, strength, and fundamental periods).]

### SLOT 2: Current State of Practice

Survey and summarize the existing normative framework - standards, guidelines, and published recommendations - for performance-based seismic design of slopes using limit-equilibrium models. The section should identify which codes and guidance documents are currently in force or widely adopted, describe the general approach each prescribes, and note any significant differences among them.
^[Confidence: HIGH, Rationale: TASK_FILE line 9 explicitly requests a state-of-practice section and instructs to research standards, guidelines, and recommendations for performance-based seismic slope design via limit-equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methods

Summarize the Newmark sliding-block displacement analysis methodologies that underpin the seismic-coefficient estimation framework. The section must define the rigid-block idealization and the flexible-block idealization, explain the physical assumptions behind each, and identify which published displacement-prediction methods correspond to each idealization.
^[Confidence: HIGH, Rationale: TASK_FILE line 12 explicitly requests a section summarizing Newmark displacement methodologies, with definitions of rigid-block and flexible-block models and a mapping of methods to each type.]

### SLOT 4: Appendix - Newmark Displacement Equations and Calibration Details

Prepare a detailed appendix that documents, for each Newmark displacement prediction method: (a) the full regression equations for predicted displacement, (b) the types of failure surfaces (e.g., shallow planar, deep rotational, translational) for which each regression model was calibrated, where such information is available, and (c) the associated error or uncertainty term (standard deviation of residuals, epistemic variance, or equivalent metric). Present equations in display-math format where appropriate.
^[Confidence: HIGH, Rationale: TASK_FILE line 14 explicitly requests an appendix detailing equations, calibration failure-surface types, and error terms for each Newmark displacement method.]

### SLOT 5: Ensemble Numerical Model

Present the numerical model adopted in this work. The model is constructed as an ensemble - a weighted combination - of the individual Newmark displacement prediction models documented in the appendix (SLOT 4). The description must emphasize the weighting rationale: more recent models, which were calibrated against larger and more comprehensive ground-motion datasets, receive greater weight in the ensemble.
^[Confidence: HIGH, Rationale: TASK_FILE line 17 explicitly requests a section on the ensemble numerical model (weighted sum of appendix models) and emphasizes assigning greater weight to newer models calibrated with larger datasets.]

## CONSTRAINTS

- The output document must be written entirely in English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 states "escribir en ingles" (write in English), an explicit document-wide language requirement.]

- The document must adopt a professional, academic register appropriate for an executive memo.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 specifies "estilo profesional" (professional style) and "memo ejecutivo" (executive memo) as the target format and tone.]

- The overall document structure is an executive memo; sections should follow the ordering established by the slots above (introduction, state of practice, Newmark methods overview, ensemble model, appendix).
^[Confidence: HIGH, Rationale: TASK_FILE lines 7-17 present the requested sections in this order; the appendix is placed last consistent with standard memo conventions and the logical dependency noted in SLOT 5's reference to the appendix.]
