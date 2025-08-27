import pytest
from app.services.hts_service import suggest_hts_code
from app.schemas.hts import HTSSuggestionRequest


@pytest.mark.parametrize(
    "description,expected",
    [
        ("men's cotton t-shirt", "010121"),
        ("laptop computer", "847130"),
        ("unknown item", "999999"),
    ],
)
def test_suggest_hts_code(description, expected):
    req = HTSSuggestionRequest(description=description, country_of_origin="USA")
    code = suggest_hts_code(req)
    assert code == expected
