from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_client import suggest_hts_code

router = APIRouter()


class HTSRequest(BaseModel):
    description: str


class HTSResponse(BaseModel):
    code: str
    description: str
    message: str


@router.post("/suggest", response_model=HTSResponse)
async def suggest_hts(request: HTSRequest):
    """
    Suggest HTS/HS code using OpenAI.
    """
    code = suggest_hts_code(request.description)
    return {
        "code": code,
        "description": request.description,
        "message": "HTS/HS code suggested by AI",
    }
