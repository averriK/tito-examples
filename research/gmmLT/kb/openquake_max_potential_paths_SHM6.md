# OpenQuake logic-tree path limit with gmmLT_SHM6

Este documento describe el problema encontrado al usar el árbol de GMPE `gmmLT_SHM6.xml` en combinación con árboles de fuentes complejos, y la solución aplicada mediante el parámetro `max_potential_paths`.

## Síntoma

Al ejecutar corridas que usan el árbol de intensidades `gmmLT_SHM6.xml` (por ejemplo `model/ZAF/run/shm6/job.ini` o `model/XAF/v2025.0.0/model/shm6/shm6.ini`), el motor de OpenQuake emite primero un *warning* relacionado con pesos dependientes de IMT en el árbol de GMPE y luego aborta con el siguiente error:

> ValueError: There are too many potential logic tree paths (23328): raise `max_potential_paths`, use sampling instead of full enumeration, or set use_rates=true

El cálculo funciona en algunas regiones (donde solo actúan TRTs como ASC/Subducción), pero falla en regiones donde la contribución de **Stable Shallow Crust (SCC)** es dominante (por ejemplo Sudáfrica), porque se activa el bloque completo de SCC del árbol SHM6.

## Causa técnica

1. El árbol `gmmLT_SHM6.xml` incluye, en el bloque SCC (`branchSetID="bs1"`), pesos que dependen del IMT:

   ```xml
   <logicTreeBranchSet uncertaintyType="gmpeModel" branchSetID="bs1"
                       applyToTectonicRegionType="SCC">
       <logicTreeBranch branchID="b11">
           <uncertaintyModel submodel='01'>CanadaSHM6_StableCrust_NGAEast</uncertaintyModel>
           <uncertaintyWeight>0.0757</uncertaintyWeight>
           <uncertaintyWeight imt="SA(0.05)">...</uncertaintyWeight>
           <uncertaintyWeight imt="SA(1.0)">...</uncertaintyWeight>
           ...
       </logicTreeBranch>
       ...
   </logicTreeBranchSet>
   ```

   Esto hace que, conceptualmente, los pesos de las ramas SCC varíen con el IMT.

2. El árbol de fuentes (`ssmLT.xml`) utilizado en ZAF/XAF tiene múltiples niveles de ramas (regiones, escenarios, etc.). Cuando se combina con el árbol completo `gmmLT_SHM6.xml`, el número potencial de caminos del árbol lógico es:

   \[
   N_{paths} = N_{paths}^{ssmLT} \times N_{paths}^{gmmLT\_SHM6} = 23\,328
   \]

3. El motor valida este número frente al parámetro global `max_potential_paths`. Con el valor por defecto (15\,000 en la versión usada), 23\,328 caminos superan el límite y se lanza el `ValueError` anterior, con el mensaje explícito de "raise `max_potential_paths`".

4. El *warning* sobre pesos dependientes de IMT en SCC es independiente del límite de caminos. Indica que, si se usa `number_of_logic_tree_samples > 0`, el motor no puede construir un conjunto único de realizaciones coherentes para todos los IMTs y, por tanto, ignora los pesos específicos de IMT y usa solo los pesos globales. Este comportamiento no impide el cálculo, pero explica por qué la configuración SHM6 no es plenamente compatible con sampling de GMPE.

## Solución aplicada

La solución adoptada fue **elevar el límite de caminos permitidos** mediante el parámetro `max_potential_paths` en el bloque `[general]` de los archivos `job.ini` afectados. Por ejemplo, en `model/ZAF/run/shm6/job.ini`:

```ini
[general]
description = South Deep Mine (S2J2E). Vs=760 m/s. Classical. ZAF(SCC)/SHM6
calculation_mode = classical
max_potential_paths = 50000
random_seed = 23
concurrent_tasks = 16
```

Con `max_potential_paths = 50\,000`:

- El número potencial de caminos reportado por el engine (23\,328) queda por debajo del límite y el `ValueError` desaparece.
- La estructura del árbol de GMPE `gmmLT_SHM6.xml` no necesita modificarse.
- El cálculo vuelve a ejecutarse correctamente tanto en regiones dominadas por ASC/subducción como en regiones SCC.

El mismo ajuste se puede aplicar a otros `.ini` que utilicen `gmmLT_SHM6.xml`, por ejemplo:

- `model/ZAF/v2025.0.0/model/shm6/job.ini`
- `model/XAF/v2025.0.0/model/shm6/shm6.ini`

## Notas sobre sampling y pesos dependientes de IMT

El aumento de `max_potential_paths` resuelve exclusivamente el problema de exceso de caminos. El *warning* sobre "IMT-dependent weights" en el bloque SCC seguirá apareciendo si se usa `number_of_logic_tree_samples > 0` en `[logic_tree]`, porque el motor no puede muestrear de forma coherente caminos distintos por IMT.

En la práctica, esto implica que:

- Si se quiere preservar exactamente el esquema de pesos dependientes de IMT definido en SHM6, es más consistente trabajar sin sampling de GMPE (enumeración completa) y con `max_potential_paths` suficientemente alto.
- Si se acepta que los pesos SCC se apliquen solo de forma global (sin dependencia estricta de IMT), se puede mantener `number_of_logic_tree_samples > 0`; el motor ignorará internamente los `uncertaintyWeight imt="..."` y utilizará el peso global de cada rama.

En ambos casos, para corridas SHM6 con `gmmLT_SHM6.xml` y `ssmLT.xml` complejos es recomendable fijar explícitamente `max_potential_paths` en un valor superior al número de caminos reportado en el mensaje de error (en este caso, mayor que 23\,328).