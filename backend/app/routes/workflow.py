from fastapi import APIRouter

router = APIRouter(prefix="/api/workflow", tags=["Workflow"])


@router.post("/process-shipment")
def process_shipment():
    return {"status": "Not implemented yet"}
