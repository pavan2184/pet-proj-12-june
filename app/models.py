from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PetBase(BaseModel):
    name: str = Field(..., example="Fluffy")
    type: str = Field(..., example="Cat")
    age: int = Field(..., ge=0, example=2)

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass

class Pet(PetBase):
    id: str
    created_at: datetime
