# Structured Prompt: claude-flow swarm parameters investigation

## SLOTS

### SLOT 1: Verify implemented parameters
Look at `https://github.com/ruvnet/claude-flow` (v2.7.32, updated 2025-11-10), specifically the `/src/` directory source code. Check the CLI argument parser to determine what flags are actually implemented. Run `npx claude-flow@alpha swarm --help` if possible. Document ONLY parameters confirmed in the actual code.

### SLOT 2: Extract official example commands
Look at `README.md` in ruvnet/claude-flow and extract every example command with `npx claude-flow`. List only the flags shown in examples (like `--claude`, `--topology mesh`, `--max-agents 5`). Note that the project is in alpha and features may not work as advertised.

### SLOT 3: Search for real-world usage
Search GitHub for repos with `claude-flow` in their code (not just README), excluding ruvnet's own repos. Look for actual command invocations in scripts/CI/documentation. Previous search found ~20 repos mentioning claude-flow, but most are wrappers/frameworks, not users. Document ONLY commands you see actually executed, with repo links.

### SLOT 4: Evaluate relevance to TITO workflows
TITO workflows include: `retrieve` (PDF/DOCX → Markdown), `research` (KB+web investigation with citations), `review` (verify KB documents against external sources), `compile` (select verified content, generate bibliography), `audit` (consensus across multiple review outputs), and `enhance` (fill gaps in audited documents). TITO currently uses: `npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"`. Determine what other parameters (if any) should TITO add based on verified parameters from slots 1-3.

### SLOT 5: Produce final report
Create a report with:
1. **Verified parameters**: List with source code references or official example links
2. **Unknown/undocumented parameters**: Flags mentioned but not proven to work
3. **Repo usage**: Links to non-ruvnet repos that execute swarm commands (if any exist)
4. **TITO recommendation**: Should we add any parameters? Or keep it minimal?
5. **Confidence level**: High (seen in code), Medium (in docs), Low (inferred)

## CONSTRAINTS

- Do not recommend parameters unless you verify they're implemented in source code or official examples
- Do not infer "this workflow should use X topology" without evidence from actual usage
- Do not cite "best practices from repos" unless you link to actual repos using those practices
- Do not assume wiki documentation is accurate (it's broken according to the task)
- Do not trust the existing document `docs/SWARM_OPTIMIZATION.md` - it's fabricated
- Clearly separate "implemented" (seen in code) from "documented" (in README/docs) from "inferred" (assumed without evidence)
- Admit when evidence doesn't exist rather than making assumptions
- Everything stated must be verifiable by checking source code or running commands
