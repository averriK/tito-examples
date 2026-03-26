# Structured Prompt: Performance-Based Horizontal Seismic Coefficient Estimation for Slope Stability

<!-- Audit policy for this workflow:
  Target scope: Structured prompt slots and constraints (coverage verification against TASK_FILE).
  Evidence rule: TASK_FILE is the sole evidence source; no external material constitutes evidence.
  Fetch policy: No external fetching during audit.
  Token requirements: None (no citation tokens expected in a structured prompt).
  Audit semantics: Confidence and Rationale reflect whether each slot is faithfully traceable to
  explicit content in TASK_FILE, with no invented objectives or dropped requirements.
-->

The target deliverable is a professional executive memo in English presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. Reference material in the kb/ directory serves as background input; the source material is acknowledged as poorly written and poorly organized and requires substantial restructuring during downstream processing.

## SLOTS

### SLOT 1: Problem Introduction

An introductory section frames the engineering problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The section addresses two calibration dimensions: (a) a target seismic intensity level, which relates to the degree of consequences upon slope failure, and (b) the physical and dynamic characteristics of the slope itself, including stiffness, strength, and fundamental period.

### SLOT 2: Current State of Practice

A survey section identifies the current state of practice for performance-based seismic design of slopes using limit-equilibrium models. The section covers relevant standards, technical guidelines, and published recommendations from recognized normative bodies and the technical literature.

### SLOT 3: Newmark Displacement Analysis Methods

A summary section describes the Newmark sliding-block displacement analysis methodologies employed within the overall framework. The section defines rigid-block and flexible-block idealizations and specifies which analytical methods correspond to each block type.

### SLOT 4: Appendix - Newmark Displacement Equations

A detailed appendix presents the regression equations for Newmark displacement estimation from each individual method. For each model, the appendix includes: (a) the complete set of predictive equations, (b) the types of failure surfaces for which the regression models were calibrated, where this information is documented, and (c) the associated error term or residual standard deviation characterizing model uncertainty.

### SLOT 5: Ensemble Numerical Model

A section presents the numerical model adopted in this work, which consists of a weighted ensemble - a weighted sum - of the individual Newmark displacement models documented in the appendix (SLOT 4). The section emphasizes the weighting strategy: more recent models receive greater weight because they were calibrated against larger and more comprehensive ground-motion datasets.

## CONSTRAINTS

- The entire output document is written in English.
- The document adopts a professional executive-memo register throughout all sections and the appendix.
- Reference material in the kb/ directory serves as background input for downstream processing; the source is noted as poorly written and organized and requires substantial revision and restructuring before incorporation.
