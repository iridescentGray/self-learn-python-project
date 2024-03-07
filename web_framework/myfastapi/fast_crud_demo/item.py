from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class ItemCreateSchema(BaseModel):
    name: str
    description: str

class ItemUpdateSchema(BaseModel):
    name: str
    description: str