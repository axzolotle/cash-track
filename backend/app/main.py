from fastapi import FastAPI
from app.database import Base, engine

from app.models import (
    transaction,
    wallet,
    category,
    budget,
    wishlist,
    saving
)

app = FastAPI(title="Money Tracker API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Backend is running"}
