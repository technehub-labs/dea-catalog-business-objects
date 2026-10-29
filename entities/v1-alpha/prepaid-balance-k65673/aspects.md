# Prepaid Balance — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-prepaid-balance-k65673`](objects-object-prepaid-balance-k65673.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Prepaid Balance is

- **Kind:** a *financial-instrument* that is **inverse money**: the operator holds the customer's funds, and usage debits them. The inverse of a receivable — exhaustion suspends service rather than creating debt.
- **Subclass:** *prepaid-balance* — stored value, replenished by top-ups; near-real-time debiting.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Prepaid Balance relates to the catalog mesh

```
  Top-up (Payment) ──replenishes──► PREPAID BALANCE ──debited by──► rated Usage Record
                                     │
                                     └── exhausted ──► Service Instance suspended
```

It is the join point between:

- the **finance-accounting domain** (revenue assurance, balance ledger),
- the **party-relationship domain** (the prepaid subscriber), and
- the **enablement-operations domain** (service suspension triggers).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `opened → credited → in-use → low → exhausted → restored/closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-15.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003; XREF gate enforced in CI).
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces coherence (CR-BO-13).
- **Content-addressing:** the `k65673` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Prepaid Balance-type BO supports)

- Recharge frequency and value (ARPU prepaid)
- Breakage (unredeemed balances)
- Balance-exhaustion to suspension latency
- Revenue-leakage rate on real-time debiting
