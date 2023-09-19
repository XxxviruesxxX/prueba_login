from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    username: str
    password: str

class UserLogin(UserCreate):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Cambia 'orm_mode' a 'from_attributes'
