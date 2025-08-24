from fastapi import FastAPI

app = FastAPI(title="CrossBorder EZ Backend")


@app.get("/ping")
def ping():
    return {"status": "ok", "message": "pong 🏓"}
