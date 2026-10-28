# Contract

Documentation for Business Object record [`objects:object-contract-w24y9z`](objects-object-contract-w24y9z.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-contract-w24y9z` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `governance-existence` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A legally binding agreement between the enterprise and another party establishing mutual obligations. The Contract is the governance instrument that authorizes the commercial relationship: it constrains orders, pricing, service levels, and the legal standing of the enterprise's operations.

## Business role

The Contract is the **authorizing instrument** of the commercial model — the "may you" behind every transaction:

- It frames the **Customer** relationship: under what terms the enterprise may sell.
- It constrains what **Orders** may contain (scope, pricing, volumes).
- It sets the service levels against which fulfilment is judged.
- It may frame the conditions of a **Grant** (what funds may be used for).

Unlike the transactional objects, a Contract is *standing governance*: it exists before, during, and after the transactions it authorizes.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `legal-instrument` | A legally enforceable artifact |
| `object_subclass` | `commercial-contract` | Enterprise-to-party commercial terms (vs. employment, lease, NDA forms) |
| `ecf_domain` | `governance-existence` | Governance-and-Existence domain |
| `ecf_stage` | `operate` | Operated in steady-state business operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-legal-matter-management-zzbd2u` — legal matter management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Customer](../customer-2qvphc/README.md) | The Contract fixes the Customer's trading terms | Customer ↔ Contract (counterparty) |
| [Order](../order-bpy4g4/README.md) | Orders are placed within the Contract's constraints | Contract → Order (authorizes/constrains) |
| [Grant](../grant-nhdwg9/README.md) | Grant conditions may be formalized contractually | Contract → Grant (frames conditions) |
| [Invoice](../invoice-z3fwgb/README.md) | Invoicing follows the Contract's pricing and terms | Contract ⇢ Invoice (via Order) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `drafted → negotiated → signed → active → renewed/amended → expired/terminated`, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- Under what legal terms may the enterprise transact with each party?
- Which contracts authorize which commercial activity (orders, grants, pricing)?
- What renewal and termination exposure exists across the contract portfolio?
- Where are obligations unmet or service levels at risk?
