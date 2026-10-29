# Policy — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-policy-nd2t4y`](objects-object-policy-nd2t4y.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Policy is

- **Kind:** a *legal-instrument* that is the enterprise **governing itself**: a Policy binds the enterprise's own people and decisions, not an external counterparty.
- **Subclass:** *policy* — the deliberate statement of position; distinct from a License (external permission) and a Contract (mutual agreement).
- **Normative semantics:** a Policy is expressed as obligation or prohibition; its tests are coverage (who it binds) and compliance (whether conduct matches).

## Relational aspect — how the Policy relates to the catalog mesh

```
  POLICY ──bounds──► Decisions ──executed──► Processes
    │                                    (audited)
    └── interpreted by ──► Standards / procedures
```

The Policy is the **top of the internal control stack**: everything the enterprise decides and does is supposed to trace up to one. It is the join point between:

- the **governance-existence domain** (oversight, audit),
- the **agency-organization domain** (who is bound), and
- every operational domain (whose conduct it shapes).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → adopted → published → in-force → under-review → superseded` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `nd2t4y` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Policy-type BO supports)

- Policy coverage of risk areas
- Compliance-audit findings per policy
- Policy age and review currency
- Exception rate
