from fastapi import APIRouter
from app.services.workflow_service import get_workflow

router = APIRouter()


@router.get("/{process}")
def workflow_check(process: str):
    workflow = get_workflow(process)
    return {"process": process, "workflow": workflow}
