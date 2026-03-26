# IND site report — Rampura Agucha

Generated (UTC): `2026-02-28T15:04:03.971857+00:00`

## Site
- project_name: **Rampura Agucha**
- lon/lat: **74.741300**, **25.847400**

## Logic tree (epistemic)
- sourceModel branches:
  - `ssm_IND/nt2012_areal_source_model_v1.xml` weight=0.4
  - `ssm_IND/nt2012_smoothed_source_model_v1_mmin4.5.xml` weight=0.27
  - `ssm_IND/nt2012_smoothed_source_model_v1_mmin5.5.xml` weight=0.33
- maxMagGRRelative (global): Δ-0.30 (w=0.32), Δ+0.00 (w=0.36), Δ+0.30 (w=0.32)
- bGRRelative (global): Δ-0.10 (w=0.32), Δ+0.00 (w=0.36), Δ+0.10 (w=0.32)

## Areal source model (areaSource zones)
- containing zones: **2**
- primary zone (selection rule): `z919`

### areaSource z919 — zone 919

- TRT: `SCC`
- depths (km): upper=0.0 lower=25.0 mean_hypo≈15.0
- MFD: truncGutenbergRichterMFD minMag=4.5 maxMag=7.2 a=2.73 b=0.72
- Mmax epistemic: range **[6.90, 7.50]**
- b epistemic: range **[0.62, 0.82]**

### areaSource z932 — zone 932

- TRT: `SCC`
- depths (km): upper=25.0 lower=70.0 mean_hypo≈25.0
- MFD: truncGutenbergRichterMFD minMag=4.5 maxMag=6.5 a=4.15 b=0.93
- Mmax epistemic: range **[6.20, 6.80]**
- b epistemic: range **[0.83, 1.03]**

## Smoothed seismicity models (pointSource grids)
### ssm_IND/nt2012_smoothed_source_model_v1_mmin4.5.xml

- branch weight in LT: 0.27
- pointSources scanned (from index CSV): 249954
- nearest pointSource: `25N_75p2E_L2_M4p5` at lon/lat=75.2000,25.0000 (distance=104.60 km)
- MFD type: `truncGutenbergRichterMFD`
- Mmax base/low/high: **6.5 / 6.2 / 6.8**
- recurrence: a=-1.4682125137753435 b=0.93
  - b low/high: 0.8300000000000001 / 1.03
- depths (km): upper=25.0 lower=70.0 mean=25.0

### ssm_IND/nt2012_smoothed_source_model_v1_mmin5.5.xml

- branch weight in LT: 0.33
- pointSources scanned (from index CSV): 193135
- nearest pointSource: `26p7N_74p1E_L2_M5p5` at lon/lat=74.1000,26.7000 (distance=114.13 km)
- MFD type: `truncGutenbergRichterMFD`
- Mmax base/low/high: **6.5 / 6.2 / 6.8**
- recurrence: a=-0.9143837776852095 b=0.93
  - b low/high: 0.8300000000000001 / 1.03
- depths (km): upper=25.0 lower=70.0 mean=25.0

## Notes / limitations
- This is a geometric association report (no OpenQuake run). Nearest sources are *candidates* for controlling hazard; definitive control requires hazard/deaggregation.
- The full smoothed grids are not expanded here; use `IND_sources_*.csv` for per-node parameters or query by provider_id.
