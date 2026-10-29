# Purchase Order — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-purchase-order-qf4tfa`](objects-object-purchase-order-qf4tfa.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Purchase Order is

- **Kind:** a *transaction* — the **inbound commitment**: the enterprise's binding offer of terms to a supplier.
- **Subclass:** *purchase-order* — the procure-to-pay counterpart of the sales Order; structurally similar but legally opposite (the enterprise is the buyer).
- **Accrual semantics:** a Purchase Order is a commitment, not an expense — the supplier invoice that follows is matched against it (three-way match).

## Relational aspect — how the Purchase Order relates to the catalog mesh

```
  Supplier ──receives──► PURCHASE ORDER ──received against──► goods/receipt
                              │                                  │
                              └── matched ──► Invoice (AP) ◄───────┘
```

The Purchase Order opens the **procure-to-pay chain**, mirroring how the Order opens order-to-cash. It is the join point between:

- the **party-relationship domain** (the supplier relationship),
- the **enablement-operations domain** (receiving, inventory), and
- the **finance-accounting domain** (commitments, accruals, accounts payable).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → issued → acknowledged → received → matched → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `qf4tfa` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Purchase Order-type BO supports)

- PO cycle time (raise to receipt)
- Three-way match exception rate
- Commitment vs. actual spend
- Supplier fill-rate and lead time
