from fastapi import FastAPI, Response, Cookie
from datetime import datetime
from .models.models import User

app = FastAPI()

sample_user: dict = {"username": "Vanya", "password": "123esad"}
sessions: dict = {}
fake_db: list[User] = [User(**sample_user)]


@app.post("/login")
async def login(usr: User, response: Response):
    for u in fake_db:
        if u.username == usr.username and u.password == usr.password:
            session_token = "sesstok12"
            sessions[session_token] = usr
            return {"message": "куки установлены"}
    return {"message": "Invalid username or password"}


@app.get('/user')
async def user_info(session_token=Cookie()):
    user = sessions.get(session_token)
    if user:
        return user.dict()
    return {"message": "Unauthorized"}
