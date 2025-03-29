# from fastapi import FastAPI, HTTPException
from schemas.schema import User, Bot, Registration
from core.models import *

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

@app.post("/prompt")
def create_prompt(prompt: Bot) -> dict:
    historial.append(HumanMessage(content=prompt.prompt))
    response = model.invoke(historial)
    historial.append(AIMessage(content=response.content)),

    return {
        "message": "succesfully created prompt",
        "data" : response.content,
        # "historial": historial[-1].content
        "historial": [i.content for i in historial]
    }

@app.post("/registration")
def registration(user: Registration):
    registration_form = user.model_dump()
    return {
        "message": "User registered successfully",
        "data": {
            "user_name": user.name
        }
    }

