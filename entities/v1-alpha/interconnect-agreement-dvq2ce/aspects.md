# Interconnect Agreement — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-interconnect-agreement-dvq2ce`](objects-object-interconnect-agreement-dvq2ce.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Interconnect Agreement is

- **Kind:** a *legal-instrument* that is **carrier-to-carrier**: where the commercial Contract binds a customer, this binds a peer operator. Its settlement runs on usage records — the only contract type whose financial consequence is metered.
- **Subclass:** *interconnect-agreement* — termination and transit terms, settlement rates, technical handover points.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Interconnect Agreement relates to the catalog mesh

```
  Partner (operator) ◄──► INTERCONNECT AGREEMENT ──settled via──► Usage Record (off-net)
                              │
                              └── notified to ──► regulator
```

It is the join point between:

- the **governance-existence domain** (regulatory notification),
- the **party-relationship domain** (the partner-operator relationship), and
- the **finance-accounting domain** (settlement accounting).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `negotiated → signed → in-force → amended → expired/renewed` |

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
- **Content-addressing:** the `dvq2ce` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Interconnect Agreement-type BO supports)

- Settlement accuracy vs. records
- Interconnect cost as share of revenue
- Dispute rate and cycle time
- Agreement coverage of traffic partners
