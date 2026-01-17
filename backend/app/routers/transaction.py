from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.transaction import TransactionCreate, TransactionResponse, TransactionUpdate
from app.crud.transaction import (
    create_transaction, 
    get_transactions, 
    delete_transaction,
    update_transaction
)
from app.models.transaction import Transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/", response_model=TransactionResponse, status_code=201)
def create(
    data: TransactionCreate, 
    db: Session = Depends(get_db)
):
    return create_transaction(db, data)

@router.get("/", response_model=list[TransactionResponse])
def list_all(
    db: Session = Depends(get_db)
):
    return get_transactions(db)

@router.get("/{transaction_id}", response_model=TransactionResponse)
def retrieve(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction  

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update(
    transaction_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    updated = update_transaction(db, transaction_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated

@router.delete("/{transaction_id}", response_model=TransactionResponse)
def delete(transaction_id: int, db: Session = Depends(get_db)):
    deleted = delete_transaction(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return deleted