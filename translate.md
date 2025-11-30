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
└── louvicourt/
```

Typical contents:

```text
translate/louvicourt/
├── kb/           # source documents in the original language
├── sessions/     # glossary + translate runs
└── task*.md      # translation task definitions
```

Use these to understand how glossary-driven translation is configured in TITO.
