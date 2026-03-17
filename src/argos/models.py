from dataclasses import dataclass
from typing import Optional


@dataclass
class AlertEvent:
    alert: str
    host: str
    service: Optional[str] = None
    interface: Optional[str] = None


@dataclass
class ActionPlan:
    action: str
    verify: str


@dataclass
class ActionResult:
    success: bool
    message: str


@dataclass
class VerificationResult:
    success: bool
    message: str