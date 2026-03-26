# SSM1C - Seismic Source Model: Structured Prompt

## CONTEXT

The knowledge base (`kb/`) contains documentation of the regional seismic source model for India (IND) and the local source representation for the Rampura Agucha site. Key files include `kb/source_model.md`, `kb/site_sources.md`, `kb/site_sources_data.md`, and `kb/ind-report.pdf.md`.

Rampura-Agucha Mine (RAM) tailings storage facility (TSF) is owned and operated by Hindustan Zinc Limited (HZL), located approximately 220 km from Jaipur in Rajasthan, India. RAM is the second-largest zinc mine in the world.

The purpose of this chapter is to describe the seismic source model (SSM) adopted for the region and to interrogate that model at the site location. The SSM contains hundreds of sources and requires a global description covering architecture, source types, tectonic region types, logic tree, recurrence, depths, maximum magnitudes, and provenance. The site falls within one or two local seismic sources whose characterisation is of particular interest because they would produce the closest maximum credible earthquakes.

## SLOTS

### SLOT 1: SSM Overview and Source Census

Provide an overview of the seismic source model (SSM) structure. The SSM defines the spatial distribution, geometry, and earthquake occurrence rates of all seismogenic sources considered capable of contributing to ground-motion hazard at the site. It is the principal input to the probabilistic seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model logic tree (ssmLT) that captures epistemic uncertainty.

The overview must cover:

- Source types included in the model.
- Geographic extent of the model domain.
- Minimum earthquake magnitude ($M_{\min}$) adopted for hazard calculations.
- Total number of seismic sources, broken down by source type and by tectonic region type.
- Number of logic-tree files and number of source-model branches.

Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with geometry and parametrisation defined in OpenQuake source-model XML files and encoded in the logic tree.

*Coverage: TASK_FILE lines 19-36. Explicit directives at lines 29-30 ("State the total number of seismic sources in the model, broken down by source type and by tectonic region type. State the number of logic-tree files and source-model branches."). Framing text at lines 19-27 defines the overview scope (source types, geographic extent, $M_{\min}$). Lines 32-36 provide PSHA framework context.*

### SLOT 2: Source-Model Logic Tree Structure

Describe the source-model logic tree structure. The logic tree encodes epistemic uncertainty by defining alternative realisations of the SSM. Each branch set addresses a specific source of uncertainty (e.g., alternative source-model geometries, maximum-magnitude perturbations, or b-value perturbations), and branches within each set carry weights reflecting the relative credibility of each alternative.

The description must include:

- Each branch set with its uncertainty type.
- The branches within each set: IDs, perturbation values, and weights.

*Coverage: TASK_FILE lines 39-45. Explicit directive at lines 44-45 ("Describe the source-model logic tree structure. List the branch sets with their uncertainty type, the branches (IDs, perturbation values, weights)"). Framing at lines 39-43 describes the role of the logic tree.*

### SLOT 3: Earthquake Recurrence Parameters

Report the earthquake recurrence parameters for each source group. Recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source.

For each source group, report:

- MFD type.
- $a$-value range and $b$-value range.
- $M_{\min}$.
- $M_{\max}$ range.
- For source types without $a$/$b$ values (e.g., incrementalMFD), describe the rate specification method.

Present the results in a summary table.

*Coverage: TASK_FILE lines 48-56. Explicit directive at lines 53-56 ("For each source group, report the recurrence parameters: MFD type, a-value range, b-value range, Mmin, and Mmax range. For source types without a/b values ... describe the rate specification method. Present a summary table."). Note: detailed $M_{\max}$ uncertainty treatment is addressed separately in SLOT 7; this slot reports $M_{\max}$ range as part of the recurrence summary.*

### SLOT 4: Magnitude-Frequency Distribution Types

State the magnitude-frequency distribution (MFD) types present in the model. For each MFD type, describe briefly how earthquake rates are parameterised:

- truncGutenbergRichterMFD: $a$-value and $b$-value with $M_{\min}$/$M_{\max}$ bounds.
- incrementalMFD: discrete occurrence rates per magnitude bin; $a$/$b$ values not defined.
- arbitraryMFD / multiMFD: occurrence rates specified at arbitrary magnitude points.

State the magnitude-area scaling relationships used in the model.

*Coverage: TASK_FILE lines 58-62. Explicit directives at lines 58-61 ("State the magnitude-frequency distribution (MFD) types present in this model. For each MFD type, briefly describe how earthquake rates are parameterised") and line 62 ("State the magnitude-area scaling relationships used"). Both directives concern MFD-related parametrisation and are grouped here as tightly coupled items within the same task paragraph.*

### SLOT 5: Slip-Rate Data and Moment Balance

Activity rates for fault sources with available slip-rate data are derived from seismic-moment balance:

$$\dot{M}_0 = \mu\, A\, S$$

where $\mu$ is the shear modulus, $A$ the fault area, and $S$ the long-term slip rate.

Report:

- The number of sources with slip-rate data.
- The range of slip rates observed.

*Coverage: TASK_FILE lines 65-67. Explicit directive at lines 66-67 ("Report the number of sources with slip-rate data and the range of slip rates observed"). Framing at lines 65-66 provides the moment-balance equation context.*

### SLOT 6: Maximum Magnitude Characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency distribution for each source and is a critical parameter controlling the tail of the hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree branches where specified.

For each source group, describe briefly:

- Base $M_{\max}$ range.
- Uncertainty bounds (low/high).
- Derivation method.
- Logic-tree treatment of $M_{\max}$ uncertainty (maxMagGRRelative branches, perturbation values, weights).
- Any source groups where $M_{\max}$ is implicit from the MFD.

*Coverage: TASK_FILE lines 69-77. Explicit directive at lines 74-77 ("For each source group, describe briefly the maximum magnitude: base Mmax range, uncertainty bounds (low/high), derivation method, and the logic-tree treatment of Mmax uncertainty (maxMagGRRelative branches, perturbation values, weights). Note any source groups where Mmax is implicit from the MFD."). Framing at lines 69-72 establishes the role of $M_{\max}$ in the hazard curve.*

### SLOT 7: Seismogenic Depth Parameters

Seismogenic depth parameters define the vertical extent within which earthquake ruptures are generated. Upper and lower seismogenic depths bound the rupture zone; hypocentral depth distributions, where specified, control the depth placement of point-source ruptures.

For each source type or tectonic region, describe briefly:

- Upper seismogenic depth range.
- Lower seismogenic depth range.
- Hypocentral depth distribution where defined.

*Coverage: TASK_FILE lines 80-83. Explicit directive at line 83 ("For each source type or tectonic region, describe briefly the seismogenic depth parameters: upper depth range, lower depth range, and hypocentral depth distribution where defined"). Framing at lines 80-82 defines the role of depth parameters.*

### SLOT 8: Local Sources and Site Interrogation

Sources closer to the site have greater potential to contribute to ground-motion hazard, subject to their magnitude potential and recurrence rate. Interrogate the model regarding the sources nearest to the site.

Describe briefly:

- The tectonic regime to which the sources surrounding or including the site belong.
- Based on the nearest local sources, interpret what magnitude levels, depths, and tectonic regime would be reasonable for the most relevant seismic events in the immediate vicinity of the site.

*Coverage: TASK_FILE lines 85-86. Explicit directive at line 86 ("Interroga al modelo respecto de las fuentes mas cercanas al sitio ... A que regimen tectonico pertenecen las fuentes que rodean o incluyen al sitio? ... interpreta que niveles de magnitud, profundidad y regimen tectonico serian razonables para los eventos mas relevantes en el entorno inmediato del sitio" - translated to English per global constraint).*

### SLOT 9: Smoothed-Seismicity Nearest Point Sources

Where the source model includes spatially smoothed seismicity grids as alternative branches, the nearest point source from each grid provides a reference for the distributed seismicity contribution at the site location.

For each smoothed-seismicity branch, describe briefly the nearest point source to the site:

- Source ID.
- Coordinates.
- Distance to the site.
- MFD parameters.
- $M_{\max}$ range.
- Depth.
- Branch weight.

*Coverage: TASK_FILE lines 88-90. Explicit directive at lines 89-90 ("For each smoothed-seismicity branch, describe briefly the nearest point source to the site: source ID, coordinates, distance, MFD parameters, Mmax range, depth, and branch weight").*

## CONSTRAINTS

- The output document must be written entirely in professional English.
