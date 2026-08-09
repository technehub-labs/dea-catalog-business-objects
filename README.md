# Business Objects

> Real-world entities of interest to the business — the atoms that populate the ECF matrix cells.

**Layer:** L2 · **Entity:** `BO` · **Metamodel:** [v1.0.0-alpha](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=BusinessObject)

## Status

This is a **scaffold** repository — created during the Business Object relocation rollout. Content population is planned for a subsequent phase.

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
| `ecf_domain` | `governance-existence` · `supply-resources` · `people-organization` · `customer-demand` · `product-offering` · `operations-delivery` · `finance-value` |
| `ecf_stage` | `conceive` · `design` · `build` · `activate` · `operate` · `improve` · `retire` |

Every BO lives in exactly one `(ecf_domain, ecf_stage)` cell at a time.

### Free-form labels (domain-specific vocabulary)

| Axis | Purpose | Example |
|---|---|---|
| `object_class` | Kind of thing the business cares about | `customer`, `order`, `product`, `invoice`, `feature-flag`, `grant` |
| `object_subclass` | Refinement under the class | `retail-customer`, `enterprise-order` |

`current_state` is a **separate** domain-specific business label (e.g. `active`, `proposed`, `suspended`) — distinct from the universal `ecf_stage` coordinate.

## Typed References

| Field | Reference | Catalog |
|---|---|---|
| `owner` | Actor (single) | [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors) |
| `stakeholders[]` | External/affected parties | [`dea-catalog-stakeholders`](https://github.com/technehub-labs/dea-catalog-stakeholders) |
| `capabilities_consumed[]` | Capabilities that act on this BO | [`dea-catalog-business-capabilities`](https://github.com/technehub-labs/dea-catalog-business-capabilities) |
| `processes_involved[]` | Processes that create/read/update/delete this BO | [`dea-catalog-processes`](https://github.com/technehub-labs/dea-catalog-processes) |
| `data_entities[]` | Data entities persisting this BO | (TBD) |
| `components_realizing[]` | Solution Components that realize this BO | [`dea-catalog-digital-business-service-factory`](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) |
| `events[]` | Business events this BO participates in | (TBD) |

## Identity

```yaml
identity:
  primary_id: customer-12345          # canonical handle
  external_ids:                       # source-system mapping
    crm_id: SF-0034Q00012
    erp_id: SAP-DEBI-9001
```

## Catalog Structure

```
dea-catalog-business-objects/
├── metamodel-pointer.yaml         ← entity mapping (do not edit manually)
├── README.md
├── LICENSE + NOTICE
├── entities/
│   └── v1-alpha/                  ← catalog entries go here
│       └── README.md
├── schemas/
│   └── entity.schema.json         ← mirrors dea-metamodel/schemas/entities/business-object.json
└── .github/
    └── workflows/
        └── ci.yml                 ← validates entries against schema
```

## Contributing

See [DEA Metamodel BusinessObject schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/business-object.json) for the canonical definition.
