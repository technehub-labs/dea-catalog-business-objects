# OpenDEA Business Objects (dea-catalog-business-objects)

> Real-world entities of interest to the business — the atoms that populate the ECF matrix cells.

**Layer:** L2 · **Entity:** `BO` · **Metamodel:** [v1.0.0-alpha](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=BusinessObject)
[![CI](https://github.com/technehub-labs/dea-catalog-business-objects/actions/workflows/ci.yml/badge.svg)](https://github.com/technehub-labs/dea-catalog-business-objects/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-See%20LICENSE-blue)](LICENSE)

## What this catalog is

This repository is the canonical catalog of **Business Objects (BO)** for the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem. A Business Object is a real-world entity the business cares about — a Customer, an Order, an Invoice — and it is the atom that populates the cells of the [ECF matrix](https://github.com/technehub-labs/dea-metamodel).

This is one of **seven interoperable catalogs** in the DEA ecosystem. Business Objects are acted on by capabilities, created and updated by processes, persisted by data entities, and realized by solution components — all expressed as typed, content-addressed, cross-catalog references.

## Status

**Phase 2 population has begun.** The contract (schemas, id-form, conformance gates, CI) landed first via CR-BO-03/04; the first content admission — eight seed Business Object records — landed with [CR-BO-05](change-requests/CR-BO-05-first-admission-seed-business-objects.md); the second admission — the wave-2 T1 commercial-core extension, 22 records — landed with [CR-BO-07](change-requests/CR-BO-07-second-admission-wave2-t1.md) under the [CR-BO-06](change-requests/CR-BO-06-second-admission-wave-proposal.md) scope. Schema validation runs on every entry (the empty-tree early-exit has been dropped).

| Level | Count |
| :--- | ---: |
| L1 (Business Object) | 30 |
| **Total** | **30** |

## Catalog of Business Objects

| Business Object | id | Class | ECF cell | Consumed by (capabilities) | Involved in (processes) |
|---|---|---|---|---|---|
| [Customer](entities/v1-alpha/customer-2qvphc/README.md) | `objects:object-customer-2qvphc` | party / customer | party-relationship · operate | customer-management | pr-operate, pr-conceive |
| [Order](entities/v1-alpha/order-bpy4g4/README.md) | `objects:object-order-bpy4g4` | transaction / sales-order | enablement-operations · operate | operations-management | eo-operate ×2 |
| [Product](entities/v1-alpha/product-dkf9gb/README.md) | `objects:object-product-dkf9gb` | offering / catalogue-product | product-value · operate | offering-management, marketing | pv-operate, pv-design |
| [Invoice](entities/v1-alpha/invoice-z3fwgb/README.md) | `objects:object-invoice-z3fwgb` | financial-instrument / billing-invoice | finance-accounting · operate | financial-resource-management, financial-stewardship | — |
| [Payment](entities/v1-alpha/payment-kgsvrg/README.md) | `objects:object-payment-kgsvrg` | financial-instrument / customer-payment | finance-accounting · operate | financial-resource-management | — |
| [Grant](entities/v1-alpha/grant-nhdwg9/README.md) | `objects:object-grant-nhdwg9` | financial-instrument / disbursement-grant | finance-accounting · operate | financial-stewardship | — |
| [Contract](entities/v1-alpha/contract-w24y9z/README.md) | `objects:object-contract-w24y9z` | legal-instrument / commercial-contract | governance-existence · operate | legal-matter-management | — |
| [Feature Flag](entities/v1-alpha/feature-flag-p5gzf7/README.md) | `objects:object-feature-flag-p5gzf7` | technology-control / release-feature-flag | enablement-operations · operate | technology-enablement, technology-management | — |
| [Supplier](entities/v1-alpha/supplier-g7m7fu/README.md) | `objects:object-supplier-g7m7fu` | party / supplier | party-relationship · operate | supplier-management, sourcing-and-procurement | eo-operate, fa-operate |
| [Employee](entities/v1-alpha/employee-phbzym/README.md) | `objects:object-employee-phbzym` | party / employee | party-relationship · operate | workforce-management | ao-operate, fa-operate |
| [Partner](entities/v1-alpha/partner-cfhqx9/README.md) | `objects:object-partner-cfhqx9` | party / partner | party-relationship · operate | partner-management | — |
| [Service](entities/v1-alpha/service-q8w4ce/README.md) | `objects:object-service-q8w4ce` | offering / service | product-value · operate | offering-management | pv-operate |
| [Subscription](entities/v1-alpha/subscription-3v98yb/README.md) | `objects:object-subscription-3v98yb` | offering / subscription-plan | product-value · operate | offering-management | pv-operate |
| [Price List](entities/v1-alpha/price-list-4bk48j/README.md) | `objects:object-price-list-4bk48j` | offering / price-list | product-value · operate | offering-management, marketing | pv-operate |
| [Quote](entities/v1-alpha/quote-gnngfe/README.md) | `objects:object-quote-gnngfe` | transaction / sales-quote | enablement-operations · operate | operations-management | eo-operate |
| [Shipment](entities/v1-alpha/shipment-mb7wgn/README.md) | `objects:object-shipment-mb7wgn` | transaction / shipment | enablement-operations · operate | operations-management | eo-operate ×2 |
| [Return](entities/v1-alpha/return-uwz79t/README.md) | `objects:object-return-uwz79t` | transaction / return-rma | enablement-operations · operate | operations-management | eo-operate |
| [Purchase Order](entities/v1-alpha/purchase-order-qf4tfa/README.md) | `objects:object-purchase-order-qf4tfa` | transaction / purchase-order | enablement-operations · operate | sourcing-and-procurement | eo-operate, fa-operate |
| [Ticket](entities/v1-alpha/ticket-2cudww/README.md) | `objects:object-ticket-2cudww` | transaction / service-ticket | enablement-operations · operate | operations-management | eo-operate |
| [Journal Entry](entities/v1-alpha/journal-entry-khck7r/README.md) | `objects:object-journal-entry-khck7r` | financial-instrument / journal-entry | finance-accounting · operate | financial-resource-management | fa-operate ×2 |
| [Budget](entities/v1-alpha/budget-h77u8h/README.md) | `objects:object-budget-h77u8h` | financial-instrument / budget | finance-accounting · operate | financial-resource-management, financial-stewardship | fa-operate |
| [Credit Note](entities/v1-alpha/credit-note-k6nktp/README.md) | `objects:object-credit-note-k6nktp` | financial-instrument / credit-note | finance-accounting · operate | financial-resource-management | fa-operate |
| [Asset](entities/v1-alpha/asset-w887xr/README.md) | `objects:object-asset-w887xr` | financial-instrument / fixed-asset | finance-accounting · operate | asset-management, financial-resource-management | eo-operate |
| [License](entities/v1-alpha/license-na3j53/README.md) | `objects:object-license-na3j53` | legal-instrument / license | governance-existence · operate | legal-matter-management, regulation-management | — |
| [Policy](entities/v1-alpha/policy-nd2t4y/README.md) | `objects:object-policy-nd2t4y` | legal-instrument / policy | governance-existence · operate | enterprise-governance, regulation-management | ge-operate |
| [Consent Record](entities/v1-alpha/consent-record-gacq7d/README.md) | `objects:object-consent-record-gacq7d` | legal-instrument / consent-record | party-relationship · operate | customer-management, information-management | — |
| [Project](entities/v1-alpha/project-5hgzd3/README.md) | `objects:object-project-5hgzd3` | work-item / project | agency-organization · operate | enterprise-performance-management, strategic-planning | sd-operate |
| [Application](entities/v1-alpha/application-eewde8/README.md) | `objects:object-application-eewde8` | technology-control / application | enablement-operations · operate | technology-management, technology-enablement | eo-operate |
| [Environment](entities/v1-alpha/environment-npd5vt/README.md) | `objects:object-environment-npd5vt` | technology-control / environment | enablement-operations · operate | technology-management, technology-enablement | eo-operate |
| [Incident](entities/v1-alpha/incident-wudf9s/README.md) | `objects:object-incident-wudf9s` | technology-control / service-incident | enablement-operations · operate | technology-management, continuity-management | eo-operate |

The eight seed records are `lifecycle_status: active`, admitted under CR-BO-05 (2026-10-28); the 22 wave-2 T1 records are `lifecycle_status: active`, admitted under CR-BO-07 (2026-10-30). All lifecycles are anchored at activation.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-business-object` |
| Class Alias | `BO` |
| Layer | L2 (Business Operating Model) |
| Metamodel Version | v1.0.0-alpha |

## Classification

Business Objects are classified by **two universal coordinates plus two free-form labels**:

### Universal coordinates (ECF matrix position)

| Axis | Values |
|---|---|
| `ecf_domain` | `governance-existence` · `strategy-direction` · `agency-organization` · `party-relationship` · `product-value` · `enablement-operations` · `finance-accounting` |
| `ecf_stage` | `conceive` · `design` · `build` · `activate` · `operate` · `improve` · `retire` |

Every BO lives in exactly one `(ecf_domain, ecf_stage)` cell at a time.

### Free-form labels (domain-specific vocabulary)

| Axis | Purpose | Example |
|---|---|---|
| `object_class` | Kind of thing the business cares about | `customer`, `order`, `product`, `invoice`, `feature-flag`, `grant` |
| `object_subclass` | Refinement under the class | `retail-customer`, `enterprise-order` |

`current_state` is a **separate** domain-specific business label (e.g. `active`, `proposed`, `suspended`) — distinct from the universal `ecf_stage` coordinate.

### Classes in use today

| `object_class` | Records | Subclasses |
|---|---|---|
| `party` | 4 | `customer`, `supplier`, `employee`, `partner` |
| `transaction` | 6 | `sales-order`, `sales-quote`, `shipment`, `return-rma`, `purchase-order`, `service-ticket` |
| `offering` | 4 | `catalogue-product`, `service`, `subscription-plan`, `price-list` |
| `financial-instrument` | 7 | `billing-invoice`, `customer-payment`, `disbursement-grant`, `journal-entry`, `budget`, `credit-note`, `fixed-asset` |
| `legal-instrument` | 4 | `commercial-contract`, `license`, `policy`, `consent-record` |
| `technology-control` | 4 | `release-feature-flag`, `application`, `environment`, `service-incident` |
| `work-item` | 1 | `project` |

Industry and segment variation is expressed at the subclass level (rule BO-TAX-01, [CR-BO-06](change-requests/CR-BO-06-second-admission-wave-proposal.md)); new `object_class` values require CR-level sign-off. Aspects prose carries an explicit sector lens (CR-BO-06 §6.3).

## Typed References

| Field | Reference | Catalog | Status |
|---|---|---|---|
| `owner` | Actor (single) | [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors) | Scaffold (unset on seeds — IDM-003 forbids unresolved references) |
| `stakeholders[]` | External/affected parties | [`dea-catalog-stakeholders`](https://github.com/technehub-labs/dea-catalog-stakeholders) | Scaffold (unset on seeds) |
| `capabilities_consumed[]` | Capabilities that act on this BO | [`dea-catalog-business-capabilities`](https://github.com/technehub-labs/dea-catalog-business-capabilities) | Populated (28 canonical records) |
| `processes_involved[]` | Processes that create/read/update/delete this BO | [`dea-catalog-business-processes`](https://github.com/technehub-labs/dea-catalog-business-processes) | Populated (3,598 records) |
| `data_entities[]` | Data entities persisting this BO | (TBD) | Unbound |
| `components_realizing[]` | Solution Components that realize this BO | [`dea-catalog-digital-business-service-factory`](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) | Scaffold |
| `events[]` | Business events this BO participates in | (TBD) | Unbound |

Every reference was resolved against the live sibling catalogs before landing; deliberately unset fields remain empty until their catalogs bind, per IDM-003.

## Identity

Records are **content-addressed**: the id hash suffix was assigned once, at admission, from the record content (first 4 bytes of the file's SHA-256, base-31 over the alphabet `a-z` minus `i`, `l`, `o` plus digits `2-9`) and is immutable thereafter. The filesystem path is the id with `:` normalized to `-` (IDM-005).

```yaml
id: objects:object-customer-2qvphc      # namespace:level-slug-hash6
identity:                              # instance-level identity (planned)
  primary_id: customer-12345            # canonical handle
  external_ids:                         # source-system mapping
    crm_id: SF-0034Q00012
    erp_id: SAP-DEBI-9001
```

See [`dea-metaframework/docs/id-system.md`](https://github.com/technehub-labs/dea-metaframework/blob/main/docs/id-system.md) §2.5 for the org-wide id contract.

## Catalog Structure

```
dea-catalog-business-objects/
├── CATALOG.yaml                        ← auto-generated catalog index (do not hand-edit)
├── metamodel-pointer.yaml              ← entity mapping (do not edit manually)
├── README.md
├── LICENSE + NOTICE
├── CHANGELOG.md · CONTRIBUTING.md
├── entities/
│   └── v1-alpha/                       ← catalog entries (flat layout)
│       ├── README.md                   ← entry-level topology, gates, workflow
│       └── object-<slug>-<hash6>/
│           ├── objects-object-<slug>-<hash6>.yaml
│           └── README.md               ← per-record documentation (IDM-007)
├── schemas/
│   └── entity.schema.json              ← mirrors dea-metamodel/schemas/entities/business-object.json
├── catalog-index-schema/
│   └── catalog-index-schema.json       ← schema for CATALOG.yaml
├── change-requests/                   ← CR-BO-01..05 governance trail
├── reconciliation/                     ← authorship registry, entity-system registry
├── docs/
│   └── governance/cardinal-rules.md
├── scripts/                            ← conformance validators (IDM, ES, AUT, catalog)
├── tests/                              ← validator unit tests
└── .github/workflows/                  ← CI: validate, conformance, allocation, authorship, entity-system
```

## Quality Gates

Every PR runs the full conformance pipeline (see [`entities/v1-alpha/README.md`](entities/v1-alpha/README.md) for the complete list):

- **Schema validation** — every record against `schemas/entity.schema.json`
- **CST suite (16 tests)** — id-pattern conformance, content-derived hash correctness, flat-layout invariants
- **ID System Gate (IDM-001..008)** — id drift detection between branches and the canonical baseline
- **Authorship Gate** — cardinal rules R1/R2, data-driven from `reconciliation/authorship-fields.yaml`
- **CR Metadata Gate** — every structural change tied to an approved Change Request
- **Allocation & register gates** — orphan/duplicate record detection, catalog-register honesty

## Contributing

Admissions go through the CR workflow described in [`entities/v1-alpha/README.md`](entities/v1-alpha/README.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md):

1. File a Change Request in `change-requests/` (`CR-BO-NN-<title>.md`).
2. Add the record at the flat layout with a content-derived hash6 id.
3. Run `scripts/check_id_system.py --strict` and the CST suite locally.
4. Regenerate reconciliation artifacts (`scripts/regenerate_catalog.py --check`).
5. Open a PR; CI enforces all gates.

See the [DEA Metamodel BusinessObject schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/business-object.json) for the canonical definition, and [`docs/governance/cardinal-rules.md`](docs/governance/cardinal-rules.md) for the authorship rules.
