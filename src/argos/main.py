import argparse

from argos.runbooks.runbook_engine import execute_runbook
from argos.detector.detect_events import detect_event
from argos.detector.detect_events import detect_event
from argos.context.context_builder import build_context
from argos.decision.decision_engine import decide_action
from argos.actions.action_engine import execute_action
from argos.verification.verify_state import verify
from argos.audit.audit_log import log_event
from argos.policy.policy_engine import evaluate_policy

def parse_args():
    parser = argparse.ArgumentParser(description="ARGOS Autonomous Operations")
    parser.add_argument("--env", default="dev", choices=["dev", "tst", "acc", "prd"])
    return parser.parse_args()

def main():

    args = parse_args()
    env = args.env   
    
    incident = detect_event()

    incident = build_context(incident)

    # Sobrescribimos entorno desde CLI
    incident.context["environment"] = env

    print(f"[MAIN] Running in environment: {env}")

    incident, error = decide_action(incident)

    allowed = evaluate_policy(incident, error)

    if not allowed:
        print("[POLICY] Action blocked by policy → manual intervention")
        incident.recommended_action = "manual_review"
        result = False

    else:
        result = execute_runbook(incident, env)

    verify(incident, result)

    log_event(incident)

    print(f"[MAIN] ARGOS execution finished with status: {incident.status}")

def handle_execution_mode(incident, env):

    action = incident.recommended_action

    if env == "dev":
        print("[EXECUTION] DEV mode → auto execution")
        return execute_action(incident)

    elif env == "tst":
        print(f"[EXECUTION] TST mode → confirm execution of {action}")
        confirm = input("Execute action? (y/n): ")

        if confirm.lower() == "y":
            return execute_action(incident)
        else:
            print("[EXECUTION] Skipped by user")
            return False

    elif env in ["acc", "prd"]:
        print(f"[EXECUTION] {env.upper()} mode → approval required for {action}")
        confirm = input("Approve execution? (y/n): ")

        if confirm.lower() == "y":
            return execute_action(incident)
        else:
            print("[EXECUTION] Blocked (no approval)")
            return False

    return False

if __name__ == "__main__":
    main()