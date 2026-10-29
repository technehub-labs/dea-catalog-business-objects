# Transformation Plan — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-transformation-plan-mpsz65`](objects-object-transformation-plan-mpsz65.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01):** dominant-stage — steered throughout its life; principally managed at `operate` (BO-STG-01).

## Semantic aspect — what kind of thing a Transformation Plan is

- **Kind:** a *work-item* — the **portfolio-level strategic vehicle**: where the Goal commits an outcome and the Project executes a piece, the Transformation Plan sequences the pieces across years with dependencies, funding phases, and checkpoints.
- **Subclass:** *transformation-plan* — multi-year and steered throughout its life, hence dominant-stage placement at `operate` under BO-STG-01 (not stage-native).
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Transformation Plan relates to the catalog mesh

```
  Goal ──sequences──► TRANSFORMATION PLAN ──funds/phases──► Projects / Initiatives
                          │
                          └── steered by ──► Performance Review / strategic review cycle
```

It is the join point between:

- the **strategy-direction domain** (intent → roadmap → steering),
- the **finance-accounting domain** (funding phases, benefit tracking), and
- the **agency-organization domain** (the initiative portfolio it orchestrates).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `drafted → ratified → in-execution → re-planned → completed / curtailed` |

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
- **Content-addressing:** the `mpsz65` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Transformation Plan-type BO supports)

- Milestone attainment vs. plan
- Benefit realization vs. business case
- Re-plan frequency (plan stability)
- Portfolio dependency risk
