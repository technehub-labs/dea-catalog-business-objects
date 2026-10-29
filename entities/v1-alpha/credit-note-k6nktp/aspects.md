# Credit Note — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-credit-note-k6nktp`](objects-object-credit-note-k6nktp.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Credit Note is

- **Kind:** a *financial-instrument* that runs **against** a receivable: a Credit Note reduces what a customer was previously invoiced.
- **Subclass:** *credit-note* — the receivable-reversing counterpart of the Invoice; triggered by Returns, corrections, or concessions.
- **Pairing semantics:** like the Return, it references a prior instrument; it is the finance leg of a commercial reversal.

## Relational aspect — how the Credit Note relates to the catalog mesh

```
  RETURN ──authorizes──► CREDIT NOTE ──reduces──► Invoice (receivable)
                              │
                              └── settles ──► Payment (refund) / offset
```

The Credit Note is the **reversal instrument of order-to-cash**: it keeps the receivables ledger honest when reality walks back a sale. It is the join point between:

- the **finance-accounting domain** (receivables, revenue adjustment),
- the **enablement-operations domain** (Return events), and
- the **party-relationship domain** (goodwill, retention).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → issued → applied → settled → archived` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `k6nktp` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Credit Note-type BO supports)

- Credit-note rate (credit value vs. invoiced value)
- Credit cycle time (return to credit)
- Credit reason distribution
- Days sales outstanding impact
