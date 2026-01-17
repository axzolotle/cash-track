from pydantic import BaseModel
from typing import Optional

class WishlistCreate(BaseModel):
    name: str
    detailed_description: Optional[str] = None
    target_amount: float

class WishlistUpdate(BaseModel):
    name: Optional[str]
    detailed_description: Optional[str]
    target_amount: Optional[float]  

class WishlistResponse(BaseModel):
    id: int
    name: str
    detailed_description: Optional[str] = None
    target_amount: float

    class Config:
        orm_mode = True