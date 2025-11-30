# STRUCTURED PROMPT

## SLOTS

### SLOT 1: Context Summary from Introduction
Review the introduction.md document in the kb folder. Read and understand the context. Prepare a compact bullet point or paragraph that summarizes the problem and the motivation.

### SLOT 2: Benchmarking Analysis Summary
Review the results comparison chapter that compares SRK values (unusually high) with values obtained from other sources. The SRC PSHA model is well-made and follows state-of-the-art rules. The fundamental hypothesis is that PGA is influenced by incorrect characterization of parameters and epistemic models of the Reitfontein Fault. Prepare a compact bullet point or paragraph that summarizes the most important points of the benchmarking analysis, emphasizing differences between SRC values and SRK/GEM reference value ranges. Do not detail the numbers. Do not repeat values already detailed in that chapter. Only summarize them compactly comparing ranges.

### SLOT 3: Reitfontein Fault Characterization Issues
Review the reitfointein.md chapter, which contains the rationale for problems with hypotheses made for the Reitfontein fault. The main problem is that this fault is apparently paleoseismic and should not have "influence" on return periods less than 10,000 years. Prepare a compact bullet point or paragraph that summarizes the main deficiencies in the epistemic characterization of the Reitfontein fault. Do not repeat what the reitfontein.md chapter already says. Summarize this in key points that have impact on PGA and PSHA.

### SLOT 4: Corrective Measures and Recommendations
Based on the deficiencies identified in SLOT 3 regarding Reitfontein fault characterization, investigate if the following correction measures are valid: Eliminate the Mmax = 7.2 value from logic tree branches or assign it a very low weight? Correct Gutenberg-Richter recurrence parameters, particularly a-, so they are consistent with Mmax values of each branch? Is it possible to use the Andersen & Luco methodology to correct GR recurrence? Prepare a compact bullet point or paragraph that proposes recommendations based on the weaknesses summarized in SLOT 3 that allow correcting the Hazard. Do not focus on recommendations about slip rate or classification of the fault as neotectonic or paleoseismic. Focus on recommendations that explain how to fix the hazard, using different branches and weights of logic trees for this fault.

## CONSTRAINTS

- Language: ENGLISH
- Output format: Compact bullet points or compact paragraphs for each slot
- Do not repeat detailed numbers or values already present in source documents
- Focus on summarizing and comparing ranges rather than listing specific values
- Recommendations should focus on hazard correction through logic tree modifications, not on slip rate or fault classification aspects
