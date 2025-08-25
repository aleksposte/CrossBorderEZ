# backend/app/services/usmca_service.py
from pathlib import Path
import json

STUB_DIR = Path("stubs/usmca")
STUB_DIR.mkdir(parents=True, exist_ok=True)


def generate_usmca_certificate(data: dict) -> str:
    """
    Generate a USMCA certificate stub and save to file.
    """
    required_fields = [
        "exporter_name",
        "importer_name",
        "producer_name",
        "hs_code",
        "description",
        "country_of_origin",
        "certifier_name",
        "certifier_signature",
        "certifier_date",
    ]
    for f in required_fields:
        if f not in data:
            raise ValueError(f"Missing field: {f}")

    file_path = STUB_DIR / f"{data['hs_code']}.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


def check_usmca_compliance(description: str) -> str:
    """
    Stub compliance check.
    Returns 'Compliant' or 'Non-Compliant'.
    """
    compliant_items = [
        "Men's Cotton T-Shirt",
        "Women's Leather Jacket",
        "Laptop Computer",
    ]
    return "Compliant" if description in compliant_items else "Non-Compliant"
