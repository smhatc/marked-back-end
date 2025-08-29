from pydantic import BaseModel


# Schema for user sign up
class UserSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


# Schema for returning user data (without exposing the password)
class UserResponseSchema(BaseModel):
    username: str

    class Config:
        orm_mode = True


# Schema for user sign in (captures username and password during sign in)
class UserSignInSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


# Schema for the sign in response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str
    message: str

    class Config:
        orm_mode = True
