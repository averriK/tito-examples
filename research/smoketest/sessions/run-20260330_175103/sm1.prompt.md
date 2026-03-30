## SLOTS

### SLOT 1: Metals ranked by melting point

All metals referenced in the KB are to be listed in descending order of melting point, from highest to lowest, with the corresponding melting-point value included for each entry. The expected output format is a ranked list.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 1 ("List the metals sorted by melting point from highest to lowest"). Full coverage of the requirement; no content invented.]

### SLOT 2: Highest-density metal and structural relevance

The metal in the KB with the highest density is to be identified, accompanied by a brief explanation of why high density matters for structural applications. The expected output format is flowing paragraphs.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 2 ("Describe briefly which metal has the highest density and why that matters for structural applications"). Both sub-parts - identification and practical relevance - are covered; the brevity instruction from "describe briefly" is preserved.]

### SLOT 3: Iron versus aluminum comparison

The key differences between iron and aluminum, as described in the KB, are to be summarized. The scope is limited to these two metals and their most salient contrasts. The expected output format is a short comparison.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE item 3 ("Summarize the key differences between iron and aluminum in a short comparison"). Scope restricted to the two named metals; format signal ("summarize," "short comparison") preserved.]

## CONSTRAINTS

- The output document must be written entirely in English.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 1 ("DOCUMENT IN ENGLISH"). This is an explicit document-wide language requirement.]

- All factual content must be drawn from the provided KB.
^[Confidence: HIGH, Rationale: Directly derived from TASK_FILE line 3 ("Using the KB provided"). This applies globally to all three work items as the designated evidence source.]
