## Reglas

DOCUMENT IN ENGLISH (PROFESSIONAL ENGLISH)

## Contexto

En la carpeta `kb/` existe informacion del modelo de fuentes de India y de las fuentes locales del sitio Rampura Agucha. En particular, `kb/source_model.md`, `kb/site_sources.md`, `kb/site_sources_data.md` e `kb/ind-report.pdf.md` contienen informacion del modelo regional IND y de la representacion local del sitio dentro de ese modelo.

Rampura-Agucha Mine (RAM) tailings storage facility (TSF) is owned and operated by Hindustan Zinc Limited (HZL) and is located approximately 220 km from Jaipur, in Rajasthan, India. RAM is the second-largest zinc mine in the world.

El propósito de este capítulo es describir el modelo de fuentes sísmicas adoptado para la región y, además, interrogar ese mismo modelo en el punto del sitio. El modelo SSM tiene cientos de fuentes y necesita una descripción global: arquitectura, tipos de fuente, tipos de región tectónica, árbol lógico, recurrencia, profundidades, máximas magnitudes y procedencia. Pero además, el sitio queda contenido en una o dos fuentes sísmicas que llamaremos locales; interesa entender qué dice el propio modelo sobre esas fuentes locales, porque son las que producirían los sismos máximos creíbles más próximos al sitio.


# Seismic Source Model (SSM)




The seismic source model (SSM) defines the spatial distribution, geometry, and earthquake
occurrence rates of all seismogenic sources considered capable of contributing to the
ground-motion hazard at the site. The SSM is the principal input to the probabilistic
seismic hazard analysis (PSHA) and is implemented in OpenQuake through a source-model
logic tree (ssmLT) that captures epistemic uncertainty by assigning weights to alternative
model configurations. This section provides an overview of the SSM structure: the source
types included, the geographic extent of the model domain, and the minimum earthquake
magnitude ($M_{\min}$) adopted for hazard calculations. The parameterisation of individual
sources is described in the following sections.

State the total number of seismic sources in the model, broken down by
source type and by tectonic region type. State the number of logic-tree files and source-model branches. 

Seismic-source characterisation follows the classical PSHA framework outlined by
Cornell [-@Cornell1968] and formalised under SSHAC guidelines [-@SSHAC1997]. Sources
are delineated from geologic, geophysical, and seismological evidence, with their
geometry and parametrisation defined in OpenQuake source-model XML files and encoded
in the logic tree.


The source-model logic tree encodes epistemic uncertainty by defining alternative
realisations of the SSM. Each branch set addresses a specific source of uncertainty
(e.g., alternative source-model geometries, maximum-magnitude perturbations, or
b-value perturbations), and the branches within each set are assigned weights reflecting
the relative credibility of each alternative.
Describe the source-model logic tree structure. List the branch sets with their uncertainty type, the branches
(IDs, perturbation values, weights)


The earthquake recurrence parameters quantify the expected rate and size distribution
of future earthquakes on each seismic source. Recurrence is described by a
magnitude-frequency distribution (MFD) whose type and parameters are specified per
source in the model.

For each source group, report the recurrence parameters: MFD type,
a-value range, b-value range, Mmin, and Mmax range. For source types without a/b
values (e.g., incrementalMFD), describe the rate specification method. Present a
summary table.

State the magnitude-frequency distribution (MFD) types present in this model. For each MFD type, briefly describe briefly how earthquake rates are parameterised in this SRC
- truncGutenbergRichterMFD: a-value and b-value with Mmin/Mmax bounds.
- incrementalMFD: discrete occurrence rates per magnitude bin; a/b values not defined.
- arbitraryMFD / multiMFD: occurrence rates specified at arbitrary magnitude points.
State the magnitude-area scaling relationships used 

Activity rates for fault sources with available slip-rate data are derived from
seismic-moment balance, $\dot{M}_0 = \mu\, A\, S$, where $\mu$ is the shear modulus,
$A$ the fault area, and $S$ the long-term slip rate. Report the number of sources with slip-rate data and the range of slip
rates observed

Maximum magnitude ($M_{\max}$) defines the upper bound of the magnitude-frequency
distribution for each source and is a critical parameter controlling the tail of the
hazard curve. Epistemic uncertainty in $M_{\max}$ is captured through logic-tree
branches where specified.

For each source group, describe briefly  the maximum magnitude: base Mmax range,
uncertainty bounds (low/high), derivation method, and the logic-tree treatment of
Mmax uncertainty (maxMagGRRelative branches, perturbation values, weights). Note any
source groups where Mmax is implicit from the MFD.]


Seismogenic depth parameters define the vertical extent within which earthquake
ruptures are generated. Upper and lower seismogenic depths bound the rupture zone;
hypocentral depth distributions, where specified, control the depth placement of
point-source ruptures.  For each source type or tectonic region, describe briefly  the seismogenic depth parameters: upper depth range, lower depth range, and hypocentral depth distribution where defined.

Sources closer to the site have greater potential to contribute to ground-motion hazard,
subject to their magnitude potential and recurrence rate.  Interroga al modelo respecto de las fuentes más cercanas al sitio. Describe resumidamente ¿A qué régimen tectónico pertenecen las fuentes que rodean o incluyen al sitio? A partir de las fuentes locales más cercanas, interpreta qué niveles de magnitud, profundidad y régimen tectónico serían razonables para los eventos más relevantes en el entorno inmediato del sitio.

Where the source model includes spatially smoothed seismicity grids as alternative
branches, the nearest point source from each grid provides a reference for the
distributed seismicity contribution at the site location. For each smoothed-seismicity branch, describe briefly  the nearest point source to the site: source ID, coordinates, distance, MFD parameters, Mmax range, depth, and branch weight.
