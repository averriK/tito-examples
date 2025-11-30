# 5.0 GROUND MOTION MODELS

Ground motion models (GMM) are used in seismic hazard analysis to estimate the source-to-site attenuation of earthquake ground motions at PGA and at other spectral periods as a function of the earthquake magnitude, source-to-site distance, local site ground conditions, and other factors. The GMMs are typically empirically derived, with the calculated acceleration values usually assuming 5% of critical damping, as in this assessment. The sections below describe the how GMMs were evaluated and selected for this assessment.

## 5.1 GMMs used for CanadaSHM6

CanadaSHM6 considered the preliminary suite of 13 GMMs developed for NGA-East ([@Goulet2017a], [@Goulet2017b]). The goal of the NGA-East project was to create a ground motion characterization model for Central and Eastern North America (CENA) comprising a set of mutually exclusive and collectively exhaustive GMMs (that is, the individual GMMs do not overlap and together represent the full range of ground motions). The resulting preliminary suite of NGA-East GMMs comprised 13 different models defined for 25 ground-motion intensity measures with frequency-dependent weighting factors. Each model is weighted to reflect the joint distribution of median ground motion estimates at different magnitude-distance scenarios for a given frequency and their fit to observed ground-motion data. The preliminary 13 NGA-East GMMs have now been superseded, as noted in the addendum to PEER Report 2017-03 ([@Goulet2017a], [@Goulet2017b]).

CanadaSHM6 uses two suites of GMMs with the following weights ([@Kolaj2019]):

- The AA13 median and standard deviation ground motions from CanadaSHM5. Weighted 50%.
- The preliminary (superseded) 13 NGA-East median ground motions with the standard deviation model from CanadaSHM5 AA13 GMMs. Weighted 50%.

### 5.1.1 AA13 GMMs

The AA13 GMMs used in CanadaSHM5 ([@Atkinson2013]) represent several different approaches to model ground motion attenuation in eastern North America (ENA). There are five ENA models: [@Pezeshk2011], [@Atkinson2006], as revised in [@Atkinson2011], [@Atkinson2008], as revised in [@Atkinson2011], [@Silva2002] single-corner (variable stress) and double-corner (with saturation).

The AA13 GMMs use the moment magnitude and closest source-to-site rupture plane as inputs and are applicable to magnitudes ranging from Mw 4.8 to Mw 8.0, and for source-to-site distances of up to 600 km. Aleatory variability in the AA13 GMMs is represented by a standard deviation (sigma) model that attempts to capture the natural variability of hypothetical future events.

The standard deviation model developed with the AA13 GMMs consists of sigma values that vary based on spectral period and is lower than other standard deviation models (e.g., [@Boore2008], or NGA-East standard deviation models) to avoid any double-counting of aleatory variability and epistemic uncertainty.

### 5.1.2 NGA-East GMMs

The preliminary 13 NGA-East GMMs ([@Goulet2017a]) were developed for a reference hard-rock site condition with an average shear-wave velocity in the upper 30 m (i.e., VS30) of 3,000 m/s. The GMMs use the moment magnitude and the closest source-to-site rupture plane as inputs. The GMMs are applicable to magnitudes ranging from Mw 4 to Mw 8.2, and for source-to-site distances of up to 1,500 km. Variations in the expected ground motion are quantified and applied in the GMMs by use of a standard deviation (sigma) model, or the total ergodic standard deviation model, which includes between-event variability and single-station within-event variability. Each component of ground motion variability was analyzed and compared to ground motion variability in other regions, particularly the western United States (WUS). The final models derived for each component of ground motion variability are largely based on NGA-West2 relationships for shallow crustal earthquakes in active tectonic regions ([@Abrahamson2014]; [@Boore2014]; [@Campbell2014]; [@Chiou2014]), residuals analysis, and standard deviation models. The final GMMs are both magnitude-and period-dependent.

Since the limited CENA dataset was used to develop the NGA-East GMMs, standard deviation models from other regions, including the western USA and Japan, were used to inform the extrapolation of CENA standard deviations to large magnitudes and frequencies outside of the 1 Hz to 10 Hz frequency range. The standard deviation models published in NGA-East have high sigma values and lead to a large discrepancy between median and mean ground motions. As such, the NGA-East standard deviation models were not implemented with the median ground motions for CanadaSHM6 for this site-specific SHA.

## 5.2 GMMs used for this Site-Specific Assessment

For this assessment WSP has used the final suite of 17 GMMs developed for the Next Generation Attenuation for Central and Eastern North America (CENA) project (NGA-East, [@Goulet2018]) to calculate median ground motions along with the standard deviation model from [@Atkinson2013] (AA13). These 17 GMMs supersede the preliminary set of 13 NGA-East GMMs (described above) that were implemented in CanadaSHM6.

The 17 NGA-East GMMs reflect the most up-to-date published and vetted GMMs developed for stable continental regions (SCRs) in central and eastern North America. The NGA-East median ground motions are suitable to model earthquake ground motion attenuation for this assessment because they were developed with a robust process for a tectonic region (i.e., SCR) like that surrounding the Louvicourt TSF site. The final 17 NGA-East GMMs are used in this assessment in conjunction with the AA13 standard deviation model as implemented in CanadaSHM6.

## 5.3 Site Amplification Model

For southeastern Canada, CanadaSHM6 uses the site amplification factors applied in CanadaSHM5 with the AA13 GMMs and a site model that combines two existing amplification models for the preliminary 13 NGA East GMMs. The CanadaSHM6 site amplification models are described in detail by [@Kolaj2019].

Since the development of CanadaSHM6, the NGA-East GMMs have been used to update the US National Seismic Hazard Maps for the CENA Region ([@Petersen2020]). Recommendations for the ergodic site amplification model in the CENA were provided by [@Stewart2020] and [@Hashash2020] to produce the earthquake ground motion intensity measures for site conditions with a VS30 less than the 3,000 m/s reference hard-rock condition, as adopted for the NGA-East GMM development.

For this assessment we have applied equally weighted [@Stewart2020] and [@Hashash2020] site amplification models to adjust the site condition from the NGA-East reference hard-rock condition with a VS30 of 3,000 m/s to the site-specific VS30 condition of 1,853 m/s.
