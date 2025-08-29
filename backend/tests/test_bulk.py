import io
import zipfile
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_bulk_upload_csv_returns_zip():
    csv_content = (
        "shipment_id,exporter_name,importer_name,producer_name,description,hs_code,"
        "country_of_origin,invoice_number,value,currency,shipment_date,certifier_name,certifier_signature,certifier_date\n"
        "SHP001,Exporter Inc,Importer LLC,Producer Co,Men's Cotton T-Shirt,,USA,INV-1001,1200.50,USD,2025-08-25,John Doe,JD,2025-08-25\n"
        "SHP002,Exporter Inc,Importer LLC,Producer Co,Laptop Computer,8471.30,Canada,INV-1002,899.99,USD,2025-08-26,Jane Roe,JR,2025-08-26\n"
    ).encode("utf-8")

    files = {"file": ("shipments.csv", io.BytesIO(csv_content), "text/csv")}
    resp = client.post("/api/bulk/upload-csv", files=files)
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "application/zip"

    zdata = io.BytesIO(resp.content)
    with zipfile.ZipFile(zdata, "r") as zf:
        names = zf.namelist()
        # Ожидаем 4 pdf (2 на отправку)
        assert len(names) == 4
        assert any(n.endswith("_USMCA.pdf") for n in names)
        assert any(n.endswith("_Invoice.pdf") for n in names)
