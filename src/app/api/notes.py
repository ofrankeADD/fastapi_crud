from fastapi import APIRouter, HTTPException
from typing import List

from app.api import crud
from app.api.models import NoteDB, NoteSchema

router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(note_payload: NoteSchema):
    note_id = await crud.post(note_payload)

    response_object = {
        "id": note_id,
        "title": note_payload.title,
        "description": note_payload.description
    }
    alternative_response_object = {**note_payload.dict(), "id": note_id}
    
    return response_object


@router.get("/{id}/", response_model=NoteDB)
async def read_one_note(id: int):
    note = await crud.get_one(id)
    
    if not note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found!")
    
    response = {
        "id": id,
        "title": note['title'],
        "description": note['description']
    }
    #response = {**note.dict(), "id": note_id}
    return response


@router.get("/", response_model=List[NoteDB])
async def read_all_notes():
    return await crud.get_all()
    
    #if not note_payload:
    #    raise HTTPException(status_code=404, detail="There are no notes!")
    #
    #response = []
    #for note in note_payload:
    #    response.append({**note_payload.dict()})
    #return response
    

@router.put("/{id}/", response_model=NoteDB)
async def update_note(id: int, note_payload: NoteSchema):
    note = await crud.get_one(id)
    
    if not note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found!")
    
    note_id = await crud.put(id, note_payload)
    #response = {
    #    "id": note_id,
    #    "title": note_payload.title,
    #    "description": note_payload.description
    #}
    response = {**note_payload.dict(), "id": note_id}
 
    return response


@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int):
    note = await crud.get_one(id)
    
    if not note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found!")
    
    return await crud.delete(id)



