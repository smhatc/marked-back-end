from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str  # User's unique name
    password: str  # Plain text password for user sign up (will be hashed before saving)

    class Config:
        orm_mode = True  # Enables compatibility with ORM models


# Schema for returning user data (without exposing the password)
class UserResponseSchema(BaseModel):
    username: str

    class Config:
        orm_mode = True


# Schema for user sign in (captures username and password during sign in)
class UserSignInSchema(BaseModel):
    username: str  # Username provided by the user during sign in
    password: str  # Plain text password provided by the user during sign in


# Schema for the response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str  # JWT token generated upon successful sign in
    message: str  # Success message

    class Config:
        orm_mode = True
