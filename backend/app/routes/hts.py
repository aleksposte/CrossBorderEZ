from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_client.py import suggest_hts_code

router = APIRouter()


class HTSRequest(BaseModel):
    description: str


@router.post("/suggest")
async def suggest_hts(request: HTSRequest):
    """
    Use OpenAI to suggest HTS/HS codes based on product description.
    """
    code = suggest_hts_code(request.description)
    return {
        "message": "HTS/HS code suggested",
        "code": code,
        "description": request.description,
    }
