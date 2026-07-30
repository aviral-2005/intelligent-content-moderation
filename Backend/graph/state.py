from typing import TypedDict, NotRequired
from models.api_models import ModerationDecision

from models.ai_models import (
    ContentAnalysis,
    RiskAssessment
)


class ModerationState(TypedDict):
    content: str
    analysis: NotRequired[ContentAnalysis]
    risk: NotRequired[RiskAssessment]
    decision: NotRequired[ModerationDecision]