import os
import pytest
from app.services.usmca_service import generate_usmca_certificate, STUB_DIR


def test_generate_usmca_certificate_success():
    shipment = {
        "shipment_id": "TEST001",
        "exporter_name": "Exporter Inc",
        "importer_name": "Importer LLC",
        "producer_name": "Producer Co",
        "hs_code": "010121",
        "description": "Men's Cotton T-Shirt",
        "country_of_origin": "USA",
        "certifier_name": "John Doe",
        "certifier_signature": "John Doe",
        "certifier_date": "2025-08-25",
    }

    path = generate_usmca_certificate(shipment)
    assert os.path.exists(path)
    # Cleanup
    os.remove(path)


def test_generate_usmca_certificate_missing_fields():
    shipment = {
        "shipment_id": "TEST002",
        "exporter_name": "",
        "importer_name": "Importer LLC",
        # missing other fields
    }
    with pytest.raises(ValueError):
        generate_usmca_certificate(shipment)
