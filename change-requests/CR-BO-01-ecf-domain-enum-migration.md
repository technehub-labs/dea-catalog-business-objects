# CR-BO-01: ECF Domain Enum Migration to v2.4.0

**Status**: Accepted
**Layer**: Catalog (business objects)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-07
**Depends on**: dea-metaframework CR-ECF-006 + CR-ECF-007 (governed by ADR-ECF-001 + ADR-ECF-002)
**Related**: dea-metamodel CR-MM-ECF-02; dea-catalog-processes CR-BP-18; dea-catalog-business-capabilities CR-CATALOG-STRUCT-09

## 1. What this CR is

This CR is the **bundled v2.3.0 + v2.4.0 migration carrier** for
`technehub-labs/dea-catalog-business-objects`. This repo was missed by the
v2.3.0 wave ground-truth scan (the scan covered 7 repos; this one was not in
scope) and was still carrying the v2.2.0 Domain enum. The migration applies
both waves in a single step:

- **v2.3.0 (CR-ECF-006)**: five of seven Domains renamed; one Domain
  replaced (`supply-resources` removed; `strategy-direction` introduced).
- **v2.4.0 (CR-ECF-007)**: Domain 3 renamed
  `people-organization` -> `agency-organization` (Substrate Independence
  Stress Test, ADR-ECF-002 §5).

## 2. Mapping applied (v2.2.0 -> v2.4.0 direct)

| v2.2.0 (was in repo) | v2.4.0 (now) |
|---|---|
| `governance-existence` | `governance-existence` (unchanged) |
| `supply-resources` | `strategy-direction` (removed; replaced) |
| `people-organization` | `agency-organization` (renamed) |
| `customer-demand` | `party-relationship` (renamed) |
| `product-offering` | `product-value` (renamed) |
| `operations-delivery` | `operations-enablement` (renamed) |
| `finance-value` | `finance-accounting` (renamed) |

## 3. Files changed

- `README.md` — `ecf_domain` axis values row updated to the v2.4.0 set.
- `schemas/entity.schema.json` — `ecf_domain` enum updated to the v2.4.0 set.
- `entities/v1-alpha/README.md` — example front-matter `ecf_domain` updated
  (`customer-demand` -> `party-relationship`).
- `change-requests/CR-BO-01-ecf-domain-enum-migration.md` — this carrier.
- `CHANGELOG.md` — new file; `[v2.4.0-migration]` section.

## 4. Verification

- Schema enum matches `dea-metaframework` v2.4.0 canonical set exactly
  (7 kebab-case values, no duplicates, correct order per the matrix row
  order).
- Zero remaining references to any v2.2.0 or v2.3.0 Domain identifier
  (grep-verified across the repo).

## 5. What did NOT change

- The `ecf_stage` enum (7 stages) is unchanged.
- No entity YAMLs exist in the catalog yet (the entities directory contains
  only the README scaffold); nothing to migrate at the entity level.
- The schema's other fields are unchanged.

## 6. Backward compatibility

`dea-metaframework` v2.4.0 preserves deprecated identifiers in
`tools/ecf_coordinates.py:DOMAIN_ALIASES` for at least 2 release cycles.
