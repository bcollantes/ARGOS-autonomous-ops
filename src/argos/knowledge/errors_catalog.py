ERRORS = {

    "service_down": {
        "severity": "high",
        "recommended_action": "restart_service",
        "verification": "service_healthcheck",
        "autonomous_allowed": True
    },

    "high_error_rate": {
        "severity": "medium",
        "recommended_action": "restart_service",
        "verification": "http_check",
        "autonomous_allowed": True
    },

    "certificate_expiring": {
        "severity": "high",
        "recommended_action": "renew_certificate",
        "verification": "certificate_check",
        "autonomous_allowed": False
    }

}