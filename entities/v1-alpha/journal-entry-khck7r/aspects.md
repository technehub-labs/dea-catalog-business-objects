# Journal Entry — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-journal-entry-khck7r`](objects-object-journal-entry-khck7r.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Journal Entry is

- **Kind:** a *financial-instrument* that is **atomic bookkeeping**: one debit, one credit, always balanced — the indivisible unit of accounting truth.
- **Subclass:** *journal-entry* — the ledger-level record; every other financial instrument (Invoice, Payment, Budget) lands in the books *as* journal entries.
- **Immutability:** a posted Journal Entry is never edited; corrections arrive as new reversing entries.

## Relational aspect — how the Journal Entry relates to the catalog mesh

```
  Invoice / Payment / Payroll ──post──► JOURNAL ENTRY ──► General Ledger
                                              │
                                              └── feeds ──► Financial Reporting
```

The Journal Entry is the **convergence point of accounting**: every money-touching object in the catalog ultimately becomes one. It is the join point between:

- the **finance-accounting domain** (ledger, close, reporting),
- every operational domain (via posting), and
- governance (audit trail).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → reviewed → posted → (reversing entry) → archived` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `khck7r` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Journal Entry-type BO supports)

- Entry volume and backlog at close
- Close cycle time
- Manual vs. automated entry ratio
- Reversal/reclass rate
