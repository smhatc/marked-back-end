from pydantic import BaseModel


# Schema for the user sign up/in request
class UserSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


# Schema for the sign up/in response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str
    message: str
    username: str

    class Config:
        orm_mode = True
