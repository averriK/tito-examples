# Structured Prompt: Horizontal Seismic Coefficient for Slope Stability - Executive Memo

This prompt defines the work items and constraints for producing a professional executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A knowledge-base folder (`kb/`) contains a preliminary summary of the methodology; downstream workflows should treat it as source material requiring substantial revision in both content organization and prose quality.


## SLOTS

### SLOT 1: Introduction to the Problem

Present the problem context for selecting a performance-based seismic coefficient for pseudo-static slope stability analysis. The introduction must establish that the horizontal seismic coefficient is calibrated along two axes: (a) a target intensity level, which is tied to the degree of consequences associated with slope failure, and (b) the mechanical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period. The section should frame why a performance-based approach is necessary and what parameters govern the selection of the coefficient.


### SLOT 2: Current State of Practice

Survey and summarize the existing normative framework - standards, guidelines, and published recommendations - for performance-based seismic design of slopes using limit-equilibrium models. The section should identify which codes and guidance documents are currently in force or widely adopted, describe the general approach each prescribes, and note any significant differences among them.


### SLOT 3: Newmark Displacement Analysis Methods

Summarize the Newmark sliding-block displacement analysis methodologies that underpin the seismic-coefficient estimation framework. The section must define the rigid-block idealization and the flexible-block idealization, explain the physical assumptions behind each, and identify which published displacement-prediction methods correspond to each idealization.


### SLOT 4: Appendix - Newmark Displacement Equations and Calibration Details

Prepare a detailed appendix that documents, for each Newmark displacement prediction method: (a) the full regression equations for predicted displacement, (b) the types of failure surfaces (e.g., shallow planar, deep rotational, translational) for which each regression model was calibrated, where such information is available, and (c) the associated error or uncertainty term (standard deviation of residuals, epistemic variance, or equivalent metric). Present equations in display-math format where appropriate.


### SLOT 5: Ensemble Numerical Model

Present the numerical model adopted in this work. The model is constructed as an ensemble - a weighted combination - of the individual Newmark displacement prediction models documented in the appendix (SLOT 4). The description must emphasize the weighting rationale: more recent models, which were calibrated against larger and more comprehensive ground-motion datasets, receive greater weight in the ensemble.


## CONSTRAINTS

- The output document must be written entirely in English.


- The document must adopt a professional, academic register appropriate for an executive memo.


- The overall document structure is an executive memo; sections should follow the ordering established by the slots above (introduction, state of practice, Newmark methods overview, ensemble model, appendix).

