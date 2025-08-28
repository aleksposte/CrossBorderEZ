from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/hts", tags=["HTS"])


class HTSRequest(BaseModel):
    description: str


@router.post("/suggest")
def suggest_hts(data: HTSRequest):
    # Здесь вместо реальной логики пока фейковые предложения
    suggestions = [f"HTS-{i}-{data.description}" for i in range(1, 4)]
    return {"suggestions": suggestions}
