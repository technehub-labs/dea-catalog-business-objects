# Product

Documentation for Business Object record [`objects:object-product-dkf9gb`](objects-object-product-dkf9gb.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-product-dkf9gb` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A product or service the enterprise offers to the market. The Product carries the value proposition: it is designed as a proposition, built as market readiness, operated through the product catalogue, and evolved through the portfolio lifecycle.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `offering` |
| `object_subclass` | `catalogue-product` |
| `ecf_domain` | `product-value` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8` — offering management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-marketing-xmc539` — marketing ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-pv-operate-zyguzp` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-pv-design-8v4k89` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
