# Structured Prompt: Performance-Based Seismic Coefficient for Pseudo-Static Slope Analysis

This document defines the structured work items and global constraints for an executive memo on the current state-of-practice methodology for estimating the horizontal seismic coefficient of slopes. The source material resides in the kb/ directory and requires substantial reorganization and rewriting.


## SLOTS

### SLOT 1: Problem Introduction and Performance-Based Objective

This section introduces the core problem: selection of a horizontal seismic coefficient for pseudo-static slope stability analysis within a performance-based framework. The seismic coefficient is calibrated to (a) a target seismic intensity level, which reflects the severity of failure consequences, and (b) the mechanical and dynamic characteristics of the slope, including stiffness, strength, and fundamental period.


### SLOT 2: Current State of Practice - Standards, Guidelines, and Recommendations

This section surveys the current state of practice for performance-based seismic design of slopes using limit-equilibrium models. The survey identifies and summarizes existing standards, guidelines, and professional recommendations relevant to this design approach.


### SLOT 3: Newmark Displacement Analysis Methodologies

This section summarizes the Newmark displacement analysis methodologies employed in the overall framework. It defines the rigid-block and flexible-block idealizations and identifies which displacement estimation methods apply to each category.


### SLOT 4: Appendix - Detailed Newmark Displacement Equations

This appendix presents the full equations for Newmark displacement estimation under each method. Where information is available, it specifies the types of failure surfaces for which the regression models were calibrated. Each method's prediction error term (standard deviation or equivalent uncertainty measure) is included.


### SLOT 5: Ensemble Numerical Model

This section presents the numerical model adopted in this work, constructed as an ensemble - a weighted sum of the individual Newmark displacement methods detailed in the appendix (SLOT 4). Greater weight is assigned to more recent models that were calibrated using larger ground-motion datasets.


## CONSTRAINTS

- Output language: English.
- Document format: executive memo in professional style.
- Source material: the kb/ directory contains a summary of the methodology that requires substantial reorganization and rewriting; downstream workflows should use it as informational input, not as a formatting template.
- Mathematical notation: all equations and symbols in LaTeX format ($...$ for inline, $$...$$ for display).

