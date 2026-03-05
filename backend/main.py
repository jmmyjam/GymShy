from fastapi import FastAPI
from database import allequipment, user_equipment

app = FastAPI()

@app.get("/")
async def greet():
    return "Welcome to Gymmy"

@app.get("/allequipment")
async def get_all_equipment():
    return allequipment

@app.get("/equipment/{name}")
async def get_equipment_id(name: str):
    for item in allequipment:
        if item.name.lower() == name.lower().replace(" ", ""):
            return item
    return "item not found"

@app.get("/myequipment")
async def get_user_equipment():
    return user_equipment

@app.post("/myequipment/{name}")
async def add_item(name: str):
    for item in allequipment:
        if item.name.lower() == name.lower().replace(" ", ""):
            if item not in user_equipment:
                user_equipment.append(item)
            return user_equipment
    return "item not found"