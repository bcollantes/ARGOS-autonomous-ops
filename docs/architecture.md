# ARGOS Architecture

ARGOS implements a **closed-loop autonomous remediation model** for operational incidents.

## High-Level Flow

```text
                ┌────────────────────┐
                │  Alert / Event     │
                │  (JSON / Metrics / │
                │   Logs / Alerts)   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     Detector       │
                │ Normalize / Parse  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  Decision Engine   │
                │ Rules / Context    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   Action Engine    │
                │ Scripts / Commands │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Verification    │
                │ Health / Status    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     Audit Log      │
                │ Incident Record    │
                └────────────────────┘
```

Detect → Decide → Act → Verify

## Core Components

### Detector

Collects and normalizes operational events from different sources.

Examples:

- JSON alerts
- Prometheus / Alertmanager
- Log pipelines
- Service health checks

### Decision Engine

Maps events to remediation actions using rules and contextual information.

Examples:

- service_down → restart_service
- port_blocked → reset_interface

### Action Engine

Executes remediation through scripts, APIs or automation tools.

Examples:

- shell scripts
- system commands
- Ansible
- API calls

### Verification

Checks whether the corrective action solved the incident.

Examples:

- HTTP status check
- port availability
- ping
- process status

### Audit Log

Records the incident, action and result for traceability.

# Initial MVP Scope

## ARGOS v0.1 focuses on:

- local or simulated event input
- rule-based decisions
- scripted remediation actions
- basic verification checks
- incident logging

## Future Extensions

Planned future directions include:

- Prometheus / Alertmanager integration
- AI-assisted decision support
- certificate lifecycle remediation
- integration with AEGIS Identity Fabric
- policy-based autonomous response