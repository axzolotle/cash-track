from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    wallet_id: int
    category_id: int
    type: str  # 'income' or 'expense'
    amount: int = Field(gt=0)
    note: Optional[str] = None

class TransactionUpdate(BaseModel):
    amount: Optional[int] = Field(default=None, gt=0) 
    category_id: Optional[int] = None
    type: Optional[str] = None
    wallet_id: Optional[int] = None
    note: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    wallet_id: int
    category_id: int
    type: str
    amount: int
    note: Optional[str] = None 
    date: datetime

    class Config:
        form_attributes = True
