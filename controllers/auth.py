from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from serializers.user import (
    UserSchema,
    UserTokenSchema,
)
from database import get_db

router = APIRouter()


@router.post("/sign-up", response_model=UserTokenSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = (
        db.query(UserModel).filter(UserModel.username == user.username).first()
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = UserModel(username=user.username)
    # Use the set_password method to hash the password
    new_user.set_password(user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate JWT token
    token = new_user.generate_token()

    # Return token and a success message
    return {
        "token": token,
        "message": "Sign up successful",
        "username": new_user.username,
    }


@router.post("/sign-in", response_model=UserTokenSchema)
def sign_in(user: UserSchema, db: Session = Depends(get_db)):

    # Find the user by username
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    # Check if the user exists and if the password is correct
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    token = db_user.generate_token()

    # Return token and a success message
    return {
        "token": token,
        "message": "Sign in successful",
        "username": db_user.username,
    }
