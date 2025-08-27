from app.schemas.usmca import USMCACheckRequest

USMCA_RULES = {
    "8708.10": ["Canada", "USA", "Mexico"],  # car parts
    "8517.12": ["China", "Vietnam"],  # phones
}


def check_usmca_compliance(request: USMCACheckRequest):
    allowed_countries = USMCA_RULES.get(request.hs_code, [])
    compliant = request.country_of_origin in allowed_countries
    message = "Shipment is compliant." if compliant else "Shipment is non-compliant."
    return compliant, message
