# backend/app/services/hts_service.py
# from app.schemas.usmca import HTSSuggestionRequest, HTSSuggestionResponse
# from app.schemas.usmca import HTSSuggestionRequest, HTSSuggestionResponse
from app.schemas.hts import HTSSuggestionRequest, HTSSuggestionResponse

HTS_DB = {
    "men's cotton t-shirt": "010121",
    "women's leather jacket": "420330",
    "laptop computer": "8471.30",
    "wireless mouse": "847160",
    "office chair": "940171",
}


def suggest_hts_code(request: HTSSuggestionRequest) -> HTSSuggestionResponse:
    desc_lower = request.description.lower()
    code = HTS_DB.get(desc_lower, "999999")
    return HTSSuggestionResponse(code=code, description=request.description)
