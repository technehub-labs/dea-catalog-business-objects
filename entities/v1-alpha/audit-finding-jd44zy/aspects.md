# Audit Finding — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-audit-finding-jd44zy`](objects-object-audit-finding-jd44zy.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01):** stage-native — this type exists only within the `improve` moment.

## Semantic aspect — what kind of thing a Audit Finding is

- **Kind:** a *work-item* — the **improvement artifact of governance**: the finding is the unit that closes a gap between the current and the required state, tracked from observation to verified remediation.
- **Subclass:** *audit-finding* — stage-native to improve; raised by audit and review processes, scored, remediated, and verified.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Audit Finding relates to the catalog mesh

```
  Audit / governance review ──raises──► AUDIT FINDING ──remediates──► improved Policy / control
                                          │
                                          └── scored by ──► finding severity / recurrence
```

It is the join point between:

- the **governance-existence domain** (audit, control framework),
- the domain where the finding lands (any), and
- risk governance (finding aggregation into the risk view).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `improve` |
| Domain business state | `current_state` | `raised → scored → remediation-planned → remediated → verified-closed (or risk-accepted)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-14.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces the coherence (CR-BO-13).
- **Content-addressing:** the `jd44zy` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Audit Finding-type BO supports)

- Findings raised vs. remediated (aging)
- Repeat-finding rate
- Time to verified closure
- Risk-accepted finding share
