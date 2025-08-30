from pydantic import BaseModel, Field
from typing import Optional


class NoteSchema(BaseModel):
    id: int
    title: str
    content: str
    collection_id: Optional[int] = Field(default=None)

    class Config:
        orm_mode = True


class NoteCreateSchema(BaseModel):
    title: str
    content: str
    collection_id: Optional[int] = Field(default=None)
