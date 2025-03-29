from fastapi import FastAPI, HTTPException
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

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

model = ChatCohere()

historial = [
    SystemMessage(content="Eres un chatbot que sabe de programacion y te llamas Ricardo"),
]