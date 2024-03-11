from fastapi import FastAPI
from .models.models import UserCreate

app = FastAPI()

lst = []


@app.post("/create_user")
async def send_feedback(uc: UserCreate):
    lst.append(uc)
    return uc


@app.get("/showuser", response_model=UserCreate)
async def show_users():
    return {"users": lst}
