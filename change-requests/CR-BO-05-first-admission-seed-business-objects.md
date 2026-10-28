# CR-BO-05: First Phase-2 Admission (Seed Business Object Records, BO Profile, Early-Exit Drop)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-05 |
| **Title** | First Phase-2 Admission (Seed Business Object Records, BO Profile, Early-Exit Drop) |
| **Status** | Proposed (this PR) |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-28 |
| **Depends on** | CR-BO-04 (entity-system slice), CR-mv1-bringup (id system) |
| **Companion to** | CR-ACT-07 (actors first admission; same landing pattern) |

## 1. Purpose

The catalog has been a contract-only scaffold since Wave 3: schemas, id-form, conformance gates, and CI existed but no Phase-2 content admissions had ever landed, so the record contract was unproven. This CR lands the first admission — eight seed Business Object records, each enriched with resolved cross-catalog references to the populated sibling catalogs — and, in doing so, exercises the full documented workflow (entities/v1-alpha/README.md §Contributor Workflow, steps 1–7) for the first time. It also closes two latent integrity defects the empty tree had masked.

## 2. Changes

### 2.1 Seed Business Object records (8)

Eight seed records covering eight `object_class` values, at `entities/v1-alpha/object-<slug>-<hash6>/objects-object-<slug>-<hash6>.yaml` per the flat layout and IDM-005:

| id | object_class | ECF (domain, stage) |
|---|---|---|
| `objects:object-customer-2qvphc` | party | party-relationship, operate |
| `objects:object-order-bpy4g4` | transaction | enablement-operations, operate |
| `objects:object-product-dkf9gb` | offering | product-value, operate |
| `objects:object-invoice-z3fwgb` | financial-instrument | finance-accounting, operate |
| `objects:object-payment-kgsvrg` | financial-instrument | finance-accounting, operate |
| `objects:object-contract-w24y9z` | legal-instrument | governance-existence, operate |
| `objects:object-grant-nhdwg9` | financial-instrument | finance-accounting, operate |
| `objects:object-feature-flag-p5gzf7` | technology-control | enablement-operations, operate |

Each record carries the schema-required envelope (`id`, `type: BusinessObject`, `name`, `version`, `object_class`, `ecf_domain`, `ecf_stage`) plus `lifecycle_status` and the registered `audit.author` / `audit.reviewed_by` authorship fields (flat key shape; same as CR-ACT-07). Each subtree carries a README.md (IDM-007).

### 2.2 Cross-catalog enrichment (integrity: resolved references only)

Every structured cross-reference in `capabilities_consumed[]` and `processes_involved[]` was resolved against the live sibling catalogs before landing (no placeholder or forward references):

- `capabilities:*` — resolved against `dea-catalog-business-capabilities` (28 canonical records at HEAD).
- `processes:*` — resolved against `dea-catalog-business-processes` (3,598 records at HEAD); only `processes:process-*` level ids are used.

`owner` and `stakeholders[]` are deliberately left unset: `dea-catalog-actors` holds only seed/system records (no business-owner actor), and `dea-catalog-stakeholders` is an empty scaffold. Populating them would create unresolved references, which IDM-003 forbids. `events[]` and `data_entities[]` remain unset for the same reason (their catalogs are not yet bound).

### 2.3 Entity-system registry: BusinessObject profile + identity alignment

`reconciliation/entity-system-registry.yaml` gains the `BusinessObject` envelope profile (required fields: `id`, `type`, `name`, `version`, `object_class`, `ecf_domain`, `ecf_stage`, `description`, `lifecycle_status`, `provenance`). Without it, ES-002 fires on any non-empty `type:` while `profiles: {}`.

The registry's `identity.canonical_pattern` is corrected from the legacy `^dea:object-[a-z0-9-]+$` to the org-wide form `^objects:object-[a-z0-9-]+-[a-z2-9]{6}$` that this repo's own IDM-001 gate enforces. The two gates previously disagreed; the moment any record landed, the ES gate would have flagged every canonical id as legacy. The pre-migration `dea:` family stays declared as `legacy_pattern` (same fix as the actors slice, CR-ACT-05).

### 2.4 Authorship registry: object-record fields

`reconciliation/authorship-fields.yaml` registers `audit.author` and `audit.reviewed_by` over `entities/v1-alpha/**/objects-*.yaml` (kind: yaml), per `docs/governance/cardinal-rules.md` R1, which notes registration as part of the first-admission CR.

### 2.5 Early-exit drop (`ci.yml`) + regenerator state-inference fix

The Phase-2 empty-tree skip block is removed; `validate` now schema-validates every `entities/**/*.yaml|json` against `schemas/entity.schema.json` on each run. All eight records validate.

The admission also exposed the same regenerator bug the actors admission found (CR-ACT-07 §2.5): `infer_state` probed `{entity_id}.yaml` — an id contains `:`, which can never be a literal filename — misclassifying every canonical subtree as `state: candidate`. Fixed: the canonical filename is the id with `:` normalized to `-` (matching IDM-005). `CATALOG.yaml` now emits `state: canonical` for all eight.

### 2.6 Hash-suffix derivation note

Per `dea-metaframework/docs/id-system.md` §2.5 the suffix is content-derived and assigned once, at admission; gates check well-formedness only (IDM-004), never recomputation. Because the id embeds the suffix (changing it changes the file), the content-derived input for a first admission is defined as the record file with the id line reduced to its suffix-less stem (`id: objects:object-<slug>`). This makes the assignment deterministic and reproducible for these eight records while preserving the once-assigned-never-recomputed contract for future edits.

### 2.7 `CATALOG.yaml` refresh

Regenerated: `open_change_requests` 4 → 5 (this CR, counted open until it merges), `entities: []` → 8 canonical entries, `counts.*` updated. The committed file was also stale on main (CR-BO-03/04 landed without regeneration); this refresh clears that drift.

### 2.8 `entities/v1-alpha/README.md` truth fix

The scaffold README's illustrative id form (`objects-<level>-<slug>-<hash6>`, missing the namespace token and colon) contradicted IDM-001/IDM-005 and the canonical form in `dea-metaframework/docs/id-system.md`. Corrected to `objects:object-<slug>-<hash6>` everywhere; population snapshot and early-exit notes updated to reflect the landed admission.

## 3. Acceptance criteria (all verified locally)

- AC-01 `scripts/check_id_system.py --strict` → CONFORMANT (8 records, 0 findings; IDM-001..007 pass on real records for the first time).
- AC-02 `scripts/check_entity_system.py --strict` → CONFORMANT (BusinessObject profile resolves; ES-002 satisfied; identity patterns aligned).
- AC-03 `scripts/check_authorship.py --strict` → CONFORMANT (audit.author / audit.reviewed_by coverage live).
- AC-04 All 8 records validate against `schemas/entity.schema.json`.
- AC-05 `scripts/regenerate_catalog.py --check` → clean (committed CATALOG.yaml matches regenerator output; `state: canonical` × 8).
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the sibling catalog HEADs named in §2.2.

## 4. Out of scope

- `owner` / `stakeholders[]` population (blocked on sibling catalogs; see §2.2).
- `events[]` / `data_entities[]` population (catalogs not yet bound).
- Reverse references from capabilities/processes records into this catalog (each sibling catalog's own CR chain).
