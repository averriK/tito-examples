Ground motion models (GMMs), also referred to as ground motion prediction equations (GMPEs), are a key part of PSHA and one of the main sources of epistemic uncertainty. This chapter should document the GMPE logic tree used in the assessment and the GMPEs assigned to each tectonic region type.

The final output must be written in English as a chapter with one section for each of the following tectonic region types:
- Active Shallow Crust (ASC)
- Stable Continental Crust (SCC)
- Subduction Interface (SIF)
- Subduction Intraslab (SIS)

The knowledge base may contain other material that is not needed for this chapter. Focus only on the information required to document the GMM framework, the logic trees, the model weights, the definitions, and the equations needed to explain the chapter.

Questions to answer:

0. What definitions, notation, and equations should be introduced so that the chapter can explain the GMM framework clearly?
1. What is a GMM or GMPE in the context of PSHA, 
2. how is epistemic uncertainty represented in a ground-motion logic tree?
3. For Active Shallow Crust (ASC), what GMPEs are included in the logic tree used for this tectonic region type? For each GMPE, identify the model reference, confirm whether it was calibrated for the corresponding regime, confirm the magnitude and distance range for which it was calibrated, report the type of distance metric used by the model in the OpenQuake hazard library, and report the weight assigned to that GMPE in the logic tree. If the supporting material explains why the model was selected or weighted in that way, summarize that basis briefly. Also describe the logic tree used for ASC.

4. For Stable Continental Crust (SCC), what GMPEs are included in the logic tree used for this tectonic region type? For each GMPE, identify the model reference, confirm whether it was calibrated for the corresponding regime, confirm the magnitude and distance range for which it was calibrated, report the type of distance metric used by the model in the OpenQuake hazard library, and report the weight assigned to that GMPE in the logic tree. If the supporting material explains why the model was selected or weighted in that way, summarize that basis briefly. Also describe the logic tree used for SCC.

5. For Subduction Interface (SIF), what GMPEs are included in the logic tree used for this tectonic region type? For each GMPE, identify the model reference, confirm whether it was calibrated for the corresponding regime, confirm the magnitude and distance range for which it was calibrated, report the type of distance metric used by the model in the OpenQuake hazard library, and report the weight assigned to that GMPE in the logic tree. If the supporting material explains why the model was selected or weighted in that way, summarize that basis briefly. Also describe the logic tree used for SIF.

6. For Subduction Intraslab (SIS), what GMPEs are included in the logic tree used for this tectonic region type? For each GMPE, identify the model reference, confirm whether it was calibrated for the corresponding regime, confirm the magnitude and distance range for which it was calibrated, report the type of distance metric used by the model in the OpenQuake hazard library, and report the weight assigned to that GMPE in the logic tree. If the supporting material explains why the model was selected or weighted in that way, summarize that basis briefly. Also describe the logic tree used for SIS.

7. All of the logic trees used here are equally weighted. What is the basis for choosing a large number of equally weighted branches? In particular, if the purpose of the GMM framework is to generalize as much as possible in regions where there are not enough recorded ground motions or accelerograms to calibrate the logic tree directly, explain why this is the chosen way to represent epistemic uncertainty in regions of this type.
