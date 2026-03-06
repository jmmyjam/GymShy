from fastapi import FastAPI
from database import Equipment, allequipment, user_equipment

app = FastAPI()

@app.get("/")
async def greet():
    return {
            "message": "Welcome to Gymmy"
            }

@app.get("/allequipment")
async def get_all_equipment():
    return allequipment

@app.get("/equipment/{name}")
async def get_equipment_id(name: str):
    for item in allequipment:
        if item.name.lower() == name.lower().replace(" ", ""):
            return item
    return {
            "message": "Not found"
            }

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
    return {
            "message": "Not found"
            }

@app.put("/allequipment")
async def update(name: str, item: Equipment):
    for i in range(len(allequipment)):
        if allequipment[i].name.lower().replace(" ", "") == name.lower().replace(" ", ""):
            allequipment[i] = item
            return {
                    "message": "Item updated successfully",
                    "update": allequipment[i]
                    }
    return {
            "message": "Not found"
            }

@app.delete("/myequipment")
async def delete(name: str):
    if len(user_equipment) == 0:
        return "Empty list nothing deleted"
    for i in range(len(user_equipment)):
        if user_equipment[i].name.lower().replace(" ", "") == name.lower().replace(" ", ""):
            deleted: Equipment = user_equipment.pop(i)
            return {
                    "message": "Item deleted successfully",
                    "deleted": deleted
                    }
    return {
            "message": "Not found"
            }