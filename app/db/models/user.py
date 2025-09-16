from sqlalchemy import Column, Integer, String, Boolean

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True)
    balance = Column(Integer, default=0)
    is_subscription_active = Column(Boolean, default=False)
