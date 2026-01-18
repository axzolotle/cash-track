from fastapi import FastAPI
from app.database import Base, engine

from app.models import (
    transaction,
    asset,
    wallet,
    category,
    budget,
    wishlist,
)

from app.routers import transaction
from app.routers import category
from app.routers import testing

app = FastAPI(title="Money Tracker API")

app.include_router(transaction.router)
app.include_router(category.router)
app.include_router(testing.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Backend is running"}


