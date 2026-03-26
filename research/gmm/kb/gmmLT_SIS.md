# SIS GMPE logic tree

## Official runtime files
- Logic tree (NRML): `gmm/TRT/SIS/gmmLT_SIS.xml`
- Branches (TSV): `gmm/TRT/SIS/gmmLT_SIS.tsv`

## Current official tree
- `logicTreeID`: `seed_SIS_modern`
- `branchingLevelID`: `bl_SIS`
- `branchSetID`: `bs_SIS`
- `applyToTectonicRegionType`: `SIS`
- Total branches: 10
- Total weight: `1.00000`
- Weighting: uniform (`0.10000` per branch)

## Branches
- `AbrahamsonEtAl2018SSlab` → `0.10000`
- `AbrahamsonGulerce2020SSlab` → `0.10000`
- `Atkinson2022SSlab` → `0.10000`
- `ChaoEtAl2020SSlab` → `0.10000`
- `JaimesEtAl2020SSlab` → `0.10000`
- `KuehnEtAl2020SSlab` → `0.10000`
- `MontalvaEtAl2017SSlab` → `0.10000`
- `ParkerEtAl2020SSlab` → `0.10000`
- `PhungEtAl2020SSlab` → `0.10000`
- `SiEtAl2020SSlab` → `0.10000`


## Requirements (hazardlib)
(Distances/site/rupture parameters required by the current local hazardlib implementation.)

### `AbrahamsonEtAl2018SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/abrahamson_2018.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,ztor`

### `AbrahamsonGulerce2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/abrahamson_gulerce_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,ztor`

### `Atkinson2022SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/nz22/atkinson_2022.py`
- requires_distances: `rrup`
- requires_sites_parameters: `backarc,vs30`
- requires_rupture_parameters: `mag`

### `ChaoEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/chao_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,vs30measured,z1pt0`
- requires_rupture_parameters: `mag,ztor`

### `JaimesEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/jaimes_2020.py`
- requires_distances: `rhypo,rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `hypo_depth,mag`

### `KuehnEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/kuehn_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,ztor`

### `MontalvaEtAl2017SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/montalva_2017.py`
- requires_distances: `rhypo`
- requires_sites_parameters: `backarc,vs30`
- requires_rupture_parameters: `hypo_depth,mag`

### `ParkerEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/parker_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `hypo_depth,mag`

### `PhungEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/phung_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,z1pt0`
- requires_rupture_parameters: `mag,ztor`

### `SiEtAl2020SSlab`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/si_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,z2pt5`
- requires_rupture_parameters: `hypo_depth,mag`
