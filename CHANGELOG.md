# Business Objects Catalog Changelog

All notable changes to this catalog are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [v2.4.0-migration] - 2026-09-07

CR-BO-01 implementation: bundled ECF Domain enum migration to the v2.4.0
canonical Domain set (carried by `technehub-labs/dea-metaframework` v2.4.0;
CR-ECF-006 + CR-ECF-007, governed by ADR-ECF-001 + ADR-ECF-002). This repo
was missed by the v2.3.0 wave ground-truth scan and was still carrying the
v2.2.0 Domain enum; both waves applied in a single step. `supply-resources`
-> `strategy-direction`; `people-organization` -> `agency-organization`;
`customer-demand` -> `party-relationship`; `product-offering` ->
`product-value`; `operations-delivery` -> `operations-enablement`;
`finance-value` -> `finance-accounting`. 3 files re-keyed (README,
entity.schema.json, entities/v1-alpha/README.md). No entity YAMLs exist yet;
nothing to migrate at the entity level.
