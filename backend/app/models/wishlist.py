from sqlalchemy import Column, Integer, String
from app.database import Base

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    detailed_description = Column(String, nullable=True)
    target_amount = Column(Integer)
