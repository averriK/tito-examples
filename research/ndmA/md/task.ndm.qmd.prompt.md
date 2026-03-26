# Structured Prompt: Horizontal Seismic Coefficient Estimation for Slopes

## SLOTS

### SLOT 1: Problem Introduction - Performance-Based Seismic Coefficient Selection

Prepare an introductory section framing the engineering problem addressed by the memo. The central objective is the selection of a performance-based horizontal seismic coefficient ($k_h$) for use in pseudo-static slope stability analysis. The coefficient is calibrated to two groups of parameters: (a) a target ground-motion intensity level, which is linked to the severity of consequences associated with slope failure, and (b) the physical and dynamic characteristics of the slope itself, including stiffness, shear strength, and fundamental period.


### SLOT 2: Current State of Practice - Standards, Guidelines, and Recommendations

Prepare a section surveying the current state of practice for performance-based seismic design of slopes. Investigate and summarize the applicable standards, design codes, published guidelines, and professional recommendations that govern seismic slope stability assessment through limit-equilibrium models. Include normative references from regulatory and professional bodies where available.


### SLOT 3: Newmark Displacement Analysis Methodologies - Rigid and Flexible Block Models

Prepare a section summarizing the Newmark sliding-block displacement analysis methodologies employed within the overall framework. Define the rigid-block and flexible-block idealizations, explain the physical assumptions underlying each, and identify which displacement prediction methods are applicable to each block type.


### SLOT 4: Appendix - Newmark Displacement Equations, Calibration, and Error Terms

Prepare a detailed appendix presenting, for each Newmark displacement prediction method, the complete regression equations. Where information is available, specify the types of failure surfaces (e.g., shallow translational, deep rotational) for which each regression model was calibrated. Report the standard error term or equivalent uncertainty measure associated with each model.


### SLOT 5: Ensemble Numerical Model - Weighted Sum of Displacement Predictions

Prepare a section presenting the specific numerical model used in this methodology. The model is a weighted ensemble, i.e., a weighted sum of the individual Newmark displacement prediction models documented in the appendix (SLOT 4). Emphasize that more recent models, which were calibrated against larger and more comprehensive ground-motion datasets, receive proportionally greater weight in the ensemble.


### SLOT 6: Seismic Coefficient Derivation from Target Residual Displacement

Prepare a section presenting the methodology for back-calculating the peak horizontal seismic coefficient ($k_{max}$) once the ensemble-estimated mean Newmark displacement has been obtained. Given a target allowable residual displacement, present the defining equations that relate $k_{max}$ to the Newmark displacement framework and explain the inversion procedure that yields the design seismic coefficient.


## CONSTRAINTS

- The output document language is English throughout.


- The document adopts a professional executive-memo register and tone.


- The knowledge base directory (kb/) contains reference material summarizing the methodology. This source is described as poorly written and poorly organized; downstream workflows should restructure and rewrite rather than reproduce its phrasing.

