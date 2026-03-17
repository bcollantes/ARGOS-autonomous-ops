def log_event(incident):

    print("[AUDIT] Logging incident")

    print(f"""
    Incident: {incident.incident_type}
    Target: {incident.target}
    Action: {incident.recommended_action}
    Status: {incident.status}
    """)