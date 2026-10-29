# Machine — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-production-machine-j5z9kv`](objects-object-production-machine-j5z9kv.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `manufacturing`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`production-machine`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Machine is

- **Kind:** a *resource* — a **resource** that is **capacity**: the Machine converts inputs to outputs over time; its availability is the constraint production plans respect.
- **Subclass:** *production-machine* — a durable production asset — the physical counterpart of the capitalized Asset record.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Machine relates to the catalog mesh

```
  Production plan ──loads──► MACHINE ──maintained──► availability
                              │
                              └── capitalized ──► Asset (finance shadow)
```

It is the join point between:

- the **enablement-operations domain** (production, maintenance),
- the **finance-accounting domain** (via the Asset record), and
- capacity governance (bottleneck investment decisions).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `commissioned → in-service → under-maintenance → degraded → decommissioned` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `j5z9kv` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Machine-type BO supports)

- OEE (overall equipment effectiveness)
- Availability / MTBF / MTTR
- Maintenance cost vs. replacement value
- Capacity utilization per machine
