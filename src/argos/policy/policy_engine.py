def evaluate_policy(incident, error_definition):

    env = incident.context.get("environment")
    autonomous_allowed = error_definition.get("autonomous_allowed", False)

    print(f"[POLICY] Evaluating policy for env={env}")

    # Política base por entorno
    if env == "dev":
        return True

    elif env == "tst":
        return True

    elif env == "acc":
        return False  # requiere validación

    elif env == "prd":
        return autonomous_allowed

    return False