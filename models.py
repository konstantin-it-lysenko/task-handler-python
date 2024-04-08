from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from database import Base
from datetime import datetime


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date)
    name = Column(String, index=True)
    priority = Column(String)
    is_completed = Column(Boolean, default=False)



