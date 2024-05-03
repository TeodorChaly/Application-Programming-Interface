from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import create_tables, drop_tables
from .router import router as task_router


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    print("Starting up")
    yield

    print("Shutting down")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
