from app.services.usmca_service import check_usmca_compliance
from app.schemas.usmca import USMCACheckRequest


def test_usmca_compliant():
    request = USMCACheckRequest(
        description="car part", hs_code="8708.10", country_of_origin="Canada"
    )
    response = check_usmca_compliance(request)
    assert response.status == "compliant"
    assert "Canada" in response.explanation


def test_usmca_non_compliant():
    request = USMCACheckRequest(
        description="phone", hs_code="8517.12", country_of_origin="China"
    )
    response = check_usmca_compliance(request)
    assert response.status == "non-compliant"
    assert "China" in response.explanation
