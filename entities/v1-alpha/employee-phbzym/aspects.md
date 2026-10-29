# Employee — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-employee-phbzym`](objects-object-employee-phbzym.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Employee is

- **Kind:** a *party* — but a party **inside** rather than outside the enterprise. The Employee is the only party bound to the enterprise by an employment relationship rather than a commercial one.
- **Subclass:** *employee* — distinct from contractors (a `partner` or supplier role) and from the general notion of workforce; the record scopes the employed-person role.
- **Core identity vs. instance identity:** the record documents the *type*; individual employees' handles live at the data layer.

## Relational aspect — how the Employee relates to the catalog mesh

```
  Position ──held by──► EMPLOYEE ──executes──► Project / Ticket
                          │
                          ├─ paid via ──► Payroll (fa-operate)
                          └─ developed ─► Learning & Development
```

The Employee is the **operational agent of the organization**: nearly every process in the catalog is ultimately executed by one. It is the join point between:

- the **agency-organization domain** (positions, org units),
- the **finance-accounting domain** (payroll, cost), and
- the **enablement-operations domain** (work execution).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `applicant → hired → onboarding → active → leave → exited` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `phbzym` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Employee-type BO supports)

- Headcount and growth by segment
- Cost per employee (payroll + overhead)
- Attrition rate and retention
- Utilization and productivity per role
