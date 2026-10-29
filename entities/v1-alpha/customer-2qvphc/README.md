# Customer

Documentation for Business Object record [`objects:object-customer-2qvphc`](objects-object-customer-2qvphc.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-customer-2qvphc` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `party-relationship` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

An external party that buys or consumes the enterprise's products and services. The Customer business object is the atom of the Party-and-Relationship domain: acquisition, retention, and relationship management processes create and update it, and customer-management capabilities act on it.

## Business role

The Customer is the demand-side anchor of the entire commercial model. Every revenue-bearing Business Object traces back to one:

- An **Order** is a Customer's commitment to buy.
- An **Invoice** bills a Customer for fulfilled commitments.
- A **Payment** settles what a Customer owes.
- A **Contract** frames the terms under which the enterprise and the Customer trade.

Because of this, the Customer sits at the head of the **order-to-cash chain** (`Customer → Order → Invoice → Payment`): it is the party whose identity, credit standing, and relationship state give the chain its commercial meaning.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | An actor the business relates to, rather than a transaction or artifact |
| `object_subclass` | `customer` | Specifically a buying/consuming external party |
| `ecf_domain` | `party-relationship` | Party-and-Relationship domain |
| `ecf_stage` | `operate` | Operated in steady-state business operations |
| `current_state` | `active` | Domain-specific business state (distinct from `ecf_stage`) |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb` — customer management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-pr-operate-bbe384` — party-relationship operate-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-pr-conceive-emfgju` — party-relationship conceive-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Order](../order-bpy4g4/README.md) | The Customer places Orders | Customer → Order (initiator) |
| [Invoice](../invoice-z3fwgb/README.md) | The Customer is billed via Invoices | Customer → Invoice (billed party) |
| [Payment](../payment-kgsvrg/README.md) | The Customer settles Invoices with Payments | Customer → Payment (payer) |
| [Contract](../contract-w24y9z/README.md) | The Customer's trading terms are fixed in Contracts | Customer ↔ Contract (counterparty) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `prospect → acquired → active → at-risk/churned`, mirrored in the free-form `current_state` label rather than the universal `ecf_stage`.

## Instance-level identity (illustrative)

```yaml
identity:
  primary_id: customer-12345          # canonical handle
  external_ids:                       # source-system mapping
    crm_id: SF-0034Q00012
    erp_id: SAP-DEBI-9001
```

## Key business questions this object answers

- Who are the enterprise's buyers and consumers, as canonical business entities (not CRM/ERP rows)?
- Which capabilities manage the customer relationship, and which processes create or update it?
- Which downstream financial objects (invoices, payments) attach to a given customer relationship?
