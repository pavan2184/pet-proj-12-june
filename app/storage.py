from models import Pet, PetCreate, PetUpdate
from datetime import datetime
from typing import Dict
import uuid

pets: Dict[str, Pet] = {}

def add_pet(pet_data: PetCreate) -> Pet:
    pet_id = str(uuid.uuid4())
    new_pet = Pet(id=pet_id, created_at=datetime.utcnow(), **pet_data.dict())
    pets[pet_id] = new_pet
    return new_pet

def get_all_pets():
    return list(pets.values())

def get_pet(pet_id: str):
    return pets.get(pet_id)

def update_pet(pet_id: str, pet_data: PetUpdate):
    if pet_id not in pets:
        return None
    updated_pet = pets[pet_id].copy(update=pet_data.dict())
    pets[pet_id] = updated_pet
    return updated_pet

def delete_pet(pet_id: str):
    return pets.pop(pet_id, None) is not None
