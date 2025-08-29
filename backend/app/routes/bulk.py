from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, PlainTextResponse
from typing import List, Dict, Any
import csv
import io
import tempfile
import os
import datetime
import zipfile

from app.services.hts_service import suggest_hts_code
from app.services.pdf_service import generate_usmca_pdf, generate_invoice_pdf

router = APIRouter(prefix="/api/bulk", tags=["bulk"])

CSV_TEMPLATE_HEADERS = [
    "shipment_id",
    "exporter_name",
    "importer_name",
    "producer_name",
    "description",
    "hs_code",
    "country_of_origin",
    "invoice_number",
    "value",
    "currency",
    "shipment_date",  # YYYY-MM-DD
    "certifier_name",  # опционально; если пусто — exporter_name
    "certifier_signature",  # опционально; если пусто — initials(exporter_name)
    "certifier_date",  # опционально; если пусто — today
]


@router.get("/template", response_class=PlainTextResponse)
def download_template():
    """Возвращает CSV-шаблон с заголовками."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(CSV_TEMPLATE_HEADERS)
    # Пример строки (можно удалить при желании)
    writer.writerow(
        [
            "SHP001",
            "Exporter Inc",
            "Importer LLC",
            "Producer Co",
            "Men's Cotton T-Shirt",
            "",
            "USA",
            "INV-1001",
            "1200.50",
            "USD",
            "2025-08-25",
            "John Doe",
            "JD",
            "2025-08-25",
        ]
    )
    return output.getvalue()


def _str(val: Any) -> str:
    return "" if val is None else str(val).strip()


def _initials(fullname: str) -> str:
    parts = [p for p in fullname.split() if p]
    return "".join(p[0].upper() for p in parts[:2]) or "X"


def _coalesce(a: str, b: str) -> str:
    return a if a else b


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    """Принимает CSV, обрабатывает каждую отправку, генерит 2 PDF/запись и отдаёт ZIP."""
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a .csv file")

    data = await file.read()
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = data.decode("utf-8")

    reader = csv.DictReader(io.StringIO(text))
    missing = [h for h in CSV_TEMPLATE_HEADERS if h not in reader.fieldnames]
    if missing:
        raise HTTPException(status_code=400, detail=f"CSV missing columns: {missing}")

    # Временная папка для сборки PDF и ZIP
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_paths: List[str] = []
        count_rows = 0

        for row in reader:
            count_rows += 1
            shipment: Dict[str, Any] = {
                k: _str(row.get(k)) for k in CSV_TEMPLATE_HEADERS
            }

            # Fallbacks
            if not shipment["hs_code"]:
                # Авто-HTS (используем существующий сервис)
                hts = suggest_hts_code(
                    description=shipment["description"],
                    country_of_origin=shipment["country_of_origin"],
                )
                shipment["hs_code"] = hts.code

            if not shipment["certifier_name"]:
                shipment["certifier_name"] = _coalesce(
                    shipment["certifier_name"], shipment["exporter_name"]
                )
            if not shipment["certifier_signature"]:
                shipment["certifier_signature"] = _initials(shipment["certifier_name"])
            if not shipment["certifier_date"]:
                shipment["certifier_date"] = datetime.date.today().isoformat()

            # Генерация PDF: USMCA и Счет (invoice)
            base = f"{shipment['shipment_id'] or f'row{count_rows:03d}'}"
            usmca_pdf_path = os.path.join(tmpdir, f"{base}_USMCA.pdf")
            invoice_pdf_path = os.path.join(tmpdir, f"{base}_Invoice.pdf")

            generate_usmca_pdf(shipment, usmca_pdf_path)
            generate_invoice_pdf(shipment, invoice_pdf_path)

            pdf_paths.extend([usmca_pdf_path, invoice_pdf_path])

        # Упаковка в ZIP (потоково)
        mem_zip = io.BytesIO()
        with zipfile.ZipFile(mem_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in pdf_paths:
                zf.write(p, arcname=os.path.basename(p))
        mem_zip.seek(0)

        filename = f"documents_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
        return StreamingResponse(mem_zip, headers=headers, media_type="application/zip")
