from fastapi import APIRouter
from pydantic import BaseModel

from app.schemas.hts import HTSSuggestionRequest, HTSSuggestionResponse
from app.services.hts_service import suggest_hts_code

router = APIRouter(prefix="/api/hts", tags=["HTS"])


class HTSSuggestionRequest(BaseModel):
    description: str
    country_of_origin: str


class HTSSuggestionResponse(BaseModel):
    code: str
    description: str


# Простейший словарь HTS кодов для примера
HTS_CODES = {
    "men's cotton t-shirt": "010121",
    "laptop computer": "847130",
    "wireless mouse": "847160",
    "office chair": "940171",
    "women's leather jacket": "420330",
}


@router.post("/suggest", response_model=HTSSuggestionResponse)
def hts_suggestion(request: HTSSuggestionRequest):
    desc_lower = request.description.lower()
    code = HTS_CODES.get(desc_lower, "999999")
    return HTSSuggestionResponse(code=code, description=request.description)
