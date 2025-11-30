---
layout: default
title: Research workflow examples
---

# Research workflow examples

This page indexes the **research** workflow scenarios stored in this repository under `research/`.

For the semantics and CLI options of `tito research` (and `tito compile-research`), rely on the main TITO documentation:

- Main repo: https://github.com/averriK/tito
- Quick start: [`docs/QUICKSTART.md`](https://github.com/averriK/tito/blob/main/docs/QUICKSTART.md)

## Directory layout

```text
research/
├── claude/
├── dedup/
├── epistemic/
├── louvicourt/
├── mmax/
├── r1/
├── r2/
├── r4/
├── reitfontein/
└── zotero/
```

Each scenario follows the usual pattern:

```text
research/<scenario>/
├── kb/           # knowledge base (Markdown, XML, etc.)
├── sessions/     # one or more run-YYYYMMDD_HHMMSS folders
└── task*.md      # task / prompt files
```

## Scenarios

Short, factual summaries based on the actual `task*.md` files in this repo:

- `research/claude` – investigation of `claude-flow` swarm parameters that are actually implemented and used, with a focus on which flags TITO should rely on.
- `research/dedup` – methods to identify the same earthquake in both USGS ComCat and ISC Bulletin catalogs without corrupting the database.
- `research/epistemic` – epistemic uncertainty analysis for the Reitfontein Fault in a PSHA context (logic-tree weights, slip rates, recurrence).
- `research/louvicourt` – expert peer review questions for a WSP PSHA study used as KB, focusing on seismotectonic setting and record selection.
- `research/mmax` – evaluation of Mmax = 7.2 for the Reitfontein Fault, including rupture area and consistency with stable continental crust.
- `research/r1` – benchmark section comparing PSHA models (SRC, SRK, GEM) using logic-tree GMPE definitions stored in KB XML files.
- `research/r2` – executive summary and recommendations (in English) for epistemic-uncertainty treatment of the Reitfontein Fault.
- `research/r4` – conclusions and recommendations for correcting PSHA results given issues with Reitfontein Fault assumptions.
- `research/reitfontein` – completion and improvement of `introduction.md` and `benchmark.md` chapters for the Reitfontein PSHA report.
- `research/zotero` – Zotero MCP smoke test: verifying Zotero-backed retrieval inside claude-flow with tokenized `[ZOTERO:<key>]` citations.

## How to reuse

1. Read the `task*.md` files to understand the objective and constraints.
2. Inspect `kb/` and `sessions/run-*/` to see how TITO structures research runs.
3. Copy and adapt tasks/KBs into your own project as described in the main TITO quick start.
