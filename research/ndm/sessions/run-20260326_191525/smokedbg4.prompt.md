# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slope Stability

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Objective

Present an introductory section that frames the problem of selecting a horizontal seismic coefficient for pseudo-static slope stability analysis. The core objective is to calibrate the seismic coefficient to (a) a target seismic intensity level, which relates to the degree of consequences associated with slope failure, and (b) the physical characteristics of the slope, including stiffness, strength, and fundamental period. The section establishes the rationale for a performance-based approach to seismic coefficient selection.
^[Confidence: HIGH, Rationale: This slot is directly justified by TASK_FILE lines 7-8, which request a section introducing the problem and explicitly specify the calibration targets (intensity level tied to failure consequences, slope characteristics including stiffness, strength, and fundamental periods). No content is invented beyond what the task states.]

### SLOT 2: Current State of Practice for Performance-Based Seismic Slope Design

Survey and synthesize the current normative frameworks, published guidelines, and recognized professional recommendations that govern performance-based seismic design of slopes using limit equilibrium models. The section identifies which standards and guidance documents are most relevant to the selection of seismic coefficients calibrated through displacement-based criteria.
^[Confidence: HIGH, Rationale: This slot is directly justified by TASK_FILE lines 9-10, which request a state-of-practice section and explicitly call for research into standards, guidelines, and recommendations for performance-based seismic slope design via limit equilibrium models. The scope is clearly distinct from SLOT 1 (which introduces the problem) and from SLOT 3 (which addresses Newmark methods specifically).]

### SLOT 3: Newmark Displacement Analysis Methodologies

Summarize the Newmark displacement analysis methods employed within this methodology. The section defines the rigid-block and flexible-block idealizations, explains the physical basis for each, and identifies which analytical methods apply to rigid-block conditions and which apply to flexible-block conditions.
^[Confidence: HIGH, Rationale: This slot is directly justified by TASK_FILE lines 12-13, which request a section summarizing Newmark displacement methodologies and explicitly require explanation of rigid-block and flexible-block definitions along with the methods applicable to each. No content is added beyond the stated requirements.]

### SLOT 4: Appendix Detailing Newmark Displacement Equations by Method

Provide a detailed appendix listing the Newmark displacement equations for each method covered in the memo. For each regression model, specify (where information is available) the types of failure surfaces for which the model was calibrated and the associated error term or uncertainty characterization.
^[Confidence: HIGH, Rationale: This slot is directly justified by TASK_FILE lines 14-15, which request an appendix detailing Newmark displacement equations per method, the failure surface types used in calibration, and the error term of each model. All three sub-requirements are captured.]

### SLOT 5: Ensemble Numerical Model Description

Present the specific numerical model employed in this work. The model is constructed as a weighted ensemble (weighted sum) of the individual Newmark displacement models detailed in the appendix (SLOT 4). The section emphasizes that greater weight is assigned to more recent models, which were calibrated using larger ground-motion datasets, reflecting improved empirical support.
^[Confidence: HIGH, Rationale: This slot is directly justified by TASK_FILE lines 17-18, which request a section presenting the numerical model as an ensemble or weighted sum of models from the appendix and explicitly state that more weight goes to modern models calibrated with larger datasets. The emphasis requirement is preserved.]

## CONSTRAINTS

- Output language: English.
- Prose style: Professional, suitable for an executive memo addressed to a technical audience.
- Document format: Executive memo presenting the current state-of-practice methodology for estimating the horizontal seismic coefficient of a slope.
- Source material: A knowledge-base document in the `kb/` directory contains a preliminary summary of the methodology; it serves as contextual input but requires substantial restructuring and rewriting due to poor organization and writing quality in its current form.
^[Confidence: HIGH, Rationale: The language constraint (English) and style constraint (professional) are explicitly stated in TASK_FILE line 3. The executive memo format and subject-matter scope (horizontal seismic coefficient estimation) are established in the same line. The KB note derives from TASK_FILE lines 5-6, which describe the existing document as poorly written and poorly organized. No constraints are invented beyond what the task states.]
