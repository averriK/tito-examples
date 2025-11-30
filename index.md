---
layout: default
title: TITO examples gallery
---

# TITO examples gallery

This site hosts **example workflow runs** for [TITO](https://github.com/averriK/tito) (Truth-Informed Technical Output).

TITO itself (CLI, installation, architecture, and full docs) lives in the main repo and its GitHub Pages site. This `tito-examples` site is intentionally minimal: it only indexes example projects and their artifacts.

## Core TITO documentation

- Main repository: https://github.com/averriK/tito
- Quick start guide: [`docs/QUICKSTART.md`](https://github.com/averriK/tito/blob/main/docs/QUICKSTART.md)

For workflow semantics (what `research`, `review`, `retrieve`, `glossary`, `translate`, `synthesis`, etc. actually do) always rely on the main TITO documentation.

## Workflow galleries

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🔬 Research</h3>
<p>Example projects using the <code>tito research</code> workflow over KB documents and tasks.</p>
<a href="research/">Browse research examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>📥 Retrieve</h3>
<p>Example runs of the <code>tito retrieve</code> workflow for PDF/DOCX → Markdown ingestion.</p>
<a href="retrieve/">Browse retrieve examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>✏️ Review</h3>
<p>Deep review and audit examples built with <code>tito review</code> (often paired with compile-review/enhance).</p>
<a href="review/">Browse review examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🔗 Synthesis</h3>
<p>Local-only audited synthesis examples built with <code>tito synthesis</code> / <code>tito compile-synthesis</code>.</p>
<a href="synthesis/">Browse synthesis examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🌐 Translate</h3>
<p>Audited translation workflows that use glossary+translate skills on KB documents.</p>
<a href="translate/">Browse translate examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>📖 Glossary</h3>
<p>Domain glossary extraction workflows (when present), built with <code>tito glossary</code>.</p>
<a href="glossary/">Browse glossary examples →</a>
</div>

</div>

## Repository layout

```text
tito-examples/
├── glossary/
├── research/
├── retrieve/
├── review/
├── synthesis/
└── translate/
```

Each scenario directory typically contains:

```text
<workflow>/<scenario>/
├── kb/           # knowledge base for the scenario
├── sessions/     # one or more `run-YYYYMMDD_HHMMSS` execution folders
└── task*.md      # task / prompt files for TITO
```

The exact structure can vary a bit per workflow, but `kb + task*.md + sessions/` is the standard pattern.

## Using these examples

1. **Install TITO** following the quick start guide in the main repo.
2. **Open a scenario** (for example `research/r1`, `research/claude`, or `retrieve/louvicourt`).
3. Read the `task*.md` files and the contents of `kb/` to understand the problem setup.
4. Inspect `sessions/run-*/` to see how TITO structures sessions and compiled outputs.
5. Use these as blueprints when designing your own tasks and KBs.

This site is intentionally conservative: it describes only what is actually present in the repository and delegates all workflow semantics to the primary TITO documentation.
