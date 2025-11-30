# GMPEs para XAF – árbol SRK (GEM + modernos)

Este documento describe el contenido del árbol lógico de GMPE **SRK–XAF**, definido en:

- `XAF/model/srk/gmmLT_SRK.xml` (logicTreeID = `GMPE_Modern`)

El objetivo de este árbol es reunir, en un único `gmmLT_SRK.xml`, **todos los modelos GEM África (ASC/SCC)** y los **modelos modernos SRK** (ASC/SCC y subducción), de forma **exclusiva** respecto a los árboles XAF de USGS y SHM6:

- USGS–XAF / SHM6–XAF (`XAF/model/usgs/gmmLT_USGS.xml`, `XAF/model/shm6/gmmLT_USGS.xml`) usan únicamente:
  - GMPEs **NGA-East** (`NGAEastUSGSSammons*`, `NGAEastUSGSSeed*`).
  - Wrappers **Canada SHM6** (`CanadaSHM6_ActiveCrust_*`, `CanadaSHM6_Interface_*`, `CanadaSHM6_InSlab_*`).
- SRK–XAF (`gmmLT_SRK.xml`) usa únicamente **GMPEs distintas** (GEM + modernas), de modo que el conjunto de nombres es disjunto.

## 1. Estructura general del árbol SRK–XAF

El árbol `GMPE_Modern` se organiza por **tipo de región tectónica** (`applyToTectonicRegionType`) con cuatro niveles principales:

1. `Stable Shallow Crust` (SCC)
2. `Active Shallow Crust` (ASC)
3. `Subduction Interface`
4. `Subduction IntraSlab30` y `Subduction IntraSlab55`

En cada nivel hay un único `logicTreeBranchSet` de tipo `gmpeModel`, con pesos normalizados a 1 dentro de cada conjunto.

## 2. Stable Shallow Crust (SCC)

Branching level: `bl_StableShallowCrust`  
BranchSet: `StableShallowCrust`, `applyToTectonicRegionType="Stable Shallow Crust"`

Incluye **5 GMPEs** con peso uniforme 0.2 cada una:

- `ESHM20Craton`  
- `RietbrockEdwards2019Mean`  
- `ShahjoueiPezeshk2016`  
- `AtkinsonBoore2006Modified2011`  *(GEM África, CEUS estable)*  
- `NRCan15SiteTerm`              *(término de sitio NRCan para Pezeshk CEUS, GEM África)*

Estas cinco ramas representan el conjunto combinado **SCC moderno + GEM** para XAF.

## 3. Active Shallow Crust (ASC)

Branching level: `bl_ActiveShallowCrust`  
BranchSet: `ActiveShallowCrust`, `applyToTectonicRegionType="Active Shallow Crust"`

Incluye **7 GMPEs** con peso uniforme ≈ 1/7 (0.1428571429):

Modelos modernos SRK:

- `KothaEtAl2020`
- `BooreEtAl2020`
- `HassaniAtkinson2020Asc`

Modelos GEM África (ASC):

- `AbrahamsonEtAl2014`
- `AkkarCagnan2010`
- `AkkarEtAlRjb2014`
- `ChiouYoungs2014`

Este conjunto mezcla explícitamente la epistemología GEM África ASC con la familia de modelos modernos SRK para corteza activa.

## 4. Subduction Interface

Branching level: `bl_SubductionInterface`  
BranchSet: `SubductionInterface`, `applyToTectonicRegionType="Subduction Interface"`

Incluye **4 GMPEs modernas** con pesos iguales 0.25:

- `AbrahamsonGulerce2020SInter`
- `KuehnEtAl2020SInter`
- `ParkerEtAl2020SInter`
- `SiEtAl2020SInter`

No se incluyen aquí los wrappers Canada SHM6 de Interfaz (éstos quedan reservados al árbol USGS/SHM6); SRK–XAF se apoya sólo en la familia 2020.

## 5. Subduction IntraSlab (30 km y 55 km)

Hay dos niveles análogos:

- `bl_SubductionIntraSlab30` con branchSet `SubductionIntraSlab30`, `applyToTectonicRegionType="Subduction IntraSlab30"`.
- `bl_SubductionIntraSlab55` con branchSet `SubductionIntraSlab55`, `applyToTectonicRegionType="Subduction IntraSlab55"`.

En ambos branchsets se usan las mismas **4 GMPEs modernas** con pesos 0.25 cada una:

- `AbrahamsonGulerce2020SSlab`
- `KuehnEtAl2020SSlab`
- `ParkerEtAl2020SSlab`
- `SiEtAl2020SSlab`

Estas ramas proporcionan un tratamiento coherente de subducción IntraSlab, separando solo por rango de profundidad (30 vs 55 km) mediante los `applyToTectonicRegionType` definidos en el árbol de fuentes.

## 6. Resumen de GMPEs incluidos en SRK–XAF

En total, `gmmLT_SRK.xml` contiene **20 modelos**:

- **SCC (Stable Shallow Crust)**:  
  `ESHM20Craton`, `RietbrockEdwards2019Mean`, `ShahjoueiPezeshk2016`,  
  `AtkinsonBoore2006Modified2011`, `NRCan15SiteTerm`.

- **ASC (Active Shallow Crust)**:  
  `KothaEtAl2020`, `BooreEtAl2020`, `HassaniAtkinson2020Asc`,  
  `AbrahamsonEtAl2014`, `AkkarCagnan2010`, `AkkarEtAlRjb2014`, `ChiouYoungs2014`.

- **Subduction Interface**:  
  `AbrahamsonGulerce2020SInter`, `KuehnEtAl2020SInter`,  
  `ParkerEtAl2020SInter`, `SiEtAl2020SInter`.

- **Subduction IntraSlab (30/55 km)**:  
  `AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`,  
  `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`.

Este árbol SRK–XAF está diseñado para ser **complementario** de los árboles USGS/SHM6 (que contienen únicamente NGA-East + Canada SHM6), de modo que un futuro árbol XAF combinado pueda mezclar explícitamente:

- Familia **GEM África** (ASC/SCC).
- Familia **NGA-East**.
- Familia **Canada SHM6** (ActiveCrust, Interface, InSlab).
- Familia **moderna SRK** para ASC/SCC/subducción.
