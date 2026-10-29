# Insurance Claim — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-insurance-claim-g5mag3`](objects-object-insurance-claim-g5mag3.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `insurance`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`insurance-claim`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Insurance Claim is

- **Kind:** a *transaction* — a **benefit-outbound transaction** triggered by a covered event: the Claim converts a policy promise into a demand for payment.
- **Subclass:** *insurance-claim* — the indemnification request — intake, assessment, and settlement give it a lifecycle distinct from ordinary payables.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Insurance Claim relates to the catalog mesh

```
  Policyholder event ──files──► CLAIM ──assessed──► settled ──► Payment
                                 │
                                 └── repudiated / disputed
```

It is the join point between:

- the **finance-accounting domain** (settlement, reserves),
- the **party-relationship domain** (the policyholder), and
- the **governance-existence domain** (regulatory reporting of claims conduct).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `notified → registered → assessed → approved → settled → closed (or repudiated / disputed)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `g5mag3` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Insurance Claim-type BO supports)

- Claims frequency and severity
- Loss ratio
- Claims cycle time (FNOL to settlement)
- Fraud detection rate
