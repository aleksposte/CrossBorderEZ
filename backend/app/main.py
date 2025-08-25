from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, usmca, hts, risk, documents, workflow

app = FastAPI(title="CrossBorder EZ API")

# подключаем роутеры
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(usmca.router, prefix="/api/usmca", tags=["usmca"])
app.include_router(hts.router, prefix="/api/hts", tags=["hts"])
app.include_router(risk.router, prefix="/api/risk", tags=["risk"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(workflow.router, prefix="/api/workflow", tags=["workflow"])

# ===== CORS =====
origins = [
    "http://localhost:5173",  # адрес фронтенда
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # разрешаем все методы
    allow_headers=["*"],  # разрешаем все заголовки
)
