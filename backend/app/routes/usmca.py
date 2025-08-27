from fastapi import APIRouter
from app.schemas.usmca import USMCACheckRequest, USMCACheckResponse
from app.services.usmca_service import check_usmca_compliance

router = APIRouter()


@router.post("/", response_model=USMCACheckResponse)
def usmca_check(request: USMCACheckRequest):
    compliant, message = check_usmca_compliance(request)
    status_str = "Compliant" if compliant else "Non-Compliant"
    return USMCACheckResponse(status=status_str, message=message)
