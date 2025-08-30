from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from dependencies.get_current_user import get_current_user
from models import UserModel, CollectionModel
from serializers.collection import CollectionSchema, CollectionCreateSchema

router = APIRouter()


# Create
@router.post("", response_model=CollectionSchema)
def create_collection(
    collection: CollectionCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Create new collection
    new_collection = CollectionModel(
        **collection.model_dump(), owner_id=current_user.id
    )

    # Save the new collection to the database
    db.add(new_collection)
    db.commit()
    db.refresh(new_collection)

    return new_collection


# Read All
@router.get("", response_model=List[CollectionSchema])
def get_collections(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch all collections for the user
    all_collections = (
        db.query(CollectionModel)
        .filter(CollectionModel.owner_id == current_user.id)
        .all()
    )

    return all_collections


# Read One
@router.get("/{collection_id}", response_model=CollectionSchema)
def get_single_collection(
    collection_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the specific collection
    collection = (
        db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
    )

    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    # Check ownership
    if collection.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this collection",
        )

    return collection


# Update
@router.put("/{collection_id}", response_model=CollectionSchema)
def update_collection(
    collection_id: int,
    collection: CollectionCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the collection to update
    db_collection = (
        db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
    )

    if not db_collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    # Check ownership
    if db_collection.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to update this collection",
        )

    # Update collection
    collection_data = collection.model_dump(exclude_unset=True)
    for key, value in collection_data.items():
        setattr(db_collection, key, value)

    db.commit()
    db.refresh(db_collection)

    return db_collection


# Delete
@router.delete("/{collection_id}")
def delete_collection(
    collection_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Fetch the collection to delete
    db_collection = (
        db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
    )

    if not db_collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    # Check ownership
    if db_collection.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to delete this collection",
        )

    # Delete collection
    db.delete(db_collection)
    db.commit()

    return {"message": f"Collection with ID {collection_id} has been deleted"}
