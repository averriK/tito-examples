# ASC GMPE logic tree

## Official runtime files
- Logic tree (NRML): `gmm/TRT/ASC/gmmLT_ASC.xml`
- Branches (TSV): `gmm/TRT/ASC/gmmLT_ASC.tsv`

## Current official tree
- `logicTreeID`: `seed_ASC_modern`
- `branchingLevelID`: `bl_ASC`
- `branchSetID`: `bs_ASC`
- `applyToTectonicRegionType`: `ASC`
- Total branches: 10
- Total weight: `1.00000`
- Weighting: uniform (`0.10000` per branch)

## Branches
- `AristeidouEtAl2024` → `0.10000`
- `Atkinson2022Crust` → `0.10000`
- `BooreEtAl2020` → `0.10000`
- `BozorgniaCampbell2016` → `0.10000`
- `CampbellBozorgnia2019` → `0.10000`
- `ChaoEtAl2020Asc` → `0.10000`
- `KothaEtAl2020` → `0.10000`
- `PhungEtAl2020Asc` → `0.10000`
- `Stafford2022` → `0.10000`
- `StewartEtAl2016` → `0.10000`


## Requirements (hazardlib)
(Distances/site/rupture parameters required by the current local hazardlib implementation.)

### `AristeidouEtAl2024`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/aristeidou_2024.py`
- requires_distances: `rjb,rrup,rx`
- requires_sites_parameters: `vs30,z2pt5`
- requires_rupture_parameters: `hypo_depth,mag,rake,ztor`

### `Atkinson2022Crust`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/nz22/atkinson_2022.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `BooreEtAl2020`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/boore_2020.py`
- requires_distances: `rjb`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,rake`

### `BozorgniaCampbell2016`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/bozorgnia_campbell_2016.py`
- requires_distances: `rjb,rrup,rx`
- requires_sites_parameters: `vs30,z2pt5`
- requires_rupture_parameters: `dip,hypo_depth,mag,rake,width,ztor`

### `CampbellBozorgnia2019`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/campbell_bozorgnia_2014.py`
- requires_distances: `rjb,rrup,rx`
- requires_sites_parameters: `vs30,z2pt5`
- requires_rupture_parameters: `dip,hypo_depth,mag,rake,width,ztor`

### `ChaoEtAl2020Asc`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/chao_2020.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30,vs30measured,z1pt0`
- requires_rupture_parameters: `mag,rake,ztor`

### `KothaEtAl2020`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/kotha_2020.py`
- requires_distances: `rjb`
- requires_rupture_parameters: `hypo_depth,mag`

### `PhungEtAl2020Asc`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/phung_2020.py`
- requires_distances: `rjb,rrup,rx`
- requires_sites_parameters: `vs30,z1pt0`
- requires_rupture_parameters: `dip,mag,rake,ztor`

### `Stafford2022`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/nz22/stafford_2022.py`
- requires_distances: `rjb,rrup,rx`
- requires_sites_parameters: `vs30,vs30measured,z1pt0`
- requires_rupture_parameters: `dip,mag,rake,ztor`

### `StewartEtAl2016`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/stewart_2016.py`
- requires_distances: `rjb`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,rake`
