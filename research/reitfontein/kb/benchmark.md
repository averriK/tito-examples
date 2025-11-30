# PSHA Models for South Deep Gold Mine Site

## Introduction [INCOMPLETE]



## SRC Model

Peak ground acceleration estimates for the South Deep Gold Mine site exhibit substantial variation across different studies. For the 475-year return period (10% probability of exceedance in 50 years), historical estimates range from 0.1 g to 0.55 g [@SRC2025]. 

The PSHA assessment by Seismology Research Centre (SRC) calculated a PGA of 0.33 g for this return period, representing a significant increase compared to the value of 0.15 g adopted in past analyses [@SRC2025]. For the 10,000-year return period, SRC estimated a PGA of 1.3 g, substantially exceeding the previously adopted value of 0.25 g [@SRC2025]. These calculations assume a Vs30 value of 600 m/s at the Doornpoort (New Facility) site [@SRC2025].


**Table 1.** PGA values (g) for different return periods according to three source models and weighted mean. Site conditions: $V_{s30} = 600$ m/s, $M_w \geq 5.0$ [@SRC2025].

| Return Period (years) | EZF Model | GEM Model | Smoothed Model | Weighted Mean |
|-----------------------|-----------|-----------|----------------|---------------|
| 475                   | 0.157     | 0.564     | 0.103          | 0.329         |
| 1,000                 | 0.236     | 0.799     | 0.154          | 0.498         |
| 2,000                 | 0.335     | 1.067     | 0.216          | 0.696         |
| 5,000                 | 0.516     | 1.501     | 0.325          | 1.028         |
| 10,000                | 0.696     | 1.892     | 0.432          | 1.328         |



The SRC study employed three seismic source models: the EZ-FRISK Africa model (developed by William Lettis & Associates, 2008), the GEM South Africa (ZAF) model (updated by Midzi et al., 2020 from the Council for Geoscience), and a smoothed seismicity model developed specifically for the site [@SRC2025]. The equally weighted mean of these three models produces the final PGA estimates.


## GSHA & GEM Models 

Global and regional seismic hazard assessments provide additional benchmarking context. The Global Seismic Hazard Assessment Program (GSHAP, 1992-1999) estimated PGA values of less than 0.01 g for the 475-year return period at the South Deep site [@SRC2025]. The Global Earthquake Model (GEM) 2023 global seismic hazard map, which collates national and regional PSHA models developed by various institutions, provides updated estimates for South Africa [@GEM2023web; @GEMZAF2023]. The GEM South Africa (ZAF) model was one of three earthquake recurrence models used in the SRC assessment, along with the EZ-FRISK Africa model and a smoothed seismicity model developed by SRC [@SRC2025]. The GEM Global Seismic Hazard Map (version 2023.1) represents the spatial distribution of PGA with 10% probability of exceedance in 50 years, calculated for reference rock conditions with $V_{s30}$ between 760 and 800 m/s [@GEM_GlobalMap]. For South Africa, the map shows PGA values ranging from 0.017 g to 0.149 g, with elevated hazard in gold mining regions [@GEM_GlobalMap]. 


## SRK Model [INCOMPLETE]


SRK ha preparado estudios de PSHA en la region, empleando diferentes modelos GMPE para regiones continentales estables SCC El detalle del modelo se puede ver en la seccion ##SRK Ground-Motion Intensity Model


Table A.1: Design Ground Motions in terms of peak ground accelerations PGA [cm/s2] for AEP = 1/475 [1/yr] and AEP = 1/9975 [1/yr]. Spectral ordinates were obtained assuming site conditions with Vs30 ranging from 180 to 1250 [m/s]. (p=mean)

|TR[yr]|poe[%]|180|270|360|560|760|1250|ID|
|---|---|---|---|---|---|---|---|---|
|475|10.0|58|58|57|55|53|53|gem|
|475|10.0|112|83|71|59|52|52|shm6|
|475|10.0|92|94|92|88|84|84|usgs|
|9,975|0.5|333|339|340|336|332|333|gem|
|9,975|0.5|348|299|271|232|208|222|shm6|
|9,975|0.5|358|377|381|386|384|386|usgs|

