# Grant

Documentation for Business Object record [`objects:object-grant-nhdwg9`](objects-object-grant-nhdwg9.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-grant-nhdwg9` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A non-repayable disbursement of funds by the enterprise to a recipient under agreed conditions. The Grant is the outbound counterpart of the Invoice: it is budgeted, awarded, disbursed, and accounted as stewardship of financial resources entrusted to the enterprise.

## Business role

The Grant covers the **outbound money direction** — the enterprise as giver, not claimant:

- It is the deliberate opposite of the **Invoice** (money demanded) and the **Payment** (money received): a Grant is money the enterprise gives away under conditions.
- Its defining trait is **conditionality**: funds are entrusted against agreed purposes, making stewardship — tracking whether funds were used as agreed — the core management concern.
- It extends order-to-cash into a **give-and-account chain**: budget → award → disbursement → accounting.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | A value-bearing financial artifact |
| `object_subclass` | `disbursement-grant` | The outbound, non-repayable instrument |
| `ecf_domain` | `finance-accounting` | Finance-and-Accounting domain |
| `ecf_stage` | `operate` | Operated in steady-state financial operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-stewardship-c7xtfk` — financial stewardship ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Invoice](../invoice-z3fwgb/README.md) | The inbound counterpart: money demanded vs. money given | Grant ↔ Invoice (out/in pair) |
| [Payment](../payment-kgsvrg/README.md) | The cash-direction opposite: funds out vs. funds in | Grant ↔ Payment (out/in pair) |
| [Contract](../contract-w24y9z/README.md) | Conditions may be formalized in contractual instruments | Contract → Grant (frames conditions) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `budgeted → awarded → disbursed → reporting → closed`, with clawback paths on condition breach, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- What funds has the enterprise disbursed, to whom, under what conditions?
- Which disbursements are fully accounted for (stewardship compliance)?
- What is the grant pipeline by budget period (budgeted, awarded, outstanding)?
- Where do clawback or condition-breach risks concentrate?
