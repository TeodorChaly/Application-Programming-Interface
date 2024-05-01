from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager

from database import create_tables, drop_tables


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    print("Starting up")
    yield

    print("Shutting down")

class STaskAdded(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdded):
    id: int


# @app.get("/tasks/")
# def get_home():
#     task = Task(name="Task 1")
#     return {"data": task}

tasks = []
app = FastAPI(lifespan=lifespan)


@app.post("/tasks/")
async def create_task(
        task: Annotated[STaskAdded, Depends()]
):
    tasks.append(task)
    return {"ok": tasks}
