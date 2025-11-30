---
layout: default
title: Retrieve workflow examples
---

# Retrieve workflow examples

This page indexes **retrieve** workflow scenarios under `retrieve/`.

The `tito retrieve` workflow is used for PDF/DOCX → Markdown ingestion with validation. For exact CLI semantics, see the main TITO docs:

- Main repo: https://github.com/averriK/tito
- Quick start: [`docs/QUICKSTART.md`](https://github.com/averrik/tito/blob/main/docs/QUICKSTART.md)

## Directory layout

```text
retrieve/
├── antamina/
├── camsig/
├── eeri/
├── louvicourt/
└── mse/
```

Each scenario follows the usual pattern:

```text
retrieve/<scenario>/
├── kb/           # extracted Markdown and supporting files
├── sessions/     # retrieve session logs/results
└── task*.md      # retrieve task definitions (source documents, constraints)
```

## How to use

1. Inspect `task*.md` in each scenario to see how source documents are specified.
2. Look at `kb/` to understand how retrieve transforms inputs to Markdown.
3. Use these patterns when wiring your own `tito retrieve` tasks and KB locations.
