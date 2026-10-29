# CR-BO-09: Fourth Admission (T3-Ready Candidates, 3 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-09 |
| **Title** | Fourth Admission (T3-Ready Candidates, 3 Records) |
| **Status** | Merged |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-06 (T3 deferred list), CR-BO-07/08 (admission mechanics proven) |
| **Companion to** | dea-catalog-business-processes#215, dea-catalog-business-capabilities#114 (cross-catalog gaps, separate) |

## 1. Purpose

Admits the first slice of the CR-BO-06 T3 deferred list: candidates whose
consuming capabilities and processes now resolve against the live sibling
catalogs. Three of the T3 candidates meet the IDM-003 resolution bar today:
Goal, Forecast, and Tax Record. The remainder of the T3 list stays deferred
until their anchors exist.

This admission also populates the **first record in the `strategy-direction`
ECF domain** (Goal) — previously the only unpopulated domain — and the second
`work-item`-class record.

## 2. Changes

### 2.1 Three Business Object records

| id | object_class | ECF (domain, stage) | T3 origin |
|---|---|---|---|
| `objects:object-goal-h2zfhv` | work-item / strategic-goal | strategy-direction, operate | Goal/OKR candidate |
| `objects:object-forecast-um3az3` | financial-instrument / forecast | finance-accounting, operate | Forecast candidate |
| `objects:object-tax-record-zwqfpa` | financial-instrument / tax-record | finance-accounting, operate | Tax Record candidate |

Each subtree carries README.md (IDM-007) and an aspects.md deep-dive with the
explicit sector lens (CR-BO-06 §6.3). Hash suffixes content-derived at
admission per CR-BO-05 §2.6 and immutable thereafter.

### 2.2 Cross-catalog enrichment (resolved references only, IDM-003)

- Goal: `capabilities:capability-strategic-planning-k3rz7a`,
  `capabilities:capability-enterprise-performance-management-5fxren`; sd-operate processes
  (u6xgu5, zdjchn, ucxpz4).
- Forecast: `capabilities:capability-financial-resource-management-cd3c7c`,
  `capabilities:capability-enterprise-performance-management-5fxren`; fa-build
  92v24c, fa-operate ycba3k.
- Tax Record: `capabilities:capability-financial-resource-management-cd3c7c`,
  `capabilities:capability-regulation-management-gya4d8`; fa-operate 8vqvkk,
  fa-design ds4drw.

All references verified against the sibling catalog HEADs; none forward.

### 2.3 Remaining T3 deferral (unchanged)

Dataset, Report, Document, Task, Position, Department, API, Configuration
Item, User Account, Expense Report, Promotion, Warranty/SLA, Discount, NDA,
Matter — each still lacks at least one resolvable consuming anchor; tracked
with the sibling-catalog gap issues (processes#215, capabilities#114).

### 2.4 Documentation refresh

- Root README: catalog table 46 → 49; counts updated.
- `entities/v1-alpha/README.md`: index and snapshot updated.
- `change-requests/README.md`: CR-BO-09 registered.
- `CATALOG.yaml`: regenerated.

## 3. Acceptance criteria (all verified locally)

- AC-01 All 49 records validate against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT (49 records, 0 findings).
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean; `state: canonical` × 49.
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the
  sibling catalog HEADs; no forward references.

## 4. Out of scope

- Remaining T3 candidates (see §2.3).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population.
- Non-`operate` ECF stages (separate proposal CR).
