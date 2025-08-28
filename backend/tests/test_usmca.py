from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_usmca_compliant():
    response = client.post(
        "/api/usmca",
        json={
            "description": "car part",
            "hs_code": "8708.10",
            "country_of_origin": "Canada",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Compliant"


def test_usmca_non_compliant():
    response = client.post(
        "/api/usmca",
        json={
            "description": "phone",
            "hs_code": "8517.12",
            "country_of_origin": "China",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Non-Compliant"
