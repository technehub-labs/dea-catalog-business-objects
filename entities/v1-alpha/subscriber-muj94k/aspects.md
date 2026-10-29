# Subscriber — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-subscriber-muj94k`](objects-object-subscriber-muj94k.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Subscriber is

- **Kind:** a *party* in a **subscription relationship**: where the Customer is the commercial party (who may pay), the Subscriber is the service-bound party (who uses). The separation is load-bearing in telecom: one payer, many users.
- **Subclass:** *subscriber* — holds the active subscription; Service Instances, SIM Profiles, and Usage Records attach to it.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Subscriber relates to the catalog mesh

```
  Candidate/Onboarding ──► SUBSCRIBER ──holds──► Service Instance ──metered──► Usage Record
                              │                                  (billed via Invoice / Prepaid Balance)
                              └── identified by ──► Service Number · SIM Profile
```

It is the join point between:

- the **party-relationship domain** (subscription lifecycle),
- the **enablement-operations domain** (service activation and delivery), and
- the **finance-accounting domain** (billing and balance).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `prospect → subscribed → active → suspended → churned (→ Candidate again for win-back)` |

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
- **Content-addressing:** the `muj94k` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Subscriber-type BO supports)

- Subscriber count, gross adds vs. churn (by segment)
- ARPU and ARPA
- Churn rate (voluntary vs. involuntary)
- Base velocity (net adds)
