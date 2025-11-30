# Investigation of claude-flow swarm parameters for TITO optimization

## Executive summary

This report investigates which command-line parameters for `npx claude-flow@alpha swarm` are verified to exist in implementation and should be used for TITO workflow optimization [KB:claude-flow-readme.md]. TITO currently uses `npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"` and removed the `--sessions` parameter due to memory sharing issues with `.swarm/memory.db` [KB:claude.md]. The investigation examines source code, official documentation, and third-party usage to determine what parameters are actually implemented versus merely documented.

^[Verdict: TRUE, Confidence: HIGH, Rationale: This paragraph accurately states the investigation's purpose as described in claude.md:3-4 and TITO's current invocation pattern from claude.md:44-46. The mention of removed --sessions parameter and memory sharing issues is directly sourced from claude.md:3-4. All claims are grounded in KB sources.]

## Verified parameters from source code analysis

### Parameters implemented in swarm-command.md

The TypeScript source code for the swarm action handler reveals a comprehensive set of command-line flags parsed from `ctx.flags` [KB:swarm-command.md]. The implementation at lines 28-40 documents explicit help text for supported options, while lines 44-67 show the actual parsing logic [KB:swarm-command.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: swarm-command.md:14-40 shows the help text output in the code, and lines 44-67 contain the options object construction that parses ctx.flags. These line numbers correspond to the actual TypeScript implementation in the KB source.]

The following parameters are confirmed in the implementation:

- `--strategy <type>`: Task decomposition strategy (values: `auto`, `research`, `development`, `analysis`) with `auto` as default [KB:swarm-command.md]
- `--max-agents <n>`: Maximum number of agents, default 5, parsed at line 46 with fallback to `--max-agents` hyphenated form [KB:swarm-command.md]
- `--max-depth <n>`: Maximum task decomposition depth, default 3, parsed at line 47 [KB:swarm-command.md]
- `--timeout <minutes>`: Execution timeout in minutes, default 60, converted to milliseconds at line 134 [KB:swarm-command.md]
- `--dry-run`: Show configuration without executing, checked at line 71 [KB:swarm-command.md]
- `--research`: Enable research capabilities (boolean flag), line 48 [KB:swarm-command.md]
- `--parallel`: Enable parallel execution (boolean flag), line 49, affects task concurrency at line 133 [KB:swarm-command.md]
- `--review`: Enable peer review between agents (boolean flag), line 54 [KB:swarm-command.md]
- `--monitor`: Enable real-time monitoring (boolean flag), line 62, passed to SwarmCoordinator at line 135 [KB:swarm-command.md]
- `--ui`: Use blessed terminal UI requiring node.js (boolean flag), line 36, handled at lines 88-123 [KB:swarm-command.md]
- `--background`: Run swarm in background mode (boolean flag), line 64, controls execution flow at line 211 [KB:swarm-command.md]
- `--distributed`: Enable distributed coordination (boolean flag), line 66, sets coordination strategy at line 139 [KB:swarm-command.md]
- `--memory-namespace <name>`: Memory namespace for swarm, default "swarm", parsed at lines 50-51 [KB:swarm-command.md]
- `--persistence`: Enable task persistence (boolean default true), line 65 [KB:swarm-command.md]
- `--coordinator`: Coordinator mode (boolean flag), line 54 [KB:swarm-command.md]
- `--config <path>` / `-c`: Configuration file path, line 55 [KB:swarm-command.md]
- `--verbose` / `-v`: Verbose output (boolean flag), line 56, used at line 621 for progress logging [KB:swarm-command.md]

^[Verdict: TRUE, Confidence: HIGH, Rationale: All parameters listed are directly traceable to specific line numbers in swarm-command.md. Each flag's parsing location, default value, and downstream usage in the code is verified by cross-referencing the implementation. For example, --max-agents at line 46, --timeout conversion at line 134, --monitor passed to SwarmCoordinator at line 135, and --background control flow at line 211 are all confirmed in the source.]

### Parameters used in SwarmCoordinator instantiation

The SwarmCoordinator class is instantiated at lines 131-140 with a configuration object that consumes several parsed flags [KB:swarm-command.md]. The mapping is as follows:

- `maxAgents`: From `options.maxAgents` (line 132)
- `maxConcurrentTasks`: Set to `options.maxAgents` if `options.parallel` is true, otherwise 1 (line 133)
- `taskTimeout`: Computed as `options.timeout * 60 * 1000` converting minutes to milliseconds (line 134)
- `enableMonitoring`: From `options.monitor` (line 135)
- `enableWorkStealing`: From `options.parallel` (line 136)
- `enableCircuitBreaker`: Hard-coded to `true` (line 137)
- `memoryNamespace`: From `options.memoryNamespace` (line 138)
- `coordinationStrategy`: `'distributed'` if `options.distributed` is true, otherwise `'centralized'` (line 139)

^[Verdict: TRUE, Confidence: HIGH, Rationale: The SwarmCoordinator instantiation at swarm-command.md:131-140 shows the exact mapping of parsed command-line options to constructor parameters. The timeout calculation (line 134), parallel execution logic (line 133), and coordination strategy ternary (line 139) are all verifiable in the source code.]

### Parameters NOT found in source code

The KB source code does not implement the following parameters that appear in some external documentation:

- `--topology`: Not parsed in swarm-command.md flags (lines 44-67) or passed to SwarmCoordinator constructor (lines 131-140)
- `--sessions`: Explicitly removed by the user due to memory sharing issues [KB:claude.md]
- `--claude`: Not present in swarm-command.md implementation
- `--continue-session`: Not parsed in the options object (lines 44-67)

^[Verdict: TRUE, Confidence: HIGH, Rationale: An exhaustive review of swarm-command.md:44-67 (options parsing) and lines 131-140 (SwarmCoordinator instantiation) confirms these parameters are absent. The --sessions removal is explicitly stated in claude.md:3-4. The absence of --topology is particularly notable given its presence in external documentation, highlighting the documentation-implementation gap.]

## Parameters documented in official examples

### README.md examples from claude-flow repository

The official README in the ruvnet/claude-flow repository v2.7.32 provides swarm command examples [KB:claude-flow-readme.md]. The Quick Swarm Commands section at lines 203-212 shows:

```bash
npx claude-flow@alpha swarm "build REST API with authentication" --claude
npx claude-flow@alpha swarm init --topology mesh --max-agents 5
npx claude-flow@alpha swarm spawn researcher "analyze API patterns"
npx claude-flow@alpha swarm spawn coder "implement endpoints"
npx claude-flow@alpha swarm status
```

^[Verdict: TRUE, Confidence: HIGH, Rationale: claude-flow-readme.md:203-212 contains the Quick Swarm Commands section with these exact examples. The examples show --claude and --topology flags that are documented but not present in the swarm-command.md source code implementation.]

The README examples introduce parameters not found in the swarm-command.md source code:

- `--claude`: Shown in the basic quick task example (line 205) and hive-mind examples (line 219, 224) [KB:claude-flow-readme.md]
- `--topology mesh`: Shown in init example (line 208) [KB:claude-flow-readme.md]
- `swarm init`, `swarm spawn`, `swarm status`: Subcommands for multi-agent coordination (lines 208-212) [KB:claude-flow-readme.md]

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: These parameters appear in claude-flow-readme.md examples at the cited lines, but they are not present in swarm-command.md implementation. This discrepancy indicates documentation-implementation drift. The --claude flag appears in lines 205, 219, 224 of the README but has no corresponding parsing logic in swarm-command.md. Confidence is MEDIUM due to this verified gap between documentation and code.]

External web sources confirm the official README examples [WEB:https://github.com/ruvnet/claude-flow]. A GitHub repository fetch retrieved identical command examples showing `--claude`, `--topology mesh`, and `--max-agents 5` flags in the swarm subcommand context [WEB:https://github.com/ruvnet/claude-flow].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The WebFetch tool successfully retrieved swarm examples from the official GitHub repository showing the same commands as claude-flow-readme.md. This external validation confirms the documented examples are present in the official README, though it does not verify these flags are implemented in the code.]

### Subcommand structure: swarm init vs. swarm <objective>

The official examples demonstrate two usage patterns [KB:claude-flow-readme.md]:

1. Direct execution: `npx claude-flow@alpha swarm "<objective>"` (line 205)
2. Multi-step workflow: `swarm init`, then `swarm spawn <type> "<task>"`, then `swarm status` (lines 208-212)

The swarm-command.md source code only implements pattern 1 (direct execution) [KB:swarm-command.md]. The `swarmAction` function at line 12 expects a single objective string formed by joining non-flag arguments (line 20) [KB:swarm-command.md]. There is no CLI routing logic for subcommands like `init`, `spawn`, or `status` in the provided source file.

^[Verdict: TRUE, Confidence: HIGH, Rationale: swarm-command.md:20 shows objective = ctx.args.join(' ').trim(), treating all non-flag arguments as a single objective string. There is no switch statement or conditional logic in swarm-command.md to handle 'init', 'spawn', or 'status' as subcommands. The README examples at claude-flow-readme.md:208-212 show these subcommands, but the source code implementation does not parse them. This is a verified discrepancy between documentation and implementation.]

## External validation and third-party usage

### Documented examples from web sources

Web search results returned several blog posts and tutorials referencing claude-flow swarm usage [WEB:https://williamzujkowski.github.io/posts/supercharging-development-with-claude-flow-ai-swarm-intelligence-for-modern-engineering/][WEB:https://adrianco.medium.com/vibe-coding-is-so-last-month-my-first-agent-swarm-experience-with-claude-flow-414b0bd6f2f2]. These sources cite the same examples as the official README, including:

- `npx claude-flow@alpha swarm "build REST API with authentication" --claude`
- `npx claude-flow@alpha swarm init --topology mesh --max-agents 5`

The sources describe claude-flow as using hive-mind swarm intelligence and coordinating multiple specialized agents (researcher, architect, coder, tester) in parallel [WEB:https://williamzujkowski.github.io/posts/supercharging-development-with-claude-flow-ai-swarm-intelligence-for-modern-engineering/]. However, these tutorials appear to be based on official documentation rather than independent implementation verification.

^[Verdict: UNCERTAIN, Confidence: LOW, Rationale: The blog posts and tutorials cite the same examples as the official README, suggesting they are derivative rather than independent verification. While the sources confirm the documented examples exist, they do not provide evidence of actual execution or successful usage. The blog posts describe features (hive-mind intelligence, parallel agent coordination) that are advertised but not demonstrated with execution logs or output. Confidence is LOW because these sources may reflect documentation claims rather than verified functionality.]

### Search for non-ruvnet usage

A targeted web search for `site:github.com "npx claude-flow" swarm NOT ruvnet` returned four GitHub repositories [WEB:https://github.com/jcolano/claude-flow][WEB:https://github.com/avaloki108/claude-flow----web3][WEB:https://github.com/rdmolony/claude-flow-getting-started]:

1. `jcolano/claude-flow`: Fork of ruvnet/claude-flow with identical README [WEB:https://github.com/jcolano/claude-flow]
2. `avaloki108/claude-flow----web3`: Another fork with identical content [WEB:https://github.com/avaloki108/claude-flow----web3]
3. `rdmolony/claude-flow-getting-started`: A minimal getting-started repository demonstrating MCP setup [WEB:https://github.com/rdmolony/claude-flow-getting-started]

None of these repositories contain unique swarm invocation commands beyond what is shown in the official README. The rdmolony repository describes claude-flow as "turning Claude Code into a subagent orchestrator" but does not show command-line usage examples with parameters [WEB:https://github.com/rdmolony/claude-flow-getting-started].

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: The web search results confirmed the existence of these three repositories. The first two are forks with identical content to ruvnet/claude-flow (verified by checking the repository descriptions and links). The third repository (rdmolony) is a getting-started guide that describes the tool's purpose but does not contain novel command examples. This validates the claim that non-ruvnet usage examples are scarce. Confidence is MEDIUM because web search results may not capture all GitHub repositories using claude-flow in non-public or unlisted contexts.]

No evidence was found of organizations or individuals using claude-flow swarm commands with parameters significantly different from the official examples. All discovered usage references either the official README or is derivative content from tutorials based on that README.

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: The web searches and repository checks did not uncover any novel usage patterns or parameter combinations beyond official documentation. This negative finding is supported by the exhaustive search attempts, but confidence is MEDIUM because absence of evidence is not definitive proof—unlisted repositories, private codebases, or non-indexed usage may exist but were not discoverable through the search methods employed.]

## Discrepancies between documentation and implementation

### Parameters documented but not implemented

The following parameters appear in official README examples but are absent from the swarm-command.md implementation:

1. `--topology`: Shown in README example (line 208) but not parsed in swarm-command.md (lines 44-67) [KB:claude-flow-readme.md][KB:swarm-command.md]
2. `--claude`: Shown in README example (line 205) but not parsed in swarm-command.md [KB:claude-flow-readme.md][KB:swarm-command.md]
3. `swarm init` subcommand: Shown in README (line 208) but swarm-command.md only accepts objective strings [KB:claude-flow-readme.md][KB:swarm-command.md]
4. `swarm spawn` subcommand: Shown in README (line 209) but not implemented in swarm-command.md [KB:claude-flow-readme.md][KB:swarm-command.md]
5. `swarm status` subcommand: Shown in README (line 211) but not implemented in swarm-command.md [KB:claude-flow-readme.md][KB:swarm-command.md]

^[Verdict: TRUE, Confidence: HIGH, Rationale: This is a verified list of discrepancies between the README examples and the source code. Each discrepancy is confirmed by checking (1) presence in claude-flow-readme.md at cited line numbers and (2) absence in swarm-command.md parsing logic (lines 44-67) and action handler (lines 12-267). For example, --topology appears in README line 208 but has no corresponding entry in the options object construction at swarm-command.md:44-67.]

### Possible causes of documentation-implementation drift

The README is dated v2.7.0 and describes itself as an alpha release (v2.7.0-alpha.10) [KB:claude-flow-readme.md]. The swarm-command.md source code may represent an earlier or later state of the implementation. The user's task description warns that "Project is in alpha - features may not work as advertised" and "Don't assume wiki documentation is accurate (it's broken)" [KB:claude.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The version information is stated in claude-flow-readme.md:1,7,451. The alpha status is confirmed by the @alpha npm tag in examples (line 61) and the release version v2.7.0-alpha.10 (line 7, 120, 451). The user's cautions about alpha status and broken wiki pages are directly quoted from claude.md:26,55. All claims are sourced from KB documents.]

External sources describe advanced features such as AgentDB integration, HNSW vector search, and 100 MCP tools [KB:claude-flow-readme.md][WEB:https://github.com/ruvnet/claude-flow], but the swarm-command.md source code does not show integration with these systems. The README's feature claims may represent planned functionality or separately implemented modules not visible in the single source file provided.

^[Verdict: UNCERTAIN, Confidence: MEDIUM, Rationale: claude-flow-readme.md:16-30 lists features like AgentDB v1.3.9 Integration, 100 MCP Tools, and HNSW indexing. However, swarm-command.md does not import or reference AgentDB or MCP tool modules. The claim that "swarm-command.md does not show integration" is verifiable by inspecting imports (lines 5-11) and the function body. However, the README features could be implemented in other files not included in the KB. Confidence is MEDIUM because the KB provides only a subset of the codebase, making it impossible to definitively state these features are unimplemented elsewhere.]

## Recommendations for TITO usage

### Current TITO invocation pattern

TITO currently uses the following command pattern [KB:claude.md]:

```bash
npx --yes claude-flow@alpha swarm "$objective" --max-agents "$max_agents"
```

This invocation uses only two parameters: the objective string and `--max-agents`. Both parameters are confirmed to be implemented in swarm-command.md [KB:swarm-command.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The current TITO usage is stated in claude.md:44-46. The implementation verification for the objective string (parsed at swarm-command.md:20) and --max-agents flag (parsed at swarm-command.md:46) is confirmed by source code analysis. Both elements are present and functional in the implementation.]

### Recommended parameters to add

Based on the verified implementation in swarm-command.md, TITO workflows could benefit from the following additional parameters:

1. `--strategy research`: Explicitly set strategy for research workflow [KB:swarm-command.md]
   - Justification: TITO's research workflow involves KB extraction and web investigation [KB:claude.md]
   - Implementation: Parsed at line 45, used at line 176 to select agent types [KB:swarm-command.md]
   - Default: `auto` (line 45), which infers strategy from objective keywords [KB:swarm-command.md]

2. `--timeout <minutes>`: Set explicit timeout for long-running operations [KB:swarm-command.md]
   - Justification: Research tasks with large knowledge bases or extensive web searches may exceed the default 60-minute timeout [KB:claude.md]
   - Implementation: Parsed at line 52, converted to milliseconds at line 134 [KB:swarm-command.md]
   - Default: 60 minutes [KB:swarm-command.md]
   - Recommendation: Set to 90 or 120 for research workflows

3. `--parallel`: Enable parallel execution of independent subtasks [KB:swarm-command.md]
   - Justification: Research workflow has independent KB extraction and web search phases that could run concurrently [KB:claude.md]
   - Implementation: Parsed at line 49, affects maxConcurrentTasks at line 133 [KB:swarm-command.md]
   - Default: `false` (sequential execution) [KB:swarm-command.md]

4. `--research`: Enable research capabilities [KB:swarm-command.md]
   - Justification: Aligns with TITO's research workflow requirements [KB:claude.md]
   - Implementation: Parsed at line 48, passed to agent task execution at line 465 [KB:swarm-command.md]
   - Default: `false` [KB:swarm-command.md]

5. `--verbose`: Enable progress logging [KB:swarm-command.md]
   - Justification: Provides visibility into long-running research operations [KB:claude.md]
   - Implementation: Parsed at line 56, used at line 621 for progress updates [KB:swarm-command.md]
   - Default: `false` [KB:swarm-command.md]

^[Verdict: TRUE, Confidence: HIGH, Rationale: Each recommended parameter is verified in swarm-command.md with specific line numbers for parsing and usage. The justifications are based on TITO workflow characteristics described in claude.md:36-42 (retrieve, research, review, compile, audit, enhance). The mapping between TITO needs and swarm parameters is logical: --strategy research aligns with research workflow, --timeout addresses long-running operations, --parallel matches independent task phases, --research enables web search tools, and --verbose provides observability. All default values and implementation details are sourced from swarm-command.md.]

### Parameters to avoid

The following parameters should NOT be used because they are not implemented in the source code:

1. `--topology`: Not parsed in swarm-command.md despite appearing in README examples [KB:swarm-command.md][KB:claude-flow-readme.md]
2. `--claude`: Not implemented in swarm-command.md [KB:swarm-command.md]
3. `swarm init`, `swarm spawn`, `swarm status`: Subcommands not supported by current implementation [KB:swarm-command.md]

^[Verdict: TRUE, Confidence: HIGH, Rationale: The absence of these parameters is verified by exhaustive review of swarm-command.md parsing logic (lines 44-67) and action handler (lines 12-267). The presence of --topology and --claude in README examples (claude-flow-readme.md:205,208) contrasts with their absence in implementation, creating a verified documentation-implementation gap. Using these parameters would result in them being ignored or causing errors.]

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

^[Verdict: TRUE, Confidence: HIGH, Rationale: Both command examples use only verified parameters from swarm-command.md. The advantages and disadvantages are logically derived from parameter functionality: --strategy research is implemented at line 45, --timeout at line 52, --research at line 48, and --verbose at line 56. The "research-specific needs" align with TITO's research workflow described in claude.md. The alpha version stability concern is grounded in the version information from claude-flow-readme.md:7,61,451 and the user's warning at claude.md:26.]

Given that claude-flow is in alpha (v2.7.0-alpha.10) and shows documentation-implementation discrepancies, a conservative approach would be to add parameters incrementally and test each addition [KB:claude-flow-readme.md][KB:claude.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The alpha version status is confirmed by claude-flow-readme.md:7,61,120,451 showing "v2.7.0-alpha.10" and "@alpha" npm tag. The documentation-implementation discrepancies are documented in the previous section with verified examples (--topology, --claude, subcommands). The recommendation for conservative incremental parameter addition is a logical inference from alpha software instability and observed discrepancies, both established facts from KB sources.]

## Confidence assessment by finding

### High confidence (verified in source code)

The following findings have HIGH confidence because they are verifiable by direct inspection of swarm-command.md source code:

- Parameters parsed at lines 44-67: `--strategy`, `--max-agents`, `--max-depth`, `--timeout`, `--dry-run`, `--research`, `--parallel`, `--review`, `--monitor`, `--ui`, `--background`, `--distributed`, `--memory-namespace`, `--persistence`, `--coordinator`, `--config`, `--verbose` [KB:swarm-command.md]
- SwarmCoordinator configuration mapping at lines 131-140 [KB:swarm-command.md]
- Objective parsing at line 20 [KB:swarm-command.md]
- Strategy-based agent type selection at line 176 [KB:swarm-command.md]
- Absence of `--topology`, `--claude`, and subcommand routing in source code [KB:swarm-command.md]

^[Verdict: TRUE, Confidence: HIGH, Rationale: All cited line numbers are traceable to swarm-command.md. The parameter parsing section (lines 44-67), coordinator configuration (lines 131-140), objective parsing (line 20), and agent type function (line 176) are all present in the KB source. The absence claims are verified by exhaustive search of the source file showing no matching strings for 'topology', '--claude' in the flags parsing section, or subcommand routing logic.]

### Medium confidence (documented but not verified in implementation)

The following findings have MEDIUM confidence because they are documented in the README but not verifiable in the provided source code:

- `--topology` parameter: Shown in README examples but not in swarm-command.md [KB:claude-flow-readme.md][KB:swarm-command.md]
- `--claude` flag: Shown in README examples but not in swarm-command.md [KB:claude-flow-readme.md][KB:swarm-command.md]
- Subcommands (`init`, `spawn`, `status`): Documented but may be in separate source files not provided [KB:claude-flow-readme.md]
- Advanced features (AgentDB, HNSW, 100 MCP tools): Listed in README but integration points not visible in swarm-command.md [KB:claude-flow-readme.md]

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: The documentation presence is verified in claude-flow-readme.md at cited line numbers (--topology at line 208, --claude at line 205, subcommands at lines 208-212, features at lines 16-30). The implementation absence is verified in swarm-command.md. However, the KB provides only a subset of the codebase. These features could be implemented in separate files (e.g., a different CLI router for subcommands, or swarm-init.ts for the init subcommand). Confidence is MEDIUM because the single source file does not represent the entire codebase, making absence claims tentative.]

### Low confidence (inferred from documentation patterns)

The following findings have LOW confidence because they are based on external sources or inference rather than direct verification:

- Third-party usage patterns: Web search found only forks and derivative tutorials, no independent usage [WEB:https://github.com/jcolano/claude-flow][WEB:https://github.com/rdmolony/claude-flow-getting-started]
- Production readiness: Blog posts describe production usage but do not provide evidence of execution [WEB:https://williamzujkowski.github.io/posts/supercharging-development-with-claude-flow-ai-swarm-intelligence-for-modern-engineering/]
- Feature functionality claims: Advanced features (hive-mind, neural learning, 100 MCP tools) are advertised but not demonstrated [KB:claude-flow-readme.md][WEB:https://github.com/ruvnet/claude-flow]

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: The categorization of these findings as LOW confidence is accurate. The web search results are documented in the "External validation" section with specific repository links, confirming the lack of independent usage examples. The blog posts retrieved via WebSearch describe features but do not show execution logs or outputs, making them documentary claims rather than verified usage. The advanced features are listed in claude-flow-readme.md but their functional status cannot be confirmed from the provided KB sources. This meta-assessment correctly identifies the limitations of evidence for these claims.]

## Conclusion

This investigation identified 17 command-line parameters implemented in the swarm-command.md source code, with `--max-agents`, `--strategy`, `--timeout`, `--research`, `--parallel`, and `--verbose` being the most relevant for TITO's research workflow [KB:swarm-command.md][KB:claude.md]. The official README documents additional parameters (`--topology`, `--claude`) and subcommands (`init`, `spawn`, `status`) that are not present in the provided source code, indicating documentation-implementation drift typical of alpha software [KB:claude-flow-readme.md][KB:swarm-command.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The count of 17 parameters is verifiable by counting the distinct flags parsed in swarm-command.md:44-67. The relevance of the six listed parameters to TITO's research workflow is justified by their functional purposes (max-agents for scale, strategy for workflow type, timeout for long operations, research for web tools, parallel for concurrency, verbose for logging) matching TITO workflow needs from claude.md:36-42. The documentation-implementation drift is verified by comparing claude-flow-readme.md examples with swarm-command.md implementation. The alpha software characterization comes from claude-flow-readme.md:7,61,120,451.]

For TITO optimization, the recommended approach is to incrementally add verified parameters starting with `--strategy research` and `--timeout 90`, testing each addition before expanding to `--research`, `--parallel`, and `--verbose` [KB:swarm-command.md]. Parameters like `--topology` and `--claude` should be avoided until their implementation status is clarified by examining additional source files or testing with the actual claude-flow binary [KB:claude.md].

^[Verdict: TRUE, Confidence: HIGH, Rationale: The recommendation for incremental addition is a conservative strategy grounded in (1) verified implementation of suggested parameters in swarm-command.md, (2) alpha software instability from claude-flow-readme.md, and (3) user's prior experience with fabricated parameters and broken documentation from claude.md:6-11,51-56. The avoidance of --topology and --claude is justified by their verified absence in swarm-command.md despite presence in README. The recommendation to examine additional source files or test the binary reflects the limitation that only one source file was provided, leaving open the possibility these features exist elsewhere in the codebase.]

No evidence was found of non-ruvnet repositories using claude-flow swarm commands in production, suggesting limited real-world validation of the tool's documented capabilities [WEB:https://github.com/jcolano/claude-flow][WEB:https://github.com/rdmolony/claude-flow-getting-started]. All usage examples traced back to the official README or derivative tutorial content [WEB:https://williamzujkowski.github.io/posts/supercharging-development-with-claude-flow-ai-swarm-intelligence-for-modern-engineering/][WEB:https://adrianco.medium.com/vibe-coding-is-so-last-month-my-first-agent-swarm-experience-with-claude-flow-414b0bd6f2f2].

^[Verdict: TRUE, Confidence: MEDIUM, Rationale: The web search results documented in the "External validation" section confirm the lack of independent usage examples beyond forks and tutorials. The repositories found (jcolano/claude-flow, avaloki108/claude-flow----web3, rdmolony/claude-flow-getting-started) are either forks with identical content or minimal getting-started guides without novel usage patterns. The blog posts by Zujkowski and Cockcroft reference the same examples as the official README. This negative finding (absence of production usage) is well-supported by the search results, but confidence is MEDIUM because exhaustive search across all possible sources is infeasible, and private/unlisted usage may exist but be undiscoverable.]

## References

### Knowledge base sources
- claude.md: TITO task specification and investigation requirements [KB:claude.md]
- claude-flow-readme.md: Official README from ruvnet/claude-flow v2.7.32 repository [KB:claude-flow-readme.md]
- swarm-command.md: TypeScript source code for swarm command implementation [KB:swarm-command.md]

### External sources
- GitHub repository: ruvnet/claude-flow official repository [WEB:https://github.com/ruvnet/claude-flow]
- Tutorial: Supercharging Development with Claude-Flow by William Zujkowski [WEB:https://williamzujkowski.github.io/posts/supercharging-development-with-claude-flow-ai-swarm-intelligence-for-modern-engineering/]
- Blog post: My First Agent Swarm Experience with claude-flow by Adrian Cockcroft [WEB:https://adrianco.medium.com/vibe-coding-is-so-last-month-my-first-agent-swarm-experience-with-claude-flow-414b0bd6f2f2]
- Repository: claude-flow-getting-started by rdmolony [WEB:https://github.com/rdmolony/claude-flow-getting-started]
- Repository fork: jcolano/claude-flow [WEB:https://github.com/jcolano/claude-flow]

^[Verdict: TRUE, Confidence: HIGH, Rationale: All KB sources are verified by their presence in the Read tool outputs. All external web sources are verified by WebSearch and WebFetch tool results showing the URLs and retrieved content. Each source was actually consulted during the research process and cited in the document body with inline tokens. The reference list accurately reflects the sources used.]
