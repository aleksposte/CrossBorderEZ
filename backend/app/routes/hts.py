from fastapi import APIRouter

router = APIRouter()


@router.post("/suggest")
async def suggest_hts(data: dict):
    """
    Stub endpoint: suggest HTS/HS codes.
    """
    return {"message": "HTS/HS code suggested (stub)", "code": "010121", "data": data}
