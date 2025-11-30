---
layout: default
title: Translate workflow examples
---

# Translate workflow examples

This page indexes **translate** workflow scenarios under `translate/`.

The `tito glossary` + `tito translate` workflows implement audited technical translation using domain glossaries. For details, see the main TITO documentation and translation workflow docs in the main repo.

- Main repo: https://github.com/averrik/tito
- Quick start: [`docs/QUICKSTART.md`](https://github.com/averrik/tito/blob/main/docs/QUICKSTART.md)

## Directory layout

```text
translate/
  <scenario>/
  <scenario>/
  ...
```

Typical contents for a scenario:

```text
translate/<scenario>/
├── kb/           # source documents in the original language
├── sessions/     # glossary + translate runs
└── task*.md      # translation task definitions
```

Scenario names and contents change frequently; use `ls translate/` (or similar) to discover current translation projects.
