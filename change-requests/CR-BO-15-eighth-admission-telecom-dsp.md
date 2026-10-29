# CR-BO-15: Eighth Admission (Telecom Operator / DSP Enrichment, 10 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-15 |
| **Title** | Eighth Admission (Telecom Operator / DSP Enrichment, 10 Records) |
| **Status** | Proposed (this PR) |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-06 (BO-TAX-01), CR-BO-08 (sector-lens pattern), CR-BO-13 (VER/XREF discipline) |
| **Companion to** | capabilities catalog MCSP specialization views (CR-DEA-BC-04) |

## 1. Purpose

Enriches the catalog with Business Objects native to a **telecom operator / digital service provider**, the sector the capabilities catalog pioneered with its Mobile Communications Service Provider (MCSP) specialization views (CR-DEA-BC-04). Per BO-TAX-01, every record is a subclass-level variant anchored to first-order capabilities and industry-neutral processes — the same pattern as the wave-2 T2 admission (CR-BO-08).

## 2. Changes

### 2.1 Ten Business Object records (telecom lens)

| id | object_class | ECF (domain, stage) |
|---|---|---|
| `objects:object-subscriber-muj94k` | party / subscriber | party-relationship, operate |
| `objects:object-tariff-plan-ah5q9f` | offering / tariff-plan | product-value, operate |
| `objects:object-service-instance-j5uxmb` | transaction / service-instance | enablement-operations, operate |
| `objects:object-usage-record-nax3b6` | transaction / usage-record | finance-accounting, operate |
| `objects:object-network-asset-wee4fw` | resource / network-asset | enablement-operations, operate |
| `objects:object-service-number-6axyb2` | resource / service-number | governance-existence, operate |
| `objects:object-coverage-area-vf8sfv` | location / coverage-area | enablement-operations, operate |
| `objects:object-sim-profile-ja8k4x` | technology-control / subscriber-identity-module | party-relationship, activate |
| `objects:object-prepaid-balance-k65673` | financial-instrument / prepaid-balance | finance-accounting, operate |
| `objects:object-interconnect-agreement-dvq2ce` | legal-instrument / interconnect-agreement | governance-existence, operate |

### 2.2 Design notes

- **Subscriber vs. Customer**: the subscriber/user vs. payer separation is
  load-bearing in telecom (one payer, many users); the record's aspects
  document the distinction rather than duplicating Customer.
- **SIM Profile** mirrors Party Credential (CR-BO-12) at `activate` — the
  telecom identity binding; **Service Number** is placed in
  `governance-existence` as a regulator-governed addressing resource
  (numbering ranges, portability).
- **Prepaid Balance** is documented as the inverse of a receivable — the
  custody instrument unique to prepaid models.
- **Service Number / Network Asset** extend `resource` beyond manufacturing;
  **Coverage Area** extends `location` beyond retail — the classes prove
  industry-portable.
- All records resolve against first-order capabilities and industry-neutral
  processes at sibling HEADs (XREF gate, 187 references total post-admission).

### 2.3 Post-merge housekeeping (workflow step 8)

CR-BO-13/14 status → `Merged`; CATALOG.yaml and version manifest refreshed in
this branch (64 → 74 records).

### 2.4 Documentation refresh

Root README table (64 → 74), classes-in-use, entities README,
project-status (coverage + lens table gains telecom), CR register, coverage
poster regenerated.

## 3. Acceptance criteria (all verified locally)

- AC-01 All 74 records validate against `schemas/entity.schema.json`.
- AC-02 `check_id_system.py --strict` → CONFORMANT (74 records).
- AC-03 Entity-system, authorship, catalog-index gates → CONFORMANT.
- AC-04 `regenerate_catalog.py --check` → clean; canonical × 74.
- AC-05 XREF gate → CONFORMANT (all references resolve at sibling HEADs).
- AC-06 VER gates strict → CONFORMANT (74 records in manifest).
- AC-07 `pytest tests/` → all pass.

## 4. Out of scope

- Roaming Agreement, Spectrum License, Wholesale Settlement (deferred: no
  first-order process anchors distinguish them yet — candidates for a
  follow-up slice or sibling-catalog enrichment via processes#215).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population.
