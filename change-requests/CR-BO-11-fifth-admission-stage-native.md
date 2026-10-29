# CR-BO-11: Fifth Admission (Stage-Native Records, First Non-Operate Cells, 5 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-11 |
| **Title** | Fifth Admission (Stage-Native Records, First Non-Operate Cells, 5 Records) |
| **Status** | Merged |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-10 (proposal and §5 decisions), CR-BO-05 §2.6 (hash contract) |
| **Companion to** | — |

## 1. Purpose

Lands the CR-BO-10 scope under its recorded §5 decisions (2026-10-30):
**BO-STG-01 adopted** (one record, one cell, principally-managed stage);
**all five** stage-native candidates admitted; the pre-role party named
**`Candidate`**. This is the catalog's first admission of records outside the
`operate` stage: the `conceive`, `design`, and `retire` cells gain their first
records.

## 2. Changes

### 2.1 Five stage-native Business Object records

| id | object_class | ECF (domain, stage) | First cell populated |
|---|---|---|---|
| `objects:object-business-case-et8p4e` | work-item / business-case | strategy-direction · conceive | first `conceive`-stage record |
| `objects:object-requirement-9ukadu` | transaction / requirement | product-value · design | first `design`-stage record |
| `objects:object-candidate-party-s8q2mk` | party / candidate-party | party-relationship · conceive | — |
| `objects:object-offboarding-plan-djz4md` | work-item / offboarding-plan | party-relationship · retire | first `retire`-stage records |
| `objects:object-sunset-plan-34225t` | work-item / sunset-plan | product-value · retire | — |

Each subtree carries README.md (IDM-007) and an aspects.md deep-dive with the
explicit sector lens and the stage-native placement note. Hash suffixes
content-derived at admission per CR-BO-05 §2.6 and immutable thereafter.

### 2.2 Cross-catalog enrichment (resolved references only, IDM-003)

All references resolve against the sibling catalog HEADs; each record carries
at least one process at its **own** ECF stage (CR-BO-10 AC-08 stage
coherence):

- Business Case: `sd-conceive-xa4h2k` (Frame Strategic Horizons),
  `sd-conceive-ahwvp5` (Develop Corporate Strategy).
- Requirement: `pv-design-8v4k89` (Design Product and Service Propositions),
  `pv-design-a4c76s` (Design Packaging and Configuration).
- Candidate: `pr-conceive-emfgju` (Develop Customer Strategy),
  `pr-conceive-tvst8u` (Develop Market Intelligence).
- Offboarding Plan: `pr-retire-bd3asa` (Close Enterprise Relationship).
- Sunset Plan: `pv-retire-6us5am` (Transition Proposition Out of Service).

No forward references; no empty `processes_involved` in this admission.

### 2.3 Improve-stage candidates remain deferred

Per CR-BO-10 §3: Post-Implementation Review and Improvement Proposal stay
deferred until the processes catalog's improve-stage anchors strengthen.

### 2.4 Documentation refresh

- Root README: catalog table 49 → 54; counts; stage note (the catalog is no
  longer operate-only).
- `entities/v1-alpha/README.md`: index and snapshot updated.
- `change-requests/README.md`: CR-BO-11 registered.
- `CATALOG.yaml`: regenerated.

## 3. Acceptance criteria (all verified locally)

- AC-01 All 54 records validate against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT (54 records, 0 findings).
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean; `state: canonical` × 54.
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the
  sibling catalog HEADs; no forward references.
- AC-08 (from CR-BO-10) Each non-operate record lists at least one process at
  its own ECF stage.

## 4. Out of scope

- Improve-stage candidates (§2.3).
- Re-placement of any existing operate-stage record (CR-BO-10 §4: none
  proposed).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population.
