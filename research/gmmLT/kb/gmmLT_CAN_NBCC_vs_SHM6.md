# Comparación de GMPEs: CAN `gmmLT_NBCC.xml` vs base `gmmLT_SHM6.xml`

## 1. Contexto y objetivo

En el modelo CAN v2025.0.0 existen dos árboles de GMPE relacionados para la familia SHM6/NBCC:

- Árbol NBCC original (modelo regulatorio):
  - `model/CAN/v2025.0.0/model/nbcc/gmmLT_NBCC.xml`
- Árbol base SHM6 usado como plantilla global en este repo:
  - `gmmLT/gmmLT_SHM6.xml`

El objetivo es documentar en qué son **idénticos** y en qué se **diferencian** estos árboles lógicos de GMPE.

---

## 2. Partes idénticas

### 2.1 Estructura general

Ambos ficheros son NRML 0.4 con un único `<logicTree logicTreeID="lt1">` y cinco niveles de branching:

- `bl1`: Stable Shallow Crust (SCC)
- `bl2`: Active Shallow Crust (ASC)
- `bl3`: Subduction Interface
- `bl4`: Subduction IntraSlab30
- `bl5`: Subduction IntraSlab55

No hay diferencias en la estructura de niveles ni en los tipos de TRT a los que se aplican.

### 2.2 Stable Shallow Crust (SCC)

En el nivel `bl1` los dos árboles son **idénticos**:

- `branchSetID="bs1"`, `applyToTectonicRegionType="SCC"`.
- 13 ramas `CanadaSHM6_StableCrust_NGAEast` (`submodel='01'..'13'`) con pesos base y pesos específicos por IMT (`PGA`, `PGV`, `SA(0.05)`... `SA(10.0)`).
- 3 ramas `CanadaSHM6_StableCrust_AA13` (`submodel='high'`, `central`, `low`) con pesos 0.15, 0.25 y 0.10.
- Para cada IMT, la suma de pesos sobre las 16 ramas es 1.0 en ambos ficheros.

Es decir, **la epistemología SCC NBCC se conserva exactamente** en `gmmLT_SHM6.xml`.

---

## 3. Diferencias por tipo tectónico

A partir de `bl2` los árboles divergen: `gmmLT_SHM6.xml` extiende el NBCC añadiendo GMPEs GEM/SRK y rebalanceando los pesos.

### 3.1 Active Shallow Crust (ASC)

**NBCC (`gmmLT_NBCC.xml`, `bl2`, `branchSetID="bs2"`):**

- Solo contiene **GMPEs Canada SHM6 ActiveCrust (NGA‑West2)**:
  - `CanadaSHM6_ActiveCrust_AbrahamsonEtAl2014`
  - `CanadaSHM6_ActiveCrust_BooreEtAl2014`
  - `CanadaSHM6_ActiveCrust_CampbellBozorgnia2014`
  - `CanadaSHM6_ActiveCrust_ChiouYoungs2014`
- Cada una con `uncertaintyWeight = 0.25` (todas las IMTs comparten este peso).  
  → Epistemología ASC puramente NBCC/SHM6.

**Base SHM6 (`gmmLT_SHM6.xml`, `bl2`, `branchSetID="ASC_ALL"`):**

- Mantiene las 4 GMPEs Canada SHM6 ActiveCrust, pero con pesos reducidos a 0.11 cada una.
- Añade 5 GMPEs adicionales:
  - GEM ASC global:
    - `AbrahamsonEtAl2014` (0.11)
    - `ChiouYoungs2014` (0.11)
  - Modernos SRK ASC:
    - `KothaEtAl2020` (0.11)
    - `BooreEtAl2020` (0.11)
    - `HassaniAtkinson2020Asc` (0.12)
- Todas las ramas ASC suman 1.0: 8×0.11 + 1×0.12 = 1.0.

**Interpretación:**

- NBCC: ASC = solo familia Canada SHM6.
- Base SHM6: ASC = mezcla de **Canada SHM6 + GEM + modernos SRK**, con pesos casi uniformes entre 9 modelos.

### 3.2 Subduction Interface

**NBCC (`bl3`, `branchSetID="bs3"`):**

- Solo Canada SHM6 Interface:
  - `CanadaSHM6_Interface_AbrahamsonEtAl2015SInter` (0.25)
  - `CanadaSHM6_Interface_AtkinsonMacias2009` (0.25)
  - `CanadaSHM6_Interface_GhofraniAtkinson2014Cascadia` (0.25)
  - `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia` (0.25)

**Base SHM6 (`bl3`, `branchSetID="SI_ALL"`):**

- Mantiene las 4 GMPEs Canada SHM6 Interface, pero con pesos 0.125 cada una.
- Añade 4 modelos modernos SRK 2020 Interface (globales):
  - `AbrahamsonGulerce2020SInter` (0.125)
  - `KuehnEtAl2020SInter` (0.125)
  - `ParkerEtAl2020SInter` (0.125)
  - `SiEtAl2020SInter` (0.125)
- Total: 8 ramas de peso 0.125 → suma 1.0.

**Interpretación:**

- NBCC: Interface = solo Canada SHM6.
- Base SHM6: Interface = combinación 50/50 (en peso total) entre **Canada SHM6** y **SRK 2020**.

### 3.3 Subduction IntraSlab30

**NBCC (`bl4`, `branchSetID="bs4"`):**

- Solo Canada SHM6 InSlab30:
  - `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab30` (0.25)
  - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30` (0.25)
  - `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30` (0.25)
  - `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30` (0.25)

**Base SHM6 (`bl4`, `branchSetID="SLAB30_ALL"`):**

- Mantiene las 4 GMPEs Canada SHM6 InSlab30 con pesos 0.125.
- Añade 4 GMPEs SRK 2020 Slab (misma función usada para 30/55 km en XAF):
  - `AbrahamsonGulerce2020SSlab` (0.125)
  - `KuehnEtAl2020SSlab` (0.125)
  - `ParkerEtAl2020SSlab` (0.125)
  - `SiEtAl2020SSlab` (0.125)
- Total: 8 ramas × 0.125 = 1.0.

### 3.4 Subduction IntraSlab55

**NBCC (`bl5`, `branchSetID="bs5"`):**

- Solo Canada SHM6 InSlab55:
  - `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab55` (0.25)
  - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55` (0.25)
  - `CanadaSHM6_InSlab_GarciaEtAl2005SSlab55` (0.25)
  - `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia55` (0.25)

**Base SHM6 (`bl5`, `branchSetID="SLAB55_ALL"`):**

- Mantiene las 4 GMPEs Canada SHM6 InSlab55 con pesos 0.125.
- Añade de nuevo las 4 GMPEs SRK 2020 Slab (se reutiliza la misma familia de modelos, aplicados a la TRT `Subduction IntraSlab55`):
  - `AbrahamsonGulerce2020SSlab` (0.125)
  - `KuehnEtAl2020SSlab` (0.125)
  - `ParkerEtAl2020SSlab` (0.125)
  - `SiEtAl2020SSlab` (0.125)
- Total: 8 ramas × 0.125 = 1.0.

---

## 4. Resumen conceptual

1. **NBCC (`gmmLT_NBCC.xml`)**
   - Es el árbol **regulatorio puro** NBCC 2020:
     - SCC: mezcla detallada de submodelos NGA‑East y AA13 (idéntica en ambos ficheros).
     - ASC: solo Canada SHM6 ActiveCrust (NGA‑West2).
     - Subducción (Interface, InSlab30, InSlab55): solo Canada SHM6.
   - No incluye GMPEs GEM globales ni la familia moderna SRK 2020.

2. **Base SHM6 (`gmmLT_SHM6.xml`)**
   - **Hereda exactamente** la parte SCC NBCC.
   - En ASC y subducción, **extiende** el árbol NBCC añadiendo familias GEM y SRK 2020:
     - ASC: Canada SHM6 + GEM + SRK modernos.
     - Interface / Slab30 / Slab55: Canada SHM6 + SRK 2020, con pesos 50/50 por familia.
   - Cambia los `branchSetID` (`bs2..bs5` → `ASC_ALL`, `SI_ALL`, `SLAB30_ALL`, `SLAB55_ALL`) y hace los `branchID` más descriptivos, pero sin alterar la lógica SCC.

3. **Uso recomendado**
   - Para **reproducir exactamente** los resultados NBCC 2020, debe usarse `gmmLT_NBCC.xml`.
   - Para estudios epistemológicos ampliados (comparar NBCC/SHM6 con GEM/SRK en un único árbol), puede usarse `gmmLT_SHM6.xml`, sabiendo que respeta SCC NBCC pero mezcla familias adicionales en ASC y subducción.
