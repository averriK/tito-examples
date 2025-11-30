# Appendix: SRK Ground-Motion Intensity Model

## Introduction

The SCR Ground-Motion Intensity Model is an integrated ensemble of ground-motion prediction equations implemented through three region-specific logic trees, corresponding to GEM, USGS and Canadian SHM6 seismic hazard configurations. 
The intensity model is represented in OpenQuake by three NRML logic trees: a GEM configuration, a USGS CEUS configuration, and a Canadian SHM6 configuration. 

## GEM SCC ensemble
Within the GEM logic tree, stable continental crust (SCC) is represented by a three-branch SRK ensemble. One branch uses the ESHM20Craton model derived from the European Seismic Hazard Model 2020, which characterises ground motions in European and adjacent cratonic regions [@DanciuEtAl2021]. A second branch uses the Rietbrock and Edwards (2019) model, which was calibrated for stable crust in the United Kingdom and northern Europe [@RietbrockEdwards2019]. A third branch uses the Shahjouei and Pezeshk (2016) model, developed for central and eastern North America and representative of broader stable continental behaviour [@ShahjoueiPezeshk2016]. The corresponding logic-tree weights are 0.34 for ESHM20Craton, and 0.33 for each of Rietbrock–Edwards and Shahjouei–Pezeshk, such that all three branches together form a balanced, modern representation of SCC motions suitable for GEM-style applications.

## USGS NGA-East ensemble
Within the USGS logic tree, stable continental crust motions are represented by the full NGA-East USGS ensemble as documented in the USGS central and eastern United States hazard model [@USGSNGAEast; @GouletEtAl2018]. This ensemble consists of seventeen "Sammons" branches, each representing a weighted combination of NGA-East candidate models derived using the Sammons mapping and averaging procedure, and six seed models corresponding to individual NGA-East candidate GMPEs (for example models by Graizer, Frankel, Yenier and Atkinson, and Pezeshk and co-authors).

## Canadian SHM6 SCC ensemble
Within the SHM6 logic tree, stable continental crust motions are represented by the logic tree from the Sixth Generation Seismic Hazard Model of Canada. Thirteen branches correspond to submodels of CanadaSHM6_StableCrust_NGAEast, each tied to a different NGA-East realisation and carrying unconditional weights that sum to 0.5. These branches also have intensity-measure-specific weights, which allow the relative contribution of each submodel to vary with spectral period, reflecting the period-dependent epistemic uncertainty inferred from NGA-East. The remaining 0.5 of the SCC weight is allocated to three branches based on the Atkinson and Adams (2013) stable-crust model for eastern Canada, representing high, central and low median levels with unconditional weights of 0.15, 0.25 and 0.10, respectively. This ensemble therefore combines NGA-East based models with national Canadian practice in a single stable-crust logic tree.


