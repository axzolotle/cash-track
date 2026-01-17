from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    type: str  # 'income' or 'expense'

class CategoryUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]  # 'income' or 'expense'

class CategoryResponse(BaseModel):
    id: int
    name: str
    type: str  # 'income' or 'expense'

    class Config:
        orm_mode = True