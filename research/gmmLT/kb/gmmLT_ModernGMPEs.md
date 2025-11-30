# GMPE_Modern: árbol lógico de GMPEs modernas para XAF

Este documento describe el árbol lógico de modelos de atenuación **GMPE_Modern** definido en `model/usgs/gmmLT_TEST.xml` y referenciado también desde `model/shm6/gmmLT_TEST.xml` para el modelo XAF.

El objetivo de este árbol es explorar GMPEs modernas para las tres grandes familias de regiones tectónicas (Stable Shallow Crust, Active Shallow Crust y Subduction) sin reutilizar los modelos ya presentes en `gmmLT_USGS.xml` / `gmmLT_USGS.xml` (SHM6).

## 1. Ficheros y `logicTreeID`

- Fichero USGS: `model/usgs/gmmLT_TEST.xml`
- Fichero SHM6: `model/shm6/gmmLT_TEST.xml` (contenido lógico idéntico al USGS)
- Identificador de árbol: `logicTreeID="GMPE_Modern"`

## 2. Selección de GMPEs por región tectónica

### 2.1. Stable Shallow Crust

Branching level `bl_StableShallowCrust`, branch set `StableShallowCrust`, `applyToTectonicRegionType="Stable Shallow Crust"`.

Modelos incluidos (peso 1/3 c/u):

- `ESHM20Craton`
- `RietbrockEdwards2019Mean`
- `ShahjoueiPezeshk2016`

En comparación con `gmmLT_USGS.xml` / `gmmLT_USGS.xml` (SHM6), estos cuatro modelos **no aparecen** allí. Los modelos originales para Stable Shallow Crust en esos árboles son exclusivamente la familia `NGAEastUSGSSammons*` y `NGAEastUSGSSeed*`.

### 2.2. Active Shallow Crust

Branching level `bl_ActiveShallowCrust`, branch set `ActiveShallowCrust`, `applyToTectonicRegionType="Active Shallow Crust"`.

Modelos incluidos (peso 0.25 c/u):

- `KothaEtAl2020`
- `Weatherill2024ESHM20AvgSA`
- `BooreEtAl2020`
- `HassaniAtkinson2020Asc`

Ninguno de estos modelos está presente en `gmmLT_USGS.xml` ni en `gmmLT_USGS.xml` (SHM6), donde las GMPEs activas son únicamente las variantes `CanadaSHM6_ActiveCrust_*` (Abrahamson 2014, Boore 2014, Campbell–Bozorgnia 2014, Chiou–Youngs 2014).

### 2.3. Subduction Interface

Branching level `bl_SubductionInterface`, branch set `SubductionInterface`, `applyToTectonicRegionType="Subduction Interface"`.

Modelos incluidos (peso 0.25 c/u):

- `AbrahamsonGulerce2020SInter`
- `KuehnEtAl2020SInter`
- `ParkerEtAl2020SInter`
- `SiEtAl2020SInter`

En los árboles `gmmLT_USGS.xml` originales, las GMPEs de subducción interface son las variantes `CanadaSHM6_Interface_*`. Ninguno de los cuatro modelos 2020 anteriores aparece allí, por lo que son todos **nuevos** respecto de los árboles existentes.

### 2.4. Subduction IntraSlab30 / IntraSlab55

Branching levels `bl_SubductionIntraSlab30` y `bl_SubductionIntraSlab55`, branch sets `SubductionIntraSlab30` y `SubductionIntraSlab55`, con `applyToTectonicRegionType="Subduction IntraSlab30"` y `"Subduction IntraSlab55"` respectivamente.

En ambos casos se usan los mismos cuatro modelos (peso 0.25 c/u):

- `AbrahamsonGulerce2020SSlab`
- `KuehnEtAl2020SSlab`
- `ParkerEtAl2020SSlab`
- `SiEtAl2020SSlab`

Los árboles `gmmLT_USGS.xml` existentes usan exclusivamente la familia `CanadaSHM6_InSlab_*` para `Subduction IntraSlab30` y `Subduction IntraSlab55`, por lo que estos cuatro modelos 2020 también son **nuevos** allí.

**Resumen:** Todos los modelos listados en `gmmLT_TEST.xml` (`GMPE_Modern`) son nuevos respecto de `gmmLT_USGS.xml` (tanto la variante USGS como la SHM6). No hay solapamiento de nombres de GMPEs entre el árbol de prueba moderno y los árboles de producción actuales.

## 3. Rango de periodos de cada GMPE (hazardlib local)

La siguiente información se ha obtenido inspeccionando el `CoeffsTable` de cada GMPE en la instalación local de `openquake.hazardlib` (`/Users/averrik/openquake/...`). Se indica el rango de periodos **SA(T)** tabulados y, en particular, la compatibilidad con las ordenadas espectrales del `job.ini` actual:

```text
IMTs de job.ini
PGA,
SA(0.05), SA(0.10), SA(0.15), SA(0.20), SA(0.25), SA(0.30),
SA(0.50), SA(1.00), SA(2.00), SA(3.00), SA(4.00), SA(5.00)
```

### 3.1. Stable Shallow Crust

- **ESHM20Craton**  
  - SA(T) tabulados: desde T = 0.01 s hasta T = 10 s.  
  - Cubre **todas** las ordenadas de `job.ini` (0.05–5.0 s).

- **RietbrockEdwards2019Mean**  
  - SA(T) tabulados: desde T ≈ 0.03 s hasta T = 5 s.  
  - Todas las SA(T) del `job.ini` (sin SA(0.075)) están dentro del rango 0.05–5.0 s, por lo que pueden evaluarse mediante interpolación interna de `hazardlib`.

- **ShahjoueiPezeshk2016**  
  - SA(T) tabulados: 0.01–10 s.  
  - Cubre **todas** las ordenadas de `job.ini`.


### 3.2. Active Shallow Crust

**Nota sobre el parámetro de sitio `region` (eshm20_region)**  
Algunos modelos ESHM20 de corteza activa (en particular `Weatherill2024ESHM20AvgSA`) requieren, además de `vs30` y `vs30measured`, un parámetro entero `region` (llamado en los artículos `eshm20_region`). Según la implementación de `KothaEtAl2020ESHM20`/`Weatherill2024ESHM20AvgSA` en `hazardlib`:

- `region` es un entero entre 0 y 5.  
- 1–5 representan las cinco "residual attenuation regions" de Europa definidas en ESHM20 (subregiones europeas con distinta atenuación).  
- 0 significa "valor por defecto" (sin aplicar una corrección regional específica).  

En este modelo XAF (Longonjo, África), el `job.ini` fija `region = 0`, es decir, usamos el comportamiento por defecto del modelo sin asignarlo a ninguna región europea concreta.

- **KothaEtAl2020**  
  - SA(T) tabulados: 0.01–8 s.  
  - **NO** tiene coeficientes exactamente en T = 0.075 s (usa 0.07 s en la tabla).  
  - Cubre todas las demás ordenadas del `job.ini` (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.50, 1–5 s).

- **Weatherill2024ESHM20AvgSA**  
  - Hereda la misma tabla base de KothaEtAl2020ESHM20.  
  - SA(T): 0.01–8 s.  
  - Igual que KothaEtAl2020, **no** tiene T = 0.075 s explícito; cubre el resto de ordenadas del `job.ini`.

- **BooreEtAl2020**  
  - SA(T) tabulados: 0.01–10 s.  
  - Cubre **todas** las ordenadas de `job.ini`.

- **HassaniAtkinson2020Asc**  
  - SA(T) tabulados: 0.01–10 s, con una malla densa de periodos.  
  - Todas las SA(T) del `job.ini` (sin SA(0.075)) caen dentro de ese rango y se pueden evaluar mediante interpolación de `CoeffsTable`.

- **AristeidouEtAl2024Geomean**  
  - En la versión actual de `hazardlib` instalada, este modelo **no define** coeficientes estándar para SA(T); por eso se ha decidido **no incluirlo** en el árbol `GMPE_Modern`.

### 3.3. Subduction Interface e IntraSlab

Para los modelos de subducción (interface e intraslab), las cuatro GMPEs 2020 comparten prácticamente el mismo rango de periodos:

- **AbrahamsonGulerce2020SInter / SSlab**  
- **KuehnEtAl2020SInter / SSlab**  
- **ParkerEtAl2020SInter / SSlab**  
- **SiEtAl2020SInter / SSlab**  

En todos los casos:

- SA(T) tabulados: 0.01–10 s.  
- Cubre **todas** las ordenadas de `job.ini` (0.05–5.0 s), tanto para interface como para slab (30 y 55 km).

## 4. Compatibilidad global con el `job.ini` actual

El `job.ini` de XAF (`model/usgs/job.ini`) define el mismo conjunto de ordenadas espectrales para **todas** las regiones tectónicas. Desde el punto de vista de `hazardlib`, un árbol lógico sólo es "limpio" si **todas** las GMPEs usadas en cada región pueden evaluar todas las IMTs pedidas.

Con el conjunto **actualizado** de modelos de `GMPE_Modern` (sin `DrouetBrazil2015`, sin `AristeidouEtAl2024Geomean` y sin SA(0.075) en el `job.ini`):

- En **Stable Shallow Crust**:
  - `ESHM20Craton`, `RietbrockEdwards2019Mean` y `ShahjoueiPezeshk2016` cubren el rango 0.05–5.0 s (la compatibilidad a periodos intermedios se consigue vía interpolación interna de `hazardlib`).
- En **Active Shallow Crust**:
  - `KothaEtAl2020`, `Weatherill2024ESHM20AvgSA`, `BooreEtAl2020` y `HassaniAtkinson2020Asc` cubren igualmente 0.05–5.0 s (de nuevo con interpolación entre los periodos tabulados en sus tablas).  
- En **Subduction Interface / IntraSlab30 / IntraSlab55**:
  - Todas las GMPEs 2020 propuestas (`AbrahamsonGulerce2020*`, `KuehnEtAl2020*`, `ParkerEtAl2020*`, `SiEtAl2020*`) cubren sin problema el rango 0.05–5.0 s.

Por tanto, con estas modificaciones (eliminación de `DrouetBrazil2015` y `AristeidouEtAl2024Geomean` y supresión de SA(0.075) en el `job.ini`), el árbol `GMPE_Modern` queda configurado de forma consistente con las ordenadas espectrales actualmente pedidas.

Este documento deja explícito qué modelos son nuevos respecto a los árboles USGS/SHM6 existentes y cuáles son las limitaciones de periodo de cada uno, de forma que se pueda decidir cómo llegar a una versión "limpia" del árbol GMPE_Modern (ajustando IMTs, ajustando el conjunto de GMPEs, o ambas cosas).