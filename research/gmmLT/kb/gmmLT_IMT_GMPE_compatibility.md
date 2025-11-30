# Auditoría IMT–GMPE para `gmmLT/`

## 1. Contexto

En `openquake/gmmLT/` existen cuatro árboles de GMPE principales:

- `gmmLT_GEM.xml`
- `gmmLT_USGS.xml`
- `gmmLT_SHM6.xml`
- `gmmLT_NBCC.xml` (NBCC puro, usado sobre todo para Canadá)

Los tres primeros comparten bloques comunes para:

- `ASC_ALL` – Active Shallow Crust
- `SI_ALL` – Subduction Interface
- `SLAB30_ALL` – Subduction IntraSlab30
- `SLAB55_ALL` – Subduction IntraSlab55

Las diferencias entre `GEM`, `USGS` y `SHM6` están en cómo tratan la corteza estable (SCC), pero las ramas de ASC y subducción son idénticas.

Los IMTs globales para estos árboles están definidos en `gmmLT/IMT.ini`:

```text
PGA
SA(0.05), SA(0.075), SA(0.10), SA(0.15), SA(0.20), SA(0.25), SA(0.30),
SA(0.50), SA(1.00), SA(2.00), SA(3.00), SA(4.00), SA(5.00)
```

La ordenada SA(0.01) **ya se ha eliminado** del fichero `IMT.ini`.

---

## 2. Rangos de periodo SA(T) por grupo de GMPE

Los rangos de periodo SA(T) se toman de la instalación local de `hazardlib` y de los documentos:

- `docs/gmmLT_GEM_SouthAfrica_GMPEs.md`
- `docs/gmmLT_XAF_GMPEs.md`
- `docs/gmmLT_ModernGMPEs.md`

### 2.1. Stable Shallow Crust (SCC)

Modelos relevantes en los árboles `gmmLT_*`:

- `AtkinsonBoore2006Modified2011`: SA(T) ≈ **0.01–10 s**.
- `ESHM20Craton`: ≈ 0.01–10 s.
- `RietbrockEdwards2019Mean`: ≈ 0.03–**5.0 s**.
- `ShahjoueiPezeshk2016`: 0.01–10 s.
- Familia NGA-East (`NGAEastUSGSSammons*`, `NGAEastUSGSSeed*`), usada como SCC en `gmmLT_USGS.xml`: 0.01–10 s.
- `CanadaSHM6_StableCrust_*` en `gmmLT_SHM6.xml` y `gmmLT_NBCC.xml`: por construcción soportan al menos 0.05–10 s (NBCC usa hasta SA(10.0)).

Con IMTs 0.05–5.0, **todas** las GMPEs SCC están dentro del rango permitido de SA(T).

### 2.2. Active Shallow Crust (ASC_ALL)

Bloque común `ASC_ALL` en `gmmLT_GEM.xml`, `gmmLT_USGS.xml`, `gmmLT_SHM6.xml`:

- Canadá SHM6 ActiveCrust:
  - `CanadaSHM6_ActiveCrust_AbrahamsonEtAl2014`
  - `CanadaSHM6_ActiveCrust_BooreEtAl2014`
  - `CanadaSHM6_ActiveCrust_CampbellBozorgnia2014`
  - `CanadaSHM6_ActiveCrust_ChiouYoungs2014`
  - SA(T): 0.01–10 s.
- GEM África ASC:
  - `AbrahamsonEtAl2014`: 0.01–10 s.
  - `ChiouYoungs2014`: 0.01–10 s.
- Modernos SRK ASC:
  - `KothaEtAl2020`: 0.01–8.0 s.
  - `BooreEtAl2020`: 0.01–10 s.
  - `HassaniAtkinson2020Asc`: 0.01–10 s.

GMPEs **eliminadas** de ASC_ALL por problemas previos de periodo:

- `AkkarCagnan2010` (error con SA(3.0))
- `AkkarEtAlRjb2014` (error con SA(5.0))

Con esta poda, todos los modelos de `ASC_ALL` cubren sin problema el rango 0.05–5.0 s.

### 2.3. Subduction Interface (SI_ALL)

Bloque `SI_ALL` (común a los tres árboles):

- Canadá SHM6 Interface:
  - `CanadaSHM6_Interface_AbrahamsonEtAl2015SInter`: 0.02–10.0 s.
  - `CanadaSHM6_Interface_AtkinsonMacias2009`: 0.05–10.0 s.
  - `CanadaSHM6_Interface_GhofraniAtkinson2014Cascadia`: 0.07–9.09 s.
  - `CanadaSHM6_Interface_ZhaoEtAl2006SInterCascadia`: 0.05–5.0 s.
- Modelos 2020 Interface:
  - `AbrahamsonGulerce2020SInter`, `KuehnEtAl2020SInter`, `ParkerEtAl2020SInter`, `SiEtAl2020SInter`: 0.01–10.0 s.

Todas las Interface cubren 0.05–5.0 s → **no hay conflicto** con los IMTs actuales.

### 2.4. Subduction IntraSlab (SLAB30_ALL y SLAB55_ALL)

Bloques `SLAB30_ALL` y `SLAB55_ALL` (idénticos en `gmmLT_GEM.xml`, `gmmLT_USGS.xml`, `gmmLT_SHM6.xml`):

- Canadá SHM6 InSlab30:
  - `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab30`: 0.02–10.0 s.
  - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`: **0.04–4.0 s** (límite superior 4 s).
  - `CanadaSHM6_InSlab_GarciaEtAl2005SSlab30`: 0.04–5.0 s.
  - `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia30`: 0.05–5.0 s.
- Canadá SHM6 InSlab55:
  - `CanadaSHM6_InSlab_AbrahamsonEtAl2015SSlab55`: 0.02–10.0 s.
  - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`: **0.04–4.0 s** (límite superior 4 s).
  - `CanadaSHM6_InSlab_GarciaEtAl2005SSlab55`: 0.04–5.0 s.
  - `CanadaSHM6_InSlab_ZhaoEtAl2006SSlabCascadia55`: 0.05–5.0 s.
- Modelos 2020 Slab (compartidos por SLAB30_ALL/SLAB55_ALL):
  - `AbrahamsonGulerce2020SSlab`, `KuehnEtAl2020SSlab`, `ParkerEtAl2020SSlab`, `SiEtAl2020SSlab`: 0.01–10.0 s.

**Únicos modelos problemáticos respecto a SA(5.0):**

- `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`
- `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`

Ambos solo están tabulados hasta 4.0 s.

---

## 3. Errores vistos y estado actual de los IMTs

### 3.1. Error previo con SA(0.01)

Se reportó un error del tipo:

```text
ValueError: SA(0.01) is out of the period range defined for [AtkinsonBoore2006Modified2011]
```

Actualmente, el fichero `gmmLT/IMT.ini` **ya no contiene** SA(0.01); el conjunto de IMTs empieza en SA(0.05). Con este cambio:

- Ninguna GMPE es llamada por debajo de 0.05 s.
- Todos los modelos SCC/ASC/Subducción relevantes tienen T_min ≤ 0.05 s, por lo que este tipo de error no puede reaparecer con la configuración actual.

### 3.2. Riesgo real con SA(5.0) en IntraSlab

Con los IMTs actuales (incluyendo SA(5.0)) y los bloques `SLAB30_ALL` / `SLAB55_ALL` tal como están:

- Para TRT = `Subduction IntraSlab30` o `Subduction IntraSlab55`, cuando se activa una de las GMPE Atkinson–Boore 2003 InSlab (`...Cascadia30/55`), una llamada a SA(5.0) está **fuera de su rango tabulado**.
- El error esperado sería del tipo:

```text
ValueError: SA(5.0) is out of the period range defined for [CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadiaXX]
```

Este riesgo existe en cualquier cálculo que use:

- Árboles con `SLAB30_ALL` / `SLAB55_ALL` (GEM, USGS, SHM6, y NBCC), **y**
- Un modelo de fuentes que incluya fuentes de tipo slab (SAM, CCA, partes de Canadá/Cascadia, etc.).

En XAF, como no hay actualmente fuentes slab, este conflicto no se manifiesta, pero el problema es real para otras regiones.

---

## 4. Opciones de tratamiento para SA(5.0) y las GMPE InSlab de Canadá

### 4.1. Opción 1 – Mantener SA(5.0) y podar las GMPE problemáticas

- **Acción:**
  - Eliminar de `SLAB30_ALL` y `SLAB55_ALL` las GMPE:
    - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30`
    - `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia55`
- **Efecto en el número de ramas:**
  - Antes:
    - Cada bloque (`SLAB30_ALL` y `SLAB55_ALL`) tiene 8 GMPE:
      - 4 Canadá SHM6 + 4 modelos 2020.
  - Después de la poda:
    - Cada bloque se queda con **7 GMPE**:
      - 3 Canadá SHM6 (`AbrahamsonEtAl2015`, `GarciaEtAl2005`, `ZhaoEtAl2006`) + 4 modelos 2020.
- **Pesos:**
  - Habrá que reajustar los `uncertaintyWeight` para que las 7 ramas de cada bloque vuelvan a sumar 1.0 (por ejemplo, pesos iguales 1/7 ≈ 0.142857 o manteniendo una relación familia Canadá vs 2020 similar a la actual).
- **Ventaja:**
  - Se puede mantener SA(5.0) sin riesgo de errores por rango en IntraSlab.
- **Inconveniente:**
  - Pierdes las GMPE Atkinson–Boore 2003 InSlab del conjunto IntraSlab30/55.

### 4.2. Opción 2 – Mantener las GMPE y ajustar los IMTs

- **Acción:**
  - Conservar las GMPE `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30/55`.
  - Ajustar los IMTs de forma que **no se pida SA(5.0)** en cálculos que involucren slab.
- **Posibles implementaciones prácticas:**
  1. **IMT global más corto:** quitar SA(5.0) de `gmmLT/IMT.ini` y trabajar con SA hasta 4.0 s para todos los cálculos que usen estos árboles.
  2. **Dos ficheros IMT distintos:**
     - `IMT_slab.ini` sin SA(5.0) (por ejemplo con IMTs hasta SA(4.0)), usado cuando el modelo de fuentes incluye slab.
     - `IMT_full.ini` con SA(5.0), usado sólo para cálculos sin slab o con árboles en los que no esté `CanadaSHM6_InSlab_AtkinsonBoore2003...`.
- **Ventaja:**
  - Se conserva el conjunto completo de GMPEs InSlab originales de Canadá SHM6.
- **Inconveniente:**
  - Pierdes SA(5.0) en los escenarios donde hay slab, o complicas el flujo de trabajo con múltiples ficheros de IMT.

---

## 5. Respuestas directas a las preguntas clave

1. **¿Voy a tener problemas con SA(5.0)?**  
   - Sí, **si** ejecutas cálculos con subducción IntraSlab (TRT = `Subduction IntraSlab30/55`) usando árboles que incluyen
     `CanadaSHM6_InSlab_AtkinsonBoore2003SSlabCascadia30/55` **y** pides SA(5.0).  
   - No habrá problema para SCC, ASC ni Interface con los IMTs actuales.

2. **Si quito esos GMPE, ¿con cuántos queda esa rama?**  
   - Cada uno de los bloques `SLAB30_ALL` y `SLAB55_ALL` pasa de **8 GMPE** a **7 GMPE**:
     - 3 Canadá SHM6 InSlab + 4 modelos 2020 InSlab.

3. **Si dejo esos GMPE, ¿cómo debo ajustar los IMT?**  
   - Debes asegurarte de **no pedir SA(5.0)** cuando uses modelos de fuente con slab junto con estos árboles.  
   - La forma más simple es quitar SA(5.0) de `IMT.ini` (quedarte hasta SA(4.0)), o bien mantener un segundo fichero de IMTs sin SA(5.0) para los cálculos con slab.

Este documento deja la auditoría preparada para que, en un siguiente paso, se decida explícitamente si se prefiere podar las GMPE problemáticas de IntraSlab o ajustar los IMTs (global o por tipo de cálculo).