from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ShipmentRequest(BaseModel):
    shipment_id: str
    description: str
    exporter_name: str
    importer_name: str
    producer_name: str
    hs_code: str = ""
    country_of_origin: str
    certifier_name: str
    certifier_signature: str
    certifier_date: str


class ShipmentResponse(BaseModel):
    shipment_id: str
    usmca_status: str
    hts_code: str
    documents_zip: str
    risk_score: int
    issues: List[str]


@router.post("/process-shipment", response_model=ShipmentResponse)
async def process_shipment(shipment: ShipmentRequest):
    """
    Stub workflow: returns fixed response for frontend testing.
    """
    return ShipmentResponse(
        shipment_id=shipment.shipment_id,
        usmca_status="generated",
        hts_code="010121",
        documents_zip=f"http://localhost:8000/api/documents/{shipment.shipment_id}.zip",
        risk_score=0,
        issues=[],
    )
