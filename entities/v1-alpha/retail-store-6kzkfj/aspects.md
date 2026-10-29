# Store — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-retail-store-6kzkfj`](objects-object-retail-store-6kzkfj.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `retail`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`retail-store`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Store is

- **Kind:** a *location* — a **location** — the second new class of CR-BO-06 §6.1: a place that the business cares about as an operating unit, not merely an address. The Store is where assortment, inventory, and customer meet physically.
- **Subclass:** *retail-store* — a customer-facing outlet — measured, staffed, and replenished as a unit.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Store relates to the catalog mesh

```
  ASSORTMENT (SKU) ──stocked──► STORE ──sells──► Customer
                                 │
                                 └── replenished ──► warehouse / supply chain
```

It is the join point between:

- the **enablement-operations domain** (sales, inventory, replenishment),
- the **party-relationship domain** (in-person customer experience), and
- facility governance (the physical footprint).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `planned → opened → trading → under-performing → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `6kzkfj` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Store-type BO supports)

- Sales per store and per square meter
- Inventory turn and stockout rate
- Store contribution margin
- Shrinkage rate
