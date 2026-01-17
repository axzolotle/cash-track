from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WalletCreate(BaseModel):
    name: str
    type: str  # e.g., 'cash', 'bank', 'credit card'
    balance: Optional[float] = 0.0

class WalletUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]  # e.g., 'cash', 'bank', 'credit card'
    balance: Optional[float]

class WalletResponse(BaseModel):
    id: int
    name: str
    type: str
    balance: float

    class Config:
        orm_mode = True
