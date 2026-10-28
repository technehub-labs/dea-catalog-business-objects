# Feature Flag

Documentation for Business Object record [`objects:object-feature-flag-p5gzf7`](objects-object-feature-flag-p5gzf7.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-feature-flag-p5gzf7` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A configuration switch controlling the runtime visibility or behavior of a product feature. The Feature Flag decouples deployment from release: technology-enablement capabilities act on it, and its state governs what customers experience without a redeployment.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `technology-control` |
| `object_subclass` | `release-feature-flag` |
| `ecf_domain` | `enablement-operations` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-enablement-y6nkws` — technology enablement ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-technology-management-maus5n` — technology management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
