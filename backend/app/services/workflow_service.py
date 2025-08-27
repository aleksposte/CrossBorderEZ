from app.schemas.workflow import ShipmentRequest, ShipmentResponse


def process_shipment_service(request: ShipmentRequest) -> ShipmentResponse:
    details = {
        "hts_code": request.hs_code,
        "hts_description": request.description,
        "message": f"Shipment {request.shipment_id} processed successfully",
    }
    return ShipmentResponse(
        shipment_id=request.shipment_id, status="processed", details=details
    )
