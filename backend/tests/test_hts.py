import pytest
from app.services.hts_service import suggest_hts_code


@pytest.mark.parametrize(
    "description,expected_code",
    [
        ("Men's Cotton T-Shirt", "010121"),
        ("Women's Leather Jacket", "420330"),
        ("Laptop Computer", "847130"),
        ("Wireless Mouse", "847160"),
        ("Office Chair", "940171"),
        ("Unknown Item", "999999"),
    ],
)
def test_suggest_hts_code(description, expected_code):
    result = suggest_hts_code(description)
    assert isinstance(result, dict)
    assert "code" in result
    assert "description" in result
    assert result["code"] == expected_code
    assert result["description"] == description
