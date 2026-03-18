import importlib


def execute_runbook(incident):

    runbook_name = incident.recommended_action

    try:
        module = importlib.import_module(f"argos.runbooks.{runbook_name}")
        result = module.run(incident)

    except ModuleNotFoundError:
        print(f"[RUNBOOK] Unknown runbook: {runbook_name}")
        result = False

    return result