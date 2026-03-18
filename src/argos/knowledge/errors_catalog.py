ERRORS = {

    "service_down": {
        "runbook": "restart_service_runbook",
        "severity": "high",
        "recommended_action": "restart_service",
        "verification": "service_healthcheck",
        "autonomous_allowed": True
    },

    "high_error_rate": {
        "runbook": "restart_service_runbook",
        "severity": "medium",
        "recommended_action": "restart_service",
        "verification": "http_check",
        "autonomous_allowed": True
    },

    "certificate_expiring": {
        "runbook": "restart_service_runbook",
        "severity": "high",
        "recommended_action": "renew_certificate",
        "verification": "certificate_check",
        "autonomous_allowed": False
    }

}