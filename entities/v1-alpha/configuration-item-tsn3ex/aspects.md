# Configuration Item — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-configuration-item-tsn3ex`](objects-object-configuration-item-tsn3ex.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01):** dominant-stage — principally managed at `operate` (BO-STG-01).

## Semantic aspect — what kind of thing a Configuration Item is

- **Kind:** a *technology-control* that is the **unit of change-control traceability**: the CI is not the running function (Application) nor the run-state (Environment) — it is anything whose change must be governed, recorded, and reversible.
- **Subclass:** *configuration-item* — admits the un-modeled remainder (middleware, network segments, runbooks, integrations). Application and Environment remain their own subclasses; this record is documented as the umbrella concept in prose, not by re-parenting (BO-TAX-01; no migration).
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Configuration Item relates to the catalog mesh

```
  Change request ──governs──► CONFIGURATION ITEM ──impacts──► Application / Environment
                                 │
                                 └── relationships ──► impact analysis ( Incident prevention )
```

It is the join point between:

- the **enablement-operations domain** (platform change and operations),
- security governance (control integrity, patch posture), and
- the **technology-control lifecycle** (Application, Environment, Incident).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `identified → baselined → under-change → verified → retired` |

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
- **Content-addressing:** the `tsn3ex` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Configuration Item-type BO supports)

- CI change success rate
- Unauthorized-change count
- CI coverage of the service estate
- Impact-analysis completeness
