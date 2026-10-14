# CR-BO-03: Authorship Cardinal Rule (Org-Wide Propagation Slice)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-03 |
| **Title** | Authorship Cardinal Rule (R1, R2) - Org-Wide Propagation Slice (dea-catalog-business-objects) |
| **Status** | Accepted (per user directive 2026-10-13) |
| **Layer** | L1 (Business Object Catalog) |
| **Depends on** | CR-BP-118 (org-wide authorship cardinal rule, main authority) |
| **Companion to** | CR-DEA-BC-34 (BC slice), CR-OU-04 (OU slice, forthcoming), CR-MF-04 (metaframework slice, forthcoming) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-13 |

## 1. The cardinal rule (pinned)

Two cardinal rules from CR-BP-118 (org-wide authority) are propagated to this
repo (dea-catalog-business-objects):

- **R1 (Authorship-field cardinal rule)**: every authorship-bearing field must
  carry a value from the allowlist `{Emmanuel A. Otchere, TechNeHub Labs}`.
  Substring matches against the denylist
  `{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}` are
  blocking (AUT-001).
- **R2 (Named-role file cardinal rule)**: any file or field whose purpose is
  to name a person playing a named role must carry the canonical identity.

The rules are CR-level (immutable by a gate change) and governance-doc-level
(immutable by a code change).

## 2. The retro sweep (BO-repo scope)

2 files, 2 textual replacements:

| File | Field | Replaced |
|---|---|---|
| change-requests/CR-BO-01-ecf-domain-enum-migration.md | `**Owner**` | `Coder (for eaojnr)` -> `Emmanuel A. Otchere` |
| change-requests/CR-BO-02-ecf-domain-enum-migration-v250.md | `**Owner**` | `Coder (for eaojnr)` -> `Emmanuel A. Otchere` |

Total: 2 files, 2 textual replacements. 0 entity content changes; 0 id
changes; 0 cross-reference changes.

The BO repo has no entity YAMLs, no CITATION.cff, and no catalog-research
YAML; the field set is the 118a baseline (`**Owner**`, `**Author**`). No
per-repo extension is needed.

## 3. The gate (BO-repo, blocking)

- **AUT-001 (blocking)**: substring denylist against
  `{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}`.
- **AUT-002 (blocking)**: parent-block present but field empty.
- **AUT-003 (advisory, blocking under --strict)**: value not in allowlist.

Data-driven from `reconciliation/authorship-fields.yaml`. Fields registered
for the BO repo (per the field shape this repo uses):

| Path | file_glob | prefix_match |
|---|---|---|
| `**Owner**` | `change-requests/CR-*.md` | (default: exact) |
| `**Author**` | `change-requests/CR-*.md` | (default: exact) |

## 4. CI wiring

A new workflow `.github/workflows/validate-authorship.yml` runs the gate
in `--strict` mode on every push and PR. The gate has its own per-repo
test module `tests/test_check_authorship.py` (21 tests, 21/21 pass on
the BO repo's tree).

## 5. Out of scope (CR-118c, deferred)

Prose-content occurrences of `Agent` / `Coder` / etc. in record `name` /
`definition` / `description` fields (not the authorship-metadata fields)
are inventoried for the 118c follow-on but not rewritten in this slice.

## 6. Test posture

- 21/21 `test_check_authorship` pass.
- Gate `--strict` exit 0 against the live BO tree.
- 0 D-004 violations across 4 new/modified files.

## 7. Carrier

This document. Plus the CHANGELOG `[Unreleased]` entry and the new
`.github/workflows/validate-authorship.yml` workflow.
