# TITO Examples

[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://averrik.github.io/tito-examples/)

This repository contains usage examples of **TITO** (Text-based Intelligent Task Orchestrator), demonstrating different workflows for intelligent technical documentation processing.

## 🎯 What is TITO

TITO is an AI agent-based task orchestration system that enables:
- **Automated research**: deep analysis of technical topics
- **Information retrieval**: extraction and processing of documents
- **Enhanced review**: critical analysis and content improvement
- **Synthesis**: consolidation of multiple sources
- **Translation**: contextual translation of technical documentation
- **Glossaries**: automatic generation of terminology

## 📁 Repository structure

```
tito-examples/
├── glossary/      # Technical glossary generation examples
├── research/      # Automated research on specific topics
├── retrieve/      # PDF/Word document extraction and processing
├── review/        # Technical content review and improvement
├── synthesis/     # Multi-source information consolidation
└── translate/     # Technical documentation translation
```

## 🚀 Featured examples

### Research
- **r1-r4**: Research series on specific topics
- **louvicourt**: Seismic hazard analysis for mines
- **reitfontein**: Seismic evaluation of mining projects
- **epistemic**: Epistemic uncertainty research
- **gmmLT**: Ground Motion Model Logic Trees

### Retrieve
- **louvicourt**: Information extraction from seismic hazard studies
- **antamina**: Mining documentation processing
- **camsig**: Seismic catalog data retrieval

### Review
- **hazard**: Seismic hazard assessment review
- **camsig**: Seismic catalog documentation improvement

### Synthesis
- **reitfontein**: Complete seismic evaluation synthesis

### Translate
- **louvicourt**: Technical studies translation to Spanish

## 📖 Documentation

Visit the [complete documentation](https://averrik.github.io/tito-examples/) to see detailed examples, session results, and usage guides.

## 🔍 Example structure

Each example typically contains:
```
example/
├── kb/                          # Knowledge base (input files)
├── sessions/                    # Execution sessions
│   └── run-YYYYMMDD_HHMMSS/    # Individual session
│       ├── agent.out           # Execution log
│       ├── *.session.json      # Session configuration
│       └── *.compile.*.md      # Compiled result
└── task.*.md                   # Task definition
```

## 🛠️ Typical usage

1. Review the example in the corresponding directory
2. Examine the configuration in `*.session.json`
3. Review the task in `task.*.md`
4. Explore compiled results in `sessions/run-*/`

## 📋 Requirements

- Python 3.8+
- TITO framework (installation and configuration per official docs)
- LLM API access (OpenAI, Anthropic, etc.)

## 🤝 Contributing

This repository serves as an examples reference. To contribute:
1. Fork the repository
2. Create a branch for your example (`git checkout -b feature/new-example`)
3. Add your example following the existing structure
4. Commit and push (`git commit -am 'Add: new example'`)
5. Create a Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 👤 Author

**averriK**
- GitHub: [@averriK](https://github.com/averriK)

## 🔗 Useful links

- [Examples documentation](https://averrik.github.io/tito-examples/)
- [TITO Framework](https://github.com/averriK/tito) (if applicable)

---

*Last updated: November 2025*
