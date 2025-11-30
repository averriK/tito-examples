---
layout: default
title: Review workflow examples
---

# Review workflow examples

This page indexes **review** workflow scenarios under `review/`.

The `tito review` and `tito compile-review` workflows are used for deep audits of KB documents, producing consensus audit reports. For details, see the main TITO documentation:

- Main repo: https://github.com/averrik/tito
- Quick start: [`docs/QUICKSTART.md`](https://github.com/averrik/tito/blob/main/docs/QUICKSTART.md)

## Directory layout

```text
review/
├── antamina/
├── camsig/
├── eeri/
├── hazard/
└── mse/
```

Each scenario normally contains:

```text
review/<scenario>/
├── kb/           # KB documents being audited
├── sessions/     # review / compile-review / enhance runs
└── task*.md      # review and enhance task definitions
```

Use the `task*.md` files and KB contents to understand the audit questions and adapt them to your own projects.
