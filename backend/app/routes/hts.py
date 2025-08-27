from fastapi import APIRouter
from app.schemas.hts import HTSSuggestionRequest, HTSSuggestionResponse
from app.services.hts_service import suggest_hts_code

router = APIRouter()


@router.post("/suggest", response_model=HTSSuggestionResponse)
def hts_suggestion(request: HTSSuggestionRequest):
    code = suggest_hts_code(request)
    return HTSSuggestionResponse(code=code, description=request.description)
