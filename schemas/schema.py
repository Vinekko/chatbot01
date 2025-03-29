from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

class Bot(BaseModel):
    prompt: str

class Registration(BaseModel):
    name: str
    email: str
    years: int
    city: str