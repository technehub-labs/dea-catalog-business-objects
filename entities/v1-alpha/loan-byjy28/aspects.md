# Loan — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-loan-byjy28`](objects-object-loan-byjy28.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `banking`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`loan`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Loan is

- **Kind:** a *financial-instrument* — a **value-bearing instrument on a term**: the Loan creates a receivable that amortizes over time, with interest as the price of duration and credit risk as the price of uncertainty.
- **Subclass:** *loan* — the lending instrument — origination, disbursement, servicing, and repayment are its four operational phases.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Loan relates to the catalog mesh

```
  Borrower ──originated──► LOAN ──disbursed──► cash out
                │ ▲
                │ └─ repaid (schedule) ──► Payment / Journal Entry
                └── impairments ──► risk provisioning
```

It is the join point between:

- the **finance-accounting domain** (interest, amortization, impairment),
- the **party-relationship domain** (the borrower), and
- risk governance (credit limits, provisioning oversight).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `applied → approved → disbursed → performing → in-arrears → restructured / written-off / closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `byjy28` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Loan-type BO supports)

- Loan book size and growth
- Non-performing loan ratio
- Net interest margin
- Origination-to-disbursement cycle time
