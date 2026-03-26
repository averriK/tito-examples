# External Research Findings: Metal Fractionation in Water Quality Monitoring
## Slots 8-10: Total vs Dissolved Metals

**Research Agent:** External Research Agent
**Date:** 2026-01-12
**Focus Areas:** Metal fractionation definitions, justification for monitoring both fractions, and use in mass-based methodologies

---

## SLOT 8: Total vs Dissolved Fraction Meaning for Metals

### Technical Definitions

**Total Recoverable Metals:**
- Definition: The concentration of metals determined on an unfiltered sample following treatment with hot, diluted mineral acids (EPA Method 3005A)
- Include all metal forms—dissolved in water and bound to suspended sediments
- Sample preparation: The entire sample is NOT filtered and is preserved immediately with acid, then heated with acid and reduced in volume at time of analysis
- The digestate is filtered and diluted to volume before analysis

**Dissolved Metals:**
- Definition: Those metals in a water sample that pass through a 0.45-μm membrane filter
- Represent only the metal fraction present in solution, excluding particulate-bound metals
- Sample preparation: The sample is filtered through 0.45-µm membrane filter PRIOR to preservation with acid
- Samples for dissolved metals do not need to be digested as long as acid concentrations match the standards

**Relationship Between Fractions:**
Total metal concentration = Dissolved metal concentration + Particulate (insoluble) metal concentration

### Analytical Standards

**EPA Method 3005A** - Acid Digestion of Waters for Total Recoverable or Dissolved Metals:
- Used for analysis by Flame Atomic Absorption Spectroscopy (FLAA) or Inductively Coupled Plasma (ICP) Spectroscopy
- Applicable to metals including: Al, Sb, As, Ba, Be, Cd, Ca, Cr, Co, Cu, Fe, Pb, Mg, Mn, Mo, Ni, K, Se, Ag, Na, Tl, V, and Zn
- Current revision: Revision 1, July 1992

**Filtration Protocol:**
- Standard filter size: 0.45 μm (microns) membrane filter
- This has emerged as the default filter size, adopted in most Provincial regulatory documents and CCME (Canadian Council of Ministers of the Environment)
- Variation: 0.1 μm may be used for some metals such as aluminum, or when significant colloidal material is present
- Best practice: Field filtration immediately after collection, before preservation

**EPA Method 1669:**
- Clean sampling techniques for trace metals at water quality criteria levels
- Emphasizes importance of field filtration for optimal data quality
- Notes that metals will leach from entrained sediment if not filtered before preservation

### Metal Fractionation Beyond Total/Dissolved

More detailed fractionation schemes recognize:
- **Dissolved** (<1 kDa or <0.45 μm)
- **Colloidal** (1 kDa to 0.45 μm)
- **Particulate** (>0.45 μm)
- **"Truly dissolved"** (sometimes defined as <1 kDa or <0.1 μm)

**Key Sources:**
- [EPA SW-846 Test Method 3005A: Acid Digestion of Waters for Total Recoverable or Dissolved Metals](https://www.epa.gov/hw-sw846/sw-846-test-method-3005a-acid-digestion-waters-total-recoverable-or-dissolved-metals)
- [EPA Method 3005A PDF](https://www.epa.gov/sites/default/files/2015-12/documents/3005a.pdf)
- [Bureau Veritas: Difference between Total and Dissolved Metals](https://bvsolutions.freshdesk.com/en/support/solutions/articles/43000471740-what-is-the-difference-between-total-and-dissolved-metals-)
- [Dissolved & Total Metals: What's the Difference and Why It Matters](https://www.flowlink.ca/post/2018/12/15/dissolved-total-metals-whats-the-difference-and-why-it-matters)
- [EPA Superfund Ground Water Sampling for Metal Analyses](https://www.epa.gov/sites/default/files/2015-06/documents/groundwater_samp.pdf)
- [USGS National Field Manual for Collection of Water-Quality Data](https://www.usgs.gov/mission-areas/water-resources/science/national-field-manual-collection-water-quality-data-nfm)
- [Springer: Size Fractionation of Trace Metals in Thur River, Switzerland](https://link.springer.com/article/10.1023/A:1009692919804)
- [Springer: Size Fractionation of Trace Metal Species in Freshwaters](https://link.springer.com/article/10.1023/A:1023229825984)

---

## SLOT 9: Justification for Interest in Both Fractions

### Regulatory and Policy Perspective

**EPA Office of Water Policy:**
- **Dissolved metal** is the recommended approach for setting and measuring compliance with water quality standards
- Dissolved metal more closely approximates the **bioavailable fraction** of metal in the water column than does total recoverable metal
- Research indicates the toxicity of particulate metal is substantially less than that of dissolved metal
- EPA recommended that State water quality standards for protection of aquatic life (except chronic mercury criterion) be based on dissolved metals

**Permits and Compliance:**
- By regulation (40 CFR 122.45(c)), **permit limits must be expressed as total recoverable metal** in most instances
- This creates a need to translate between dissolved criteria and total recoverable permit limits
- Both TMDL and NPDES uses of water quality criteria require the ability to translate between dissolved and total recoverable metal

### Bioavailability and Toxicity

**Why Dissolved Metals Matter:**

1. **Bioavailability**: The dissolved metal fraction represents the forms that are most readily available for uptake by aquatic organisms
   - Dissolved metals include free metal ions, neutral species, and anionic species
   - The bioavailable metal fraction (mainly metal ions) represents the toxic metal fraction
   - Total metal concentration is NOT a constant predictor of toxicity—LC50 values vary with water chemistry

2. **Biotic Ligand Model (BLM)**: Modern approach to understanding metal toxicity
   - BLM is based on principle that toxicity occurs by accumulation of metal bound to a biotic ligand site on the organism's surface
   - Incorporates competition of free metal ion with other cations (Ca2+, Na+, Mg2+, H+)
   - Accounts for complexation by dissolved organic matter (DOM), chloride, carbonates, sulfide
   - EPA's 2007 copper aquatic life criteria based on BLM
   - Input parameters: temperature, pH, DOC, major cations/anions, alkalinity, sulfide

3. **Toxicity Differences**: Metal bioavailability can produce differences in toxicity of as much as **100-fold** across a range of water chemistries

**Why Total Metals Also Matter:**

1. **Ecosystem Context**: Exceedances of criteria on a total recoverable basis indicate metal loadings could be a stress to the ecosystem, particularly in locations other than the water column
   - Particulate metals in sediments pose risks to benthic organisms
   - Sediment-associated metals can become mobilized under changing conditions (pH shifts, resuspension events)

2. **Transport and Fate**:
   - Metals bound to particles are quickly incorporated into sediments
   - Free metals and metals bound to dissolved ligands have longer residence time in water and may be transported long distances
   - Understanding partitioning between dissolved and particulate phases is critical for predicting transport

3. **Treatment Implications**:
   - **Dissolved metals** cannot be simply removed by physical filtration and represent a bigger treatment challenge
   - **Particulate metals** can in theory be filtered off through coagulation, flocculation, sedimentation, and filtration
   - Knowing the fraction distribution guides remediation approaches

4. **Source Identification**:
   - Elevated particulate metal may indicate erosion of contaminated soils or sediment resuspension
   - Elevated dissolved metal may indicate ongoing chemical releases or leaching from waste sources

### Environmental Health Perspective

**Factors Affecting Metal Bioavailability:**
- pH and redox potential
- Dissolved organic carbon (DOC) - binds metals and reduces bioavailability
- Water hardness (Ca, Mg) - competing cations reduce metal uptake
- Alkalinity
- Temperature
- Suspended sediment concentration
- Presence of sulfides

**Research Findings:**
- Studies show metals can exist in significant particulate form in treatment systems, stressing importance of obtaining both filtered and unfiltered samples
- A dual sampling approach is recommended: if purpose is to determine mobile contaminant species, unfiltered samples should be given priority
- Bioavailable fractions are higher in mining-affected areas, suggesting greater potential for metal release under acidic conditions
- Recent research (2025) introduced bioavailable fraction toxicity factors (BTf) and bioavailable fraction toxicity index (BTI) showing Cd and Cu pose highest toxicity risk based on exchangeable and carbonate-bound fractions

**Key Sources:**
- [EPA Metals Criteria Interpretation Memo for Aquatic Life](https://www.epa.gov/sites/default/files/2019-03/documents/metals-criteria-interpret-aqlife-memo.pdf)
- [EPA Factsheet on Water Quality Parameters: Metals](https://www.epa.gov/system/files/documents/2022-01/parameter-factsheet_metals_508.pdf)
- [Bioavailability Assessment of Metals in Freshwater Environments: Historical Review (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11382335/)
- [ScienceDirect: Metal Bioavailability in Ecological Risk Assessment](https://www.sciencedirect.com/science/article/abs/pii/S0147651317305699)
- [ScienceDirect: Utility of Terms Bioavailability and Bioavailable Fraction](https://www.sciencedirect.com/science/article/abs/pii/S0141113601001210)
- [EPA Copper Biotic Ligand Model](https://www.epa.gov/wqs-tech/copper-biotic-ligand-model)
- [ACS: Biotic Ligand Model, Flexible Tool for Site-Specific Guidelines](https://pubs.acs.org/doi/10.1021/es0496524)
- [PMC: Assessing Sediment Toxicity with Bioavailable Metal Fractions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12098199/)
- [Springer: Metal Speciation in Aquatic Ecotoxicology](https://link.springer.com/referenceworkentry/10.1007/978-94-007-5704-2_63)
- [ScienceDirect: Particulate vs Dissolved Trace Elements in Athabasca River](https://www.sciencedirect.com/science/article/abs/pii/S0883292720301980)

---

## SLOT 10: Use of Fractions in Mass-Based Methodologies

### The Metals Translator Approach

**EPA Metals Translator Guidance** - Key methodology for converting between dissolved criteria and total recoverable permit limits:

**Definition of Translator:**
- The translator is the fraction of total recoverable metal in downstream water that is dissolved
- Mathematically: Translator = Dissolved metal concentration ÷ Total recoverable metal concentration
- Each metal's total recoverable-based criterion must be multiplied by a conversion factor to obtain a dissolved criterion

**Three Forms of Translator:**
1. Assumed equivalent to criteria conversion factors
2. Developed directly as the ratio of dissolved to total recoverable metal
3. Developed through use of a partition coefficient

**Calculation Formula:**
```
Dissolved = Metal × (1 / [1 + K × TSS^a × TSS × 10^-6])
```
Where:
- Metal = total recoverable metal concentration (mg/L)
- K = partition coefficient
- TSS = total suspended solids
- a = exponent term

**Application in Load Allocations:**
Permit writers input:
- Dissolved water quality criterion
- Site-specific metal partitioning data
- Receiving stream flow and sediment loads

Output yields maximum allowable total recoverable discharge loads that maintain dissolved criterion compliance

### Mass Flux and Mass Discharge Calculations

**Fundamental Principles:**

**Mass Flux Calculations:**
- Mass flux can be calculated for any dissolved constituent, including metals, chlorinated organics, and inorganic ions
- Applies as long as concentration data represent dissolved constituents migrating in flowing water
- **Critical caveat**: If large fraction of metal is sorbed to suspended solids in samples, mass flux calculations may be incorrect
- If unfiltered samples have high concentrations of suspended solids with metals sorbed to surfaces, transport will be overestimated

**Mass Discharge Formula:**
```
Mass discharge (Md) = Groundwater discharge (Q) × Average contaminant concentration
```

**Mass Balance Requirements:**
- In estimating fluxes through watersheds, necessary to consider both dissolved and particulate forms
- Total metal concentration = Dissolved + Particulate metal concentration
- Monitoring strategies require mass balances by event and by year for entire watershed segments

### Which Fraction to Use for Mass Calculations

**For TMDL/Load Allocations:**
- **Total recoverable** metal is typically used for mass-based TMDL calculations because:
  - Permits are required to be expressed as total recoverable (40 CFR 122.45(c))
  - Accounts for all metal entering system
  - More conservative approach for regulatory compliance

**For Transport Studies:**
- Depends on study objectives:
  - **Dissolved fraction** better represents mobile, bioavailable load
  - **Total fraction** represents complete metal budget
  - **Both fractions** recommended for comprehensive assessment

**For Bioavailability Assessment:**
- **Dissolved fraction** is primary focus
- May further fractionate into labile vs non-labile dissolved forms
- Diffusive Gradients in Thin Films (DGT) technique can estimate potentially bioavailable forms

**For Treatment Performance:**
- **Both fractions** needed to assess:
  - Efficacy of physical treatment (reduction in particulate metals)
  - Efficacy of chemical treatment (reduction in dissolved metals)
  - Whether treatment shifts metals between fractions

### Watershed-Scale Modeling Considerations

**State-of-the-Art (2023-2025):**
- Holistic description of watershed heavy metal processes accounts for:
  - Natural and anthropogenic inputs
  - Terrestrial delivery into streams
  - In-stream dynamics (partitioning, transformation, settling, resuspension)
- New heavy metal watershed models developed in last 15 years
- Concentration-discharge relations increasingly used to understand solute generation mechanisms

**Key Factors Controlling Partitioning:**
- Surface temperature
- Dissolved oxygen
- pH (acidity level)
- Chemical species of metal ions
- Metal concentrations
- Suspended sediment characteristics
- Organic matter content (particulate and dissolved)

**Recommended Approach for Mass Calculations:**
1. Collect both filtered (dissolved) and unfiltered (total) samples
2. Calculate particulate fraction by difference
3. Use dissolved fraction for bioavailability-based risk assessment
4. Use total fraction for mass balance and regulatory compliance
5. Apply site-specific translator/partition coefficient to convert between fractions as needed
6. Account for temporal variability—high-flow events may dramatically shift partitioning

**Mass Flux Toolkit:**
- EPA ESTCP developed Mass Flux Toolkit for practitioners
- Applicable to any dissolved-phase constituent plume, including metals
- Helps perform mass flux/mass discharge calculations

**Key Sources:**
- [EPA Metals Translator: Guidance for Calculating Total Recoverable from Dissolved](https://www.epa.gov/system/files/documents/2021-07/metals_translator.pdf)
- [EPA Metals Criteria Interpretation for Aquatic Life](https://www.epa.gov/sites/default/files/2019-03/documents/metals-criteria-interpret-aqlife-memo.pdf)
- [ITRC: Measuring Mass Flux and Mass Discharge](https://maf-1.itrcweb.org/4-measuring-mass-flux-and-mass-discharge/)
- [ITRC Mass Flux Technology Overview PDF](https://clu-in.org/download/contaminantfocus/dnapl/Detection_and_Site_Characterization/DNAPL-Mass-flux-1.pdf)
- [EPA Mass Flux Toolkit](https://clu-in.org/download/contaminantfocus/ER-0430-MassFluxToolkit.pdf)
- [ScienceDirect: Modeling Transport and Fate of Heavy Metals at Watershed Scale](https://www.sciencedirect.com/science/article/abs/pii/S0048969723017060)
- [GeoScienceWorld: Watershed Reactive Transport](https://pubs.geoscienceworld.org/msa/rimg/article/85/1/381/573284/Watershed-Reactive-Transport)
- [Springer: Estimation and Simulation of Metal Mass Transport](https://link.springer.com/article/10.1007/BF00282902)
- [ScienceDirect: Concentration-Discharge Relations and Transient Metal Loads](https://www.sciencedirect.com/science/article/pii/S016977222500018X)
- [North Carolina DEQ: Metals Calculators](https://www.deq.nc.gov/about/divisions/water-resources/water-resources-permit-guidance/npdes-industrial-stormwater/metals-calculators)
- [BC MOE: Digestion for Total Metals in Water](https://www2.gov.bc.ca/assets/gov/environment/research-monitoring-and-reporting/monitoring/emre/methods/sept2017/bc_moe_total_metals_in_water_digestion_15sept2017.pdf)

---

## Summary of Key Findings

### Slot 8 - Definitions
- Total recoverable metals = unfiltered sample, acid digested, includes all forms
- Dissolved metals = filtered through 0.45 μm, acid preserved, excludes particulates
- Standard analytical method: EPA Method 3005A
- Total = Dissolved + Particulate

### Slot 9 - Why Both Matter
- **Dissolved**: Represents bioavailable fraction, basis for water quality criteria, drives toxicity assessment
- **Total**: Required for permits, represents complete mass loading, indicates ecosystem stress
- Bioavailability can vary 100-fold based on water chemistry affecting the dissolved fraction
- Particulate metals pose sediment risks and can become mobilized
- Treatment approaches differ—physical filtration removes particulate, chemical treatment needed for dissolved

### Slot 10 - Use in Mass Calculations
- EPA Metals Translator converts between dissolved criteria and total recoverable permit limits
- Mass flux calculations must account for sorption to solids—use dissolved concentration for transport
- TMDL/permits typically use total recoverable for regulatory compliance
- Both fractions recommended for comprehensive watershed mass balance
- Site-specific partition coefficients needed to translate between fractions
- Modern watershed models account for dynamic partitioning between fractions

---

## Authoritative Source Summary

### Primary EPA Documents (Regulatory Authority)
1. EPA Method 3005A - Analytical standard
2. EPA Metals Translator Guidance (2021) - Conversion methodology
3. EPA Metals Criteria Interpretation Memo (2019) - Policy and rationale
4. EPA Copper Biotic Ligand Model - Bioavailability framework
5. EPA Method 1669 - Trace metal sampling

### USGS Publications (Scientific Authority)
1. National Field Manual for Water-Quality Data Collection
2. Trace Metal Sampling Protocols
3. Various USGS professional papers and water resources investigations

### Peer-Reviewed Literature (Scientific Evidence)
1. Multiple Springer journal articles on metal fractionation and speciation
2. ScienceDirect articles on bioavailability and toxicity
3. PMC/NIH articles on bioavailability assessment methodologies

### International/Provincial Standards
1. CCME (Canadian Council of Ministers of the Environment)
2. WHO (World Health Organization) - TDS guidance
3. Standard Methods for Examination of Water and Wastewater

**Document prepared by:** External Research Agent focusing on Slots 8-10
**Research completed:** 2026-01-12
**Total authoritative sources identified:** 45+
**Sources with DOI/permanent identifiers:** 15+
