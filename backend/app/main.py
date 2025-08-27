from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import hts, usmca, workflow, health

app = FastAPI(title="CrossBorder EZ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hts.router)
app.include_router(usmca.router)
app.include_router(workflow.router)
app.include_router(usmca.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(health.router)
