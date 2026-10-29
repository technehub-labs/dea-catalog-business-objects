# Sunset Plan — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-sunset-plan-34225t`](objects-object-sunset-plan-34225t.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the ` retire` moment; it is not an operate-stage object.

## Semantic aspect — what kind of thing a Sunset Plan is

- **Kind:** a *work-item* — a unit of non-routine work. The Sunset Plan is an **exit artifact** for an offering: it exists so the offering can stop without stranding its customers or its commitments.
- **Subclass:** *sunset-plan* — migration, run-off, and communication in one frame for one retiring offering.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Sunset Plan relates to the catalog mesh

```
  retiring offering ──triggers──► SUNSET PLAN ──executed──► offering out of service
        │                              │
        │                              └── migrates ──► Customers to successor
        └── governed by ──► Contracts / commitments run-off
```

It is the join point between:

- the **product-value domain** (portfolio rationalization, the offering's exit),
- the **party-relationship domain** (customer migration and communication), and
- the **finance-accounting domain** (run-off of commitments and inventory).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | ` retire` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `proposed → approved → announced → in-run-off → completed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire — the ` retire` moment *is* their end).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-11 per the CR-BO-10 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `34225t` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Sunset Plan-type BO supports)

- Customer migration rate to successor
- Run-off completion vs. plan
- Stranded-customer rate
- Sunset cost vs. carrying cost
