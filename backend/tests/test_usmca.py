# backend/tests/test_usmca_service.py
import pytest
from app.services.usmca_service import (
    generate_usmca_certificate,
    check_usmca_compliance,
    STUB_DIR,
)
import os


def test_generate_usmca_certificate_success():
    data = {
        "exporter_name": "Exporter Co",
        "importer_name": "Importer Co",
        "producer_name": "Producer Co",
        "hs_code": "010121",
        "description": "Men's Cotton T-Shirt",
        "country_of_origin": "USA",
        "certifier_name": "John Doe",
        "certifier_signature": "John Doe",
        "certifier_date": "2025-08-25",
    }
    file_path = generate_usmca_certificate(data)
    assert os.path.exists(file_path)
    # clean up
    os.remove(file_path)


def test_generate_usmca_certificate_missing_fields():
    data = {"exporter_name": "Exporter Co"}
    with pytest.raises(ValueError):
        generate_usmca_certificate(data)


@pytest.mark.parametrize(
    "description,expected_status",
    [
        ("Men's Cotton T-Shirt", "Compliant"),
        ("Laptop Computer", "Compliant"),
        ("Wireless Mouse", "Non-Compliant"),
        ("Office Chair", "Non-Compliant"),
        ("Unknown Item", "Non-Compliant"),
    ],
)
def test_check_usmca_compliance(description, expected_status):
    assert check_usmca_compliance(description) == expected_status
