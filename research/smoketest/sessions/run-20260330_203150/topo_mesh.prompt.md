# Structured Prompt: topo_mesh

## SLOTS

### SLOT 1: Metals Ranked by Melting Point

A complete list of all metals found in the KB, sorted by melting point from highest to lowest. Each entry includes the metal name and its corresponding melting point value. Present as a sorted list.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 1 (line 4): "List the metals sorted by melting point from highest to lowest." The slot preserves the ranking task, descending sort order, and explicit list format signal without introducing additional requirements.]

### SLOT 2: Highest-Density Metal and Structural Relevance

Identification of the metal in the KB with the highest density, accompanied by a brief explanation of why high density is relevant to structural applications. Write in flowing paragraphs.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 2 (line 5): "Describe briefly which metal has the highest density and why that matters for structural applications." The slot captures both the identification component and the application-relevance explanation; the "briefly" qualifier is preserved through the flowing-paragraph format instruction.]

### SLOT 3: Iron versus Aluminum Comparison

A concise summary of the key differences between iron and aluminum, drawing on the properties available in the KB. Present as a short comparison.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 3 (line 6): "Summarize the key differences between iron and aluminum in a short comparison." The slot preserves the comparison scope (iron and aluminum only), the summarization intent, and the brevity requirement.]

## CONSTRAINTS

- The output document is written entirely in English.
- All slot responses draw evidence exclusively from the KB provided.

^[Confidence: HIGH, Rationale: The English-language constraint is stated explicitly in TASK_FILE line 1: "DOCUMENT IN ENGLISH." The KB-evidence constraint is stated explicitly in TASK_FILE line 3: "Using the KB provided." Both are document-wide requirements applicable to every slot; no additional constraints are inferred.]
