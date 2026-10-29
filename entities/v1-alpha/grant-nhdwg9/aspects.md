# Grant — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-grant-nhdwg9`](objects-object-grant-nhdwg9.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Grant is

- **Kind:** a *financial-instrument* — value-bearing, deliberately created, with a governed lifecycle.
- **Subclass:** *disbursement-grant* — defined by two traits that distinguish it from all sibling instruments: **non-repayability** (no receivable is created; there is nothing to collect back absent a breach) and **conditionality** (funds are entrusted against agreed purposes).
- **Stewardship character:** unlike an Invoice (a *claim* the enterprise holds) or a Payment (a *settlement* the enterprise receives), a Grant is a *trust* the enterprise extends — which is why the sole capability acting on it is financial stewardship.

## Relational aspect — the outbound mirror

```
            INVOICE (money demanded in)          PAYMENT (money received)
                        ▲                                  ▲
                        └────────── pair ──────────────────┘
                                    vs.
                     GRANT (money given out, conditional)

  Contract ──may frame conditions──► GRANT ──accounted via──► stewardship reporting
```

The Grant completes the **money-direction triangle** of the finance domain: claim (Invoice), settlement (Payment), trust (Grant). Its position also makes it the natural pair of the Contract — grant conditions are often formalized contractually.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `budgeted → awarded → disbursed → reporting → closed` (plus `clawed-back`) |

Two terminal variants matter: `closed` (conditions met, funds fully accounted) and `clawed-back` (condition breach — the exceptional case that reverses disbursement).

## Operational aspect — acting on the object

- **Created by:** grant budgeting and award processes.
- **Read by:** budget control, disbursement scheduling, compliance monitoring.
- **Updated by:** disbursement tranches, recipient reporting, condition reviews.
- **Completed by:** closure on full accounting — or clawback on breach.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** the financial-stewardship capability was resolved against the live capabilities catalog before landing; owner/stakeholders/events remain unset per IDM-003.
- **Content-addressing:** the `nhdwg9` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).
- **Stewardship accountability:** of the seed set, the Grant carries the strongest ongoing-obligation profile — its `state_history` is effectively a compliance log.

## Measurement aspect (indicative KPIs a Grant-type BO supports)

- Disbursement volume by budget period and recipient category
- Stewardship compliance rate: grants fully accounted vs. outstanding reporting
- Time-to-disbursement: award → funds transferred
- Clawback incidence and condition-breach exposure
