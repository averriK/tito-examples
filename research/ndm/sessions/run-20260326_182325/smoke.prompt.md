# Structured Prompt: Performance-Based Horizontal Seismic Coefficient for Slope Stability

## SLOTS

### SLOT 1: Introduction and Problem Statement

Present an introductory section that frames the core engineering problem: selection of a horizontal seismic coefficient for pseudo-static slope stability analysis within a performance-based framework. The seismic coefficient is calibrated along two axes: (a) a target seismic intensity level, which reflects the degree of consequences associated with slope failure, and (b) the mechanical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period. This section should establish why a performance-based approach is adopted and what quantities the methodology estimates.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 7-8, which explicitly request an introduction section describing the problem of selecting a performance-based seismic coefficient calibrated to a target intensity level (related to failure consequences) and to slope characteristics (stiffness, strength, fundamental periods).]

### SLOT 2: Current State of Practice

Survey and summarize the current normative and guideline landscape for performance-based seismic design of slopes using limit-equilibrium models. Identify relevant national and international standards, engineering guidelines, and published recommendations that govern or inform the selection of seismic coefficients for pseudo-static slope analysis. Provide context on how these documents relate to one another and where the profession currently stands regarding performance-based calibration of seismic coefficients.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 9-10, which request a state-of-practice section and explicitly call for research into standards, guidelines, and recommendations for performance-based seismic slope design via limit-equilibrium models.]

### SLOT 3: Newmark Displacement Analysis Methodologies

Summarize the Newmark sliding-block displacement analysis methodologies that underpin the performance-based approach described in this memo. Define and distinguish between rigid-block and flexible-block idealizations of slope response. For each idealization, identify which analytical or empirical displacement prediction methods are applicable and explain the conceptual basis for these distinctions.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 12-13, which request a section summarizing Newmark displacement methodologies, including the definitions of rigid block versus flexible block and which methods apply to each.]

### SLOT 4: Appendix - Newmark Displacement Equations and Calibration Details

Prepare a detailed appendix listing the displacement prediction equations for each Newmark-type method included in the analysis framework. For each method, provide: (a) the full regression equation in proper mathematical notation, (b) the type(s) of failure surface or mechanism for which the regression model was calibrated, where such information is available, and (c) the standard error term or residual uncertainty associated with the model. Present this information in a systematic, method-by-method format.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 14-15, which request an appendix detailing the Newmark displacement equations of each method, the types of failure surfaces for which the regression models were calibrated, and the error term of each method.]

### SLOT 5: Ensemble Numerical Model

Present the numerical model adopted in this methodology. The model is constructed as a weighted ensemble - a weighted sum - of the individual Newmark displacement prediction models detailed in the appendix (SLOT 4). Emphasize that greater weight is assigned to more recent models on the grounds that they were calibrated against larger and more comprehensive ground-motion datasets. Explain the rationale for this weighting strategy and how the ensemble produces a single displacement estimate from multiple underlying models.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE lines 17-18, which request a section presenting the numerical model as an ensemble or weighted sum of the appendix models, with explicit emphasis on assigning more weight to modern models calibrated with larger datasets.]

## CONSTRAINTS

- The output document language is English.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly states "escribir en ingles" (write in English).]

- The document adopts the format and tone of a professional executive memo.
^[Confidence: HIGH, Rationale: TASK_FILE line 3 explicitly requests "estilo profesional, un memo ejecutivo" (professional style, executive memo).]

- Reference material in the `kb/` directory contains an existing summary of the methodology; this material is described as poorly written and poorly organized, and serves as a starting-point source that downstream workflows must substantially restructure and improve.
^[Confidence: HIGH, Rationale: TASK_FILE lines 5-6 explicitly note that the kb/ folder holds a poorly written and disorganized summary document intended as source material.]
