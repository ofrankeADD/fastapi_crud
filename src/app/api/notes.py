from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import NoteDB, NoteSchema

router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(note_payload: NoteSchema):
    note_id = await crud.post(note_payload)

    response_object = {
        "id": note_id,
        "title": note_payload.title,
        "description": note_payload.description,
    }
    alternative_response_object = {**note_payload.dict(), "id": note_id}
    
    return response_object
