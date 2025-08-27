from app.services.hts_service import suggest_hts_code
from app.schemas.hts import HTSSuggestionRequest


def test_suggest_hts_code():
    request = HTSSuggestionRequest(
        description="Men's Cotton T-Shirt", country_of_origin="USA"
    )
    result = suggest_hts_code(request)
    assert result.code == "010121"
