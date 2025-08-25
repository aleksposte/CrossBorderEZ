from pydantic import BaseModel
from typing import List, Optional


class ShipmentRequest(BaseModel):
    shipment_id: str
    description: str
    exporter_name: str
    importer_name: str
    producer_name: Optional[str] = None
    hs_code: str
    country_of_origin: str
    certifier_name: str
    certifier_signature: str
    certifier_date: str
    documents: Optional[List[str]] = []


class ShipmentResponse(BaseModel):
    shipment_id: str
    status: str
    hts_code: Optional[str] = None
    hts_description: Optional[str] = None
    message: Optional[str] = None
