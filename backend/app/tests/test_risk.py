from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_risk_score_stub():
    payload = {"shipment_id": "SHIP123", "hts_code": "010121", "usmca_complete": False}
    response = client.post("/api/risk/score", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk_score" in data
    assert "issues" in data
    assert data["risk_score"] == 70
    assert len(data["issues"]) == 2
