from app.models import Pet, PetCreate
from app.storage import pets
from datetime import datetime
import uuid

def create_pet(pet_data: PetCreate) -> Pet:
    pet_id = str(uuid.uuid4())
    new_pet = Pet(id=pet_id, created_at=datetime.utcnow(), **pet_data.dict())
    pets[pet_id] = new_pet
    return new_pet

def get_all_pets():
    return list(pets.values())

def get_pet_by_id(pet_id: str):
    return pets.get(pet_id)

def update_pet(pet_id: str, pet_data: PetCreate):
    if pet_id in pets:
        updated_pet = Pet(id=pet_id, created_at=pets[pet_id].created_at, **pet_data.dict())
        pets[pet_id] = updated_pet
        return updated_pet
    return None

def delete_pet(pet_id: str):
    return pets.pop(pet_id, None)
