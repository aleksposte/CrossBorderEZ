from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, risk, workflow, hts, usmca, bulk
from api import process_csv

app = FastAPI(title="Trade Compliance API")
# router = APIRouter()
# CORS для фронта
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Роуты
app.include_router(health.router, prefix="/api/health", tags=["Health"])
app.include_router(risk.router, prefix="/api/risk", tags=["Risk"])
app.include_router(workflow.router, prefix="/api/workflow", tags=["Workflow"])
# app.include_router(hts.router, prefix="/api/hts", tags=["HTS"])
app.include_router(hts.router)
app.include_router(usmca.router, prefix="/api/usmca", tags=["USMCA"])
app.include_router(bulk.router)
app.include_router(process_csv.router, prefix="/api", tags=["process"])


@app.get("/")
def root():
    return {"message": "Backend is running"}
