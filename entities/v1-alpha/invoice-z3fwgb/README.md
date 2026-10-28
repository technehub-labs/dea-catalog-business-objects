# Invoice

Documentation for Business Object record [`objects:object-invoice-z3fwgb`](objects-object-invoice-z3fwgb.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-invoice-z3fwgb` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A commercial document issued by the enterprise to a customer, itemizing products or services delivered and demanding payment. The Invoice is the financial counterpart of the Order: it converts fulfilled commitments into receivables and drives revenue recognition and collections.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `financial-instrument` |
| `object_subclass` | `billing-invoice` |
| `ecf_domain` | `finance-accounting` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c` — financial resource management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-financial-stewardship-c7xtfk` — financial stewardship ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
