from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.peer_agent import PeerAgent

router = APIRouter()
peer_agent = PeerAgent()

class TaskRequest(BaseModel):
    task: str

@router.post("/execute")
def execute_task(request: TaskRequest):
    if not request.task.strip():
        raise HTTPException(status_code=400, detail="Task cannot be empty")
    result = peer_agent.route_task(request.task)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
