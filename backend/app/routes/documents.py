from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import zipfile

router = APIRouter()

# Абсолютный путь к папке stub_docs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUB_DIR = os.path.join(BASE_DIR, "stub_docs")

# Создаём папку, если её нет
os.makedirs(STUB_DIR, exist_ok=True)


@router.get("/{shipment_id}.zip")
async def get_stub_document(shipment_id: str):
    """
    Returns a stub ZIP file for the given shipment_id.
    Automatically creates a ZIP with a simple TXT inside if it doesn't exist.
    """
    zip_path = os.path.join(STUB_DIR, f"{shipment_id}.zip")
    txt_path = os.path.join(STUB_DIR, f"{shipment_id}.txt")

    # Создаём TXT если нет
    if not os.path.exists(txt_path):
        with open(txt_path, "w") as f:
            f.write(f"This is a stub document for shipment {shipment_id}")

    # Создаём ZIP если нет
    if not os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "w") as zipf:
            zipf.write(txt_path, arcname=f"{shipment_id}.txt")

    # Проверяем ZIP перед возвратом
    if not os.path.exists(zip_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=zip_path, filename=f"{shipment_id}.zip", media_type="application/zip"
    )
