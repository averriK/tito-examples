---
layout: default
title: TITO Examples - Home
---

# TITO Examples

Welcome to the **TITO** (Text-based Intelligent Task Orchestrator) examples collection, an AI agent-based task orchestration system for intelligent technical documentation processing.

## 🎯 Overview

This site documents real-world TITO usage examples across different domains:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🔬 Research</h3>
<p>Automated research on complex technical topics with deep analysis and bibliographic synthesis.</p>
<a href="research/">View examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>📥 Retrieve</h3>
<p>Intelligent information extraction from PDF, Word, and other unstructured sources.</p>
<a href="retrieve/">View examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>✏️ Review</h3>
<p>Critical review and improvement of technical content with contextual suggestions.</p>
<a href="review/">View examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🔗 Synthesis</h3>
<p>Information consolidation from multiple sources into coherent documents.</p>
<a href="synthesis/">View examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>🌐 Translate</h3>
<p>Contextual translation of technical documentation preserving specialized terminology.</p>
<a href="translate/">View examples →</a>
</div>

<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px;">
<h3>📖 Glossary</h3>
<p>Automatic generation of technical glossaries with contextual definitions.</p>
<a href="glossary/">View examples →</a>
</div>

</div>

## 🚀 Featured examples

### Seismic hazard assessment (Louvicourt)
- **Research**: [Deep seismic hazard analysis](research/#louvicourt)
- **Retrieve**: [Technical study data extraction](retrieve/#louvicourt)
- **Translate**: [Translation to Spanish](translate/#louvicourt)

### Mining projects (Reitfontein)
- **Research**: [Mine seismic evaluation](research/#reitfontein)
- **Synthesis**: [Assessment synthesis](synthesis/#reitfontein)

### Ground Motion Models
- **Research**: [GMM Logic Trees](research/#gmmlt)
- **Research**: [Epistemic uncertainty](research/#epistemic)

## 📊 Statistics

This repository contains:
- **12+** research examples
- **5** retrieve examples
- **4** review examples
- **1** synthesis example
- **1** translate example
- **1** glossary example

## 🔍 How to use this site

1. **Browse by workflow type**: Use the top navigation to explore examples by category
2. **Review complete sessions**: Each example includes execution sessions with full logs
3. **Examine results**: The `*.compile.*.md` files contain consolidated results
4. **Adapt to your case**: Use the `*.session.json` configurations as templates

## 📖 Example structure

Each example follows this structure:

```
example/
├── kb/                          # Knowledge base (input documents)
├── sessions/                    # Execution sessions
│   └── run-YYYYMMDD_HHMMSS/    # Execution timestamp
│       ├── agent.out           # Complete agent log
│       ├── *.session.json      # Session configuration
│       └── *.compile.*.md      # Compiled result
└── task.*.md                   # Task definition
```

## 🛠️ Technology

TITO uses:
- AI agents (LLMs: GPT-4, Claude, etc.)
- Natural language processing
- Structured information extraction
- Knowledge synthesis and consolidation
- JSON-configurable workflows

## 🤝 Contributing

Have an interesting TITO usage example? Contribute to the repository:

1. Fork the [repository](https://github.com/averriK/tito-examples)
2. Add your example following the existing structure
3. Create a Pull Request with detailed description

## 📄 License

MIT License

## 👤 Contact

**averriK**
- GitHub: [@averriK](https://github.com/averriK)

---

*Last updated: November 2025*
