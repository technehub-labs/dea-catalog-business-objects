# Consent Record — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-consent-record-gacq7d`](objects-object-consent-record-gacq7d.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Consent Record is

- **Kind:** a *legal-instrument* that is **party-held permission**: unlike a Policy (enterprise binds itself) or Contract (mutual terms), a Consent Record is evidence of a right the *party* holds over the enterprise.
- **Subclass:** *consent-record* — versioned evidence of permission for named processing or contact purposes.
- **Withdrawal semantics:** the defining event is **withdrawal** — it terminates permissions retroactively going forward and often triggers downstream erasure or suppression.

## Relational aspect — how the Consent Record relates to the catalog mesh

```
  Party ──grants──► CONSENT RECORD ──authorizes──► data processing / contact
                        │
                        └── withdrawn ──► suppression / erasure obligations
```

The Consent Record is the **compliance hinge of the party relationship**: it converts a legal obligation into an operational state the enterprise must track. It is the join point between:

- the **party-relationship domain** (the party's rights),
- information governance (processing permissions), and
- every domain that touches customer data or contact.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `captured → active → amended → withdrawn → (erasure executed)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `gacq7d` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Consent Record-type BO supports)

- Consent coverage of the active base
- Grant vs. withdrawal rate
- Time-to-effect of withdrawals
- Consent-channel distribution
