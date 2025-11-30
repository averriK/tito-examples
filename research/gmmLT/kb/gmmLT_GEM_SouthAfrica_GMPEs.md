# GMPEs GEM para África (NAF, WAF, SSA, ZAF)

Este documento resume los modelos de atenuación (GMPEs) empleados en los árboles lógicos **GEM originales** para las regiones africanas NAF, WAF, SSA y ZAF en este repositorio, usando los ficheros de entrada versionados:

- NAF: `/Users/averrik/kashimaDB/openquake/model/NAF/v2017.1.1/in/gmmLT.xml`
- WAF: `/Users/averrik/kashimaDB/openquake/model/WAF/v2018.1.0/in/gmmLT.xml`
- SSA: `/Users/averrik/kashimaDB/openquake/model/SSA/v2018.0.1/in/gmmLT.xml`
- ZAF: `/Users/averrik/kashimaDB/openquake/model/ZAF/v2018.1.0/in/gmmLT.xml`

El objetivo es obtener **(1)** el listado unificado de GMPEs usados en estos árboles GEM de África y **(2)**, para cada GMPE, la región tectónica para la que fue calibrado originalmente (Active Shallow Crust vs Stable Continental/Stable Shallow Crust), junto con un indicador del rango de periodos SA(T) disponible en la `hazardlib` local.

La asignación de región tectónica se ha obtenido a partir de `DEFINED_FOR_TECTONIC_REGION_TYPE` en la `hazardlib` local, salvo en el caso de `NRCan15SiteTerm`, donde se ha inferido a partir de la GMPE subyacente (`PezeshkEtAl2011NEHRPBC`).

## 1. Lista de GMPEs y región de calibración

### 1.1. Modelos para Active Shallow Crust (ASC)

Estos modelos están calibrados para corteza activa / Active Shallow Crust. Aparecen en los árboles GEM originales de NAF, WAF, SSA y/o ZAF.

- **AbrahamsonEtAl2014**  
  - **Región de calibración:** Active Shallow Crust.  
  - **Uso en GEM África:** sólo en ZAF (`.../ZAF/v2018.1.0/in/gmmLT.xml`).

- **AkkarCagnan2010**  
  - **Región de calibración:** Active Shallow Crust.  
  - **Uso en GEM África:** sólo en ZAF (`.../ZAF/v2018.1.0/in/gmmLT.xml`).

- **AkkarEtAlRjb2014**  
  - **Región de calibración:** Active Shallow Crust.  
  - **Uso en GEM África:** aparece en los árboles GEM de NAF y SSA (`.../NAF/v2017.1.1/in/gmmLT.xml`, `.../SSA/v2018.0.1/in/gmmLT.xml`).

- **ChiouYoungs2014**  
  - **Región de calibración:** Active Shallow Crust.  
  - **Uso en GEM África:** se utiliza en NAF, SSA y ZAF.

### 1.2. Modelos para Stable Continental / Stable Shallow Crust (SCC)

Estos modelos están diseñados para corteza estable (Stable Continental/Stable Shallow Crust) y aparecen en los árboles GEM originales de NAF, WAF y SSA.

- **AtkinsonBoore2006Modified2011**  
  - **Región de calibración:** Stable Shallow Crust (CEUS / corteza estable).  
  - **Uso en GEM África:** se usa en NAF, SSA y WAF.

- **NRCan15SiteTerm**  
  - **Región de calibración:** Stable Continental Crust (a través de la GMPE `PezeshkEtAl2011NEHRPBC`, pensada para CEUS).  
  - **Uso en GEM África:** aparece como `uncertaintyModel` en NAF, SSA y WAF, siempre asociado a `PezeshkEtAl2011NEHRPBC`.  
  - En `hazardlib` este identificador representa el término de sitio NRCan para esa GMPE estable; dado su origen, se clasifica aquí como SCC.

## 2. Rangos de periodos SA(T) en hazardlib

A partir de las tablas de coeficientes (`CoeffsTable`) en la instalación local de `openquake.hazardlib`, los rangos de periodos SA(T) disponibles para cada GMPE son:

### 2.1. Modelos ASC

- **AbrahamsonEtAl2014**  
  - SA(T) tabulados desde **0.01 s** hasta **10 s**.  
  - Incluye explícitamente: 0.01, 0.02, 0.03, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.75, 1.0, 1.5, 2.0, 3.0, **4.0**, **5.0**, 6.0, 7.5, 10.0.

- **AkkarCagnan2010**  
  - SA(T) tabulados desde **0.01 s** hasta **10 s**.  
  - Incluye explícitamente: 0.01–0.06, 0.075, 0.09, 0.10, 0.12, 0.15, 0.17, 0.20, 0.24, 0.25, 0.30, 0.36, 0.40, 0.46, 0.50, 0.60, 0.75, 0.85, 1.0, 1.5, 2.0, 3.0, **4.0**, **5.0**, 7.5, 10.0.

- **AkkarEtAlRjb2014**  
  - SA(T) tabulados desde **0.01 s** hasta **4 s** (no tiene periodos más largos).  
  - Malla muy densa entre 0.01 y **4.0 s**; 4.0 s es su periodo máximo.

- **ChiouYoungs2014**  
  - SA(T) tabulados desde **0.01 s** hasta **10 s**.  
  - Incluye explícitamente: 0.01–0.05, 0.075, 0.10, 0.12, 0.15, 0.17, 0.20, 0.25, 0.30, 0.40, 0.50, 0.75, 1.0, 1.5, 2.0, 3.0, **4.0**, **5.0**, 7.5, 10.0.

### 2.2. Modelos SCC

- **AtkinsonBoore2006Modified2011**  
  - SA(T) tabulados desde **0.01 s** hasta **10 s**.  
  - Incluye una malla fina de periodos cortos (0.01–0.1 s) y largos: 4.0, **5.0**, 7.5, 10.0 s.

- **NRCan15SiteTerm**  
  - SA(T) tabulados desde **0.01 s** hasta **10 s**.  
  - Incluye explícitamente: 0.01–0.06, 0.075, 0.09, 0.10, 0.12, 0.15, 0.17, 0.20, 0.24, 0.25, 0.30, 0.36, 0.40, 0.46, 0.50, 0.60, 0.75, 0.85, 1.0, 1.5, 2.0, 3.0, **4.0**, **5.0**, 7.5, 10.0.

## 3. GMPE limitantes respecto a periodos largos (4–5 s)

- Todos los modelos listados tienen tablas SA(T) explícitas que llegan al menos hasta **4.0 s** y, en la mayoría de los casos, hasta **5.0 s** y más allá.  
- `AkkarEtAlRjb2014` es el más "restrictivo" en términos de periodo máximo: llega hasta **4.0 s**, pero **no** incluye nodos por encima de 4 s (no tiene 5 s en las tablas).  
- Los modelos restantes (`AbrahamsonEtAl2014`, `AkkarCagnan2010`, `ChiouYoungs2014`, `AtkinsonBoore2006Modified2011`, `NRCan15SiteTerm`) soportan sin problema T = 4–5 s.

En consecuencia, si se arma un árbol lógico combinado `gmmLT_GEM.xml` que use este conjunto de GMPEs y se quiere pedir ordenadas hasta **4–5 s**, el único modelo a vigilar especialmente es `AkkarEtAlRjb2014` (llega bien a 4 s, pero no a 5 s). El resto de modelos cubren 5 s sin necesidad de extrapolación.

## 4. Resumen consolidado

Agrupando por tipo de región de calibración, para los árboles GEM originales de **NAF, WAF, SSA y ZAF**:

- **Active Shallow Crust (ASC)**:  
  `AbrahamsonEtAl2014`, `AkkarCagnan2010`, `AkkarEtAlRjb2014`, `ChiouYoungs2014`.

- **Stable Continental / Stable Shallow Crust (SCC)**:  
  `AtkinsonBoore2006Modified2011`, `NRCan15SiteTerm` (vinculado a `PezeshkEtAl2011NEHRPBC`).

Este listado refleja **qué GMPEs** ha utilizado GEM en los árboles lógicos originales para NAF, WAF, SSA y ZAF, y **para qué tipo de región tectónica fueron calibrados originalmente**, independientemente de cómo se combinen posteriormente en modelos derivados (p.ej. XAF).
