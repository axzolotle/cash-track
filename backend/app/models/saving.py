from sqlalchemy import Column, Integer, String
from app.database import Base 

class Saving(Base):
    __tablename__ = "savings"

    id = Column(Integer, primary_key=True, index=True)
    wishlist_id = Column(Integer, nullable=False)
    wallet_id = Column(Integer, nullable=False)
    target_amount = Column(Integer, nullable=False)