from app.api.models import NoteSchema
from app.db import notes, database


async def post(note_payload: NoteSchema):
    query = notes.insert().values(title=note_payload.title, description=note_payload.description)
    return await database.execute(query=query)
