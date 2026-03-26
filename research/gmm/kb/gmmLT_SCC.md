# SCC GMPE logic tree

## Official runtime files
- Logic tree (NRML): `gmm/TRT/SCC/gmmLT_SCC.xml`
- Branches (TSV): `gmm/TRT/SCC/gmmLT_SCC.tsv`
- Runtime collapsed table: `gmm/TRT/SCC/NGAEastUSGS_collapsed.hdf5`

## Current official tree
- `logicTreeID`: `seed_SCC_modern`
- `branchingLevelID`: `bl_SCC`
- `branchSetID`: `bs_SCC`
- `applyToTectonicRegionType`: `SCC`
- Total branches: 6
- Total weight: `1.00000`
- Weighting: quasi-uniform; five regional branches carry `0.16667` each and the collapsed NGA-East replacement carries the residual `0.16665`

## Branches
- `Atkinson2008prime` → `0.16667`
- `AtkinsonBoore2006Modified2011` → `0.16667`
- `PezeshkEtAl2011` → `0.16667`
- `ESHM20Craton` → `0.16667`
- `SomervilleEtAl2009YilgarnCraton_SS14` → `0.16667`
- `CollapsedNGAEastUSGS` → `0.16665`


## Requirements (hazardlib)
(Distances/site/rupture parameters required by the current local hazardlib implementation.)

### `Atkinson2008prime`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/boore_atkinson_2011.py`
- requires_distances: `rjb`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag,rake`

### `AtkinsonBoore2006Modified2011`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/atkinson_boore_2006.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `PezeshkEtAl2011`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/pezeshk_2011.py`
- requires_distances: `rrup`
- requires_rupture_parameters: `mag`

### `ESHM20Craton`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/eshm20_craton.py`
- requires_distances: `rrup`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `SomervilleEtAl2009YilgarnCraton_SS14`
- source: `/Users/averrik/.pyenv/versions/3.12.11/lib/python3.12/site-packages/openquake/hazardlib/gsim/somerville_2009.py`
- requires_distances: `rjb`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`

### `CollapsedNGAEastUSGS`
- source: `gmm/gmpe/gsim/collapsed_nga_east_usgs.py`
- requires_sites_parameters: `vs30`
- requires_rupture_parameters: `mag`
- runtime table: `gmm/TRT/SCC/NGAEastUSGS_collapsed.hdf5`
- note: custom GSIM registered via `gmm.gmpe`; it extends `NGAEastUSGSGMPE` and inflates total sigma with a stored between-model term
