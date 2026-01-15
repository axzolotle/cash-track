from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # e.g., 'cash', 'bank', 'credit card'
    balance = Column(Float, default=0.0, nullable=False)