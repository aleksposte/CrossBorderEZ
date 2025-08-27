from pydantic import BaseModel
from typing import List


class ShipmentRequest(BaseModel):
    shipment_id: str
    exporter_name: str
    importer_name: str
    producer_name: str
    description: str
    hs_code: str
    country_of_origin: str


class ShipmentResponse(BaseModel):
    shipment_id: str
    status: str
    details: dict
