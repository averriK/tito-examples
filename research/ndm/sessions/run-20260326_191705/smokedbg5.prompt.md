# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slope Stability

## CONTEXT

The downstream deliverable is an executive memo, written in English with a professional technical register, presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope. A draft of the methodology exists in the kb/ directory; it is described as poorly written and poorly organized, requiring substantial restructuring and rewriting before it can serve as usable source material.
^[Confidence: HIGH, Rationale: The deliverable type, language, and register are stated explicitly in TASK_FILE line 3 ("escribir en ingles, en estilo profesional, un memo ejecutivo que presente la metodologia del estado actual de la practica para la estimacion del coeficiente sismico horizontal de un talud"). The kb/ characterization derives from TASK_FILE lines 5-6.]

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

This section introduces the problem of selecting a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The coefficient is calibrated to (a) a target seismic intensity level, which relates to the degree of consequences associated with slope failure, and (b) the characteristics of the slope itself, including stiffness, strength, and fundamental periods.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 7-8, which request an introductory section defining the problem, the performance-based objective, the calibration targets (intensity level related to failure consequences), and the slope characteristics (stiffness, strength, fundamental periods). Full coverage of the stated requirement.]

### SLOT 2: Current State of Practice for Performance-Based Seismic Slope Design

This section surveys the current state of practice for performance-based seismic design of slopes. It identifies and summarizes applicable regulations, guidelines, and published recommendations that govern seismic slope design through limit equilibrium models.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 9-10, which request a state-of-practice section and specify research into regulations, guidelines, and recommendations for performance-based seismic slope design using limit equilibrium models. Full coverage.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies used within the estimation framework. It defines the rigid-block and flexible-block idealizations and identifies which analytical methods apply to each type.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 12-13, which request a summary of Newmark displacement methodologies, including definitions of the rigid-block and flexible-block concepts and an account of which methods apply to each. Full coverage.]

### SLOT 4: Appendix - Newmark Displacement Equations and Regression Model Details

This appendix presents the detailed Newmark displacement equations for each method. For each regression model, it documents (a) the complete equation set, (b) the types of failure surfaces for which the regression was calibrated, where such information is available, and (c) the error term or residual standard deviation.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 14-15, which request an appendix detailing equations, failure-surface calibration types ("para que tipos de figuras de falla fueron calibrados"), and error terms ("el termino del error de cada metodo"). The qualifier "si es posible" for failure-surface types is preserved as "where such information is available." Full coverage.]

### SLOT 5: Ensemble Numerical Model Description

This section presents the numerical model employed in this methodology. The model consists of an ensemble, defined as a weighted sum, of the individual Newmark displacement models detailed in the appendix (SLOT 4). Greater weight is assigned to more recent models that were calibrated using larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 17-18, which describe the numerical model as an ensemble or weighted sum of appendix models and emphasize the preferential weighting of modern models calibrated with larger datasets. Full coverage.]

## CONSTRAINTS

- Output language: English.
- Document register: professional executive memo with academic and technical tone.
- Source material in the kb/ directory provides a methodology summary that requires substantial reorganization and rewriting; downstream workflows should use it as primary input.
^[Confidence: HIGH, Rationale: The language and register constraints derive explicitly from TASK_FILE line 3, which specifies English, professional style, and executive memo format. The kb/ source-material note and its quality characterization derive from TASK_FILE lines 5-6. No constraints were added beyond what TASK_FILE states.]
