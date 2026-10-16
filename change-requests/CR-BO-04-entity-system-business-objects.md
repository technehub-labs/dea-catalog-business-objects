# CR-BO-04: Entity System Stage 5-6 (BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. Slice)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-04 |
| **Title** | Entity System Stage 5-6 (Catalog Adoption + Institutionalisation) - BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. Slice |
| **Status** | Proposed (this PR) |
| **Layer** | L1 (BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. Catalog) |
| **Depends on** | CR-BP-121..125 (the 6-stage institutionalisation in dea-catalog-processes) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-15 |

## 1. Purpose

This is the BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. slice of the General Entity System institutionalisation programme (CR-BP-121..125 in `dea-catalog-processes`). The pilot implementation in the processes catalog is the reference; this PR ports the pattern to `technehub-labs/dea-catalog-business-objects` (0 entity records at the time of CR landing).

The slice ships:

1. The 5-rule umbrella gate `scripts/check_entity_system.py` (copied verbatim from `dea-catalog-processes`).
2. The BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT.-specific data-driven registry `reconciliation/entity-system-registry.yaml` (generic: no profiles; canonical pattern matches the repo namespace).
3. The 32-test suite `tests/test_check_entity_system.py` (4 pilot-specific tests made generic for cross-repo portability; all pass).
4. The CI workflow `.github/workflows/validate-entity-system.yml` that runs the gate under `--strict` on every PR.

The gate is vacuously CONFORMANT for this repo (0 entities to check). When entity records are added in follow-on CRs, they MUST conform to the entity-system standard or carry an exception per the EGV-011 escape hatch.

## 2. The BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT.-specific registry

The BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. repo is in the pre-migration namespace state: canonical prefix and legacy prefix are both `dea:` (no canonical namespace upgrade has been adopted yet). The canonical pattern is `^dea:object-[a-z0-9-]+$`; the legacy pattern mirrors it. The umbrella programme's T8 follow-on will introduce the org-wide canonical namespace + per-record migration maps.

The registry declares:

- envelope.file_globs: `entities/**/*.yaml`
- envelope.type_field: `type`
- envelope.profiles: empty (no entity types registered; to be added when entity records are admitted)
- identity.canonical_prefix: `dea:`
- identity.canonical_pattern: `^dea:object-[a-z0-9-]+$`
- identity.legacy_prefix: `dea:`
- identity.legacy_pattern: `^dea:object-[a-z0-9-]+$`
- relationships: empty (no entity records declare relationships)
- lifecycle: empty (no entity records have a lifecycle state machine)
- per_type_gates: empty (no entity types registered)
- exceptions: same as processes (registry_path is `reconciliation/normalization.yaml`, verdict_key is `verdict`, verdict_value is `review-retained`, cr_key is `cr`, excepted_rules_key is `excepted_rules`).

## 3. The gate posture (live, 2026-10-15)

```
$ python3 scripts/check_entity_system.py --self-test
self-test PASS (5 cases)

$ python3 scripts/check_entity_system.py --strict
Entity System Gate (CR-BP-123): CONFORMANT
```

The gate is vacuously CONFORMANT (0 entities in the file_globs). When entity records are added, they will be checked against the registered profile (or, if no profile is registered, the gate's ES-002 will report a missing-profile finding; per the Stage 5 staging, this is advisory).

## 4. The exception mechanism (the EGV-011 escape hatch)

The exception mechanism (CS-008/CS-009) consults `reconciliation/normalization.yaml` for `review-retained` verdicts. This slice ships no exceptions; future CRs that admit entity records MAY add per-record exceptions if the entity-system profile cannot be satisfied.

## 5. Repository changes

| Path | Status | Notes |
|---|---|---|
| `reconciliation/entity-system-registry.yaml` | NEW | BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT.-specific registry (generic; no profiles) |
| `scripts/check_entity_system.py` | NEW | Copied verbatim from `dea-catalog-processes` (5 rules; --self-test + --strict + --json) |
| `tests/test_check_entity_system.py` | NEW | Copied verbatim; 32 tests (4 pilot-specific tests made generic); all pass |
| `.github/workflows/validate-entity-system.yml` | NEW | Runs the gate under --strict on every PR |
| `change-requests/CR-BO-04-entity-system-business-objects.md` | NEW | This file (the carrier CR) |
| `change-requests/README.md` | MOD | New row |
| `CHANGELOG.md` | MOD | [Unreleased] entry |

## 6. Acceptance criteria

- AC-01 The registry is filed under `reconciliation/entity-system-registry.yaml`; data-driven from the registry.
- AC-02 The 5-rule umbrella gate is in place (`scripts/check_entity_system.py`); the BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. registry is registered.
- AC-03 The 32-test suite passes (`tests/test_check_entity_system.py`; 4 pilot-specific tests made generic for cross-repo portability).
- AC-04 The CI workflow runs the gate under `--strict` on every PR.
- AC-05 D-004 (no en/em-dash, no U+2E3B) is clean across all new/modified files.
- AC-06 The 118a/b/c authorship gates remain CONFORMANT (no overlap with this slice).
- AC-07 The gate is vacuously CONFORMANT (0 entities in the file_globs).

## 7. Out-of-scope follow-ons

- **T8 of umbrella programme** (Legacy ID reconciliation): per-repo disposition registers + cross-catalog URI form (U-01 resolution) + IDM-001 pattern fix. This is when the BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. repo's id family will be promoted from the pre-migration `dea:` namespace to the org-wide canonical namespace.
- **Future entity-record admissions**: when the BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. repo admits its first entity record, the registry's `profiles` block will be populated with the type-specific profile (per the entity contract EC-001..EC-004).

## 8. Cross-references

- **CR-BP-121..125**: the 6-stage institutionalisation in `dea-catalog-processes`.
- **CR-DEA-BC-35**: the BC slice of the cross-repo cascade (the full slice that established the pattern; this PR mirrors it generically).
- **DEA-ID-000**: the foundation paper in `dea-governance/docs/design/entity-system-foundation.md`.
- **CR-012**: the org-wide governance CR in `dea-governance/change-requests/CR-012-org-wide-entity-governance.md`.
- **T7 of umbrella programme**: the cross-repo cascade (this PR is one slice).
