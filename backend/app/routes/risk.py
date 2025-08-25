from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class RiskRequest(BaseModel):
    shipment_id: str
    hts_code: str
    usmca_complete: bool


class RiskResponse(BaseModel):
    risk_score: int
    issues: list[str]


@router.post("/score", response_model=RiskResponse)
async def calculate_risk(request: RiskRequest):
    """
    Stub endpoint: calculates risk score for a shipment.
    """
    issues = []
    score = 0

    if not request.usmca_complete:
        issues.append("USMCA certificate incomplete")
        score += 50
    if request.hts_code == "010121":
        issues.append("HTS code is a placeholder")
        score += 20

    score = min(score, 100)

    return {"risk_score": score, "issues": issues}
