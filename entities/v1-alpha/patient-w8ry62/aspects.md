# Patient — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-patient-w8ry62`](objects-object-patient-w8ry62.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `healthcare`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`patient`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Patient is

- **Kind:** a *party* — the party in a **care-receiving** role. In a healthcare lens the Patient plays the role the Customer plays in a commercial lens — but the relationship is fiduciary, not transactional: the enterprise owes a duty of care, not merely delivery.
- **Subclass:** *patient* — the demand-side party whose wellbeing, not spend, is the outcome of the chain.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Patient relates to the catalog mesh

```
  PATIENT ──admitted──► Treatment ──discharged──► outcome recorded
     │                       │
     └── consents ──► Consent Record    └── billed ──► Invoice / Claim
```

It is the join point between:

- the **party-relationship domain** (the care relationship),
- the **enablement-operations domain** (encounter delivery), and
- the **finance-accounting domain** (claim and billing flows).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `registered → in-care → discharged → follow-up → (deceased / archived)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `w8ry62` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Patient-type BO supports)

- Active patient count and access times
- Care outcomes per cohort
- Readmission rate
- Cost per care episode
