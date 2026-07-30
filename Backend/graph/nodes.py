from graph.state import ModerationState
from agents.content_analyzer import analyze_content
from agents.risk_assessor import assess_risk
# from agents.review_coordinator import review_content


def analyzer_node(state: ModerationState):
    content = state["content"]
    analysis = analyze_content(content)
    state["analysis"] = analysis
    return state


def risk_node(state: ModerationState):
    analysis = state["analysis"]
    risk = assess_risk(analysis)
    state["risk"] = risk
    return state


# def review_node(state: ModerationState):
#     analysis = state["analysis"]
#     risk = state["risk"]
#     decision = review_content(analysis, risk)
#     state["decision"] = decision
#     return state


def auto_approve_node(state):
    state["decision"] = {
        "decision": "Approved",
        "reason": "Low risk content approved automatically.",
        "confidence": state["risk"].confidence,
        "recommended_action": "Approve",
    }
    return state


def human_review_node(state):
    state["decision"] = {
        "decision": "Human Review Required",
        "reason": "Content requires manual review due to elevated risk.",
        "confidence": state["risk"].confidence,
        "recommended_action": "Review",
    }
    return state
