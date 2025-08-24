from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_suggest_hts():
    response = client.post(
        "/api/hts/suggest", json={"description": "Men's cotton T-shirt"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"].isdigit()  # проверяем, что вернулся числовой код
    assert "HTS/HS code suggested" in data["message"]
