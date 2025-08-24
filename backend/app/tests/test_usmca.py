from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_usmca_certificate():
    response = client.post(
        "/api/usmca/certificate",
        json={
            "exporter_name": "ABC Exporters Ltd.",
            "importer_name": "XYZ Imports Inc.",
            "producer_name": "Global Producer Inc.",
            "hs_code": "9403.20",
            "description": "Wooden furniture",
            "country_of_origin": "Canada",
            "certifier_name": "John Doe",
            "certifier_signature": "JDoe",
            "certifier_date": "2025-08-24",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "generated"
    assert data["certificate_id"] == "USMCA-123456"
