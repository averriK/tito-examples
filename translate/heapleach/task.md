# Heap leach translation demo – EN → ES with TBX termbase

This task exercises the **new `translate` + `compile-translate` workflows** using
heap‑leach terminology and a minimal TBX termbase that encodes the
`pregnant solution` → `solución rica` mapping and forbids `solución embarazada`.

## Languages and domain

- Source language: `en-US` (technical English).
- Target language: `es-ES` (neutral technical Spanish).
- Domain: heap leaching / hydrometallurgy terminology.

## Documents

- KB directory for this demo: `kb/`.
- Document to translate: `kb/heapleach.source.en.md`.

Translate **the entire document**, preserving:
- All headings (levels and order).
- All paragraph boundaries (one audit footnote per paragraph).
- Inline formatting (bold, italics) and any inline math if present.

## Terminology and TBX

- This demo ships with a minimal TBX termbase under:
  - `kb/heapleach-es.glossary.tbx`
- The TBX file follows the profile in `docs/TRANSLATE_TBX_PROFILE.md` and
  contains a single concept:
  - EN: `pregnant solution` → `preferredTerm`.
  - ES: `solución rica` → `preferredTerm`.
  - ES: `solución embarazada` → `forbiddenTerm`.

**TBX RULES for this task (must follow `workflows/translate.session.md`):**

- Treat `pregnant solution` as a single technical term.
- When the source paragraph contains `pregnant solution`, you MUST:
  - Use `solución rica` as the main Spanish rendering.
  - NEVER use `solución embarazada` or any obvious variants.
- When you apply a TBX-governed mapping for this concept, it is RECOMMENDED that
  you mark the occurrence with a token:
  - `... solución rica [TBX:T0001] ...`

If no TBX-covered terms appear in a paragraph, the TBX rule is silent and you
fall back to general technical translation using KB and general knowledge.

## Structural and audit constraints

Use the **TRANSLATE session workflow contract** (`workflows/translate.session.md`):

- Preserve Markdown structure from `kb/heapleach.source.en.md`.
- For each non-empty paragraph, produce exactly one translated paragraph
  in Spanish, immediately followed by its audit footnote:

  ```text
  <translated paragraph in Spanish>
  ^[Verdict: TRUE|FALSE|UNCERTAIN, Confidence: HIGH|MEDIUM|LOW, Rationale: ...]
  ```

- Audit semantics (per `rules/audit.md`, specialized for translation):
  - `Verdict` evaluates **semantic fidelity** (not style).
  - `Confidence` reflects how sure you are that meaning is preserved.
  - `Rationale` must be short (1–2 sentences) and may mention TBX
    compliance (e.g., that `solución rica` was used instead of
    `solución embarazada`).

Do **not** include the English source text in the output; this is a
monolingual Spanish translation with per-paragraph audits.

## Expected CLI usage (for humans)

From the `tito-examples` root:

```bash
cd translate/heapleach

# 1) Run a session-level translation using TBX
tito translate \
  --id heapleach-es \
  --task task.md \
  --kb kb \
  --sessions 1

# 2) (Optional) Compile over multiple sessions once you have several runs
# tito compile-translate --id heapleach-es --sessions-dir sessions
```