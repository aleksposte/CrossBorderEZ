import pytest
from app.services.documents_service import process_document


@pytest.mark.parametrize(
    "document_name, expected_status",
    [
        ("Invoice", "Processed"),
        ("Bill of Lading", "Processed"),
        ("Packing List", "Pending"),
        ("Unknown Doc", "Pending"),
    ],
)
def test_process_document(document_name, expected_status):
    status = process_document(document_name)
    assert status == expected_status
