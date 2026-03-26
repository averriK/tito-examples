# Structured Prompt: Seismotectonic Setting - Rampura Agucha Mine

## CONTEXT

Rampura Agucha Mine (RAM) tailings storage facility (TSF), owned and operated by Hindustan Zinc Limited (HZL), is located approximately 220 km from Jaipur in Rajasthan, India. RAM is the second-largest zinc mine in the world. The kb/ folder contains project information, including site coordinates. The scope of this chapter is the seismotectonic environment of the site and surrounding region.

## SLOTS

### SLOT 1: Regional seismic generation mechanisms

Identify the seismic generation mechanisms that control the seismic hazard of the region surrounding the Rampura Agucha Mine site. Classify which mechanism types are present in the region: Active Shallow Crust (ASC), Stable Continental Crust (SCC), Subduction Interface (SIF), and Subduction Intra-slab (SIS).

> Coverage: First question in TASK_FILE Preguntas section, which requests the controlling seismic generation mechanisms and explicit classification by type (ASC, SCC, SIF, SIS).

### SLOT 2: Site-specific seismogenic setting

Identify the seismic generation mechanisms of the sources closest to the project site. Determine the type of seismogenic region in which the site is located, acknowledging that multiple seismogenesis mechanisms may coexist across the continent but the site falls within a specific seismogenic domain.

> Coverage: Second question in TASK_FILE, which narrows focus from regional mechanisms (SLOT 1) to the specific seismogenic classification applicable to the site itself.

### SLOT 3: Notable historical seismic events

Identify the most relevant historical seismic events in the region. Present each event as a brief bullet entry including date, location, and magnitude. Use the reference file kb/events.csv (containing events with $M > 7.0$) as a starting point, and supplement with additional historical events not present in that catalog.

> Coverage: Third question in TASK_FILE, including the explicit instruction to consult kb/events.csv and to investigate beyond its contents. The requested output format (brief bullet list with date, location, magnitude) is preserved.

### SLOT 4: Active faults with neotectonic activity

Identify the known active faults in the region that exhibit neotectonic activity, defined as activity during the last 10,000 to 35,000 years following ANCOLD criteria for neotectonic classification.

> Coverage: Fourth question in TASK_FILE, which explicitly references ANCOLD criteria and the 10,000-35,000 year recency window for neotectonic activity.

### SLOT 5: Distance to nearest active fault

Determine the distance from the Rampura Agucha Mine project site to the nearest active fault.

> Coverage: Fifth question in TASK_FILE - a standalone spatial query about proximity to the closest active fault.

### SLOT 6: Slip rates, maximum magnitude, and distances of major active faults

For the most important active faults in the region, report the assigned slip rates, the assigned maximum magnitude ($M_{max}$) for each fault, and the distance of each fault from the project site.

> Coverage: Sixth and final question in TASK_FILE, which requests three specific parameters (slip rate, $M_{max}$, distance) for the most important active faults.

## CONSTRAINTS

- The output document must be written in professional English.
