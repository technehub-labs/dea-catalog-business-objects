# Ticket — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-ticket-2cudww`](objects-object-ticket-2cudww.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Ticket is

- **Kind:** a *transaction* that is a **request for work**: a Ticket exists to drive something to resolution; its payload is a need, not a good.
- **Subclass:** *service-ticket* — the customer-facing support request (distinct from Incident, which is a technology-service disruption the enterprise experiences itself).
- **Closure semantics:** a Ticket is only done when resolved *and confirmed* — reopening is a first-class transition.

## Relational aspect — how the Ticket relates to the catalog mesh

```
  Customer ──reports──► TICKET ──resolved──► knowledge / fix
                          │                      │
                          └── escalates ──► SLA clock ◄────┘
```

The Ticket is the **operational atom of service delivery** — where the Service offering meets its moments of truth. It is the join point between:

- the **party-relationship domain** (customer experience, escalation),
- the **enablement-operations domain** (service delivery), and
- the **product-value domain** (quality feedback into the offering).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `new → triaged → in-progress → pending-customer → resolved → confirmed / reopened` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `2cudww` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Ticket-type BO supports)

- First-response and resolution time vs. SLA
- Ticket volume by channel and severity
- Reopen rate
- CSAT per closed ticket
