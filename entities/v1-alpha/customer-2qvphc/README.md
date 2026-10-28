# Customer

Documentation for Business Object record [`objects:object-customer-2qvphc`](objects-object-customer-2qvphc.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-customer-2qvphc` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

An external party that buys or consumes the enterprise's products and services. The Customer business object is the atom of the Party-and-Relationship domain: acquisition, retention, and relationship management processes create and update it, and customer-management capabilities act on it.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `party` |
| `object_subclass` | `customer` |
| `ecf_domain` | `party-relationship` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb` — customer management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-pr-operate-bbe384` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-pr-conceive-emfgju` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
