from fastapi import APIRouter
from pydantic import BaseModel
from app.services.hts_service import suggest_hts_code

router = APIRouter()  # 🔹 обязательно! без этого include_router ломается


class HTSRequest(BaseModel):
    description: str


class HTSResponse(BaseModel):
    hts_code: str


@router.post("/suggest", response_model=HTSResponse)
async def suggest_hts(request: HTSRequest):
    """
    Suggest HTS code for a product description.
    """
    code = suggest_hts_code(request.description)
    return {"hts_code": code}
