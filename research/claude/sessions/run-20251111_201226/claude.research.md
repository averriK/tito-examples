# Investigation Report: claude-flow swarm Parameters for TITO Optimization

## Executive Summary

This investigation examined claude-flow v2.7.32 to determine verified CLI parameters for the `swarm` command and provide evidence-based recommendations for TITO workflows. The investigation revealed a significant gap between documented parameters and verified real-world usage, with limited evidence of non-ruvnet repositories using claude-flow swarm commands.

---

## 1. Verified Parameters (HIGH CONFIDENCE)

These parameters are confirmed through `npx claude-flow@alpha swarm --help` output:

| Parameter | Type | Description | Source |
|-----------|------|-------------|--------|
| `--strategy` | string | Execution strategy: research, development, analysis, testing, optimization, maintenance | CLI help output |
| `--mode` | string | Coordination mode: centralized, distributed, hierarchical, mesh, hybrid | CLI help output |
| `--max-agents` | number | Maximum number of agents (default: 5) | CLI help output |
| `--parallel` | boolean | Enable parallel execution (2.8-4.4x speed improvement) | CLI help output |
| `--monitor` | boolean | Real-time swarm monitoring | CLI help output |
| `--background` | boolean | Run in background with progress tracking | CLI help output |
| `--claude` | boolean | Open Claude Code CLI | CLI help output |
| `--executor` | boolean | Use built-in executor instead of Claude Code | CLI help output |
| `--analysis` | boolean | Enable analysis/read-only mode (no code changes) | CLI help output |
| `--read-only` | boolean | Alias for --analysis | CLI help output |

**Evidence**: Direct execution of `npx claude-flow@alpha swarm --help` on 2025-11-11 [WEB:cli_help_output]

---

## 2. Parameters in Official Examples (MEDIUM CONFIDENCE)

These parameters appear in ruvnet/claude-flow README.md examples:

### From README Examples:

```bash
# Example 1: Basic swarm with Claude integration
npx claude-flow@alpha swarm "build REST API with authentication" --claude

# Example 2: Swarm initialization
npx claude-flow@alpha swarm init --topology mesh --max-agents 5

# Example 3: Session continuation
npx claude-flow@alpha swarm "Add password reset" --continue-session
```

**Additional parameters found in examples:**
- `--topology` (values: mesh, hierarchical, ring, star) - Used with `swarm init`
- `--continue-session` - Allows continuing previous session
- `--namespace` - Mentioned in memory store examples

**Evidence**: [WEB:https://github.com/ruvnet/claude-flow README.md]

**Note**: The `--topology` parameter appears only in `swarm init` context, not in standard `swarm "objective"` commands. The relationship between `swarm init` and `swarm "task"` is unclear from documentation.

---

## 3. Unknown/Undocumented Parameters

### Parameters Removed or Deprecated:
- `--sessions` - Removed by TITO maintainers due to memory sharing issues with `.swarm/memory.db`

### Parameters Mentioned But Unverified:
None found beyond those listed in sections 1-2.

---

## 4. Real-World Repository Usage (LOW CONFIDENCE)

### Search Results:
Conducted GitHub searches for non-ruvnet repositories using `claude-flow swarm` commands:

**Query 1**: `"claude-flow swarm" site:github.com -site:github.com/ruvnet`
- **Result**: All results still pointed to ruvnet/claude-flow repository
- **Conclusion**: No verified external usage found

**Query 2**: `"npx claude-flow" swarm filetype:sh OR filetype:bash site:github.com`
- **Result**: Web search error/unavailable

**Repository Statistics**:
- ruvnet/claude-flow: 9.6k stars, 1.3k forks [WEB:https://github.com/ruvnet/claude-flow]
- Despite high engagement, minimal evidence of actual production usage outside official examples

### External Tutorial Examination:

**Source**: Deeplearning.fr tutorial [WEB:https://deeplearning.fr/claude-flow-the-complete-beginners-guide-to-ai-powered-development/]

Commands shown:
```bash
./claude-flow swarm "build, test, and deploy my application"
./claude-flow sparc run coder "implement user authentication"
./claude-flow sparc run architect "design microservice architecture"
./claude-flow sparc tdd "create test suite for API"
./claude-flow start --ui --port 3000
```

**Observation**: These examples use local `./claude-flow` (cloned repo) rather than `npx claude-flow@alpha`, suggesting different usage pattern than TITO's approach.

### GitHub Issues Analysis:

**Issue #510**: "Claude-Flow Swarm Command Works But Lacks Headless/Production Support"
- Confirms basic command works: `npx claude-flow@alpha swarm "Task"`
- Reports failures in headless/production environments
- Testing data: 29.2 seconds execution, 2,239 tokens, 5 AI tasks, 440 lines of code, ~$0.02 per run
- **Critical finding**: 2-minute Bash timeout conflicts with claude-flow's 120-minute internal timeout
- Commands shown: `claude-flow swarm "simple task" --max-agents 5` (conservative), `--max-agents 10` (medium), `--max-agents 15 --strategy development` (complex)

[WEB:https://github.com/ruvnet/claude-flow/issues/510]

**Issue #59**: "Claude-Flow v1.0.70 Swarm Timeout"
- Reports timeout issues with swarm execution
[WEB:https://github.com/ruvnet/claude-flow/issues/59]

**Issue #564**: "require is not defined" error with version 2.0.0-alpha.83
- Execution failures when spawning Claude Code
- Falls back to built-in executor
[WEB:https://github.com/ruvnet/claude-flow/issues/564]

---

## 5. Source Code Investigation

### Attempted Access:
- `/src/cli/swarm.js` - 404 error
- `/src/terminal/claude-flow.ts` - 404 error
- `/bin/claude-flow.js` - Found, but contains only runtime dispatcher, not parameter definitions

**Conclusion**: Could not access source code files that define CLI parameter parsing. The project structure suggests parameters are defined elsewhere in the TypeScript source, but files were inaccessible via raw.githubusercontent.com.

**Implication**: Cannot verify parameter implementation at source code level. Must rely on CLI help output as definitive reference.

---

## 6. TITO Use Case Analysis

### Current TITO Implementation:
```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```

### TITO Workflows:
1. **retrieve**: PDF/DOCX → Markdown conversion
2. **research**: KB+web investigation with citations
3. **review**: Verify KB documents against external sources
4. **compile**: Select verified content, generate bibliography
5. **audit**: Consensus across multiple review outputs
6. **enhance**: Fill gaps in audited documents

### Parameter Relevance Assessment:

| Parameter | TITO Relevance | Justification |
|-----------|----------------|---------------|
| `--max-agents` | **Currently used** | Controls parallelism, already implemented |
| `--strategy` | **Potentially useful** | Values like `research`, `analysis` align with TITO workflows |
| `--mode` | **Low relevance** | TITO uses centralized orchestration by default |
| `--parallel` | **High relevance** | Could improve performance (2.8-4.4x claimed speedup) |
| `--monitor` | **Low relevance** | Adds overhead, TITO tracks via other means |
| `--background` | **Not applicable** | TITO workflows are user-initiated, not background tasks |
| `--claude` | **Not applicable** | TITO is already running within Claude Code |
| `--executor` | **Not applicable** | TITO requires Claude Code integration |
| `--analysis` | **High relevance** | `review` and `audit` workflows are read-only |
| `--read-only` | **High relevance** | Alias for --analysis |
| `--topology` | **Unknown utility** | Only works with `swarm init`, unclear if compatible with TITO's usage pattern |
| `--continue-session` | **Removed** | Previously caused memory.db conflicts |

---

## 7. Recommendations for TITO

### Conservative Recommendation (RECOMMENDED):
**Keep current implementation minimal**

```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```

**Rationale**:
1. **Stability**: Current implementation works
2. **Alpha software**: claude-flow is in alpha, features may be unstable
3. **Limited evidence**: No verified production usage outside ruvnet's examples
4. **Timeout issues**: GitHub issues report execution failures in headless environments
5. **Broken features**: Issue #564 shows recent breakage in v2.0.0-alpha.83

### Experimental Additions (TEST BEFORE DEPLOYING):

#### Option A: Add --strategy for workflow types
```bash
# For research/review/audit workflows
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents" --strategy research

# For compile/enhance workflows
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents" --strategy development
```

**Risk**: Unknown whether `--strategy` parameter actually affects behavior or is placeholder

#### Option B: Add --analysis for read-only workflows
```bash
# For review/audit workflows
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents" --analysis
```

**Risk**: May restrict tool usage needed for TITO workflows (e.g., WebFetch, Read)

#### Option C: Add --parallel for performance
```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents" --parallel
```

**Risk**: Claimed 2.8-4.4x speedup is unverified; may introduce race conditions

### Testing Protocol:
If experimenting with new parameters:
1. Test with single workflow type (e.g., `research`)
2. Verify output quality matches current implementation
3. Monitor for timeout issues (2-minute Bash limit vs 120-minute swarm limit)
4. Check for "require is not defined" errors
5. Validate memory.db behavior if session continuity is needed

---

## 8. Confidence Levels Summary

| Finding | Confidence | Evidence |
|---------|-----------|----------|
| Parameters in CLI help output | **HIGH** | Direct execution confirmed |
| --max-agents currently used by TITO | **HIGH** | Observed in TITO codebase |
| --strategy values (research, development, etc.) | **MEDIUM** | In help output, but effect unverified |
| --parallel provides speedup | **LOW** | Claimed but unverified |
| --topology works with standard swarm commands | **LOW** | Only shown with `swarm init` |
| External production usage exists | **VERY LOW** | No verified examples found |
| New parameters will improve TITO | **LOW** | Alpha software, limited evidence |

---

## 9. Critical Gaps and Unknowns

1. **Parameter Implementation**: Cannot verify source code implementation
2. **Feature Stability**: Alpha software with reported breakages (Issue #564)
3. **Production Readiness**: Issue #510 reports headless execution failures
4. **Parameter Interactions**: Unknown how parameters combine (e.g., --strategy + --parallel)
5. **Real-World Usage**: Despite 9.6k stars, minimal evidence of production deployment
6. **Documentation Accuracy**: Wiki pages noted as "broken" in task requirements
7. **Timeout Conflicts**: 2-minute Bash timeout vs 120-minute swarm timeout

---

## 10. Conclusion

**Primary Finding**: TITO should maintain its current minimal parameter usage (`--max-agents` only) unless specific experiments demonstrate clear value.

**Evidence Quality**: This investigation found:
- **Verified**: 10 parameters confirmed via CLI help
- **Documented**: 3 additional parameters in official examples
- **Unverified**: 0 parameters in real-world usage outside ruvnet

**Risk Assessment**: Adding parameters introduces:
- **Stability risk**: Alpha software with known issues
- **Maintenance risk**: Parameters may change or break
- **Compatibility risk**: Headless execution failures reported
- **Value uncertainty**: No evidence of improved outcomes

**Next Steps**:
1. Monitor claude-flow releases for stability improvements
2. Re-evaluate when project reaches beta/stable
3. Test experimental parameters in isolated environment before production
4. Consider alternatives to claude-flow if stability is critical

---

## Appendices

### A. CLI Help Output (Verification Artifact)

```
🧠 SWARM COMMAND - Multi-Agent AI Coordination

USAGE:
  claude-flow swarm <objective> [options]

OPTIONS:
  --strategy <type>    Execution strategy: research, development, analysis,
                       testing, optimization, maintenance
  --mode <type>        Coordination mode: centralized, distributed,
                       hierarchical, mesh, hybrid
  --max-agents <n>     Maximum number of agents (default: 5)
  --parallel           Enable parallel execution (2.8-4.4x speed improvement)
  --monitor            Real-time swarm monitoring
  --background         Run in background with progress tracking
  --claude             Open Claude Code CLI
  --executor           Use built-in executor instead of Claude Code
  --analysis           Enable analysis/read-only mode (no code changes)
  --read-only          Enable read-only mode (alias for --analysis)
```

### B. Investigation Methodology

1. **Primary Sources**:
   - Direct CLI execution: `npx claude-flow@alpha swarm --help`
   - Official repository: https://github.com/ruvnet/claude-flow
   - Package version: v2.7.32 (confirmed via package.json)

2. **Secondary Sources**:
   - GitHub issues: #510, #59, #564, #108, #125
   - External tutorials: Deeplearning.fr beginner's guide
   - Community reports: Medium article by Adrian Cockcroft (access denied)

3. **Verification Attempts**:
   - Source code: Attempted access to /src/cli/, /src/terminal/, /bin/ (partial success)
   - GitHub code search: Multiple queries (limited results)
   - Real-world usage: Extensive searching (no verified examples found)

4. **Limitations**:
   - Could not access TypeScript source files defining parameter logic
   - Could not verify claimed performance improvements (--parallel)
   - Could not test in production-like headless environment
   - Limited to public repositories (no access to private implementations)

---

**Report Generated**: 2025-11-11
**claude-flow Version Investigated**: v2.7.32
**TITO Context**: Bash CLI using npx invocation
**Investigator Confidence**: Medium (verified CLI parameters) to Low (real-world usage patterns)

