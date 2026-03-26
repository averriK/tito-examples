# Structured Research Prompt: Iduapriem Seismic Record Selection Methodology

## CONTEXT

The knowledge base document (kb/) contains a Probabilistic Seismic Hazard Analysis (PSHA) report prepared by WSP. The report consists of two parts: chapters 1-7 provide the PSHA methodology and hazard results (background context), while chapter 8.0 establishes criteria for selecting seismic record suites. The objective is to develop a detailed methodology for selecting seismic records (accelerograms) that can be applied to other sites based on the approach described in the WSP report.

## SLOTS

### SLOT 1: Executive summary of seismic record selection for site compatibility

Provide an executive summary explaining how seismic records were selected to be compatible with the project site. The summary should describe the overall selection methodology, criteria used, and approach taken to ensure site compatibility based on the PSHA results.

### SLOT 2: Scaling methodology across period ranges

Explain how the seismic records were scaled across different period ranges. Describe which period ranges were considered, the specific scaling approach or factors employed, and the methodology for applying these scaling procedures to different structural periods of interest.

### SLOT 3: PEER API spectral matching equations and scaling procedures

If spectral matching was performed through the PEER Ground Motion Database API, identify and explain the specific equations employed to adjust a suite of seismic records through spectral matching. Describe how these equations affect the structural periods of each spectrum and explain how records are scaled for spectral matching purposes through the API methodology.

### SLOT 4: Spectral matching method equations with amplification factors

Provide the mathematical equations for the spectral matching method. Explain the approach for determining $N$ amplification factors (one per seismic record) such that, given $N$ seismic records with $M$ spectral ordinates $Sa(T_n)$, the weighted sum of the scaled spectra produces the target average spectrum. Include the mathematical formulation showing how these amplification factors are calculated.

### SLOT 5: Baker methodology for additional intensity measures in seismic selection

Expand on the methodology from Baker's paper mentioned in the report regarding the incorporation of additional intensity measures (IMs) for seismic record selection. Provide a detailed explanation of this methodology including relevant equations in LaTeX format (using $...$ for inline math and $$...$$ for display equations).

## CONSTRAINTS

- All responses and analysis generated from this task must be written in English only.
- Mathematical expressions must use LaTeX format: inline expressions with $...$ and display equations with $$...$$.
- All claims should be supported by citations to the KB document or external authoritative sources.
- Each answer should reference the specific chapter or section of the WSP report where the methodology is described when applicable.
- Maintain professional academic tone throughout.
