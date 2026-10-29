# License — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-license-na3j53`](objects-object-license-na3j53.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a License is

- **Kind:** a *legal-instrument* that is **permission granted from outside**: unlike a Contract (mutual terms), a License is one-directional authority from an external regulator or owner.
- **Subclass:** *license* — operating permits, software licenses, professional licenses; the common shape is granted authority on terms.
- **Dependency semantics:** a License's loss can remove the enterprise's right to operate at all — it is an existence condition, not merely a commercial one.

## Relational aspect — how the License relates to the catalog mesh

```
  Authority ──grants──► LICENSE ──permits──► enterprise activity
                          │
                          ├── bounded by ──► conditions / scope
                          └── renews / expires on ──► dates
```

The License is an **existence-layer control** in the governance domain: it sits above commercial instruments because it conditions them. It is the join point between:

- the **governance-existence domain** (right to operate),
- the **party-relationship domain** (grantor authority), and
- every regulated operational domain.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `applied → granted → active → renewal-due → renewed / lapsed / revoked` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `na3j53` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a License-type BO supports)

- License coverage of regulated activities
- Renewal lead time and lapse incidents
- License cost and utilization
- Compliance findings per license
