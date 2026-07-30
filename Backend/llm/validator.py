REQUIRED_CONTENT_FIELDS = [
    "language",
    "sentiment",
    "keywords",
    "tone",
    "quality_score",
]


REQUIRED_RISK_FIELDS = [
    "overall_risk_score",
    "overall_risk_level",
    "spam_risk",
    "policy_risk",
    "legal_risk",
    "brand_risk",
    "confidence",
    "reasoning",
    "recommended_action",
]


def validate_response(data: dict, required_fields: list):
    missing = [field for field in required_fields if field not in data]

    if missing:
        raise ValueError(
            f"Missing fields from AI response: {', '.join(missing)}"
        )

    return data