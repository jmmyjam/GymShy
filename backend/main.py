from fastapi import FastAPI
from database import Equipment, equipment

app = FastAPI()

@app.get("/")
async def greet():
    return "Welcome to Gymmy"

@app.get("/allequipment")
async def get_all_equipment():
    return equipment

@app.get("/equipment/{name}")
async def get_equipment_id(name: str):
    for item in equipment:
        if item.name.lower() == name:
            return item
    return "item not found" 

@app.post("/equipment")
async def add_item(item: Equipment):
    idx = len(equipment)
    equipment.append(item)
    item.id = idx + 1
    return equipment