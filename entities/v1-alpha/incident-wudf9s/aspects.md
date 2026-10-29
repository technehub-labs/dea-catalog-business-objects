# Incident — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-incident-wudf9s`](objects-object-incident-wudf9s.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Incident is

- **Kind:** a *technology-control* that is an **unplanned exception**: an Incident is not part of the designed behavior of technology — it is the moment the design fails.
- **Subclass:** *service-incident* — an unplanned interruption or degradation of a technology service; distinct from the Ticket, which is a *customer's* request, and from the Problem, which is the underlying cause an Incident is a symptom of.
- **Clock semantics:** an Incident is defined by its **clocks** — detection, response, restoration — and its lifecycle is a race against them.

## Relational aspect — how the Incident relates to the catalog mesh

```
  ENVIRONMENT / APPLICATION ──fails──► INCIDENT ──restored──► service resumed
       ▲                                   │
       └── post-incident review ◄──────────┘ (recurrence prevention)
```

The Incident is the **operational exception object of technology management**: it is where continuity planning meets reality. It is the join point between:

- the **enablement-operations domain** (platform operations),
- the **governance-existence domain** (continuity, risk oversight), and
- the customer experience (Incidents become Tickets when customers notice).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `detected → triaged → worked → mitigated → restored → closed → (problem follow-up)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `wudf9s` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Incident-type BO supports)

- MTTD / MTTR by severity
- Incident volume by service and cause
- Repeat-incident rate (same cause)
- SLA/OLA attainment on restoration
