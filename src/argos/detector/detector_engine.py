import json
from pathlib import Path

from argos.models import AlertEvent


def detect_event(path: str = "data/sample_alert.json") -> AlertEvent:
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    return AlertEvent(
        alert=raw["alert"],
        host=raw["host"],
        service=raw.get("service"),
        interface=raw.get("interface"),
    )