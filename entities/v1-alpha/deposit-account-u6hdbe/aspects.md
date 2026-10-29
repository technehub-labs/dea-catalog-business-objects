# Account — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-deposit-account-u6hdbe`](objects-object-deposit-account-u6hdbe.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `banking`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`deposit-account`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Account is

- **Kind:** a *financial-instrument* — the **custody instrument**: the Account holds and tracks a customer's funds; its defining behavior is the ledger balance reconciled daily, not a single value transfer.
- **Subclass:** *deposit-account* — the deposit sense of Account — a standing holding, distinct from the transactional ledger Account of general bookkeeping.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Account relates to the catalog mesh

```
  Customer ──deposits/withdraws──► ACCOUNT ──ledger──► Journal Entry
                 │                    │
                 └── interest ─────────┴─ daily reconciliation
```

It is the join point between:

- the **finance-accounting domain** (ledger, reconciliation),
- the **party-relationship domain** (the depositor), and
- regulatory governance (deposit insurance, liquidity rules).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `opened → active → dormant → closed (or frozen / escheated)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `u6hdbe` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Account-type BO supports)

- Account count and balances
- Net interest cost of deposits
- Dormancy and churn rate
- Reconciliation break rate
