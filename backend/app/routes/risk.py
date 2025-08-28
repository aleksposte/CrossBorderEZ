from fastapi import APIRouter
from app.services.risk_service import assess_risk

router = APIRouter()


@router.get("/")
def risk_check(item: str):
    risk = assess_risk(item)
    return {"item": item, "risk": risk}
