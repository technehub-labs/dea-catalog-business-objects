# Contract

Documentation for Business Object record [`objects:object-contract-w24y9z`](objects-object-contract-w24y9z.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-contract-w24y9z` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A legally binding agreement between the enterprise and another party establishing mutual obligations. The Contract is the governance instrument that authorizes the commercial relationship: it constrains orders, pricing, service levels, and the legal standing of the enterprise's operations.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `legal-instrument` |
| `object_subclass` | `commercial-contract` |
| `ecf_domain` | `governance-existence` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-legal-matter-management-zzbd2u` — legal matter management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
