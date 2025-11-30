# tito-examples

This repository contains **end-to-end workflow runs and artifacts generated with TITO (Truth-Informed Technical Output)**.

TITO itself lives in the main project:
- GitHub: https://github.com/averriK/tito
- Quick start guide: [`docs/QUICKSTART.md`](https://github.com/averriK/tito/blob/main/docs/QUICKSTART.md)

This `tito-examples` repo does **not** contain the CLI implementation. It is a companion repository that stores concrete projects and their outputs.

## What is TITO?

TITO is a Bash CLI that orchestrates `claude-flow` for **multi-agent technical document generation with audited claims and traceable sources**. Every workflow run produces structured sessions under `sessions/run-*/` plus user-facing compiled reports.

For a full description of features, commands and workflows, always refer to the main [`tito`](https://github.com/averriK/tito) README and docs.

## Repository layout

```text
tito-examples/
├── glossary/   # glossary workflow runs (when present)
├── research/   # research workflow runs
├── retrieve/   # retrieve workflow runs
├── review/     # review workflow runs
├── synthesis/  # synthesis workflow runs
└── translate/  # translate workflow runs
```

Each scenario directory under these folders typically looks like:

```text
<workflow>/<scenario>/
├── kb/           # knowledge base for the scenario
├── sessions/     # one or more `run-YYYYMMDD_HHMMSS` execution folders
└── task*.md      # task / prompt files for TITO
```

The exact filenames vary slightly by workflow, but the pattern `kb + task*.md + sessions/` is consistent across the examples in this repository.

## How to use these examples

1. **Install and configure TITO** following `docs/QUICKSTART.md` in the main repo.
2. **Open any scenario directory** under `research/`, `retrieve/`, `review`, `synthesis/`, `translate/`, etc.:
   - Read `task.md` / `task.prompt.md` to see the prompt used.
   - Inspect `kb/` to understand the knowledge base.
   - Inspect `sessions/run-*/` for raw outputs and compiled artifacts.
3. **Use the tasks and KB files as templates** for your own projects, adjusting paths, IDs, and KB content as described in the main TITO documentation.
4. **Remember:** scenario names and counts are intentionally unstable; this repo is not a canonical catalog of examples, just a working set of projects and regression fixtures.

Conceptual explanations of what each workflow type (`research`, `review`, `retrieve`, `glossary`, `translate`, `synthesis`, etc.) does are maintained in the **primary TITO documentation**, not here.

## GitHub Pages

GitHub Pages for this repository are published at:

- https://averrik.github.io/tito-examples/

The site provides a simple index of the example workflows and links back to the primary TITO docs.

## License

MIT License — see `LICENSE` in this repository.
