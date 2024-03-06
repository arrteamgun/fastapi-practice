from fastapi import FastAPI
from fastapi import responses

app = FastAPI()


@app.get("/")
async def root():
    return responses.FileResponse('index.html')


@app.post('/calculate')
def calculate(num1: int, num2: int):
    return responses.JSONResponse({"result": num1 + num2})
