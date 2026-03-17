def log_event(incident):

    log_entry = f"""
Incident: {incident.incident_type}
Target: {incident.target}
Action: {incident.recommended_action}
Status: {incident.status}
"""

    print("[AUDIT] Logging incident")
    print(log_entry)

    with open("argos_audit.log", "a") as f:
        f.write(log_entry + "\n")