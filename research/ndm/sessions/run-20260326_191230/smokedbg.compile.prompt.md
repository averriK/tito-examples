# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## Context

This prompt structures the requirements for an executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of slopes. A reference document in the `kb/` directory contains a preliminary summary of the methodology; that material requires substantial reorganization and rewriting before incorporation into the final deliverable.

## SLOTS

### SLOT 1: Problem Introduction - Performance-Based Seismic Coefficient Selection

This section frames the central problem. The objective is the selection of a performance-based seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated for two factors: (a) a target seismic intensity level, which corresponds to the degree of consequences associated with slope failure, and (b) the physical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.

### SLOT 2: Current State of Practice - Standards, Guidelines, and Recommendations

This section surveys the current state of practice for performance-based seismic design of slopes using limit equilibrium models. The scope encompasses identification and discussion of relevant codes and standards, engineering guidelines, and published recommendations that govern or inform this design approach.

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed within the seismic coefficient estimation framework. It defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each block type.

### SLOT 4: Appendix - Newmark Displacement Equations and Model Calibration Details

This appendix provides detailed technical content for each Newmark displacement method referenced in SLOT 3. For each method, it includes: (a) the complete governing regression equations, (b) the types of failure surfaces for which the regression models were calibrated, where such information is available, and (c) the associated error term or residual standard deviation.

### SLOT 5: Ensemble Numerical Model

This section presents the specific numerical model used in this methodology. The model is an ensemble constructed as a weighted sum of the individual Newmark displacement models detailed in the appendix (SLOT 4). The weighting scheme assigns greater weight to more recent models that were calibrated using larger ground-motion datasets, reflecting the assumption that newer models benefit from improved data coverage and quality.

## CONSTRAINTS

- Output language: English.
- Document style: professional, academic tone appropriate for an executive memo.
- Document format: executive memo presenting a methodology overview for horizontal seismic coefficient estimation.
- The `kb/` directory contains a reference document with a preliminary methodology summary; downstream workflows should consult it as source material but must substantially reorganize and improve that content.


