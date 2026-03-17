from argos.detector.detect_events import detect_event
from argos.decision.decision_engine import decide_action
from argos.actions.action_engine import execute_action
from argos.verification.verify_state import verify
from argos.audit.audit_log import log_event


def main():

    incident = detect_event()

    incident = decide_action(incident)

    result = execute_action(incident)

    verify(incident, result)

    log_event(incident)


if __name__ == "__main__":
    main()