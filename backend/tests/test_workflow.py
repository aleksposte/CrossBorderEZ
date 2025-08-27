from app.services.workflow_service import process_shipment_service
from app.schemas.workflow import ShipmentRequest


def test_process_shipment():
    req = ShipmentRequest(
        shipment_id="SHP001",
        exporter_name="ACME Corp",
        importer_name="Maple Inc",
        producer_name="ACME Factory",
        description="Men's Cotton T-Shirt",
        hs_code="010121",
        country_of_origin="USA",
    )
    res = process_shipment_service(req)
    assert res.status == "processed"
    assert res.details["hts_code"] == "010121"
