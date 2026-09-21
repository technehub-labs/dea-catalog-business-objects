# v1-alpha Catalog Entries

This directory will hold Business Object catalog entries once Phase 2 content population begins.

Each entry should be a YAML or JSON file following the schema in `../../schemas/entity.schema.json`. Example shape:

```yaml
id: objects:object-customer-12345-xxxxxx
type: BusinessObject
name: Customer Account
object_class: customer
object_subclass: retail
ecf_domain: party-relationship
ecf_stage: operate
current_state: active
version: 1.0.0
description: Active retail customer record in the CRM.
identity:
  primary_id: customer-12345
  external_ids:
    crm_id: SF-0034Q00012
    erp_id: SAP-DEBI-9001
owner: actors:actor-customer-success-manager-xxxxxx
stakeholders:
  - stakeholders:stakeholder-end-customer-xxxxxx
capabilities_consumed:
  - capabilities:capability-manage-account-xxxxxx
  - capabilities:capability-issue-refund-xxxxxx
processes_involved:
  - processes:process-customer-onboarding-xxxxxx
  - processes:process-refund-handling-xxxxxx
```

See [DEA Metamodel BusinessObject schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/business-object.json) for the canonical definition.
