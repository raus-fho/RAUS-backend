from sqlalchemy import Column, Integer, Boolean, types, sql
from .db import Base

class Status(Base):
    """
    Query the actual status of the hardware
    returns humidity levels and  actuator status
    """
    __tablename__ = "status"
    
    humidity = Column(Integer, primary_key = True)
    actuator_status = Column(Boolean)


class History(Base):
    """
    Query the table history, returning
    all registers 
    """
    __tablename__ = "history"
    
    id = Column(Integer, primary_key = True)
    humidity = Column(Integer)
    actuator_status = Column(Boolean)
    registered_at = Column(types.DATETIME, default=sql.func.now())