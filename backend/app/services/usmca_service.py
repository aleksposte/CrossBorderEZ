from app.schemas.usmca import USMCACheckRequest, USMCACheckResponse


def check_usmca_compliance(request: USMCACheckRequest) -> USMCACheckResponse:
    """
    Simple compliance logic:
    - If country_of_origin is USA or Canada, compliant
    - Otherwise, non-compliant
    """
    compliant_countries = ["USA", "Canada", "Mexico"]
    if request.country_of_origin in compliant_countries:
        status = "compliant"
        explanation = f"Shipment from {request.country_of_origin} is USMCA compliant."
    else:
        status = "non-compliant"
        explanation = (
            f"Shipment from {request.country_of_origin} is NOT USMCA compliant."
        )

    return USMCACheckResponse(status=status, explanation=explanation)
