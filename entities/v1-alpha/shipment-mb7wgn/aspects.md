# Shipment — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-shipment-mb7wgn`](objects-object-shipment-mb7wgn.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Shipment is

- **Kind:** a *transaction* whose payload is **physical movement**: goods leaving the enterprise under a fulfilment commitment.
- **Subclass:** *shipment* — outbound to customer or between enterprise locations; distinct from the Return, which reverses the flow.
- **Atomicity:** a Shipment is indivisible in law (title and risk transfer at delivery) even when split across carriers or legs.

## Relational aspect — how the Shipment relates to the catalog mesh

```
  Order ──fulfilled via──► SHIPMENT ──received──► Customer
                              │
                              └── triggers ──► Invoice (on delivery terms)
```

The Shipment carries the **physical leg of order-to-cash**: up to it the chain is informational; from it onward the customer holds the goods. It is the join point between:

- the **enablement-operations domain** (logistics, warehouse),
- the **finance-accounting domain** (revenue-recognition trigger on delivery), and
- the **party-relationship domain** (the customer's receipt experience).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `planned → picked → in-transit → delivered → confirmed / lost` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `mb7wgn` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Shipment-type BO supports)

- On-time delivery rate
- Order-to-delivery cycle time
- Shipment cost per unit / order
- Delivery exceptions and loss rate
