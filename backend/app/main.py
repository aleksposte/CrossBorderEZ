from fastapi import FastAPI
from app.routes import hts, usmca, health
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CrossBorder EZ API")

# Include routes with /api prefix
app.include_router(health.router, prefix="/api")
app.include_router(hts.router, prefix="/api/hts")
app.include_router(usmca.router, prefix="/api/usmca", tags=["USMCA"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # фронтенд
    allow_credentials=True,
    allow_methods=["*"],  # разрешить POST, GET, OPTIONS и т.д.
    allow_headers=["*"],
)
