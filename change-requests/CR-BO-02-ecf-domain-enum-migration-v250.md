# CR-BO-02: ECF Domain Enum v2.5.0 Migration (Domain 6 Enablement & Operations)

**Status**: Accepted
**Layer**: Catalog (business objects)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-08
**Depends on**: CR-BO-01 (v2.4.0 migration carrier); dea-metaframework CR-ECF-008; dea-metamodel CR-MM-ECF-03
**Related**: dea-metaframework ADR-ECF-003; dea-catalog-processes CR-BP-23; dea-catalog-business-capabilities CR-BC-ECF-03

## 1. What this CR is

This CR is the **v2.5.0 migration carrier** for `technehub-labs/dea-catalog-business-objects`. ECF Domain 6 is renamed from `operations-enablement` (v2.4.0 kebab-case) to `enablement-operations` (v2.5.0), driven by the Domain/Stage Orthogonality Stress Test (`dea-metaframework` ADR-ECF-003 §5; CR-ECF-008). The Domain 6 name shared a lexical root with Stage 5 `Operate`, obscuring the orthogonality that the ECF requires between the Domain axis and the Stage axis. The rename swaps the two nouns: `Enablement` now leads (lexically distinct from any Stage name) and `Operations` trails (the sustained day-to-day concern, not the lifecycle Stage).

The change is a **single Domain rename**; the other six Domains and the cardinality of the seven-Domain × seven-Stage matrix are unchanged. No content redistribution is required (CR-ECF-008 §3.5): all content that previously belonged to `Operations & Enablement` remains in `Enablement & Operations`.

## 2. Mapping

| Old form (v2.4.0) | New form (v2.5.0) |
|---|---|
| `OperationsAndEnablement` (PascalCase) | `EnablementAndOperations` |
| `operations-enablement` (kebab-case) | `enablement-operations` |
| `operationsEnablement` (lowerCamelCase identifier suffix) | `enablementAndOperations` |
| `Operations & Enablement` (display) | `Enablement & Operations` |

## 3. Files changed

- `schemas/entity.schema.json` — `ecf_domain` enum updated to include `enablement-operations`.
- `README.md` — `ecf_domain` axis values row updated.
- `entities/v1-alpha/README.md` — narrative updated.
- `change-requests/CR-BO-02-ecf-domain-enum-migration-v250.md` — this carrier.
- `CHANGELOG.md` — `[v2.5.0-migration]` section.

Total: **5 files modified** + 1 new CR.

## 4. Verification

- Schema enum matches `dea-metaframework` v2.5.0 canonical set exactly (7 kebab-case values, no duplicates, correct order per the matrix row order).
- Zero remaining references to any v2.4.0 Domain 6 identifier (`OperationsAndEnablement`, `operations-enablement`, `Operations & Enablement`).
- The schema validator (built into the schema itself) accepts the new kebab-case value as valid.

## 5. Backward compatibility

`dea-metaframework` v2.5.0 preserves the deprecated identifiers in `tools/ecf_coordinates.py:DOMAIN_ALIASES` for at least 2 release cycles (CR-ECF-008 §17):
- `OperationsAndEnablement`
- `operationsAndEnablement`
- `operations-enablement`
- `Operations & Enablement`
- `operations_and_enablement`

Downstream consumers may resolve the alias and use the canonical value.

## 6. Companion CRs (downstream cascade)

- `dea-metaframework` CR-ECF-008 (PR #30) — merged 2026-09-08
- `dea-metamodel` CR-MM-ECF-03 (PR #167) — open
- `dea-catalog-processes` CR-BP-23 (PR #61) — open
- `dea-catalog-business-capabilities` CR-BC-ECF-03 (PR #56) — open
- `dea-catalog-organizational-units` CR-OU-02 — planned (3 file footprint)

Repos audited as having zero footprint (no migration needed): `dea-catalog-actors`, `dea-catalog-stakeholders`, `dea-catalog-digital-business-service-factory`, `dea-architecture-framework`.