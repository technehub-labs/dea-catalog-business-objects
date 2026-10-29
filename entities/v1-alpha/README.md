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
│   ├── README.md                                 # record documentation (IDM-007)
│   └── aspects.md                                # aspects deep-dive (documentation only)
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

## 📚 Documentation Index

Every record subtree carries its record YAML, a `README.md` with record-level documentation (identity, definition, classification, relationships, lifecycle), and an `aspects.md` deep-dive covering the semantic, relational, lifecycle, operational, governance, and measurement aspects around the object.

| Business Object | id | Class | Record docs | Aspects deep-dive |
| --- | --- | --- | --- | --- |
| Customer | `objects:object-customer-2qvphc` | party / customer | [README](customer-2qvphc/README.md) | [aspects](customer-2qvphc/aspects.md) |
| Order | `objects:object-order-bpy4g4` | transaction / sales-order | [README](order-bpy4g4/README.md) | [aspects](order-bpy4g4/aspects.md) |
| Product | `objects:object-product-dkf9gb` | offering / catalogue-product | [README](product-dkf9gb/README.md) | [aspects](product-dkf9gb/aspects.md) |
| Invoice | `objects:object-invoice-z3fwgb` | financial-instrument / billing-invoice | [README](invoice-z3fwgb/README.md) | [aspects](invoice-z3fwgb/aspects.md) |
| Payment | `objects:object-payment-kgsvrg` | financial-instrument / customer-payment | [README](payment-kgsvrg/README.md) | [aspects](payment-kgsvrg/aspects.md) |
| Grant | `objects:object-grant-nhdwg9` | financial-instrument / disbursement-grant | [README](grant-nhdwg9/README.md) | [aspects](grant-nhdwg9/aspects.md) |
| Contract | `objects:object-contract-w24y9z` | legal-instrument / commercial-contract | [README](contract-w24y9z/README.md) | [aspects](contract-w24y9z/aspects.md) |
| Feature Flag | `objects:object-feature-flag-p5gzf7` | technology-control / release-feature-flag | [README](feature-flag-p5gzf7/README.md) | [aspects](feature-flag-p5gzf7/aspects.md) |
| Supplier | `objects:object-supplier-g7m7fu` | party / supplier | [README](supplier-g7m7fu/README.md) | [aspects](supplier-g7m7fu/aspects.md) |
| Employee | `objects:object-employee-phbzym` | party / employee | [README](employee-phbzym/README.md) | [aspects](employee-phbzym/aspects.md) |
| Partner | `objects:object-partner-cfhqx9` | party / partner | [README](partner-cfhqx9/README.md) | [aspects](partner-cfhqx9/aspects.md) |
| Service | `objects:object-service-q8w4ce` | offering / service | [README](service-q8w4ce/README.md) | [aspects](service-q8w4ce/aspects.md) |
| Subscription | `objects:object-subscription-3v98yb` | offering / subscription-plan | [README](subscription-3v98yb/README.md) | [aspects](subscription-3v98yb/aspects.md) |
| Price List | `objects:object-price-list-4bk48j` | offering / price-list | [README](price-list-4bk48j/README.md) | [aspects](price-list-4bk48j/aspects.md) |
| Quote | `objects:object-quote-gnngfe` | transaction / sales-quote | [README](quote-gnngfe/README.md) | [aspects](quote-gnngfe/aspects.md) |
| Shipment | `objects:object-shipment-mb7wgn` | transaction / shipment | [README](shipment-mb7wgn/README.md) | [aspects](shipment-mb7wgn/aspects.md) |
| Return | `objects:object-return-uwz79t` | transaction / return-rma | [README](return-uwz79t/README.md) | [aspects](return-uwz79t/aspects.md) |
| Purchase Order | `objects:object-purchase-order-qf4tfa` | transaction / purchase-order | [README](purchase-order-qf4tfa/README.md) | [aspects](purchase-order-qf4tfa/aspects.md) |
| Ticket | `objects:object-ticket-2cudww` | transaction / service-ticket | [README](ticket-2cudww/README.md) | [aspects](ticket-2cudww/aspects.md) |
| Journal Entry | `objects:object-journal-entry-khck7r` | financial-instrument / journal-entry | [README](journal-entry-khck7r/README.md) | [aspects](journal-entry-khck7r/aspects.md) |
| Budget | `objects:object-budget-h77u8h` | financial-instrument / budget | [README](budget-h77u8h/README.md) | [aspects](budget-h77u8h/aspects.md) |
| Credit Note | `objects:object-credit-note-k6nktp` | financial-instrument / credit-note | [README](credit-note-k6nktp/README.md) | [aspects](credit-note-k6nktp/aspects.md) |
| Asset | `objects:object-asset-w887xr` | financial-instrument / fixed-asset | [README](asset-w887xr/README.md) | [aspects](asset-w887xr/aspects.md) |
| License | `objects:object-license-na3j53` | legal-instrument / license | [README](license-na3j53/README.md) | [aspects](license-na3j53/aspects.md) |
| Policy | `objects:object-policy-nd2t4y` | legal-instrument / policy | [README](policy-nd2t4y/README.md) | [aspects](policy-nd2t4y/aspects.md) |
| Consent Record | `objects:object-consent-record-gacq7d` | legal-instrument / consent-record | [README](consent-record-gacq7d/README.md) | [aspects](consent-record-gacq7d/aspects.md) |
| Project | `objects:object-project-5hgzd3` | work-item / project | [README](project-5hgzd3/README.md) | [aspects](project-5hgzd3/aspects.md) |
| Application | `objects:object-application-eewde8` | technology-control / application | [README](application-eewde8/README.md) | [aspects](application-eewde8/aspects.md) |
| Environment | `objects:object-environment-npd5vt` | technology-control / environment | [README](environment-npd5vt/README.md) | [aspects](environment-npd5vt/aspects.md) |
| Incident | `objects:object-incident-wudf9s` | technology-control / service-incident | [README](incident-wudf9s/README.md) | [aspects](incident-wudf9s/aspects.md) |

The seed set forms a coherent mini-mesh: the **order-to-cash chain** (Customer → Order → Invoice → Payment), the **outbound money direction** (Grant), the **governance layer** above the chain (Contract), and the **runtime product control** (Product, Feature Flag).

The wave-2 T1 set (CR-BO-07) extends each seeded area of the mesh: the **party roster** (Supplier, Employee, Partner around Customer), the **offering space** (Service, Subscription, Price List around Product), the **transaction spine** (Quote → Order → Shipment → Return; Purchase Order; Ticket), the **finance core** (Journal Entry, Budget, Credit Note, Asset around Invoice/Payment/Grant), the **legal layer** (License, Policy, Consent Record around Contract), the **work layer** (Project), and the **technology footprint** (Application, Environment, Incident around Feature Flag). Aspects deep-dives for the wave-2 records landed in the follow-up documentation wave (all records now carry one).

---

## 📈 Population Snapshot

| Level | Count |
| :--- | ---: |
| L1 (Business Object) | 54 |
| **Total** | **54** |

The first admission (CR-BO-05) landed eight seed Business Object records; the second admission (CR-BO-07) landed the wave-2 T1 commercial-core extension (22 records), and the third admission (CR-BO-08) landed the wave-2 T2 cross-industry records (16 records with sector lenses), and the fourth admission (CR-BO-09) landed the first T3-ready records (goal, forecast, tax-record), and the fifth admission (CR-BO-11) landed the first stage-native records outside the operate stage (business-case, requirement, candidate-party, offboarding-plan, sunset-plan). The CI early-exit pattern in `.github/workflows/ci.yml` has been dropped; schema validation runs on every entry.

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
8. **Mark the CR Merged on landing.** When the PR merges, update the CR's `**Status**` field from `Proposed (this PR)` to `Merged` (and the change-requests/README.md table) in a follow-up commit, then refresh `CATALOG.yaml`. The regenerator counts every non-`Merged` CR as open, so skipping this step leaves `open_change_requests` overstated.

For deeper metamodel definitions and the canonical id-system / entity-storage-layout specs, refer to:

* `technehub-labs/dea-metaframework` → `docs/id-system.md` (org-wide id contract)
* `technehub-labs/dea-metaframework` → `docs/entity-storage-layout.md` (§3 flat-layout-for-non-ECF)
* `technehub-labs/dea-metaframework` → `docs/conformance.md` (CST suite reference)
* `schemas/entity.schema.json` (record schema)
