# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## SLOTS

### SLOT 1: Introduction and Problem Statement

Present an introductory section that frames the core engineering problem: selection of a horizontal seismic coefficient for pseudo-static slope stability analysis within a performance-based framework. The seismic coefficient is calibrated along two axes: (a) a target seismic intensity level, which reflects the degree of consequences associated with slope failure, and (b) the mechanical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period. This section should establish why a performance-based approach is adopted and what quantities the methodology estimates.


### SLOT 2: Current State of Practice

Survey and summarize the current normative and guideline landscape for performance-based seismic design of slopes using limit-equilibrium models. Identify relevant national and international standards, engineering guidelines, and published recommendations that govern or inform the selection of seismic coefficients for pseudo-static slope analysis. Provide context on how these documents relate to one another and where the profession currently stands regarding performance-based calibration of seismic coefficients.


### SLOT 3: Newmark Displacement Analysis Methodologies

Summarize the Newmark sliding-block displacement analysis methodologies that underpin the performance-based approach described in this memo. Define and distinguish between rigid-block and flexible-block idealizations of slope response. For each idealization, identify which analytical or empirical displacement prediction methods are applicable and explain the conceptual basis for these distinctions.


### SLOT 4: Appendix - Newmark Displacement Equations and Calibration Details

Prepare a detailed appendix listing the displacement prediction equations for each Newmark-type method included in the analysis framework. For each method, provide: (a) the full regression equation in proper mathematical notation, (b) the type(s) of failure surface or mechanism for which the regression model was calibrated, where such information is available, and (c) the standard error term or residual uncertainty associated with the model. Present this information in a systematic, method-by-method format.


### SLOT 5: Ensemble Numerical Model

Present the numerical model adopted in this methodology. The model is constructed as a weighted ensemble - a weighted sum - of the individual Newmark displacement prediction models detailed in the appendix (SLOT 4). Emphasize that greater weight is assigned to more recent models on the grounds that they were calibrated against larger and more comprehensive ground-motion datasets. Explain the rationale for this weighting strategy and how the ensemble produces a single displacement estimate from multiple underlying models.


## CONSTRAINTS

- The output document language is English.


- The document adopts the format and tone of a professional executive memo.


- Reference material in the `kb/` directory contains an existing summary of the methodology; this material is described as poorly written and poorly organized, and serves as a starting-point source that downstream workflows must substantially restructure and improve.

