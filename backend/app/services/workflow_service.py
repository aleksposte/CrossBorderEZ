# backend/app/services/workflow_service.py

from app.services.hts_service import suggest_hts_code
from app.services.risk_service import assess_risk
from app.services.documents_service import generate_documents


def process_workflow(product: str, expected_hts: str = None) -> dict:
    """
    End-to-end workflow: HTS suggestion, risk, and documents.
    """
    return {
        "product": product,
        "hts_code": suggest_hts_code(product, expected_hts),
        "risk": assess_risk(product),
        "documents": generate_documents(product),
    }
