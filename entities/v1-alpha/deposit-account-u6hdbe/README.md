# Account

Documentation for Business Object record [`objects:object-deposit-account-u6hdbe`](objects-object-deposit-account-u6hdbe.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `banking` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-deposit-account-u6hdbe` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A holding of funds at the enterprise in which a customer's money is kept and tracked. The Account (deposit sense) is the custody instrument of a banking lens: open, transact, and close processes act on it, and its ledger is reconciled daily against Journal Entries.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | Kind of thing the business cares about |
| `object_subclass` | `deposit-account` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c`

### Processes involved

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-2pmqb2`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
