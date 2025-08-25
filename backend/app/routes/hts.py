from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HTSRequest(BaseModel):
    description: str


class HTSResponse(BaseModel):
    hts_code: str


@router.post("/suggest", response_model=HTSResponse)
async def suggest_hts(request: HTSRequest):
    """
    Stub endpoint for HTS code suggestion
    """
    return {"hts_code": "010121"}


# 🔹 функция для workflow
def suggest_hts_stub(description: str) -> str:
    return "010121"
