def decide_action(incident):

    if incident.incident_type == "service_down":
        incident.recommended_action = "restart_service"

    elif incident.incident_type == "high_error_rate":
        incident.recommended_action = "restart_service"

    elif incident.incident_type == "certificate_expiring":
        incident.recommended_action = "renew_certificate"

    else:
        incident.recommended_action = "manual_review"

    print(f"[DECISION] Action decided: {incident.recommended_action}")

    return incident