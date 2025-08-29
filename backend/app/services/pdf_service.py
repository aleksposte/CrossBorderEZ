from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from typing import Dict, Any


def _draw_label_value(
    c: canvas.Canvas,
    x: int,
    y: int,
    label: str,
    value: str,
    label_w=60 * mm,
    max_w=120 * mm,
):
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x, y, f"{label}:")
    c.setFont("Helvetica", 9)
    text = value or "-"
    c.drawString(x + label_w, y, text[:200])  # простая обрезка


def generate_usmca_pdf(shipment: Dict[str, Any], out_path: str) -> None:
    """
    Минимальный PDF с 9 обязательными элементами USMCA:
    1) Exporter
    2) Producer
    3) Importer
    4) Description
    5) HS Code
    6) Country of Origin
    7) Certifier Name
    8) Certifier Signature
    9) Date
    """
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    x = 20 * mm
    y = height - 30 * mm

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "USMCA Certificate of Origin (Simplified)")
    y -= 15 * mm

    fields = [
        ("Exporter", shipment.get("exporter_name", "")),
        ("Producer", shipment.get("producer_name", "")),
        ("Importer", shipment.get("importer_name", "")),
        ("Description", shipment.get("description", "")),
        ("HS Code", shipment.get("hs_code", "")),
        ("Country of Origin", shipment.get("country_of_origin", "")),
        ("Certifier Name", shipment.get("certifier_name", "")),
        ("Certifier Signature", shipment.get("certifier_signature", "")),
        ("Date", shipment.get("certifier_date", "")),
    ]

    for label, value in fields:
        _draw_label_value(c, x, y, label, str(value))
        y -= 10 * mm

    c.showPage()
    c.save()


def generate_invoice_pdf(shipment: Dict[str, Any], out_path: str) -> None:
    """
    Простой Commercial Invoice PDF.
    """
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    x = 20 * mm
    y = height - 30 * mm

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Commercial Invoice (Simplified)")
    y -= 15 * mm

    fields = [
        ("Shipment ID", shipment.get("shipment_id", "")),
        ("Exporter", shipment.get("exporter_name", "")),
        ("Importer", shipment.get("importer_name", "")),
        ("Description", shipment.get("description", "")),
        ("HS Code", shipment.get("hs_code", "")),
        ("Country of Origin", shipment.get("country_of_origin", "")),
        ("Invoice #", shipment.get("invoice_number", "")),
        ("Value", shipment.get("value", "")),
        ("Currency", shipment.get("currency", "")),
        ("Shipment Date", shipment.get("shipment_date", "")),
    ]

    for label, value in fields:
        _draw_label_value(c, x, y, label, str(value))
        y -= 10 * mm

    c.showPage()
    c.save()
