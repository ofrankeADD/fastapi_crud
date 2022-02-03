from pydantic import BaseModel
from typing import Optional


class NoteSchema(BaseModel):
    title: str
    description: str


class NoteDB(NoteSchema):
    id: int


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
