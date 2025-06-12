from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class Pet(BaseModel):
    id: str
    name: str
    type: str
    age: int
    created_at: datetime

class PetCreate(BaseModel):
    name: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    age: int = Field(..., ge=0)
