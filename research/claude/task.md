# Task: Investigate claude-flow swarm parameters for TITO optimization

## Context
TITO is a bash CLI that uses `npx claude-flow@alpha swarm` to orchestrate multi-agent workflows. We removed the `--sessions` parameter due to memory sharing issues (`.swarm/memory.db`). Now we need to determine what swarm parameters actually work and should be used.

## What the previous attempt failed at
1. **Invented recommendations** without verifying they work in practice
2. **Confused documentation** (available syntax) with **actual usage** (what people run)
3. **Made inferences** about what parameters to use for different workflows without evidence
4. **Claimed "evidence from repos"** when only official docs were found
5. **Created a comprehensive guide** (`docs/SWARM_OPTIMIZATION.md`) with made-up strategy/topology recommendations

## What you need to investigate

### 1. What parameters does `claude-flow swarm` actually accept?
- Look at: `https://github.com/ruvnet/claude-flow` (v2.7.32, updated 2025-11-10)
- Check: Source code in `/src/` directory, NOT wiki (wiki pages are broken)
- Find: CLI argument parser - what flags are implemented vs documented
- Verify: Run `npx claude-flow@alpha swarm --help` if possible
- Document: ONLY parameters you can confirm are in the actual code

### 2. What parameters does ruvnet recommend in official examples?
- Look at: `README.md` in ruvnet/claude-flow
- Extract: Every example command with `npx claude-flow`
- List: Only flags shown in examples (like `--claude`, `--topology mesh`, `--max-agents 5`)
- Note: Project is in alpha - features may not work as advertised

### 3. Do any public repos actually USE these parameters?
- Search GitHub for: Repos with `claude-flow` in their code (not just README)
- Exclude: ruvnet's own repos
- Look for: Actual command invocations in scripts/CI/documentation
- Found so far: ~20 repos mention claude-flow, but most are wrappers/frameworks, not users
- Document: ONLY commands you see actually executed, with repo links

### 4. What parameters are relevant to TITO's use case?
TITO workflows:
- `retrieve`: PDF/DOCX → Markdown conversion
- `research`: KB+web investigation with citations
- `review`: Verify KB documents against external sources
- `compile`: Select verified content, generate bibliography
- `audit`: Consensus across multiple review outputs
- `enhance`: Fill gaps in audited documents

TITO currently uses:
```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```

Question: What other parameters (if any) should TITO add?

## What NOT to do
- ❌ Don't recommend parameters unless you verify they're implemented
- ❌ Don't infer "this workflow should use X topology" without evidence
- ❌ Don't cite "best practices from repos" unless you link to actual repos
- ❌ Don't assume wiki documentation is accurate (it's broken)
- ❌ Don't trust my previous document `docs/SWARM_OPTIMIZATION.md` - it's fabricated

## Expected output
A report with:
1. **Verified parameters**: List with source code references or official example links
2. **Unknown/undocumented parameters**: Flags mentioned but not proven to work
3. **Repo usage**: Links to non-ruvnet repos that execute swarm commands (if any exist)
4. **TITO recommendation**: Should we add any parameters? Or keep it minimal?
5. **Confidence level**: High (seen in code), Medium (in docs), Low (inferred)

## Success criteria
- Everything you state can be verified by checking source code or running commands
- You clearly separate "implemented" from "documented" from "inferred"
- You admit when evidence doesn't exist rather than making assumptions
- The human can trust your report won't waste tokens on fabrications
