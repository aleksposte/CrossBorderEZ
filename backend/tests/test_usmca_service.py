import pytest
from app.services.usmca_service import check_usmca_compliance
from app.schemas.usmca import USMCACheckRequest


def test_usmca_compliant():
    req = USMCACheckRequest(
        description="car part", hs_code="8708.10", country_of_origin="Canada"
    )
    compliant, msg = check_usmca_compliance(req)
    assert compliant is True
    assert "compliant" in msg.lower()


def test_usmca_non_compliant():
    req = USMCACheckRequest(
        description="phone", hs_code="8517.12", country_of_origin="USA"
    )
    compliant, msg = check_usmca_compliance(req)
    assert compliant is False
    assert "non-compliant" in msg.lower()
