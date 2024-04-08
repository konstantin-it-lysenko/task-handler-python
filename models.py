from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from database import Base
from datetime import datetime


class Tasks(Base):
    __tablename__ = 'task'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date)
    name = Column(String, index=True)
    priority = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=True)


class TimeBlock(Base):
    __tablename__ = 'time_block'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date)
    name = Column(String)
    color = Column(String, nullable=True)
    duration = Column(Integer)
    order = Column(Integer, default=1)
