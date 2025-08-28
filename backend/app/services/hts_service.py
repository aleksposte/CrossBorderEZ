def suggest_hts_code(keyword: str):
    mock_db = {
        "phone": ["8517.12", "8517.62"],
        "battery": ["8507.10", "8507.20"],
        "laptop": ["8471.30", "8471.41"],
    }
    return mock_db.get(keyword.lower(), ["0000.00"])
