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
  <scenario>/
  <scenario>/
  ...
```

Each scenario follows the usual pattern:

```text
research/<scenario>/
├── kb/           # knowledge base (Markdown, XML, etc.)
├── sessions/     # one or more run-YYYYMMDD_HHMMSS folders
└── task*.md      # task / prompt files
```

The **set of scenarios is intentionally unstable**: examples are added and removed frequently. Do not treat this page as a canonical list; use your git tooling (`ls research/`, `git ls-files`, etc.) to see what exists at any given time.

## How to use this directory

1. List the current scenarios under `research/`.
2. For any scenario, read its `task*.md`, `kb/` and `sessions/` contents.
3. Consult the main TITO docs for how to interpret and reproduce research runs.
