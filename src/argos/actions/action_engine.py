import subprocess

from argos.models import AlertEvent, ActionPlan, ActionResult


def execute_action(plan: ActionPlan, event: AlertEvent, simulate: bool = True) -> ActionResult:
    if simulate:
        return ActionResult(
            success=True,
            message=f"[SIMULATED] Executed action '{plan.action}' for alert '{event.alert}' on host '{event.host}'",
        )

    script_path = f"scripts/{plan.action}.sh"

    try:
        completed = subprocess.run(
            ["bash", script_path],
            check=True,
            capture_output=True,
            text=True,
        )
        return ActionResult(
            success=True,
            message=completed.stdout.strip() or f"Executed {plan.action}",
        )
    except subprocess.CalledProcessError as exc:
        return ActionResult(
            success=False,
            message=exc.stderr.strip() or str(exc),
        )