from fastapi import FastAPI, Request, Response, Header
from typing import Annotated

from .models.models import User

from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.get("/")
def root(response: Response):
    user_agent = response.headers.get('user-agent')
    accept_language = response.headers.get('accept-language')
    if not user_agent or not accept_language:
        raise HTTPException(status_code=400, detail="Missed Header")
    return {"User-Agent": user_agent, "Accept-Language": accept_language}
