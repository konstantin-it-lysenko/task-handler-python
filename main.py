from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from datetime import datetime
from enum import Enum

app = FastAPI()


class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class TaskBase(BaseModel):
    id: str
    created_at: datetime = datetime.now()
    updated_at: datetime
    name: str
    priority: Priority
    is_completed: bool


