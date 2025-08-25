import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_process_shipment_endpoint():
    payload = {
        "exporter_name": "ACME Corp",
        "importer_name": "Maple Inc",
        "producer_name": "ACME Factory",
        "description": "Men's Cotton T-Shirt",
        "hs_code": "010121",
        "country_of_origin": "USA",
        "certifier_name": "John Doe",
        "certifier_signature": "JD",
        "certifier_date": "2025-08-25",
        # Если модель ожидает дополнительные поля, укажем их:
        "documents": [],
        "shipment_id": "SHP001",
    }

    response = client.post("/api/workflow/process-shipment", json=payload)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем базовую структуру ответа
    json_data = response.json()
    assert "shipment_id" in json_data
    assert "status" in json_data
    assert json_data["status"] == "processed"
    assert "hts_code" in json_data
    assert "hts_description" in json_data
    assert "message" in json_data
