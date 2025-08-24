from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_documents():
    response = client.post("/api/documents/generate", json={"shipment_id": "SHIP123"})
    assert response.status_code == 200
    data = response.json()
    assert data["zip_url"].endswith(".zip")
    assert "Documents generated" in data["message"]
