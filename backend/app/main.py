from fastapi import FastAPI
from app.routes import health, usmca, hts, documents, risk

app = FastAPI(title="CrossBorder EZ API")

# подключаем роутеры
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(hts.router, prefix="/api/hts", tags=["hts"])
app.include_router(usmca.router, prefix="/api/usmca", tags=["usmca"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(risk.router, prefix="/api/risk", tags=["risk"])
