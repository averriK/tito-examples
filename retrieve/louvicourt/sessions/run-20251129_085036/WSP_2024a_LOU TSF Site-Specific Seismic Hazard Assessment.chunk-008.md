# 8.0 EARTHQUAKE ACCELERATION TIME HISTORY DEVELOPMENT

WSP developed two suites of eight, two-horizontal-component earthquake acceleration time histories (EATHs) to support advanced geotechnical stability analyses of the Louvicourt TSF. Earthquake ground motions were selected and amplitude-scaled to represent the mean UHS for the 1/10,000 AEP (i.e., the target spectrum) for the site seismic ground conditions of VS30 = 1,853 m/s. Various secondary intensity measures (IMs) of the scaled ground motions were also considered in the final selection of input ground motions.

The Louvicourt TSF contains embankments of differing height and stiffness, and, therefore, varying fundamental periods. WSP was provided with two fundamental period values; one shorter period (TS) in the range 0.25 s to 0.37 s, and one longer period (TL) of approximately 1.15 s. A suite of eight, two-horizontal-component EATHs has been developed for each of the short and long fundamental periods.

Each suite of EATHs was selected using the following approach:

1. The 1/10,000 AEP hazard disaggregation results (Figure 17, Table 6) were reviewed, and a representative set of causal parameters (i.e., earthquake magnitude and rupture distance) selected.

2. Target secondary IMs consistent with the 1/10,000 AEP hazard were estimated using an earthquake scenario based on the input parameters listed below. The causal parameters (magnitude and rupture distance) are as highlighted in Figure 17 and Table 6. The other input parameters were assumed based on our judgement of reasonable values for earthquakes occuring in stable continental regions such as southeastern Canada.

   - Magnitude (Mw) = 7.3
   - Rupture distance (rrup) = 170 km
   - Hypocentral depth (zhypo) = 20 km
   - Depth to top of rupture (ztor) = 10 km
   - Rupture plane dip (δ) = 90°

   The secondary IMs considered were cumulative absolute velocity (CAV), Arias intensity (AI); and the 5% to 75% AI and 5% to 95% AI significant durations (D5-75 and D5-95, respectively). These secondary IMs are known to influence earthquake geotechnical engineering behaviour. Target secondary IMs were conditioned to the target spectrum at the two fundamental periods identified.

3. A catalogue of candidate ground motion records with generally similar causal parameters was developed from the PEER NGA-West2 ([@Ancheta2014]) and NGA-East databases ([@Goulet2021]).

4. Candidate ground motions were amplitude-scaled to be in general agreement with the target spectrum. A suite of eight ground motions was selected for each fundamental period, with a focus on the fit of the horizontal geometric mean response with the horizontal target spectrum across each of the period ranges of interest.

5. The secondary IMs of each of the selected, scaled horizontal ground motion records were compared with the estimated conditional IM values.

6. The selected suite of ground motions was accepted once the geometric mean of the horizontal components agreed with the target spectrum within the period range of interest and the empirical IMs compared reasonably well with the conditional IM values.

## 8.1 Ground Motion Selection Criteria

Ground motion selection criteria used in EATH development are presented in this section.

- **Target spectrum:** The mean UHS for the 1/10,000 AEP.

- **Conditioning period, T*:** For the short fundamental period, TS* was taken as 0.31 s (i.e., the centre of the range 0.25 s to 0.37 s). For the long fundamental period, TL* was taken as 1.15 s.

- **Period range of interest:** For the short fundamental period, a period range of interest of 0.062 s to 0.62 s (i.e., 0.2TS* to 2.0TS*) for scaling of candidate ground motions. For the longer fundamental period, a period range of interest of 0.23 s to 2.3 s (i.e., 0.2TL* to 2.0TL*) was adopted for scaling of candidate ground motions.

- **Causal parameters:** The magnitude and distance used for motion selection and estimation of IMs were selected based on the disaggregation results presented in Section 7.1.3. Figure 17 shows that the largest contribution to the 1/10,000 AEP seismic hazard at the Louvicourt TSF site is from earthquakes with magnitudes of about Mw 6.8 to Mw 7.5 and source-to-site distances of about 100 to 200 km, for both the shorter spectral periods (e.g., 0.2 s) and longer spectral periods (e.g., 1.0 s). Table 6 shows that mean, median, and mode values for the magnitude and distance generally agree at the shorter and longer spectral periods as well. Based on these results, ground motions were selected based on the modal disaggregation scenario of Mw 7.3 and 170 km source-to-site distance.

- **Secondary IMs:**

  - Median and lognormal standard deviation (σ) of the secondary IMs were estimated for the causal parameters listed above using the ground motions models listed in Table 8 and Table 9.

  - AI and CAV were conditioned to the 1/10,000 AEP hazard at each of TS* and TL* following the approach described by [@Baker2021]. Conditioning involves the use of epsilon (ε), which is the number of standard deviations for the spectral acceleration at T* to be equal to the hazard level. The ε was estimated to be 1.5 for both the short and long fundamental periods, based on the 1/10,000 AEP hazard disaggregations (Table 6).

  - The shaking duration IMs of D5-75 and D5-95 were not conditioned for each of the TS* and TL* because they are period-independent IMs.

  - Table 8 lists the conditional median values of AI and CAV. The unconditional median values of D5-75 and D5-95 are listed in Table 9. Figure 20 and Figure 21 show the distributions of all secondary IMs.

**Table 8: Ground Motion and Conditional Correlation Models of AI and CAV for Time History Selection.**

| Intensity Measure | Ground Motion Model | Conditional Correlation Model | Conditional Median Value | |
| | | | TS* (0.31 s) | TL* (1.15 s) |
|-------------------|---------------------|-------------------------------|-------------------|-------------------|
| SA (T*) | See Section 5.2 | Not Applicable | 0.296 (ε = 1.5) | 0.122 (ε = 1.5) |
| Arias Intensity, AI | [@Farhadi2020] | [@Bradley2015] | 0.098 (m/s) | 0.073 (m/s) |
| Cumulative Absolute Velocity, CAV | [@Farhadi2020] | [@Bradley2012] | 5.46 (m/s) | 5.10 (m/s) |

**Table 9: Ground Motion Models of D5-75 and D5-95 for Time History Selection.**

| Intensity Measure | Ground Motion Model | Median Value (Period-Independent) |
|-------------------|---------------------|-----------------------------------|
| Significant Duration, D5-75 | [@Bommer2009] | 5.66 (s) |
| Significant Duration, D5-95 | [@Bommer2009] | 10.50 (s) |

## 8.2 Candidate Ground Motion Records

The PEER NGA-West2 database was used to create a catalogue of prospective ground motions ranging in magnitude from Mw 6.0 to Mw 7.8 and source-to-site distance from 0 to 200 km for each period range of interest, consistent with the disaggregation results. The PEER NGA-East database was also consulted but lacked ground motions records with magnitudes greater than Mw 5.85. Relatively loose bounds were used for earthquake magnitude and distance because the ground motion selection process explicitly considered secondary IMs. By explicitly considering the secondary IMs, it is less important to target specific causal parameters such as earthquake magnitude (e.g., [@Baker2021]). The site parameters, therefore, were not limited in creating the prospective ground motion catalogues to increase the number of prospective motions in the catalogue. Similarly, while scale factors applied to prospective ground motions were generally kept within the range 0.5 to 4.0, the scale factor was considered less important than the comparison of secondary IMs and the fit of selected ground motions to the target spectrum.

## 8.3 Ground Motion Selection Results

Table 10 and Table 11 list the key parameters of the two suites of eight, two-horizontal-component time histories selected for TS and TL, respectively.

Figure 18 and Figure 19 show the geometric means of the suites of selected scaled ground motions compared to the target 1/10/000 AEP UHS, respectively. The figures show that the geometric mean of each suite of ground motions agrees well with the target spectra because it falls between 90% and 130% of the target spectra within the period range of interest.

Table 12 and Table 13 list selected intensity measures for each component for the suites of motions selected for TS and TL, respectively. The intensity measures of the suites of selected motions generally agree with the theoretical values listed in Table 8 and Table 9. Figure 20 and Figure 21 show the cumulative probability of empirical and estimated conditional intensity measures for AI, CAV, D5-75, and D5-95. Figure 20 and Figure 21 show that the IMs of the selected motions are generally well matched to their theoretical values. However, the IMs of the scaled motions appear higher relative to the target IMs (i.e., average values of scaled IMs are slightly greater than the median of the respective target IMs).

As discussed in Section 8.1, the ground motion selection process focused on selecting motions that matched the target spectrum and generally agreed with estimated conditional IMs. Consequently, the selected suites of ground motions for TS and TL include records with shorter source-to-site distances than suggested by the magnitude-distance-epsilon disaggregation results presented in Section 7.1.3. The shorter source-to-site distances allowed a better fit to the target spectrum, while still agreeing with the estimated conditional IMs. The selection of records with shorter source-to-site distances is commonly used when applying earthquake ground motions from plate boundary areas to intraplate stable continental regions such as that surrounding the Louvicourt TSF site in southeast Canada.

A major reason why the source-to-site distances of selected records are shorter than the disaggregation results is in part because of the difference between the Louvicourt TSF site condition (VS30 = 1,853 m/s) and the relatively less stiff plate boundary ground conditions where the prospective ground motions were recorded. Moderate- to high-frequency ground motions are attenuated faster by weaker seismic ground conditions (i.e., lower VS30) compared to stiffer ground conditions. Additionally, moderate- to high-frequency ground motions are attenuated faster than lower frequency ground motions. To capture the high-frequency (short-period) ground motions indicated by the 1/10,000 AEP UHS at the Louvicourt TSF site, records with shorter source-to-site distances were required. Some records with larger scale factors were also required to obtain a good match to the target spectrum in the shorter period range of interest (notably, RSNs 1833 and 2927 in Table 10). We anticipate that suitable candidate ground motions from intraplate conditions would have source-to-site distances that are more consistent with the disaggregation results. Regardless, the selected motions have engineering IMs that are consistent with the hazard based on intraplate conditions, so we consider that they are suitable for engineering analyses at the Louvicourt TSF site.

Appendix A and Appendix B present the selected, scaled EATHs for the short and long period range of interest, respectively. Digital records from the EATH development accompany this report.

**Table 10: Suite of Selected EATHs Scaled for the Short Period Range (0.062 s to 0.62 s) at the Louvicourt TSF Site.**

| ID | Record Sequence Number | Earthquake Designation or Name | Year | Recording Station Name | Source Mechanism Type | Earthquake Magnitude (Mw) | Source-to-Site Distance (Rrup km) | Site Ground Condition (VS30 m/s) | Scale Factor |
|----|------------------------|--------------------------------|------|------------------------|----------------------|---------------------------|-----------------------------------|----------------------------------|--------------|
| 1 | 516 | N. Palm Springs, USA | 1986 | Cranston Forest Station | Reverse Oblique | 6.06 | 28 | 425 | 1.11 |
| 2 | 530 | N. Palm Springs, USA | 1986 | Palm Springs Airport | Reverse Oblique | 6.06 | 11 | 312 | 0.95 |
| 3 | 1833 | Hector Mine, USA | 1999 | Snow Creek | Strike Slip | 7.13 | 73 | 524 | 8.28 |
| 4 | 2927 | Chi-Chi, Taiwan-04 | 1999 | TTN040 | Strike Slip | 6.2 | 51 | 728 | 6.85 |
| 5 | 3185 | Chi-Chi, Taiwan-05 | 1999 | TCU060 | Reverse | 6.2 | 56 | 375 | 3.19 |
| 6 | 4347 | Umbria Marche, Italy | 1997 | Borgo-Cerreto Torre | Normal | 6 | 19 | 519 | 1.90 |
| 7 | 5618 | Iwate, Japan | 2008 | IWT010 | Reverse | 6.9 | 16 | 826 | 0.59 |
| 8 | 5773 | Iwate, Japan | 2008 | Miyagi Great Village | Reverse | 6.9 | 41 | 531 | 0.80 |

**Table 11: Suite of Selected EATHs Scaled for the Long Period Range (0.23 s to 2.3 s) at the Louvicourt TSF Site.**

| ID | Record Sequence Number | Earthquake Designation or Name | Year | Recording Station Name | Source Mechanism Type | Earthquake Magnitude (Mw) | Source-to-Site Distance (Rrup km) | Site Ground Condition (VS30 m/s) | Scale Factor |
|----|------------------------|--------------------------------|------|------------------------|----------------------|---------------------------|-----------------------------------|----------------------------------|--------------|
| 1 | 68 | San Fernando, USA | 1971 | LA - Hollywood Stor FF | Reverse | 6.61 | 23 | 316 | 0.64 |
| 2 | 746 | Loma Prieta, USA | 1989 | Bear Valley #5 Callens Ranch | Reverse Oblique | 6.93 | 54 | 391 | 1.51 |
| 3 | 774 | Loma Prieta, USA | 1989 | Hayward City Hall - North | Reverse Oblique | 6.93 | 55 | 735 | 2.67 |
| 4 | 869 | Landers, USA | 1992 | LA - N Westmoreland | Strike Slip | 7.28 | 159 | 315 | 2.33 |
| 5 | 923 | Big Bear-01, USA | 1992 | Phelan - Wilson Ranch | Strike Slip | 6.46 | 64 | 333 | 2.87 |
| 6 | 1474 | Chi-Chi, Taiwan | 1999 | TCU025 | Reverse Oblique | 7.62 | 53 | 665 | 1.51 |
| 7 | 3471 | Chi-Chi, Taiwan-06 | 1999 | TCU075 | Reverse | 6.3 | 26 | 573 | 1.71 |
| 8 | 6060 | Big Bear-01, USA | 1992 | North Palm Springs Fire Sta #36 | Strike Slip | 6.46 | 42 | 368 | 0.77 |

**Table 12: Intensity Measures of the Selected Scaled EATHs for the Short Period Range (0.062 s to 0.62 s) at the Louvicourt TSF Site.**

| ID | Earthquake Designation or Name | Scale Factor | Recording Component | PGV (cm/s) | AI (m/s) | CAV (m/s) | D5-75 (s) | D5-95 (s) |
|----|--------------------------------|--------------|---------------------|------------|----------|-----------|-----------|-----------|
| 1 | 516 | 1.11 | 225 | 8.24 | 0.14 | 2.03 | 5.04 | 7.45 |
| | | | 315 | 13.25 | 0.23 | 2.61 | 3.39 | 5.60 |
| 2 | 530 | 0.95 | 180 | 11.93 | 0.27 | 4.87 | 6.14 | 14.70 |
| | | | 270 | 11.61 | 0.29 | 5.25 | 5.87 | 17.21 |
| 3 | 1833 | 8.28 | 90 | 38.55 | 0.71 | 10.23 | 14.01 | 23.35 |
| | | | 180 | 24.14 | 0.62 | 10.04 | 15.43 | 26.78 |
| 4 | 2927 | 6.85 | N | 15.10 | 0.29 | 4.70 | 6.00 | 14.13 |
| | | | E | 26.50 | 0.27 | 4.62 | 6.75 | 14.12 |
| 5 | 3185 | 3.19 | N | 9.72 | 0.28 | 5.35 | 9.84 | 17.88 |
| | | | E | 10.19 | 0.37 | 6.09 | 10.24 | 16.72 |
| 6 | 4347 | 1.90 | 0 | 6.36 | 0.25 | 3.69 | 5.08 | 9.32 |
| | | | 90 | 8.49 | 0.24 | 3.52 | 4.37 | 8.74 |
| 7 | 5618 | 0.59 | NS | 12.92 | 0.44 | 8.26 | 9.28 | 19.85 |
| | | | EW | 15.57 | 0.44 | 8.44 | 7.87 | 24.62 |
| 8 | 5773 | 0.80 | NS | 9.21 | 0.34 | 6.18 | 10.02 | 17.85 |
| | | | EW | 11.57 | 0.47 | 6.9 | 7.96 | 16.86 |

**Table 13: Intensity Measures of the Selected Scaled EATHs for the Long Period Range (0.23 s to 2.3 s) at the Louvicourt TSF Site.**

| ID | Earthquake Designation or Name | Scale Factor | Recording Component | PGV (cm/s) | AI (m/s) | CAV (m/s) | D5-75 (s) | D5-95 (s) |
|----|--------------------------------|--------------|---------------------|------------|----------|-----------|-----------|-----------|
| 1 | 68 | 0.64 | 90 | 13.86 | 0.27 | 4.84 | 5.25 | 13.19 |
| | | | 180 | 10.81 | 0.18 | 4.04 | 5.10 | 13.53 |
| 2 | 746 | 1.51 | 220 | 14.00 | 0.20 | 4.41 | 10.82 | 17.47 |
| | | | 310 | 15.43 | 0.20 | 4.36 | 10.97 | 17.79 |
| 3 | 774 | 2.67 | 64 | 14.98 | 0.28 | 5.45 | 7.53 | 19.55 |
| | | | 334 | 16.15 | 0.27 | 4.90 | 6.69 | 14.65 |
| 4 | 869 | 2.33 | 0 | 27.55 | 0.33 | 6.37 | 15.26 | 22.60 |
| | | | 270 | 10.91 | 0.26 | 5.81 | 16.48 | 24.05 |
| 5 | 923 | 2.87 | 90 | 9.16 | 0.41 | 8.19 | 14.66 | 30.70 |
| | | | 180 | 11.62 | 0.50 | 8.15 | 10.19 | 21.83 |
| 6 | 1474 | 1.51 | W | 26.12 | 0.24 | 4.64 | 12.71 | 18.15 |
| | | | N | 14.12 | 0.21 | 4.36 | 11.78 | 14.65 |
| 7 | 3471 | 1.71 | N | 7.98 | 0.17 | 4.66 | 10.97 | 24.72 |
| | | | E | 13.63 | 0.39 | 6.28 | 8.87 | 17.04 |
| 8 | 6060 | 0.77 | 90 | 10.33 | 0.24 | 4.36 | 8.54 | 12.89 |
| | | | 180 | 8.99 | 0.23 | 4.29 | 7.50 | 12.54 |

**Figure 18: Acceleration Response Spectra for Horizontal Geometric Mean and Individual Selected Scaled EATHs Compared to the Target Spectrum (Short Period Range). Period Range of Interest Highlighted.**

**Figure 19: Acceleration Response Spectra for Horizontal Geometric Mean and Individual Selected Scaled EATHs Compared to the Target Spectrum (Long Period Range). Period Range of Interest Highlighted.**

**Figure 20: Cumulative Probability of Scaled (blue) and Conditional (black) AI, CAV, D5-75, and D5-95 Intensity Measures from the Selected Scaled EATHs (Short Period Range).**

**Figure 21: Cumulative Probability of Scaled (blue) and Conditional (black) AI, CAV, D5-75, and D5-95 Intensity Measures from the Selected Scaled EATHs (Long Period Range).**
