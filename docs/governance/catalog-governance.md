# Catalog Governance

How this catalog changes: the rules that bind every admission, the workflow a
change follows, and the record of decisions that shaped the taxonomy.

Cardinal authorship rules live in [`cardinal-rules.md`](cardinal-rules.md); the
Change Request register lives in [`change-requests/README.md`](../../change-requests/README.md).

## Governing rules

| Rule | Statement | Source |
|---|---|---|
| **BO-TAX-01** | Industry and segment variation is expressed as a new `object_subclass` under an existing `object_class`; a new `object_class` value requires CR-level sign-off | [CR-BO-06](../../change-requests/CR-BO-06-second-admission-wave-proposal.md) §2 |
| **BO-STG-01** | A Business Object is placed at the ECF stage where the business principally manages the type. Types whose whole life is inside a single lifecycle moment are placed at that stage (stage-native); cross-stage types sit at their dominant stage, with other-stage activity expressed through `processes_involved[]`. One record, one cell, at all times | [CR-BO-10](../../change-requests/CR-BO-10-ecf-stage-diversification-proposal.md) §2 |
| **Reference integrity** | Every cross-catalog reference must resolve against the live sibling catalog before landing; deliberately unset fields stay empty rather than forward-referencing (IDM-003) | [dea-metaframework id-system](https://github.com/technehub-labs/dea-metamodel/blob/main/docs/id-system.md) |
| **Content addressing** | The id hash suffix is assigned once at admission from the record content and is immutable thereafter; renaming a slug or moving a file breaks the id contract and is forbidden (IDM-004/005) | [CR-BO-05](../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) §2.6 |
| **Authorship** | Authorship-bearing fields follow cardinal rules R1/R2, enforced by the authorship gate | [`cardinal-rules.md`](cardinal-rules.md) |

## Change workflow

Every structural change — new records, taxonomy changes, migrations — follows the same path:

1. **Proposal CR** (when scope is contested or rules change): a document in `change-requests/` stating the problem, the candidate scope, and the decisions requested from review.
2. **Admission CR**: the record set, class/subclass assignments, ECF cell mapping, and the resolved cross-catalog references.
3. **Landing**: records at the flat layout (`entities/v1-alpha/<slug>-<hash6>/`), each subtree carrying the record YAML, a `README.md`, and an `aspects.md` deep-dive; CATALOG.yaml regenerated.
4. **Post-merge (workflow step 8)**: the CR's status moves to `Merged` and `CATALOG.yaml` is refreshed — the regenerator counts every non-`Merged` CR as open, so skipping this step overstates `open_change_requests`.

All conformance gates run on every PR: schema validation, the CST suite (16 tests), the ID-system gate (IDM-001..008), the entity-system gate, the authorship gate, and the catalog-index freshness check. See [Quality Gates](../../README.md#quality-gates).

## Decision log

Decisions that shaped the catalog, most recent first:

| Date | Decision | Source |
|---|---|---|
| 2026-10-30 | BO-STG-01 adopted; all five stage-native candidates admitted; the pre-role party named **Candidate** | [CR-BO-10](../../change-requests/CR-BO-10-ecf-stage-diversification-proposal.md) §5 |
| 2026-10-30 | New classes `work-item`, `resource`, `location` approved; all 22 T1 records in one admission; explicit sector-lens labels on aspects prose | [CR-BO-06](../../change-requests/CR-BO-06-second-admission-wave-proposal.md) §6 |
| 2026-10-28 | Admission mechanics pinned: flat layout, content-derived hash suffixes, resolved-references-only | [CR-BO-05](../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) |

## Related governance artifacts

- [`reconciliation/authorship-fields.yaml`](../../reconciliation/authorship-fields.yaml) — the authorship-field registry the gate is data-driven from
- [`reconciliation/entity-system-registry.yaml`](../../reconciliation/entity-system-registry.yaml) — the entity-system envelope profile
- [`CATALOG.yaml`](../../CATALOG.yaml) — the machine-generated catalog index (never hand-edited)
- [CHANGELOG.md](../../CHANGELOG.md) — notable changes, Keep-a-Changelog format
