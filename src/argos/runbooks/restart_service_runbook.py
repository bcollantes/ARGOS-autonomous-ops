def run(incident):

    print("[RUNBOOK] restart_service_runbook")

    # 1. acción
    print(f"[RUNBOOK] Restarting service: {incident.target}")

    # aquí luego irá la llamada real
    action_result = True

    # 2. verificación
    if action_result:
        print("[RUNBOOK] Verifying service health...")
        verified = True
    else:
        verified = False

    return verified