from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
import pandas as pd
import io, zipfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

router = APIRouter()


def make_usmca_form(row):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "USMCA Certificate of Origin")
    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Product: {row.get('product', 'N/A')}")
    c.drawString(100, 750, f"HTS Code: {row.get('hts', 'N/A')}")
    c.drawString(100, 730, f"Country: {row.get('country', 'N/A')}")
    c.drawString(100, 710, "Generated automatically")

    c.showPage()
    c.save()
    buf.seek(0)
    return buf


def make_hts_form(row):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "HTS Classification Form")
    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Product: {row.get('product', 'N/A')}")
    c.drawString(100, 750, f"Suggested HTS: {row.get('hts', 'N/A')}")
    c.drawString(100, 730, "Classification notes:")
    c.drawString(120, 710, "→ Automated suggestion based on input data")

    c.showPage()
    c.save()
    buf.seek(0)
    return buf


def make_9element_form(row):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "USMCA 9-Element Certification")
    c.setFont("Helvetica", 12)

    # 9 обязательных элементов
    elements = [
        ("Exporter", row.get("exporter", "N/A")),
        ("Producer", row.get("producer", "N/A")),
        ("Importer", row.get("importer", "N/A")),
        ("Description", row.get("product", "N/A")),
        ("HS Code", row.get("hts", "N/A")),
        ("Origin Criteria", row.get("origin", "N/A")),
        ("Period", row.get("period", "N/A")),
        ("Authorized Signature", row.get("signature", "N/A")),
        ("Certifier", row.get("certifier", "N/A")),
    ]

    y = 770
    for name, value in elements:
        c.drawString(100, y, f"{name}: {value}")
        y -= 20

    c.showPage()
    c.save()
    buf.seek(0)
    return buf


@router.post("/process_csv")
async def process_csv(file: UploadFile = File(...)):
    # читаем CSV
    df = pd.read_csv(file.file)

    # создаем ZIP в памяти
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        for idx, row in df.iterrows():
            # USMCA
            pdf1 = make_usmca_form(row)
            zipf.writestr(f"row{idx+1}_usmca.pdf", pdf1.read())

            # HTS
            pdf2 = make_hts_form(row)
            zipf.writestr(f"row{idx+1}_hts.pdf", pdf2.read())

            # 9 Elements
            pdf3 = make_9element_form(row)
            zipf.writestr(f"row{idx+1}_9element.pdf", pdf3.read())

    zip_buffer.seek(0)
    return StreamingResponse(
        zip_buffer,
        media_type="application/x-zip-compressed",
        headers={"Content-Disposition": "attachment; filename=usmca_package.zip"},
    )
