from sqlalchemy import Column, Integer, DateTime, String, func, Enum
from sqlalchemy.orm import relationship, DeclarativeBase
from app.enums import Gender

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'

    user_id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_name = Column(String(50), nullable=False)
    user_phone = Column(String(15), nullable=False, unique=True)
    user_email = Column(String(100), nullable=False, unique=True, index=True)
    user_password = Column(String(100), nullable=False)
    user_gender = Column(Enum(Gender), nullable=False)
    user_location = Column(String(150), nullable=False)
    user_created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    user_updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
     