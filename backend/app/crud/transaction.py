from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate


def create_transaction(db: Session, data: TransactionCreate):
    transaction = Transaction(
        amount=data.amount,
        category_id=data.category_id,
        wallet_id=data.wallet_id, 
        note=data.note,
        type=data.type
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def get_transactions(db: Session):
    return db.query(Transaction).all()

def update_transaction(db: Session, transaction_id: int, data: TransactionUpdate):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    for field, value in data.dict(exclude_unset=True).items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return transaction
