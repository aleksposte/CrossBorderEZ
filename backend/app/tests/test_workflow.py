from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_workflow_stub():
    payload = {
        "shipment_id": "SHIP123",
        "description": "Men's cotton T-shirt",
        "usmca_complete": False,
    }
    response = client.post("/api/workflow/process-shipment", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["hts_code"] == "010121"
    assert data["documents_zip"].endswith(".zip")
    assert data["risk_score"] > 0
