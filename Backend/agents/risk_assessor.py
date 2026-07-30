# from utils.profanity import contains_profanity
# from utils.scoring import calculate_risk_score


# def assess_risk(analysis):

#     profanity = contains_profanity(
#         analysis["keywords"]
#     )

#     risk = {
#         "contains_profanity": profanity,
#         "risk_score": calculate_risk_score(
#             analysis,
#             profanity
#         )
#     }

#     return risk

import json

from llm.client import generate_response
from llm.prompt.risk_assessor import RISK_ASSESSOR_PROMPT
from llm.validator import (
    validate_response,
    REQUIRED_RISK_FIELDS,
)
from models.ai_models import (
    ContentAnalysis,
    RiskAssessment,
)


def assess_risk(
    analysis: ContentAnalysis,
) -> RiskAssessment:

    ai_risk = generate_response(
        RISK_ASSESSOR_PROMPT,
        json.dumps(analysis.model_dump(), indent=4),
        output_model=RiskAssessment,
    )

    risk = ai_risk.model_dump()

    risk = validate_response(
        risk,
        REQUIRED_RISK_FIELDS,
    )

    return RiskAssessment(**risk)
