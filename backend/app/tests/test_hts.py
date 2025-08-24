from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_suggest_hts():
    response = client.post("/api/hts/suggest", json={"description": "widget"})
    assert response.status_code == 200
    assert "HTS/HS code suggested" in response.json()["message"]
