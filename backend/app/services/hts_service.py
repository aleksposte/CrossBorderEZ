from app.schemas.hts import HTSSuggestionRequest

HTS_CODES = {
    "men's cotton t-shirt": "010121",
    "women's leather jacket": "420330",
    "laptop computer": "847130",
    "wireless mouse": "847160",
    "office chair": "940171",
}


def suggest_hts_code(request: HTSSuggestionRequest) -> str:
    key = request.description.lower()
    return HTS_CODES.get(key, "999999")
