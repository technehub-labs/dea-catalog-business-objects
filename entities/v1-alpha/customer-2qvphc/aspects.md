# Customer — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-customer-2qvphc`](objects-object-customer-2qvphc.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Customer is

- **Kind:** a *party* — a business entity with identity and agency, not a transaction, artifact, or instrument. Parties are referenced by other objects; they do not represent events themselves.
- **Subclass:** *customer* — the party in a buying/consuming role vis-à-vis the enterprise. The same real-world party could also appear in other roles (supplier, partner) as distinct subclasses; `customer` scopes this record to the demand-side role.
- **Core identity vs. instance identity:** the record documents the *type* "Customer". Individual customers are instances whose handles live in `identity.primary_id` / `identity.external_ids` at the data layer.

## Relational aspect — how the Customer relates to the catalog mesh

```
            ┌──────────────┐
            │  Capabilities │  customer-management acts on it
            └──────┬───────┘
                   ▼
  Contract ◄──── CUSTOMER ────► Order ────► Invoice ────► Payment
  (counterparty)    │
                    ▼
            Processes (pr-operate, pr-conceive create/update it)
```

The Customer is the **origin of the order-to-cash chain**. This makes it the natural join point between:

- the **party-relationship domain** (who the enterprise deals with),
- the **finance-accounting domain** (what the relationship is worth), and
- the **product-value domain** (what the relationship consumes).

## Lifecycle aspect

Two lifecycles deliberately do not overlap:

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → design → build → activate → operate → improve → retire` |
| Domain business state | `current_state` | `prospect → acquired → active → suspended → churned` |

A customer can be `ecf_stage: operate` (the catalog cell) while its business state moves between `active` and `at-risk` — the state transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** acquisition and onboarding processes (`pr-conceive`, `pr-operate`).
- **Read by:** order capture, invoicing, credit checks, service entitlement checks.
- **Updated by:** relationship management, segmentation, contact-data maintenance.
- **Retired by:** offboarding/churn processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** any structural change to this record requires a Change Request in `change-requests/` (CR gate). The record was admitted under CR-BO-05.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry must resolve against a live sibling-catalog record (IDM-003); this is why owner/stakeholders/events are unset on the seed.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.
- **Content-addressing:** the `2qvphc` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.

## Measurement aspect (indicative KPIs a Customer-type BO supports)

- Customer count and growth (new vs. churned, by segment)
- Revenue per customer relationship (via the Invoice/Payment chain)
- Order-to-cash cycle time per customer
- Relationship duration and retention rate
