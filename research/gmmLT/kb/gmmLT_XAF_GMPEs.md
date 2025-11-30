# GMPEs para XAF (árboles USGS, SHM6 y SRK)

Este documento resume los modelos de atenuación (GMPEs) empleados en los árboles lógicos de GMPE para la **región compuesta XAF** en este repositorio, usando los siguientes ficheros:

- USGS–XAF: `/Users/averrik/kashimaDB/openquake/model/XAF/model/usgs/gmmLT_USGS.xml`
- SHM6–XAF: `/Users/averrik/kashimaDB/openquake/model/XAF/model/shm6/gmmLT_USGS.xml`  
  *(mismo contenido lógico que el árbol USGS, sólo cambia el contexto de uso)*
- SRK–XAF: `/Users/averrik/kashimaDB/openquake/model/XAF/model/srk/gmmLT_SRK.xml`

El objetivo es obtener **(1)** el listado unificado de GMPEs usados en estos tres árboles XAF, **(2)** la región tectónica para la que fueron calibrados según `hazardlib` (Active Shallow Crust, Stable Shallow Crust, Subduction Interface, Subduction IntraSlab) y **(3)** un indicador del rango de periodos SA(T) disponible en la instalación local de `openquake.hazardlib` (periodos mínimos y máximos en las tablas de coeficientes).

La asignación de región tectónica se ha obtenido de `DEFINED_FOR_TECTONIC_REGION_TYPE` en la `hazardlib` local. En particular, los modelos NGA-East (`NGAEastUSGSSammons*`, `NGAEastUSGSSeed*`) aparecen categorizados como `Active Shallow Crust` en `hazardlib`, aunque físicamente representan CEUS estable; aquí se reporta la clasificación literal de `hazardlib` sin reinterpretarla.

## 1. GMPEs por tipo de región tectónica

### 1.1. Stable Shallow Crust (SCC)

Modelos modernos de corteza estable / cratónica, usados solo en el árbol SRK–XAF (`gmmLT_SRK.xml`).

- `ESHM20Craton`  
  - **TRT (`hazardlib`):** Stable Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T) en hazardlib:** de **0.01 s** a **10.0 s**.

- `RietbrockEdwards2019Mean`  
  - **TRT:** Stable Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.03 s** a **5.0 s** (no tiene periodos por encima de 5 s).

- `ShahjoueiPezeshk2016`  
  - **TRT:** Stable Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

### 1.2. Active Shallow Crust (ASC)

#### 1.2.1. Ramas NGA-East (CEUS, árboles USGS–XAF y SHM6–XAF)

La familia NGA-East USGS para CEUS se codifica en `hazardlib` como Active Shallow Crust. En los árboles XAF USGS/SHM6 aparecen:

- `NGAEastUSGSSammons1` – `NGAEastUSGSSammons17` (17 modelos Sammons)  
  - **TRT:** Active Shallow Crust (según `hazardlib`).  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** todos con tablas de **0.01 s** a **10.0 s**.

- `NGAEastUSGSSeedFrankel`, `NGAEastUSGSSeedGraizer16`, `NGAEastUSGSSeedGraizer17`,  
  `NGAEastUSGSSeedYA15`, `NGAEastUSGSSeedPZCT15_M1SS`, `NGAEastUSGSSeedPZCT15_M2ES` (6 modelos "seed")  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** todos con tablas de **0.01 s** a **10.0 s**.

#### 1.2.2. Ramas ActiveCrust de Canadá SHM6 (USGS–XAF y SHM6–XAF)

Estas ramas son las mismas que en el modelo canadiense SHM6, aplicadas a `Active Shallow Crust` en los árboles XAF de USGS y SHM6:

- `CanadaSHM6_ActiveCrust_AbrahamsonEtAl2014`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `CanadaSHM6_ActiveCrust_BooreEtAl2014`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `CanadaSHM6_ActiveCrust_CampbellBozorgnia2014`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `CanadaSHM6_ActiveCrust_ChiouYoungs2014`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

#### 1.2.3. Modelos modernos Active Shallow Crust (SRK–XAF)

Estos modelos solo aparecen en el árbol moderno SRK–XAF (`GMPE_Modern`):

- `KothaEtAl2020`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **8.0 s**.

- `BooreEtAl2020`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `HassaniAtkinson2020Asc`  
  - **TRT:** Active Shallow Crust.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

### 1.3. Subduction Interface

#### 1.3.1. Ramas Interface Canadá SHM6 (USGS–XAF y SHM6–XAF)

- `CanadaSHM6_Interface_AbrahamsonEtAl2015SInter`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.02 s** a **10.0 s**.

- `CanadaSHM6_Interface_AtkinsonMacias2009`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.05 s** a **10.0 s**.

- `CanadaSHM6_Interface_GhofraniAtkinson2014Cascadia`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.07 s** a **9.09 s**.

- `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.05 s** a **5.0 s**.

#### 1.3.2. Modelos subducción modernos (SRK–XAF)

- `AbrahamsonGulerce2020SInter`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `KuehnEtAl2020SInter`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `ParkerEtAl2020SInter`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `SiEtAl2020SInter`  
  - **TRT:** Subduction Interface.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

### 1.4. Subduction IntraSlab (30 km y 55 km)

#### 1.4.1. Ramas InSlab de Canadá SHM6 (USGS–XAF y SHM6–XAF)

- `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab30`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.02 s** a **10.0 s**.

- `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab55`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.02 s** a **10.0 s**.

- `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.04 s** a **4.0 s** (no permite T > 4 s).

- `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.04 s** a **4.0 s**.

- `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.04 s** a **5.0 s**.

- `CanadaSHM6_InSlab_GarciaEtAl2005SSlab55`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.04 s** a **5.0 s**.

- `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.05 s** a **5.0 s**.

- `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia55`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** USGS, SHM6.  
  - **SA(T):** de **0.05 s** a **5.0 s**.

#### 1.4.2. Modelos IntraSlab modernos (SRK–XAF)

- `AbrahamsonGulerce2020SSlab`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `KuehnEtAl2020SSlab`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `ParkerEtAl2020SSlab`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

- `SiEtAl2020SSlab`  
  - **TRT:** Subduction IntraSlab.  
  - **Árboles XAF:** SRK.  
  - **SA(T):** de **0.01 s** a **10.0 s**.

## 2. Rangos de periodos SA(T) y modelos limitantes

A partir de las tablas de coeficientes en la `hazardlib` local se obtiene:

- La mayoría de los modelos **Active Shallow Crust** (NGA-East, ramas ActiveCrust de Canadá SHM6, `BooreEtAl2020`, `HassaniAtkinson2020Asc`) cubren SA(T) desde ~**0.01 s** hasta **10 s**.  
- `KothaEtAl2020` es ligeramente más corto en periodo máximo (**0.01–8.0 s**), pero sigue cubriendo sin problema T = 4–5 s.  
- Para corteza estable (SCC), `ESHM20Craton` y `ShahjoueiPezeshk2016` llegan hasta **10 s**, mientras que `RietbrockEdwards2019Mean` llega hasta **5 s** (incluido).  
- En subducción Interface, todos los modelos modernos (`AbrahamsonGulerce2020SInter`, `KuehnEtAl2020SInter`, `ParkerEtAl2020SInter`, `SiEtAl2020SInter`) y la mayoría de las ramas Canadá SHM6 alcanzan periodos de **9–10 s**. La rama más restrictiva es `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia`, que sólo llega a **5 s**.  
- En subducción IntraSlab, los modelos modernos (`AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`, `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`) cubren **0.01–10 s**. Entre las ramas Canadá SHM6, las más limitantes son:
  - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30/55`: **0.04–4.0 s** (no tienen 5 s).  
  - `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30/55` y `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30/55`: **0.04–0.05 s** hasta **5.0 s**.

En consecuencia, para un diseño de IMTs en XAF que incluya ordenadas hasta **SA(5.0)**:

- Todos los modelos de corteza activa/estable de SRK–XAF y las ramas NGA-East / ActiveCrust de USGS–XAF/SHM6–XAF soportan T = 5 s.  
- En subducción Interface, todas las GMPEs consideradas llegan como mínimo a 5 s.  
- Las **únicas** GMPEs que **no** alcanzan 5 s son `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30` y `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55` (límite en 4 s). Si se desea pedir SA(5.0) también para subducción IntraSlab, habría que tratarlas específicamente (p. ej. excluirlas para T > 4 s o ajustar el árbol InSlab).

## 3. Resumen consolidado para XAF

Agrupando por tipo de región tectónica, el conjunto completo de GMPEs usado en los árboles XAF (USGS, SHM6 y SRK) es:

- **Stable Shallow Crust (SCC):**  
  `ESHM20Craton`, `RietbrockEdwards2019Mean`, `ShahjoueiPezeshk2016`.

- **Active Shallow Crust (ASC):**  
  `NGAEastUSGSSammons1–17`, `NGAEastUSGSSeedFrankel`, `NGAEastUSGSSeedGraizer16`, `NGAEastUSGSSeedGraizer17`,  
  `NGAEastUSGSSeedYA15`, `NGAEastUSGSSeedPZCT15_M1SS`, `NGAEastUSGSSeedPZCT15_M2ES`,  
  `CanadaSHM6_ActiveCrust_AbrahamsonEtAl2014`, `CanadaSHM6_ActiveCrust_BooreEtAl2014`,  
  `CanadaSHM6_ActiveCrust_CampbellBozorgnia2014`, `CanadaSHM6_ActiveCrust_ChiouYoungs2014`,  
  `KothaEtAl2020`, `BooreEtAl2020`, `HassaniAtkinson2020Asc`.

- **Subduction Interface:**  
  `CanadaSHM6_Interface_AbrahamsonEtAl2015SInter`, `CanadaSHM6_Interface_AtkinsonMacias2009`,  
  `CanadaSHM6_Interface_GhofraniAtkinson2014Cascadia`, `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia`,  
  `AbrahamsonGulerce2020SInter`, `KuehnEtAl2020SInter`, `ParkerEtAl2020SInter`, `SiEtAl2020SInter`.

- **Subduction IntraSlab (30/55 km):**  
  `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab30`, `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab55`,  
  `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`, `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`,  
  `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30`, `CanadaSHM6_InSlab_GarciaEtAl2005SSlab55`,  
  `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30`, `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia55`,  
  `AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`, `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`.

Este documento proporciona así el resumen de GMPEs efectivamente usados en la región compuesta **XAF** (para las variantes USGS, SHM6 y SRK), la región tectónica de calibración de cada modelo según `hazardlib` y el rango de periodos SA(T) que soportan en la instalación local.

## 4. Ajustes recientes en los árboles XAF (USGS, SHM6, SRK)

Esta sección documenta los cambios implementados al actualizar los árboles XAF para que:

- compartan un bloque común de corteza activa (**ASC_ALL**) y de subducción (**SI_ALL**, **SLAB30_ALL**, **SLAB55_ALL**) en las tres variantes (USGS, SHM6, SRK), y
- sigan siendo compatibles con los IMTs usados en los `job.ini` de XAF (incluyendo SA(5.0)), sin errores de rango de periodos ni de inicialización de GMPEs.

Los ficheros afectados son:

- `model/XAF/model/usgs/gmmLT_USGS.xml`
- `model/XAF/model/shm6/gmmLT_SHM6.xml`
- `model/XAF/model/srk/gmmLT_SRK.xml`

### 4.1. Bloques comunes ASC_ALL / SI_ALL / SLAB30_ALL / SLAB55_ALL

1. **Inserción de bloques comunes en SHM6–XAF**

   En `gmmLT_SHM6.xml` se dejó intacto el bloque original de corteza estable Canadá SHM6 (branchSet `bs1`, TRC `Stable Shallow Crust`) y se reemplazaron los bloques de:

   - `Active Shallow Crust` por el bloque común **ASC_ALL**.
   - `Subduction Interface` por **SI_ALL**.
   - `Subduction IntraSlab30` por **SLAB30_ALL**.
   - `Subduction IntraSlab55` por **SLAB55_ALL**.

   El contenido de estos bloques es idéntico (mismas GMPEs y pesos) al usado ya en los árboles USGS–XAF y SRK–XAF, de modo que en regiones puramente ASC o de subducción, las tres variantes XAF se comportan de manera consistente.

2. **Contenido de ASC_ALL tras los ajustes**

   El bloque **ASC_ALL** quedó finalmente formado por 9 GMPEs:

   - Canadá SHM6 ActiveCrust (NGA-West2):
     - `CanadaSHM6_ActiveCrust_AbrahamsonEtAl2014`
     - `CanadaSHM6_ActiveCrust_BooreEtAl2014`
     - `CanadaSHM6_ActiveCrust_CampbellBozorgnia2014`
     - `CanadaSHM6_ActiveCrust_ChiouYoungs2014`
   - GEM / global ASC:
     - `AbrahamsonEtAl2014`
     - `ChiouYoungs2014`
   - Modelos modernos SRK ASC:
     - `KothaEtAl2020`
     - `BooreEtAl2020`
     - `HassaniAtkinson2020Asc`

   Se eliminaron explícitamente dos modelos GEM ASC de los árboles XAF:

   - `AkkarCagnan2010` (error de rango de periodo: SA(3.0) fuera del rango definido en `hazardlib`).
   - `AkkarEtAlRjb2014` (error de rango de periodo: SA(5.0) fuera del rango definido).

   Tras estas eliminaciones se reasignaron los pesos de ASC_ALL con la siguiente regla simple:

   - 8 ramas con peso **0.11**.
   - 1 rama con peso **0.12**, de forma que \(8·0.11 + 0.12 = 1.0\).

   En los tres árboles XAF se asignó \(0.12\) a `HassaniAtkinson2020Asc`, quedando las demás ramas de ASC_ALL con \(0.11\).

3. **Contenido de SI_ALL / SLAB30_ALL / SLAB55_ALL**

   No se modificaron listas de modelos en los bloques de subducción respecto al diseño original; sólo se centralizó su uso en los tres árboles:

   - **SI_ALL** (Subduction Interface):
     - Ramas Canadá SHM6 Interface: `CanadaSHM6_Interface_AbrahamsonEtAl2015SInter`, `CanadaSHM6_Interface_AtkinsonMacias2009`, `CanadaSHM6_Interface_GhofraniAtkinson2014Cascadia`, `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia`.
     - Ramas modernas 2020 Interface: `AbrahamsonGulerce2020SInter`, `KuehnEtAl2020SInter`, `ParkerEtAl2020SInter`, `SiEtAl2020SInter`.
     - Todas con peso **0.125** cada una.

   - **SLAB30_ALL** (Subduction IntraSlab30):
     - Canadá SHM6 InSlab30: `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab30`, `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`, `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30`, `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30`.
     - Modernos 2020 Slab (~30 km): `AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`, `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`.
     - Todas con peso **0.125** cada una.

   - **SLAB55_ALL** (Subduction IntraSlab55):
     - Canadá SHM6 InSlab55: `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab55`, `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`, `CanadaSHM6_InSlab_GarciaEtAl2005SSlab55`, `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia55`.
     - Modernos 2020 Slab (~55 km): `AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`, `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`.
     - Todas con peso **0.125** cada una.

### 4.2. Ajustes específicos en el árbol SRK–XAF (SCC_ALL)

En el árbol moderno SRK–XAF (`model/XAF/model/srk/gmmLT_SRK.xml`) se depuró el bloque exclusivo de corteza estable **SCC_ALL**:

- Se eliminó la rama basada en `NRCan15SiteTerm` porque en `hazardlib` este modelo se implementa como término de sitio (requiere un argumento adicional `gmpe_name` en su constructor) y no puede usarse directamente como GMPE autónoma en el árbol lógico.
- El bloque SCC_ALL quedó finalmente con 4 GMPEs, todas con peso **0.25**:
  - `AtkinsonBoore2006Modified2011`
  - `ESHM20Craton`
  - `RietbrockEdwards2019Mean`
  - `ShahjoueiPezeshk2016`

Con estos ajustes los tres árboles XAF (USGS, SHM6 y SRK) se pueden ejecutar con los `job.ini` de XAF hasta **SA(5.0)** sin errores de:

- número excesivo de rutas lógicas (se mantiene la estructura original de SCC en cada modelo),
- rangos de periodo fuera de SA(T), ni
- inicialización incorrecta de GMPEs como `NRCan15SiteTerm`.
