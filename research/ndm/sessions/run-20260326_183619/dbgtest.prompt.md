# Structured Prompt: Performance-Based Seismic Coefficient for Pseudo-Static Slope Analysis

This document defines the structured work items and global constraints for an executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of slopes. The source material resides in the kb/ directory and requires substantial reorganization and rewriting.
^[Confidence: HIGH, Rationale: The overall deliverable is stated explicitly in TASK_FILE line 3 as an executive memo presenting the state-of-practice methodology for horizontal seismic coefficient estimation. The KB source note appears on lines 5-6, describing it as poorly written and poorly organized.]

## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Objective

This section introduces the core problem: selection of a horizontal seismic coefficient for pseudo-static slope stability analysis within a performance-based framework. The seismic coefficient is calibrated to (a) a target seismic intensity level, which reflects the severity of failure consequences, and (b) the mechanical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE lines 7-8, which request an introductory section and specify the performance-based calibration objective tied to a target intensity level (related to failure consequences) and slope characteristics (stiffness, strength, fundamental periods). All elements in this slot trace to explicit TASK_FILE language.]

### SLOT 2: Current State of Practice - Standards, Guidelines, and Recommendations

This section surveys the current state of practice for performance-based seismic design of slopes using limit-equilibrium models. The survey identifies and summarizes existing standards, guidelines, and professional recommendations relevant to this design approach.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 9, which requests a state-of-practice section and specifies investigation of standards, guidelines, and recommendations for performance-based seismic slope design via limit-equilibrium models. No elements are added beyond what TASK_FILE requests.]

### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed in the overall framework. It defines the rigid-block and flexible-block idealizations and identifies which displacement estimation methods apply to each category.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 12, which requests a section summarizing Newmark displacement methodologies with explanation of rigid-block versus flexible-block definitions and the methods applicable to each. All scope elements trace to explicit TASK_FILE language.]

### SLOT 4: Appendix - Detailed Newmark Displacement Equations

This appendix presents the full equations for Newmark displacement estimation under each method. Where information is available, it specifies the types of failure surfaces for which the regression models were calibrated. Each method's prediction error term (standard deviation or equivalent uncertainty measure) is included.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 14, which requests a detailed appendix covering equations, failure-surface calibration types (qualified by "si es posible," reflected here as "where information is available"), and error terms for each method. All elements have explicit TASK_FILE justification.]

### SLOT 5: Ensemble Numerical Model

This section presents the numerical model adopted in this work, constructed as an ensemble - a weighted sum of the individual Newmark displacement methods detailed in the appendix (SLOT 4). Greater weight is assigned to more recent models that were calibrated using larger ground-motion datasets.
^[Confidence: HIGH, Rationale: Directly supported by TASK_FILE line 17, which describes the numerical model as an ensemble or weighted sum of different models from the appendix and emphasizes that more weight is assigned to modern models calibrated with larger datasets. All scope elements trace to explicit TASK_FILE language.]

## CONSTRAINTS

- Output language: English.
- Document format: executive memo in professional style.
- Source material: the kb/ directory contains a summary of the methodology that requires substantial reorganization and rewriting; downstream workflows should use it as informational input, not as a formatting template.
- Mathematical notation: all equations and symbols in LaTeX format ($...$ for inline, $$...$$ for display).
^[Confidence: HIGH, Rationale: Language and style constraints are stated in TASK_FILE line 3, which specifies English, professional style, and executive memo format. The KB source note derives from TASK_FILE lines 5-6. The mathematical notation constraint derives from FORMAT_RULES, which mandates LaTeX math for all expressions. No constraints are invented beyond these explicit sources.]
