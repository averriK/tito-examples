# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slope Stability

## CONTEXT

The downstream deliverable is an executive memo, written in English with a professional technical register, presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A draft of the methodology exists in the kb/ directory; it is described as poorly written and poorly organized, requiring substantial restructuring and rewriting before it can serve as usable source material.


## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

This section introduces the problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The coefficient is calibrated to (a) a target seismic intensity level, which relates to the degree of consequences associated with slope failure, and (b) the characteristics of the slope itself, including stiffness, strength, and fundamental periods.


### SLOT 2: Current State of Practice for Performance-Based Seismic Slope Design

This section surveys the current state of practice for performance-based seismic design of slopes. It identifies and summarizes applicable regulations, guidelines, and published recommendations that govern seismic slope design through limit equilibrium models.


### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies used within the estimation framework. It defines the rigid-block and flexible-block idealizations and identifies which analytical methods apply to each type.


### SLOT 4: Appendix - Newmark Displacement Equations and Regression Model Details

This appendix presents the detailed Newmark displacement equations for each method. For each regression model, it documents (a) the complete equation set, (b) the types of failure surfaces for which the regression was calibrated, where such information is available, and (c) the error term or residual standard deviation.


### SLOT 5: Ensemble Numerical Model Description

This section presents the numerical model employed in this methodology. The model consists of an ensemble, defined as a weighted sum, of the individual Newmark displacement models detailed in the appendix (SLOT 4). Greater weight is assigned to more recent models that were calibrated using larger ground-motion datasets.


## CONSTRAINTS

- Output language: English.
- Document register: professional executive memo with academic and technical tone.
- Source material in the kb/ directory provides a methodology summary that requires substantial reorganization and rewriting; downstream workflows should use it as primary input.

