class Incident:

    def __init__(self, incident_type, source, target, severity):
        self.incident_type = incident_type
        self.source = source
        self.target = target
        self.severity = severity

        self.context = {}
        self.recommended_action = None
        self.status = "detected"

    def __str__(self):
        return f"[{self.incident_type}] target={self.target} severity={self.severity}"