# backend/app/services/hts_service.py

HTS_DATABASE = {
    "Men's Cotton T-Shirt": "010121",
    "Women's Leather Jacket": "420330",
    "Laptop Computer": "847130",
    "Wireless Mouse": "847160",
    "Office Chair": "940171",
}


def suggest_hts_code(description: str) -> dict:
    """
    Функция возвращает HTS код и описание для данного товара.
    Возвращает словарь вида: {"code": "...", "description": "..."}
    """
    code = HTS_DATABASE.get(description, "999999")
    return {"code": code, "description": description}
