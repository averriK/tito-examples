# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## Context

This prompt structures the requirements for an executive memo presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A reference document summarizing the methodology exists in the `kb/` directory; it is noted as poorly written and poorly organized, and may serve as a starting point for downstream research and synthesis workflows.


## SLOTS

### SLOT 1: Problem Introduction

Prepare an introductory section framing the central problem: selection of a performance-based horizontal seismic coefficient ($k_h$) for pseudo-static slope stability analysis. The coefficient is calibrated to (a) a target seismic intensity level, which relates to the degree of consequences associated with slope failure, and (b) the physical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.


### SLOT 2: State of Current Practice

Prepare a state-of-practice section surveying the standards, guidelines, and professional recommendations that govern performance-based seismic design of slopes through limit-equilibrium models. The survey identifies relevant normative frameworks and practice documents currently in use.


### SLOT 3: Newmark Displacement Analysis Methods

Prepare a section summarizing the Newmark displacement analysis methodologies employed in the overall approach. The section defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each category.


### SLOT 4: Appendix - Newmark Displacement Equations by Method

Prepare a detailed appendix presenting, for each Newmark displacement method: (a) the regression equations for predicted displacement, (b) the types of failure surfaces for which the regression models were calibrated (where such information is available), and (c) the error term or residual standard deviation of each model.


### SLOT 5: Ensemble Numerical Model

Prepare a section presenting the numerical model used in the methodology. The model is a weighted ensemble - a weighted sum - of the individual Newmark displacement models detailed in the appendix (SLOT 4). The section emphasizes that more recent models, which were calibrated with larger ground-motion datasets, receive higher weights in the ensemble.


## CONSTRAINTS

- Output language: English.
- Document format and register: professional executive memo.

