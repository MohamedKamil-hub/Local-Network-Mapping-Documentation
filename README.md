# Local-Network-Mapping-Documentation


**Objective:** Safe local network discovery and topology generation using `nmap` → Graphviz.

**Safety notice:** All published outputs are sanitized. Raw scans are never committed.

## What I publish
- `demo/topology.svg` — anonymized topology
- `nmap-sanitized.xml` — anonymized nmap output
- `scripts/` — commands and parsing/anonymization scripts
- `demo/demo-terminal.gif` — sanitized run

## Quick run (local-only)
1. `bash scripts/scan.sh`  # only run on your own subnet
2. `python3 scripts/anonymize_nmap.py scan.xml nmap-sanitized.xml`
3. `python3 scripts/generate_graph.py nmap-sanitized.xml > demo/topology.dot`
4. `dot -Tsvg demo/topology.dot -o demo/topology.svg`

## Notes
- Do **not** scan networks you do not own or have permission to scan.
- Keep mapping keys private — do not commit them.
