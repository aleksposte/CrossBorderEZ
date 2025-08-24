from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Healthcheck endpoint.
    Returns service status.
    """
    return {"status": "ok"}
