# from fastapi import FastAPI
# from app.routes import health


# def create_app() -> FastAPI:
#     app = FastAPI(title="CrossBorder EZ Backend")

#     # include routers
#     app.include_router(health.router)

#     return app


# app = create_app()


# app = FastAPI(title="CrossBorder EZ Backend")

from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="CrossBorder EZ API")

# подключаем router из health.py
app.include_router(health.router, prefix="/api", tags=["health"])
