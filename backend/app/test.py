from fastapi import FastAPI, Depends
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Session
from app.database import Base, SessionLocal
from datetime import date


test = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## models

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    note = Column(String, nullable=True)
    date = Column(Date, default=date.today, nullable=False)

## SCHEMAS
class TransactionCreate(BaseModel):
    amount: int = Field(gt=0)
    note: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: int
    note: Optional[str] = None 
    date: datetime

    class Config:
        form_attributes = True

## CRUD
def create_transaction(db, data):
    transaction = Transaction(
        amount=data.amount,
        note=data.note,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transactions(db: Session):
    return db.query(Transaction).all()


## Routees
@test.get("/")
def read_root():
    return {"message": "Test endpoint is working. sukses!"}

@test.post("/transactions")
def create(
    data: TransactionCreate, 
    db: Session = Depends(get_db)
):
    return create_transaction(db, data)

@test.get("/", response_model=list[TransactionResponse])
def list_all( 
    db: Session = Depends(get_db)
):
    return get_transactions(db)
