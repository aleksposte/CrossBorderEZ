from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_documents():
    response = client.post("/api/documents/generate", json={"shipment": "data"})
    assert response.status_code == 200
    assert "Documents generated" in response.json()["message"]
