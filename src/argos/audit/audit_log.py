from datetime import datetime
from pathlib import Path

from argos.models import AlertEvent, ActionPlan, ActionResult, VerificationResult


def log_result(
    event: AlertEvent,
    plan: ActionPlan,
    action_result: ActionResult,
    verification_result: VerificationResult,
    log_path: str = "logs/argos.log",
) -> None:
    file_path = Path(log_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().isoformat()

    line = (
        f"{timestamp} | "
        f"alert={event.alert} | "
        f"host={event.host} | "
        f"action={plan.action} | "
        f"action_success={action_result.success} | "
        f"verify={plan.verify} | "
        f"verify_success={verification_result.success} | "
        f"message={verification_result.message}\n"
    )

    with file_path.open("a", encoding="utf-8") as f:
        f.write(line)