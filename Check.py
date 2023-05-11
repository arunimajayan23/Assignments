from fastapi import FastAPI
from pydantic import BaseModel


class Calc(BaseModel):
    num1: float
    num2: float


app = FastAPI()


@app.post("/add")
async def add(nums: Calc):
    return {"result": nums.dict()['num1'] + nums.dict()['num2']}


@app.post('/subtract')
async def subtract(nums: Calc):
    return {"result": nums.dict()['num1'] - nums.dict()['num2']}


@app.post("/multiply")
async def multiply(nums: Calc):
    return {"result": nums.dict()['num1'] * nums.dict()['num2']}


@app.post("/divide")
async def divide(nums: Calc):
    if nums == 0:
        return {"error": "division by zero"}
    else:
        return {"result": nums.dict()['num1'] / nums.dict()['num2']}
