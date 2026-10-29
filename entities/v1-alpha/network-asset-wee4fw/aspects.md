# Network Asset — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-network-asset-wee4fw`](objects-object-network-asset-wee4fw.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Network Asset is

- **Kind:** a *resource* that is **capacity**: the physical and logical components carrying service. Its utilization is the constraint on quality and the case for investment.
- **Subclass:** *network-asset* — radio units, transmission, switches, logical capacity; the telecom specialization of the Machine/Asset pattern.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Network Asset relates to the catalog mesh

```
  SERVICE INSTANCE ──loads──► NETWORK ASSET ──covers──► Coverage Area
                                │
                                └── capitalized as ──► Asset (finance shadow)
```

It is the join point between:

- the **enablement-operations domain** (operations, maintenance),
- the **finance-accounting domain** (capitalization via Asset), and
- capacity planning (utilization drives investment).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `commissioned → in-service → congested → upgraded → decommissioned` |

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
- **Content-addressing:** the `wee4fw` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Network Asset-type BO supports)

- Utilization by asset class
- Congestion incidents per asset
- Coverage quality per area
- Cost per GB delivered
