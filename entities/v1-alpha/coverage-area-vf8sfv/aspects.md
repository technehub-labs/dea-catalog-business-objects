# Coverage Area — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-coverage-area-vf8sfv`](objects-object-coverage-area-vf8sfv.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Coverage Area is

- **Kind:** a *location* that is a **place of service**: where a Store is where business transacts, the Coverage Area is where service reaches. Its boundaries are license conditions; its quality is the customer experience.
- **Subclass:** *coverage-area* — planned and measured footprint; the telecom specialization of location.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Coverage Area relates to the catalog mesh

```
  License (geographic) ──bounds──► COVERAGE AREA ──carried by──► Network Asset
                                   │
                                   └── measured by──► quality targets / experience
```

It is the join point between:

- the **enablement-operations domain** (network operations, quality),
- the **governance-existence domain** (license conditions), and
- the **party-relationship domain** (where subscribers experience quality).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `licensed → planned → built-out → measured → degraded → re-planned` |

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
- **Content-addressing:** the `vf8sfv` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Coverage Area-type BO supports)

- Population/area covered vs. licensed
- Quality attainment by area (throughput, drop rate)
- Coverage investment per area
- Not-speps/white-spot closure rate
