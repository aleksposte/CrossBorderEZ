from fastapi import APIRouter
from app.models.usmca_models import USMCACheckRequest, USMCACheckResponse
from app.services.usmca_service import check_usmca_compliance

router = APIRouter()


@router.post("/", response_model=USMCACheckResponse)
def usmca_check(request: USMCACheckRequest):
    status, message = check_usmca_compliance(request)
    return USMCACheckResponse(status=status, message=message)
