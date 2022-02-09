from app.api.models import NoteSchema
from app.db import notes, database


#    database.fetch_all(query)
#    database.fetch_one(query)
#    database.iterate(query)
#    database.execute(query)
#    database.execute_many(query)


async def post(note_payload: NoteSchema):
    query = notes.insert().values(title=note_payload.title, description=note_payload.description)
    return await database.execute(query=query)


async def get_one(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)


async def put(id: int, note_payload: NoteSchema):
    query = notes.update().values(title=note_payload.title, description=note_payload.description).where(id == notes.c.id).returning(notes.c.id)
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)

