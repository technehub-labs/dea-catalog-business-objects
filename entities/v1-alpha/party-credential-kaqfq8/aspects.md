# Party Credential — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-party-credential-kaqfq8`](objects-object-party-credential-kaqfq8.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the `activate` moment.

## Semantic aspect — what kind of thing a Party Credential is

- **Kind:** a *technology-control* that is an **identity binding**: the credential is not the party, and not the account — it is the issued secret that authenticates one to the other.
- **Subclass:** *party-credential* — account, key, or token issued at provisioning, rotated in service, revoked at exit.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Party Credential relates to the catalog mesh

```
  Onboarding Program ──issues──► PARTY CREDENTIAL ──authenticates──► party to systems
                                    │
                                    └── revoked at ──► Offboarding Plan execution
```

It is the join point between:

- the **party-relationship domain** (whose identity it carries),
- security governance (issuance, rotation, revocation), and
- the **enablement-operations domain** (the systems it unlocks).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `activate` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `issued → active → rotated → suspended → revoked` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-12 per the CR-BO-10 scope continuation.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `kaqfq8` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Party Credential-type BO supports)

- Credential rotation compliance
- Revocation timeliness at exit
- Orphan-credential count
- Authentication failure and lockout rates
