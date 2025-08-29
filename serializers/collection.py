from pydantic import BaseModel
from typing import List
from .note import NoteSchema


class CollectionSchema(BaseModel):
    id: int
    name: str

    # Relationships
    notes: List[NoteSchema] = []

    class Config:
        orm_mode = True


class CollectionCreateSchema(BaseModel):
    name: str
