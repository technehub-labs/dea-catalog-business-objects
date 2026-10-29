# Application — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-application-eewde8`](objects-object-application-eewde8.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Application is

- **Kind:** a *technology-control* — but a **standing asset** rather than a runtime control: where the Feature Flag changes behavior in flight, the Application *is* the behavior.
- **Subclass:** *application* — a deployed software system performing or supporting business functions; includes packaged, custom, and SaaS forms.
- **Boundary semantics:** the defining design question is scope — what counts as one Application (instance, product, or estate) is a governance choice, fixed at admission.

## Relational aspect — how the Application relates to the catalog mesh

```
  Business function ──realized by──► APPLICATION ──runs in──► Environment
                                        │
                                        └── disrupted by ──► Incident
```

The Application is the **standing technology asset of operations**: the durable half of the technology footprint. It is the join point between:

- the **enablement-operations domain** (platform operations),
- the business capabilities it realizes, and
- the **technology-control lifecycle** (Environment, Incident, Feature Flag).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → built/acquired → deployed → in-service → deprecated → retired` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `eewde8` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Application-type BO supports)

- Application coverage of business capabilities
- Availability and MTTR per application
- Cost per application (run vs. build)
- Estate age and end-of-support exposure
