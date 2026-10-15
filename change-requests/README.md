# Change Requests

This directory tracks formal change requests (CRs) for `technehub-labs/dea-catalog-business-objects`.

| CR | Title | Status | Summary |
|---|---|---|---|
| [CR-BO-04](CR-BO-04-entity-system-business-objects.md) | Entity System Stage 5-6 (Catalog Adoption + Institutionalisation) - BO Slice | **Proposed (this PR)** | BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. slice of the General Entity System institutionalisation (cross-repo cascade T7). New `reconciliation/entity-system-registry.yaml` (per-repo; generic; no profiles; canonical pattern matches the repo namespace). New `scripts/check_entity_system.py` (5-rule umbrella gate; copied verbatim from `dea-catalog-processes`). New `tests/test_check_entity_system.py` (32 tests; 4 pilot-specific tests made generic for cross-repo portability; all pass). New `.github/workflows/validate-entity-system.yml` (CI). Live: gate vacuously CONFORMANT (0 entities in file_globs). D-004 clean. 118a/b/c authorship gates remain CONFORMANT. Follow-on: T8 legacy ID reconciliation. |
