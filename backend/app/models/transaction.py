from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base
from datetime import date

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    type = Column(String, nullable=False)  # 'income' or 'expense'
    amount = Column(Float, nullable=False)
    note = Column(String, nullable=True)
    date = Column(Date, default=date.today, nullable=False)