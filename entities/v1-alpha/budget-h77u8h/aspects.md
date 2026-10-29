# Budget — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-budget-h77u8h`](objects-object-budget-h77u8h.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Budget is

- **Kind:** a *financial-instrument* that is **authority, not money**: a Budget grants permission to spend; it holds no value itself.
- **Subclass:** *budget* — the approved allocation over a period; it bounds the disbursement instruments (Payment, Grant) that execute against it.
- **Consumption semantics:** a Budget is *consumed* by commitments and actuals; the residual (remaining budget) is a derived, continuously-updated quantity.

## Relational aspect — how the Budget relates to the catalog mesh

```
  BUDGET ──authorizes──► Purchase Order / Grant ──► Payment
    │                                        (actuals)
    └── compared to ──► Journal Entries (plan vs. actual)
```

The Budget is the **control point of spending**: it converts strategy into financial permission. It is the join point between:

- the **strategy-direction domain** (planned intentions),
- the **finance-accounting domain** (control, variance), and
- every spending domain (operations, technology, workforce).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → proposed → approved → in-force → closing → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `h77u8h` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Budget-type BO supports)

- Budget vs. actual variance
- Forecast accuracy through the period
- Commitment coverage (spent + committed vs. budget)
- Rebudgeting frequency
