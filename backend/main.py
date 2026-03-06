from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Equipment, allequipment
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from sqlalchemy import func

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database_models.Base.metadata.create_all(bind = engine)

def get_database():
    database = session()
    try:
        yield database
    finally:
        database.close()

def init_database():
    database = session()
    count = database.query(database_models.Equipment).count()
    if count != len(allequipment):
        database.query(database_models.UserEquipment).delete()
        database.query(database_models.Equipment).delete()
        for item in allequipment:
            database.add(database_models.Equipment(**item.model_dump()))
        database.commit()

init_database()

@app.get("/")
async def greet():
    return {
            "message": "Welcome to Gymmy"
            }

@app.get("/allequipment")
async def get_all_equipment(database: Session = Depends(get_database)):
    database_equipment = database.query(database_models.Equipment).all()
    return database_equipment

@app.get("/equipment/{name}")
async def get_equipment(name: str, database: Session = Depends(get_database)):
    database_item = database.query(database_models.Equipment).filter(func.lower(func.replace(database_models.Equipment.name, " ", "")) == name.lower().replace(" ", "")).first()
    if database_item:
            return database_item
    else: 
        return {
                "message": "Not found"
                }

@app.get("/myequipment")
async def get_user_equipment(database: Session = Depends(get_database)):
    rows = database.query(database_models.UserEquipment).all()
    equipment_ids = [row.equipment_id for row in rows]
    return database.query(database_models.Equipment).filter(database_models.Equipment.id.in_(equipment_ids)).all()

@app.post("/myequipment/{name}")
async def add_item(name: str, database: Session = Depends(get_database)):
    item = database.query(database_models.Equipment).filter(func.lower(func.replace(database_models.Equipment.name, " ", "")) == name.lower().replace(" ", "")).first()
    if not item:
        return {
                "message": "Not found"
                }
    existing = database.query(database_models.UserEquipment).filter(database_models.UserEquipment.equipment_id == item.id).first()
    if not existing:
        database.add(database_models.UserEquipment(equipment_id=item.id))
        database.commit()
    rows = database.query(database_models.UserEquipment).all()
    equipment_ids = [row.equipment_id for row in rows]
    return database.query(database_models.Equipment).filter(database_models.Equipment.id.in_(equipment_ids)).all()

@app.put("/allequipment")
async def update(name: str, item: Equipment, database: Session = Depends(get_database)):
    database_item = database.query(database_models.Equipment).filter(func.lower(func.replace(database_models.Equipment.name, " ", "")) == name.lower().replace(" ", "")).first()
    if not database_item:
        return {
                "message": "Not found"
                }
    database_item.type = item.type
    database_item.name = item.name
    database_item.description = item.description
    database.commit()
    database.refresh(database_item)
    return {
            "message": "Item updated successfully",
            "update": database_item
            }

@app.delete("/myequipment")
async def delete(name: str, database: Session = Depends(get_database)):
    database_item = database.query(database_models.Equipment).filter(func.lower(func.replace(database_models.Equipment.name, " ", "")) == name.lower().replace(" ", "")).first()
    if not database_item:
        return {"message": "Not found"}
    row = database.query(database_models.UserEquipment).filter(database_models.UserEquipment.equipment_id == database_item.id).first()
    if not row:
        return {
                "message": "Not found in your equipment"
                }
    database.delete(row)
    database.commit()
    database.refresh(database_item)
    return {
            "message": "Item deleted successfully",
            "deleted": database_item
            }