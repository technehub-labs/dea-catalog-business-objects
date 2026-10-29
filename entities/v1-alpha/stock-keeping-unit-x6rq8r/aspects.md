# SKU — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-stock-keeping-unit-x6rq8r`](objects-object-stock-keeping-unit-x6rq8r.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `retail`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`stock-keeping-unit`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a SKU is

- **Kind:** a *offering* — an **offering at inventory granularity**: the smallest sellable unit tracked for stock and price — where the commercial Product meets the physical Lot.
- **Subclass:** *stock-keeping-unit* — the retail catalogue's unit of sale, distinct from the range-level Product.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the SKU relates to the catalog mesh

```
  PRODUCT ──ranges──► SKU ──stocked──► Store ──priced──► Price List
                       │
                       └── tracked as ──► Lot (batch traceability)
```

It is the join point between:

- the **product-value domain** (assortment, pricing),
- the **enablement-operations domain** (stock, warehouse), and
- the **party-relationship domain** (what the customer actually buys).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `listed → active → out-of-stock → clearance → delisted` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `x6rq8r` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a SKU-type BO supports)

- SKU count and assortment depth
- Availability / on-shelf fill rate
- Sell-through and margin per SKU
- Slow-mover and dead-stock share
