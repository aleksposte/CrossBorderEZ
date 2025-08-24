from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class DocumentRequest(BaseModel):
    shipment_id: str

class DocumentResponse(BaseModel):
    zip_url: str
    message: str

@router.post("/generate", response_model=DocumentResponse)
async def generate_documents(request: DocumentRequest):
    """
    Stub endpoint: generates shipping documents and returns ZIP URL.
    """
    # Пока возвращаем фиктивную ссылку
    return {
        "zip_url": f"https://example.com/{request.shipment_id}.zip",
        "message": "Documents generated (stub)"
    }
