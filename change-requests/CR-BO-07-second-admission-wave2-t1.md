# CR-BO-07: Second Admission Wave, T1 (Commercial-Core Extension, 22 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-07 |
| **Title** | Second Admission Wave, T1 (Commercial-Core Extension, 22 Records) |
| **Status** | Merged |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-05 (admission mechanics), CR-BO-06 (wave-2 scope and decisions) |
| **Companion to** | — |

## 1. Purpose

Lands the T1 tier of the CR-BO-06 wave-2 scope: 22 commercial-core Business
Object records, admitted under the §6 decisions recorded by the review
authority on 2026-10-30:

- **§6.1 — new classes approved:** `work-item`, `resource`, `location` are
  approved `object_class` values. This admission exercises `work-item`
  (Project); `resource` and `location` have no T1 records and first land with
  a T2 manufacturing/retail admission.
- **§6.2 — one CR, all 22:** all T1 records land in this single admission.
- **§6.3 — explicit lens labels:** new-record aspects prose names its sector
  lens explicitly, following the seed convention.

## 2. Changes

### 2.1 Twenty-two Business Object records

At `entities/v1-alpha/<slug>-<hash6>/objects-object-<slug>-<hash6>.yaml`
per the flat layout and IDM-005. Hash suffixes content-derived at admission per
CR-BO-05 §2.6 (SHA-256 of the record with the id line reduced to its
suffix-less stem; first 4 bytes; base-31 over the 31-symbol alphabet; 6 chars)
and immutable thereafter.

| id | object_class | ECF (domain, stage) |
|---|---|---|
| `objects:object-supplier-g7m7fu` | party / supplier | party-relationship, operate |
| `objects:object-employee-phbzym` | party / employee | party-relationship, operate |
| `objects:object-partner-cfhqx9` | party / partner | party-relationship, operate |
| `objects:object-service-q8w4ce` | offering / service | product-value, operate |
| `objects:object-subscription-3v98yb` | offering / subscription-plan | product-value, operate |
| `objects:object-price-list-4bk48j` | offering / price-list | product-value, operate |
| `objects:object-quote-gnngfe` | transaction / sales-quote | enablement-operations, operate |
| `objects:object-shipment-mb7wgn` | transaction / shipment | enablement-operations, operate |
| `objects:object-return-uwz79t` | transaction / return-rma | enablement-operations, operate |
| `objects:object-purchase-order-qf4tfa` | transaction / purchase-order | enablement-operations, operate |
| `objects:object-ticket-2cudww` | transaction / service-ticket | enablement-operations, operate |
| `objects:object-journal-entry-khck7r` | financial-instrument / journal-entry | finance-accounting, operate |
| `objects:object-budget-h77u8h` | financial-instrument / budget | finance-accounting, operate |
| `objects:object-credit-note-k6nktp` | financial-instrument / credit-note | finance-accounting, operate |
| `objects:object-asset-w887xr` | financial-instrument / fixed-asset | finance-accounting, operate |
| `objects:object-license-na3j53` | legal-instrument / license | governance-existence, operate |
| `objects:object-policy-nd2t4y` | legal-instrument / policy | governance-existence, operate |
| `objects:object-consent-record-gacq7d` | legal-instrument / consent-record | party-relationship, operate |
| `objects:object-project-5hgzd3` | work-item / project | agency-organization, operate |
| `objects:object-application-eewde8` | technology-control / application | enablement-operations, operate |
| `objects:object-environment-npd5vt` | technology-control / environment | enablement-operations, operate |
| `objects:object-incident-wudf9s` | technology-control / service-incident | enablement-operations, operate |

Each subtree carries a README.md (IDM-007) with identity, definition,
classification, relationships, lifecycle, and governance sections.

### 2.2 Cross-catalog enrichment (resolved references only, IDM-003)

- `capabilities_consumed[]` — every entry resolves against
  `dea-catalog-business-capabilities` HEAD (29 canonical capability records);
  27 distinct capabilities referenced.
- `processes_involved[]` — every entry resolves against
  `dea-catalog-business-processes` HEAD; only `processes:process-*` level ids
  are used, matching the CR-BO-05 convention.

Records whose natural process anchors are not yet present in the processes
catalog carry an empty `processes_involved` rather than a forward reference:
Partner (partner joint-operations processes), License (license lifecycle
processes), Consent Record (consent capture/withdrawal processes). These
populate in a follow-up sweep when the sibling catalog admits them.

`owner`, `stakeholders[]`, `events[]`, `data_entities[]`, and
`components_realizing[]` remain unset for the same reason as CR-BO-05 §2.2
(sibling catalogs not yet bound; IDM-003 forbids unresolved references).

### 2.3 Taxonomy note

This admission adds one new `object_class` value in use — `work-item`
(approved under CR-BO-06 §6.1) — for the Project record. The class covers
non-routine work items (Project, Initiative, Task, OKR candidates in the
CR-BO-06 T3 list) that are neither transactions nor instruments.

### 2.4 Documentation refresh

- Root `README.md`: catalog table extended 8 → 30 records; counts, classes-in-use table, and lens-labelling note updated.
- `entities/v1-alpha/README.md`: documentation index extended.
- `change-requests/README.md`: CR-BO-07 registered.
- `CATALOG.yaml`: regenerated (`open_change_requests` 6 → 7; `entities` 8 → 30).

## 3. Acceptance criteria (all verified locally)

- AC-01 All 30 records validate against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT (30 records, 0 findings).
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean; `state: canonical` × 30.
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the sibling catalog HEADs named in §2.2; no forward references.

## 4. Out of scope

- T2 cross-industry records (healthcare, government, banking, insurance, manufacturing, retail, education lenses) — follow-up admission.
- T3 deferred candidates (CR-BO-06 §3).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population (blocked on sibling catalogs).
- Aspects deep-dives for the new records (follow-up documentation wave, as with the seeds).
