from pydantic import BaseModel
from models.ai_models import ContentAnalysis, RiskAssessment


class ModerationRequest(BaseModel):
    content: str

class ModerationDecision(BaseModel):
    decision: str
    reason: str
    confidence: float
    recommended_action: str

class ModerationResponse(BaseModel):
    analysis: ContentAnalysis
    risk: RiskAssessment
    decision: ModerationDecision
