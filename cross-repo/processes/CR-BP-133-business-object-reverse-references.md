# CR-BP-133: Business Object Cross-Catalog Reverse References (CR-BO-05 companion)

> **Co-location note:** this is a cross-repo CR (companion to CR-BO-05 in
> technehub-labs/dea-catalog-business-objects, PR #11), co-located in this
> repo's change-requests/ by the same convention as CR-ECF-CG-004.

**Status**: Proposed
**Layer**: Cross-cutting (catalog conformance)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Depends on**: CR-BP-124 (cross-catalog resolution registry), CR-BO-05 (dea-catalog-business-objects first admission)
**Companion to**: CR-BO-05 in technehub-labs/dea-catalog-business-objects (PR #11)

---

## 1. Change Request

Land the processes-direction of the business-object cross-catalog relationship: the six Process records that CR-BO-05's eight Business Object records reference via `processes_involved[]` gain the inverse `business_objects_involved[]` array. The mapping provenance is exact inversion — no new semantic claims:

| Process record | business_objects_involved |
|---|---|
| `processes:process-pr-operate-bbe384` (Manage Customer Relationship) | `objects:object-customer-2qvphc` |
| `processes:process-pr-conceive-emfgju` (Develop Customer Strategy) | `objects:object-customer-2qvphc` |
| `processes:process-pv-operate-zyguzp` (Operate Product Catalogue) | `objects:object-product-dkf9gb` |
| `processes:process-pv-design-8v4k89` (Design Product and Service Propositions) | `objects:object-product-dkf9gb` |
| `processes:process-eo-operate-xud3hs` (Run Production Line) | `objects:object-order-bpy4g4` |
| `processes:process-eo-operate-2jnz85` (Operate Service Delivery) | `objects:object-order-bpy4g4` |

Every entry resolves against dea-catalog-business-objects HEAD (its PR #11) per EGV-006 / the CR-BP-124 cross-catalog resolution registry.

## 2. Cross-catalog resolution registry truth fix

`reconciliation/cross-catalog-resolution.yaml` declares the `dea-catalog-business-objects` scope with `id_format: "dea:object-*"` (legacy; not yet migrated). That catalog has now landed its first admission in the org-wide id form (`objects:object-<slug>-<hash6>`, per dea-metaframework docs/id-system.md §2). The registry entry is updated:

```yaml
- scope: dea-catalog-business-objects
  repository: technehub-labs/dea-catalog-business-objects
  id_format: "objects:object-*"        # org-wide id form (CR-BO-05 first admission)
  legacy_id_format: "dea:object-*"     # pre-migration family (none exist in records)
```

## 3. Field placement and schema

`business_objects_involved` is inserted immediately after `process_specialization` on the six records. The Process schema (schemas/entity.schema.json) does not set top-level `additionalProperties: false`, so no schema change is required; a formal schema adoption of the field can ride a later CR-BP-CE (content enrichment) slice if the maintainers prefer it explicit.

## 4. Acceptance criteria (verified locally)

- AC-01 All six patched records parse and validate against `schemas/entity.schema.json` (0 errors each).
- AC-02 Every `objects:object-*` reference resolves against dea-catalog-business-objects HEAD (PR #11).
- AC-03 The six (process, object) pairs are the exact inverse of CR-BO-05's `processes_involved[]` edges (verified by extraction from both catalog HEADs).
- AC-04 This catalog's own gates (`check_id_system`, `check_cr_metadata`, `check_catalog_index`) remain CONFORMANT — `objects:` references are cross-catalog and outside this repo's in-namespace IDM-003 resolution scope, by design.

## 5. Out of scope

- References from the remaining 3,592 process records (await business-object coverage upstream).
- Schema-level formal adoption of `business_objects_involved` (see §3).
