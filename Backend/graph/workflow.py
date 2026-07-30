from langgraph.graph import StateGraph, START, END
from graph.state import ModerationState
from graph.nodes import (
    analyzer_node,
    risk_node,
    auto_approve_node,
    human_review_node,
)


def route_by_risk(state: ModerationState):
    level = state["risk"].overall_risk_level.lower()
    if level == "low":
        return "auto_approve"
    return "human_review"


workflow = StateGraph(ModerationState)
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("risk", risk_node)
workflow.add_node("auto_approve", auto_approve_node)
workflow.add_node("human_review", human_review_node)

workflow.add_edge(START, "analyzer")
workflow.add_edge("analyzer", "risk")
workflow.add_conditional_edges("risk", route_by_risk,{"auto_approve": "auto_approve","human_review": "human_review"})
workflow.add_edge("human_review", END)
workflow.add_edge("auto_approve", END)

app = workflow.compile()
