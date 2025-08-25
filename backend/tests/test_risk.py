import pytest
from app.services.risk_service import assess_risk


@pytest.mark.parametrize(
    "description, expected_risk",
    [
        ("Men's Cotton T-Shirt", "Low"),
        ("Laptop Computer", "High"),
        ("Wireless Mouse", "High"),
        ("Office Chair", "Low"),
        ("Unknown Item", "Low"),
    ],
)
def test_assess_risk(description, expected_risk):
    risk = assess_risk(description)
    assert risk == expected_risk
