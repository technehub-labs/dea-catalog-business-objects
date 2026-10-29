# Feature Flag — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-feature-flag-p5gzf7`](objects-object-feature-flag-p5gzf7.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Feature Flag is

- **Kind:** a *technology-control* — the only seed object whose essence is not what it *is* but what it *governs*: a runtime switch over product behavior.
- **Subclass:** *release-feature-flag* — the release/deployment decoupling switch. The wider vocabulary includes permission toggles, experiment flags, and ops kill-switches; the release form is what this record instantiates.
- **State-as-value:** unlike parties, offerings, or instruments, the flag's payload is basically its state. Its business value lies in state *transitions* (off → canary → on) being safe, targeted, and reversible.

## Relational aspect — the control plane

```
 Capabilities ──act on──► FEATURE FLAG ──controls──► Product
 (enablement, management)       │
                                │ targets
                                ▼
                             Customer
```

The Feature Flag is the **runtime link between the product and what customers experience**:

- the **Product** defines what *could* be experienced,
- the **Customer** is who experiences it,
- the flag decides the mapping between the two at any given moment.

Two capabilities act on it — technology enablement (operating it day to day) and technology management (governing it) — reflecting that flags are both an operational tool and a portfolio to be managed.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `created → enabled-off → canary → fully-on → cleanup-removed` |

A distinguishing trait: the *desired* end state of a healthy flag is **removal** (`cleanup-removed`) once the feature is unconditionally on — stale flags are technical debt. Few Business Objects treat their own retirement as routine hygiene the way flags do.

## Operational aspect — acting on the object

- **Created by:** feature development, alongside the code it gates.
- **Read by:** runtime evaluation (serving), release dashboards, experiment reporting.
- **Updated by:** targeted rollouts (percentage, cohort, environment), incident kill-switch flips.
- **Completed by:** cleanup removal once the gated behavior is unconditional.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** both technology capabilities were resolved against the live capabilities catalog before landing; owner/stakeholders/events remain unset per IDM-003.
- **Content-addressing:** the `p5gzf7` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).
- **Change-visibility discipline:** as a control object, flag transitions are governance-sensitive — a flip can change customer-visible behavior without any code change, so its `state_history` doubles as a release-audit trail.

## Measurement aspect (indicative KPIs a Feature-Flag-type BO supports)

- Flag inventory and state distribution (off / canary / on / stale)
- Rollout health: canary error rates vs. baseline during gradual exposure
- Time-to-full-release: flag created → fully-on
- Flag hygiene: stale-flag count and cleanup lead time
