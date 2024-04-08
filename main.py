from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Annotated
from datetime import datetime
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from enum import Enum


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class Priority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class UserBase(BaseModel):
    id: str
    created_at: datetime = datetime.now()
    updated_at: datetime
    email: str
    name: str
    password: str


class TaskBase(BaseModel):
    id: str
    created_at: datetime = datetime.now()
    updated_at: datetime
    name: str
    priority: Optional[Priority]
    is_completed: Optional[bool]


class TimeBlockBase(BaseModel):
    id: str
    created_at: datetime = datetime.now()
    updated_at: datetime
    name: str
    color: Optional[str]
    duration: int
    order: int = 1


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('user/tasks')
async def create_task(task: TaskBase, db: db_dependency):
    db_task = models.Tasks(name=task.name)
    db.add(task)
    db.commit()
    db.refresh(task)

    return task
