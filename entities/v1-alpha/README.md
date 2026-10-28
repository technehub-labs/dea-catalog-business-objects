# v1-alpha Catalog Entries

This directory will hold authoritative `v1-alpha` Business Object catalog entries for the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem.

Business Objects are stored in a **flat layout** under this directory (one subtree per record), per the org-wide entity-storage-layout spec ratified in `dea-metaframework/docs/entity-storage-layout.md`, §3. Each record will be a `<level>-<slug>-<hash>` subtree containing the record YAML. The catalog is not ECF-coordinated: Business Object entries do not decompose into a 7x7 ECF matrix.

This README mirrors the structural template set in `technehub-labs/dea-catalog-processes` PR #153. The flat-layout sections below replace the containment-tree and ECF-matrix sections that are specific to ECF-coordinated catalogs.

> **Phase 2 population has begun (CR-BO-05).** This catalog was brought up during Wave 3 of the org-wide id-system rollout; the contract (schemas, id-form, conformance gates, CI) landed first, and the first content admission (eight seed Business Object records) has now landed. The CI early-exit pattern that skipped schema validation while the entities tree was empty has been dropped.

---

## 📁 Directory Topology & Naming Conventions

```
v1-alpha/
├── object-<slug>-<hash6>/                        # record subtree
│   ├── objects-object-<slug>-<hash6>.yaml
│   └── README.md
└── README.md
```

Subdirectory names follow `object-<slug>-<hash6>`. The 6-character hash is content-derived (first 4 bytes of the record file's SHA-256, base-31 over the alphabet `a-z` minus `i`, `l`, `o` plus digits `2-9`). See `dea-metaframework/docs/id-system.md` §2.5.

---

## 📄 Entity Anatomy: Business Objects

Per the DEA Metamodel, `objects:Business` is the abstract kernel; concrete instances in this catalog will be specialized to `business objects`.

### Canonical id forms

| Level | id form |
| :--- | :--- |
| L1: Business Object | `objects:object-<slug>-<hash6>` |

Each record file's id is content-addressed: the hash suffix was assigned once, at admission (CR-BO-05 §2.6), from the record content and is immutable thereafter; the filesystem path is the id with `:` normalized to `-` (IDM-005). This is what makes the catalog content-addressed rather than directory-addressed.

### Canonical YAML Shape (illustrative)

```yaml
# id pattern: objects:object-<slug>-<hash6>
id: objects:object-example-slug-xxxxxx
name: Example Business Object
type: BusinessObject
version: 1.0.0
object_class: example-class
ecf_domain: product-value
ecf_stage: operate
lifecycle_status: active
description: >
  The illustrative definition for a Business Object record.
capabilities_consumed:
  - capabilities:capability-example-7a4kqz
processes_involved:
  - processes:process-pv-operate-7a4kqz
audit.author: Emmanuel A. Otchere
audit.reviewed_by: Emmanuel A. Otchere
```

Cross-catalog references use the org-wide id form `<namespace>:<level>-...-<hash6>`.

---

## 📈 Population Snapshot

| Level | Count |
| :--- | ---: |
| L1 (Business Object) | 8 |
| **Total** | **8** |

The first admission (CR-BO-05) landed eight seed Business Object records. The CI early-exit pattern in `.github/workflows/ci.yml` has been dropped; schema validation runs on every entry.

---

## 🛡 Governance & Conformance Gates

This catalog is protected by an automated CI pipeline with the following gates. All gates run on every PR via `.github/workflows/catalog-conformance.yml` (and adjacent workflows):

1. **`validate-entries`** (CI job)
   Validates every record file against `schemas/entity.schema.json` and the cell-charter contract.
   *Why it matters:* Catches malformed records and structural drift before they reach the catalog. Live since the CR-BO-05 admission (early-exit dropped).

2. **ECF Conformance Consumer** (where applicable)
   Validates that `domain` and ECF coordinate references match the canonical ECF Domain Enum (current: v2.4.x).
   *Why it matters:* Prevents taxonomy drift across the seven catalog repositories.

3. **Catalog Conformance Suite** (CST, layout-agnostic, from `dea-metaframework/tools/conformance_test_catalog_structure.py`)
   Runs the 16-test CST suite that checks id-pattern conformance, content-derived hash correctness, and the flat-layout invariants.
   *Why it matters:* Enforces the org-wide id-system contract across all 7 catalog repositories.

4. **ID System Gate** (`scripts/check_id_system.py`)
   Runs IDM-001..007 (catalog-wide) plus IDM-008 (PR-scoped coherence via `id-system-coherence-report.md` artifact).
   *Why it matters:* Catches id drift between branches and the canonical baseline before merge.

5. **Register Audit Gate** (`scripts/check_register_audit.py`)
   Walks the catalog register and confirms every record's `audit_status: landed` vs `pending`.
   *Why it matters:* Keeps the catalog register honest as a single source of truth.

6. **CR Metadata Gate** (`scripts/check_cr_metadata.py --strict`)
   Verifies that any structural change, new admission, or migration is explicitly tied to an approved Change Request (CR) markdown file in `change-requests/`.
   *Why it matters:* Enforces the "no undocumented mutations" rule. Every change must have an auditable governance trail.

7. **`allocate / validate`** (CI job)
   Generates a per-record allocation matrix and validates it against the catalog register.
   *Why it matters:* Detects orphan or duplicated records that escape the schema-level checks.

---

## 🔄 Lifecycle, Reconciliation, and Baselines

This directory is the source of truth for the repository's reconciliation artifacts under `reconciliation/`:

* **`CATALOG.yaml`** (repo root): Automatically refreshed to reflect the current state of all entities in this tree. The CI gate runs `scripts/regenerate_catalog.py --check` and fails on any drift. Currently emits the eight-record catalog (all canonical).
* **`reconciliation/inventory.yaml`**: Flat inventory of every entity, indexed by id.
* **`reconciliation/baseline/v1.yaml`**: Byte-identical, round-trip verifiable snapshot of the catalog at the last accepted baseline.
* **`reconciliation/conformance_report.yaml`**: Last CST run output.

When modifying this directory, contributors must run the reconciliation build scripts to ensure the baseline remains consistent with the committed tree. CI enforces this.

---

## 🔗 Cross-Repo References

This catalog is one of seven in the DEA ecosystem. Records reference other catalogs using the org-wide id form `<namespace>:<level>-...-<hash6>`:

| Namespace | Catalog | Status |
| --- | --- | --- |
| `actors:` | `technehub-labs/dea-catalog-actors` | This catalog |
| `orgunits:` | `technehub-labs/dea-catalog-organizational-units` | Wave 3 scaffold |
| `objects:` | `technehub-labs/dea-catalog-business-objects` | Wave 3 scaffold |
| `stakeholders:` | `technehub-labs/dea-catalog-stakeholders` | Wave 3 scaffold |
| `capabilities:` | `technehub-labs/dea-catalog-business-capabilities` | Populated (31 records, Wave 2) |
| `services:` | `technehub-labs/dea-catalog-business-services` | Populated (18 records, Wave 2b) |
| `processes:` | `technehub-labs/dea-catalog-business-processes` | Populated (3,598 records) |

This catalog has secondary references to the `dea:catalog-*` self-identity records, which remain in the legacy form on purpose.

---

## 🚀 Contributor Workflow

To add the first record to this catalog:

1. **Identify the record type and metadata.** Choose the canonical name, slug, and (where applicable) the ECF domain and stage the record belongs to.
2. **File a Change Request (CR).** Create or reference an existing CR in `change-requests/` (e.g., `CR-<NS>-NN-<title>.md`).
3. **Create the YAML.** Place the file at the correct flat-layout subtree. Compute the content-derived hash for the id. Use the org-wide id form for cross-catalog references.
4. **Drop the early-exit.** ~~Remove the empty-tree skip block from `.github/workflows/ci.yml`~~ (done in CR-BO-05; keep it dropped for every subsequent admission).
5. **Run Local Conformance.** Execute `scripts/check_id_system.py --strict` and the CST suite locally. The CI pipeline runs the same gates on every PR.
6. **Regenerate Reconciliation Artifacts.** Run `scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json`.
7. **Submit PR.** Link the PR to the CR. The CI pipeline enforces the gates described above.

For deeper metamodel definitions and the canonical id-system / entity-storage-layout specs, refer to:

* `technehub-labs/dea-metaframework` → `docs/id-system.md` (org-wide id contract)
* `technehub-labs/dea-metaframework` → `docs/entity-storage-layout.md` (§3 flat-layout-for-non-ECF)
* `technehub-labs/dea-metaframework` → `docs/conformance.md` (CST suite reference)
* `schemas/entity.schema.json` (record schema)
