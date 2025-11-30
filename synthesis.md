---
layout: default
title: Synthesis workflow examples
---

# Synthesis workflow examples

This page indexes **synthesis** workflow scenarios under `synthesis/`.

The `tito synthesis` and `tito compile-synthesis` workflows are used for local-only, audited executive summaries over KB documents. For full semantics, see the main TITO documentation:

- Main repo: https://github.com/averrik/tito
- Quick start: [`docs/QUICKSTART.md`](https://github.com/averrik/tito/blob/main/docs/QUICKSTART.md)

## Directory layout

```text
synthesis/
└── reitfontein/
```

The scenario in this repo follows the usual pattern:

```text
synthesis/reitfontein/
├── kb/           # source document(s) to be summarized
├── sessions/     # synthesis and compile-synthesis runs
└── task*.md      # synthesis task definitions
```

Use this as a template for setting up your own synthesis projects.
