from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class USMCACertificateRequest(BaseModel):
    exporter_name: str
    importer_name: str
    producer_name: str
    hs_code: str
    description: str
    country_of_origin: str
    certifier_name: str
    certifier_signature: str
    certifier_date: str


class USMCACertificateResponse(BaseModel):
    certificate_id: str
    status: str
    details: dict


@router.post("/certificate", response_model=USMCACertificateResponse)
async def generate_certificate(request: USMCACertificateRequest):
    """
    Stub: generate USMCA Certificate of Origin.
    """
    return {
        "certificate_id": "USMCA-123456",
        "status": "generated",
        "details": request.dict(),
    }
