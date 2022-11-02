from sqlalchemy import Column, Integer, Boolean
from .db import Base

class Status(Base):
    """
    Query the actual status of the hardware
    returns humidity levels and  actuator status
    """
    __tablename__ = "status"
    
    humidity = Column(Integer, primary_key = True)
    actuator_status = Column(Boolean)