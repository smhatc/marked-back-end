from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class NoteModel(BaseModel):

    __tablename__ = "notes"  # Table name in the SQL database

    # Data columns specific to this table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    # Foreign key linking to the user
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Foreign key linking to the collection (if any)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=True)

    # Relationships with other tables
    user = relationship("UserModel", back_populates="notes")
    collection = relationship("CollectionModel", back_populates="notes")
