from fastapi import APIRouter

from graph.workflow import app as workflow_app
from models.api_models import ModerationRequest, ModerationResponse

router = APIRouter()


@router.post("/moderate", response_model=ModerationResponse)
def moderate(request: ModerationRequest):
    final_state = workflow_app.invoke(
        {
            "content": request.content
        }
    )

    return ModerationResponse(
        analysis=final_state["analysis"],
        risk=final_state["risk"],
        decision=final_state["decision"],
    )