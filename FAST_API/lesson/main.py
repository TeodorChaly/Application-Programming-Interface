import random

from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

app = FastAPI()
name = ["John Doe", "Jane Doe", "Alice Doe", "Bob Doe"]
address = ["New York", "London", "Moscow", "Paris"]
ip = ["198.23.123.2", "18.23.12.4", "228.63.163.5", "12.22.223.2"]


@app.get("/")
async def read_root(request: Request):
    return RedirectResponse(f"{request.url}docs")


@app.get("/name")
async def get_random_name():
    return {"name": random.choice(name)}


@app.get("/address")
async def get_random_address():
    return {"address": random.choice(address)}


@app.get("/id")
async def get_random_id():
    return {"ip": random.choice(ip)}


@app.get("/all")
async def get_random_all():
    return {"ip": random.choice(ip), "address": random.choice(address), "name": random.choice(name)}
