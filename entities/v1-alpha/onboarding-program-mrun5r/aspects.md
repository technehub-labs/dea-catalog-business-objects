# Onboarding Program — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-onboarding-program-mrun5r`](objects-object-onboarding-program-mrun5r.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the `activate` moment.

## Semantic aspect — what kind of thing a Onboarding Program is

- **Kind:** a *work-item* — a unit of non-routine work. The Onboarding Program is an **activation artifact**: it converts an accepted party into an operating one.
- **Subclass:** *onboarding-program* — access, accounts, entitlements, and first interactions in one frame for one new party relationship.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Onboarding Program relates to the catalog mesh

```
  accepted party ──enters──► ONBOARDING PROGRAM ──provisions──► operating Customer/Supplier/Member
                                 │
                                 └── issues ──► Party Credential
```

It is the join point between:

- the **party-relationship domain** (the relationship it activates),
- the **enablement-operations domain** (access and entitlements), and
- the **finance-accounting domain** (activation spend and first revenue).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `activate` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `triggered → provisioning → guided-first-use → operational → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-12 per the CR-BO-10 scope continuation.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `mrun5r` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Onboarding Program-type BO supports)

- Onboarding cycle time to first value
- Onboarding completion rate (drop-off)
- Time-to-first-transaction
- Activation cost per party
