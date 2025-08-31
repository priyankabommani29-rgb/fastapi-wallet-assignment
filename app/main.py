from fastapi import FastAPI
from . import models
from .database import engine, Base
from .routes import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wallet API - FastAPI Assignment")
app.include_router(api_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}