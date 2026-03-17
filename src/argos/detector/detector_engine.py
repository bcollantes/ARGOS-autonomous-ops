from argos.core.incident import Incident


def detect_event():

    # simulación inicial
    incident = Incident(
        incident_type="service_down",
        source="monitoring",
        target="payments-api",
        severity="high"
    )

    print(f"[DETECTOR] Detected incident: {incident}")

    return incident