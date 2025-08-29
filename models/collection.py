from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class CollectionModel(BaseModel):

    __tablename__ = "collections"  # Table name in the SQL database

    # Data columns specific to this table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Foreign key linking to the user
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships with other tables
    user = relationship("UserModel", back_populates="collections")
    notes = relationship("NoteModel", back_populates="collection")
