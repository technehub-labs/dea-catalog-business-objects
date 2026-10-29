# SIM Profile — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-sim-profile-ja8k4x`](objects-object-sim-profile-ja8k4x.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a SIM Profile is

- **Kind:** a *technology-control* that is the **network identity binding**: the cryptographic credentials admitting a device to the network. The telecom counterpart of Party Credential — issued at activation, bound to one subscription, suspended with it.
- **Subclass:** *subscriber-identity-module* — physical SIM or embedded profile holding authentication keys.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the SIM Profile relates to the catalog mesh

```
  Onboarding/Activation ──issues──► SIM PROFILE ──admits──► device to Network Asset
                                     │
                                     └── bound to ──► Subscriber · Service Instance
```

It is the join point between:

- the **party-relationship domain** (the subscription it binds),
- security governance (key management, fraud prevention), and
- the **enablement-operations domain** (the network it unlocks).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `activate` |
| Domain business state | `current_state` | `issued → active → suspended → replaced → retired` |

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
- **Content-addressing:** the `ja8k4x` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a SIM Profile-type BO supports)

- SIM issuance success at activation
- Fraud events via compromised credentials
- Swap/upgrade cycle time
- Dormant credential cleanup
