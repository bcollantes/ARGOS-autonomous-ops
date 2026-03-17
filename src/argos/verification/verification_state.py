def verify(incident, result):

    print("[VERIFY] Verifying system state...")

    if result:
        incident.status = "resolved"
        print("[VERIFY] Incident resolved")
        return True

    else:
        incident.status = "failed"
        print("[VERIFY] Incident not resolved")
        return False