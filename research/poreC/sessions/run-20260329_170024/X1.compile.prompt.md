# Structured Prompt: Pore Pressure Increment Proxy Model for Saturated Fine-Grained Soils Under Seismic Loading

## CONTEXT

The overarching research objective is to formulate a simple proxy model for predicting the pore pressure increment in a saturated fine-grained material subjected to a seismic acceleration record. The physical setting consists of a homogeneous, saturated, fine-grained stratum of thickness $H_s$ resting on rock, with depth-variable shear modulus $G_o(z)$ whose maximum value $G_o = G(z=0)$ occurs at the base. The stratum is subjected to base accelerations $a_g(t)$. The KB/ directory contains analytical closed-form solutions for the site response expressed as instantaneous accelerations $a(t,z)$ at various depths within the stratum.

## SLOTS

### SLOT 1: Numerical strategies for estimating maximum shear strain during a seismic event

Identify and describe the numerical strategies available for estimating the maximum shear strain throughout the duration of a seismic event in a 1D site-response context. Specifically address the RMS-based approach and the max-max approach, together with any other relevant strategies recognized in earthquake geotechnical engineering. For each strategy, present the advantages and disadvantages.

### SLOT 2: Empirical methods for pore pressure increment from PGA and earthquake magnitude

Provide a concise reference summary of empirical methods that estimate the pore pressure increment from peak ground acceleration (PGA) and earthquake magnitude. This slot serves as background context; a brief overview of each method and its key parameters is sufficient. Detailed derivation or extended discussion is not required.

### SLOT 3: Numerical implementation strategies for pore pressure estimation from instantaneous shear strain

Describe the strategies for numerical implementation - whether closed-form analytical solutions or numerical methods - that, given a base acceleration history $a_g(t)$, permit estimation of pore pressure or excess pore pressure at a point within the fine-grained stratum. The estimation is to be derived from the instantaneous shear strain $\gamma(z,t)$ and the geotechnical properties of the material. Address both analytical and computational approaches to this problem.

### SLOT 4: Available R and Python libraries for advanced constitutive pore pressure models and 1D site response integration

Identify available libraries in R and Python for analyzing pore pressure increment through advanced constitutive models such as PM4Sand. Describe how these algorithms can be integrated into the workflow of a 1D site response analysis, considering both instantaneous-shear-strain-based and RMS-based approaches as input to the constitutive model.

### SLOT 5: Failure extent criteria and global failure definition in 1D liquefaction analysis

In a 1D liquefaction problem analyzed via instantaneous shear strains, address the following interconnected sub-questions: (a) the criteria for defining the spatial extent of zones where excess pore pressures exceed critical thresholds and the factor of safety drops below unity; (b) whether point failure (a single depth exceeding the threshold) is equivalent to failure of a proportion of the stratum thickness (e.g., 30%); (c) whether failure in deep zones carries the same engineering significance as failure in shallow zones; and (d) the design and analysis criteria for liquefaction potential that define global failure of a stratum.

## CONSTRAINTS

- The output document must be written in English.

- The document must follow a professional engineering methodology style.
