# Research Task – Zotero smoke test

## Questions

1. Realiza un **smoke test de mi servidor Zotero MCP** usando claude-flow.
2. Usa UNA sola query corta para todo el experimento, por ejemplo:
   "probabilistic seismic hazard analysis"
3. Para esa query:
   - Haz un pase externo normal (WebSearch/WebFetch).
   - En paralelo, consulta mi biblioteca Zotero usando las herramientas del
     servidor Zotero para obtener candidatos.
4. El objetivo principal es:
   - Recuperar hasta 3 ítems desde Zotero que parezcan relevantes.
   - Para cada ítem, listar:
     - Zotero key
     - Título limpio
     - Año
     - Identificador preferido (DOI si existe, si no URL)
   - Añadir en el cuerpo al menos una oración explicando por qué es relevante.

## Output format

1. Escribe un breve texto de 2–3 párrafos sobre el estado del arte del tema
   de la query, usando citas token:
   - [WEB:...], [DOI:...], [ARXIV:...], [ZOTERO:<key>]
2. Añade al final una sección:

   ## ZOTERO SMOKE REPORT

   - Lista en tabla o lista numerada los ítems recuperados de Zotero con:
     - [ZOTERO:<key>]
     - Título
     - Año
     - DOI o URL preferido

## Constraints

- No hace falta usar en serio el KB; se puede ignorar el contenido de kb/.
- El objetivo es **verificar que Zotero MCP está accesible desde claude-flow**,
  no escribir una revisión exhaustiva.
- No inventes citas: solo usa DOIs/URLs que vengan de Web o Zotero.
