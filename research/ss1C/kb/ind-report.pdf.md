# PSHA input model documentation for

# India and surroundings (IND)

### GEM Hazard Team

### Version history

Table 1 summarises version history for the IND input model, named according to the versioning system described here, and indicating which version was used in each of the global maps produced since 2018. Refer to the GEM Products Page for information on which model versions are available for various use cases. The changelog describes the changes between consecutive versions and are additive for all versions with the same model year.

Table 1 – Version history for the IND input model.

### Version

### 2018.1

### 2019.1

##### 2022.1 2023.1 Changelog

v2012.0.0 X First version of the model implemented in OpenQuake. v2012.1.0 X X Corrected to use GMPE Kanno et al. (2006) for shallow earthquakes instead of the version for deep earthquakes. On layer 3 the "subduction interface" TRT is replaced with "subduction intraslab". v2012.2.0 X gmmLT.xml updated with more recent GMPEs

The following text describes v2012.2.0.

### Authors: N. Ackerley, K.K.S. Thingbaijam, S.K. Nath

### Summary

Coverage of the Indian subcontinent is with the hazard model developed by Nath and Thingbaijam (2012). This model covers India, Bangladesh, Bhutan and Nepal. The model has been updated and translated from its original format into the OpenQuake (OQ) engine in collaboration with Natural Resources Canada. Additional information, material and documentation about the implementation of the model can be found at: https://github.com/nackerley/indian-subcontinent-psha

### Tectonic overview

The Indian subcontinent moves northward with respect to Eurasia and is colliding with the southern Asian margin at 35-45 mm/yr; this collision has contributed greatly to the uplift of the great mountain ranges of central and eastern Asia, including the Himalaya, the Tien Shan, the Pamir, and the Tibetan plateau. The Indian subcontinent is much stronger than the Asian continental crust with which it collides, though, so most of the deformation and seismicity that results from the plate collision is located in and north of the Himalaya outside of India. Exceptions include in northwest and northeast India where the Himalaya are within the national borders, and the Shillong region of eastern India, where some component of the plate convergence is accommodated on intraplate faults. The faults in the Himalayan belt take up at least half of the total plate convergence and represent the greatest source of seismic hazard to India; earthquakes on the Himalayan thrusts may be large enough that those in Nepal, Bhutan and Pakistan may still produce dangerous seismic shaking in densely-populated northern India.

Nonetheless, the strong Indian crust is capable of transmitting compressive stresses over great distances, and large, damaging earthquakes have occurred well within the Indian borders as a result. A prime example of this is the 2001 Mw 7.6 Bhuj earthquake in Gujarat, which killed over 2000 people (Bodin and Horton, 2004, Bulletin of the Seismological Society of America)

### Basic Datasets

See Nath and Thingbaijam (2012) for a description of the datasets used for developing the hazard model.

### Hazard Model

### 4.1

### Seismic Source Characterisation

Nath and Thingbaijam (2012) proposed three source models: a single set of areal seismogenic source zones, and two smoothed-gridded point source models. Epistemic uncertainty is considered through alternative values of b and Mmax in each source zone.

### 4.2

### Ground Motion Characterisation

A wide range of tectonic regions are considered, and epistemic uncertainty is accounted

### for by using multiple GMPEs per tectonic region; see Table ??

### subduction interface megathrust

### Weight

AtkinsonMacias2009NSHMP2014 0.25 ZhaoEtAl2006SInter 0.25 Kanno2006Shallow 0.25 AtkinsonBoore2003SInter 0.25

### subduction interface

### Weight

Kanno2006Shallow 0.333 ZhaoEtAl2006SInter 0.333 AtkinsonBoore2003SInter 0.334

### active shallow crust normal

### Weight

BooreEtAl2014 0.25 Kanno2006Shallow 0.25 AkkarEtAlRjb2014 0.25 CampbellBozorgnia2014 0.25

### stable shallow crust

### Weight

RaghukanthIyengar2007 0.25 Campbell2003MwNSHMP2008 0.25 ToroEtAl2002SHARE 0.25 AtkinsonBoore2006 0.25

### intraplate margin upper

### Weight

SharmaEtAl2009 0.25 ToroEtAl2002SHARE 0.25 AtkinsonBoore2006 0.25 NathEtAl2012Upper 0.25

### subduction intraslab

### Weight

Gupta2010SSlab 0.25 AbrahamsonEtAl2015SSlab 0.25 AtkinsonBoore2003SSlabCascadia 0.25 ZhaoEtAl2006SSlab 0.25

### intraplate margin lower

### Weight

SharmaEtAl2009 0.25 ToroEtAl2002SHARE 0.25 NathEtAl2012Lower 0.25 AtkinsonBoore2006 0.25

### active shallow crust strike-slip reverse

### Weight

CampbellBozorgnia2014 0.2 AkkarEtAlRjb2014 0.2 Kanno2006Shallow 0.2 SharmaEtAl2009 0.2 BooreEtAl2014 0.2

### subduction intraslab Himalayas

### Weight

AtkinsonBoore2003SSlabJapan 0.25 AbrahamsonEtAl2015SSlab 0.25 ZhaoEtAl2006SSlab 0.25 LinLee2008SSlab 0.25

### Table 2 – GMPEs used in the IND model.

### Results

Hazard curves were computed with the OQ engine for the following:

- Intensity measure types (IMTs): peak ground acceleration (PGA) and spectral accel-
eration (SA) at 0.2s, 0.3s, 0.6s, 1.0s, and 2s

- reference site conditions with shear wave velocity in the upper 30 meters (Vs30) of
760-800 m/s, as well as for Vs30 derived from a topography proxy (Allen and Wald, 2009)

Hazard maps were generated for each reference site condition-IMT pair for 10% and 2% probabilities of exceedance (POEs) in 50 yrs. Additionally, disaggregation by magnitude, distance, and epsilon was computed for the following cities: Dhaka, Kathmandu, Colombo, New Delhi and Thimphu. The results were produced as csv ﬁles and bar plots for each of the following combinations:

- hazard levels for 10% and 2% POE in 50 yrs
- PGA and SA at 0.2s, 0.3s, 0.6s, and 1.0s
- Vs30=800 m/s
All calculations used a ground motion sigma truncation of 5. Results were computed for sites with 6 km spacing

Visit the GEM Interactive Viewer to explore the Global Seismic Hazard Map values (PGA for Vs30=800 m/s, 10% poe in 50 years). For a comprehensive set of hazard and risk results, see the GEM Products Page.

### References

Allen, T. I., and Wald, D. J., 2009, On the use of high-resolution topographic data as a proxy for seismic site conditions V s30, Bulletin of the Seismological Society of America, 99, no.

### 2A, 935-943

Nath, S. K. and Thingbaijam, K. K. S. (2012). Probabilistic seismic hazard assessment of India. Seismological Research Letters, 83(1):135–149. Last processed: Wednesday 24th September, 2025 @ 09:26 www.globalquakemodel.org If you have any questions please contact the GEM Foundation Hazard Team at: hazard@globalquakemodel.org
