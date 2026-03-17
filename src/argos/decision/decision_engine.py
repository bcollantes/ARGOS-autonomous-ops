from pathlib import Path

import yaml

from argos.models import AlertEvent, ActionPlan


def decide_action(event: AlertEvent, rules_path: str = "config/rules.yaml") -> ActionPlan:
    file_path = Path(rules_path)

    with file_path.open("r", encoding="utf-8") as f:
        rules = yaml.safe_load(f)

    rule = rules["rules"].get(event.alert)

    if not rule:
        raise ValueError(f"No rule defined for alert type: {event.alert}")

    return ActionPlan(
        action=rule["action"],
        verify=rule["verify"],
    )