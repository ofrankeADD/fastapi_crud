import os
import sqlalchemy as sqla
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = sqla.create_engine(DATABASE_URL)
metadata = sqla.MetaData()
notes = sqla.Table(
    "notes",
    metadata,
    sqla.Column("id", sqla.Integer, primary_key=True),
    sqla.Column("title", sqla.String(50)),
    sqla.Column("description", sqla.String(50)),
    sqla.Column("created_date", sqla.DateTime, default=sqla.sql.func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
