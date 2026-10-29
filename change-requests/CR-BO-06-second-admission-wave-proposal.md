# CR-BO-06: Second Admission Wave Proposal (Candidate Business Objects, Class/Subclass Taxonomy, Industry-Variation Guidance)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-06 |
| **Title** | Second Admission Wave Proposal (Candidate Business Objects, Class/Subclass Taxonomy, Industry-Variation Guidance) |
| **Status** | Proposed (this PR) |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-05 (first admission; record contract proven) |
| **Companion to** | — |

## 1. Purpose

CR-BO-05 landed the first eight seed Business Objects, all clustered around the
commercial order-to-cash chain plus a few cross-industry instruments. This CR does
**not** admit records; it proposes the scope, taxonomy, and admission order for the
**second admission wave** and settles the design question the first wave surfaced:
how Business Objects should vary by organization type, industry, and segment without
breaking the universal ECF coordinate system.

## 2. Design decision: industry variation via subclass, not class

The README already establishes the split:

- **Universal coordinates** (`ecf_domain`, `ecf_stage`) are fixed and
  industry-neutral; every BO lives in exactly one cell.
- **Free-form labels** (`object_class`, `object_subclass`) are domain-specific
  vocabulary (examples given: `retail-customer`, `enterprise-order`).

This CR pins that principle as a cardinal admission rule for future waves:

> **BO-TAX-01.** Industry/segment variation MUST be expressed as a new
> `object_subclass` under an existing `object_class` wherever the kind-of-thing is
> semantically the same. A new `object_class` value requires a CR-level taxonomy
> change (this document or a successor), not a per-record choice.

Rationale: the ECF matrix join points (capabilities, processes, data entities)
bind to records, and the eight-class vocabulary already in use (party,
transaction, offering, financial-instrument, legal-instrument,
technology-control) covers the structural kinds. Industry specificity
(`patient`, `loan`, `finished-good`, `citizen`) is a subclass concern. The
`party` aspects doc already anticipates this: the same real-world party can
appear as distinct subclasses (`customer`, `supplier`, `partner`).

Consequences for the seeded aspects narratives: per-record KPI/join-point
prose (e.g. the Customer "order-to-cash" framing) is commercial-lens
documentation of a universal type, not part of the type contract. Wave-2
records should write aspects prose neutral to sector, or explicitly note the
lens.

## 3. Proposed wave-2 candidates

Grouped by priority tier. Tiers reflect reference resolution readiness: T1
candidates map cleanly to capabilities/processes already populated in the
sibling catalogs; T2 candidates are admitted when their consuming capabilities
resolve; T3 is deferred pending sibling catalog growth.

### T1 — commercial-core extension (admit first)

| Candidate | object_class | object_subclass | ECF (domain, stage) |
|---|---|---|---|
| Supplier | party | supplier | party-relationship, operate |
| Employee | party | employee | party-relationship, operate |
| Partner | party | partner | party-relationship, operate |
| Service | offering | service | product-value, operate |
| Subscription | offering | subscription-plan | product-value, operate |
| Price List | offering | price-list | product-value, operate |
| Quote | transaction | sales-quote | enablement-operations, operate |
| Shipment | transaction | shipment | enablement-operations, operate |
| Return | transaction | return-rma | enablement-operations, operate |
| Purchase Order | transaction | purchase-order | enablement-operations, operate |
| Ticket | transaction | service-ticket | enablement-operations, operate |
| Journal Entry | financial-instrument | journal-entry | finance-accounting, operate |
| Budget | financial-instrument | budget | finance-accounting, operate |
| Credit Note | financial-instrument | credit-note | finance-accounting, operate |
| Asset | financial-instrument | fixed-asset | finance-accounting, operate |
| License | legal-instrument | license | governance-existence, operate |
| Policy | legal-instrument | policy | governance-existence, operate |
| Consent Record | legal-instrument | consent-record | party-relationship, operate |
| Project | work-item | project | agency-organization, operate |
| Application | technology-control | application | enablement-operations, operate |
| Environment | technology-control | environment | enablement-operations, operate |
| Incident | technology-control | service-incident | enablement-operations, operate |

Note: `work-item` is a **new object_class** proposed under BO-TAX-01's CR-level
path (Project, Initiative, Task, OKR are neither transactions nor instruments);
alternatively these may be admitted as `agency-organization`-cell records under
an `initiative` class — decision requested at review.

### T2 — cross-industry universal types (admit after T1)

| Candidate | object_class | object_subclass | ECF (domain, stage) | Sector lens |
|---|---|---|---|---|
| Patient | party | patient | party-relationship, operate | healthcare |
| Citizen | party | citizen | party-relationship, operate | government |
| Member | party | member | party-relationship, operate | non-profit / co-op |
| Claim | transaction | insurance-claim | finance-accounting, operate | insurance |
| Treatment | transaction | care-encounter | enablement-operations, operate | healthcare |
| Loan | financial-instrument | loan | finance-accounting, operate | banking |
| Account | financial-instrument | deposit-account | finance-accounting, operate | banking |
| Benefit | financial-instrument | benefit-entitlement | finance-accounting, operate | government |
| Case | transaction | public-case | governance-existence, operate | government |
| Study Program | offering | education-program | product-value, operate | education |
| Course Section | offering | course-section | enablement-operations, operate | education |
| Lot / Batch | resource | manufacturing-lot | enablement-operations, operate | manufacturing |
| Bill of Material | resource | bill-of-material | enablement-operations, operate | manufacturing |
| Machine | resource | production-machine | enablement-operations, operate | manufacturing |
| Store | location | retail-store | enablement-operations, operate | retail |
| SKU | offering | stock-keeping-unit | product-value, operate | retail |

Note: `resource` and `location` are further **new object_class** candidates
(manufacturing/physical-footprint kinds that fit neither `technology-control`
nor `transaction`); both are proposed here for decision rather than assumed.

### T3 — deferred (no admitting CR until consuming capabilities/processes exist)

Dataset, Report, Document, Goal/OKR, Task, Position, Department, API,
Configuration Item, User Account, Expense Report, Forecast, Tax Record,
Promotion, Warranty/SLA, Discount, NDA, Matter/Claim (legal sense).

Each deferred candidate needs a resolved `capabilities_consumed[]` anchor before
admission; none is admitted on a forward reference (IDM-003).

## 4. Segment variation within a type

Segments vary a type's instances and KPIs, not its record. Per the Customer
aspects doc, one record documents the type; instances (and their segment
attributes) live at the data layer (`identity.primary_id` /
`identity.external_ids`). The catalog therefore models segment variation at
most as subclass pairs (`retail-customer` vs `enterprise-customer`) when the
lifecycle, references, or ECF position genuinely differ — otherwise a single
type with segment-neutral aspects prose is preferred to avoid record
proliferation.

## 5. Admission mechanics (unchanged from CR-BO-05)

- Flat layout, `entities/v1-alpha/object-<slug>-<hash6>/`, id
  `objects:object-<slug>-<hash6>` (IDM-001/IDM-005).
- Hash suffix content-derived at admission, never recomputed (CR-BO-05 §2.6).
- Resolved references only (IDM-003): every T1 admission must resolve
  `capabilities_consumed[]` against `dea-catalog-business-capabilities` and
  `processes_involved[]` against `dea-catalog-business-processes` at HEAD.
- Each subtree carries a README.md (IDM-007); aspects.md deep-dives follow the
  seed pattern where the object is a mesh join point.
- `audit.author` / `audit.reviewed_by` per the authorship registry; CATALOG.yaml
  regenerated via `scripts/regenerate_catalog.py`.

## 6. Open decisions requested from review

1. **New object_class values** — approve `work-item`, `resource`, `location`?
   (BO-TAX-01 requires CR-level sign-off; alternatives noted in §3.)
2. **Wave-2 T1 size** — all 22 T1 records in one admission CR, or split by
   ECF domain (party/offering wave first, financial/legal second)?
3. **Aspects prose lens** — require sector-neutral narratives for new records,
   or explicit-lens labeling as in the seeds?

## 7. Acceptance criteria (for the admission CR this proposal authorizes)

- AC-01 Every admitted record validates against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT over the new records.
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean.
- AC-06 Every `capabilities:*` / `processes:*` reference resolves against the
  sibling catalog HEADs; no forward references.
- AC-07 Any new `object_class` value is recorded in this CR's decision log
  before the record lands.

## 8. Out of scope

- Actual record admission (separate CR once §6 decisions land).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population
  (blocked on sibling catalogs, as CR-BO-05 §2.2).
- Cross-catalog reverse references (each sibling's own CR chain).
