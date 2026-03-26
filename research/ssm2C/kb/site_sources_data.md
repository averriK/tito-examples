# XAF site report — Longonjo

Generated (UTC): `2026-02-28T15:04:04.377797+00:00`

## Site
- lon/lat: **15.248450**, **-12.907950**

## Source inventory (from regional docs)
- Total sources in regional docs: **255**
- Counts by source type: `{"multiPointSource": 140, "simpleFaultSource": 115}`

## Nearest sources (overall)
- `MPS-2` (multiPointSource) — 2.5 km — 
- `MPS-1` (multiPointSource) — 271.5 km — 
- `MPS-1200` (multiPointSource) — 592.9 km — Mweru - Katanga - Upemba
- `MPS-1100` (multiPointSource) — 874.8 km — Luama rift
- `MPS-1201` (multiPointSource) — 920.3 km — Mweru - Katanga - Upemba (2L)
- `MPS-1300` (multiPointSource) — 921.6 km — Kariba - Okavango
- `MPS-1101` (multiPointSource) — 1051.6 km — Luama rift (2L)
- `MPS-3` (multiPointSource) — 1201.8 km — 
- `MPS-1301` (multiPointSource) — 1263.8 km — Kariba - Okavango (2L)
- `MPS-1000` (multiPointSource) — 1340.3 km — Walikale and Masisi

## Detailed sources (closest / most relevant)
This section is intentionally *not* a full source listing. Full per-source data (all sources + distances) is in the JSON companion file.

### MPS-2 — <unnamed>

- distance (km): **2.52**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/WAF_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.76 / 6.56 / 6.96**
- recurrence: a=3.85022754903 b=1.04821870845
  - b low/high: 0.99821870845 / 1.0982187084500001
  - N0: 7083.168104801887 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=45.0 mean=18.33332
- logic-tree epistemic (from `ssmLT_XAF.xml`):
  - Mmax: maxMagGRRelative (branchSetID=mmax_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 6.96 (Δ=+0.20) w=0.25, 6.76 (Δ=+0.00) w=0.5, 6.56 (Δ=-0.20) w=0.25
  - b: bGRRelative (branchSetID=bval_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 1.10 (Δ=+0.05) w=0.25, 1.05 (Δ=+0.00) w=0.5, 1.00 (Δ=-0.05) w=0.25

### MPS-1 — <unnamed>

- distance (km): **271.51**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/WAF_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **5.76 / 5.56 / 5.96**
- recurrence: a=4.0471038639 b=1.04821870845
  - b low/high: 0.99821870845 / 1.0982187084500001
  - N0: 11145.610550909903 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=45.0 mean=18.33332
- logic-tree epistemic (from `ssmLT_XAF.xml`):
  - Mmax: maxMagGRRelative (branchSetID=mmax_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 5.96 (Δ=+0.20) w=0.25, 5.76 (Δ=+0.00) w=0.5, 5.56 (Δ=-0.20) w=0.25
  - b: bGRRelative (branchSetID=bval_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 1.10 (Δ=+0.05) w=0.25, 1.05 (Δ=+0.00) w=0.5, 1.00 (Δ=-0.05) w=0.25

### MPS-1200 — Mweru - Katanga - Upemba

- distance (km): **592.94**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=4.04527187775 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 11098.694001050155 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1100 — Luama rift

- distance (km): **874.82**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.51002108308 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 3236.0936635454837 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1201 — Mweru - Katanga - Upemba (2L)

- distance (km): **920.33**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=4.13034183245 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 13500.250669551759 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1300 — Kariba - Okavango

- distance (km): **921.59**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=4.08186411875 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 12074.359956717131 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1101 — Luama rift (2L)

- distance (km): **1051.65**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.92725619244 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 8457.776263895168 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-3 — <unnamed>

- distance (km): **1201.82**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/WAF_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.5 / 6.3 / 6.7**
- recurrence: a=4.12526753323 b=1.04821870845
  - b low/high: 0.99821870845 / 1.0982187084500001
  - N0: 13343.431584784243 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=45.0 mean=18.33332
- logic-tree epistemic (from `ssmLT_XAF.xml`):
  - Mmax: maxMagGRRelative (branchSetID=mmax_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 6.70 (Δ=+0.20) w=0.25, 6.50 (Δ=+0.00) w=0.5, 6.30 (Δ=-0.20) w=0.25
  - b: bGRRelative (branchSetID=bval_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 1.10 (Δ=+0.05) w=0.25, 1.05 (Δ=+0.00) w=0.5, 1.00 (Δ=-0.05) w=0.25

### MPS-1301 — Kariba - Okavango (2L)

- distance (km): **1263.79**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.99041880332 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 9781.800549288257 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1000 — Walikale and Masisi

- distance (km): **1340.34**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.89590604332 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 7868.755360677387 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-1001 — Walikale and Masisi (2L)

- distance (km): **1670.47**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.91777492937 b=0.991465033403
  - b low/high: 0.991465033403 / 0.991465033403
  - N0: 8275.131985878437 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=17.987000000000002

### MPS-800 — Western Rift - Tanganika

- distance (km): **1673.45**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `ASC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **7.9 / 7.9 / 7.9**
- recurrence: a=4.84168258571 b=1.01540069736
  - b low/high: 1.01540069736 / 1.01540069736
  - N0: 69451.65283814794 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.47851

### MPS-600 — Western Rift - Lake Edward, Albert and Kivu

- distance (km): **1794.41**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `ASC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **7.9 / 7.9 / 7.9**
- recurrence: a=4.88633433769 b=1.01540069736
  - b low/high: 1.01540069736 / 1.01540069736
  - N0: 76972.27763923426 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.47851

### MPS-4 — <unnamed>

- distance (km): **1795.84**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/WAF_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **5.43 / 5.2299999999999995 / 5.63**
- recurrence: a=3.83718813757 b=1.04821870845
  - b low/high: 0.99821870845 / 1.0982187084500001
  - N0: 6873.661444401164 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=45.0 mean=18.33332
- logic-tree epistemic (from `ssmLT_XAF.xml`):
  - Mmax: maxMagGRRelative (branchSetID=mmax_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 5.63 (Δ=+0.20) w=0.25, 5.43 (Δ=+0.00) w=0.5, 5.23 (Δ=-0.20) w=0.25
  - b: bGRRelative (branchSetID=bval_waf) applyToSources='MPS-1 MPS-2 MPS-3 MPS-4 MPS-5 MPS-6' => 1.10 (Δ=+0.05) w=0.25, 1.05 (Δ=+0.00) w=0.5, 1.00 (Δ=-0.05) w=0.25

### MPS-900 — Malawi - Nyasa Rift

- distance (km): **1826.63**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `ASC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **7.9 / 7.9 / 7.9**
- recurrence: a=4.92874324503 b=1.01540069736
  - b low/high: 1.01540069736 / 1.01540069736
  - N0: 84867.8587770641 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.47851

### MPS-1800 — South Mozambique

- distance (km): **1913.73**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `ASC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **7.9 / 7.9 / 7.9**
- recurrence: a=4.39891335151 b=1.01540069736
  - b low/high: 1.01540069736 / 1.01540069736
  - N0: 25056.092952141298 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.47851

### MPS-700 — Lake Victoria

- distance (km): **1923.88**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.99555407902 b=1.02153138044
  - b low/high: 1.02153138044 / 1.02153138044
  - N0: 9898.15109502568 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.23076

### MPS-2000 — Rowuma Basin

- distance (km): **2100.33**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=3.30548320061 b=1.02153138044
  - b low/high: 1.02153138044 / 1.02153138044
  - N0: 2020.613269067557 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.23076

### MPS-701 — Lake Victoria (2L)

- distance (km): **2147.68**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **6.9 / 6.9 / 6.9**
- recurrence: a=4.22920011806 b=1.02153138044
  - b low/high: 1.02153138044 / 1.02153138044
  - N0: 16951.18712337824 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=19.23076

### MPS-1500 — Eastern Rift

- distance (km): **2226.33**
- present in sourceModel branches: `naf_faults` (w=0.5), `naf_smooth` (w=0.5)
- xml: `ssm_XAF/SSA_GridMultiSources_Collapsed.xml`
- tectonic region: `SCC`
- MFD type: `multiMFD:truncGutenbergRichterMFD`
- Mmax base/low/high: **7.4 / 7.4 / 7.4**
- recurrence: a=5.30875842381 b=1.15852989658
  - b low/high: 1.15852989658 / 1.15852989658
  - N0: 203590.92886780223 (method=sum(10**a_val))
- depths (km): upper=0.0 lower=40.0 mean=18.76811

