# Order

Documentation for Business Object record [`objects:object-order-bpy4g4`](objects-object-order-bpy4g4.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-order-bpy4g4` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A request from a customer for products or services, created at commitment time and fulfilled through the enterprise's execution and fulfilment processes. The Order coordinates delivery, production, and revenue recognition and is the operational commitment of the enterprise to its customer.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `transaction` |
| `object_subclass` | `sales-order` |
| `ecf_domain` | `enablement-operations` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k` — operations management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-eo-operate-2jnz85` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-eo-operate-xud3hs` ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
