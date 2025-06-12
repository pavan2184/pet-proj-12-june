from fastapi import FastAPI, HTTPException
from app.models import PetCreate, Pet
from app import crud

app = FastAPI()

@app.post("/pets", response_model=Pet)
def add_pet(pet: PetCreate):
    return crud.create_pet(pet)

@app.get("/pets", response_model=list[Pet])
def read_pets():
    return crud.get_all_pets()

@app.get("/pets/{pet_id}", response_model=Pet)
def read_pet(pet_id: str):
    pet = crud.get_pet_by_id(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@app.put("/pets/{pet_id}", response_model=Pet)
def update_pet(pet_id: str, pet: PetCreate):
    updated = crud.update_pet(pet_id, pet)
    if not updated:
        raise HTTPException(status_code=404, detail="Pet not found")
    return updated

@app.delete("/pets/{pet_id}")
def remove_pet(pet_id: str):
    deleted = crud.delete_pet(pet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted"}
