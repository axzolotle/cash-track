from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BudgetCreate(BaseModel):
    category_id: int
    amount_monthly: int

class BudgetUpdate(BaseModel):
    category_id: Optional[int]
    amount_monthly: Optional[int]

class BudgetResponse(BaseModel):
    id: int
    category_id: int
    amount_monthly: int

    class Config:
        orm_mode = True

