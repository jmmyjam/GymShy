from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Equipment(Base):

    __tablename__ = "equipment"

    id = Column(Integer, primary_key = True, index = True)
    type = Column(String)
    name = Column(String)
    description = Column(String)

class UserEquipment(Base):

    __tablename__ = "user_equipment"

    id = Column(Integer, primary_key = True, index = True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"), unique = True)