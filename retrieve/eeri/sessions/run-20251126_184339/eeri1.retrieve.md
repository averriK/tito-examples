# Seismic Assessment of Buried Prestressed Concrete Reservoir using Nonlinear Soil-Structure Interaction Analysis

A. Nisar, N. Doumbalski, E. Mantchev, and W. Yen

## Abstract

This paper presents seismic assessment of a 32 million gallon buried prestressed concrete reservoir owned and operated by the Seattle Public Utilities (SPU). The reservoir was designed for Seismic Zone 3 provisions of the Uniform Building Code. The design earthquake ground motions and detailing requirements in the current codes are significantly higher and more stringent than those in the 1980s. The reservoir is located in an area of high seismic hazard because of its proximity to the Cascadia Subduction Zone (CSZ) and the Seattle Fault Zone (SFZ). The reservoir sustained minor to moderate damage in the 2001 Nisqually earthquake with an increase in observed leakage following the earthquake. Potential damage to the reservoir in a major earthquake is a significant concern for both post-earthquake water needs and the potential risk of flooding of the surrounding residential developments. Buried reservoirs have a highly complex soil-structure interaction (SSI) response that cannot be accurately captured using simplified procedures. A nonlinear SSI analysis was performed to assess the risk of damage to the reservoir. The assessment was performed for multiple earthquake cases to make prudent risk versus retrofit cost decisions.

## Introduction

The 32 million gallon (MG) Eastside reservoir is located in an area of high seismic hazard because of its proximity to the Cascadia Subduction Zone (CSZ) and the Seattle Fault Zone (SFZ) as shown in Figure 1. There is evidence of numerous large-magnitude CSZ earthquakes with average recurrence interval between 300 to 500 years with the most recent earthquake on January 26, 1700 (323 years ago). The estimated probability of a major (M9) earthquake on CSZ is 7 to 12 percent in the next 50 years and 16 to 22 percent of a smaller M8 to M9 earthquake.

The reservoir site is located in open space in a 5.5 acre park with the surrounding neighborhood consisting of dense single-family housing developments. The reservoir sustained minor to moderate damage in the 2001 Nisqually earthquake with an increase in the amount of observed leakage increased following the earthquake. Potential damage to the reservoir in a major earthquake is a significant concern for both post-earthquake water needs and the potential risk of flooding of the surrounding residential developments.

## Reservoir Description

The Eastside reservoir, constructed in 1986, is a fully buried cast-in-place prestressed circular concrete tank with an outside diameter of 352 feet (Figure 2a). It was designed for Seismic Zone 3 provisions of the 1982 Uniform Building Code [@UBC1982]. The reservoir has a 10-inch thick roof slab supported by the exterior reservoir wall and interior concrete columns (Figure 2b). The tapered exterior wall is prestressed in the hoop direction by cables and in the vertical direction by prestressing rods. Seismic cables (Figure 3) are the only positive connection between the wall and its foundation, allowing movement in the radial direction but restraint in the tangential direction. The reservoir floor slab is cone-shaped and provides an additional 20 feet of water depth near the center of the structure. The maximum fill-height of the reservoir along the perimeter wall is 33.5 feet.

The roof-to-wall connection is through shear keys (Figure 4). Neoprene pads between the roof slab and the wall allow movement in the radial direction. A shift of as much as 1.5 inches in the shear keys between the wall and the roof was observed at multiple locations. This movement could have been a result of the 2001 Nisqually earthquake but it cannot be confirmed.

## Seismic Hazard

Geotechnical investigations show the site to be underlain by medium dense to very dense fill over glacial till. The glacial till is likely underlain by sandstone and siltstone but the borings do not show a consistent pattern throughout the site. The geophysical investigations show site $V_{s30}$ to range between 1,351 ft/s to 1,157 ft/s. The reservoir site is underlain by the Seattle Basin with the depth to basement rock over 7,000 meters. Ground motions considering basin effects and measured $V_{s30}$ were computed for eight earthquake cases including M9 and M7 on CSZ, M7 on SFZ and probabilistic ground motions for 72, 100, 475, 975, and 2,475-year return periods. For nonlinear SSI analysis acceleration time histories were selected by developing the conditional mean spectrum as described in Baker and Cornell [@BakerCornell2006] and Baker [@Baker2011].

## Soil-Structure Interaction Analysis

SSI analysis was performed using LS-Dyna with the schematic of the model shown in Figure 5.

The reservoir wall, base slab, and roof slab was modeled with shell elements and interior columns with beam elements. Elastic material model for concrete was used because no significant material nonlinearity is expected due to the existing prestressing. Contact elements to allow for uncoupled behavior between the roof and the wall and between the wall and the foundations were used. Mass of the water inside the reservoir was modeled as impulsive and convective components per ACI 350.3-06 [@ACI3503-06]. The impulsive mass was rigidly attached to the reservoir wall. Force associated with the convective mass was applied as a static load in the direction of maximum response; a reasonable assumption because of the very long calculated sloshing period.

Soil around and below the reservoir was modeled with solid elements. Separate hysteretic soil material models were used to model till, fill and the drainage material around the reservoir. Input parameters included mass density; bulk modulus at the reference pressure; and cut-off pressure. Custom curves defining shear stress versus shear strain were defined for each material. The nonlinear material model was validated using simple finite element models of a retaining wall and comparing the calculated passive soil pressure with theoretical values. The interface between the soil and the structure was modeled with interface elements that do not transfer tension and allow separation of soil from the structure during intense shaking.

To avoid reflection of pressure waves from the perimeter of the finite element model, nonreflecting boundary condition was specified at the model perimeter. Earthquake ground motion time histories selected for the project are applied at the base of the model and propagated through vertical soil columns along the edges of the model. The vertical soil column along the edges was modeled with its size much larger than the reservoir diameter. Nodal constraints were applied at the nodes of the soil mesh boundary to enable 1-D like soil behavior to represent free-field motion. The analysis includes radiation damping in the soil.

## Assessment Results

The results of the analysis showed a generally good performance of the reservoirs with three significant vulnerabilities. For 975-year return period and higher ground motions hoop stress in the upper 3 to 4 feet of the reservoir wall exceed capacity and there is a potential for several inches of sliding at the wall base (Figure 6). The assessment also showed potential risk of cracking the shear key corners due to brittle reinforcing detail. Although costly to repair, the risk of major damage and loss of water for this vulnerability is low.

## Conclusions

The complex soil-structure interaction (SSI) response of buried reservoir cannot be accurately captured using traditional analysis. There are many factors that can only be modeled through an SSI analysis including nonlinear response of the soil, poorly compacted soil close to the reservoir wall, variation of passive soil along the wall height, radiation damping, and radial movement of roof and base slab. The SSI analysis for a range of ground motions provided a complete risk picture. Additional simplified analyses were performed to study the impact of analysis assumptions and to evaluate operational changes such as reduction in water height or the removal of soil cover from the roof on the identified vulnerabilities.

## Acknowledgments

The authors thank Professor S. Kramer; Drs. F. Naeim, M. Mehrain, M. Greenfield, and J. Donahue; Mr. D. Lee (formerly EBMUD) for their technical contribution. The study was initiated and substantially completed under Mr. W. Heubach. Mr. W. Wells of SPU provided a detailed review and final approval of the study.
