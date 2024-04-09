from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(String, default=datetime.now())
    updated_at = Column(Date)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)

    # tasks = relationship('Tasks', back_populates='user')
    # time_blocks = relationship('TimeBlock', back_populates='user')

    def set_password(self, password):
        self.password = ph.hash(password)

    def check_password(self, password):
        try:
            return ph.verify(self.password, password)
        except VerifyMismatchError:
            return False


class Tasks(Base):
    __tablename__ = 'task'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.now(), nullable=True)
    updated_at = Column(Date, nullable=True)
    name = Column(String, index=True)
    priority = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=True)
    # user_id = Column(String, ForeignKey('user.id'))
    #
    # user = relationship('User', back_populates='task')


class TimeBlock(Base):
    __tablename__ = 'time_block'

    id = Column(String, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date)
    name = Column(String)
    color = Column(String, nullable=True)
    duration = Column(Integer)
    order = Column(Integer, default=1)
#     user_id = Column(String, ForeignKey('user.id'))
#
#     user = relationship('User', back_populates='time_block')
