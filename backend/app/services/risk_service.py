def assess_risk(item: str) -> str:
    if "battery" in item.lower():
        return "high"
    elif "phone" in item.lower():
        return "medium"
    return "low"
