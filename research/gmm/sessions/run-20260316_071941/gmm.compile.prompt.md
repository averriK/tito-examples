# Ground Motion Models (GMMs) - Structured Prompt

## SLOTS

### SLOT 1: Definitions, notation, and equations for the GMM framework

Identify and introduce the definitions, notation conventions, and equations necessary for the chapter to explain the GMM framework clearly. This includes mathematical notation for ground-motion prediction (e.g., median prediction, aleatory variability terms, standard deviation components), standard symbols used across GMPEs, and the formal structure of a ground-motion prediction equation. The purpose is to establish the technical vocabulary and formalism before the per-region sections.

This slot covers question 0 in the task: "What definitions, notation, and equations should be introduced so that the chapter can explain the GMM framework clearly?"

### SLOT 2: Definition of GMM/GMPE in the context of PSHA

Define what a ground motion model (GMM), also referred to as a ground motion prediction equation (GMPE), is in the context of probabilistic seismic hazard analysis (PSHA). Explain the role that GMMs play in PSHA and why they constitute one of the main sources of epistemic uncertainty.

This slot covers question 1 in the task: "What is a GMM or GMPE in the context of PSHA?" It also addresses the framing in the task preamble that GMMs are "a key part of PSHA and one of the main sources of epistemic uncertainty."

### SLOT 3: Epistemic uncertainty and ground-motion logic trees

Explain how epistemic uncertainty is represented in a ground-motion logic tree. Describe the structure and purpose of logic trees as a mechanism for capturing model-to-model uncertainty in ground-motion prediction, including how alternative GMPEs and their assigned weights are organized within the tree.

This slot covers question 2 in the task: "How is epistemic uncertainty represented in a ground-motion logic tree?"

### SLOT 4: Active Shallow Crust (ASC) - GMPEs and logic tree

For the Active Shallow Crust (ASC) tectonic region type, document the following for each GMPE included in the logic tree:

- Model reference (author, year, publication)
- Whether the model was calibrated for the ASC regime
- Magnitude and distance range for which the model was calibrated
- Distance metric used by the model in the OpenQuake hazard library
- Weight assigned to the GMPE in the logic tree
- If the supporting material explains why the model was selected or weighted in that way, a brief summary of that basis

Also describe the overall structure of the logic tree used for ASC.

This slot covers question 3 in the task, specific to the ASC tectonic region type.

### SLOT 5: Stable Continental Crust (SCC) - GMPEs and logic tree

For the Stable Continental Crust (SCC) tectonic region type, document the following for each GMPE included in the logic tree:

- Model reference (author, year, publication)
- Whether the model was calibrated for the SCC regime
- Magnitude and distance range for which the model was calibrated
- Distance metric used by the model in the OpenQuake hazard library
- Weight assigned to the GMPE in the logic tree
- If the supporting material explains why the model was selected or weighted in that way, a brief summary of that basis

Also describe the overall structure of the logic tree used for SCC.

This slot covers question 4 in the task, specific to the SCC tectonic region type.

### SLOT 6: Subduction Interface (SIF) - GMPEs and logic tree

For the Subduction Interface (SIF) tectonic region type, document the following for each GMPE included in the logic tree:

- Model reference (author, year, publication)
- Whether the model was calibrated for the SIF regime
- Magnitude and distance range for which the model was calibrated
- Distance metric used by the model in the OpenQuake hazard library
- Weight assigned to the GMPE in the logic tree
- If the supporting material explains why the model was selected or weighted in that way, a brief summary of that basis

Also describe the overall structure of the logic tree used for SIF.

This slot covers question 5 in the task, specific to the SIF tectonic region type.

### SLOT 7: Subduction Intraslab (SIS) - GMPEs and logic tree

For the Subduction Intraslab (SIS) tectonic region type, document the following for each GMPE included in the logic tree:

- Model reference (author, year, publication)
- Whether the model was calibrated for the SIS regime
- Magnitude and distance range for which the model was calibrated
- Distance metric used by the model in the OpenQuake hazard library
- Weight assigned to the GMPE in the logic tree
- If the supporting material explains why the model was selected or weighted in that way, a brief summary of that basis

Also describe the overall structure of the logic tree used for SIS.

This slot covers question 6 in the task, specific to the SIS tectonic region type.

### SLOT 8: Basis for equally weighted logic tree branches

All logic trees in this assessment use equally weighted branches. Explain the basis for choosing a large number of equally weighted branches. In particular, if the purpose of the GMM framework is to generalize as broadly as possible in regions where recorded ground motions or accelerograms are insufficient to calibrate the logic tree directly, explain why equal weighting is the chosen approach for representing epistemic uncertainty in such data-scarce regions.

This slot covers question 7 in the task: "What is the basis for choosing a large number of equally weighted branches?" and "explain why this is the chosen way to represent epistemic uncertainty in regions of this type."

## CONSTRAINTS

- The final output must be written in English.
- The output is structured as a chapter with one section for each tectonic region type: Active Shallow Crust (ASC), Stable Continental Crust (SCC), Subduction Interface (SIF), and Subduction Intraslab (SIS).
- Focus exclusively on information required to document the GMM framework, logic trees, model weights, definitions, and equations. Disregard unrelated material in the knowledge base.
- Mathematical expressions must use LaTeX notation ($...$ for inline, $$...$$ for display).
- Professional, impersonal academic voice throughout; no instructional, promotional, or second-person language.
- ASCII text only (no accented characters, smart quotes, em-dashes, or non-LaTeX Unicode symbols).
- Preserve all citation tokens ([KB:...], [WEB:...], [DOI:...], [ARXIV:...]) exactly as they appear.
