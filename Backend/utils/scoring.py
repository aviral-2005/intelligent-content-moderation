def calculate_risk_score(analysis, contains_profanity):
    score = 0.0

    # Negative sentiment increases risk
    if analysis["sentiment"] == "Negative":
        score += 0.30

    # Profanity is a strong indicator
    if contains_profanity:
        score += 0.50

    # Too many important keywords may indicate suspicious content
    if len(analysis["keywords"]) > 8:
        score += 0.10

    # Aggressive or hostile tone increases risk
    if analysis["tone"] in ["Aggressive", "Hostile"]:
        score += 0.10

    # Very low quality content may be spam
    if analysis["quality_score"] < 0.40:
        score += 0.10

    return min(score, 1.0)