from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Annotated
from datetime import datetime
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from enum import Enum
import uuid


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
    name: str
    priority: Optional[Priority]


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


@app.get('user/tasks')
async def get_tasks(db: db_dependency):
    tasks = db.query(models.Tasks)

    return tasks


@app.put('/user/tasks/{task_id}')
async def update_task(task_id: int, db: db_dependency):
    result = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Task was not found')

    return result


@app.post('/user/tasks')
async def create_task(task: TaskBase, db: db_dependency):
    task_id = str(uuid.uuid4())

    db_task = models.Tasks(id=task_id, name=task.name, priority=task.priority)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task
