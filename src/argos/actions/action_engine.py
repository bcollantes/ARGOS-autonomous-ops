def execute_action(incident):

    action = incident.recommended_action

    print(f"[ACTION] Executing action: {action}")

    if action == "restart_service":
        print(f"Restarting service: {incident.target}")
        result = True

    elif action == "renew_certificate":
        print("Renewing certificate...")
        result = True

    else:
        print("Manual intervention required")
        result = False

    return result