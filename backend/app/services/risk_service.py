def assess_risk(description: str) -> str:
    """
    Assess risk level for a given product.
    """
    high_risk_items = {"Wireless Mouse", "Laptop Computer"}
    return "High" if description in high_risk_items else "Low"
