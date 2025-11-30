# Investigation of claude-flow swarm parameters for TITO optimization

## Executive summary

This report investigates which command-line parameters for `npx claude-flow@alpha swarm` are verified to exist in implementation and should be used for TITO workflow optimization [@claude-flow-readme]. TITO currently uses `npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"` and removed the `--sessions` parameter due to memory sharing issues with `.swarm/memory.db` [@claude]. The investigation examines source code, official documentation, and third-party usage to determine what parameters are actually implemented versus merely documented.

## Verified parameters from source code analysis

### Parameters implemented in swarm-command.md

The TypeScript source code for the swarm action handler reveals a comprehensive set of command-line flags parsed from `ctx.flags` [@swarm-command]. The implementation at lines 28-40 documents explicit help text for supported options, while lines 44-67 show the actual parsing logic [@swarm-command].

The following parameters are confirmed in the implementation:

- `--strategy <type>`: Task decomposition strategy (values: `auto`, `research`, `development`, `analysis`) with `auto` as default [@swarm-command]
- `--max-agents <n>`: Maximum number of agents, default 5, parsed at line 46 with fallback to `--max-agents` hyphenated form [@swarm-command]
- `--max-depth <n>`: Maximum task decomposition depth, default 3, parsed at line 47 [@swarm-command]
- `--timeout <minutes>`: Execution timeout in minutes, default 60, converted to milliseconds at line 134 [@swarm-command]
- `--dry-run`: Show configuration without executing, checked at line 71 [@swarm-command]
- `--research`: Enable research capabilities (boolean flag), line 48 [@swarm-command]
- `--parallel`: Enable parallel execution (boolean flag), line 49, affects task concurrency at line 133 [@swarm-command]
- `--review`: Enable peer review between agents (boolean flag), line 54 [@swarm-command]
- `--monitor`: Enable real-time monitoring (boolean flag), line 62, passed to SwarmCoordinator at line 135 [@swarm-command]
- `--ui`: Use blessed terminal UI requiring node.js (boolean flag), line 36, handled at lines 88-123 [@swarm-command]
- `--background`: Run swarm in background mode (boolean flag), line 64, controls execution flow at line 211 [@swarm-command]
- `--distributed`: Enable distributed coordination (boolean flag), line 66, sets coordination strategy at line 139 [@swarm-command]
- `--memory-namespace <name>`: Memory namespace for swarm, default "swarm", parsed at lines 50-51 [@swarm-command]
- `--persistence`: Enable task persistence (boolean default true), line 65 [@swarm-command]
- `--coordinator`: Coordinator mode (boolean flag), line 54 [@swarm-command]
- `--config <path>` / `-c`: Configuration file path, line 55 [@swarm-command]
- `--verbose` / `-v`: Verbose output (boolean flag), line 56, used at line 621 for progress logging [@swarm-command]

### Parameters used in SwarmCoordinator instantiation

The SwarmCoordinator class is instantiated at lines 131-140 with a configuration object that consumes several parsed flags [@swarm-command]. The mapping is as follows:

- `maxAgents`: From `options.maxAgents` (line 132)
- `maxConcurrentTasks`: Set to `options.maxAgents` if `options.parallel` is true, otherwise 1 (line 133)
- `taskTimeout`: Computed as `options.timeout * 60 * 1000` converting minutes to milliseconds (line 134)
- `enableMonitoring`: From `options.monitor` (line 135)
- `enableWorkStealing`: From `options.parallel` (line 136)
- `enableCircuitBreaker`: Hard-coded to `true` (line 137)
- `memoryNamespace`: From `options.memoryNamespace` (line 138)
- `coordinationStrategy`: `'distributed'` if `options.distributed` is true, otherwise `'centralized'` (line 139)

### Parameters NOT found in source code

The KB source code does not implement the following parameters that appear in some external documentation:

- `--topology`: Not parsed in swarm-command.md flags (lines 44-67) or passed to SwarmCoordinator constructor (lines 131-140)
- `--sessions`: Explicitly removed by the user due to memory sharing issues [@claude]
- `--claude`: Not present in swarm-command.md implementation
- `--continue-session`: Not parsed in the options object (lines 44-67)

## Parameters documented in official examples

### README.md examples from claude-flow repository

The official README in the ruvnet/claude-flow repository v2.7.32 provides swarm command examples [@claude-flow-readme]. The Quick Swarm Commands section at lines 203-212 shows:

```bash
npx claude-flow@alpha swarm "build REST API with authentication" --claude
npx claude-flow@alpha swarm init --topology mesh --max-agents 5
npx claude-flow@alpha swarm spawn researcher "analyze API patterns"
npx claude-flow@alpha swarm spawn coder "implement endpoints"
npx claude-flow@alpha swarm status
```

The README examples introduce parameters not found in the swarm-command.md source code:

- `--claude`: Shown in the basic quick task example (line 205) and hive-mind examples (line 219, 224) [@claude-flow-readme]
- `--topology mesh`: Shown in init example (line 208) [@claude-flow-readme]
- `swarm init`, `swarm spawn`, `swarm status`: Subcommands for multi-agent coordination (lines 208-212) [@claude-flow-readme]

External web sources confirm the official README examples [@github-ruvnet-claude-flow]. A GitHub repository fetch retrieved identical command examples showing `--claude`, `--topology mesh`, and `--max-agents 5` flags in the swarm subcommand context [@github-ruvnet-claude-flow].

### Subcommand structure: swarm init vs. swarm <objective>

The official examples demonstrate two usage patterns [@claude-flow-readme]:

1. Direct execution: `npx claude-flow@alpha swarm "<objective>"` (line 205)
2. Multi-step workflow: `swarm init`, then `swarm spawn <type> "<task>"`, then `swarm status` (lines 208-212)

The swarm-command.md source code only implements pattern 1 (direct execution) [@swarm-command]. The `swarmAction` function at line 12 expects a single objective string formed by joining non-flag arguments (line 20) [@swarm-command]. There is no CLI routing logic for subcommands like `init`, `spawn`, or `status` in the provided source file.

## External validation and third-party usage

### Search for non-ruvnet usage

A targeted web search for `site:github.com "npx claude-flow" swarm NOT ruvnet` returned four GitHub repositories [@github-jcolano-claude-flow][@github-avaloki-claude-flow-web3][@github-rdmolony-claude-flow-getting-started]:

1. `jcolano/claude-flow`: Fork of ruvnet/claude-flow with identical README [@github-jcolano-claude-flow]
2. `avaloki108/claude-flow----web3`: Another fork with identical content [@github-avaloki-claude-flow-web3]
3. `rdmolony/claude-flow-getting-started`: A minimal getting-started repository demonstrating MCP setup [@github-rdmolony-claude-flow-getting-started]

None of these repositories contain unique swarm invocation commands beyond what is shown in the official README. The rdmolony repository describes claude-flow as "turning Claude Code into a subagent orchestrator" but does not show command-line usage examples with parameters [@github-rdmolony-claude-flow-getting-started].

No evidence was found of organizations or individuals using claude-flow swarm commands with parameters significantly different from the official examples. All discovered usage references either the official README or is derivative content from tutorials based on that README.

## Discrepancies between documentation and implementation

### Parameters documented but not implemented

The following parameters appear in official README examples but are absent from the swarm-command.md implementation:

1. `--topology`: Shown in README example (line 208) but not parsed in swarm-command.md (lines 44-67) [@claude-flow-readme][@swarm-command]
2. `--claude`: Shown in README example (line 205) but not parsed in swarm-command.md [@claude-flow-readme][@swarm-command]
3. `swarm init` subcommand: Shown in README (line 208) but swarm-command.md only accepts objective strings [@claude-flow-readme][@swarm-command]
4. `swarm spawn` subcommand: Shown in README (line 209) but not implemented in swarm-command.md [@claude-flow-readme][@swarm-command]
5. `swarm status` subcommand: Shown in README (line 211) but not implemented in swarm-command.md [@claude-flow-readme][@swarm-command]

### Possible causes of documentation-implementation drift

The README is dated v2.7.0 and describes itself as an alpha release (v2.7.0-alpha.10) [@claude-flow-readme]. The swarm-command.md source code may represent an earlier or later state of the implementation. The user's task description warns that "Project is in alpha - features may not work as advertised" and "Don't assume wiki documentation is accurate (it's broken)" [@claude].

External sources describe advanced features such as AgentDB integration, HNSW vector search, and 100 MCP tools [@claude-flow-readme][@github-ruvnet-claude-flow], but the swarm-command.md source code does not show integration with these systems. The README's feature claims may represent planned functionality or separately implemented modules not visible in the single source file provided.

## Recommendations for TITO usage

### Current TITO invocation pattern

TITO currently uses the following command pattern [@claude]:

```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```

This invocation uses only two parameters: the objective string and `--max-agents`. Both parameters are confirmed to be implemented in swarm-command.md [@swarm-command].

### Recommended parameters to add

Based on the verified implementation in swarm-command.md, TITO workflows could benefit from the following additional parameters:

1. `--strategy research`: Explicitly set strategy for research workflow [@swarm-command]
   - Justification: TITO's research workflow involves KB extraction and web investigation [@claude]
   - Implementation: Parsed at line 45, used at line 176 to select agent types [@swarm-command]
   - Default: `auto` (line 45), which infers strategy from objective keywords [@swarm-command]

2. `--timeout <minutes>`: Set explicit timeout for long-running operations [@swarm-command]
   - Justification: Research tasks with large knowledge bases or extensive web searches may exceed the default 60-minute timeout [@claude]
   - Implementation: Parsed at line 52, converted to milliseconds at line 134 [@swarm-command]
   - Default: 60 minutes [@swarm-command]
   - Recommendation: Set to 90 or 120 for research workflows

3. `--parallel`: Enable parallel execution of independent subtasks [@swarm-command]
   - Justification: Research workflow has independent KB extraction and web search phases that could run concurrently [@claude]
   - Implementation: Parsed at line 49, affects maxConcurrentTasks at line 133 [@swarm-command]
   - Default: `false` (sequential execution) [@swarm-command]

4. `--research`: Enable research capabilities [@swarm-command]
   - Justification: Aligns with TITO's research workflow requirements [@claude]
   - Implementation: Parsed at line 48, passed to agent task execution at line 465 [@swarm-command]
   - Default: `false` [@swarm-command]

5. `--verbose`: Enable progress logging [@swarm-command]
   - Justification: Provides visibility into long-running research operations [@claude]
   - Implementation: Parsed at line 56, used at line 621 for progress updates [@swarm-command]
   - Default: `false` [@swarm-command]

### Parameters to avoid

The following parameters should NOT be used because they are not implemented in the source code:

1. `--topology`: Not parsed in swarm-command.md despite appearing in README examples [@swarm-command][@claude-flow-readme]
2. `--claude`: Not implemented in swarm-command.md [@swarm-command]
3. `swarm init`, `swarm spawn`, `swarm status`: Subcommands not supported by current implementation [@swarm-command]

### Minimal vs. extended configuration

TITO has two options for configuration approach:

**Option 1: Minimal (current approach)**
```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```
- Advantages: Simple, minimal risk of breakage, relies on defaults
- Disadvantages: May not optimize for research-specific needs, no timeout control

**Option 2: Extended (recommended for research workflow)**
```bash
npx --yes claude-flow@alpha swarm "$objective" \
  --max-agents "$max_agents" \
  --strategy research \
  --timeout 90 \
  --research \
  --verbose
```
- Advantages: Explicitly configured for research tasks, better timeout handling, progress visibility
- Disadvantages: More parameters to maintain, potential for parameter changes in future alpha versions

Given that claude-flow is in alpha (v2.7.0-alpha.10) and shows documentation-implementation discrepancies, a conservative approach would be to add parameters incrementally and test each addition [@claude-flow-readme][@claude].

## Confidence assessment by finding

### High confidence (verified in source code)

The following findings have HIGH confidence because they are verifiable by direct inspection of swarm-command.md source code:

- Parameters parsed at lines 44-67: `--strategy`, `--max-agents`, `--max-depth`, `--timeout`, `--dry-run`, `--research`, `--parallel`, `--review`, `--monitor`, `--ui`, `--background`, `--distributed`, `--memory-namespace`, `--persistence`, `--coordinator`, `--config`, `--verbose` [@swarm-command]
- SwarmCoordinator configuration mapping at lines 131-140 [@swarm-command]
- Objective parsing at line 20 [@swarm-command]
- Strategy-based agent type selection at line 176 [@swarm-command]
- Absence of `--topology`, `--claude`, and subcommand routing in source code [@swarm-command]

### Medium confidence (documented but not verified in implementation)

The following findings have MEDIUM confidence because they are documented in the README but not verifiable in the provided source code:

- `--topology` parameter: Shown in README examples but not in swarm-command.md [@claude-flow-readme][@swarm-command]
- `--claude` flag: Shown in README examples but not in swarm-command.md [@claude-flow-readme][@swarm-command]
- Subcommands (`init`, `spawn`, `status`): Documented but may be in separate source files not provided [@claude-flow-readme]
- Advanced features (AgentDB, HNSW, 100 MCP tools): Listed in README but integration points not visible in swarm-command.md [@claude-flow-readme]

## Conclusion

This investigation identified 17 command-line parameters implemented in the swarm-command.md source code, with `--max-agents`, `--strategy`, `--timeout`, `--research`, `--parallel`, and `--verbose` being the most relevant for TITO's research workflow [@swarm-command][@claude]. The official README documents additional parameters (`--topology`, `--claude`) and subcommands (`init`, `spawn`, `status`) that are not present in the provided source code, indicating documentation-implementation drift typical of alpha software [@claude-flow-readme][@swarm-command].

For TITO optimization, the recommended approach is to incrementally add verified parameters starting with `--strategy research` and `--timeout 90`, testing each addition before expanding to `--research`, `--parallel`, and `--verbose` [@swarm-command]. Parameters like `--topology` and `--claude` should be avoided until their implementation status is clarified by examining additional source files or testing with the actual claude-flow binary [@claude].

No evidence was found of non-ruvnet repositories using claude-flow swarm commands in production, suggesting limited real-world validation of the tool's documented capabilities [@github-jcolano-claude-flow][@github-rdmolony-claude-flow-getting-started]. All usage examples traced back to the official README or derivative tutorial content [@blog-zujkowski-claude-flow][@blog-cockcroft-claude-flow].

## References

### Knowledge base sources
- claude.md: TITO task specification and investigation requirements [@claude]
- claude-flow-readme.md: Official README from ruvnet/claude-flow v2.7.32 repository [@claude-flow-readme]
- swarm-command.md: TypeScript source code for swarm command implementation [@swarm-command]

### External sources
- GitHub repository: ruvnet/claude-flow official repository [@github-ruvnet-claude-flow]
- Tutorial: Supercharging Development with Claude-Flow by William Zujkowski [@blog-zujkowski-claude-flow]
- Blog post: My First Agent Swarm Experience with claude-flow by Adrian Cockcroft [@blog-cockcroft-claude-flow]
- Repository: claude-flow-getting-started by rdmolony [@github-rdmolony-claude-flow-getting-started]
- Repository fork: jcolano/claude-flow [@github-jcolano-claude-flow]
