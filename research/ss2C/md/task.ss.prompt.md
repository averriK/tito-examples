# Structured Prompt: Seismotectonic Environment and Active Faults - Longonjo Project

## CONTEXT

The kb/ folder contains information on the seismotectonic environment of the Longonjo project and a document describing regional faults. The purpose of this chapter is to describe the seismotectonic setting of the site and region and to investigate potential active faults within a 500 km radius. Site coordinates: latitude = $-12.939727$ S, longitude = $+15.240812$ E.


## SLOTS

### SLOT 1: Earthquake generation mechanisms controlling regional seismic hazard

Identify the earthquake generation mechanisms that control the seismic hazard of the region surrounding the Longonjo project site. Determine which mechanism types - Active Shallow Crust (ASC), Stable Continental Crust (SCC), Subduction Interface (SIF), and Subduction Intra-slab (SIS) - control seismicity in this region.


### SLOT 2: Seismogenic source mechanisms nearest to the site

Identify the mechanisms associated with the seismogenic sources closest to the project site. Although multiple seismogenesis mechanisms may exist across the continent, determine the specific type of seismogenic region in which the site is located.


### SLOT 3: Relevant historical seismic events

Identify the most relevant historical seismic events in the region and detail each by date, location, and magnitude in a brief bullet list. Use kb/events.csv (which contains events with magnitude greater than 6.5) as a starting reference, but also investigate additional historical events that may not appear in that file.


### SLOT 4: Known active faults with neotectonic activity

Identify the known active faults in the region that exhibit neotectonic activity, defined as activity during the last 10,000 to 35,000 years according to the ANCOLD criterion.


### SLOT 5: Distance from the project site to the nearest active fault

Determine the distance from the Longonjo project site to the nearest active fault.


### SLOT 6: Slip rates, maximum magnitude, and distances for major active faults

For the most important active faults, report the assigned slip rates and the assigned maximum magnitude ($M_{\mathrm{max}}$). Include the distance of each fault from the project site.


## CONSTRAINTS

- The entire output document must be written in professional English.

