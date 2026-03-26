# SIF GMPE logic tree

## Official runtime files
- Logic tree (NRML): `gmm/TRT/SIF/gmmLT_SIF.xml`
- Branches (TSV): `gmm/TRT/SIF/gmmLT_SIF.tsv`

## Current official tree
- `logicTreeID`: `seed_SIF_modern`
- `branchingLevelID`: `bl_SIF`
- `branchSetID`: `bs_SIF`
- `applyToTectonicRegionType`: `SIF`
- Total branches: 10
- Total weight: `1.00000`
- Weighting: uniform (`0.10000` per branch)

## Branches
- `AbrahamsonEtAl2018SInter` → `0.10000`
- `AbrahamsonGulerce2020SInter` → `0.10000`
- `Atkinson2022SInter` → `0.10000`
- `AtkinsonMacias2009NSHMP2014` → `0.10000`
- `ChaoEtAl2020SInter` → `0.10000`
- `KuehnEtAl2020SInter` → `0.10000`
- `MontalvaEtAl2017SInter` → `0.10000`
- `ParkerEtAl2020SInter` → `0.10000`
- `PhungEtAl2020SInter` → `0.10000`
- `SiEtAl2020SInter` → `0.10000`


## Requirements (hazardlib)
(Distances/site/rupture parameters required by the current local hazardlib implementation.)

### `AbrahamsonEtAl2018SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/abrahamson_2018.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `AbrahamsonGulerce2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/abrahamson_gulerce_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `Atkinson2022SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/nz22/atkinson_2022.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `AtkinsonMacias2009NSHMP2014`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/can15/sinter.py`
- requires_distances: `rrup`
- requires_rupture_parameters: `mag`

### `ChaoEtAl2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/chao_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,vs30measured,z1pt0`
- requires_rupture_parameters: `mag,ztor`

### `KuehnEtAl2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/kuehn_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,ztor`

### `MontalvaEtAl2017SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/montalva_2017.py`
- requires_distances: `rrup`
- requires_sites_parameters: `backarc,vs30`
- requires_rupture_parameters: `mag`

### `ParkerEtAl2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/parker_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `PhungEtAl2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/phung_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,z1pt0`
- requires_rupture_parameters: `mag,ztor`

### `SiEtAl2020SInter`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/si_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,z2pt5`
- requires_rupture_parameters: `hypo_depth,mag`
