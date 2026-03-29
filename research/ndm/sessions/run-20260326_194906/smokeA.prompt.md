# Structured Prompt: Horizontal Seismic Coefficient Estimation - Executive Memo

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Seismic Coefficient

This section introduces the problem addressed by the memo. The core objective is the selection of a performance-based horizontal seismic coefficient for pseudo-static slope stability analysis. The seismic coefficient is calibrated to (a) a target intensity level related to the degree of consequences associated with slope failure, and (b) slope characteristics including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly and fully supported by TASK_FILE lines 7-8, which request an introduction covering the performance-based seismic coefficient, target intensity calibration, failure consequence severity, and slope properties (stiffness, strength, fundamental periods). No content was added beyond what the task specifies.]

### SLOT 2: State of Current Practice for Performance-Based Seismic Slope Design

This section surveys the current state of practice for performance-based seismic design of slopes. The scope encompasses existing standards, guidelines, and technical recommendations that govern seismic slope design through limit-equilibrium models.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests a state-of-practice section and specifies the scope as standards ("normativas"), guidelines, and recommendations for performance-based seismic slope design via limit equilibrium.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed in the approach described by the memo. The section covers the definitions of rigid-block and flexible-block idealizations and identifies which displacement prediction methods apply to each block type.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a summary of Newmark displacement methodologies and explicit treatment of the rigid-block versus flexible-block distinction.]

### SLOT 4: Appendix - Newmark Displacement Equations by Method

A detailed appendix presenting the Newmark displacement equations for each method covered in SLOT 3. Where available, the appendix specifies the types of failure surfaces for which each regression model was calibrated. The standard-error or uncertainty term associated with each predictive model is also reported.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests an appendix with detailed Newmark displacement equations, failure-surface calibration scope ("tipos de figuras de falla"), and error terms ("termino del error") for each method.]

### SLOT 5: Ensemble Numerical Model

This section presents the numerical model used in the current work. The model is constructed as a weighted ensemble (weighted sum) of the individual Newmark displacement models detailed in the appendix (SLOT 4). The weighting scheme assigns greater weight to more recent models that were calibrated using larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which requests a section on the ensemble model, the weighted-sum structure, and the emphasis on modern models calibrated with larger datasets.]

## CONSTRAINTS

- Output language: English.
- Prose style: professional, suitable for an executive memo.
- Document type: executive memo presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope.
- A reference document in kb/ contains a summary of the methodology; downstream workflows should consult it as a source, noting that the original material requires substantial reorganization and rewriting.
^[Confidence: HIGH, Rationale: All four constraints derive directly from TASK_FILE: English output (line 3, "en ingles"), professional style (line 3, "estilo profesional"), executive memo format (line 3, "memo ejecutivo"), and the kb/ reference note (lines 5-6, which state the summary is poorly written and poorly organized).]
