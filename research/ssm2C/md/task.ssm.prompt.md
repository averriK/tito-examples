## CONTEXT

The knowledge base (`kb/`) contains information on the Seismic Source Model (SSM) used in the PSHA for the Longonjo project, Angola, and on the local sources most relevant to the site. Specifically, `kb/source_model.md` describes the SSM at the regional scale, while `kb/site_sources.md` and `kb/site_sources_data.md` show how the site is represented within the model and which sources are nearest.

The purpose of this chapter is to describe the SSM adopted for the project and the epistemic uncertainty model applied to the different source types and their parameters. The SSM contains hundreds of thousands of sources and requires a global description covering architecture, source types, tectonic region types, logic tree, recurrence, depths, maximum magnitudes, and provenance. In addition, the site lies within one or two seismic sources referred to here as local sources; the chapter should convey what the model indicates about these local sources, as they would produce the nearest maximum credible earthquakes.

## SLOTS

### SLOT 1: SSM Overview and Source Inventory

The seismic source model defines the spatial distribution, geometry, and earthquake occurrence rates of all seismogenic sources considered capable of contributing to ground-motion hazard at the site. It is the principal input to the PSHA and is implemented in OpenQuake through a source-model logic tree (ssmLT) that captures epistemic uncertainty.

Provide an overview of the SSM structure: source types included, geographic extent of the model domain, and minimum earthquake magnitude ($M_{\min}$) adopted for hazard calculations. State the total number of seismic sources in the model, broken down by source type and by tectonic region type. State the number of logic-tree files and source-model branches.

Seismic-source characterisation follows the classical PSHA framework outlined by Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources are delineated from geologic, geophysical, and seismological evidence, with their geometry and parametrisation defined in OpenQuake source-model XML files and encoded in the logic tree.

> **Coverage**: TASK_FILE lines 17-34. Directives at lines 27-28. Framing paragraphs provide SSM definition, PSHA context, and SSHAC framework reference.

### SLOT 2: Source-Model Logic Tree Structure

The source-model logic tree encodes epistemic uncertainty by defining alternative realisations of the SSM. Each branch set addresses a specific source of uncertainty (e.g., alternative source-model geometries, maximum-magnitude perturbations, or b-value perturbations), and the branches within each set are assigned weights reflecting the relative credibility of each alternative.

Describe the source-model logic tree structure. List the branch sets with their uncertainty type, the branches (IDs, perturbation values, weights).

> **Coverage**: TASK_FILE lines 37-43. Directive at lines 42-43.

### SLOT 3: Earthquake Recurrence Parameters by Source Group

The earthquake recurrence parameters quantify the expected rate and size distribution of future earthquakes on each seismic source. Recurrence is described by a magnitude-frequency distribution (MFD) whose type and parameters are specified per source in the model.

For each source group, report the recurrence parameters: MFD type, a-value range, b-value range, $M_{\min}$, and $M_{\max}$ range. For source types without a/b values (e.g., incrementalMFD), describe the rate specification method. Present a summary table.

> **Coverage**: TASK_FILE lines 46-54. Directive at lines 51-54.

### SLOT 4: MFD Types and Rate Parameterisation

State the magnitude-frequency distribution (MFD) types present in the model. For each MFD type, briefly describe how earthquake rates are parameterised:

- truncGutenbergRichterMFD: a-value and b-value with $M_{\min}$/$M_{\max}$ bounds.
- incrementalMFD: discrete occurrence rates per magnitude bin; a/b values not defined.
- arbitraryMFD / multiMFD: occurrence rates specified at arbitrary magnitude points.

> **Coverage**: TASK_FILE lines 56-59. Enumeration of MFD types provided directly in the task.

### SLOT 5: Magnitude-Area Scaling Relationships

State the magnitude-area scaling relationships used in the source model.

> **Coverage**: TASK_FILE line 60. Single directive.

### SLOT 6: Slip-Rate Data and Moment-Balance Activity Rates

Activity rates for fault sources with available slip-rate data are derived from seismic-moment balance, $\dot{M}_0 = \mu\, A\, S$, where $\mu$ is the shear modulus, $A$ the fault area, and $S$ the long-term slip rate.

Report the number of sources with slip-rate data and the range of slip rates observed.

> **Coverage**: TASK_FILE lines 62-65. Directive at lines 64-65.

### SLOT 7: Maximum Magnitude Characterisation

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency distribution for each source and is a critical parameter controlling the tail of the hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree branches where specified.

For each source group, describe the maximum magnitude: base $M_{\max}$ range, uncertainty bounds (low/high), derivation method, and the logic-tree treatment of $M_{\max}$ uncertainty (maxMagGRRelative branches, perturbation values, weights). Note any source groups where $M_{\max}$ is implicit from the MFD.

> **Coverage**: TASK_FILE lines 67-75. Directive at lines 72-75.

### SLOT 8: Seismogenic Depth Parameters

Seismogenic depth parameters define the vertical extent within which earthquake ruptures are generated. Upper and lower seismogenic depths bound the rupture zone; hypocentral depth distributions, where specified, control the depth placement of point-source ruptures.

For each source type or tectonic region, describe the seismogenic depth parameters: upper depth range, lower depth range, and hypocentral depth distribution where defined.

> **Coverage**: TASK_FILE lines 78-81. Directive at line 81.

### SLOT 9: Local Sources and Site Tectonic Context

Sources closer to the site have greater potential to contribute to ground-motion hazard, subject to their magnitude potential and recurrence rate.

Identify the sources nearest to or containing the site. Describe the tectonic regime of the sources that surround or contain the site. From the nearest local sources, interpret what magnitude levels, depth, and tectonic regime would be reasonable for the most relevant events in the immediate vicinity of the site.

> **Coverage**: TASK_FILE lines 83-84. Directive translated from Spanish original at line 84.

### SLOT 10: Nearest Smoothed-Seismicity Point Sources

Where the source model includes spatially smoothed seismicity grids as alternative branches, the nearest point source from each grid provides a reference for the distributed seismicity contribution at the site location.

For each smoothed-seismicity branch, describe the nearest point source to the site: source ID, coordinates, distance, MFD parameters, $M_{\max}$ range, depth, and branch weight.

> **Coverage**: TASK_FILE lines 86-88. Directive at line 88.

## CONSTRAINTS

- The entire output must be written in professional English.

> **Coverage**: TASK_FILE line 4 ("DOCUMENT IN ENGLISH (PROFESSIONAL ENGLISH)").
