# Return — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-return-uwz79t`](objects-object-return-uwz79t.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Return is

- **Kind:** a *transaction* that **reverses** a prior fulfilment: goods flow back to the enterprise, and money may flow back to the customer.
- **Subclass:** *return-rma* — the customer-initiated send-back with an authorization (return merchandise authorization) as its operational handle.
- **Pairing semantics:** every Return references the original fulfilment; it never stands alone.

## Relational aspect — how the Return relates to the catalog mesh

```
  Customer ──sends back──► RETURN ──authorizes──► Credit Note
                            │                     (finance reversal)
  Shipment (reversed leg) ◄─┘
```

The Return is the **exception path of order-to-cash** — the chain running backwards. It is the join point between:

- the **enablement-operations domain** (reverse logistics, inspection),
- the **finance-accounting domain** (Credit Note, refund), and
- the **party-relationship domain** (satisfaction recovery or churn signal).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `requested → authorized → in-transit → received → inspected → credited / rejected` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `uwz79t` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Return-type BO supports)

- Return rate by product / reason
- Return cycle time (request to credit)
- Recovery value vs. original sale
- Return-driven churn correlation
