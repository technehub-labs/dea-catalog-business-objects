# Supplier — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-supplier-g7m7fu`](objects-object-supplier-g7m7fu.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Supplier is

- **Kind:** a *party* — a business entity with identity and agency on the **supply side** of the enterprise. The Supplier is the mirror image of the Customer: where the Customer is the demand-side counterparty, the Supplier is the source-side counterparty.
- **Subclass:** *supplier* — the party in a providing role vis-à-vis the enterprise. The same real-world party could appear as a `customer` or `partner` subclass in other roles; this record scopes the supply-side role only.
- **Core identity vs. instance identity:** the record documents the *type*; individual suppliers' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Supplier relates to the catalog mesh

```
  CUSTOMER ──► Order ──► fulfillment ──► SUPPLIER
       ▲                                  │
       └── Invoice ◄── Payment ────────────┘
        (order-to-cash)      (procure-to-pay)
```

The Supplier is the **origin of the procure-to-pay chain**, the inbound counterpart of the order-to-cash chain. It is the join point between:

- the **party-relationship domain** (who the enterprise buys from),
- the **enablement-operations domain** (procurement cycle, receiving), and
- the **finance-accounting domain** (accounts payable, spend).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `prospect → qualified → approved → active → under-review → suspended → exited` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `g7m7fu` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Supplier-type BO supports)

- Supplier count and concentration (spend share by supplier)
- On-time delivery and quality performance per supplier
- Procure-to-pay cycle time per supplier
- Supplier risk and compliance coverage
