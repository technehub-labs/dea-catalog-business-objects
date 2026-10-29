# Offboarding Plan — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-offboarding-plan-djz4md`](objects-object-offboarding-plan-djz4md.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the ` retire` moment; it is not an operate-stage object.

## Semantic aspect — what kind of thing a Offboarding Plan is

- **Kind:** a *work-item* — a unit of non-routine work. The Offboarding Plan is an **exit artifact**: it orchestrates the wind-down of one relationship, and its completion *is* the relationship's end.
- **Subclass:** *offboarding-plan* — obligations, access, data, and communication in one frame for one exiting party.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Offboarding Plan relates to the catalog mesh

```
  exiting party ──triggers──► OFFBOARDING PLAN ──executed──► relationship closed
                                 │
                                 └── governs ──► data retention/erasure (Consent Record)
```

It is the join point between:

- the **party-relationship domain** (the relationship it closes),
- the **finance-accounting domain** (final settlements, receivables closure), and
- the **governance-existence domain** (data-retention and regulatory obligations).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | ` retire` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `triggered → planned → in-execution → obligations-settled → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire — the ` retire` moment *is* their end).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-11 per the CR-BO-10 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `djz4md` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Offboarding Plan-type BO supports)

- Offboarding cycle time
- Obligation-settlement completeness at close
- Access-revocation timeliness
- Data-retention compliance rate
