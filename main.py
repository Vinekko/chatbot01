from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        "id": 1, 
        "name": "John Doe",
        "email": "test@gmail.com",
        "age": 25,
    },
    {
        "id": 2, 
        "name": "Jane silva",
        "email": "test1@gmail.com",
        "age": 20,
    },
    {
        "id": 3, 
        "name": "John Smith",
        "email": "test2@gmail.com",
        "age": 20,
    },
]

class User(BaseModel):
    name: str
    email: str
    age: int


@app.get("/")
def hello_world():
    return {"Hello": "World"}

# get all users
@app.get("/users")
def get_all_users() -> dict:
    return {
        "message": "succesfully fetched all users",
        "data" : users
    }

@app.get(
    "/users/{user_id}",
    )
def get_user_by_id(user_id: int) -> dict:
    for user in users:
        if user["id"] == user_id:
            return {
                "message": "succesfully fetched user",
                "data" : user
            }
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User) -> dict:
    user_data = user.model_dump()
    return {
        "message": "succesfully created user",
        "data" : user_data
    }

class Bot(BaseModel):
    prompt: str

@app.post("/prompt")
def create_prompt(prompt: Bot) -> dict:
    return {
        "message": "succesfully created prompt",
        "data" : prompt
    }