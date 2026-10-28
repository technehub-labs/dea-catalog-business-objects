# Order — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-order-bpy4g4`](objects-object-order-bpy4g4.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing an Order is

- **Kind:** a *transaction* — a business event that creates obligations. Unlike parties and offerings, transactions are created, progress through states, and complete.
- **Subclass:** *sales-order* — the demand-side commitment from a customer. Sibling subclasses in the wider vocabulary include purchase orders (supply side) and work orders (internal execution); only the sales form is instantiated here.
- **Timestamp-centric:** transactions are anchored to when they occur (commitment time), making them the natural home of due dates, promised dates, and fulfilment windows.

## Relational aspect — the pivot of order-to-cash

```
 Customer ──places──► ORDER ──billed as──► Invoice ──settled by──► Payment
                       │
                       │ lines reference
                       ▼
                    Product
```

The Order is the **only seed object that touches all four domains of the chain**:

- upstream to the **party-relationship** domain (Customer),
- upstream to the **product-value** domain (Product),
- downstream into the **finance-accounting** domain (Invoice, Payment),
- while itself living in **enablement-operations** — the domain that executes fulfilment.

## Lifecycle aspect

The Order carries the richest state model of the seed set. Two lifecycles stay separated:

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → placed → confirmed → in-fulfilment → fulfilled → closed` (plus `cancelled`) |

Transitions are recorded in `state_history` entries with state, ECF stage, date, and note — the auditable trail of the transaction's progress.

## Operational aspect — acting on the object

- **Created by:** order-capture processes at commitment time (`eo-operate` processes).
- **Read by:** fulfilment planning, inventory reservation, credit checking, revenue scheduling.
- **Updated by:** fulfilment progress, amendments, splits, and cancellations.
- **Completed by:** closure on fulfilment confirmation — the Invoice takes over commercially.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** both `eo-operate` process references were resolved against the live processes catalog before landing; unresolved references are forbidden (IDM-003).
- **Content-addressing:** the `bpy4g4` hash suffix is content-derived and immutable; the filesystem path is the id with `:` normalized (IDM-005).
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs an Order-type BO supports)

- Order volume and value (by channel, product, customer segment)
- Fulfilment cycle time: placement → fulfilment → closure
- Order backlog and exception rate (amendments, cancellations, splits)
- Perfect-order rate (on-time, complete, accurate)
