# Seismic Hazard Assessment

## Ground Motion Intensity Measures

Ground motion intensity measures (IMs) quantify the strength of earthquake shaking at a site. Common IMs include peak ground acceleration (PGA), peak ground velocity (PGV), and spectral acceleration at various periods (Sa(T)).

The choice of intensity measure affects hazard curve accuracy and depends on the engineering application. For structural analysis, spectral acceleration at the fundamental period of the structure is typically most relevant [@BakerCornell2006].

## Seismic Source Characterization

Seismic sources are characterized by their geometry, activity rate, and maximum magnitude. Source models include point sources, line sources (faults), and area sources representing distributed seismicity.

The Gutenberg-Richter relationship describes the frequency-magnitude distribution of earthquakes: $\log_{10}(N) = a - bM$, where N is the annual number of events exceeding magnitude M [@GutenbergRichter1944].

Fault rupture dimensions scale with magnitude following empirical relationships. Wells and Coppersmith (1994) provide widely-used scaling relations between magnitude, rupture length, and rupture area based on global earthquake data [@WellsCoppersmith1994].

## Site Effects

Local soil conditions significantly amplify or attenuate seismic waves. Site classification schemes (e.g., NEHRP, Eurocode 8) categorize sites based on average shear-wave velocity in the upper 30 meters (Vs30).

Amplification factors vary with input motion intensity, exhibiting nonlinear behavior at high strain levels. Modern ground motion models incorporate site-specific Vs30 values to account for these effects [@BooreAtkinson2008].
