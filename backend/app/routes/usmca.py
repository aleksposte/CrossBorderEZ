from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.usmca import USMCACheckRequest, USMCACheckResponse
from app.services.usmca_service import check_usmca_compliance

router = APIRouter(prefix="/api/usmca", tags=["USMCA"])


@router.post("/", response_model=USMCACheckResponse)
def usmca_check(request: USMCACheckRequest):
    """
    Simple USMCA compliance check endpoint.
    """
    return check_usmca_compliance(request)


class USMCACheckRequest(BaseModel):
    description: str
    hs_code: str
    country_of_origin: str


class USMCACheckResponse(BaseModel):
    status: str
    explanation: str


@router.post("/check", response_model=USMCACheckResponse)
def check_usmca(data: USMCACheckRequest):
    if data.country_of_origin.lower() in ["canada", "mexico"]:
        return USMCACheckResponse(status="Compliant", explanation="Meets USMCA rules")
    else:
        return USMCACheckResponse(
            status="Non-Compliant", explanation="Does not meet USMCA rules"
        )
