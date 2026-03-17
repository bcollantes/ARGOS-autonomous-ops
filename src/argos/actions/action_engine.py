import importlib


def execute_action(incident):

    action_name = incident.recommended_action

    try:
        module = importlib.import_module(f"argos.actions.{action_name}")
        result = module.run(incident)

    except ModuleNotFoundError:
        print(f"[ACTION] Unknown action: {action_name}")
        result = False

    return result