from fastapi import APIRouter, HTTPException
from app.schemas import ShipmentRequest, ShipmentResponse
from app.services.hts_service import suggest_hts_code

router = APIRouter()


@router.post("/process-shipment", response_model=ShipmentResponse)
async def process_shipment(shipment: ShipmentRequest):
    """
    Обрабатывает отправку, получает HTS-код и возвращает результат.
    """
    try:
        # Получаем HTS-код и описание через сервис
        hts_result = suggest_hts_code(shipment.description)
        hts_code = hts_result["code"]
        hts_description = hts_result["description"]

        # Формируем успешный ответ
        return ShipmentResponse(
            shipment_id=shipment.shipment_id,
            status="processed",
            hts_code=hts_code,
            hts_description=hts_description,
            message=f"Shipment {shipment.shipment_id} processed successfully.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
