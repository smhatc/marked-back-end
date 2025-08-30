from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from dependencies.get_current_user import get_current_user
from models import UserModel, NoteModel
from serializers.note import NoteSchema, NoteCreateSchema

router = APIRouter()


# Create
@router.post("", response_model=NoteSchema)
def create_note(
    note: NoteCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Create new note
    new_note = NoteModel(**note.model_dump(), owner_id=current_user.id)

    # Save the new note to the database
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# Read All
@router.get("", response_model=List[NoteSchema])
def get_notes(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch all notes for the user
    all_notes = db.query(NoteModel).filter(NoteModel.owner_id == current_user.id).all()

    return all_notes


# Read One
@router.get("/{note_id}", response_model=NoteSchema)
def get_single_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the specific note
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Check ownership
    if note.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this note",
        )

    return note


# Update
@router.put("/{note_id}", response_model=NoteSchema)
def update_note(
    note_id: int,
    note: NoteCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the note to update
    db_note = db.query(NoteModel).filter(NoteModel.id == note_id).first()

    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Check ownership
    if db_note.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to update this note",
        )

    # Update note
    note_data = note.model_dump(exclude_unset=True)
    for key, value in note_data.items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note)

    return db_note


# Delete
@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the note to delete
    db_note = db.query(NoteModel).filter(NoteModel.id == note_id).first()

    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Check ownership
    if db_note.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to delete this note",
        )

    # Delete note
    db.delete(db_note)
    db.commit()

    return {"message": f"Note with ID {note_id} has been deleted"}
