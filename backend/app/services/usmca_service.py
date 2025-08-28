from app.models.usmca_models import USMCACheckRequest


def check_usmca_compliance(request: USMCACheckRequest):
    if request.hs_code.startswith("85") and request.country_of_origin.lower() in [
        "mexico",
        "canada",
        "usa",
    ]:
        return True, "Shipment is compliant."
    return False, "Shipment is not compliant."
