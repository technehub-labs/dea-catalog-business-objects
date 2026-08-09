# v1-alpha Catalog Entries

This directory will hold Business Object catalog entries once Phase 2 content population begins.

Each entry should be a YAML or JSON file following the schema in `../../schemas/entity.schema.json`. Example shape:

```yaml
id: dea:object-customer-12345
type: BusinessObject
name: Customer Account
object_class: customer
object_subclass: retail
ecf_domain: customer-demand
ecf_stage: operate
current_state: active
version: 1.0.0
description: Active retail customer record in the CRM.
identity:
  primary_id: customer-12345
  external_ids:
    crm_id: SF-0034Q00012
    erp_id: SAP-DEBI-9001
owner: dea:actor-customer-success-manager
stakeholders:
  - dea:stakeholder-end-customer
capabilities_consumed:
  - dea:capability-manage-account
  - dea:capability-issue-refund
processes_involved:
  - dea:process-customer-onboarding
  - dea:process-refund-handling
```

See [DEA Metamodel BusinessObject schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/business-object.json) for the canonical definition.
