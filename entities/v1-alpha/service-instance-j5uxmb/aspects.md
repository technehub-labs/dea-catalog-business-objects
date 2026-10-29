# Service Instance — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-service-instance-j5uxmb`](objects-object-service-instance-j5uxmb.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Service Instance is

- **Kind:** a *transaction* that is the **running subscription**: an activated, billable instance of one offering to one subscriber. It is not the order (which created it) nor the asset (which carries it) — it is the live relationship between them.
- **Subclass:** *service-instance* — suspends and restores rather than being re-created; the unit of recurring billing.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Service Instance relates to the catalog mesh

```
  Order ──activates──► SERVICE INSTANCE ──carried on──► Network Asset
                         │ │
                         │ └── metered by──► Usage Record
                         └── identified via ──► Service Number · SIM Profile
```

It is the join point between:

- the **enablement-operations domain** (activation, delivery),
- the **product-value domain** (the offering it instantiates), and
- the **finance-accounting domain** (the recurring billing cycle).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `ordered → activated → active → suspended → restored → terminated` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-15.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003; XREF gate enforced in CI).
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces coherence (CR-BO-13).
- **Content-addressing:** the `j5uxmb` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Service Instance-type BO supports)

- Activation success rate and time-to-active
- Instance base vs. subscriber base (instances per subscriber)
- Suspension/restoration cycle frequency
- Involuntary termination rate
