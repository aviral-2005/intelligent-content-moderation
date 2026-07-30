from pydantic import BaseModel


class ContentAnalysis(BaseModel):
    original_content: str
    word_count: int
    character_count: int

    language: str
    sentiment: str
    keywords: list[str]
    tone: str
    quality_score: float


class RiskAssessment(BaseModel):
    overall_risk_score: float
    overall_risk_level: str

    spam_risk: str
    policy_risk: str
    legal_risk: str
    brand_risk: str

    confidence: float

    reasoning: str

    recommended_action: str