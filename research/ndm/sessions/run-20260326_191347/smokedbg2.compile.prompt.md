# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

This section introduces the problem of selecting a performance-based horizontal seismic coefficient ($k_h$) for pseudo-static slope stability analysis. The seismic coefficient is calibrated to a target intensity level, which relates to the degree of consequences associated with slope failure, and to the physical characteristics of the slope, including stiffness, strength, and fundamental period. The scope encompasses the rationale for adopting a performance-based framework rather than a single deterministic seismic coefficient.


### SLOT 2: State of Current Practice for Performance-Based Seismic Slope Design

This section surveys the current state of practice for seismic slope design, including applicable standards, guidelines, and published recommendations that govern performance-based design of slopes through limit-equilibrium models. The survey covers normative frameworks and consensus documents from relevant professional and regulatory bodies.


### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark sliding-block displacement analysis methodologies employed in the overall approach. It defines the rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each category.


### SLOT 4: Appendix Detailing Newmark Displacement Equations by Method

This appendix presents, for each Newmark displacement prediction method, the governing regression equations with full notation. Where available, it specifies the types of failure surfaces (e.g., shallow translational, deep rotational) for which each regression model was calibrated. It also reports the associated error term (standard deviation or similar uncertainty measure) for each model.


### SLOT 5: Ensemble Numerical Model

This section presents the numerical model used in this work. The model is an ensemble, or weighted sum, of the individual Newmark displacement prediction models detailed in the appendix (SLOT 4). More recent models, which were calibrated with larger ground-motion datasets, receive greater weight in the ensemble.


## CONSTRAINTS

- The output language is English.


- The document adopts a professional executive-memo style.


- A reference document in the kb/ directory contains a summary of the methodology; it serves as an input source but is noted as poorly written and poorly organized, requiring substantial restructuring and rewriting.

