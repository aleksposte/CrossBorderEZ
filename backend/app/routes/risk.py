from fastapi import APIRouter

router = APIRouter()


@router.post("/score")
async def risk_score(data: dict):
    """
    Stub endpoint: calculate risk score for shipment.
    """
    return {"message": "Risk score calculated (stub)", "score": 0, "data": data}
