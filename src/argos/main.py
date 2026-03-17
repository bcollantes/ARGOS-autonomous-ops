from argos.action_engine import execute_action
from argos.audit import log_result
from argos.decision_engine import decide_action
from argos.detector import detect_event
from argos.verification import verify


def main() -> None:
    event = detect_event()
    plan = decide_action(event)
    action_result = execute_action(plan, event, simulate=True)
    verification_result = verify(event, plan, simulate=True)

    log_result(event, plan, action_result, verification_result)

    print("ARGOS execution completed")
    print(f"Event: {event}")
    print(f"Plan: {plan}")
    print(f"Action result: {action_result}")
    print(f"Verification result: {verification_result}")


if __name__ == "__main__":
    main()