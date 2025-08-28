from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hts_suggestion():
    response = client.post(
        "/api/hts/suggest",
        json={"description": "laptop computer", "country_of_origin": "China"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "8471.30"
