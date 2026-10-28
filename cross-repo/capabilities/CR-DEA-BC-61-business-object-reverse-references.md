# CR-DEA-BC-61: Business Object Cross-Catalog Reverse References (CR-BO-05 companion)

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-61 |
| **Title** | Business Object Cross-Catalog Reverse References (CR-BO-05 companion) |
| **Status** | Proposed (this PR) |
| **Layer** | Cross-cutting (catalog conformance) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-10-28 |
| **Depends on** | CR-DEA-BC-58 (business-object reconciliation register; blocked upstream), CR-BO-05 (dea-catalog-business-objects first admission) |
| **Companion to** | CR-BO-05 in technehub-labs/dea-catalog-business-objects (PR #11) |

## 1. Purpose

CR-DEA-BC-58 established the business-object reconciliation register with disposition `U-1 blocked upstream`: the business-objects catalog was a Wave-3 scaffold with 0 entities, so the register's free-text `business_object` labels had no canonical targets to resolve against. CR-BO-05 (companion PR, technehub-labs/dea-catalog-business-objects #11) has now landed the first eight canonical Business Object records in the org-wide id form (`objects:object-<slug>-<hash6>`), each carrying `capabilities_consumed[]` references into this catalog. This CR lands the reverse direction: resolved, id-typed references from this catalog's capability records into the business-objects catalog, completing the cross-catalog relationship both ways per EGV-006 (references SHALL resolve to valid entities within the declared identity scope).

## 2. Changes

### 2.1 Schema: `business_object_refs[]`

`schemas/entity.schema.json` gains an optional `business_object_refs` array (items constrained to `^objects:object-[a-z0-9-]+-[a-z2-9]{6}$`). It is a companion to — not a replacement for — the legacy free-text `business_object` label, which stays verbatim (its prose values are part of the METHODOLOGY.md §4 Object Focus evidence and are tracked separately by the CR-DEA-BC-58 register). Populating it on a record asserts that every entry resolves against a canonical record in technehub-labs/dea-catalog-business-objects.

### 2.2 Record population (9 capabilities)

The nine capabilities whose records CR-BO-05 references via `capabilities_consumed[]` gain the inverse `business_object_refs[]`:

| Capability | business_object_refs |
|---|---|
| Customer Management | `objects:object-customer-2qvphc` |
| Financial Resource Management | `objects:object-invoice-z3fwgb`, `objects:object-payment-kgsvrg` |
| Financial Stewardship | `objects:object-grant-nhdwg9`, `objects:object-invoice-z3fwgb` |
| Legal Matter Management | `objects:object-contract-w24y9z` |
| Marketing | `objects:object-product-dkf9gb` |
| Offering Management | `objects:object-product-dkf9gb` |
| Operations Management | `objects:object-order-bpy4g4` |
| Technology Enablement | `objects:object-feature-flag-p5gzf7` |
| Technology Management | `objects:object-feature-flag-p5gzf7` |

Mapping provenance: the nine (capability, object) pairs are exactly the inverse of the `capabilities_consumed[]` edges asserted by the eight CR-BO-05 records at that catalog's HEAD; no new semantic claims are introduced.

### 2.3 Reconciliation register refresh

`reconciliation/business-object-reconciliation-register.yaml`: `upstream_status` updated to the post-CR-BO-05 state (8 canonical records, org-wide id form); the disposition moves from `U-1 blocked upstream` to a partially-resolvable state — the register's free-text values with canonical targets (Customer, Product) gain resolvable mappings via the new field; the remainder stay as descriptive values pending further upstream admissions (Invoice, Payment, Contract, Grant, Order, Feature Flag do not match any register value verbatim and are not force-mapped).

## 3. Acceptance criteria (verified locally)

- AC-01 All 29 capability records validate against the patched `schemas/entity.schema.json` (0 failures).
- AC-02 `business_object_refs` present on exactly the 9 records listed in §2.2; every entry matches the org-wide id pattern and resolves against dea-catalog-business-objects HEAD (PR #11).
- AC-03 The nine (capability, object) pairs are the exact inverse of CR-BO-05's `capabilities_consumed[]` edges (verified by extraction from both catalog HEADs).
- AC-04 This catalog's existing gates (`check_id_system`, `check_relationship_integrity`, `check_entity_system`, `check_authorship`) remain CONFORMANT — `objects:` references are cross-catalog and outside this repo's IDM-003 in-namespace resolution scope, by design.

## 4. Out of scope

- Rewriting the legacy free-text `business_object` labels (CR-DEA-BC-58's register governs those; semantic review at further upstream admissions).
- References from the remaining 19 capabilities whose `business_object` labels have no canonical upstream target yet.
