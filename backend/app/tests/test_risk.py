from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_risk_score():
    response = client.post("/api/risk/score", json={"shipment": "data"})
    assert response.status_code == 200
    assert "Risk score calculated" in response.json()["message"]
