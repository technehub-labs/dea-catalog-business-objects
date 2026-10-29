# Journal Entry

Documentation for Business Object record [`objects:object-journal-entry-khck7r`](objects-object-journal-entry-khck7r.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-journal-entry-khck7r` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

The atomic recording of a debit and credit against ledger accounts that together keep the books balanced. The Journal Entry is the unit of accounting truth: every Invoice, Payment, and payroll run lands in the ledger as journal entries posted through the close.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | Kind of thing the business cares about |
| `object_subclass` | `journal-entry` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c`

### Processes involved

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
