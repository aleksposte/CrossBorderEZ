from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_suggest_hts():
    response = client.post(
        "/api/hts/suggest", json={"description": "men's cotton T-shirt"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert data["code"].isdigit()  # должно быть число
