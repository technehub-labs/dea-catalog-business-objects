# Grant

Documentation for Business Object record [`objects:object-grant-nhdwg9`](objects-object-grant-nhdwg9.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-grant-nhdwg9` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A non-repayable disbursement of funds by the enterprise to a recipient under agreed conditions. The Grant is the outbound counterpart of the Invoice: it is budgeted, awarded, disbursed, and accounted as stewardship of financial resources entrusted to the enterprise.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `financial-instrument` |
| `object_subclass` | `disbursement-grant` |
| `ecf_domain` | `finance-accounting` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-stewardship-c7xtfk` — financial stewardship ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
