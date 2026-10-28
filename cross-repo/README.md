# Cross-Repo Coordination Artifacts (CR-BO-05 reverse references)

This directory holds the reverse-reference CRs for the sibling catalogs,
co-located here by the org's cross-repo CR convention (the processes
catalog's CR-ECF-CG-004 precedent) while this repo's PR #11 is the carrier.

Each sibling change is delivered as a `git format-patch` bundle (branch
`vibe/bo-reverse-refs-9b5035` in each sibling repo) plus the CR doc that
would land in that sibling's `change-requests/`. Apply from a checkout of
the sibling repo at its `main`:

```
git am path/to/this/directory/<repo>/0001-*.patch
```

Then push the branch and open the PR per that repo's own governance chain
(the patch commit message and CR doc are the governance artifacts).

## Contents

| Repo | CR | Change | Verified |
|---|---|---|---|
| `dea-catalog-business-capabilities` | CR-DEA-BC-61 | Schema gains optional id-typed `business_object_refs[]` (org-wide `objects:object-*` pattern); populated on the 9 capabilities this catalog's records reference via `capabilities_consumed[]` (exact inverse edges); CR-DEA-BC-58 business-object reconciliation register refresh (upstream unblocked) | All gates at that HEAD: schema 29/29, IDM, relationship integrity, entity system, authorship, CR-index, catalog index, ECF conformance, doc conformance/links |
| `dea-catalog-business-processes` | CR-BP-133 | `business_objects_involved[]` on the 6 process records this catalog's records reference via `processes_involved[]` (exact inverse edges; no schema change needed — Process schema permits additional top-level properties); CR-BP-124 cross-catalog resolution registry `id_format` truth fix for this catalog's scope (`dea:object-*` → `objects:object-*`) | CR metadata (175 CRs), IDM (3,723 records), catalog index; 6 records parse + schema-validate |

## Integrity invariants

- Every `objects:object-*` reference in both patches resolves against this
  catalog's canonical records at this PR's HEAD (the 8 CR-BO-05 admissions).
- The (capability, object) and (process, object) pairs are exactly the
  inverse of the `capabilities_consumed[]` / `processes_involved[]` edges
  declared by this catalog's records — no new semantic claims, no
  name-similarity inference (the inference CR-DEA-BC-57 forbids).
- Neither patch touches any field the sibling gates resolve in-namespace:
  `objects:` references are cross-catalog and outside each sibling's
  IDM-003 resolution scope by design.

## Status

- Built and gate-verified at sibling `main` HEADs on branch
  `vibe/bo-reverse-refs-9b5035` in both sibling repos.
- Delivery from this environment is sandbox-blocked (git push to sibling
  repos is not authenticated); apply the patches from any environment with
  sibling-repo write access, per the instructions above.
