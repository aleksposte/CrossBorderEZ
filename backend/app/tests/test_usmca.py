from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_usmca():
    response = client.post("/api/usmca/generate", json={"field": "value"})
    assert response.status_code == 200
    assert "USMCA Certificate generated" in response.json()["message"]


def test_validate_usmca():
    response = client.post("/api/usmca/validate", json={"field": "value"})
    assert response.status_code == 200
    assert response.json()["valid"] == True
