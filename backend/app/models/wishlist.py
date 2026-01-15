from sqlalchemy import Column, Integer, String
from app.database import Base

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    target_amount = Column(Integer)
