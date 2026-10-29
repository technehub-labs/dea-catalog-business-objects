# Lot / Batch — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-manufacturing-lot-pkbqev`](objects-object-manufacturing-lot-pkbqev.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `manufacturing`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`manufacturing-lot`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Lot / Batch is

- **Kind:** a *resource* — a **resource** — the first of the new class approved under CR-BO-06 §6.1: a physical thing the business cares about that is neither a party nor an instrument nor a transaction. The Lot is tracked material.
- **Subclass:** *manufacturing-lot* — a quantity produced under shared conditions — the traceability unit of production.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Lot / Batch relates to the catalog mesh

```
  Production Line ──produces──► LOT ── quality-gated ──► shipment / stock
                 │                  │
                 └── recalled ◄──── (traceability chain)
```

It is the join point between:

- the **enablement-operations domain** (production, quality, inventory),
- the **finance-accounting domain** (costing, write-off), and
- regulatory governance (recall and safety obligations).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `created → in-production → quarantined → released → shipped → consumed / recalled` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `pkbqev` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Lot / Batch-type BO supports)

- First-pass yield per lot
- Traceability coverage (one-step back/forward)
- Quarantine and rejection rate
- Recall response time
