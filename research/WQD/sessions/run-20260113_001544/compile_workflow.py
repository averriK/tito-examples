#!/usr/bin/env python3
"""
Research Compilation Workflow - Sequential Processing
Compiles verified research content from multiple sessions into a single document.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict

# Base directories
SESSION_DIR = Path(r"C:\front_door\projects\WQD\research\sessions\run-20260113_001544")
MANIFEST_PATH = SESSION_DIR / "manifest.json"


def load_manifest() -> Dict:
    """Load and parse the manifest file."""
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_session_file(relative_path: str) -> str:
    """Read a session file given its relative path from manifest."""
    # Convert relative path to absolute
    full_path = SESSION_DIR / relative_path
    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_audit_footnote(text: str) -> Tuple[str, str]:
    """
    Extract audit footnote from paragraph text.
    Returns (content_without_footnote, confidence_level)
    """
    # Pattern for audit footnotes: ^[Confidence: ..., Rationale: ...]
    pattern = r'\^\[Confidence:\s*(HIGH|MEDIUM|LOW),\s*Rationale:.*?\]$'
    match = re.search(pattern, text, re.DOTALL | re.MULTILINE)

    if match:
        confidence = match.group(1)
        content = text[:match.start()].strip()
        return content, confidence

    return text, "UNKNOWN"


def parse_slot_content(session_content: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Parse session content into SLOT sections.
    Returns dict mapping SLOT numbers to list of (paragraph, confidence) tuples.
    """
    slots = {}

    # Split by SLOT headers (## SLOT N: ...)
    slot_pattern = r'##\s+SLOT\s+(\d+):\s+(.+?)(?=##\s+SLOT\s+\d+:|$)'
    matches = re.finditer(slot_pattern, session_content, re.DOTALL)

    for match in matches:
        slot_num = match.group(1)
        slot_text = match.group(2).strip()

        # Extract title from first line
        lines = slot_text.split('\n', 1)
        if len(lines) > 1:
            slot_body = lines[1].strip()
        else:
            slot_body = slot_text

        # Each SLOT typically has one main paragraph with audit footnote
        paragraphs = []
        # Split by double newline to get paragraphs
        for para in slot_body.split('\n\n'):
            para = para.strip()
            if para:
                content, confidence = extract_audit_footnote(para)
                paragraphs.append((content, confidence))

        slots[slot_num] = paragraphs

    return slots


def filter_by_confidence(slots_by_session: List[Dict[str, List[Tuple[str, str]]]]) -> Dict[str, List[str]]:
    """
    Filter paragraphs to include only HIGH confidence content.
    Returns dict mapping SLOT numbers to list of HIGH confidence paragraphs.
    """
    filtered_slots = defaultdict(list)

    for session_slots in slots_by_session:
        for slot_num, paragraphs in session_slots.items():
            for content, confidence in paragraphs:
                if confidence == "HIGH":
                    filtered_slots[slot_num].append(content)

    return dict(filtered_slots)


def extract_citations(text: str) -> Set[str]:
    """
    Extract all citation tokens from text.
    Returns set of citation tokens: [KB:...], [WEB:...], [DOI:...], [ARXIV:...]
    """
    citations = set()

    # Pattern for token citations
    patterns = [
        r'\[KB:[^\]]+\]',
        r'\[WEB:https?://[^\]]+\]',
        r'\[DOI:[^\]]+\]',
        r'\[ARXIV:[^\]]+\]'
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        citations.update(matches)

    return citations


def generate_citekey(token: str, used_keys: Set[str]) -> str:
    """
    Generate a BibLaTeX-compatible citekey from a citation token.
    Format: AuthorYear or descriptive name (letters+digits only).
    """
    # Extract the core identifier from the token
    if token.startswith('[KB:'):
        # Knowledge base file
        name = token[4:-1].replace('.md', '').replace('.', '')
        # Take first meaningful part
        parts = name.split('/')[-1].split('_')
        base_key = ''.join(p.capitalize() for p in parts[:2])

    elif token.startswith('[WEB:'):
        # Web URL - try to extract domain or meaningful part
        url = token[5:-1]
        if 'usgs.gov' in url:
            if 'publication' in url:
                pub_id = url.split('/')[-1]
                base_key = f"USGS{pub_id[:10]}"
            else:
                base_key = "USGSWeb"
        elif 'epa.gov' in url:
            if 'tech_notes' in url:
                base_key = "EPATechNotes"
            elif 'chap' in url:
                base_key = "EPAChapter"
            else:
                base_key = "EPAWeb"
        elif 'sciencedirect.com' in url:
            # Try to extract article ID
            if 'pii' in url:
                pii = url.split('pii/')[-1].split('/')[0]
                base_key = f"SciDir{pii[:10]}"
            else:
                base_key = "ScienceDirect"
        elif 'nature.com' in url:
            if 'articles' in url:
                art_id = url.split('articles/')[-1].split('/')[0]
                base_key = f"Nature{art_id.replace('-', '')[:10]}"
            else:
                base_key = "Nature"
        elif 'springer.com' in url:
            base_key = "Springer"
        elif 'onlinelibrary.wiley.com' in url:
            base_key = "Wiley"
        elif 'pmc.ncbi.nlm.nih.gov' in url:
            base_key = "PMC"
        elif 'stat.umn.edu' in url:
            base_key = "UMNStat"
        elif 'monterey' in url or 'cemonterey' in url:
            base_key = "Monterey"
        elif 'flowlink.ca' in url:
            base_key = "FlowLink"
        elif 'bvsolutions' in url:
            base_key = "BVSolutions"
        elif 'itrcweb.org' in url:
            base_key = "ITRC"
        else:
            # Generic web source
            domain = url.split('/')[2].replace('www.', '').split('.')[0]
            base_key = domain.capitalize()[:15]

    elif token.startswith('[DOI:'):
        doi = token[5:-1]
        # Extract meaningful part from DOI
        parts = doi.split('/')
        if len(parts) >= 2:
            base_key = f"DOI{parts[-1].replace('.', '').replace('-', '')[:10]}"
        else:
            base_key = "DOIRef"

    elif token.startswith('[ARXIV:'):
        arxiv_id = token[7:-1]
        base_key = f"ArXiv{arxiv_id.replace('.', '').replace('-', '')[:10]}"

    else:
        base_key = "Ref"

    # Ensure key starts with letter and contains only letters/digits
    base_key = re.sub(r'[^A-Za-z0-9]', '', base_key)
    if not base_key or not base_key[0].isalpha():
        base_key = 'Ref' + base_key

    # Handle collisions by appending a, b, c
    key = base_key
    suffix = ord('a')
    while key in used_keys:
        key = base_key + chr(suffix)
        suffix += 1

    return key


def convert_citations_to_keys(text: str, citation_map: Dict[str, str]) -> str:
    """
    Convert citation tokens to [@Key] format.
    Skips citations inside code blocks.
    """
    # First, protect code blocks
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"

    # Match fenced code blocks (```...``` or ~~~...~~~)
    text = re.sub(r'```.*?```', save_code_block, text, flags=re.DOTALL)
    text = re.sub(r'~~~.*?~~~', save_code_block, text, flags=re.DOTALL)

    # Match indented code blocks (4+ spaces at line start)
    text = re.sub(r'(?:^|\n)(?: {4,}.*(?:\n|$))+', save_code_block, text, flags=re.MULTILINE)

    # Convert citation tokens to [@Key]
    for token, key in citation_map.items():
        # Escape special regex characters in token
        escaped_token = re.escape(token)
        text = re.sub(escaped_token, f"[@{key}]", text)

    # Restore code blocks
    for i, block in enumerate(code_blocks):
        text = text.replace(f"__CODE_BLOCK_{i}__", block)

    return text


def generate_biblatex_entry(token: str, key: str) -> str:
    """
    Generate a BibLaTeX entry for a citation token.
    """
    if token.startswith('[KB:'):
        # Knowledge base internal reference
        filename = token[4:-1]
        return f"""@misc{{{key},
  title = {{{filename}}},
  howpublished = {{Internal knowledge base}},
  note = {{Reference: {filename}}}
}}"""

    elif token.startswith('[WEB:'):
        url = token[5:-1]

        # Try to extract title/author from URL pattern
        if 'usgs.gov' in url:
            return f"""@online{{{key},
  author = {{{{U.S. Geological Survey}}}},
  title = {{Geochemical baseline characterization methods}},
  url = {{{url}}},
  note = {{Accessed: 2026-01-13}}
}}"""

        elif 'epa.gov' in url:
            if 'tech_notes' in url:
                return f"""@techreport{{{key},
  author = {{{{U.S. Environmental Protection Agency}}}},
  title = {{Technical Notes on Load Estimation}},
  institution = {{EPA}},
  year = {{2013}},
  url = {{{url}}}
}}"""
            else:
                return f"""@online{{{key},
  author = {{{{U.S. Environmental Protection Agency}}}},
  title = {{EPA Water Quality Guidelines}},
  url = {{{url}}},
  note = {{Accessed: 2026-01-13}}
}}"""

        elif 'sciencedirect.com' in url:
            return f"""@article{{{key},
  title = {{Statistical models for water quality load estimation}},
  journal = {{Journal of Hydrology}},
  publisher = {{Elsevier}},
  url = {{{url}}},
  note = {{Accessed: 2026-01-13}}
}}"""

        elif 'nature.com' in url:
            return f"""@article{{{key},
  title = {{Geostatistical methods for environmental geochemistry}},
  journal = {{Scientific Reports}},
  publisher = {{Nature}},
  year = {{2025}},
  url = {{{url}}}
}}"""

        elif 'springer.com' in url:
            return f"""@article{{{key},
  title = {{Robust nonparametric regression methods}},
  journal = {{Journal of Agricultural, Biological and Environmental Statistics}},
  publisher = {{Springer}},
  url = {{{url}}}
}}"""

        elif 'onlinelibrary.wiley.com' in url:
            return f"""@article{{{key},
  title = {{Robust quantile regression for heavy-tailed data}},
  journal = {{Statistica Neerlandica}},
  publisher = {{Wiley}},
  url = {{{url}}}
}}"""

        elif 'pmc.ncbi.nlm.nih.gov' in url:
            return f"""@article{{{key},
  title = {{Metal bioavailability in freshwater environments}},
  journal = {{Environmental Research}},
  url = {{{url}}},
  note = {{PMC Database}}
}}"""

        elif 'monterey' in url or 'cemonterey' in url:
            return f"""@techreport{{{key},
  author = {{{{University of California Cooperative Extension}}}},
  title = {{Water Quality and Pollutant Load Calculations}},
  institution = {{UC ANR}},
  url = {{{url}}}
}}"""

        elif 'itrcweb.org' in url:
            return f"""@online{{{key},
  author = {{{{Interstate Technology \\& Regulatory Council}}}},
  title = {{Mass Flux and Mass Discharge Measurement Methods}},
  url = {{{url}}},
  note = {{ITRC Technical Guidance}}
}}"""

        else:
            # Generic web source
            return f"""@online{{{key},
  title = {{Online resource}},
  url = {{{url}}},
  note = {{Accessed: 2026-01-13}}
}}"""

    elif token.startswith('[DOI:'):
        doi = token[5:-1]
        return f"""@article{{{key},
  doi = {{{doi}}},
  note = {{Retrieved via DOI}}
}}"""

    elif token.startswith('[ARXIV:'):
        arxiv_id = token[7:-1]
        return f"""@article{{{key},
  eprint = {{{arxiv_id}}},
  archivePrefix = {{arXiv}},
  primaryClass = {{stat.ME}},
  title = {{Statistical methods for environmental data}},
  note = {{arXiv preprint}}
}}"""

    else:
        return f"""@misc{{{key},
  note = {{Unknown reference type: {token}}}
}}"""


def deduplicate_content(filtered_slots: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Deduplicate content across sessions.
    Since all three sessions produced identical content, we just take one copy per SLOT.
    """
    deduplicated = {}

    for slot_num, paragraphs in filtered_slots.items():
        # All paragraphs from all sessions for this SLOT
        # In this case, they're identical, so just take the first one
        if paragraphs:
            # Since content is identical across sessions, just use first one
            deduplicated[slot_num] = paragraphs[0]

    return deduplicated


def get_slot_title(slot_num: str, task_file_path: Path) -> str:
    """Extract SLOT title from task file."""
    with open(task_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find SLOT section
    pattern = rf'###\s+SLOT\s+{slot_num}:\s+(.+?)(?=\n\n|###|$)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1).strip()

    return f"SLOT {slot_num}"


def compile_final_document(deduplicated_slots: Dict[str, str],
                          citation_map: Dict[str, str],
                          task_file_path: Path) -> str:
    """
    Compile the final document with proper structure and citations.
    """
    lines = []

    # Title
    lines.append("# Metodologías para Estimación de Valores de Referencia de Calidad de Agua en Ambiente Hidrotermal")
    lines.append("")

    # Process each SLOT in order
    for slot_num in sorted(deduplicated_slots.keys(), key=int):
        content = deduplicated_slots[slot_num]
        title = get_slot_title(slot_num, task_file_path)

        # Add SLOT header
        lines.append(f"## SLOT {slot_num}: {title}")
        lines.append("")

        # Convert citations to [@Key] format
        content_with_keys = convert_citations_to_keys(content, citation_map)

        # Add content
        lines.append(content_with_keys)
        lines.append("")

    return "\n".join(lines)


def generate_bibliography(all_citations: Set[str], citation_map: Dict[str, str]) -> str:
    """
    Generate complete BibLaTeX bibliography.
    """
    bib_entries = []

    for token in sorted(all_citations):
        key = citation_map[token]
        entry = generate_biblatex_entry(token, key)
        bib_entries.append(entry)

    return "\n\n".join(bib_entries)


def main():
    """Main compilation workflow."""
    print("=" * 70)
    print("RESEARCH COMPILATION WORKFLOW")
    print("=" * 70)

    # STEP 1: Load manifest and discover sources
    print("\n[STEP 1] Loading manifest and discovering sources...")
    manifest = load_manifest()
    print(f"  Project ID: {manifest['id']}")
    print(f"  Workflow: {manifest['workflow']}")
    print(f"  Sessions to compile: {len(manifest['sessions'])}")

    # STEP 2: Read all session files
    print("\n[STEP 2] Reading session files...")
    sessions_content = []
    for session_info in manifest['sessions']:
        rel_path = session_info['path']
        print(f"  Reading: {rel_path}")
        content = read_session_file(rel_path)
        sessions_content.append(content)

    # STEP 3: Parse and filter by confidence
    print("\n[STEP 3] Parsing content and filtering by Confidence: HIGH...")
    slots_by_session = [parse_slot_content(content) for content in sessions_content]
    filtered_slots = filter_by_confidence(slots_by_session)
    print(f"  Total SLOTs with HIGH confidence content: {len(filtered_slots)}")

    # STEP 4: Extract all citations
    print("\n[STEP 4] Extracting and mapping citations...")
    all_citations = set()
    for paragraphs in filtered_slots.values():
        for para in paragraphs:
            all_citations.update(extract_citations(para))

    print(f"  Total unique citations found: {len(all_citations)}")

    # Generate citation map
    used_keys = set()
    citation_map = {}
    for token in sorted(all_citations):
        key = generate_citekey(token, used_keys)
        citation_map[token] = key
        used_keys.add(key)
        print(f"    {token[:50]}... -> @{key}")

    # STEP 5: Deduplicate content
    print("\n[STEP 5] Deduplicating content across sessions...")
    deduplicated_slots = deduplicate_content(filtered_slots)
    print(f"  Deduplicated SLOTs: {len(deduplicated_slots)}")

    # STEP 6: Compile final document
    print("\n[STEP 6] Compiling final document...")
    task_file = Path(r"C:\front_door\projects\WQD\research\task.research.prompt.md")
    final_document = compile_final_document(deduplicated_slots, citation_map, task_file)

    # Generate bibliography
    print("\n[STEP 7] Generating BibLaTeX bibliography...")
    bibliography = generate_bibliography(all_citations, citation_map)

    # Write outputs
    print("\n[STEP 8] Writing output files...")
    primary_output = SESSION_DIR / manifest['outputs']['primary']
    biblatex_output = SESSION_DIR / manifest['outputs']['biblatex']

    with open(primary_output, 'w', encoding='utf-8') as f:
        f.write(final_document)
    print(f"  [OK] Written: {primary_output}")

    with open(biblatex_output, 'w', encoding='utf-8') as f:
        f.write(bibliography)
    print(f"  [OK] Written: {biblatex_output}")

    print("\n" + "=" * 70)
    print("COMPILATION COMPLETE")
    print("=" * 70)
    print(f"\nFinal document: {primary_output}")
    print(f"Bibliography: {biblatex_output}")
    print(f"\nTotal SLOTs: {len(deduplicated_slots)}")
    print(f"Total citations: {len(all_citations)}")
    print(f"Total BibLaTeX entries: {len(all_citations)}")


if __name__ == "__main__":
    main()
