from fastapi import FastAPI
from database import Equipment

app = FastAPI()

@app.get("/")
async def greet():
    return "Welcome to Gymmy"

equipment = [
    Equipment(id = 1, name = "weights", description = "heavy"),
    Equipment(id = 2, name = "barbell", description = "heavy")
]

@app.get("/equipment")
async def get_all_equipment():
    return equipment

