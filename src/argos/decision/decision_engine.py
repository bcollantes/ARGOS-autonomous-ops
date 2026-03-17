from argos.knowledge.errors_catalog import ERRORS


def decide_action(incident):

    error = ERRORS.get(incident.incident_type)

    if error:
        incident.recommended_action = error["recommended_action"]
    else:
        incident.recommended_action = "manual_review"

    print(f"[DECISION] Action decided: {incident.recommended_action}")

    return incident, error