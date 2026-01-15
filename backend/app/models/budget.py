from sqlalchemy import Column, Integer, String
from app.database import Base   

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    amount_monthly = Column(Integer)  