from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from app.api import ping

app = FastAPI()

app.include_router(ping.router)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World HTTPS on the fly high with postgres!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
def update_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
