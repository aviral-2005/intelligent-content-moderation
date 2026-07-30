from graph.workflow import app


def main():
    print("=" * 60)
    print(" Intelligent Content Review & Moderation Workflow ")
    print("=" * 60)

    content = input("\nEnter content:\n\n")

    result = app.invoke({"content": content})

    print("\n========== CONTENT ANALYSIS ==========")

    analysis = result["analysis"]

    print(f"Language      : {analysis.language}")
    print(f"Sentiment     : {analysis.sentiment}")
    print(f"Tone          : {analysis.tone}")
    print(f"Keywords      : {', '.join(analysis.keywords)}")
    print(f"Quality Score : {analysis.quality_score}")

    print("\n========== RISK ANALYSIS ==========")

    risk = result["risk"]

    print(f"Risk Level    : {risk.overall_risk_level}")
    print(f"Risk Score    : {risk.overall_risk_score}")
    print(f"Confidence    : {risk.confidence}")

    print("\n========== FINAL DECISION ==========")

    decision = result["decision"]

    print(f"Decision      : {decision['decision']}")
    print(f"Reason        : {decision['reason']}")
    print(f"Action        : {decision['recommended_action']}")


if __name__ == "__main__":
    main()