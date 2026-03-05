from fastapi import FastAPI

app = FastAPI()


@app.get("/equipment/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}