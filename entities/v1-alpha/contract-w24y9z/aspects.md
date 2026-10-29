# Contract — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-contract-w24y9z`](objects-object-contract-w24y9z.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Contract is

- **Kind:** a *legal-instrument* — an artifact whose essence is enforceability. Where financial instruments carry value, a legal instrument carries *obligation*: mutual duties enforceable between the parties.
- **Subclass:** *commercial-contract* — enterprise-to-party trading terms. The wider vocabulary includes employment, lease, licensing, and NDA subclasses; only the commercial form is instantiated in this seed.
- **Standing character:** unlike transactions, a Contract persists across the many Orders, Invoices, and Grants it governs. It is referenced by them; it does not complete with them.

## Relational aspect — the governance layer

```
                     CONTRACT
                    ╱    │    ╲
       authorizes ╱   frames│     constrains
                 ╱        ╲          ╲
            Customer      Grant      Order ──► Invoice
```

The Contract is the **only seed object in the governance-existence domain**, and that placement is meaningful: it does not participate in order-to-cash as a link in the chain — it stands *above* the chain, defining what the chain is permitted to do. Every commercial object's legitimacy traces back to contractual authorization.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `drafted → negotiated → signed → active → renewed/amended → expired/terminated` |

The distinguishing pattern is **renewal and amendment**: most objects progress monotonically, but a mature Contract portfolio is dominated by amendment cycles, making version lineage and obligation history first-class concerns.

## Operational aspect — acting on the object

- **Created by:** drafting and negotiation processes (legal matter management).
- **Read by:** deal desk, order capture (terms validation), pricing, grant management, compliance.
- **Updated by:** amendments, renewals, assignments, novations.
- **Completed by:** expiry or termination — after which obligations (warranties, survival clauses) may persist.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** the legal-matter-management capability was resolved against the live capabilities catalog before landing; owner/stakeholders/events remain unset per IDM-003.
- **Content-addressing:** the `w24y9z` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).
- **Obligation tracking:** as a legal artifact, the Contract's `state_history` doubles as an obligation-compliance trail — amendments and renewals are governance events, not just state changes.

## Measurement aspect (indicative KPIs a Contract-type BO supports)

- Contract portfolio value and coverage (which commercial activity is contract-authorized)
- Renewal rate and revenue-at-risk from expiring contracts
- Negotiation cycle time: draft → signature
- Obligation and SLA compliance rates; amendment frequency as a churn/instability signal
