# CR-BO-08: Third Admission, Wave-2 T2 (Cross-Industry Records, 16 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-08 |
| **Title** | Third Admission, Wave-2 T2 (Cross-Industry Records, 16 Records) |
| **Status** | Merged |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-05 (admission mechanics), CR-BO-06 (wave-2 scope), CR-BO-07 (T1 landed; class taxonomy extended) |
| **Companion to** | — |

## 1. Purpose

Lands the T2 tier of the CR-BO-06 wave-2 scope: 16 cross-industry Business
Object records across seven sector lenses (healthcare, government, non-profit,
insurance, banking, education, manufacturing, retail). This admission is the
first exercised test of rule BO-TAX-01: every record expresses its industry
variant as an `object_subclass` under an existing or newly approved
`object_class` — and it lands the first records of the two remaining §6.1
classes: `resource` (3 records) and `location` (1 record).

## 2. Changes

### 2.1 Sixteen Business Object records

At `entities/v1-alpha/<slug>-<hash6>/objects-object-<slug>-<hash6>.yaml` per
the flat layout and IDM-005; hash suffixes content-derived at admission per
CR-BO-05 §2.6 and immutable thereafter.

| id | object_class | ECF (domain, stage) | Sector lens |
|---|---|---|---|
| `objects:object-patient-w8ry62` | party / patient | party-relationship, operate | healthcare |
| `objects:object-citizen-2xqsse` | party / citizen | party-relationship, operate | government |
| `objects:object-member-vbxqke` | party / member | party-relationship, operate | non-profit / co-op |
| `objects:object-insurance-claim-g5mag3` | transaction / insurance-claim | finance-accounting, operate | insurance |
| `objects:object-care-encounter-8enzdc` | transaction / care-encounter | enablement-operations, operate | healthcare |
| `objects:object-loan-byjy28` | financial-instrument / loan | finance-accounting, operate | banking |
| `objects:object-deposit-account-u6hdbe` | financial-instrument / deposit-account | finance-accounting, operate | banking |
| `objects:object-benefit-entitlement-yx4ckm` | financial-instrument / benefit-entitlement | finance-accounting, operate | government |
| `objects:object-public-case-ae4yg8` | transaction / public-case | governance-existence, operate | government |
| `objects:object-education-program-n6mp9m` | offering / education-program | product-value, operate | education |
| `objects:object-course-section-j4fdpq` | transaction / course-section | enablement-operations, operate | education |
| `objects:object-manufacturing-lot-pkbqev` | resource / manufacturing-lot | enablement-operations, operate | manufacturing |
| `objects:object-bill-of-material-9skzte` | resource / bill-of-material | enablement-operations, operate | manufacturing |
| `objects:object-production-machine-j5z9kv` | resource / production-machine | enablement-operations, operate | manufacturing |
| `objects:object-retail-store-6kzkfj` | location / retail-store | enablement-operations, operate | retail |
| `objects:object-stock-keeping-unit-x6rq8r` | offering / stock-keeping-unit | product-value, operate | retail |

Each subtree carries a README.md (IDM-007) and an aspects.md deep-dive with
the explicit sector lens labeled (CR-BO-06 §6.3).

### 2.2 New object_class values exercised

- **`resource`** (approved CR-BO-06 §6.1, first exercised here): physical or
  structural things the business cares about that are neither parties,
  instruments, transactions, nor controls — Lot / Batch, Bill of Material,
  Machine.
- **`location`** (approved CR-BO-06 §6.1, first exercised here): places
  operated as units — Store.

With `work-item` (exercised by CR-BO-07's Project), all three §6.1-approved
classes are now in use.

### 2.3 Cross-catalog enrichment (resolved references only, IDM-003)

- `capabilities_consumed[]` — every entry resolves against
  `dea-catalog-business-capabilities` HEAD.
- `processes_involved[]` — every entry resolves against
  `dea-catalog-business-processes` HEAD at `processes:process-*` level.

Citizen carries an empty `processes_involved` (public-service intake processes
are not yet present in the sibling catalog); populated in a follow-up sweep
per IDM-003 rather than by forward reference.

### 2.4 Documentation refresh

- Root `README.md`: catalog table 30 → 46 records; counts and classes-in-use
  table updated; sector-lens note extended.
- `entities/v1-alpha/README.md`: documentation index and population snapshot
  updated.
- `change-requests/README.md`: CR-BO-08 registered.
- `CATALOG.yaml`: regenerated (`open_change_requests` 7 → 8; `entities`
  30 → 46).

## 3. Acceptance criteria (all verified locally)

- AC-01 All 46 records validate against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT (46 records, 0 findings).
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean; `state: canonical` × 46.
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the
  sibling catalog HEADs named in §2.3; no forward references.

## 4. Out of scope

- T3 deferred candidates (CR-BO-06 §3) — none admitted until their consuming
  capabilities/processes exist.
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population
  (blocked on sibling catalogs).
- Sector lenses not yet represented (e.g. logistics, energy, agriculture);
  future T-tier admissions under the same BO-TAX-01 rule.
